# -*- coding: utf-8 -*-
"""Verify a clean 準2級 2026-1 main build against audited data.json."""
import json
import os
import shutil
import subprocess
import sys
import tempfile

sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE, "data", "grade-pre2", "2026-1", "data.json")
GENERATORS = [
    "gen_pre2_2026-1_reading.py",
    "gen_pre2_2026-1_main_section1.py",
    "gen_pre2_2026-1_main_section2.py",
    "gen_pre2_2026-1_main_section3.py",
    "gen_pre2_2026-1_main_section4.py",
    "gen_pre2_2026-1_vocab.py",
    "gen_pre2_2026-1_main_lessonplan.py",
]


def without_audio(value):
    if isinstance(value, dict):
        return {
            key: without_audio(item)
            for key, item in value.items()
            if "audio" not in key.lower()
        }
    if isinstance(value, list):
        return [without_audio(item) for item in value]
    return value


with open(DATA_PATH, encoding="utf-8") as handle:
    expected = without_audio(json.load(handle))

with tempfile.TemporaryDirectory(prefix="readpass-pre2-main-sync-") as temp_dir:
    out_dir = os.path.join(temp_dir, "data", "grade-pre2", "2026-1")
    os.makedirs(out_dir)
    for name in GENERATORS:
        shutil.copy2(os.path.join(BASE, name), os.path.join(temp_dir, name))

    env = os.environ.copy()
    env["PYTHONUTF8"] = "1"
    for name in GENERATORS:
        completed = subprocess.run(
            [sys.executable, name],
            cwd=temp_dir,
            env=env,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        if completed.returncode:
            print(completed.stdout)
            print(completed.stderr, file=sys.stderr)
            raise SystemExit(completed.returncode)

    with open(os.path.join(out_dir, "data.json"), encoding="utf-8") as handle:
        actual = without_audio(json.load(handle))

if actual != expected:
    print("ERROR: clean generator output differs from audited data.json")
    raise SystemExit(1)

print("OK: clean generator output matches all audited non-audio fields")

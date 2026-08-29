# -*- coding: utf-8 -*-
"""Verify two clean main-venue generator runs against audited Grade 2 data."""
import json
import os
import shutil
import subprocess
import sys
import tempfile

sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE, "data", "grade2", "2026-1", "data.json")
GENERATORS = [
    "gen_g2_2026-1_reading.py",
    "gen_g2_2026-1_section1.py",
    "gen_g2_2026-1_section2.py",
    "gen_g2_2026-1_section3.py",
    "gen_g2_2026-1_vocab.py",
    "gen_g2_2026-1_lessonplan.py",
]


def run_generators(temp_dir):
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


with open(DATA_PATH, encoding="utf-8") as handle:
    expected = json.load(handle)

with tempfile.TemporaryDirectory(prefix="readpass-g2-main-sync-") as temp_dir:
    out_dir = os.path.join(temp_dir, "data", "grade2", "2026-1")
    os.makedirs(out_dir)
    for name in GENERATORS:
        shutil.copy2(os.path.join(BASE, name), os.path.join(temp_dir, name))

    run_generators(temp_dir)
    generated_path = os.path.join(out_dir, "data.json")
    with open(generated_path, encoding="utf-8") as handle:
        first = json.load(handle)

    run_generators(temp_dir)
    with open(generated_path, encoding="utf-8") as handle:
        second = json.load(handle)

if first != second:
    print("ERROR: second clean generator run is not idempotent")
    raise SystemExit(1)
if second != expected:
    print("ERROR: clean generator output differs from audited data.json")
    raise SystemExit(1)

print("OK: two clean main-venue generator runs match audited data.json")

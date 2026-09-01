# -*- coding: utf-8 -*-
"""Verify two clean Pre-1 2026-1 generator runs match committed data.json."""

import json
import os
import shutil
import subprocess
import sys
import tempfile


sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE, "data", "pre-grade1", "2026-1", "data.json")
GENERATORS = [
    "gen_pre1_2026-1.py",
    "gen_pre1_2026-1_section1.py",
    "gen_pre1_2026-1_section2.py",
    "gen_pre1_2026-1_section3.py",
    "gen_pre1_2026-1_vocab.py",
    "gen_pre1_2026-1_lessonplan.py",
]


def run_generators(directory):
    environment = os.environ.copy()
    environment["PYTHONUTF8"] = "1"
    for filename in GENERATORS:
        completed = subprocess.run(
            [sys.executable, filename],
            cwd=directory,
            env=environment,
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

with tempfile.TemporaryDirectory(prefix="readpass-pre1-2026-sync-") as directory:
    out_dir = os.path.join(directory, "data", "pre-grade1", "2026-1")
    os.makedirs(out_dir)
    for filename in GENERATORS:
        shutil.copy2(os.path.join(BASE, filename), os.path.join(directory, filename))

    run_generators(directory)
    generated_path = os.path.join(out_dir, "data.json")
    with open(generated_path, encoding="utf-8") as handle:
        first = json.load(handle)

    run_generators(directory)
    with open(generated_path, encoding="utf-8") as handle:
        second = json.load(handle)

if first != second:
    raise SystemExit("second clean generator run is not idempotent")
if second != expected:
    raise SystemExit("clean generator output differs from data.json")

print("OK: two clean Pre-1 2026-1 generator runs match data.json")

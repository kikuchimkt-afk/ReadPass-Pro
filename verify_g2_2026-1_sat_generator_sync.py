# -*- coding: utf-8 -*-
"""2026-1-sat 2級を空ディレクトリから生成し、登録JSONと完全比較する。"""
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "grade2" / "2026-1-sat" / "data.json"
GENERATORS = [
    "gen_g2_2026-1.py",
    "gen_g2_2026-1_sections.py",
    "gen_g2_2026-1_sat_enrichment.py",
    "gen_g2_2026-1_sat_lessonplan.py",
]

expected_bytes = DATA.read_bytes()
expected = json.loads(expected_bytes.decode("utf-8"))


def first_difference(left, right, path="root"):
    if type(left) is not type(right):
        return f"{path}: type {type(left).__name__} != {type(right).__name__}"
    if isinstance(left, dict):
        if left.keys() != right.keys():
            missing = [key for key in left if key not in right]
            extra = [key for key in right if key not in left]
            return f"{path}: keys differ missing={missing} extra={extra}"
        for key in left:
            difference = first_difference(left[key], right[key], f"{path}.{key}")
            if difference:
                return difference
        return None
    if isinstance(left, list):
        if len(left) != len(right):
            return f"{path}: length {len(left)} != {len(right)}"
        for index, (left_item, right_item) in enumerate(zip(left, right)):
            difference = first_difference(left_item, right_item, f"{path}[{index}]")
            if difference:
                return difference
        return None
    if left != right:
        return f"{path}: {left!r} != {right!r}"
    return None

with tempfile.TemporaryDirectory(prefix="readpass-g2-sat-sync-") as temp:
    temp_root = Path(temp)
    output = temp_root / "data" / "grade2" / "2026-1-sat"
    output.mkdir(parents=True)
    for name in GENERATORS:
        shutil.copy2(ROOT / name, temp_root / name)

    env = os.environ.copy()
    env.pop("PYTHONUTF8", None)
    for name in GENERATORS:
        completed = subprocess.run(
            [sys.executable, name], cwd=temp_root, env=env,
            capture_output=True, text=True, encoding="utf-8",
        )
        if completed.returncode:
            print(completed.stdout)
            print(completed.stderr, file=sys.stderr)
            raise SystemExit(completed.returncode)

    actual_bytes = (output / "data.json").read_bytes()
    actual = json.loads(actual_bytes.decode("utf-8"))

if actual != expected:
    raise SystemExit(
        "ERROR: clean generator output differs from audited data.json: "
        + (first_difference(expected, actual) or "unknown difference")
    )

digest = hashlib.sha256(actual_bytes).hexdigest().upper()
print(f"OK: clean generator output matches audited data.json SHA256={digest}")

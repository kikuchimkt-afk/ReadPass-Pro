# -*- coding: utf-8 -*-
"""Verify 2026-1 grade5（本会場）vocabulary."""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade5", "2026-1",
)
DATA = os.path.join(BASE, "data.json")

d = json.load(open(DATA, encoding="utf-8"))
errors = []
vocab = d.get("vocabulary", [])

if len(vocab) != 20:
    errors.append(f"vocab count {len(vocab)} != 20")

for i, v in enumerate(vocab):
    for key in ("word", "meaning", "pos", "level", "example", "distractors"):
        if not v.get(key):
            errors.append(f"vocab[{i}] missing {key}")
    if len(v.get("distractors", [])) != 3:
        errors.append(f"vocab {v.get('word')}: distractors != 3")
    rel = v.get("wordAudio", "")
    expected = f"audio/vocab/w_{i + 1:03d}_"
    if rel and not rel.startswith(expected):
        errors.append(f"vocab {v['word']}: wordAudio {rel}")

print(f"errors={len(errors)}")
for e in errors:
    print(" ", e)
sys.exit(1 if errors else 0)

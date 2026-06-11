# -*- coding: utf-8 -*-
"""Verify 2026-1-sat grade5 vocabulary structure."""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade5", "2026-1-sat",
)
DATA = os.path.join(BASE, "data.json")

d = json.load(open(DATA, encoding="utf-8"))
errors = []
vocab = d.get("vocabulary", [])

if len(vocab) != 20:
    errors.append(f"vocabulary count {len(vocab)} != 20")

meanings = []
for i, v in enumerate(vocab):
    for key in ("word", "meaning", "pos", "level", "example", "distractors"):
        if not v.get(key):
            errors.append(f"vocab[{i}]: missing {key}")
    if len(v.get("distractors", [])) != 3:
        errors.append(f"{v.get('word')}: distractors != 3")
    m = v.get("meaning", "")
    if m in meanings:
        errors.append(f"duplicate meaning: {m}")
    meanings.append(m)
    if m in v.get("distractors", []):
        errors.append(f"{v['word']}: distractors contain correct meaning")
    for rel in (v.get("wordAudio"), v.get("exampleAudio")):
        if rel:
            fp = os.path.join(BASE, rel.replace("/", os.sep))
            if not os.path.isfile(fp) or os.path.getsize(fp) < 500:
                errors.append(f"{v['word']}: missing audio {rel}")

print(f"vocabulary={len(vocab)} errors={len(errors)}")
for e in errors:
    print(" ", e)
if errors:
    sys.exit(1)
print("OK: 20 vocabulary items verified")

# -*- coding: utf-8 -*-
"""2026-1-sat 3級 vocabulary 検証"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade3", "2026-1-sat",
)
DATA = os.path.join(BASE, "data.json")

d = json.load(open(DATA, encoding="utf-8"))
errors = []
vocab = d.get("vocabulary", [])

if len(vocab) != 30:
    errors.append(f"vocabulary count {len(vocab)} != 30")

meanings = []
for i, v in enumerate(vocab):
    for key in ("word", "meaning", "pos", "level", "example", "distractors", "wordAudio"):
        if key not in v:
            errors.append(f"vocab[{i + 1}] missing {key}")
    if len(v.get("distractors", [])) != 3:
        errors.append(f"vocab[{i + 1}] distractors != 3")
    if v.get("level") != "3級":
        errors.append(f"vocab[{i + 1}] level != 3級")
    m = v.get("meaning", "")
    if m in meanings:
        errors.append(f"duplicate meaning: {m}")
    meanings.append(m)
    audio = v.get("wordAudio", "")
    if audio:
        path = os.path.join(BASE, audio.replace("/", os.sep))
        if not os.path.isfile(path):
            errors.append(f"vocab[{i + 1}] missing audio: {audio}")
    else:
        errors.append(f"vocab[{i + 1}] no wordAudio")

print(f"errors={len(errors)}")
for e in errors:
    print(" ", e)
if errors:
    sys.exit(1)
print("OK: 30 vocabulary items with audio")

# -*- coding: utf-8 -*-
"""2026-1 準2級プラス（本会場）vocabulary 検証"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade-pre2plus", "2026-1",
)
DATA = os.path.join(BASE, "data.json")

d = json.load(open(DATA, encoding="utf-8"))
errors = []
vocab = d.get("vocabulary", [])

EXPECTED = 55
if len(vocab) != EXPECTED:
    errors.append(f"vocabulary count {len(vocab)} != {EXPECTED}")

meanings = []
sources = {"大問1": 0, "大問2A": 0, "大問2B": 0, "大問3A": 0, "大問3B": 0}
for i, v in enumerate(vocab):
    for key in ("word", "meaning", "pos", "level", "example", "distractors", "source"):
        if not v.get(key):
            errors.append(f"vocab[{i}]: missing {key}")
    if len(v.get("distractors", [])) != 3:
        errors.append(f"{v.get('word')}: distractors != 3")
    m = v.get("meaning", "")
    if m in meanings:
        errors.append(f"duplicate meaning: {m} ({v.get('word')})")
    meanings.append(m)
    if m in v.get("distractors", []):
        errors.append(f"{v['word']}: distractors contain correct meaning")
    src = v.get("source", "")
    if src in sources:
        sources[src] += 1
    wa = v.get("wordAudio")
    if wa:
        fp = os.path.join(BASE, wa.replace("/", os.sep))
        if not os.path.isfile(fp) or os.path.getsize(fp) < 500:
            errors.append(f"{v['word']}: missing audio {wa}")

expected_sources = {"大問1": 17, "大問2A": 9, "大問2B": 10, "大問3A": 6, "大問3B": 13}
for src, count in expected_sources.items():
    if sources.get(src, 0) != count:
        errors.append(f"{src}: {sources.get(src, 0)} words != {count}")

print(f"vocabulary={len(vocab)} errors={len(errors)}")
for e in errors:
    print(" ", e)
if errors:
    sys.exit(1)
print(f"OK: {EXPECTED} vocabulary items verified")

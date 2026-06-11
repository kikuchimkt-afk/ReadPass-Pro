# -*- coding: utf-8 -*-
"""Verify 2026-1 grade5（本会場）section2."""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade5", "2026-1", "data.json",
)
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "grade5", "2026-1")

EXPECTED = {16: 1, 17: 2, 18: 1, 19: 1, 20: 1}
KEYS = ("grammar", "grammarSimple", "translation", "choiceTranslations",
        "choiceAnalysis", "choiceAnalysisSimple", "questionAudio")

d = json.load(open(DATA, encoding="utf-8"))
errors = []
sec = next(s for s in d["sections"] if s["name"] == "大問2")

for q in sec["questions"]:
    n = q["number"]
    if q["answer"] != EXPECTED[n]:
        errors.append(f"Q{n}: answer {q['answer']} != {EXPECTED[n]}")
    for key in KEYS:
        if not q.get(key):
            errors.append(f"Q{n}: missing {key}")

print(f"errors={len(errors)}")
for e in errors:
    print(" ", e)
sys.exit(1 if errors else 0)

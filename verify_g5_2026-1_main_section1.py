# -*- coding: utf-8 -*-
"""Verify 2026-1 grade5（本会場）section1."""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade5", "2026-1", "data.json",
)
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "grade5", "2026-1")

EXPECTED = {
    1: 3, 2: 4, 3: 4, 4: 2, 5: 4, 6: 4, 7: 2, 8: 2, 9: 4, 10: 1,
    11: 1, 12: 4, 13: 1, 14: 4, 15: 1,
}
KEYS = ("grammar", "grammarSimple", "translation", "choiceTranslations",
        "choiceAnalysis", "choiceAnalysisSimple", "questionAudio")

d = json.load(open(DATA, encoding="utf-8"))
errors = []
sec = next(s for s in d["sections"] if s["name"] == "大問1")

for q in sec["questions"]:
    n = q["number"]
    if q["answer"] != EXPECTED[n]:
        errors.append(f"Q{n}: answer {q['answer']} != {EXPECTED[n]}")
    for key in KEYS:
        if not q.get(key):
            errors.append(f"Q{n}: missing {key}")
    ca = q.get("choiceAnalysis", [])
    if [i + 1 for i, t in enumerate(ca) if t.lstrip().startswith("✅")] != [q["answer"]]:
        errors.append(f"Q{n}: ✅ mark mismatch")
    qa = q.get("questionAudio")
    if qa:
        fp = os.path.join(BASE, qa.replace("/", os.sep))
        if not os.path.isfile(fp) or os.path.getsize(fp) < 500:
            errors.append(f"Q{n}: audio missing")

print(f"errors={len(errors)}")
for e in errors:
    print(" ", e)
sys.exit(1 if errors else 0)

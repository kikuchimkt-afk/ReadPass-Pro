# -*- coding: utf-8 -*-
"""Verify 2026-1 準2級プラス（本会場）section2 structure and answers."""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade-pre2plus", "2026-1", "data.json",
)

EXPECTED = {18: 2, 19: 4, 20: 3, 21: 1, 22: 2, 23: 4}

with open(DATA_PATH, encoding="utf-8") as f:
    d = json.load(f)

errors = []
sec = d["sections"][1]
assert sec["type"] == "passage-fill"

for pa in sec["passages"]:
    for key in ("label", "title", "paragraphs", "translations"):
        if key not in pa or not pa[key]:
            errors.append(f"passage {pa.get('label')}: missing {key}")
    if len(pa["paragraphs"]) != len(pa["translations"]):
        errors.append(f"passage {pa.get('label')}: paragraphs/translations length mismatch")

all_qs = [q for pa in sec["passages"] for q in pa["questions"]]
for q in all_qs:
    n = q["number"]
    if q["answer"] != EXPECTED[n]:
        errors.append(f"Q{n}: answer {q['answer']} != expected {EXPECTED[n]}")
    for key in ("choices", "choiceTranslations", "choiceAnalysis"):
        if key not in q or len(q[key]) != 4:
            errors.append(f"Q{n}: bad {key}")
    if "grammar" not in q or not q["grammar"]:
        errors.append(f"Q{n}: missing grammar")

print(f"section2 questions={len(all_qs)} errors={len(errors)}")
for e in errors:
    print(" ", e)
if errors:
    sys.exit(1)
print("OK: section2 verified")

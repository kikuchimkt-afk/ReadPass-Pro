# -*- coding: utf-8 -*-
"""Verify 2026-1 準2級プラス（本会場）section3 structure and answers."""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade-pre2plus", "2026-1", "data.json",
)

EXPECTED = {24: 3, 25: 2, 26: 3, 27: 1, 28: 4, 29: 3, 30: 4, 31: 2}

with open(DATA_PATH, encoding="utf-8") as f:
    d = json.load(f)

errors = []
sec = d["sections"][2]
assert sec["type"] == "reading-comprehension"

for pa in sec["passages"]:
    for key in ("label", "title", "paragraphs", "translations"):
        if key not in pa or not pa[key]:
            errors.append(f"passage {pa.get('label')}: missing {key}")
    if len(pa["paragraphs"]) != len(pa["translations"]):
        errors.append(f"passage {pa.get('label')}: paragraphs/translations length mismatch")
    if pa.get("label") == "A" and pa.get("format") != "email":
        errors.append("passage A: expected format=email")

all_qs = [q for pa in sec["passages"] for q in pa["questions"]]
for q in all_qs:
    n = q["number"]
    if q["answer"] != EXPECTED[n]:
        errors.append(f"Q{n}: answer {q['answer']} != expected {EXPECTED[n]}")
    for key in ("question", "questionTranslation", "choices", "choiceTranslations", "choiceAnalysis"):
        if key in ("choices", "choiceTranslations", "choiceAnalysis"):
            if key not in q or len(q[key]) != 4:
                errors.append(f"Q{n}: bad {key}")
        elif key not in q or not q[key]:
            errors.append(f"Q{n}: missing {key}")
    if "grammar" not in q or not q["grammar"]:
        errors.append(f"Q{n}: missing grammar")
    if "sourceEvidence" not in q or not q["sourceEvidence"]:
        errors.append(f"Q{n}: missing sourceEvidence")

print(f"section3 questions={len(all_qs)} errors={len(errors)}")
for e in errors:
    print(" ", e)
if errors:
    sys.exit(1)
print("OK: section3 verified")

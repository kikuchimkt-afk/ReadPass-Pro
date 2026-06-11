# -*- coding: utf-8 -*-
"""Verify 2026-1-sat grade5 section1 structure and answers."""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade5", "2026-1-sat", "data.json",
)

EXPECTED = {
    1: 2, 2: 1, 3: 1, 4: 2, 5: 3, 6: 4, 7: 2, 8: 3, 9: 1, 10: 1,
    11: 3, 12: 1, 13: 3, 14: 3, 15: 3,
}

REQUIRED_KEYS = (
    "text", "translation", "choices", "choiceTranslations",
    "choiceAnalysis", "choiceAnalysisSimple", "grammar", "grammarSimple",
    "questionAudio",
)

with open(DATA_PATH, encoding="utf-8") as f:
    d = json.load(f)

errors = []
sec = d["sections"][0]
if sec.get("name") != "大問1":
    errors.append(f"sections[0] is {sec.get('name')}, expected 大問1")

qs = sec["questions"]
if len(qs) != 15:
    errors.append(f"question count {len(qs)} != 15")

for q in qs:
    n = q["number"]
    if q["answer"] != EXPECTED[n]:
        errors.append(f"Q{n}: answer {q['answer']} != expected {EXPECTED[n]}")
    for key in REQUIRED_KEYS:
        if key not in q or not q[key]:
            errors.append(f"Q{n}: missing {key}")
    if len(q["choices"]) != 4:
        errors.append(f"Q{n}: choices count {len(q['choices'])}")
    if len(q["choiceAnalysis"]) != 4:
        errors.append(f"Q{n}: choiceAnalysis count {len(q['choiceAnalysis'])}")
    if len(q["choiceAnalysisSimple"]) != 4:
        errors.append(f"Q{n}: choiceAnalysisSimple count {len(q['choiceAnalysisSimple'])}")
    for i, ca in enumerate(q["choiceAnalysis"]):
        if i + 1 == q["answer"]:
            if not ca.startswith("○"):
                errors.append(f"Q{n}: correct choice {i + 1} missing ○")
        elif ca.startswith("○"):
            errors.append(f"Q{n}: wrong choice {i + 1} has ○")

print(f"questions={len(qs)} errors={len(errors)}")
for e in errors:
    print(" ", e)
if errors:
    sys.exit(1)
print("OK: section1 rich data verified")

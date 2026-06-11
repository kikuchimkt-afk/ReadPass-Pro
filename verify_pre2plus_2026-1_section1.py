# -*- coding: utf-8 -*-
"""Verify 2026-1-sat pre2plus section1 structure and answers."""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade-pre2plus", "2026-1-sat", "data.json",
)

EXPECTED = {
    1: 2, 2: 2, 3: 4, 4: 4, 5: 3, 6: 1, 7: 2,
    8: 2, 9: 4, 10: 3, 11: 4, 12: 2, 13: 2, 14: 4,
    15: 4, 16: 3, 17: 3,
}

with open(DATA_PATH, encoding="utf-8") as f:
    d = json.load(f)

errors = []
assert len(d["sections"]) >= 1, f"expected >=1 sections, got {len(d['sections'])}"
sec = d["sections"][0]
qs = sec["questions"]

for q in qs:
    n = q["number"]
    if q["answer"] != EXPECTED[n]:
        errors.append(f"Q{n}: answer {q['answer']} != expected {EXPECTED[n]}")
    for key in ("text", "translation", "choices", "choiceTranslations", "choiceAnalysis", "grammar"):
        if key not in q or not q[key]:
            errors.append(f"Q{n}: missing {key}")
    if len(q["choices"]) != 4:
        errors.append(f"Q{n}: choices count {len(q['choices'])}")
    if len(q["choiceAnalysis"]) != 4:
        errors.append(f"Q{n}: choiceAnalysis count {len(q['choiceAnalysis'])}")
    for i, ca in enumerate(q["choiceAnalysis"]):
        if i + 1 == q["answer"]:
            if not ca.startswith("✅"):
                errors.append(f"Q{n}: correct choice {i+1} missing ✅")
        else:
            if not ca.startswith("❌"):
                errors.append(f"Q{n}: wrong choice {i+1} missing ❌")

print(f"sections={len(d['sections'])} questions={len(qs)} errors={len(errors)}")
for e in errors:
    print(" ", e)
if errors:
    sys.exit(1)

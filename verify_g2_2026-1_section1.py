# -*- coding: utf-8 -*-
"""Verify 2026-1 grade2 (本会場) section1 structure and answers."""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade2", "2026-1", "data.json",
)

EXPECTED = {
    1: 4, 2: 2, 3: 3, 4: 1, 5: 2, 6: 3, 7: 4, 8: 3, 9: 3, 10: 1,
    11: 4, 12: 4, 13: 2, 14: 1, 15: 1, 16: 1, 17: 2,
}

with open(DATA_PATH, encoding="utf-8") as f:
    d = json.load(f)

errors = []
if not d.get("sections"):
    errors.append("no sections")
    print(f"errors={len(errors)}")
    for e in errors:
        print(" ", e)
    sys.exit(1)

sec = d["sections"][0]
if sec.get("name") != "大問1":
    errors.append(f"sections[0] is {sec.get('name')}, expected 大問1")

qs = sec["questions"]
if len(qs) != 17:
    errors.append(f"question count {len(qs)} != 17")

for q in qs:
    n = q["number"]
    if q["answer"] != EXPECTED[n]:
        errors.append(f"Q{n}: answer {q['answer']} != expected {EXPECTED[n]}")
    for key in ("text", "translation", "choices", "choiceTranslations", "choiceAnalysis", "grammar"):
        if key not in q or not q[key]:
            errors.append(f"Q{n}: missing {key}")
    if len(q["choices"]) != 4:
        errors.append(f"Q{n}: choices count {len(q['choices'])}")
    if len(q.get("choiceTranslations", [])) != 4:
        errors.append(f"Q{n}: choiceTranslations count != 4")
    if len(q.get("choiceAnalysis", [])) != 4:
        errors.append(f"Q{n}: choiceAnalysis count != 4")
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
print("OK: section1 (17 questions) verified")

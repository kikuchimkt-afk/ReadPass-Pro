# -*- coding: utf-8 -*-
"""Verify 2026-1 grade2 (本会場) section2 structure and answers."""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade2", "2026-1", "data.json",
)

EXPECTED = {18: 1, 19: 1, 20: 3, 21: 2, 22: 1, 23: 4}

with open(DATA_PATH, encoding="utf-8") as f:
    d = json.load(f)

errors = []
sec = next((s for s in d["sections"] if s.get("name") == "大問2"), None)
if not sec:
    errors.append("section 大問2 not found")
    print(f"errors={len(errors)}")
    for e in errors:
        print(" ", e)
    sys.exit(1)

if sec["type"] != "passage-fill":
    errors.append(f"expected passage-fill, got {sec['type']}")
if len(sec["passages"]) != 2:
    errors.append(f"expected 2 passages, got {len(sec['passages'])}")

for pa in sec["passages"]:
    for key in ("label", "title", "paragraphs", "translations", "sentencePairs"):
        if key not in pa or not pa[key]:
            errors.append(f"passage {pa.get('label')}: missing {key}")
    if len(pa["paragraphs"]) != len(pa["translations"]):
        errors.append(f"passage {pa.get('label')}: paragraphs/translations mismatch")

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
    for i, ca in enumerate(q["choiceAnalysis"]):
        if i + 1 == q["answer"]:
            if not ca.startswith("✅"):
                errors.append(f"Q{n}: correct choice {i+1} missing ✅")
        elif not ca.startswith("❌"):
            errors.append(f"Q{n}: wrong choice {i+1} missing ❌")

print(f"section2 passages=2 questions={len(all_qs)} errors={len(errors)}")
for e in errors:
    print(" ", e)
if errors:
    sys.exit(1)
print("OK: section2 (6 questions) verified")

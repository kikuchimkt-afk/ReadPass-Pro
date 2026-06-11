# -*- coding: utf-8 -*-
"""Verify 2026-1 grade2 (本会場) section3 structure and answers."""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade2", "2026-1", "data.json",
)

EXPECTED = {24: 3, 25: 1, 26: 4, 27: 3, 28: 1, 29: 3, 30: 1, 31: 4}

with open(DATA_PATH, encoding="utf-8") as f:
    d = json.load(f)

errors = []
sec = next((s for s in d["sections"] if s.get("name") == "大問3"), None)
if not sec:
    errors.append("section 大問3 not found")
    print(f"errors={len(errors)}")
    for e in errors:
        print(" ", e)
    sys.exit(1)

if sec["type"] != "reading-comprehension":
    errors.append(f"expected reading-comprehension, got {sec['type']}")
if len(sec["passages"]) != 2:
    errors.append(f"expected 2 passages, got {len(sec['passages'])}")

for pa in sec["passages"]:
    for key in ("label", "title", "paragraphs", "translations", "sentencePairs"):
        if key not in pa or not pa[key]:
            errors.append(f"passage {pa.get('label')}: missing {key}")
    if len(pa["paragraphs"]) != len(pa["translations"]):
        errors.append(f"passage {pa.get('label')}: paragraphs/translations mismatch")
    if pa.get("label") == "A" and pa.get("format") != "email":
        errors.append("passage A: expected format=email")

all_qs = [q for pa in sec["passages"] for q in pa["questions"]]
for q in all_qs:
    n = q["number"]
    if q["answer"] != EXPECTED[n]:
        errors.append(f"Q{n}: answer {q['answer']} != expected {EXPECTED[n]}")
    for key in ("question", "questionTranslation", "choices", "choiceTranslations", "choiceAnalysis"):
        if key == "choices" or key == "choiceTranslations" or key == "choiceAnalysis":
            if key not in q or len(q[key]) != 4:
                errors.append(f"Q{n}: bad {key}")
        elif key not in q or not q[key]:
            errors.append(f"Q{n}: missing {key}")
    if "grammar" not in q or not q["grammar"]:
        errors.append(f"Q{n}: missing grammar")
    if "sourceEvidence" not in q or not q["sourceEvidence"]:
        errors.append(f"Q{n}: missing sourceEvidence")
    for i, ca in enumerate(q["choiceAnalysis"]):
        if i + 1 == q["answer"]:
            if not ca.startswith("✅"):
                errors.append(f"Q{n}: correct choice {i+1} missing ✅")
        elif not ca.startswith("❌"):
            errors.append(f"Q{n}: wrong choice {i+1} missing ❌")

print(f"section3 passages=2 questions={len(all_qs)} errors={len(errors)}")
for e in errors:
    print(" ", e)
if errors:
    sys.exit(1)
print("OK: section3 (8 questions) verified")

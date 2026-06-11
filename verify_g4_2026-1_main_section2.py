# -*- coding: utf-8 -*-
"""Verify 2026-1 grade4（本会場）section2 structure and answers."""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade4", "2026-1", "data.json",
)

EXPECTED = {16: 4, 17: 2, 18: 4, 19: 3, 20: 3}

REQUIRED_KEYS = (
    "text", "translation", "choices", "choiceTranslations",
    "choiceAnalysis", "choiceAnalysisSimple", "grammar", "grammarSimple",
    "questionAudio",
)

with open(DATA_PATH, encoding="utf-8") as f:
    d = json.load(f)

errors = []
sec = next((s for s in d["sections"] if s.get("name") == "大問2"), None)
if not sec:
    errors.append("missing 大問2")
    print(f"errors={len(errors)}")
    for e in errors:
        print(" ", e)
    sys.exit(1)

qs = sec["questions"]
if len(qs) != 5:
    errors.append(f"question count {len(qs)} != 5")

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
print("OK: section2 Q16-20 with rich explanations")

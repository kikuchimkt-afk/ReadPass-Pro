# -*- coding: utf-8 -*-
"""Verify 2026-1-sat grade3 section1 structure and answers."""
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade3", "2026-1-sat", "data.json",
)

EXPECTED = {
    1: 2, 2: 4, 3: 1, 4: 4, 5: 1, 6: 4, 7: 3, 8: 4, 9: 4, 10: 4,
    11: 3, 12: 4, 13: 3, 14: 3, 15: 2,
}

REQUIRED_KEYS = (
    "text", "translation", "choices", "choiceTranslations",
    "choiceAnalysis", "choiceAnalysisSimple", "grammar", "grammarSimple",
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
    if len(q.get("choiceTranslations", [])) != 4:
        errors.append(f"Q{n}: choiceTranslations count {len(q.get('choiceTranslations', []))}")
    for field in ("choiceAnalysis", "choiceAnalysisSimple"):
        values = q.get(field, [])
        marks = [i + 1 for i, text in enumerate(values) if text.startswith("○")]
        if marks != [q["answer"]]:
            errors.append(f"Q{n}: {field} marks={marks}, answer={q['answer']}")
        if any(text.startswith(("×", "✅", "❌")) for text in values):
            errors.append(f"Q{n}: {field} uses unsupported marker")
    normalized_translation = re.sub(
        r"[（(]\s*[　\s]*\s*[)）]", "( )", q.get("translation", "")
    )
    if normalized_translation.count("( )") != 1:
        errors.append(f"Q{n}: translation must preserve exactly one blank")

print(f"questions={len(qs)} errors={len(errors)}")
for e in errors:
    print(" ", e)
if errors:
    sys.exit(1)
print("OK: section1 Q1-15 with rich explanations")

# -*- coding: utf-8 -*-
"""Verify 2026-1-sat grade3 section2 structure and answers."""
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade3", "2026-1-sat", "data.json",
)

EXPECTED = {16: 3, 17: 3, 18: 3, 19: 1, 20: 2}

REQUIRED_KEYS = (
    "text", "translation", "choices", "choiceTranslations",
    "choiceAnalysis", "choiceAnalysisSimple", "grammar", "grammarSimple",
)

with open(DATA_PATH, encoding="utf-8") as f:
    d = json.load(f)

errors = []
sec = next((s for s in d["sections"] if s.get("name") == "大問2"), None)
if not sec:
    errors.append("missing 大問2 section")
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
    if len(q.get("choiceAnalysisSimple", [])) != 4:
        errors.append(f"Q{n}: choiceAnalysisSimple count {len(q.get('choiceAnalysisSimple', []))}")
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

q20 = next((q for q in qs if q.get("number") == 20), {})
q20_wrong = " ".join(
    q20.get("choiceAnalysis", [])[:1]
    + q20.get("choiceAnalysisSimple", [])[:1]
)
if "OK, I will" not in q20_wrong and "わかった、するね" not in q20_wrong:
    errors.append("Q20: Have a nice trip rationale must use Mother's response")
if "訪ねてくるので旅のあいさつではない" in q20_wrong or "きてくれるから合わない" in q20_wrong:
    errors.append("Q20: stale travel rationale remains")

print(f"questions={len(qs)} errors={len(errors)}")
for e in errors:
    print(" ", e)
if errors:
    sys.exit(1)
print("OK: section2 Q16-20 with rich explanations")

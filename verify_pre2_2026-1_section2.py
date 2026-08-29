# -*- coding: utf-8 -*-
"""2026-1-sat 準2級 大問2の正答・対訳・marker規則を検証。"""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

data_path = Path(__file__).resolve().parent / "data" / "grade-pre2" / "2026-1-sat" / "data.json"
data = json.loads(data_path.read_text(encoding="utf-8"))
section = data["sections"][1]
errors = []
official = [1, 1, 4, 1, 2]

if (section.get("name"), section.get("type")) != ("大問2", "vocabulary"):
    errors.append("section name/type mismatch")
if [q.get("number") for q in section.get("questions", [])] != list(range(16, 21)):
    errors.append("question numbers must be 16..20")

for q, answer in zip(section.get("questions", []), official):
    n = q["number"]
    if q.get("answer") != answer:
        errors.append(f"Q{n}: answer={q.get('answer')} != {answer}")
    for key in ("text", "translation", "choices", "choiceTranslations", "choiceAnalysis", "grammar"):
        if not q.get(key):
            errors.append(f"Q{n}: missing {key}")
    if len(q.get("choices", [])) != 4 or len(q.get("choiceTranslations", [])) != 4:
        errors.append(f"Q{n}: choice fields != 4")
    if f"( {n} )" not in q.get("text", "") or f"( {n} )" not in q.get("translation", ""):
        errors.append(f"Q{n}: blank missing in English/Japanese")
    analyses = q.get("choiceAnalysis", [])
    if len(analyses) != 4:
        errors.append(f"Q{n}: choiceAnalysis != 4")
        continue
    for i, analysis in enumerate(analyses, 1):
        if analysis.startswith(("✅", "❌", "○")):
            errors.append(f"Q{n} choice{i}: leading marker forbidden")
        if ("→正解。💡" in analysis) != (i == answer):
            errors.append(f"Q{n} choice{i}: correct marker mismatch")
        if len(analysis) > 100:
            errors.append(f"Q{n} choice{i}: analysis too long ({len(analysis)})")

by_number = {q["number"]: q for q in section["questions"]}
if by_number[16]["choiceTranslations"][0] != "そこへ直行する":
    errors.append("Q16 goes straight there translation is inaccurate")
if by_number[18]["choiceTranslations"][3] != "登山用ジャケット":
    errors.append("Q18 mountain jacket translation is inaccurate")
if by_number[20]["choiceTranslations"][2] != "搭乗便の時間が近い":
    errors.append("Q20 coming up translation is inaccurate")

print(f"section2 questions={len(section.get('questions', []))} errors={len(errors)}")
for error in errors:
    print(" ", error)
sys.exit(1 if errors else 0)

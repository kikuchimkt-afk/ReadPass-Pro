# -*- coding: utf-8 -*-
"""2026-1-sat 準2級 大問1の正答・対訳・解説規則を検証。"""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

data_path = Path(__file__).resolve().parent / "data" / "grade-pre2" / "2026-1-sat" / "data.json"
data = json.loads(data_path.read_text(encoding="utf-8"))
section = data["sections"][0]
errors = []
official = [2, 2, 3, 4, 3, 4, 3, 4, 2, 4, 4, 2, 3, 1, 2]

if (section.get("name"), section.get("type")) != ("大問1", "vocabulary"):
    errors.append("section name/type mismatch")
if [q.get("number") for q in section.get("questions", [])] != list(range(1, 16)):
    errors.append("question numbers must be 1..15")

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
        marker = "✅" if i == answer else "❌"
        if not analysis.startswith(marker):
            errors.append(f"Q{n} choice{i}: expected {marker}")
        if len(analysis) > 100:
            errors.append(f"Q{n} choice{i}: analysis too long ({len(analysis)})")

by_number = {q["number"]: q for q in section["questions"]}
if by_number[8]["choiceTranslations"][0] != "思い出させた":
    errors.append("Q8 reminded translation must be 思い出させた")
if by_number[10]["choiceTranslations"][3] != "使用中の":
    errors.append("Q10 occupied translation must be 使用中の")
if "あら探し" not in by_number[14]["choiceTranslations"][0]:
    errors.append("Q14 find fault with translation is inaccurate")
if by_number[15]["choiceTranslations"][1] != "自由に取ってください":
    errors.append("Q15 help yourself translation is inaccurate")

print(f"section1 questions={len(section.get('questions', []))} errors={len(errors)}")
for error in errors:
    print(" ", error)
sys.exit(1 if errors else 0)

# -*- coding: utf-8 -*-
"""2026-1-sat 準2級 大問3の原文・全文対訳・根拠を検証。"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

data_path = Path(__file__).resolve().parent / "data" / "grade-pre2" / "2026-1-sat" / "data.json"
data = json.loads(data_path.read_text(encoding="utf-8"))
section = data["sections"][2]
errors = []

if (section.get("name"), section.get("type")) != ("大問3", "passage-fill"):
    errors.append("section name/type mismatch")
if len(section.get("passages", [])) != 1:
    errors.append("passage count != 1")

passage = section["passages"][0]
if passage.get("title") != "A Lost Dog":
    errors.append("title mismatch")
if len(passage.get("paragraphs", [])) != 2 or len(passage.get("translations", [])) != 2:
    errors.append("paragraph/translation count != 2")
pairs = passage.get("sentencePairs", [])
if len(pairs) != 14:
    errors.append(f"sentencePairs={len(pairs)} != 14")
compact = lambda text: re.sub(r"\s+", "", text)
if compact(" ".join(x[0] for x in pairs)) != compact(" ".join(passage["paragraphs"])):
    errors.append("English sentencePairs are not full ordered coverage")
if compact(" ".join(x[1] for x in pairs)) != compact(" ".join(passage["translations"])):
    errors.append("Japanese sentencePairs are not full ordered coverage")

corpus = " ".join(passage["paragraphs"])
official = {21: 4, 22: 1}
if [q.get("number") for q in passage.get("questions", [])] != [21, 22]:
    errors.append("question numbers must be 21,22")
for q in passage.get("questions", []):
    n = q["number"]
    if q.get("answer") != official[n]:
        errors.append(f"Q{n}: answer mismatch")
    if len(q.get("choices", [])) != 4 or len(q.get("choiceTranslations", [])) != 4:
        errors.append(f"Q{n}: choice fields != 4")
    analyses = q.get("choiceAnalysis", [])
    if len(analyses) != 4:
        errors.append(f"Q{n}: choiceAnalysis != 4")
    for i, analysis in enumerate(analyses, 1):
        if analysis.startswith(("✅", "❌", "○")):
            errors.append(f"Q{n} choice{i}: leading marker forbidden")
        if ("→正解。💡" in analysis) != (i == official[n]):
            errors.append(f"Q{n} choice{i}: correct marker mismatch")
    for evidence in q.get("sourceEvidence", []):
        if evidence not in corpus:
            errors.append(f"Q{n}: evidence not in source: {evidence!r}")
    if not q.get("sourceEvidence") or not q.get("grammar"):
        errors.append(f"Q{n}: evidence/grammar missing")

print(f"section3 pairs={len(pairs)} errors={len(errors)}")
for error in errors:
    print(" ", error)
sys.exit(1 if errors else 0)

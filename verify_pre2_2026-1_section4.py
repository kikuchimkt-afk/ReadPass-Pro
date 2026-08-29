# -*- coding: utf-8 -*-
"""2026-1-sat 準2級 大問4の原文・全文対訳・根拠を検証。"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

data_path = Path(__file__).resolve().parent / "data" / "grade-pre2" / "2026-1-sat" / "data.json"
data = json.loads(data_path.read_text(encoding="utf-8"))
section = data["sections"][3]
errors = []
expected = {
    "A job at a ski resort": ([23, 24, 25], [3, 4, 1], 3, 21),
    "Social Media for Mental Health": ([26, 27, 28, 29], [4, 4, 3, 2], 4, 19),
}

if (section.get("name"), section.get("type")) != ("大問4", "reading-comprehension"):
    errors.append("section name/type mismatch")
if len(section.get("passages", [])) != 2:
    errors.append("passage count != 2")

compact = lambda text: re.sub(r"\s+", "", text)
for passage in section.get("passages", []):
    title = passage.get("title")
    if title not in expected:
        errors.append(f"unexpected passage {title}")
        continue
    numbers, answers, paragraph_count, pair_count = expected[title]
    if len(passage.get("paragraphs", [])) != paragraph_count:
        errors.append(f"{title}: paragraph count")
    if len(passage.get("translations", [])) != paragraph_count:
        errors.append(f"{title}: translation count")
    pairs = passage.get("sentencePairs", [])
    if len(pairs) != pair_count:
        errors.append(f"{title}: sentencePairs={len(pairs)} != {pair_count}")
    if compact(" ".join(x[0] for x in pairs)) != compact(" ".join(passage["paragraphs"])):
        errors.append(f"{title}: English pairs are not full ordered coverage")
    if compact(" ".join(x[1] for x in pairs)) != compact(" ".join(passage["translations"])):
        errors.append(f"{title}: Japanese pairs are not full ordered coverage")
    if [q.get("number") for q in passage.get("questions", [])] != numbers:
        errors.append(f"{title}: question numbers")
    corpus = " ".join(passage["paragraphs"])
    for q, answer in zip(passage.get("questions", []), answers):
        n = q["number"]
        if q.get("answer") != answer:
            errors.append(f"Q{n}: answer mismatch")
        for key in (
            "question", "questionTranslation", "choices", "choiceTranslations",
            "choiceAnalysis", "sourceEvidence", "grammar",
        ):
            if not q.get(key):
                errors.append(f"Q{n}: missing {key}")
        if len(q.get("choices", [])) != 4 or len(q.get("choiceTranslations", [])) != 4:
            errors.append(f"Q{n}: choice fields != 4")
        for i, analysis in enumerate(q.get("choiceAnalysis", []), 1):
            if analysis.startswith(("✅", "❌", "○")):
                errors.append(f"Q{n} choice{i}: leading marker forbidden")
            if ("→正解。💡" in analysis) != (i == answer):
                errors.append(f"Q{n} choice{i}: correct marker mismatch")
        for evidence in q.get("sourceEvidence", []):
            if evidence not in corpus:
                errors.append(f"Q{n}: evidence not in source: {evidence!r}")

email = section["passages"][0]
if email.get("format") != "email" or set(email.get("meta", {})) != {"from", "to", "date", "subject"}:
    errors.append("email format/meta mismatch")

print(f"section4 passages={len(section.get('passages', []))} errors={len(errors)}")
for error in errors:
    print(" ", error)
sys.exit(1 if errors else 0)

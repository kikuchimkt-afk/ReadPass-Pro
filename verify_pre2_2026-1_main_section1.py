# -*- coding: utf-8 -*-
"""2026-1 準2級（本会場）大問1 リッチ解説検証"""
import json
import os
import re
import statistics
import sys

sys.stdout.reconfigure(encoding="utf-8")

path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade-pre2", "2026-1", "data.json",
)
d = json.load(open(path, encoding="utf-8"))
s = d["sections"][0]
errs = []
expected = [2, 1, 1, 4, 4, 3, 2, 3, 4, 1, 2, 4, 1, 1, 2]

if s.get("name") != "大問1":
    errs.append(f"sections[0] is {s.get('name')}, not 大問1")

for q, a in zip(s["questions"], expected):
    n = q["number"]
    if q["answer"] != a:
        errs.append(f"Q{n} answer {q['answer']} != {a}")
    for k in ["text", "translation", "choices", "choiceTranslations", "choiceAnalysis", "grammar"]:
        if k not in q:
            errs.append(f"Q{n} missing {k}")
    if len(q.get("choices", [])) != 4:
        errs.append(f"Q{n} choices")
    if len(q.get("choiceAnalysis", [])) != 4:
        errs.append(f"Q{n} analysis count")
    if q.get("text") and "( )" in q["text"] and not re.search(r"[（(][\s　]*[）)]", q.get("translation", "")):
        errs.append(f"Q{n} translation lost blank")
    for i, ca in enumerate(q.get("choiceAnalysis", [])):
        if q["answer"] == i + 1 and not ca.startswith("✅"):
            errs.append(f"Q{n} opt{i+1} should be ✅")
        elif q["answer"] != i + 1 and not ca.startswith("❌"):
            errs.append(f"Q{n} opt{i+1} should be ❌")

analysis_lengths = [len(ca) for q in s["questions"] for ca in q.get("choiceAnalysis", [])]
if analysis_lengths and statistics.mean(analysis_lengths) > 75:
    errs.append(f"choiceAnalysis average too long: {statistics.mean(analysis_lengths):.1f}")

blob = json.dumps(s, ensure_ascii=False)
for stale in ("feel nervously", "学生の先生", "行き道で", "誰かの親切をする", "父娘の会話では使わない"):
    if stale in blob:
        errs.append(f"stale or inaccurate wording remains: {stale}")

print(f"sections={len(d['sections'])} questions={len(s['questions'])} errors={len(errs)}")
for e in errs:
    print(e)
if errs:
    sys.exit(1)
print("OK: section1 rich explanations verified")

# -*- coding: utf-8 -*-
"""2026-1 準2級（本会場）大問1 リッチ解説検証"""
import json
import os
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
    for i, ca in enumerate(q.get("choiceAnalysis", [])):
        if q["answer"] == i + 1 and not ca.startswith("✅"):
            errs.append(f"Q{n} opt{i+1} should be ✅")
        elif q["answer"] != i + 1 and not ca.startswith("❌"):
            errs.append(f"Q{n} opt{i+1} should be ❌")

print(f"sections={len(d['sections'])} questions={len(s['questions'])} errors={len(errs)}")
for e in errs:
    print(e)
if errs:
    sys.exit(1)
print("OK: section1 rich explanations verified")

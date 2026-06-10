# -*- coding: utf-8 -*-
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

path = os.path.join("data", "grade-pre2", "2026-1-sat", "data.json")
d = json.load(open(path, encoding="utf-8"))
assert len(d["sections"]) == 3, f"expected 3 sections, got {len(d['sections'])}"

s = d["sections"][2]
errs = []
if s["type"] != "passage-fill":
    errs.append("wrong type")
if s["name"] != "大問3":
    errs.append("wrong name")

p = s["passages"][0]
expected = [4, 1]
for q, a in zip(p["questions"], expected):
    n = q["number"]
    if q["answer"] != a:
        errs.append(f"Q{n} answer {q['answer']} != {a}")
    for k in ["choices", "choiceTranslations", "choiceAnalysis", "grammar"]:
        if k not in q:
            errs.append(f"Q{n} missing {k}")
    if len(q.get("choiceAnalysis", [])) != 4:
        errs.append(f"Q{n} analysis count")

for k in ["title", "paragraphs", "translations", "sentencePairs", "questions"]:
    if k not in p:
        errs.append(f"passage missing {k}")
if len(p.get("paragraphs", [])) != 2:
    errs.append("paragraph count")

print(f"section3 errors={len(errs)}")
for e in errs:
    print(e)
sys.exit(1 if errs else 0)

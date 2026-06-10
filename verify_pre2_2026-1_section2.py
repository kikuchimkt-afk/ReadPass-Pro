# -*- coding: utf-8 -*-
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

path = os.path.join("data", "grade-pre2", "2026-1-sat", "data.json")
d = json.load(open(path, encoding="utf-8"))
assert len(d["sections"]) >= 2, f"expected >=2 sections, got {len(d['sections'])}"

s = d["sections"][1]
assert s["name"] == "大問2"
errs = []
expected = [1, 1, 4, 1, 2]

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

print(f"section2 questions={len(s['questions'])} errors={len(errs)}")
for e in errs:
    print(e)
sys.exit(1 if errs else 0)

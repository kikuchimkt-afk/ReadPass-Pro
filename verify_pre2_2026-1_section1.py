# -*- coding: utf-8 -*-
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

path = os.path.join("data", "grade-pre2", "2026-1-sat", "data.json")
d = json.load(open(path, encoding="utf-8"))
s = d["sections"][0]
errs = []
expected = [2, 2, 3, 4, 3, 4, 3, 4, 2, 4, 4, 2, 3, 1, 2]

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
sys.exit(1 if errs else 0)

# -*- coding: utf-8 -*-
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

path = os.path.join("data", "grade-pre2", "2026-1-sat", "data.json")
d = json.load(open(path, encoding="utf-8"))
assert len(d["sections"]) == 4, f"expected 4 sections, got {len(d['sections'])}"

s = d["sections"][3]
errs = []
if s["type"] != "reading-comprehension":
    errs.append("wrong type")

all_q = []
for p in s["passages"]:
    all_q.extend(p["questions"])

expected = [3, 4, 1, 4, 4, 3, 2]
for q, a in zip(all_q, expected):
    n = q["number"]
    if q["answer"] != a:
        errs.append(f"Q{n} answer {q['answer']} != {a}")
    for k in ["question", "questionTranslation", "choices", "choiceTranslations", "choiceAnalysis", "grammar"]:
        if k not in q:
            errs.append(f"Q{n} missing {k}")
    if len(q.get("choiceAnalysis", [])) != 4:
        errs.append(f"Q{n} analysis count")

pa = s["passages"][0]
if pa.get("format") != "email" or "meta" not in pa:
    errs.append("passage A email meta")

print(f"section4 questions={len(all_q)} errors={len(errs)}")
for e in errs:
    print(e)
sys.exit(1 if errs else 0)

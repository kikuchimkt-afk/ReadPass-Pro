# -*- coding: utf-8 -*-
"""2026-1 準2級（本会場）大問3 リッチ解説検証"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade-pre2", "2026-1", "data.json",
)
d = json.load(open(path, encoding="utf-8"))
assert len(d["sections"]) >= 3, f"expected >=3 sections, got {len(d['sections'])}"

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
    for k in ["choices", "choiceTranslations", "choiceAnalysis", "grammar", "sourceEvidence"]:
        if k not in q:
            errs.append(f"Q{n} missing {k}")
    if not q.get("sourceEvidence"):
        errs.append(f"Q{n} missing sourceEvidence items")
    if len(q.get("choiceAnalysis", [])) != 4:
        errs.append(f"Q{n} analysis count")
    for i, ca in enumerate(q.get("choiceAnalysis", [])):
        if q["answer"] == i + 1 and not ca.startswith("✅"):
            errs.append(f"Q{n} opt{i+1} should be ✅")
        elif q["answer"] != i + 1 and not ca.startswith("❌"):
            errs.append(f"Q{n} opt{i+1} should be ❌")

for k in ["title", "paragraphs", "translations", "sentencePairs", "questions"]:
    if k not in p:
        errs.append(f"passage missing {k}")
if len(p.get("paragraphs", [])) != 2:
    errs.append("paragraph count")
if p.get("title") != "The Advice":
    errs.append(f"title={p.get('title')}")

print(f"section3 errors={len(errs)}")
for e in errs:
    print(e)
if errs:
    sys.exit(1)
print("OK: section3 rich explanations verified")

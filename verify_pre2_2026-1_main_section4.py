# -*- coding: utf-8 -*-
"""2026-1 準2級（本会場）大問4 リッチ解説検証"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade-pre2", "2026-1", "data.json",
)
d = json.load(open(path, encoding="utf-8"))
assert len(d["sections"]) == 4, f"expected 4 sections, got {len(d['sections'])}"

s = d["sections"][3]
errs = []
if s["type"] != "reading-comprehension":
    errs.append("wrong type")
if s["name"] != "大問4":
    errs.append("wrong name")

all_q = []
for p in s["passages"]:
    all_q.extend(p["questions"])

expected = [3, 4, 3, 3, 4, 2, 3]
for q, a in zip(all_q, expected):
    n = q["number"]
    if q["answer"] != a:
        errs.append(f"Q{n} answer {q['answer']} != {a}")
    for k in ["question", "questionTranslation", "choices", "choiceTranslations", "choiceAnalysis", "grammar", "sourceEvidence"]:
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

pa = s["passages"][0]
pb = s["passages"][1]
if pa.get("format") != "email" or "meta" not in pa:
    errs.append("passage A email meta")
if pa.get("title") != "About joining my band":
    errs.append(f"passage A title={pa.get('title')}")
if pb.get("title") != "Pig Beach":
    errs.append(f"passage B title={pb.get('title')}")
for k in ["translations", "sentencePairs"]:
    if k not in pa:
        errs.append(f"passage A missing {k}")
    if k not in pb:
        errs.append(f"passage B missing {k}")

print(f"section4 questions={len(all_q)} errors={len(errs)}")
for e in errs:
    print(e)
if errs:
    sys.exit(1)
print("OK: section4 rich explanations verified")

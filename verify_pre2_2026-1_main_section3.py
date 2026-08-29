# -*- coding: utf-8 -*-
"""2026-1 準2級（本会場）大問3 リッチ解説検証"""
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
        if ca.lstrip().startswith(("✅", "❌", "○")):
            errs.append(f"Q{n} opt{i+1} has a legacy leading marker")
        is_correct_text = "正解" in ca and "誤答" not in ca
        if q["answer"] == i + 1:
            if not is_correct_text or "💡" not in ca:
                errs.append(f"Q{n} opt{i+1} should contain 正解 and 💡")
        elif is_correct_text:
            errs.append(f"Q{n} opt{i+1} incorrectly says 正解")

for k in ["title", "paragraphs", "translations", "sentencePairs", "questions"]:
    if k not in p:
        errs.append(f"passage missing {k}")
if len(p.get("paragraphs", [])) != 2:
    errs.append("paragraph count")
if p.get("title") != "The Advice":
    errs.append(f"title={p.get('title')}")

english = " ".join(p.get("paragraphs", []))
japanese = " ".join(p.get("translations", []))
for n in (21, 22):
    if not re.search(rf"[（(][\s　]*{n}[\s　]*[）)]", japanese):
        errs.append(f"Q{n} translation lost numbered blank")
if len(p.get("sentencePairs", [])) != 14:
    errs.append(f"sentencePairs count={len(p.get('sentencePairs', []))}, expected 14")
for i, pair in enumerate(p.get("sentencePairs", [])):
    if len(pair) < 2 or pair[0] not in english or not pair[1]:
        errs.append(f"sentencePairs[{i}] invalid")

analysis_lengths = [len(ca) for q in p["questions"] for ca in q.get("choiceAnalysis", [])]
if analysis_lengths and statistics.mean(analysis_lengths) > 90:
    errs.append(f"choiceAnalysis average too long: {statistics.mean(analysis_lengths):.1f}")

blob = json.dumps(s, ensure_ascii=False)
for stale in ("努力そのものを否定", "スピーチの活動"):
    if stale in blob:
        errs.append(f"stale wording remains: {stale}")

print(f"section3 errors={len(errs)}")
for e in errs:
    print(e)
if errs:
    sys.exit(1)
print("OK: section3 rich explanations verified")

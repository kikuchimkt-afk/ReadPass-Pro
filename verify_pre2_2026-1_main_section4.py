# -*- coding: utf-8 -*-
"""2026-1 準2級（本会場）大問4 リッチ解説検証"""
import json
import os
import statistics
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
        if ca.lstrip().startswith(("✅", "❌", "○")):
            errs.append(f"Q{n} opt{i+1} has a legacy leading marker")
        is_correct_text = "正解" in ca and "誤答" not in ca
        if q["answer"] == i + 1:
            if not is_correct_text or "💡" not in ca:
                errs.append(f"Q{n} opt{i+1} should contain 正解 and 💡")
        elif is_correct_text:
            errs.append(f"Q{n} opt{i+1} incorrectly says 正解")

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

for passage, expected_pairs in ((pa, 18), (pb, 20)):
    corpus = " ".join(passage.get("paragraphs", []))
    if len(passage.get("sentencePairs", [])) != expected_pairs:
        errs.append(
            f"{passage.get('title')} sentencePairs={len(passage.get('sentencePairs', []))}, expected {expected_pairs}"
        )
    for i, pair in enumerate(passage.get("sentencePairs", [])):
        if len(pair) < 2 or pair[0] not in corpus or not pair[1]:
            errs.append(f"{passage.get('title')} sentencePairs[{i}] invalid")

q24 = next(q for q in all_q if q["number"] == 24)
if not any(ev.startswith("The band started last year") for ev in q24.get("sourceEvidence", [])):
    errs.append("Q24 sourceEvidence should contain the full The band started sentence")
q25 = next(q for q in all_q if q["number"] == 25)
if not any(ev.startswith("Then, you can go watch") for ev in q25.get("sourceEvidence", [])):
    errs.append("Q25 sourceEvidence should contain the Then sentence")

analysis_lengths = [len(ca) for q in all_q for ca in q.get("choiceAnalysis", [])]
if analysis_lengths and statistics.mean(analysis_lengths) > 90:
    errs.append(f"choiceAnalysis average too long: {statistics.mean(analysis_lengths):.1f}")

blob = json.dumps(s, ensure_ascii=False)
for stale in ("もともとギタリストを探していた", "古い船員", "船が着陸", "食べるのに良くない餌", "観客増"):
    if stale in blob:
        errs.append(f"stale wording remains: {stale}")

print(f"section4 questions={len(all_q)} errors={len(errs)}")
for e in errs:
    print(e)
if errs:
    sys.exit(1)
print("OK: section4 rich explanations verified")

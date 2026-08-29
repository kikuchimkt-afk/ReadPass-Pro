# -*- coding: utf-8 -*-
"""Verify 2026-1 grade2 (本会場) section3 structure and answers."""
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade2", "2026-1", "data.json",
)

EXPECTED = {24: 3, 25: 1, 26: 4, 27: 3, 28: 1, 29: 3, 30: 1, 31: 4}
EXPECTED_PAIR_COUNTS = {"A": 14, "B": 22}


def norm(text):
    return re.sub(r"\s+", " ", text or "").strip()

with open(DATA_PATH, encoding="utf-8") as f:
    d = json.load(f)

errors = []
sec = next((s for s in d["sections"] if s.get("name") == "大問3"), None)
if not sec:
    errors.append("section 大問3 not found")
    print(f"errors={len(errors)}")
    for e in errors:
        print(" ", e)
    sys.exit(1)

if sec["type"] != "reading-comprehension":
    errors.append(f"expected reading-comprehension, got {sec['type']}")
if len(sec["passages"]) != 2:
    errors.append(f"expected 2 passages, got {len(sec['passages'])}")

for pa in sec["passages"]:
    for key in ("label", "title", "paragraphs", "translations", "sentencePairs"):
        if key not in pa or not pa[key]:
            errors.append(f"passage {pa.get('label')}: missing {key}")
    if len(pa["paragraphs"]) != len(pa["translations"]):
        errors.append(f"passage {pa.get('label')}: paragraphs/translations mismatch")
    if pa.get("label") == "A" and pa.get("format") != "email":
        errors.append("passage A: expected format=email")
    label = pa.get("label")
    pairs = pa.get("sentencePairs", [])
    if len(pairs) != EXPECTED_PAIR_COUNTS.get(label):
        errors.append(
            f"passage {label}: sentencePairs={len(pairs)} "
            f"!= {EXPECTED_PAIR_COUNTS.get(label)}"
        )
    pair_english = []
    for index, pair in enumerate(pairs, 1):
        if (
            not isinstance(pair, list)
            or len(pair) != 4
            or not all(isinstance(item, str) and item.strip() for item in pair)
        ):
            errors.append(f"passage {label}: sentencePair {index} is not 4 nonempty strings")
            continue
        pair_english.append(pair[0])
        slash_segments = pair[2].split("||")
        if len(slash_segments) < 2:
            errors.append(f"passage {label}: sentencePair {index} has fewer than 2 slash units")
            continue
        if any(
            segment.count("|") != 1
            or not all(part.strip() for part in segment.split("|", 1))
            for segment in slash_segments
        ):
            errors.append(f"passage {label}: sentencePair {index} has invalid slash syntax")
            continue
        slash_english = " ".join(
            segment.split("|", 1)[0] for segment in slash_segments
        )
        if norm(slash_english) != norm(pair[0]):
            errors.append(f"passage {label}: sentencePair {index} slash English mismatch")
        if not re.search(
            rf"(?<!\w){re.escape(pair[3])}(?!\w)", pair[0], re.IGNORECASE
        ):
            errors.append(f"passage {label}: sentencePair {index} main verb not in English")
    if label == "A":
        # 2025年度と同じく、あいさつ・署名を除いたメール本文14文を全て対訳化。
        expected_corpus = (
            pa["paragraphs"][0].split("\n", 1)[1]
            + " " + pa["paragraphs"][1]
            + " " + pa["paragraphs"][2]
        )
    else:
        expected_corpus = " ".join(pa["paragraphs"])
    if norm(" ".join(pair_english)) != norm(expected_corpus):
        errors.append(f"passage {label}: sentencePairs do not cover full text")

all_qs = [q for pa in sec["passages"] for q in pa["questions"]]
for q in all_qs:
    n = q["number"]
    if q["answer"] != EXPECTED[n]:
        errors.append(f"Q{n}: answer {q['answer']} != expected {EXPECTED[n]}")
    for key in ("question", "questionTranslation", "choices", "choiceTranslations", "choiceAnalysis"):
        if key == "choices" or key == "choiceTranslations" or key == "choiceAnalysis":
            if key not in q or len(q[key]) != 4:
                errors.append(f"Q{n}: bad {key}")
        elif key not in q or not q[key]:
            errors.append(f"Q{n}: missing {key}")
    if "grammar" not in q or not q["grammar"]:
        errors.append(f"Q{n}: missing grammar")
    if "sourceEvidence" not in q or not q.get("sourceEvidence"):
        errors.append(f"Q{n}: missing sourceEvidence")
    analyses = q["choiceAnalysis"]
    if any(text.lstrip().startswith(("✅", "❌", "○", "×")) for text in analyses):
        errors.append(f"Q{n}: leading marker remains")
    for i, ca in enumerate(analyses):
        if i + 1 == q["answer"]:
            if ca.count("→正解。💡") != 1:
                errors.append(f"Q{n}: correct choice {i+1} missing exact answer marker")
        elif "→正解" in ca:
            errors.append(f"Q{n}: wrong choice {i+1} contains answer marker")

by_number = {q["number"]: q for q in all_qs}
if "兄からの誘い" not in by_number.get(28, {}).get("choiceTranslations", [None, None, ""])[2]:
    errors.append("Q28: brother translation regression")

serialized = json.dumps(sec, ensure_ascii=False)
for stale in (
    "弟が新たな冒険",
    "弟からの新しい場所",
    "兄からの新しい場所への旅の誘い",
    "裕福な背景は質の高い教育",
):
    if stale in serialized:
        errors.append(f"stale translation remains: {stale}")
email_pairs = sec["passages"][0]["sentencePairs"]
if not email_pairs[4][1].startswith("また、"):
    errors.append("email sentencePair 5: Also translation missing")
if not email_pairs[7][1].startswith("現在、"):
    errors.append("email sentencePair 8: Currently translation missing")
if not email_pairs[8][1].startswith("ウェブサイトによると、"):
    errors.append("email sentencePair 9: According to the website translation missing")

print(f"section3 passages=2 questions={len(all_qs)} errors={len(errors)}")
for e in errors:
    print(" ", e)
if errors:
    sys.exit(1)
print("OK: section3 (8 questions) verified")

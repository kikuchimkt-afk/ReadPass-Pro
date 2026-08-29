# -*- coding: utf-8 -*-
"""Verify 2026-1-sat grade3 section3 structure and answers."""
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade3", "2026-1-sat", "data.json",
)

EXPECTED = {
    21: 3, 22: 1, 23: 1, 24: 4, 25: 3,
    26: 3, 27: 1, 28: 2, 29: 3, 30: 4,
}

Q_KEYS = (
    "question", "questionTranslation", "choices", "choiceTranslations",
    "choiceAnalysis", "choiceAnalysisSimple", "grammar", "grammarSimple",
)
PAIR_COUNTS = {"A": 12, "B": 34, "C": 18}


def norm(text):
    return re.sub(r"\s+", " ", text or "").strip()

with open(DATA_PATH, encoding="utf-8") as f:
    d = json.load(f)

errors = []
sec = next((s for s in d["sections"] if s.get("name") == "大問3"), None)
if not sec:
    errors.append("missing 大問3")
    print(f"errors={len(errors)}")
    sys.exit(1)

passages = sec.get("passages", [])
if len(passages) != 3:
    errors.append(f"passage count {len(passages)} != 3")

all_qs = []
for pa in passages:
    if pa.get("label") not in ("A", "B", "C"):
        errors.append(f"bad label {pa.get('label')}")
    if "translations" not in pa or not pa["translations"]:
        errors.append(f"passage {pa.get('label')}: missing translations")
    if len(pa.get("paragraphs", [])) != len(pa.get("translations", [])):
        errors.append(
            f"passage {pa.get('label')}: paragraphs/translations length mismatch"
        )
    if pa.get("format") == "multi-email":
        for em in pa.get("emails", []):
            if "translation" not in em or not em["translation"]:
                errors.append(f"passage B email missing translation")
        source_corpus = " ".join(em.get("body", "") for em in pa.get("emails", []))
    else:
        source_corpus = " ".join(pa.get("paragraphs", []))
    pairs = pa.get("sentencePairs", [])
    if len(pairs) != PAIR_COUNTS.get(pa.get("label")):
        errors.append(
            f"passage {pa.get('label')}: sentencePairs {len(pairs)} "
            f"!= {PAIR_COUNTS.get(pa.get('label'))}"
        )
    pair_english = []
    for i, pair in enumerate(pairs, 1):
        if (
            not isinstance(pair, list)
            or len(pair) != 2
            or not all(isinstance(text, str) and text.strip() for text in pair)
        ):
            errors.append(f"passage {pa.get('label')} pair{i}: invalid")
            continue
        pair_english.append(pair[0])
    if norm(" ".join(pair_english)) != norm(source_corpus):
        errors.append(f"passage {pa.get('label')}: sentencePairs incomplete")
    all_qs.extend(pa.get("questions", []))

if len(all_qs) != 10:
    errors.append(f"question count {len(all_qs)} != 10")

for q in all_qs:
    n = q["number"]
    if EXPECTED.get(n) != q.get("answer"):
        errors.append(f"Q{n}: answer={q.get('answer')} official={EXPECTED.get(n)}")
    for key in Q_KEYS:
        if key not in q or not q[key]:
            errors.append(f"Q{n}: missing {key}")
    if len(q.get("choices", [])) != 4:
        errors.append(f"Q{n}: choices != 4")
    if not q.get("sourceEvidence"):
        errors.append(f"Q{n}: missing sourceEvidence")
    for field in ("choices", "choiceTranslations", "choiceAnalysis", "choiceAnalysisSimple"):
        values = q.get(field, [])
        if len(values) != 4:
            errors.append(f"Q{n}: {field} count {len(values)}")
            continue
        if field.startswith("choiceAnalysis"):
            marks = [i + 1 for i, text in enumerate(values) if text.startswith("○")]
            if marks != [q["answer"]]:
                errors.append(f"Q{n}: {field} marks={marks}, answer={q['answer']}")
            if any(text.startswith(("×", "✅", "❌")) for text in values):
                errors.append(f"Q{n}: {field} uses unsupported marker")

print(f"passages={len(passages)} questions={len(all_qs)} errors={len(errors)}")
for e in errors:
    print(" ", e)
if errors:
    sys.exit(1)
print("OK: section3 Q21-30 with rich explanations")

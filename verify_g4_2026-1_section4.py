# -*- coding: utf-8 -*-
"""Verify 2026-1-sat grade4 section4 (reading) structure and answers."""
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade4", "2026-1-sat", "data.json",
)
DATA_DIR = os.path.dirname(DATA_PATH)

EXPECTED = {
    26: 3, 27: 4, 28: 4, 29: 1, 30: 2,
    31: 2, 32: 2, 33: 1, 34: 4, 35: 4,
}

Q_KEYS = (
    "question", "questionTranslation", "choices", "choiceTranslations",
    "choiceAnalysis", "choiceAnalysisSimple", "grammar", "grammarSimple",
    "sourceEvidence", "questionAudio",
)
PAIR_COUNTS = {"A": 7, "B": 17, "C": 13}


def compact(text):
    return re.sub(r"\s+", "", text or "")


def audio_ok(rel):
    path = os.path.join(DATA_DIR, (rel or "").replace("/", os.sep))
    return bool(rel) and os.path.isfile(path) and os.path.getsize(path) >= 500

with open(DATA_PATH, encoding="utf-8") as f:
    d = json.load(f)

errors = []
sec = next((s for s in d["sections"] if s.get("name") == "大問4"), None)
if not sec:
    errors.append("missing 大問4")
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
    pairs = pa.get("sentencePairs", [])
    if len(pairs) != PAIR_COUNTS.get(pa.get("label")):
        errors.append(
            f"passage {pa.get('label')}: sentencePairs={len(pairs)} "
            f"!= {PAIR_COUNTS.get(pa.get('label'))}"
        )
    valid = [p for p in pairs if isinstance(p, list) and len(p) == 2 and all(p)]
    if len(valid) != len(pairs):
        errors.append(f"passage {pa.get('label')}: invalid sentencePair")
    if compact("".join(p[0] for p in valid)) != compact("".join(pa.get("paragraphs", []))):
        errors.append(f"passage {pa.get('label')}: sentencePairs do not fully cover English")
    if compact("".join(p[1] for p in valid)) != compact("".join(pa.get("translations", []))):
        errors.append(f"passage {pa.get('label')}: sentencePairs do not fully cover Japanese")
    corpus = " ".join(pa.get("paragraphs", []))
    for q in pa.get("questions", []):
        if q.get("sourceEvidence") not in corpus:
            errors.append(f"Q{q.get('number')}: sourceEvidence not found in passage")
    all_qs.extend(pa.get("questions", []))

if len(all_qs) != 10:
    errors.append(f"question count {len(all_qs)} != 10")

q34 = next((q for q in all_qs if q.get("number") == 34), {})
if q34.get("choiceAnalysisSimple", [None])[0] != "れきしのほんは「1さつ」じゃないよ。":
    errors.append("Q34: 1冊を小説の冊数とする誤説明が残っています")

for q in all_qs:
    n = q["number"]
    if EXPECTED.get(n) != q.get("answer"):
        errors.append(f"Q{n}: answer={q.get('answer')} official={EXPECTED.get(n)}")
    for key in Q_KEYS:
        if key not in q or not q[key]:
            errors.append(f"Q{n}: missing {key}")
    if len(q.get("choices", [])) != 4:
        errors.append(f"Q{n}: choices != 4")
    if len(q.get("choiceTranslations", [])) != 4:
        errors.append(f"Q{n}: choiceTranslations != 4")
    if not audio_ok(q.get("questionAudio")):
        errors.append(f"Q{n}: missing audio {q.get('questionAudio')}")
    for field in ("choiceAnalysis", "choiceAnalysisSimple"):
        values = q.get(field, [])
        marked = [i + 1 for i, ca in enumerate(values) if ca.lstrip().startswith("○")]
        if marked != [q["answer"]]:
            errors.append(f"Q{n}: {field} marker positions {marked}")
        if any(ca.lstrip().startswith(("✅", "❌")) for ca in values):
            errors.append(f"Q{n}: {field} has old emoji marker")

print(f"passages={len(passages)} questions={len(all_qs)} errors={len(errors)}")
for e in errors:
    print(" ", e)
if errors:
    sys.exit(1)
print("OK: section4 Q26-35 with rich explanations")

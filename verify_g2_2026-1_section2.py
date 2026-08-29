# -*- coding: utf-8 -*-
"""Verify 2026-1 grade2 (本会場) section2 structure and answers."""
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade2", "2026-1", "data.json",
)

EXPECTED = {18: 1, 19: 1, 20: 3, 21: 2, 22: 1, 23: 4}
EXPECTED_PAIR_COUNTS = {"A": 19, "B": 18}


def norm(text):
    return re.sub(r"\s+", " ", text or "").strip()


def phrase_exists(sentence, phrase):
    """Match a verb/verb phrase as English tokens, not inside another word."""
    pattern = r"(?<![A-Za-z])" + r"\s+".join(
        re.escape(part) for part in phrase.split()
    ) + r"(?![A-Za-z])"
    return re.search(pattern, sentence, flags=re.IGNORECASE) is not None

with open(DATA_PATH, encoding="utf-8") as f:
    d = json.load(f)

errors = []
sec = next((s for s in d["sections"] if s.get("name") == "大問2"), None)
if not sec:
    errors.append("section 大問2 not found")
    print(f"errors={len(errors)}")
    for e in errors:
        print(" ", e)
    sys.exit(1)

if sec["type"] != "passage-fill":
    errors.append(f"expected passage-fill, got {sec['type']}")
if len(sec["passages"]) != 2:
    errors.append(f"expected 2 passages, got {len(sec['passages'])}")

for pa in sec["passages"]:
    for key in ("label", "title", "paragraphs", "translations", "sentencePairs"):
        if key not in pa or not pa[key]:
            errors.append(f"passage {pa.get('label')}: missing {key}")
    if len(pa["paragraphs"]) != len(pa["translations"]):
        errors.append(f"passage {pa.get('label')}: paragraphs/translations mismatch")
    pairs = pa.get("sentencePairs", [])
    if len(pairs) != EXPECTED_PAIR_COUNTS.get(pa.get("label")):
        errors.append(f"passage {pa.get('label')}: incomplete sentencePairs ({len(pairs)})")
    pair_english = []
    for pair_index, pair in enumerate(pairs, 1):
        pair_name = f"passage {pa.get('label')} pair {pair_index}"
        if not isinstance(pair, list) or len(pair) != 4:
            errors.append(f"{pair_name}: expected 4 elements, got {len(pair) if isinstance(pair, list) else type(pair).__name__}")
            continue
        if any(not isinstance(value, str) or not value.strip() for value in pair):
            errors.append(f"{pair_name}: all 4 elements must be non-empty strings")
            continue

        sentence, _translation, slash, main_verb = pair
        pair_english.append(sentence)
        segments = slash.split("||")
        if len(segments) < 2:
            errors.append(f"{pair_name}: slash reading must contain at least 2 meaning units")
        slash_english = []
        for segment_index, segment in enumerate(segments, 1):
            if "|" not in segment:
                errors.append(f"{pair_name}: slash segment {segment_index} has no English/Japanese separator")
                continue
            english, japanese = segment.split("|", 1)
            if not norm(english) or not norm(japanese):
                errors.append(f"{pair_name}: slash segment {segment_index} has an empty side")
                continue
            slash_english.append(english)
        if norm(" ".join(slash_english)) != norm(sentence):
            errors.append(f"{pair_name}: slash English does not reconstruct the sentence")
        if not phrase_exists(sentence, main_verb):
            errors.append(f"{pair_name}: main verb '{main_verb}' is not present in the sentence")

    if norm(" ".join(pair_english)) != norm(" ".join(pa["paragraphs"])):
        errors.append(f"passage {pa.get('label')}: sentencePairs do not cover full text")
    source_blanks = sorted(int(x) for x in re.findall(r"\(\s*(\d+)\s*\)", " ".join(pa["paragraphs"])))
    translation_blanks = sorted(int(x) for x in re.findall(r"\(\s*(\d+)\s*\)", " ".join(pa["translations"])))
    if source_blanks != translation_blanks:
        errors.append(f"passage {pa.get('label')}: translation blanks mismatch")

all_qs = [q for pa in sec["passages"] for q in pa["questions"]]
for q in all_qs:
    n = q["number"]
    if q["answer"] != EXPECTED[n]:
        errors.append(f"Q{n}: answer {q['answer']} != expected {EXPECTED[n]}")
    for key in ("choices", "choiceTranslations", "choiceAnalysis", "sourceEvidence"):
        if key not in q or (key != "sourceEvidence" and len(q[key]) != 4):
            errors.append(f"Q{n}: bad {key}")
    if not q.get("sourceEvidence"):
        errors.append(f"Q{n}: missing sourceEvidence")
    if "grammar" not in q or not q["grammar"]:
        errors.append(f"Q{n}: missing grammar")
    for i, ca in enumerate(q["choiceAnalysis"]):
        if ca.lstrip().startswith(("✅", "❌", "○", "×")):
            errors.append(f"Q{n}: choice {i+1} has forbidden leading marker")
        if i + 1 == q["answer"]:
            if ca.count("→正解。💡") != 1:
                errors.append(f"Q{n}: correct choice {i+1} missing →正解。💡")
        elif "→正解" in ca:
            errors.append(f"Q{n}: wrong choice {i+1} contains correct marker")

by_number = {q["number"]: q for q in all_qs}
if not any("She protected passengers" in evidence for evidence in by_number[20]["sourceEvidence"]):
    errors.append("Q20: sourceEvidence does not include the method being summarized")
serialized = json.dumps(sec, ensure_ascii=False)
for stale in ("恐怖はすぐに脳に反応させ", "農村の村", "移動中の公共の読書"):
    if stale in serialized:
        errors.append(f"stale translation remains: {stale}")

print(f"section2 passages=2 questions={len(all_qs)} errors={len(errors)}")
for e in errors:
    print(" ", e)
if errors:
    sys.exit(1)
print("OK: section2 (6 questions) verified")

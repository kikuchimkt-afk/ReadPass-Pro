# -*- coding: utf-8 -*-
"""2026-1-sat 3級 vocabulary 検証"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade3", "2026-1-sat",
)
DATA = os.path.join(BASE, "data.json")

d = json.load(open(DATA, encoding="utf-8"))
errors = []
vocab = d.get("vocabulary", [])
EXPECTED_WORDS = [
    "kite", "pass", "boring", "tired", "exercise",
    "market", "college", "take care of", "himself", "wait for",
    "feel", "look around", "painted", "taught", "to practice",
    "help", "ice-skating", "wear", "stomachache", "say hello to",
    "ingredients", "vegetables", "website",
    "performance", "practiced", "nervous", "comedy",
    "indoors", "championships", "athlete",
]

EXAMPLE_FORMS = {
    # 見出し語は原形、出典文は過去形。出典文を改変せず活用形を許容する。
    "look around": ("look around", "looks around", "looked around", "looking around"),
}

if len(vocab) != 30:
    errors.append(f"vocabulary count {len(vocab)} != 30")
if [item.get("word") for item in vocab] != EXPECTED_WORDS:
    errors.append("vocabulary words/order mismatch")

meanings = []
for i, v in enumerate(vocab):
    for key in (
        "word", "meaning", "pos", "level", "source",
        "example", "distractors", "wordAudio",
    ):
        if not v.get(key):
            errors.append(f"vocab[{i + 1}] missing {key}")
    if len(v.get("distractors", [])) != 3:
        errors.append(f"vocab[{i + 1}] distractors != 3")
    if v.get("level") != "3級":
        errors.append(f"vocab[{i + 1}] level != 3級")
    m = v.get("meaning", "")
    if m in meanings:
        errors.append(f"duplicate meaning: {m}")
    meanings.append(m)
    if m in v.get("distractors", []):
        errors.append(f"vocab[{i + 1}] correct meaning in distractors")
    word = v.get("word", "").lower()
    example = v.get("example", "").lower()
    forms = EXAMPLE_FORMS.get(word, (word,))
    if not any(form in example for form in forms):
        errors.append(f"vocab[{i + 1}] word absent from example")
    audio = v.get("wordAudio", "")
    if audio:
        path = os.path.join(BASE, audio.replace("/", os.sep))
        if not os.path.isfile(path) or os.path.getsize(path) < 500:
            errors.append(f"vocab[{i + 1}] missing audio: {audio}")
    else:
        errors.append(f"vocab[{i + 1}] no wordAudio")

source_counts = {}
for item in vocab:
    source_counts[item.get("source")] = source_counts.get(item.get("source"), 0) + 1
if source_counts != {"大問1": 15, "大問2": 5, "大問3A": 3, "大問3B": 4, "大問3C": 3}:
    errors.append(f"bad source counts: {source_counts}")

known = {item.get("word"): item for item in vocab}
if known.get("college", {}).get("meaning") != "大学":
    errors.append("college meaning mismatch")
if known.get("himself", {}).get("meaning") != "彼自身（by himself で「彼一人で」）":
    errors.append("himself meaning mismatch")
if known.get("wait for", {}).get("meaning") != "待つ（for＋時間で期間）":
    errors.append("wait for meaning mismatch")
if known.get("wear", {}).get("meaning") != "身につける（帽子をかぶる）":
    errors.append("wear meaning mismatch")

print(f"errors={len(errors)}")
for e in errors:
    print(" ", e)
if errors:
    sys.exit(1)
print("OK: 30 vocabulary items with audio")

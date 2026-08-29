# -*- coding: utf-8 -*-
"""Verify 2026-1-sat grade4 vocabulary content, provenance, and audio."""
import json
import os
import sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")

DATA_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade4", "2026-1-sat",
)
DATA_PATH = os.path.join(DATA_DIR, "data.json")

EXPECTED_SOURCES = {
    "大問1": 15, "大問2": 5, "大問3": 5,
    "大問4A": 1, "大問4B": 2, "大問4C": 2,
}


def audio_ok(rel):
    path = os.path.join(DATA_DIR, (rel or "").replace("/", os.sep))
    return bool(rel) and os.path.isfile(path) and os.path.getsize(path) >= 500


d = json.load(open(DATA_PATH, encoding="utf-8"))
vocabulary = d.get("vocabulary", [])
errors = []

if len(vocabulary) != 30:
    errors.append(f"vocabulary count {len(vocabulary)} != 30")

sources = Counter()
meanings = set()
for index, item in enumerate(vocabulary, 1):
    for key in (
        "word", "meaning", "pos", "level", "source", "example",
        "distractors", "wordAudio", "exampleAudio",
    ):
        if not item.get(key):
            errors.append(f"vocab[{index}]: missing {key}")
    if item.get("level") != "4級":
        errors.append(f"{item.get('word')}: level != 4級")
    if len(item.get("distractors", [])) != 3:
        errors.append(f"{item.get('word')}: distractors != 3")
    if item.get("meaning") in item.get("distractors", []):
        errors.append(f"{item.get('word')}: distractors contain correct meaning")
    if item.get("meaning") in meanings:
        errors.append(f"duplicate meaning: {item.get('meaning')}")
    meanings.add(item.get("meaning"))
    sources[item.get("source")] += 1
    for field in ("wordAudio", "exampleAudio"):
        if not audio_ok(item.get(field)):
            errors.append(f"{item.get('word')}: missing {field} {item.get(field)}")

if dict(sources) != EXPECTED_SOURCES:
    errors.append(f"source counts {dict(sources)} != {EXPECTED_SOURCES}")

playing = next((item for item in vocabulary if item.get("word") == "playing"), {})
if playing.get("meaning") != "（ゲームなどを）すること" or playing.get("pos") != "動名詞":
    errors.append("playing must be explained as a gerund in stop playing")

print(f"vocabulary={len(vocabulary)} errors={len(errors)}")
for error in errors:
    print(" ", error)
if errors:
    sys.exit(1)
print("OK: vocabulary 30 items, provenance, meanings, and audio verified")

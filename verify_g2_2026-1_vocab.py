# -*- coding: utf-8 -*-
"""Verify 2026-1 grade2 (本会場) vocabulary structure."""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade2", "2026-1",
)
DATA = os.path.join(BASE, "data.json")

d = json.load(open(DATA, encoding="utf-8"))
errors = []
vocab = d.get("vocabulary", [])

EXPECTED_WORDS = [
    "bride", "lawyer", "surgeon", "globe", "branch", "difficulty", "glory",
    "tendency", "discrimination", "foster", "typical", "gradual", "weep",
    "occur", "illustrate", "occupy", "barely", "frown", "as a general rule",
    "on his own", "go along with", "a series of", "in other words",
    "distinct from", "lay off", "rural", "literacy", "motivate", "costume",
    "rumor", "dramatic", "community", "spread", "superhero", "creative",
    "starve", "emotion", "dangerous", "breathing", "muscle", "fight-or-flight",
    "fascinated", "intensely", "overwhelming", "mechanism", "treatment",
    "facility", "athletic", "coworker", "access", "suitable", "wealthy",
    "adventure", "tutor", "proposal", "perceive", "individuality",
    "intellectual", "impact", "indirectly", "economics",
]
EXPECTED = len(EXPECTED_WORDS)
CRITICAL = {
    "access": ("（場所などに）行く、利用する", "動詞"),
    "tutor": ("個別に教える、家庭教師として教える", "動詞"),
}
if len(vocab) != EXPECTED:
    errors.append(f"vocabulary count {len(vocab)} != {EXPECTED}")
if [item.get("word") for item in vocab] != EXPECTED_WORDS:
    errors.append("vocabulary words/order differ from audited list")

meanings = []
sources = {"大問1": 0, "大問2A": 0, "大問2B": 0, "大問3A": 0, "大問3B": 0}
for i, v in enumerate(vocab):
    for key in ("word", "meaning", "pos", "level", "example", "distractors", "source"):
        if not v.get(key):
            errors.append(f"vocab[{i}]: missing {key}")
    if len(v.get("distractors", [])) != 3:
        errors.append(f"{v.get('word')}: distractors != 3")
    m = v.get("meaning", "")
    if m in meanings:
        errors.append(f"duplicate meaning: {m} ({v.get('word')})")
    meanings.append(m)
    if m in v.get("distractors", []):
        errors.append(f"{v['word']}: distractors contain correct meaning")
    src = v.get("source", "")
    if src in sources:
        sources[src] += 1
    wa = v.get("wordAudio")
    expected_prefix = f"audio/vocab/w_{i + 1:03d}_"
    if not wa or not wa.startswith(expected_prefix):
        errors.append(f"{v.get('word')}: missing/misnumbered wordAudio")
    if wa:
        fp = os.path.join(BASE, wa.replace("/", os.sep))
        if not os.path.isfile(fp) or os.path.getsize(fp) < 500:
            errors.append(f"{v['word']}: missing audio {wa}")

expected_sources = {"大問1": 25, "大問2A": 11, "大問2B": 10, "大問3A": 5, "大問3B": 10}
for src, count in expected_sources.items():
    if sources.get(src, 0) != count:
        errors.append(f"{src}: {sources.get(src, 0)} words != {count}")

by_word = {item.get("word"): item for item in vocab}
for word, (meaning, pos) in CRITICAL.items():
    item = by_word.get(word, {})
    if (item.get("meaning"), item.get("pos")) != (meaning, pos):
        errors.append(f"{word}: audited meaning/pos regression")

print(f"vocabulary={len(vocab)} errors={len(errors)}")
for e in errors:
    print(" ", e)
if errors:
    sys.exit(1)
print(f"OK: {EXPECTED} vocabulary items verified")

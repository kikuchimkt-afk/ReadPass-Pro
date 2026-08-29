# -*- coding: utf-8 -*-
"""2026-1-sat 2級の語彙61件と音声参照を検証する。"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

BASE = Path(__file__).resolve().parent / "data" / "grade2" / "2026-1-sat"
data = json.loads((BASE / "data.json").read_text(encoding="utf-8"))
vocab = data["vocabulary"]

expected_words = [
    "incident", "argument", "outcome", "quantity", "sacrifice", "stir",
    "resemble", "favor", "cable", "appreciation", "preference", "scold",
    "detect", "estimate", "decline", "neglect", "patiently", "current",
    "up until now", "needless to say", "lose one's temper",
    "keep one's fingers crossed", "confident of", "keep to", "effect on",
    "effort", "surround", "trial", "permanently", "indicate", "observation",
    "urban", "improvement", "reflect", "community", "ban", "habitat",
    "creature", "absorb", "substance", "moisture", "eventually", "bark",
    "element", "maintain", "cycle", "manufacturing", "impress", "research",
    "permit", "consideration", "conveniently", "restore", "ancient", "collapse",
    "gradually", "investigation", "sculpture", "underwater", "explore", "ruins",
]
assert [item["word"] for item in vocab] == expected_words

for index, item in enumerate(vocab, 1):
    assert item["meaning"] and item["pos"] and item["example"]
    assert item["level"] == "2級"
    assert len(item["distractors"]) == len(set(item["distractors"])) == 3
    assert item["meaning"] not in item["distractors"]
    slug = re.sub(r"[^a-zA-Z0-9_]", "_", item["word"].lower()).strip("_")
    expected_ref = f"audio/vocab/w_{index:03d}_{slug}.mp3"
    assert item["wordAudio"] == expected_ref, (item["word"], item["wordAudio"], expected_ref)
    path = BASE / Path(expected_ref)
    assert path.is_file() and path.stat().st_size >= 500

by_word = {item["word"]: item for item in vocab}
assert by_word["favor"]["meaning"] == "好む、支持する"
assert by_word["keep to"]["meaning"] == "〜に従う、〜から離れない"
assert by_word["observation"]["meaning"] == "観察、意見"
assert by_word["underwater"]["pos"] == "形容詞"

print("OK: 61 vocabulary entries and deterministic word-audio references")

# -*- coding: utf-8 -*-
"""Strictly verify the 80-item Grade Pre-1 2026-2 vocabulary dataset.

wordAudio is optional until data/pre-grade1/2026-2/_gen_tts.py has been run;
pass --require-audio to also require every MP3 to exist.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent
DEFAULT_DATA_PATH = BASE_DIR / "data" / "pre-grade1" / "2026-2" / "data.json"

OFFICIAL_PART1_CHOICES = [
    ["restrain", "recharge", "resume", "reflect"],
    ["dizzy", "keen", "fussy", "bare"],
    ["dignity", "controversy", "monarchy", "itinerary"],
    ["confine", "inhibit", "familiarize", "seize"],
    ["diversion", "maneuver", "urgency", "contempt"],
    ["dwellings", "refuges", "prospects", "ornaments"],
    ["rugged", "clerical", "majestic", "apt"],
    ["loiter", "scratch", "mourn", "applaud"],
    ["preoccupied", "trespassed", "grated", "endorsed"],
    ["column", "succession", "inaction", "inspection"],
    ["soothing", "punctual", "clumsy", "idealistic"],
    ["peculiar", "conceited", "fragrant", "transparent"],
    ["distress", "referral", "detention", "prominence"],
    ["inheritance", "excerpt", "odor", "agenda"],
    ["hammer out", "jump in", "weed out", "step aside"],
    ["held against", "kept from", "grown into", "sailed through"],
    ["phase out", "swear by", "rub in", "run up"],
    ["set about", "took after", "brought down", "called on"],
]
READING_WORDS = [
    "malfunction",
    "viability",
    "savory",
    "receptor",
    "eligibility",
    "recession",
    "invasive species",
    "surveillance",
]
EXPECTED_WORDS = [word for choices in OFFICIAL_PART1_CHOICES for word in choices] + READING_WORDS
BASE_KEYS = {"word", "meaning", "pos", "level", "example", "distractors", "exampleJa"}
JAPANESE_RE = re.compile(r"[ぁ-んァ-ヶ一-龠]")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def nonempty_text(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def audio_slug(word: str) -> str:
    # Same rule as data/pre-grade1/2026-2/_gen_tts.py.
    return re.sub(r"[^a-zA-Z0-9_]", "_", word.lower()).strip("_")


def verify(data_path: Path, require_audio: bool = False) -> None:
    data = json.loads(data_path.read_text(encoding="utf-8"))
    vocabulary = data.get("vocabulary")
    require(isinstance(vocabulary, list), "top-level vocabulary must be a list")
    require(len(vocabulary) == 80, f"vocabulary must contain exactly 80 items, got {len(vocabulary)}")
    words = [item.get("word") for item in vocabulary]
    require(words == EXPECTED_WORDS, "vocabulary words/order differ from the 72 official choices + 8 reading terms")
    require(len({word.casefold() for word in words}) == 80, "vocabulary words are not unique")

    audio_count = 0
    for index, item in enumerate(vocabulary, start=1):
        word = item["word"]
        prefix = f"vocabulary[{index}] ({word})"
        keys = set(item)
        require(keys in (BASE_KEYS, BASE_KEYS | {"wordAudio"}), f"{prefix} keys differ: {sorted(keys)}")
        for field in ("meaning", "pos", "example", "exampleJa"):
            require(nonempty_text(item[field]), f"{prefix} {field} is empty")
        require(JAPANESE_RE.search(item["meaning"]) is not None, f"{prefix} meaning must be Japanese")
        require(JAPANESE_RE.search(item["exampleJa"]) is not None, f"{prefix} exampleJa must be Japanese")
        require(item["level"] == "準1級", f"{prefix} level must be 準1級")
        require(word.casefold() in item["example"].casefold(), f"{prefix} example must contain the registered form")

        distractors = item["distractors"]
        require(isinstance(distractors, list) and len(distractors) == 3, f"{prefix} needs three distractors")
        require(all(nonempty_text(value) for value in distractors), f"{prefix} has an empty distractor")
        require(len({value.strip() for value in distractors}) == 3, f"{prefix} distractors are not unique")
        require(item["meaning"].strip() not in {value.strip() for value in distractors}, f"{prefix} distractor equals the meaning")

        expected_audio = f"audio/vocab/w_{index:03d}_{audio_slug(word)}.mp3"
        if "wordAudio" in item:
            audio_count += 1
            require(item["wordAudio"] == expected_audio, f"{prefix} wordAudio differs: {item['wordAudio']!r}")
            require((data_path.parent / expected_audio).is_file(), f"{prefix} referenced audio file is missing")
        elif require_audio:
            raise AssertionError(f"{prefix} has no wordAudio (run _gen_tts.py)")

    require(audio_count in (0, 80), f"wordAudio is set on {audio_count}/80 items; rerun _gen_tts.py")
    print(f"vocabulary=80 wordAudio={audio_count}/80")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA_PATH)
    parser.add_argument("--require-audio", action="store_true", help="also require every word MP3")
    args = parser.parse_args()
    verify(args.data.resolve(), require_audio=args.require_audio)
    print(f"PASS: Grade Pre-1 2026-2 vocabulary verified ({args.data})")


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""Strictly verify the 80-item Grade Pre-1 2026-1 vocabulary dataset."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DEFAULT_DATA_PATH = BASE_DIR / "data" / "pre-grade1" / "2026-1" / "data.json"

OFFICIAL_PART1_CHOICES = [
    ["cemetery", "diagram", "equation", "forecast"],
    ["possessive", "horizontal", "redundant", "drastic"],
    ["haul", "envy", "subtract", "censor"],
    ["referral", "recipient", "bouncer", "successor"],
    ["triggering", "fabricating", "conserving", "renouncing"],
    ["ransom", "specimen", "cavity", "citation"],
    ["distortion", "generosity", "turbulence", "conjecture"],
    ["nutritious", "diverse", "barren", "coincidental"],
    ["slack", "sparse", "vast", "vital"],
    ["descendant", "triumph", "emission", "deficiency"],
    ["flourishing", "pledging", "scattering", "drooping"],
    ["reptile", "glacier", "blockade", "portfolio"],
    ["abbreviate", "attest", "carve", "yield"],
    ["radiate", "magnify", "extract", "impart"],
    ["sank in", "let out", "went under", "lived off"],
    ["add up", "read into", "take off", "fall out"],
    ["slip away", "tear up", "drop out", "follow up"],
    ["fed off", "burnt out", "fell through", "ate up"],
]
READING_WORDS = [
    "birth order",
    "stereotype",
    "virtual reconstruction",
    "sovereign",
    "irrigation canal",
    "cuneiform",
    "genetic manipulation",
    "animal uplift",
]
EXPECTED_WORDS = [word for choices in OFFICIAL_PART1_CHOICES for word in choices] + READING_WORDS

VOCAB_KEYS = {
    "word",
    "meaning",
    "pos",
    "level",
    "example",
    "distractors",
    "wordAudio",
    "exampleJa",
}
AUDIO_RE = re.compile(r"^audio/vocab/w_\d{3}_[a-z0-9_]+\.mp3$")
CRITICAL_CARDS = {
    "descendant": {
        "meaning": "子孫",
        "distractors": ["祖先", "勝利", "欠乏"],
    },
    "emission": {
        "example": "The factory reduced its carbon emissions through new technology.",
    },
    "virtual reconstruction": {
        "exampleJa": "仮想復元は、古代の宮殿がどのような姿だった可能性があるかを示している。",
    },
    "sovereign": {
        "meaning": "主権を有する・独立した／君主・主権者",
        "pos": "形容詞・名詞",
        "example": "A sovereign nation has authority over its own territory.",
        "exampleJa": "主権国家は自国の領土に対する統治権を持つ。",
        "distractors": ["従属した", "一時的な", "地方の"],
    },
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def nonempty_text(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def slugify(word: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", word.casefold()).strip("_")


def verify(data_path: Path, require_audio: bool = False) -> None:
    require(data_path.is_file(), f"data file not found: {data_path}")
    with data_path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)

    vocabulary = data.get("vocabulary")
    require(isinstance(vocabulary, list), "top-level vocabulary must be a list")
    require(len(vocabulary) == 80, f"vocabulary must contain exactly 80 items, got {len(vocabulary)}")
    words = [item.get("word") if isinstance(item, dict) else None for item in vocabulary]
    require(words == EXPECTED_WORDS, "vocabulary words/order differ from official 72 choices + required 8 reading terms")
    require(len({word.casefold() for word in words}) == 80, "vocabulary words are not case-insensitively unique")

    audio_paths: list[str] = []
    data_dir = data_path.parent
    for index, (item, expected_word) in enumerate(zip(vocabulary, EXPECTED_WORDS), start=1):
        prefix = f"vocabulary[{index}] ({expected_word})"
        require(isinstance(item, dict), f"{prefix} must be an object")
        require(set(item) == VOCAB_KEYS, f"{prefix} keys differ: {sorted(item)}")
        require(item["word"] == expected_word, f"{prefix} word differs")
        for field in ("meaning", "pos", "example", "exampleJa", "wordAudio"):
            require(nonempty_text(item[field]), f"{prefix} {field} is empty")
        require(item["level"] == "準1級", f"{prefix} level must be 準1級")
        require(
            expected_word.casefold() in item["example"].casefold(),
            f"{prefix} example must contain the registered word/phrase",
        )

        distractors = item["distractors"]
        require(isinstance(distractors, list) and len(distractors) == 3, f"{prefix} needs three distractors")
        require(all(nonempty_text(value) for value in distractors), f"{prefix} has an empty distractor")
        require(
            len({value.strip().casefold() for value in distractors}) == 3,
            f"{prefix} distractors are not unique",
        )
        require(
            item["meaning"].strip().casefold() not in {value.strip().casefold() for value in distractors},
            f"{prefix} distractor duplicates the correct meaning",
        )

        expected_audio = f"audio/vocab/w_{index:03d}_{slugify(expected_word)}.mp3"
        require(item["wordAudio"] == expected_audio, f"{prefix} audio path differs: {item['wordAudio']!r}")
        require(AUDIO_RE.fullmatch(item["wordAudio"]) is not None, f"{prefix} audio path format is invalid")
        audio_paths.append(item["wordAudio"])
        if require_audio:
            require((data_dir / item["wordAudio"]).is_file(), f"{prefix} audio file is missing")

    require(len(set(audio_paths)) == 80, "wordAudio paths are not unique")
    by_word = {item["word"]: item for item in vocabulary}
    for word, expected_fields in CRITICAL_CARDS.items():
        for field, expected in expected_fields.items():
            require(
                by_word[word][field] == expected,
                f"critical vocabulary meaning check failed: {word}.{field}",
            )
    require(
        [word for choices in OFFICIAL_PART1_CHOICES for word in choices] == EXPECTED_WORDS[:72],
        "internal official Part 1 snapshot is not 72 ordered choices",
    )
    require(EXPECTED_WORDS[72:] == READING_WORDS, "required reading vocabulary order differs")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA_PATH)
    parser.add_argument(
        "--require-audio",
        action="store_true",
        help="also require every referenced MP3 to exist",
    )
    args = parser.parse_args()
    verify(args.data.resolve(), require_audio=args.require_audio)
    suffix = " with audio files" if args.require_audio else " (audio references only)"
    print(f"PASS: Grade Pre-1 2026-1 vocabulary verified{suffix} ({args.data})")


if __name__ == "__main__":
    main()

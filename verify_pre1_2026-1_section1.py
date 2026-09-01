# -*- coding: utf-8 -*-
"""Strictly verify the official 2026-1 Grade Pre-1 Part 1 snapshot and schema."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DEFAULT_DATA_PATH = BASE_DIR / "data" / "pre-grade1" / "2026-1" / "data.json"

EXPECTED = [
    (
        1,
        "In order to illustrate how a cell functions, the biology teacher drew a detailed ( 1 ) on the board showing all of its parts.",
        ["cemetery", "diagram", "equation", "forecast"],
        2,
    ),
    (
        2,
        "A: I think this sentence in your essay is ( 2 ).\nB: Oh, you're right. It's almost the same as what I said in the previous paragraph.",
        ["possessive", "horizontal", "redundant", "drastic"],
        3,
    ),
    (
        3,
        "In some countries, governments ( 3 ) the media in order to prevent criticism of them from being published.",
        ["haul", "envy", "subtract", "censor"],
        4,
    ),
    (
        4,
        "The scholarship is only available to students who meet its requirements. A ( 4 ) must have excellent grades and be from a low-income background.",
        ["referral", "recipient", "bouncer", "successor"],
        2,
    ),
    (
        5,
        "The scientist was accused of ( 5 ) his data after experts attempted to copy his experiments but were unable to produce the same results.",
        ["triggering", "fabricating", "conserving", "renouncing"],
        2,
    ),
    (
        6,
        "Last week, a police officer stopped Javier and gave him a traffic ( 6 ) for driving faster than the speed limit.",
        ["ransom", "specimen", "cavity", "citation"],
        4,
    ),
    (
        7,
        "Because some ( 7 ) was expected, the captain turned on the seat belt sign and asked all the passengers to return to their seats.",
        ["distortion", "generosity", "turbulence", "conjecture"],
        3,
    ),
    (
        8,
        "After several years with almost no rain, the area became a ( 8 ) wasteland where no trees or other plants could survive.",
        ["nutritious", "diverse", "barren", "coincidental"],
        3,
    ),
    (
        9,
        "When Simon pulled on the rope, it suddenly became ( 9 ). He realized that it must have come untied at the other end.",
        ["slack", "sparse", "vast", "vital"],
        1,
    ),
    (
        10,
        "The patient was diagnosed with a vitamin ( 10 ). The doctor said she would need to take supplements until her vitamin levels were normal again.",
        ["descendant", "triumph", "emission", "deficiency"],
        4,
    ),
    (
        11,
        "Tanya seemed shy and nervous when she entered her new school, but she is now ( 11 ) socially and has made a lot of friends.",
        ["flourishing", "pledging", "scattering", "drooping"],
        1,
    ),
    (
        12,
        "The art student showed her ( 12 ) to the gallery owner. It contained samples of her paintings, drawings, and photographs.",
        ["reptile", "glacier", "blockade", "portfolio"],
        4,
    ),
    (
        13,
        "The teacher asked the student to ( 13 ) his essay. She said it should be about half the length it was.",
        ["abbreviate", "attest", "carve", "yield"],
        1,
    ),
    (
        14,
        "The patient was in so much pain that the dentist had no choice but to ( 14 ) the patient's damaged tooth.",
        ["radiate", "magnify", "extract", "impart"],
        3,
    ),
    (
        15,
        "The company was badly affected by the financial crisis and nearly ( 15 ), but it has now recovered and is making a profit again.",
        ["sank in", "let out", "went under", "lived off"],
        3,
    ),
    (
        16,
        "The police officer became suspicious of the man because his story did not ( 16 ). He was later found to have lied to the police.",
        ["add up", "read into", "take off", "fall out"],
        1,
    ),
    (
        17,
        "The patient tried to ( 17 ) from the hospital without anyone noticing, but the nurse saw him and stopped him.",
        ["slip away", "tear up", "drop out", "follow up"],
        1,
    ),
    (
        18,
        "A: Our meeting prep took longer than expected.\nB: Yeah, the budget review really ( 18 ) most of our afternoon.",
        ["fed off", "burnt out", "fell through", "ate up"],
        4,
    ),
]

SECTION_KEYS = {"name", "nameEn", "type", "instruction", "questions"}
QUESTION_KEYS = {
    "number",
    "text",
    "translation",
    "choices",
    "answer",
    "choiceAnalysis",
    "grammar",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def nonempty_text(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def verify(data_path: Path) -> None:
    require(data_path.is_file(), f"data file not found: {data_path}")
    with data_path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)

    sections = data.get("sections")
    require(isinstance(sections, list) and sections, "top-level sections must be a nonempty list")
    section = sections[0]
    require(isinstance(section, dict), "sections[0] must be an object")
    require(set(section) == SECTION_KEYS, f"Part 1 section keys differ: {sorted(section)}")
    require(section["name"] == "大問1", "Part 1 name must be 大問1")
    require(section["nameEn"] == "Part 1", "Part 1 nameEn must be Part 1")
    require(section["type"] == "vocabulary", "Part 1 type must be vocabulary")
    require(nonempty_text(section["instruction"]), "Part 1 instruction is empty")

    questions = section.get("questions")
    require(isinstance(questions, list), "Part 1 questions must be a list")
    require(len(questions) == 18, f"Part 1 must contain 18 questions, got {len(questions)}")

    for index, (number, text, choices, answer) in enumerate(EXPECTED):
        question = questions[index]
        prefix = f"Q{number}"
        require(isinstance(question, dict), f"{prefix} must be an object")
        require(set(question) == QUESTION_KEYS, f"{prefix} keys differ: {sorted(question)}")
        require(question["number"] == number, f"{prefix} number differs")
        require(question["text"] == text, f"{prefix} official text differs")
        require(question["choices"] == choices, f"{prefix} official choices differ")
        require(question["answer"] == answer, f"{prefix} official answer differs")
        require(len(set(question["choices"])) == 4, f"{prefix} choices are not unique")
        require(nonempty_text(question["translation"]), f"{prefix} translation is empty")
        blank = f"( {number} )"
        require(question["text"].count(blank) == 1, f"{prefix} English must contain {blank!r} exactly once")
        require(
            question["translation"].count(blank) == 1,
            f"{prefix} translation must contain {blank!r} exactly once",
        )
        require(
            all(f"( {other} )" not in question["translation"] for other in range(1, 19) if other != number),
            f"{prefix} translation contains another question's numbered blank",
        )
        require(nonempty_text(question["grammar"]), f"{prefix} grammar is empty")
        require(question["grammar"].startswith("💡"), f"{prefix} grammar must start with 💡")

        analyses = question["choiceAnalysis"]
        require(isinstance(analyses, list) and len(analyses) == 4, f"{prefix} needs four analyses")
        for choice_index, (choice, analysis) in enumerate(zip(choices, analyses), start=1):
            require(nonempty_text(analysis), f"{prefix} choice {choice_index} analysis is empty")
            require(
                choice.casefold() in analysis.casefold(),
                f"{prefix} choice {choice_index} analysis does not name '{choice}'",
            )
            if choice_index == answer:
                require(analysis.startswith("✅"), f"{prefix} correct analysis must start with ✅")
                require("→ 正解。💡" in analysis, f"{prefix} correct analysis lacks '→ 正解。💡'")
                require(not analysis.startswith("❌"), f"{prefix} correct analysis starts with ❌")
            else:
                require(analysis.startswith("❌"), f"{prefix} wrong choice {choice_index} must start with ❌")
                require("✅" not in analysis, f"{prefix} wrong choice {choice_index} contains ✅")

        require(
            sum(item.startswith("✅") for item in analyses) == 1,
            f"{prefix} must have exactly one ✅ analysis",
        )
        require(
            sum(item.startswith("❌") for item in analyses) == 3,
            f"{prefix} must have exactly three ❌ analyses",
        )

    require([question["number"] for question in questions] == list(range(1, 19)), "Q1-Q18 order differs")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA_PATH)
    args = parser.parse_args()
    verify(args.data.resolve())
    print(f"PASS: official Grade Pre-1 2026-1 Part 1 verified ({args.data})")


if __name__ == "__main__":
    main()

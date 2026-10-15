"""Build ReadPass data for EIKEN Grade Pre-2 2024-3 Saturday sub-venue.

The 2025-01-25 (土曜準会場) paper uses the same 2024 format as 2024-1-sat:
15 + 5 questions, one fill-in passage, an e-mail and a reading passage.
Content lives in three sibling scripts loaded by path (no package needed):
  gen_pre2_2024-3-sat_part12.py     Parts 1-2
  gen_pre2_2024-3-sat_passages.py   Parts 3-4
  gen_pre2_2024-3-sat_materials.py  vocabulary and lesson plan
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
from pathlib import Path
from types import SimpleNamespace


ROOT = Path(__file__).resolve().parent
DEFAULT_OUTPUT = ROOT / "data" / "grade-pre2" / "2024-3-sat" / "data.json"
# 準２級_解答.pdf (2024年度 第3回, 1月25日（土）実施).
OFFICIAL_ANSWERS = [
    3, 2, 2, 2, 1, 2, 3, 1, 3, 4,
    4, 2, 4, 1, 4, 2, 1, 3, 1, 4,
    1, 3, 2, 3, 2, 4, 4, 3, 1,
]


def _analyses(number: int, answer: int, explanations: list[str]) -> list[str]:
    if len(explanations) != 4:
        raise ValueError("Every question needs four choice explanations")
    if number <= 15:
        return [
            ("✅ " if index == answer else "❌ ") + explanation
            for index, explanation in enumerate(explanations, start=1)
        ]

    analyses = []
    for index, explanation in enumerate(explanations, start=1):
        if index == answer:
            head, separator, detail = explanation.partition("。")
            explanation = f"{head}→正解。💡{detail}" if separator else f"{explanation}→正解。💡"
        analyses.append(explanation)
    return analyses


def question(
    number: int,
    text: str,
    translation: str,
    choices: list[str],
    choice_translations: list[str],
    answer: int,
    explanations: list[str],
    grammar: str,
) -> dict:
    if len(choices) != 4 or len(choice_translations) != 4:
        raise ValueError(f"Question {number} must have four choices")
    return {
        "number": number,
        "text": text,
        "translation": translation,
        "choices": choices,
        "choiceTranslations": choice_translations,
        "answer": answer,
        "choiceAnalysis": _analyses(number, answer, explanations),
        "grammar": grammar,
    }


def passage_question(
    number: int,
    prompt: str | None,
    prompt_translation: str | None,
    choices: list[str],
    choice_translations: list[str],
    answer: int,
    explanations: list[str],
    grammar: str,
) -> dict:
    if len(choices) != 4 or len(choice_translations) != 4:
        raise ValueError(f"Question {number} must have four choices")
    item = {
        "number": number,
        "choices": choices,
        "choiceTranslations": choice_translations,
        "answer": answer,
        "choiceAnalysis": _analyses(number, answer, explanations),
        "grammar": grammar,
    }
    if prompt is not None:
        item = {
            "number": number,
            "question": prompt,
            "questionTranslation": prompt_translation,
            **{key: value for key, value in item.items() if key != "number"},
        }
    return item


def audio_slug(word: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", word.lower()).strip("_")


def vocab(
    index: int,
    word: str,
    meaning: str,
    pos: str,
    example: str,
    distractors: list[str],
) -> dict:
    if len(distractors) != 3:
        raise ValueError(f"Vocabulary {index} must have three distractors")
    return {
        "word": word,
        "meaning": meaning,
        "pos": pos,
        "level": "準2級",
        "example": example,
        "distractors": distractors,
        "wordAudio": f"audio/vocab/w_{index:03d}_{audio_slug(word)}.mp3",
    }


FOCUS_COLORS = {
    "fp1": "#4f8cff",
    "fp2": "#f472b6",
    "fp3": "#34d399",
    "fp4": "#fbbf24",
    "fp5": "#f59e0b",
}


def focus_point(
    point_id: str,
    title: str,
    subtitle: str,
    explanation: str,
    source_quote: str,
    source_location: str,
    examples: list[dict],
    passage_en: str,
    passage_ja: str,
    patterns: list[str],
    label: str,
    questions: list[dict],
) -> dict:
    return {
        "id": point_id,
        "title": title,
        "subtitle": subtitle,
        "explanation": explanation,
        "sourceQuote": source_quote,
        "sourceLocation": source_location,
        "examples": examples,
        "practicePassage": {
            "en": passage_en,
            "ja": passage_ja,
            "audioFile": f"audio/practice_pp{int(point_id[2:])}.mp3",
        },
        "highlightPatterns": patterns,
        "highlightColor": FOCUS_COLORS[point_id],
        "highlightLabel": label,
        "practiceQuestions": questions,
    }


HELPERS = SimpleNamespace(
    question=question,
    passage_question=passage_question,
    vocab=vocab,
    focus_point=focus_point,
)


def _load(filename: str):
    path = ROOT / filename
    spec = importlib.util.spec_from_file_location(path.stem.replace("-", "_"), path)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def build_sections() -> list[dict]:
    part12 = _load("gen_pre2_2024-3-sat_part12.py")
    passages = _load("gen_pre2_2024-3-sat_passages.py")
    return [
        {
            "name": "大問1",
            "nameEn": "Part 1",
            "type": "vocabulary",
            "instruction": "次の(1)から(15)までの(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選びなさい。",
            "questions": part12.build_part1(HELPERS),
        },
        {
            "name": "大問2",
            "nameEn": "Part 2",
            "type": "vocabulary",
            "instruction": "次の四つの会話文を完成させるために，(16)から(20)に入るものとして最も適切なものを1，2，3，4の中から一つ選びなさい。",
            "questions": part12.build_part2(HELPERS),
        },
        passages.build_part3(HELPERS),
        passages.build_part4(HELPERS),
    ]


def build_vocabulary() -> list[dict]:
    return _load("gen_pre2_2024-3-sat_materials.py").build_vocabulary(HELPERS)


def build_lesson_plan() -> dict:
    return _load("gen_pre2_2024-3-sat_materials.py").build_lesson_plan(HELPERS)


def build_data() -> dict:
    data = {
        "grade": "準2級",
        "year": "2024",
        "session": "3",
        "title": "2024年度 第3回（土曜準会場） 英語資格検定準2級 リーディング",
        "vocabulary": build_vocabulary(),
        "sections": build_sections(),
        "lessonPlan": build_lesson_plan(),
    }
    answers: list[int] = []
    numbers: list[int] = []
    for section in data["sections"]:
        for item in section.get("questions", []):
            numbers.append(item["number"])
            answers.append(item["answer"])
        for passage in section.get("passages", []):
            for item in passage["questions"]:
                numbers.append(item["number"])
                answers.append(item["answer"])
    if numbers != list(range(1, 30)):
        raise ValueError(f"Unexpected question numbers: {numbers}")
    if answers != OFFICIAL_ANSWERS:
        raise ValueError(f"Official answer mismatch: {answers}")
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    data = build_data()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, ensure_ascii=False, indent=4) + "\n", encoding="utf-8")
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""Strictly verify Part 2 of the 2026-1 Grade Pre-1 reading data."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "data" / "pre-grade1" / "2026-1" / "data.json"
TOP_PATH = ROOT / "top.js"

EXPECTED_META = {
    "name": "大問2",
    "nameEn": "Part 2",
    "type": "passage-fill",
    "instruction": "次の英文A，Bを読み，その文意にそって(19)から(24)までの(　)に入れるのに最も適切なものを選びなさい。",
}

EXPECTED_PASSAGES = {
    "A": {
        "title": "Birth Order",
        "paragraphs": [
            "The idea that the order in which children are born can have a lasting and dramatic effect on their personalities was developed by the Austrian psychologist Alfred Adler more than a century ago. ( 19 ), Adler believed that firstborns tended to be responsible yet anxious, that middle children were more diplomatic, and that youngest siblings were more rebellious. Today, the theory is featured in many parenting books.",
            "Extensive research has been conducted on birth order. One notable study, for example, examined thousands of teenagers and found that it did lead to some measurable differences. Eldest siblings, for instance, differed from others in terms of things like responsibility and anxiety. However, while firstborns were, as expected, found to be more responsible, they tended to be less anxious, which did not fit the stereotype. In addition to such contradictions, the differences for every birth position were extremely slight. According to the researchers, associations between birth order and a person’s character ( 20 ).",
            "As children grow, there are obvious differences in everything from maturity to rebelliousness. Parents often observe that younger children have less self-control and disobey them more than older children. However, it is also true that this ( 21 ). It therefore seems that what many people take to be birth order affecting personality is really just the temporary stages of development their children are going through. Personality, experts tell us, is determined more by things like genetics and one’s living environment than it is by the order in which children were born.",
        ],
        "pairCount": 14,
    },
    "B": {
        "title": "Digital Nations",
        "paragraphs": [
            "The small Polynesian island nation of Tuvalu is in danger of disappearing forever. Scientists have predicted that, decades from now, living in Tuvalu will become impossible due to rising sea levels caused by climate change. When that happens, the only option for Tuvaluans will be to move elsewhere. ( 22 ), the preparations for doing this are already in place. Tuvalu has negotiated an agreement with Australia that allows a certain number of its people to emigrate there every year.",
            "Tuvalu’s government is doing what it can to save its nation. Sea barriers have been built, and work is underway to create an area of raised land that will provide a habitable area for residents. However, the government knows these measures may be useless in the long term. So, it ( 23 ). A few years ago, it set up the Future Now Project. Part of this project involves creating a virtual reconstruction of the nation. Along with preserving geographical features, the project aims to create a digital record of Tuvalu’s people and customs.",
            "Some critics claim the resources required for the project could be better used to tackle climate change. In response, Tuvalu’s government points out that the project ( 24 ). The current international treaty states that sovereign nations must have a “defined territory” and a “permanent population.” Tuvalu’s government hopes to pioneer a new form of statehood that allows it to continue to exist by meeting these criteria in a virtual form. This could also help to ensure the survival of other island nations facing similar threats from the sea.",
        ],
        "pairCount": 17,
    },
}

EXPECTED_QUESTIONS = {
    19: {
        "choices": ["Consequently", "Specifically", "Nonetheless", "Otherwise"],
        "answer": 2,
    },
    20: {
        "choices": [
            "have less effect on youngest siblings",
            "become stronger as children age",
            "are mostly meaningless",
            "should be more widely accepted",
        ],
        "answer": 3,
    },
    21: {
        "choices": [
            "tends to fade with time",
            "is related mainly to intelligence",
            "affects their success as adults",
            "is due to parenting styles",
        ],
        "answer": 1,
    },
    22: {
        "choices": ["On the contrary", "Despite this", "Similarly", "In fact"],
        "answer": 4,
    },
    23: {
        "choices": [
            "is turning to technology instead",
            "is planning to construct stronger defenses",
            "has stopped all current projects",
            "has requested help from other nations",
        ],
        "answer": 1,
    },
    24: {
        "choices": [
            "is no longer necessary",
            "should not take long to complete",
            "will not only benefit Tuvalu",
            "has no clear purpose",
        ],
        "answer": 3,
    },
}

SECTION_KEYS = {"name", "nameEn", "type", "instruction", "passages"}
PASSAGE_KEYS = {
    "label",
    "title",
    "paragraphs",
    "translations",
    "sentencePairs",
    "questions",
}
QUESTION_KEYS = {
    "number",
    "choices",
    "answer",
    "choiceTranslations",
    "choiceAnalysis",
    "sourceEvidence",
}
JAPANESE_RE = re.compile(r"[ぁ-んァ-ヶ一-龠]")
BLANK_RE = re.compile(r"\(\s*(\d+)\s*\)")


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def compact(text: str) -> str:
    return re.sub(r"\s+", "", text or "")


def add(errors: list[str], condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


def verify_top_registration(errors: list[str]) -> None:
    top = TOP_PATH.read_text(encoding="utf-8")
    start = top.find("id: 'pre-grade1'")
    end = top.find("id: 'grade2'", start + 1)
    add(errors, start >= 0 and end > start, "top.js: could not isolate pre-grade1 catalog")
    if start < 0 or end <= start:
        return
    block = top[start:end]
    entry = "{ id: '2026-1', label: '2026年度 第1回', sub: '一次試験リーディング' }"
    add(errors, block.count(entry) == 1, "top.js: pre-grade1 2026-1 entry must occur exactly once")
    add(
        errors,
        block.find("id: '2025-3'") < block.find("id: '2026-1'"),
        "top.js: pre-grade1 2026-1 must follow 2025-3",
    )


def main() -> None:
    errors: list[str] = []
    if not DATA_PATH.is_file():
        print(f"ERROR: data file does not exist: {DATA_PATH}")
        raise SystemExit(1)

    with DATA_PATH.open(encoding="utf-8") as source:
        data = json.load(source)

    sections = data.get("sections")
    add(errors, isinstance(sections, list), "root: sections must be an array")
    if not isinstance(sections, list):
        sections = []

    part2s = [section for section in sections if section.get("name") == "大問2"]
    add(errors, len(part2s) == 1, f"sections: expected one 大問2, found {len(part2s)}")
    if not part2s:
        verify_top_registration(errors)
        for error in errors:
            print("ERROR:", error)
        raise SystemExit(1)

    section = part2s[0]
    add(errors, set(section) == SECTION_KEYS, f"大問2: keys differ: {sorted(set(section) ^ SECTION_KEYS)}")
    for key, expected in EXPECTED_META.items():
        add(errors, section.get(key) == expected, f"大問2: {key} differs from expected")

    names = [item.get("name") for item in sections]
    if "大問1" in names:
        add(errors, names.index("大問1") < names.index("大問2"), "sections: 大問2 must follow 大問1")
    else:
        errors.append("sections: 大問1 is missing")
    if "大問3" in names:
        add(errors, names.index("大問2") < names.index("大問3"), "sections: 大問2 must precede 大問3")

    passages = section.get("passages")
    add(errors, isinstance(passages, list) and len(passages) == 2, "大問2: expected exactly 2 passages")
    if not isinstance(passages, list):
        passages = []

    all_questions: list[dict] = []
    for passage in passages:
        label = passage.get("label", "?")
        prefix = f"passage {label}"
        expected = EXPECTED_PASSAGES.get(label)
        add(errors, expected is not None, f"{prefix}: unexpected label")
        if expected is None:
            continue

        add(errors, set(passage) == PASSAGE_KEYS, f"{prefix}: keys differ: {sorted(set(passage) ^ PASSAGE_KEYS)}")
        add(errors, passage.get("title") == expected["title"], f"{prefix}: title differs")
        add(errors, passage.get("paragraphs") == expected["paragraphs"], f"{prefix}: official English differs")

        paragraphs = passage.get("paragraphs", [])
        translations = passage.get("translations", [])
        add(errors, len(paragraphs) == 3, f"{prefix}: expected 3 paragraphs")
        add(errors, len(translations) == len(paragraphs), f"{prefix}: paragraph/translation count differs")
        for index, translation in enumerate(translations, 1):
            add(
                errors,
                isinstance(translation, str) and bool(translation.strip()) and bool(JAPANESE_RE.search(translation)),
                f"{prefix}: translation {index} is not a complete Japanese translation",
            )

        source_blanks = sorted(int(item) for item in BLANK_RE.findall(" ".join(paragraphs)))
        translation_blanks = sorted(int(item) for item in BLANK_RE.findall(" ".join(translations)))
        add(errors, source_blanks == translation_blanks, f"{prefix}: translation blank numbers differ")

        pairs = passage.get("sentencePairs", [])
        add(errors, len(pairs) == expected["pairCount"], f"{prefix}: expected {expected['pairCount']} sentence pairs, found {len(pairs)}")
        pair_english: list[str] = []
        pair_japanese: list[str] = []
        for pair_index, pair in enumerate(pairs, 1):
            pair_prefix = f"{prefix} pair {pair_index}"
            if not isinstance(pair, list) or len(pair) not in (2, 4):
                errors.append(f"{pair_prefix}: expected 2 or 4 elements")
                continue
            if any(not isinstance(value, str) or not value.strip() for value in pair):
                errors.append(f"{pair_prefix}: every element must be a non-empty string")
                continue

            sentence, translation = pair[:2]
            pair_english.append(sentence)
            pair_japanese.append(translation)
            blanks = BLANK_RE.findall(sentence)
            add(errors, bool(JAPANESE_RE.search(translation)), f"{pair_prefix}: Japanese translation is missing")
            add(
                errors,
                sorted(BLANK_RE.findall(translation)) == sorted(blanks),
                f"{pair_prefix}: English/Japanese blank numbers differ",
            )
            if blanks:
                add(errors, len(pair) == 2, f"{pair_prefix}: a blank-containing sentence must have exactly 2 elements")
                continue

            add(errors, len(pair) == 4, f"{pair_prefix}: a non-blank sentence must have exactly 4 elements")
            if len(pair) != 4:
                continue
            slash, main_verb = pair[2:]
            slash_english: list[str] = []
            units = slash.split("||")
            add(errors, len(units) >= 2, f"{pair_prefix}: slash reading needs at least 2 units")
            for unit_index, unit in enumerate(units, 1):
                if "|" not in unit:
                    errors.append(f"{pair_prefix}: slash unit {unit_index} has no English/Japanese separator")
                    continue
                english, japanese = unit.split("|", 1)
                add(errors, bool(norm(english)), f"{pair_prefix}: slash unit {unit_index} has empty English")
                add(
                    errors,
                    bool(norm(japanese)) and bool(JAPANESE_RE.search(japanese)),
                    f"{pair_prefix}: slash unit {unit_index} has no Japanese",
                )
                slash_english.append(english)
            add(
                errors,
                norm(" ".join(slash_english)) == norm(sentence),
                f"{pair_prefix}: slash English does not reconstruct the source sentence",
            )
            main_verb_matches = list(re.finditer(re.escape(main_verb), sentence, re.IGNORECASE))
            add(
                errors,
                len(main_verb_matches) == 1,
                f"{pair_prefix}: main verb must have one unambiguous literal match: {main_verb!r}",
            )
            add(
                errors,
                bool(re.search(rf"(?<!\w){re.escape(main_verb)}(?!\w)", sentence, re.IGNORECASE)),
                f"{pair_prefix}: main verb match must use word boundaries: {main_verb!r}",
            )

        add(
            errors,
            norm(" ".join(pair_english)) == norm(" ".join(paragraphs)),
            f"{prefix}: sentencePairs do not cover the complete official English",
        )
        add(
            errors,
            compact("".join(pair_japanese)) == compact("".join(translations)),
            f"{prefix}: sentencePairs do not cover the complete Japanese translation",
        )

        questions = passage.get("questions", [])
        add(errors, isinstance(questions, list) and len(questions) == 3, f"{prefix}: expected 3 questions")
        if isinstance(questions, list):
            all_questions.extend(questions)

        full_source = norm(" ".join(paragraphs))
        for question in questions if isinstance(questions, list) else []:
            number = question.get("number")
            q_prefix = f"Q{number}"
            expected_question = EXPECTED_QUESTIONS.get(number)
            add(errors, expected_question is not None, f"{q_prefix}: unexpected question number")
            if expected_question is None:
                continue
            add(errors, set(question) == QUESTION_KEYS, f"{q_prefix}: keys differ: {sorted(set(question) ^ QUESTION_KEYS)}")
            add(errors, question.get("choices") == expected_question["choices"], f"{q_prefix}: official choices differ")
            add(errors, question.get("answer") == expected_question["answer"], f"{q_prefix}: official answer differs")

            choices = question.get("choices", [])
            choice_translations = question.get("choiceTranslations", [])
            analyses = question.get("choiceAnalysis", [])
            evidence = question.get("sourceEvidence", [])
            add(errors, len(choice_translations) == 4, f"{q_prefix}: expected 4 choice translations")
            add(errors, len(analyses) == 4, f"{q_prefix}: expected 4 choice analyses")
            for choice_index, translation in enumerate(choice_translations, 1):
                add(
                    errors,
                    isinstance(translation, str) and bool(translation.strip()) and bool(JAPANESE_RE.search(translation)),
                    f"{q_prefix} choice {choice_index}: Japanese choice translation is missing",
                )
            for choice_index, analysis in enumerate(analyses, 1):
                if not isinstance(analysis, str):
                    errors.append(f"{q_prefix} choice {choice_index}: analysis must be a string")
                    continue
                is_correct = choice_index == expected_question["answer"]
                expected_mark = "✅" if is_correct else "❌"
                add(errors, analysis.startswith(expected_mark), f"{q_prefix} choice {choice_index}: expected leading {expected_mark}")
                if choice_index <= len(choices):
                    add(errors, choices[choice_index - 1] in analysis, f"{q_prefix} choice {choice_index}: analysis must name the choice")
                if is_correct:
                    add(errors, analysis.count("→正解。💡") == 1, f"{q_prefix} choice {choice_index}: correct marker must be exactly →正解。💡")
                else:
                    add(errors, "→正解" not in analysis, f"{q_prefix} choice {choice_index}: wrong analysis contains a correct marker")

            add(errors, isinstance(evidence, list) and bool(evidence), f"{q_prefix}: sourceEvidence is missing")
            for evidence_index, quote in enumerate(evidence, 1):
                add(
                    errors,
                    isinstance(quote, str) and bool(quote.strip()) and norm(quote) in full_source,
                    f"{q_prefix}: sourceEvidence {evidence_index} is not an exact passage excerpt",
                )

    numbers = [question.get("number") for question in all_questions]
    add(errors, numbers == [19, 20, 21, 22, 23, 24], f"questions: expected Q19-Q24 in order, got {numbers}")
    add(errors, set(numbers) == set(EXPECTED_QUESTIONS), "questions: missing or duplicate official question numbers")
    actual_pairs = {
        pair[0]: pair[1:]
        for passage in passages
        for pair in passage.get("sentencePairs", [])
        if isinstance(pair, list) and len(pair) == 4
    }
    critical_pair = "Part of this project involves creating a virtual reconstruction of the nation."
    add(
        errors,
        actual_pairs.get(critical_pair) == [
            "このプロジェクトの一部には、国を仮想空間に再現する取り組みが含まれる。",
            "Part of this project involves|このプロジェクトの一部には||creating a virtual reconstruction of the nation.|国を仮想復元する取り組みが含まれる。",
            "involves",
        ],
        "Digital Nations: audited virtual-reconstruction slash translation regressed",
    )
    verify_top_registration(errors)

    print(f"section2 passages={len(passages)} questions={len(all_questions)} errors={len(errors)}")
    for error in errors:
        print("ERROR:", error)
    if errors:
        raise SystemExit(1)
    print("OK: 2026-1 Grade Pre-1 Part 2 and top-page registration verified")


if __name__ == "__main__":
    main()

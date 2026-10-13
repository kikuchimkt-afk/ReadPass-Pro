# -*- coding: utf-8 -*-
"""Verify Part 1-3 of Grade Pre-1 2026-2 against the official answer key."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "pre-grade1" / "2026-2" / "data.json"
TOP_PATH = BASE_DIR / "top.js"
TOP_HTML_PATH = BASE_DIR / "top.html"

# Official answer key (2026年度 第2回 準1級, 10月4日実施).
OFFICIAL_ANSWERS = [
    1, 4, 4, 3, 3, 4, 2, 1, 1, 4, 4, 1, 4, 2, 1, 1, 4, 1,
    2, 1, 4, 3, 2, 4,
    3, 1, 4, 4, 2, 1, 2,
]
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
OFFICIAL_PART2_CHOICES = {
    19: ["was the only viable option", "might have limitations", "could only be understood by scientists", "mainly benefited large businesses"],
    20: ["Furthermore", "However", "In any case", "On the contrary"],
    21: ["governments wanted their money back", "problems could not be fixed", "new bugs were found", "people saw it differently"],
    22: ["In exchange", "Consequently", "Nevertheless", "In short"],
    23: ["should be found in a range of food sources", "must trigger a physical response in the body", "should be easy for people to describe", "must last for a certain amount of time"],
    24: ["could lose their significance in the future", "remain constant throughout a person’s lifetime", "often have cultural and historical significance", "influence eating behavior and health"],
}
EXPECTED_PASSAGES = [
    ("大問2", "A", "The Y2K Bug", 3, [19, 20, 21]),
    ("大問2", "B", "Searching for a Sixth Taste", 3, [22, 23, 24]),
    ("大問3", "A", "Employment Requirements for Welfare", 3, [25, 26, 27]),
    ("大問3", "B", "Saint Helena", 4, [28, 29, 30, 31]),
]
EXPECTED_SECTION_META = [
    ("大問1", "Part 1", "vocabulary"),
    ("大問2", "Part 2", "passage-fill"),
    ("大問3", "Part 3", "reading-comprehension"),
]
TOP_KEYS = ["grade", "year", "session", "title", "vocabulary", "sections", "lessonPlan"]
PART1_KEYS = {"number", "text", "translation", "choices", "answer", "choiceAnalysis", "grammar"}
PASSAGE_KEYS = {"label", "title", "paragraphs", "translations", "sentencePairs", "questions"}
PART2_KEYS = {"number", "choices", "answer", "choiceTranslations", "choiceAnalysis", "sourceEvidence"}
PART3_KEYS = PART2_KEYS | {"question", "questionTranslation"}
JAPANESE_RE = re.compile(r"[ぁ-んァ-ヶ一-龠]")
BLANK_RE = re.compile(r"\(\s*(\d+)\s*\)")
FORBIDDEN_CHARS = {"ﬁ": "fi ligature", "ﬂ": "fl ligature", "­": "soft hyphen", ";": "Greek question mark"}


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def compact(text: str) -> str:
    return re.sub(r"\s+", "", text or "")


def check_analyses(errors: list[str], prefix: str, analyses: list, choices: list, answer: int, part: int) -> None:
    if not isinstance(analyses, list) or len(analyses) != 4:
        errors.append(f"{prefix}: needs four choiceAnalysis entries")
        return
    marker = "→ 正解。💡" if part == 1 else "→正解。💡"
    for index, analysis in enumerate(analyses, 1):
        if not isinstance(analysis, str) or not analysis.strip():
            errors.append(f"{prefix} choice {index}: empty analysis")
            continue
        if part in (1, 2) and choices[index - 1].casefold() not in analysis.casefold():
            errors.append(f"{prefix} choice {index}: analysis does not name {choices[index - 1]!r}")
        if index == answer:
            if not analysis.startswith("✅ ") or analysis.count(marker) != 1:
                errors.append(f"{prefix} choice {index}: correct analysis needs '✅ ' and one {marker!r}")
        else:
            if not analysis.startswith("❌ "):
                errors.append(f"{prefix} choice {index}: wrong analysis must start with '❌ '")
            if "✅" in analysis or "→ 正解" in analysis or "→正解" in analysis:
                errors.append(f"{prefix} choice {index}: wrong analysis contains a correct marker")


def check_pairs(errors: list[str], prefix: str, passage: dict) -> None:
    pairs = passage.get("sentencePairs", [])
    english: list[str] = []
    japanese: list[str] = []
    for index, pair in enumerate(pairs, 1):
        pair_prefix = f"{prefix} pair {index}"
        if not isinstance(pair, list) or len(pair) not in (2, 4) or not all(isinstance(v, str) and v.strip() for v in pair):
            errors.append(f"{pair_prefix}: expected 2 or 4 non-empty strings")
            continue
        sentence, translation = pair[:2]
        english.append(sentence)
        japanese.append(translation)
        blanks = BLANK_RE.findall(sentence)
        if not JAPANESE_RE.search(translation):
            errors.append(f"{pair_prefix}: Japanese translation is missing")
        if sorted(BLANK_RE.findall(translation)) != sorted(blanks):
            errors.append(f"{pair_prefix}: English/Japanese blank numbers differ")
        if blanks:
            if len(pair) != 2:
                errors.append(f"{pair_prefix}: a blank-containing sentence must have exactly 2 elements")
            continue
        if len(pair) != 4:
            errors.append(f"{pair_prefix}: a non-blank sentence must have exactly 4 elements")
            continue
        slash, main_verb = pair[2:]
        units = slash.split("||")
        if len(units) < 2:
            errors.append(f"{pair_prefix}: slash reading needs at least 2 units")
        slash_english = []
        for unit_index, unit in enumerate(units, 1):
            if "|" not in unit:
                errors.append(f"{pair_prefix}: slash unit {unit_index} has no separator")
                continue
            unit_en, unit_ja = unit.split("|", 1)
            if not norm(unit_en) or not JAPANESE_RE.search(unit_ja):
                errors.append(f"{pair_prefix}: slash unit {unit_index} is incomplete")
            slash_english.append(unit_en)
        if norm(" ".join(slash_english)) != norm(sentence):
            errors.append(f"{pair_prefix}: slash English does not reconstruct the sentence")
        if len(list(re.finditer(re.escape(main_verb), sentence, re.IGNORECASE))) != 1:
            errors.append(f"{pair_prefix}: main verb needs one unambiguous match: {main_verb!r}")
        if not re.search(rf"(?<!\w){re.escape(main_verb)}(?!\w)", sentence, re.IGNORECASE):
            errors.append(f"{pair_prefix}: main verb must match on word boundaries: {main_verb!r}")
    if norm(" ".join(english)) != norm(" ".join(passage.get("paragraphs", []))):
        errors.append(f"{prefix}: sentencePairs do not cover the complete English text")
    if compact("".join(japanese)) != compact("".join(passage.get("translations", []))):
        errors.append(f"{prefix}: sentencePairs do not cover the complete Japanese translation")


def verify_registration(errors: list[str]) -> None:
    top = TOP_PATH.read_text(encoding="utf-8")
    start = top.find("id: 'pre-grade1'")
    end = top.find("id: 'grade2'", start + 1)
    if start < 0 or end <= start:
        errors.append("top.js: could not isolate the pre-grade1 catalog")
        return
    block = top[start:end]
    entry = "{ id: '2026-2', label: '2026年度 第2回', sub: '一次試験リーディング' }"
    if block.count(entry) != 1:
        errors.append("top.js: pre-grade1 2026-2 entry must occur exactly once")
    elif block.find("id: '2026-1'") > block.find("id: '2026-2'"):
        errors.append("top.js: pre-grade1 2026-2 must follow 2026-1")
    # Later releases bump the version again; it only must not predate this exam.
    cache = re.search(r"top\.js\?v=(\d{8})-", TOP_HTML_PATH.read_text(encoding="utf-8"))
    if not cache or cache.group(1) < "20261013":
        errors.append("top.html: top.js cache-busting version was not bumped")


def main() -> None:
    errors: list[str] = []
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))

    if list(data) != TOP_KEYS:
        errors.append(f"top-level keys/order differ: {list(data)}")
    expected_meta = {"grade": "準1級", "year": "2026", "session": "2", "title": "2026年度 第2回 英語資格検定準1級 リーディング"}
    for key, value in expected_meta.items():
        if data.get(key) != value:
            errors.append(f"{key}={data.get(key)!r} != {value!r}")

    raw = DATA_PATH.read_text(encoding="utf-8")
    for char, name in FORBIDDEN_CHARS.items():
        if char in raw:
            errors.append(f"data.json contains a PDF extraction artifact: {name}")

    sections = data.get("sections", [])
    if [(s.get("name"), s.get("nameEn"), s.get("type")) for s in sections] != EXPECTED_SECTION_META:
        errors.append("sections: 大問1-3 metadata/order differs")
        sections = (sections + [{}, {}, {}])[:3]

    # Part 1
    part1 = sections[0].get("questions", [])
    if len(part1) != 18:
        errors.append(f"Part 1: expected 18 questions, found {len(part1)}")
    for index, question in enumerate(part1[:18]):
        number = index + 1
        prefix = f"Q{number}"
        if set(question) != PART1_KEYS:
            errors.append(f"{prefix}: keys differ: {sorted(question)}")
            continue
        if question["number"] != number:
            errors.append(f"{prefix}: number differs")
        if question["choices"] != OFFICIAL_PART1_CHOICES[index]:
            errors.append(f"{prefix}: official choices differ")
        if question["answer"] != OFFICIAL_ANSWERS[index]:
            errors.append(f"{prefix}: official answer differs")
        blank = f"( {number} )"
        if question["text"].count(blank) != 1 or question["translation"].count(blank) != 1:
            errors.append(f"{prefix}: English and Japanese must each contain {blank!r} once")
        if not JAPANESE_RE.search(question["translation"]):
            errors.append(f"{prefix}: translation is not Japanese")
        if not question["grammar"].startswith("💡"):
            errors.append(f"{prefix}: grammar must start with 💡")
        check_analyses(errors, prefix, question["choiceAnalysis"], question["choices"], question["answer"], 1)

    # Part 2 and Part 3
    seen_numbers: list[int] = []
    for section_name, label, title, paragraph_count, numbers in EXPECTED_PASSAGES:
        section = next((s for s in sections if s.get("name") == section_name), {})
        passage = next((p for p in section.get("passages", []) if p.get("label") == label), None)
        prefix = f"{section_name}{label}"
        if passage is None:
            errors.append(f"{prefix}: passage is missing")
            continue
        if set(passage) != PASSAGE_KEYS:
            errors.append(f"{prefix}: keys differ: {sorted(passage)}")
        if passage.get("title") != title:
            errors.append(f"{prefix}: title={passage.get('title')!r}")
        paragraphs = passage.get("paragraphs", [])
        translations = passage.get("translations", [])
        if len(paragraphs) != paragraph_count or len(translations) != paragraph_count:
            errors.append(f"{prefix}: expected {paragraph_count} paragraphs and translations")
        source_blanks = sorted(int(n) for n in BLANK_RE.findall(" ".join(paragraphs)))
        expected_blanks = numbers if section_name == "大問2" else []
        if source_blanks != expected_blanks:
            errors.append(f"{prefix}: blanks in English={source_blanks} expected={expected_blanks}")
        if sorted(int(n) for n in BLANK_RE.findall(" ".join(translations))) != expected_blanks:
            errors.append(f"{prefix}: blanks in Japanese differ")
        check_pairs(errors, prefix, passage)

        full_source = norm(" ".join(paragraphs))
        questions = passage.get("questions", [])
        if [q.get("number") for q in questions] != numbers:
            errors.append(f"{prefix}: question numbers {[q.get('number') for q in questions]} != {numbers}")
        for question in questions:
            number = question.get("number")
            q_prefix = f"Q{number}"
            seen_numbers.append(number)
            keys = PART2_KEYS if section_name == "大問2" else PART3_KEYS
            if set(question) != keys:
                errors.append(f"{q_prefix}: keys differ: {sorted(question)}")
                continue
            if question["answer"] != OFFICIAL_ANSWERS[number - 1]:
                errors.append(f"{q_prefix}: official answer differs")
            if section_name == "大問2" and question["choices"] != OFFICIAL_PART2_CHOICES[number]:
                errors.append(f"{q_prefix}: official choices differ")
            if len(question["choices"]) != 4 or len(set(question["choices"])) != 4:
                errors.append(f"{q_prefix}: needs four unique choices")
            translations_ok = len(question["choiceTranslations"]) == 4 and all(
                isinstance(t, str) and JAPANESE_RE.search(t) for t in question["choiceTranslations"]
            )
            if not translations_ok:
                errors.append(f"{q_prefix}: needs four Japanese choiceTranslations")
            if section_name == "大問3" and not JAPANESE_RE.search(question.get("questionTranslation", "")):
                errors.append(f"{q_prefix}: questionTranslation is missing")
            check_analyses(
                errors, q_prefix, question["choiceAnalysis"], question["choices"], question["answer"],
                2 if section_name == "大問2" else 3,
            )
            evidence = question["sourceEvidence"]
            if not isinstance(evidence, list) or not evidence:
                errors.append(f"{q_prefix}: sourceEvidence is missing")
                continue
            for quote in evidence:
                if not isinstance(quote, str) or norm(quote) not in full_source:
                    errors.append(f"{q_prefix}: sourceEvidence is not an exact passage excerpt: {quote!r}")
                elif BLANK_RE.search(quote):
                    errors.append(f"{q_prefix}: sourceEvidence must not contain a blank")
    if seen_numbers != list(range(19, 32)):
        errors.append(f"Part 2/3 question numbers differ: {seen_numbers}")

    verify_registration(errors)

    if errors:
        print(f"ERRORS={len(errors)}")
        for error in errors:
            print(f"  {error}")
        raise SystemExit(1)
    print("OK: Grade Pre-1 2026-2 Part 1-3 (31 questions) and top-page registration verified")


if __name__ == "__main__":
    main()

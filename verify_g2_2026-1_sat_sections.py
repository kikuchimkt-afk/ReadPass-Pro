# -*- coding: utf-8 -*-
"""2026-1-sat 2級の本文・対訳・根拠・解説を検証する。"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

data = json.loads(
    (Path(__file__).resolve().parent / "data" / "grade2" / "2026-1-sat" / "data.json")
    .read_text(encoding="utf-8")
)

expected = {
    "Child-Friendly City": (3, 15, [18, 19, 20]),
    "Dead Trees": (3, 19, [21, 22, 23]),
    "Inquiry about the factory": (4, 14, [24, 25, 26]),
    "The Lost City": (4, 20, [27, 28, 29, 30, 31]),
}


def compact(text):
    return re.sub(r"\s+", "", text)


questions = []
passages = []
for section in data["sections"]:
    questions.extend(section.get("questions", []))
    passages.extend(section.get("passages", []))
    for passage in section.get("passages", []):
        questions.extend(passage["questions"])

assert {p["title"] for p in passages} == set(expected)
no_main_verb_english = {
    "Dear James White,",
    "Sincerely,\nJessica Jenkins\nRiverstone High School",
}
for passage in passages:
    paragraphs, pairs, numbers = expected[passage["title"]]
    assert len(passage["paragraphs"]) == len(passage["translations"]) == paragraphs
    assert len(passage["sentencePairs"]) == pairs
    assert [q["number"] for q in passage["questions"]] == numbers
    for pair in passage["sentencePairs"]:
        assert len(pair) == 4 and all(isinstance(field, str) for field in pair)
        assert all(pair[:3])
        slash_english = []
        slash_chunks = pair[2].split("||")
        assert len(slash_chunks) >= 2
        for chunk in slash_chunks:
            assert chunk.count("|") == 1
            english_unit, japanese_unit = chunk.split("|", 1)
            assert english_unit.strip() and japanese_unit.strip()
            slash_english.append(english_unit)
        assert compact(" ".join(slash_english)) == compact(pair[0])
        if pair[0] in no_main_verb_english:
            assert pair[3] == ""
        else:
            assert pair[3]
            assert re.search(
                r"(?<![A-Za-z0-9])" + re.escape(pair[3]) + r"(?![A-Za-z0-9])",
                pair[0],
            )
    assert compact(" ".join(pair[0] for pair in passage["sentencePairs"])) == compact(
        " ".join(passage["paragraphs"])
    )
    assert compact(" ".join(pair[1] for pair in passage["sentencePairs"])) == compact(
        " ".join(passage["translations"])
    )
    corpus = " ".join(passage["paragraphs"])
    for question in passage["questions"]:
        assert question["sourceEvidence"]
        assert all(phrase in corpus for phrase in question["sourceEvidence"])

email = next(p for p in passages if p["title"] == "Inquiry about the factory")
assert email["paragraphs"][0].startswith("Dear James White,\nMy name is Jessica Jenkins")
assert email["paragraphs"][-1] == "Sincerely,\nJessica Jenkins\nRiverstone High School"
assert email["translations"][0].startswith("ジェームズ・ホワイト様\n")
assert email["translations"][-1] == "敬具\nジェシカ・ジェンキンス\nリバーストーン高校"
assert email["sentencePairs"][0][3] == ""
assert email["sentencePairs"][-1][3] == ""
assert next(
    pair for pair in email["sentencePairs"] if pair[0].startswith("Could you also tell us")
)[3] == "tell us"

child_friendly = next(p for p in passages if p["title"] == "Child-Friendly City")
walk_pair = next(pair for pair in child_friendly["sentencePairs"] if "on their own" in pair[0])
assert "自分たちだけで歩いて学校へ行くことができる" in walk_pair[1]
assert "during the school arrival time from 7:30 to 8:00 a.m.,|" in walk_pair[2]
assert "during the school arrival time|" not in walk_pair[2]
assert "自分たちだけで歩いて学校へ行くことができる" in child_friendly["translations"][0]

dead_trees = next(p for p in passages if p["title"] == "Dead Trees")
assert "すると今度は、新しい昆虫" in dead_trees["translations"][0]
assert "やがて、新しい昆虫" not in dead_trees["translations"][0]

for question in questions:
    assert len(question["choiceTranslations"]) == 4
    assert question["grammar"].startswith("💡")
    for index, analysis in enumerate(question["choiceAnalysis"], 1):
        assert not analysis.startswith(("✅", "❌", "○"))
        assert ("→正解。💡" in analysis) == (index == question["answer"])

assert next(q for q in questions if q["number"] == 18)["choiceTranslations"][3] == "その代わりに"
assert next(q for q in questions if q["number"] == 25)["sourceEvidence"] == [
    "His last class of the day ends at 2:00 p.m. on Fridays, which is earlier than on other days."
]
assert next(q for q in questions if q["number"] == 25)["choiceTranslations"][2] == (
    "その日は生徒にとって交通の便がよりよいから。"
)
assert next(q for q in questions if q["number"] == 31)["answer"] == 1

print("OK: source text, 68 four-field sentence pairs, email greeting/signature, evidence, and marker rules")

# -*- coding: utf-8 -*-
"""2026-1-sat 2級のFocus Practice 5件を検証する。"""
import json
import os
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

BASE = Path(__file__).resolve().parent / "data" / "grade2" / "2026-1-sat"
data = json.loads((BASE / "data.json").read_text(encoding="utf-8"))
points = data["lessonPlan"]["focusPoints"]
assert [point["id"] for point in points] == ["fp1", "fp2", "fp3", "fp4", "fp5"]

passages = [p for section in data["sections"] for p in section.get("passages", [])]
corpus = " ".join(" ".join(p["paragraphs"]) for p in passages)
filled = corpus
questions = {
    q["number"]: q
    for section in data["sections"]
    for passage in section.get("passages", [])
    for q in passage["questions"]
}
for number in range(18, 24):
    question = questions[number]
    filled = filled.replace(f"( {number} )", question["choices"][question["answer"] - 1])

for point in points:
    assert len(point["examples"]) == 3
    assert len(point["practiceQuestions"]) == 4
    assert all(item["en"] and item["ja"] and item["note"] for item in point["examples"])
    assert all(item["q"] and item["a"] for item in point["practiceQuestions"])
    practice = point["practicePassage"]
    assert practice["en"].startswith("[出典:") and practice["ja"]
    for line in practice["en"].splitlines():
        if not line or line.startswith("[出典:"):
            continue
        for sentence in re.split(r"(?<=[.!?])\s+", line):
            assert not sentence or sentence in filled, (point["id"], sentence)
    for pattern in point["highlightPatterns"]:
        assert pattern in corpus, (point["id"], pattern)
    audio = BASE / Path(practice["audioFile"].replace("/", os.sep))
    assert audio.is_file() and audio.stat().st_size >= 500

assert "すると今度は、新しい昆虫" in points[1]["practicePassage"]["ja"]
assert "自分たちだけで歩いて学校へ行くことができる" in points[3]["practicePassage"]["ja"]
assert "自分の足で歩いて学校" not in points[3]["practicePassage"]["ja"]
assert "since はその時点から現在までの継続" in points[0]["practiceQuestions"][3]["a"]

print("OK: five Focus Practice units, four questions each, source text, and audio")

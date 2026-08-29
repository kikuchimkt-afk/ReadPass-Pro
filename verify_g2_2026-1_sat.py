# -*- coding: utf-8 -*-
"""2026-1-sat 2級の登録データを横断検証する。"""
import json
import os
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "data" / "grade2" / "2026-1-sat"
data = json.loads((BASE / "data.json").read_text(encoding="utf-8"))

official = [
    3, 2, 3, 3, 1, 3, 3, 1, 4, 3, 3, 3, 4, 2, 3, 1, 1,
    4, 2, 3, 1, 4, 3, 4, 1, 3, 1, 3, 4, 2, 1,
]
listening = [4, 4, 1, 1, 4, 4, 4, 3, 3, 2, 4, 1, 1, 1, 4,
             1, 2, 2, 3, 4, 2, 2, 3, 4, 4, 3, 2, 4, 2, 1]

questions = []
for section in data["sections"]:
    questions.extend(section.get("questions", []))
    for passage in section.get("passages", []):
        questions.extend(passage.get("questions", []))

assert [q["number"] for q in questions] == list(range(1, 32))
assert [q["answer"] for q in questions] == official
assert all(len(q["choices"]) == len(q["choiceTranslations"]) == 4 for q in questions)
assert all(q.get("grammar", "").startswith("💡") for q in questions)
assert all(q.get("sourceEvidence") for q in questions if q["number"] >= 18)
assert all(q.get("questionTranslation") for q in questions if q["number"] >= 24)

actual_listening = []
for part in ("part1", "part2"):
    actual_listening.extend(data["listening"][part].values())
assert actual_listening == listening

for item in data["vocabulary"]:
    ref = item["wordAudio"]
    path = BASE / Path(ref.replace("/", os.sep))
    assert path.is_file() and path.stat().st_size >= 500, (item["word"], ref)
for point in data["lessonPlan"]["focusPoints"]:
    ref = point["practicePassage"]["audioFile"]
    path = BASE / Path(ref.replace("/", os.sep))
    assert path.is_file() and path.stat().st_size >= 500, (point["id"], ref)

print("OK: 31 reading answers, 30 listening answers, translations, evidence, and audio references")

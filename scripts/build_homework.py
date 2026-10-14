"""Validate the homework print data and write data/homework/index.json.

Each data/homework/<grade>/<exam>.json is a four-page A4 homework print:
pages 1-2 have the aim, goals and Part-1-style four-choice questions on the exam's
focus points (★ items also ask for a full translation); pages 3-4 have, for every
question, the answer, translation, explanation, choice notes and a tutor's one-line
tip, then a closing message and the next lesson's flash-card QR. print.js flows the
items onto the pages by measured height; this script checks the content (including
the lengths that keep it within four sheets) and lists the available sets.

Usage:
    python scripts/build_homework.py           # validate all and rewrite the index
    python scripts/build_homework.py --check   # validate and confirm the index is current
"""
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
HOMEWORK = ROOT / "data/homework"
INDEX = HOMEWORK / "index.json"
BLANK = "(　)"


def validate(path):
    errors = []

    def check(ok, msg):
        if not ok:
            errors.append(f"{path.relative_to(ROOT).as_posix()}: {msg}")

    hw = json.loads(path.read_text(encoding="utf-8"))
    grade, exam = path.parent.name, path.stem
    check(hw.get("grade") == grade and hw.get("exam") == exam, "grade/exam must match the file path")
    data_path = ROOT / "data" / grade / exam / "data.json"
    check(data_path.is_file(), f"exam data missing: {data_path.relative_to(ROOT).as_posix()}")
    if not data_path.is_file():
        return hw, errors
    data = json.loads(data_path.read_text(encoding="utf-8"))
    focus_ids = {fp["id"] for fp in data.get("lessonPlan", {}).get("focusPoints", [])}
    exam_texts = {q.get("text", "") for s in data["sections"] for q in s.get("questions", [])}

    for key, low, high in (("title", 2, 20), ("theme", 4, 30), ("aim", 40, 140), ("closing", 80, 200)):
        check(low <= len(hw.get(key, "")) <= high, f"{key} length {low}-{high}")
    goals = hw.get("goals", [])
    check(3 <= len(goals) <= 4 and all(8 <= len(g) <= 40 for g in goals), "3-4 goals of 8-40 characters")
    questions = hw.get("questions", [])
    check(10 <= len(questions) <= 14, "10-14 questions (two pages of questions, two of explanations)")
    check([q.get("number") for q in questions] == list(range(1, len(questions) + 1)), "questions numbered from 1")
    instruction = hw.get("instruction", "")
    check(f"(1)から({len(questions)})まで" in instruction, "instruction names the question range")
    starred = [q for q in questions if q.get("translate")]
    check(3 <= len(starred) <= 5, "3-5 ★ translation items")
    check("★" in instruction, "instruction explains ★")
    used_focus = set()
    for q in questions:
        tag = f"Q{q.get('number')}"
        text = q.get("text", "")
        check(text.count(BLANK) == 1 and len(text) <= 120, tag + " one blank (　), at most 120 characters")
        check(text not in exam_texts, tag + " is an original sentence, not the exam's")
        choices = q.get("choices", [])
        check(len(choices) == 4 and len(set(choices)) == 4 and all(choices), tag + " four distinct choices")
        check(q.get("answer") in (1, 2, 3, 4), tag + " answer 1-4")
        check(q.get("focus") in focus_ids, tag + " focus point exists in the exam lesson plan")
        used_focus.add(q.get("focus"))
        check(isinstance(q.get("translate"), bool), tag + " translate flag")
        check(15 <= len(q.get("translation", "")) <= 60 and BLANK not in q.get("translation", ""), tag + " translation 15-60")
        check(30 <= len(q.get("explanation", "")) <= 110, tag + " explanation 30-110")
        notes = q.get("choiceNotes", [])
        check(len(notes) == 4 and all(n.startswith(c) for n, c in zip(notes, choices)), tag + " one note per choice, in order")
        check(sum(len(n) for n in notes) <= 70, tag + " choice notes fit one line")
        check(15 <= len(q.get("tip", "")) <= 70, tag + " tutor tip 15-70")
    check(len(used_focus) >= 3, "questions cover at least three focus points")
    answers = [q.get("answer") for q in questions]
    limit = -(-len(questions) // 4) + 1
    check(all(answers.count(a) >= 2 for a in (1, 2, 3, 4)) and max(answers.count(a) for a in (1, 2, 3, 4)) <= limit,
          f"correct answers spread: every position at least twice, none more than {limit} times")
    return hw, errors


def build_index():
    index, errors = {}, []
    for path in sorted(HOMEWORK.glob("*/*.json")):
        hw, problems = validate(path)
        errors += problems
        index[f"{path.parent.name}/{path.stem}"] = {
            "path": path.relative_to(ROOT).as_posix(),
            "title": hw.get("title", ""),
            "questions": len(hw.get("questions", [])),
            "translations": sum(1 for q in hw.get("questions", []) if q.get("translate")),
        }
    return index, errors


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    index, errors = build_index()
    text = json.dumps(index, ensure_ascii=False, indent=2) + "\n"
    if args.check and (not INDEX.is_file() or INDEX.read_text(encoding="utf-8") != text):
        errors.append("data/homework/index.json is out of date (run scripts/build_homework.py)")
    for error in errors:
        print("ERROR:", error)
    if errors:
        raise SystemExit(1)
    if not args.check:
        INDEX.write_text(text, encoding="utf-8")
    print(f"HOMEWORK OK: {len(index)} sets -> {INDEX.relative_to(ROOT).as_posix()}")


if __name__ == "__main__":
    main()

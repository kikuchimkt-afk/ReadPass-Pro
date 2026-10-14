"""Validate the homework print data and write data/homework/index.json.

Each data/homework/<grade>/<exam>.json is a four-page A4 homework print (pages 1-2
questions, pages 3-4 answers and explanations), rendered by print.js, which flows
the items onto the pages by measured height. Two layouts exist (docs/homework-print.md):

- "grammar" (default; Pre-2 and above): aim, goals and Part-1-style four-choice
  questions on the exam's focus points; ★ items also ask for a full translation.
- "writing" (Grade 3 and below): word practice and model sentences on four-line
  guides, Part-1-style questions whose ★ items are copied onto four-line guides,
  and a spelling check of the practised words.

Both end with a closing message and the next lesson's flash-card QR. This script
checks the content (lengths that keep the print within four sheets, answer spread,
similarity to past exams, existence of focus points / words / lesson sentences)
and lists the available sets.

Usage:
    python scripts/build_homework.py           # validate all and rewrite the index
    python scripts/build_homework.py --check   # validate and confirm the index is current
"""
import argparse
import difflib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
HOMEWORK = ROOT / "data/homework"
INDEX = HOMEWORK / "index.json"
BLANK = "(　)"
SIMILAR = 0.75  # a homework sentence this close to an exam sentence is treated as copied
LIMITS = {
    "grammar": dict(questions=(10, 14), starred=(3, 5), text=120, translation=(15, 60), explanation=(30, 110), tip=(15, 70)),
    "writing": dict(questions=(6, 8), starred=(2, 4), text=100, translation=(8, 70), explanation=(20, 100), tip=(10, 70)),
}


def normalized(text):
    text = re.sub(r"\(\s*\d*\s*\)|\(　\)", " ___ ", text)
    return re.sub(r"\s+", " ", text).strip().lower()


def most_similar(mine, past):
    """Highest similarity to a past sentence; the cheap upper bounds skip clearly different ones."""
    best = (0.0, "")
    for norm, original in past:
        matcher = difflib.SequenceMatcher(None, mine, norm)
        if matcher.real_quick_ratio() < SIMILAR or matcher.quick_ratio() < SIMILAR:
            continue
        best = max(best, (matcher.ratio(), original))
    return best


def compact(text):
    return re.sub(r"\s+", "", text)


def grade_sentences(grade):
    """Every question text, stem and passage sentence of all exams of a grade (past papers)."""
    sentences = []
    for data_path in sorted((ROOT / "data" / grade).glob("*/data.json")):
        data = json.loads(data_path.read_text(encoding="utf-8"))
        for section in data["sections"]:
            sentences += [q.get("text") or q.get("question", "") for q in section.get("questions", [])]
            for passage in section.get("passages", []):
                sentences += [row[0] for row in passage.get("sentencePairs", [])]
                sentences += [q.get("question", "") for q in passage.get("questions", [])]
    return [(normalized(s), s) for s in sentences if s]


def lesson_corpus(data):
    """Text a student met in the lesson: completed questions, passages and lesson examples."""
    parts = []
    for section in data["sections"]:
        for q in section.get("questions", []):
            text = q.get("text", "")
            if "words" in q:  # word order: the completed sentence
                text = " ".join([q.get("framePrefix", ""), *[q["words"][i - 1] for i in q["correctOrder"]], q.get("frameSuffix", "")])
            elif q.get("choices") and q.get("answer"):
                text = re.sub(r"\(\s*\d*\s*\)|\(　\)", q["choices"][q["answer"] - 1], text)
            parts.append(text)
        for passage in section.get("passages", []):
            parts += passage.get("paragraphs", [])
    for fp in data.get("lessonPlan", {}).get("focusPoints", []):
        parts += [e.get("en", "") for e in fp.get("examples", [])]
    return compact(" ".join(parts)).replace("’", "'")


def validate(path):
    errors = []

    def check(ok, msg):
        if not ok:
            errors.append(f"{path.relative_to(ROOT).as_posix()}: {msg}")

    try:
        hw = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        check(False, f"invalid JSON: {error}")
        return {}, errors
    grade, exam = path.parent.name, path.stem
    layout = hw.get("layout", "grammar")
    check(layout in LIMITS, "layout must be grammar or writing")
    limits = LIMITS.get(layout, LIMITS["grammar"])
    check(hw.get("grade") == grade and hw.get("exam") == exam, "grade/exam must match the file path")
    data_path = ROOT / "data" / grade / exam / "data.json"
    check(data_path.is_file(), f"exam data missing: {data_path.relative_to(ROOT).as_posix()}")
    if not data_path.is_file():
        return hw, errors
    data = json.loads(data_path.read_text(encoding="utf-8"))
    focus_ids = {fp["id"] for fp in data.get("lessonPlan", {}).get("focusPoints", [])}
    past = grade_sentences(grade)

    for key, low, high in (("title", 2, 20), ("theme", 4, 30), ("aim", 40, 140), ("closing", 60, 200)):
        check(low <= len(hw.get(key, "")) <= high, f"{key} length {low}-{high}")
    goals = hw.get("goals", [])
    check(3 <= len(goals) <= 4 and all(8 <= len(g) <= 40 for g in goals), "3-4 goals of 8-40 characters")

    questions = hw.get("questions", [])
    star_key = "copy" if layout == "writing" else "translate"
    low, high = limits["questions"]
    check(low <= len(questions) <= high, f"{low}-{high} questions")
    check([q.get("number") for q in questions] == list(range(1, len(questions) + 1)), "questions numbered from 1")
    instruction = hw.get("instruction", "")
    check(f"(1)から({len(questions)})まで" in instruction, "instruction names the question range")
    check("★" in instruction, "instruction explains ★")
    starred = [q for q in questions if q.get(star_key)]
    low, high = limits["starred"]
    check(low <= len(starred) <= high, f"{low}-{high} ★ items ({star_key})")
    used_focus = set()
    for q in questions:
        tag = f"Q{q.get('number')}"
        text = q.get("text", "")
        check(text.count(BLANK) == 1 and len(text) <= limits["text"], f"{tag} one blank (　), at most {limits['text']} characters")
        ratio, closest = most_similar(normalized(text), past)
        check(ratio < SIMILAR, f"{tag} is too close to a past-exam sentence ({ratio:.2f}): {closest[:60]}")
        choices = q.get("choices", [])
        check(len(choices) == 4 and len(set(choices)) == 4 and all(choices), tag + " four distinct choices")
        check(q.get("answer") in (1, 2, 3, 4), tag + " answer 1-4")
        check(q.get("focus") in focus_ids, tag + " focus point exists in the exam lesson plan")
        used_focus.add(q.get("focus"))
        check(isinstance(q.get(star_key), bool), f"{tag} {star_key} flag")
        other = "translate" if star_key == "copy" else "copy"
        check(other not in q, f"{tag} uses {star_key}, not {other}, in the {layout} layout")
        low, high = limits["translation"]
        check(low <= len(q.get("translation", "")) <= high and BLANK not in q.get("translation", ""), f"{tag} translation {low}-{high}")
        low, high = limits["explanation"]
        check(low <= len(q.get("explanation", "")) <= high, f"{tag} explanation {low}-{high}")
        notes = q.get("choiceNotes", [])
        check(len(notes) == 4 and all(n.startswith(c) for n, c in zip(notes, choices)), tag + " one note per choice, in order")
        check(sum(len(n) for n in notes) <= 70, tag + " choice notes fit one line")
        low, high = limits["tip"]
        check(low <= len(q.get("tip", "")) <= high, f"{tag} tutor tip {low}-{high}")
    check(len(used_focus) >= 3, "questions cover at least three focus points")
    answers = [q.get("answer") for q in questions]
    least = 2 if len(questions) >= 10 else 1
    most = -(-len(questions) // 4) + 1
    check(all(answers.count(a) >= least for a in (1, 2, 3, 4)) and max(answers.count(a) for a in (1, 2, 3, 4)) <= most,
          f"correct answers spread: every position at least {least} time(s), none more than {most}")

    if layout == "writing":
        check("書き写" in instruction, "instruction asks to copy ★ items")
        for q in questions:
            if q.get("copy"):
                check("\n" not in q.get("text", "") and len(q.get("text", "")) <= 60,
                      f"Q{q.get('number')} ★ copy item is one sentence of at most 60 characters")
        vocab = {v["word"] for v in data.get("vocabulary", [])}
        words = hw.get("words", [])
        check(5 <= len(words) <= 7 and len({w.get("word") for w in words}) == len(words), "5-7 distinct practice words")
        for w in words:
            check(w.get("word") in vocab, f"word {w.get('word')!r} is in the exam vocabulary")
            check(0 < len(w.get("word", "")) <= 14, f"word {w.get('word')!r} fits the model cell (14 letters)")
            check(0 < len(w.get("meaning", "")) <= 12, f"word {w.get('word')!r} meaning 1-12")
        corpus = lesson_corpus(data)
        sentences = hw.get("sentences", [])
        check(2 <= len(sentences) <= 3, "2-3 model sentences")
        for i, s in enumerate(sentences, 1):
            tag = f"sentence {i}"
            check(0 < len(s.get("en", "")) <= 100, tag + " English length")
            check(compact(s.get("en", "")) in corpus, tag + " is a sentence the student met in the lesson")
            check(8 <= len(s.get("ja", "")) <= 60, tag + " Japanese 8-60")
            check(4 <= len(s.get("point", "")) <= 34, tag + " point 4-34")
            check(20 <= len(s.get("note", "")) <= 80, tag + " note 20-80")
            check(s.get("focus") in focus_ids, tag + " focus point exists")
    else:
        check(not hw.get("words") and not hw.get("sentences"), "words/sentences belong to the writing layout")
    return hw, errors


def build_index():
    index, errors = {}, []
    for path in sorted(HOMEWORK.glob("*/*.json")):
        hw, problems = validate(path)
        errors += problems
        star_key = "copy" if hw.get("layout") == "writing" else "translate"
        index[f"{path.parent.name}/{path.stem}"] = {
            "path": path.relative_to(ROOT).as_posix(),
            "layout": hw.get("layout", "grammar"),
            "title": hw.get("title", ""),
            "questions": len(hw.get("questions", [])),
            "translations": sum(1 for q in hw.get("questions", []) if q.get(star_key)),
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

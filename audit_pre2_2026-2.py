"""Regression audit of Grade Pre-2, 2026-2 (main venue, October 4).

The booklet has a text layer, so every English field (Part 1 text, choices,
question stems, passage sentences, email headers) is compared with the original
PDF directly, and the official answer sheet is parsed independently. After that
check the English payload is frozen by SOURCE_PAYLOAD_HASH.
Use --skip-sources only on hosts without the local original PDFs, and
--require-audio once data/grade-pre2/2026-2/_gen_tts.py has been run.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "data/grade-pre2/2026-2"
SOURCE = Path(r"D:\Files\英検過去問\準2級\準2級2026-2")
BOOKLET = "2026年度第2回_準2級_問題冊子.pdf"
ANSWERS = "2026年度第2回_準2級_解答.pdf"
HASHES = {
    BOOKLET: "f3fa3d66c0d8fcbae045e77229f6ecf7ac1e2f6cd2ed9b1478e55d9638e34e0d",
    ANSWERS: "f0adbef30932351b409908d68e164090ed93e101cf06c6daa2c019353f09575f",
}
READING = [4, 4, 4, 2, 4, 3, 3, 3, 1, 4, 2, 4, 2, 4, 3,
           3, 2, 1, 1, 4, 3, 1, 3, 1, 3, 2, 3, 4, 2]
LISTENING = [3, 3, 2, 3, 2, 3, 3, 2, 3, 3,
             1, 2, 1, 1, 2, 2, 2, 1, 3, 2,
             4, 1, 1, 1, 4, 3, 2, 2, 1, 3]
# Frozen after the text-layer comparison: original text, choices, stems, instructions.
SOURCE_PAYLOAD_HASH = "704b28058add6139f32a50d6e08b08d75c6c03d9a5a6f6f28cd0545eb0d691e6"
EXPECTED_SHAPE = [("A Dream", 2), ("A film event", 4), ("Days Without Meat", 4)]
EMAIL_META = {"from": "Megan White <megan.white-0211@w.g-college.net>", "to": "Alan Jones <alan.jones-0427@w.g-college.net>",
              "date": "December 9", "subject": "A film event"}
AUDIO_KEYS = ("wordAudio", "exampleAudio", "audioFile")
PRACTICE_PAGES = 10
NO_FINITE_VERB = {"Hi Alan,", "Thank you,", "Megan White"}
COLORS = ["#4f8cff", "#34d399", "#f472b6", "#fbbf24", "#f59e0b"]
# Each focus point practices exactly one original paragraph: (passage index, paragraph index).
FP_PARAGRAPHS = [(0, 0), (0, 1), (1, 2), (2, 3), (2, 1)]


def source_payload(data):
    result = []
    for section in data["sections"]:
        item = {k: section[k] for k in ("name", "nameEn", "type", "instruction")}

        def qsource(q):
            return {k: q[k] for k in ("number", "text", "question", "choices", "answer") if k in q}
        if "questions" in section:
            item["questions"] = [qsource(q) for q in section["questions"]]
        if "passages" in section:
            item["passages"] = [
                dict({k: p[k] for k in ("label", "title", "format", "meta", "paragraphs") if k in p},
                     questions=[qsource(q) for q in p["questions"]])
                for p in section["passages"]]
        result.append(item)
    return result


def source_digest(data):
    return hashlib.sha256(json.dumps(source_payload(data), ensure_ascii=False,
                                     separators=(",", ":")).encode("utf-8")).hexdigest()


def compact(s):
    return re.sub(r"\s+", "", s)


def pdf_norm(text):
    text = unicodedata.normalize("NFKC", text)  # ligatures and full-width brackets
    text = text.replace("\u00ad", "-").replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    text = re.sub(r"\(\s*\d*\s*\)", "()", text)
    return re.sub(r"\s+", "", text.replace("A : ", "A:").replace("B : ", "B:"))


def strip_audio(value):
    if isinstance(value, dict):
        return {k: strip_audio(v) for k, v in value.items() if k not in AUDIO_KEYS}
    if isinstance(value, list):
        return [strip_audio(v) for v in value]
    return value


def word_in(word, text):
    # Headwords are dictionary forms: "tidy up" must match "tidies up", "postpone" "postponed".
    tokens = [t for t in re.findall(r"[a-z]+", word.lower()) if t not in ("one", "s")]
    stems = [t[:-1] if len(t) > 3 and t.endswith(("e", "y")) else t for t in tokens]
    return all(re.search(r"\b" + re.escape(s), text.lower()) for s in stems)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    args = argparse.ArgumentParser()
    args.add_argument("--skip-sources", action="store_true")
    args.add_argument("--require-audio", action="store_true")
    args.add_argument("--show-source-hash", action="store_true")
    opts = args.parse_args()
    data = json.loads((BASE / "data.json").read_text(encoding="utf-8"))
    if opts.show_source_hash:
        print(source_digest(data))
        return
    errors = []

    def check(ok, msg):
        if not ok:
            errors.append(msg)

    passages = [p for s in data["sections"] for p in s.get("passages", [])]
    qs = [q for s in data["sections"] for q in s.get("questions", [])] + [q for p in passages for q in p["questions"]]

    if not opts.skip_sources:
        import fitz
        for name, digest in HASHES.items():
            path = SOURCE / name
            check(path.is_file(), f"missing original PDF: {name}")
            if path.is_file():
                check(hashlib.sha256(path.read_bytes()).hexdigest() == digest, f"source hash: {name}")
        answer_text = fitz.open(SOURCE / ANSWERS)[0].get_text()
        reading = {int(n): int(a) for n, a in re.findall(r"\((\d+)\)\s+([1-4])", answer_text)}
        listening = {int(n): int(a) for n, a in re.findall(r"No\.\s*(\d+)\s+([1-4])", answer_text)}
        check(reading == dict(enumerate(READING, 1)), "official reading answer PDF mismatch")
        check(listening == dict(enumerate(LISTENING, 1)), "official listening answer PDF mismatch")
        booklet = fitz.open(SOURCE / BOOKLET)
        corpus = pdf_norm("\n".join(booklet[i].get_text() for i in range(2, 11)))
        fields = [line for q in qs[:20] for line in q["text"].split("\n")]
        fields += [c for q in qs for c in q["choices"]] + [q["question"] for q in qs if q.get("question")]
        fields += [row[0] for p in passages for row in p["sentencePairs"]] + [p["title"] for p in passages]
        fields += list(EMAIL_META.values())
        missing = [f for f in fields if pdf_norm(f) not in corpus]
        check(not missing, f"{len(missing)} English fields differ from the booklet text layer: {missing[:3]}")

    check((data["grade"], data["year"], data["session"]) == ("準2級", "2026", "2"), "exam identity")
    check(source_digest(data) == SOURCE_PAYLOAD_HASH, "immutable original content fingerprint")
    check([s["type"] for s in data["sections"]] == ["vocabulary", "vocabulary", "passage-fill", "reading-comprehension"], "section types/order")
    check([q["number"] for q in qs] == list(range(1, 30)), "question sequence/count")
    check([q["answer"] for q in qs] == READING, "reading answers")
    check([len(p["questions"]) for p in passages] == [2, 3, 4], "passage question counts")
    lengths = []
    for q in qs:
        n = q["number"]
        for key in ("choices", "choiceTranslations", "choiceAnalysis"):
            check(len(q.get(key, [])) == 4, f"Q{n} {key} count")
        check(q.get("grammar", "").startswith("💡"), f"Q{n} grammar marker")
        for i, a in enumerate(q["choiceAnalysis"], 1):
            check(("→正解。💡" in a) == (i == q["answer"]), f"Q{n}/{i} correct marker")
            check(not a.startswith(("✅", "❌", "○")), f"Q{n}/{i} leading marker")
            if i == q["answer"]:
                check(bool(a.split("→正解。💡", 1)[-1].strip()), f"Q{n} empty evidence after 💡")
            lengths.append(len(a))
        if n <= 20:
            check(f"( {n} )" in q["text"] and f"( {n} )" in q["translation"], f"Q{n} bilingual blank")
        elif n <= 22:
            p = next(p for p in passages if q in p["questions"])
            check(f"( {n} )" in " ".join(p["paragraphs"]) and f"( {n} )" in " ".join(p["translations"]), f"Q{n} bilingual passage blank")
        else:
            check(bool(q.get("question") and q.get("questionTranslation")), f"Q{n} stem translation")
        if n >= 21:
            p = next(p for p in passages if q in p["questions"])
            check(bool(q.get("sourceEvidence")), f"Q{n} missing evidence")
            check(all(e in " ".join(p["paragraphs"]) for e in q["sourceEvidence"]), f"Q{n} nonliteral evidence")
    check(sum(lengths) / len(lengths) <= 65 and max(lengths) <= 120, "overlong choice analysis")

    check([(p["title"], len(p["paragraphs"])) for p in passages] == EXPECTED_SHAPE, "passage titles/paragraphs")
    for p in passages:
        name = p["title"]
        pairs = p["sentencePairs"]
        check(len(p["paragraphs"]) == len(p["translations"]), name + " paragraph translation count")
        check(compact(" ".join(p["paragraphs"])) == compact(" ".join(r[0] for r in pairs)), name + " full ordered English coverage")
        check(compact(" ".join(p["translations"])) == compact(" ".join(r[1] for r in pairs)), name + " full ordered Japanese coverage")
        for i, r in enumerate(pairs, 1):
            tag = f"{name}/{i}"
            check(len(r) == 4 and all(isinstance(x, str) for x in r) and all(r[:3]), tag + " four fields")
            chunks = [c.split("|") for c in r[2].split("||")]
            check(all(len(c) == 2 and all(c) for c in chunks), tag + " bilingual slash format")
            check(compact(" ".join(c[0] for c in chunks)) == compact(r[0]), tag + " slash English reconstruction")
            if r[3]:
                check(bool(re.search(r"(?<![A-Za-z])" + re.escape(r[3]) + r"(?![A-Za-z'])", r[0])), tag + " main verb token")
            else:
                # Only the greeting/signature lines and sentences whose verb is the answer blank.
                check(r[0] in NO_FINITE_VERB or bool(re.search(r"\( (2[12]) \)", r[0])),
                      tag + " missing main verb")
    email = passages[1]
    check(email.get("format") == "email" and email.get("meta") == EMAIL_META, "email original headers")
    check(email["paragraphs"][0].startswith("Hi Alan,\n"), "email greeting")
    check(email["paragraphs"][-1] == "Thank you,\nMegan White", "email closing/signature")

    vocab = data["vocabulary"]
    check(len(vocab) == 40 and len({v["word"] for v in vocab}) == 40, "40 unique balanced headwords")
    for section, selected in zip(data["sections"], [vocab[:17], vocab[17:23], vocab[23:29], vocab[29:]]):
        original = " ".join(q["text"] + " " + " ".join(q["choices"]) for q in section.get("questions", []))
        for p in section.get("passages", []):
            original += " " + " ".join(p["paragraphs"])
            original += " " + " ".join(q.get("question", "") + " " + " ".join(q["choices"]) for q in p["questions"])
        for v in selected:
            check(v["source"] == section["name"], "vocabulary source label: " + v["word"])
            check(v["sourceForm"].lower() in original.lower(), "balanced source vocabulary: " + v["word"])
            check(v["example"] not in original, "vocabulary example must be original: " + v["word"])
    for v in vocab:
        check(all(v.get(k) for k in ("word", "meaning", "pos", "level", "example", "distractors", "source", "sourceForm")), "incomplete vocab: " + v["word"])
        check(v["level"] == "準2級", "vocab level")
        check(len(v["distractors"]) == len(set(v["distractors"])) == 3 and v["meaning"] not in v["distractors"], "vocab distractors: " + v["word"])

    fps = data["lessonPlan"]["focusPoints"]
    check([fp["id"] for fp in fps] == [f"fp{i}" for i in range(1, 6)], "five focus-point ids")
    check(fps[-1]["title"] == "今回の重要なパラフレーズ" and fps[-1]["highlightLabel"] == "パラフレーズ", "FP5 paraphrase")
    old_titles = {fp["title"] for file in BASE.parent.glob("*/data.json") if file.parent != BASE
                  for fp in json.loads(file.read_text(encoding="utf-8")).get("lessonPlan", {}).get("focusPoints", [])[:4]}
    check(all(fp["title"] not in old_titles for fp in fps[:4]), "new grammar topics, no duplicate titles")
    corpus = " ".join(" ".join(p["paragraphs"]) for p in passages)
    filled = corpus
    for q in qs[20:22]:
        filled = filled.replace(f"( {q['number']} )", q["choices"][q["answer"] - 1])
    spans = []
    for fp, color, (pi, para_i) in zip(fps, COLORS, FP_PARAGRAPHS):
        tag = fp["id"]
        check(all(fp.get(k) for k in ("title", "subtitle", "explanation", "sourceQuote", "sourceLocation", "examples", "practicePassage", "practiceQuestions", "highlightPatterns", "highlightColor", "highlightLabel")), tag + " required fields")
        check(fp["highlightColor"] == color, tag + " standard color")
        check(len(fp["examples"]) == 3 and all(all(e.get(k) for k in ("en", "ja", "note")) for e in fp["examples"]), tag + " three bilingual examples")
        paragraph = passages[pi]["paragraphs"][para_i]
        check(any(e["en"] in paragraph for e in fp["examples"]), tag + " one example quoted from the practice paragraph")
        check(all(h in paragraph for h in fp["highlightPatterns"]), tag + " markers inside the practice paragraph")
        check(len(fp["practiceQuestions"]) == 4 and all(x.get("q") and x.get("a") for x in fp["practiceQuestions"]), tag + " four practice questions")
        check(len(fp["highlightPatterns"]) >= 3 and all(h in corpus for h in fp["highlightPatterns"]), tag + " literal highlight patterns")
        for h in fp["highlightPatterns"]:
            for m in re.finditer(re.escape(h), corpus):
                spans.append((m.start(), m.end(), tag, h))
        pp = fp["practicePassage"]
        check(pp["en"].startswith("[出典:") and bool(pp["ja"]) and "( " not in pp["ja"], tag + " labeled bilingual practice")
        body = pp["en"].split("\n", 1)[1]
        completed = paragraph
        for q in passages[pi]["questions"]:
            completed = completed.replace(f"( {q['number']} )", q["choices"][q["answer"] - 1])
        check(body == completed and "( " not in body, tag + " exactly one original paragraph, blanks filled")
        check(5 <= sum(row[0] in paragraph for row in passages[pi]["sentencePairs"]) <= 7, tag + " five to seven sentences")
    for a in spans:
        for b in spans:
            if a[2] < b[2] and a[0] < b[1] and b[0] < a[1]:
                errors.append(f"highlight overlap across focus points: {a[2]} '{a[3]}' / {b[2]} '{b[3]}'")

    audio_refs = [v.get(k) for v in vocab for k in ("wordAudio", "exampleAudio")] + [fp["practicePassage"].get("audioFile") for fp in fps]
    if opts.require_audio or any(audio_refs):
        check(all(audio_refs) and len(set(audio_refs)) == 85, "85 unique audio references (run _gen_tts.py)")
        for ref in filter(None, audio_refs):
            path = (BASE / ref).resolve()
            check(path.is_relative_to(BASE.resolve()) and path.is_file() and path.stat().st_size >= 500, "missing/incomplete audio: " + ref)
            if path.is_file():
                check(path.read_bytes()[:3] == b"ID3" or path.read_bytes()[:1] == b"\xff", "invalid MP3: " + ref)
    listening = {f"part{i + 1}": dict(zip(map(str, range(10 * i + 1, 10 * i + 11)), LISTENING[10 * i:10 * i + 10])) for i in range(3)}
    check(data["listening"] == listening, "listening answer map")

    from pypdf import PdfReader
    pdf = ROOT / "output/pdf/ReadPass_EIKEN_GradePre2_2026-2_Practice_Exam_Large_Type_v1.pdf"
    check(pdf.is_file(), "fixed exam PDF missing")
    if pdf.is_file():
        reader = PdfReader(pdf)
        check(len(reader.pages) == PRACTICE_PAGES, "fixed PDF page count")
        printed = compact(" ".join(page.extract_text() for page in reader.pages))
        original_fields = [q.get("text", q.get("question", "")) for q in qs]
        original_fields += [c for q in qs for c in q["choices"]]
        original_fields += [row[0] for p in passages for row in p["sentencePairs"]]
        check(all(compact(field.replace("A : ", "A: ").replace("B : ", "B: ")) in printed
                  or compact(field) in printed for field in original_fields), "fixed PDF must contain all source fields")
        printed_answers = {int(n): int(a) for n, a in re.findall(r"Q(\d+)\s+([1-4])", reader.pages[-1].extract_text())}
        check(printed_answers == dict(enumerate(READING, 1)), "fixed PDF official answer map")

    guides = json.loads((ROOT / "output/pdf/grammar_guides.json").read_text(encoding="utf-8"))
    check("grade-pre2/2026-2" in guides, "grammar guide PDF not built (scripts/build_grammar_guide_pdf.py)")

    top = (ROOT / "top.js").read_text(encoding="utf-8")
    prn = (ROOT / "print.js").read_text(encoding="utf-8")
    for name, text in (("top.js", top), ("print.js", prn)):
        start = text.index("exams: [", text.index("id: 'grade-pre2'"))
        block = text[start:text.index("]", start)]
        check(block.count("{ id: '2026-2',") == 1, f"{name}: grade-pre2 2026-2 entry must occur exactly once")
        check(block.find("{ id: '2026-1-sat'") < block.find("{ id: '2026-2',") < block.find("{ id: '2026-2-sat'"), f"{name}: 2026-2 order")
    check(prn.count("'grade-pre2/2026-2': {") == 1 and f"pages: {PRACTICE_PAGES}" in prn[prn.index("'grade-pre2/2026-2': {"):][:400], "print.js fixed PDF registration")
    for page, script in (("top.html", "top.js"), ("print.html", "print.js")):
        cache = re.search(re.escape(script) + r"\?v=(\d{8})-", (ROOT / page).read_text(encoding="utf-8"))
        check(bool(cache) and cache.group(1) >= "20261013", f"{page}: {script} cache version predates 2026-2")

    # Regenerate in isolation; audio references are added later by _gen_tts.py.
    with tempfile.TemporaryDirectory(prefix="readpass-p2-2026-2-") as folder:
        dest = Path(folder)
        for file in ROOT.glob("gen_pre2_2026-2*.py"):
            if "_sat" not in file.name:
                shutil.copyfile(file, dest / file.name)
        subprocess.run([sys.executable, str(dest / "gen_pre2_2026-2.py")], check=True, capture_output=True)
        fresh = json.loads((dest / "data/grade-pre2/2026-2/data.json").read_text(encoding="utf-8"))
        check(strip_audio(data) == fresh, "generator/JSON synchronization")
    for e in errors:
        print("ERROR:", e)
    audio_count = sum(1 for r in audio_refs if r)
    print(f"questions={len(qs)} vocabulary={len(vocab)} sentences={sum(len(p['sentencePairs']) for p in passages)} "
          f"focus={len(fps)} audio={audio_count}/85 analysis_avg={sum(lengths) / len(lengths):.1f} errors={len(errors)}")
    if errors:
        raise SystemExit(1)
    print("AUDIT OK: grade-pre2/2026-2; original PDFs, official answers, reproducible data, teaching fields"
          + (", audio" if audio_count else " (audio pending: run data/grade-pre2/2026-2/_gen_tts.py)"))


if __name__ == "__main__":
    main()

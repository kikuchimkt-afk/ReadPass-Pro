"""Regression audit of Grade 5, 2026-2 (main venue, October 4).

The booklet has a text layer, so every English field (Part 1-2 text and choices,
word-order chunks and frames) is compared with the original PDF directly; the
word-order Japanese sentences were checked against the rendered page. The official
answer sheet is parsed independently, and each word-order answer is re-derived from
the completed sentence. After that check the source payload is frozen by
SOURCE_PAYLOAD_HASH. Use --skip-sources only on hosts without the local original
PDFs, and --require-audio once data/grade5/2026-2/_gen_tts.py has been run.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "data/grade5/2026-2"
SOURCE = Path(r"D:\Files\英検過去問\5級\5級2026-2")
BOOKLET = "2026年度第2回_5級_問題冊子.pdf"
ANSWERS = "2026年度第2回_5級_解答.pdf"
HASHES = {
    BOOKLET: "0e4c55a3ac85dae55d073f914228a824686737d0ae1ffbd5002591fa5217a6d5",
    ANSWERS: "61cf3297e057dd51c927cff3702ba31ffc5e309c99a612f57d4c018c4a500c21",
}
READING = [1, 2, 1, 1, 4, 2, 1, 4, 3, 2, 4, 1, 2, 1, 2,
           2, 4, 1, 2, 4,
           2, 1, 4, 1, 3]
LISTENING = [2, 2, 2, 1, 2, 3, 3, 2, 3, 2,
             1, 4, 4, 3, 2,
             2, 3, 1, 3, 2, 2, 1, 3, 1, 3]
# Frozen after the text-layer comparison: original text, choices, chunks and frames.
SOURCE_PAYLOAD_HASH = "5e94ac2c019158b6f5579c56ee674626bb234b6c16ae9ec7ba1c23ea2a4ded06"
COMPLETED = ["John, which calendar do you want?",
             "My mother can't dance well.",
             "That volleyball player is from Italy.",
             "How much is a movie ticket?",
             "I'm not using the computer now."]
ORDER_PATTERNS = ["which calendar", "can't dance", "is from", "How much", "not using"]
AUDIO_KEYS = ("questionAudio", "wordAudio", "exampleAudio", "audio", "sourceQuoteAudio", "audioFile")
AUDIO_COUNT = 80
PRACTICE_PAGES = 6
COLORS = ["#4f8cff", "#34d399", "#a78bfa"]


def compact(s):
    return re.sub(r"\s+", "", s)


def pdf_norm(text):
    text = unicodedata.normalize("NFKC", text)  # ligatures and full-width spaces/brackets
    text = text.replace("\u00ad", "-").replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    text = re.sub(r"[\x00-\x1f]", "", text)  # the booklets put control characters between speaker and colon
    text = re.sub(r"\(\s*\d*\s*\)", "()", text)
    return re.sub(r"\s+", "", text)


def payload(d):
    def question(q):
        return {k: q[k] for k in ("number", "text", "choices", "answer", "words", "correctOrder",
                                  "framePrefix", "frameSuffix", "answerSlots") if k in q}
    return [dict({k: s[k] for k in ("name", "nameEn", "type", "instruction")}, questions=[question(q) for q in s["questions"]])
            for s in d["sections"]]


def digest(d):
    return hashlib.sha256(json.dumps(payload(d), ensure_ascii=False, separators=(",", ":")).encode()).hexdigest()


def strip_audio(value):
    if isinstance(value, dict):
        return {k: strip_audio(v) for k, v in value.items() if k not in AUDIO_KEYS}
    if isinstance(value, list):
        return [strip_audio(v) for v in value]
    return value


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser()
    parser.add_argument("--skip-sources", action="store_true")
    parser.add_argument("--require-audio", action="store_true")
    parser.add_argument("--show-source-hash", action="store_true")
    args = parser.parse_args()
    d = json.loads((BASE / "data.json").read_text(encoding="utf-8"))
    if args.show_source_hash:
        print(digest(d))
        return
    errors = []

    def check(ok, msg):
        if not ok:
            errors.append(msg)

    sections = d["sections"]
    qs = [q for s in sections for q in s["questions"]]
    orders = sections[2]["questions"]

    if not args.skip_sources:
        import fitz
        for name, h in HASHES.items():
            path = SOURCE / name
            check(path.is_file(), "missing original PDF: " + name)
            if path.is_file():
                check(hashlib.sha256(path.read_bytes()).hexdigest() == h, "original PDF hash: " + name)
        answer = fitz.open(SOURCE / ANSWERS)[0].get_text()
        key = {int(n): int(a) for n, a in re.findall(r"\((\d+)\)\s+([1-4])", answer)}
        lkey = {int(n): int(a) for n, a in re.findall(r"No\.\s*(\d+)\s+([1-4])", answer)}
        check(key == dict(enumerate(READING, 1)), "official reading key")
        check(lkey == dict(enumerate(LISTENING, 1)), "official listening key")
        booklet = fitz.open(SOURCE / BOOKLET)
        corpus = pdf_norm("\n".join(booklet[i].get_text() for i in range(1, 5)))
        fields = [line for q in qs[:20] for line in q["text"].split("\n")] + [c for q in qs[:20] for c in q["choices"]]
        fields += [w for q in orders for w in q["words"]] + [q[k] for q in orders for k in ("framePrefix", "frameSuffix") if q[k]]
        missing = [f for f in fields if pdf_norm(f) not in corpus]
        check(not missing, f"{len(missing)} English fields differ from the booklet text layer: {missing[:3]}")

    check(digest(d) == SOURCE_PAYLOAD_HASH, "frozen text-layer-verified source content")
    check((d["grade"], d["year"], d["exam"], d["session"]) == ("grade5", "2026", "2026-2", "2026-2"), "exam identity")
    check(d["title"] == "英検5級 2026年度 第2回", "exam title")
    check([s["type"] for s in sections] == ["vocabulary", "vocabulary", "sentence-order"], "original sections")
    check([len(s["questions"]) for s in sections] == [15, 5, 5], "section counts")
    check([q["number"] for q in qs] == list(range(1, 26)), "Q1-Q25 sequence")
    check([q["answer"] for q in qs] == READING, "25 official answers")
    for q in qs:
        n = q["number"]
        for field in ("choices", "choiceAnalysis", "choiceAnalysisSimple"):
            check(len(q[field]) == 4 and all(q[field]), f"Q{n} {field} count")
        for field in ("choiceAnalysis", "choiceAnalysisSimple"):
            check([i for i, a in enumerate(q[field], 1) if a.startswith("○")] == [q["answer"]], f"Q{n} {field} correct marker")
            check(all(len(a) >= 12 for a in q[field]), f"Q{n} {field} substantive")
            check(not any("。。" in a for a in q[field]), f"Q{n} {field} doubled period")
        check(len(q["grammar"]) >= 25 and len(q["grammarSimple"]) >= 25, f"Q{n} normal/easy explanation")
        if n <= 20:
            check("(　)" in q["text"] and "(　)" in q["translation"], f"Q{n} retained bilingual blank")
            check(q["text"].count("\n") == q["translation"].count("\n"), f"Q{n} speaker lines")
            check(len(q["choiceTranslations"]) == 4, f"Q{n} four option meanings")

    o = load("g5_2026_2_order", ROOT / "gen_g5_2026-2_order.py")
    for q, expected, pattern in zip(orders, COMPLETED, ORDER_PATTERNS):
        n = q["number"]
        check(len(q["words"]) == 4 and sorted(q["correctOrder"]) == [1, 2, 3, 4], f"Q{n} four intact chunks")
        check(q["answerSlots"] == [1, 3], f"Q{n} first/third answer positions")
        pair = "−".join("①②③④"[q["correctOrder"][slot - 1] - 1] for slot in q["answerSlots"])
        check(pair == q["choices"][q["answer"] - 1], f"Q{n} derived answer vs official key")
        check(o.completed(q) == expected, f"Q{n} completed sentence")
        check(expected in q["grammar"] and pattern.lower() in q["grammar"].lower(), f"Q{n} construction rationale")
        check("1番目" in q["grammar"] and "3番目" in q["grammar"], f"Q{n} explained positions")
        check(q["translation"] == q["text"] and "choiceTranslations" not in q, f"Q{n} existing Grade 5 schema")
        for c, a, e in zip(q["choices"], q["choiceAnalysis"], q["choiceAnalysisSimple"]):
            words = [q["words"]["①②③④".index(t)] for t in c if t in "①②③④"]
            check(all(w in a and w in e for w in words), f"Q{n} candidate-specific placements")
    check("1番目と3番目" in sections[2]["instruction"] and "①から④" in sections[2]["instruction"] and "小文字" in sections[2]["instruction"], "original word-order instructions")

    corpus = " ".join(q["text"].replace("(　)", q["choices"][q["answer"] - 1]) for q in qs[:20]) + " " + " ".join(COMPLETED)
    vocab = d["vocabulary"]
    check(len(vocab) == len({v["word"] for v in vocab}) == 20, "20 distinct vocabulary items")
    for v in vocab:
        check(v["sourceForm"].lower() in corpus.lower(), "source vocabulary " + v["word"])
        check(v["level"] == "5級" and len(set(v["distractors"])) == 3 and v["meaning"] not in v["distractors"], "vocabulary options " + v["word"])
        check(bool(v["example"] and v["exampleJa"]), "bilingual example " + v["word"])
        check(compact(v["example"]) not in compact(corpus), "vocabulary example is original " + v["word"])

    tts = load("g5_2026_2_tts", BASE / "_gen_tts.py")
    work = tts.jobs(d)
    jobmap = dict(work)
    for q, expected in zip(orders, COMPLETED):
        check(jobmap[f"audio/q{q['number']}.mp3"] == expected, f"Q{q['number']} audio reads the completed sentence")
    fps = d["lessonPlan"]["focusPoints"]
    check([f["id"] for f in fps] == ["fp1", "fp2", "fp3"], "three existing-format focus points")
    check([f["highlightColor"] for f in fps] == COLORS, "standard Grade 5 colors")
    source_units = [q["text"].replace("(　)", q["choices"][q["answer"] - 1]) for q in qs[:20]] + COMPLETED
    spans = []
    for f in fps:
        check(all(f.get(k) for k in ("title", "subtitle", "explanation", "explanationSimple", "sourceQuote", "sourceLocation", "highlightColor", "highlightLabel")),
              f["id"] + " normal/easy lesson")
        check(len(f["examples"]) == 3 and all(all(e.get(k) for k in ("en", "ja", "note", "noteSimple")) for e in f["examples"]), f["id"] + " three bilingual examples")
        check(len(f["practiceQuestions"]) == len(f["practiceQuestionsSimple"]) == 3, f["id"] + " three normal/easy challenges")
        check(len(f["highlightPatterns"]) >= 3 and all(p.lower() in corpus.lower() for p in f["highlightPatterns"]), f["id"] + " literal highlights")
        for pattern in f["highlightPatterns"]:
            spans += [(m.start(), m.end(), f["id"], pattern) for m in re.finditer(re.escape(pattern), corpus)]
        check(all(compact(part) in compact(corpus) for part in f["sourceQuote"].split(" / ")), f["id"] + " literal source quote")
        check(all(compact(e["en"]) in compact(corpus) for e in f["examples"]), f["id"] + " original examples")
        remaining = compact(re.sub(r"\[出典:.*?\]\n?", "", f["practicePassage"]["en"]))
        for unit in sorted(source_units, key=len, reverse=True):
            remaining = remaining.replace(compact(unit), "")
        check(not remaining, f["id"] + " practice made of intact original sentences")
        spoken = jobmap[f"audio/practice_pp{f['id'][2:]}.mp3"]
        check("[出典:" not in spoken and not re.search(r"(?m)^[A-Z][a-z]*(?: \d)?:", spoken), f["id"] + " spoken text excludes labels and speakers")
    for a in spans:
        for b in spans:
            if a[2] < b[2] and a[0] < b[1] and b[0] < a[1]:
                errors.append(f"highlight overlap across focus points: {a[2]} '{a[3]}' / {b[2]} '{b[3]}'")

    refs = [ref for ref, _ in work]
    check(len(refs) == len(set(refs)) == AUDIO_COUNT, f"{AUDIO_COUNT} audio jobs")
    linked = [q.get("questionAudio") for q in qs] + [r for v in vocab for r in (v.get("wordAudio"), v.get("exampleAudio"))]
    linked += [r for f in fps for r in [e.get("audio") for e in f["examples"]] + [f.get("sourceQuoteAudio"), f["practicePassage"].get("audioFile")]]
    if args.require_audio or any(linked):
        check(sorted(filter(None, linked)) == sorted(refs), f"{AUDIO_COUNT} linked audio references (run _gen_tts.py)")
        actual = {p.relative_to(BASE).as_posix() for p in (BASE / "audio").rglob("*.mp3")} if (BASE / "audio").is_dir() else set()
        check(actual == set(refs), "audio files: no missing/orphans")
        for ref in refs:
            path = BASE / ref
            # A single word is about 11 KB at this voice/rate; a truncated stream once saved 2 KB.
            check(path.is_file() and path.stat().st_size >= 6000, "missing/truncated audio: " + ref)
    check([len(d["listening"][f"part{i}"]) for i in range(1, 4)] == [10, 5, 10], "original listening partitions")
    check([a for i in range(1, 4) for a in d["listening"][f"part{i}"].values()] == LISTENING, "listening key")

    from pypdf import PdfReader
    pdf = ROOT / "output/pdf/ReadPass_EIKEN_Grade5_2026-2_Practice_Exam_Large_Type_v1.pdf"
    check(pdf.is_file(), "fixed exam PDF missing")
    if pdf.is_file():
        reader = PdfReader(pdf)
        check(len(reader.pages) == PRACTICE_PAGES, f"{PRACTICE_PAGES}-page practice PDF")
        printed = " ".join(p.extract_text() for p in reader.pages)
        for q in qs:
            if q["number"] <= 20:
                check(compact(q["text"].replace("(　)", "( )")) in compact(printed), f"PDF Q{q['number']} full stem")
            for c in q["choices"]:
                check(compact(c.replace("−", "-")) in compact(printed), f"PDF Q{q['number']} choice {c}")
        ordertext = reader.pages[4].extract_text()
        check(len(re.findall(r"(?m)^1番目$", ordertext)) == 5 and len(re.findall(r"(?m)^3番目$", ordertext)) == 5, "PDF first/third highlighted slots")
        for q in orders:
            check(all(compact(w) in compact(ordertext) for w in q["words"]), f"PDF Q{q['number']} intact chunks")
            check(all(compact(q[k]) in compact(ordertext) for k in ("text", "framePrefix", "frameSuffix")), f"PDF Q{q['number']} Japanese/fixed frame")
        printedkey = {int(n): int(a) for n, a in re.findall(r"Q(\d\d)\s+([1-4])\s", reader.pages[-1].extract_text())}
        check(printedkey == dict(enumerate(READING, 1)), "PDF official answer key")

    guides = json.loads((ROOT / "output/pdf/grammar_guides.json").read_text(encoding="utf-8"))
    check("grade5/2026-2" in guides, "grammar guide PDF not built (scripts/build_grammar_guide_pdf.py)")
    top = (ROOT / "top.js").read_text(encoding="utf-8")
    prn = (ROOT / "print.js").read_text(encoding="utf-8")
    for name, text in (("top.js", top), ("print.js", prn)):
        start = text.index("exams: [", text.index("id: 'grade5'"))
        block = text[start:text.index("]", start)]
        check(block.count("{ id: '2026-2',") == 1, f"{name}: grade5 2026-2 entry must occur exactly once")
        check(block.find("{ id: '2026-1-sat'") < block.find("{ id: '2026-2',") < block.find("{ id: '2026-2-sat'"), f"{name}: 2026-2 order")
    check(prn.count("'grade5/2026-2': {") == 1 and f"pages: {PRACTICE_PAGES}" in prn[prn.index("'grade5/2026-2': {"):][:400], "print.js fixed PDF registration")
    for page, script in (("top.html", "top.js"), ("print.html", "print.js")):
        cache = re.search(re.escape(script) + r"\?v=(\d{8})-", (ROOT / page).read_text(encoding="utf-8"))
        check(bool(cache) and cache.group(1) >= "20261013", f"{page}: {script} cache version predates 2026-2")

    # Regenerate in isolation; audio references are added later by _gen_tts.py.
    with tempfile.TemporaryDirectory(prefix="readpass-g5-2026-2-") as folder:
        dest = Path(folder)
        for script in ROOT.glob("gen_g5_2026-2*.py"):
            if "_sat" not in script.name:
                shutil.copy2(script, dest / script.name)
        proc = subprocess.run([sys.executable, str(dest / "gen_g5_2026-2.py")], capture_output=True, text=True, encoding="utf-8")
        check(proc.returncode == 0, "isolated generator execution")
        if proc.returncode == 0:
            fresh = json.loads((dest / "data/grade5/2026-2/data.json").read_text(encoding="utf-8"))
            check(strip_audio(d) == fresh, "generator/JSON synchronization")
    for error in errors:
        print("ERROR:", error)
    audio_count = sum(1 for r in linked if r)
    print(f"Grade 5 2026-2: {len(qs)} questions / 5 word orders / {len(vocab)} vocab / {len(fps)} focus points / "
          f"audio {audio_count}/{AUDIO_COUNT}; {len(errors)} errors")
    if errors:
        raise SystemExit(1)
    print("AUDIT OK: grade5/2026-2; original PDFs, official answers, reproducible data, teaching fields"
          + (", audio" if audio_count else " (audio pending: run data/grade5/2026-2/_gen_tts.py)"))


if __name__ == "__main__":
    main()

"""Regression audit of Grade 4, 2026-2 (main venue, October 4).

The booklet has a text layer, so every English field (Part 1-2 text and choices,
word-order chunks and frames, reading stems, choices, passage sentences and e-mail
headers) is compared with the original PDF directly; the word-order Japanese
sentences were checked against the rendered page. The official answer sheet is
parsed independently, and each word-order answer is re-derived from the completed
sentence. After that check the source payload is frozen by SOURCE_PAYLOAD_HASH.
Use --skip-sources only on hosts without the local original PDFs, and
--require-audio once data/grade4/2026-2/_gen_tts.py has been run.
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
BASE = ROOT / "data/grade4/2026-2"
SOURCE = Path(r"D:\Files\英検過去問\4級\4級2026-2")
BOOKLET = "2026年度第2回_4級_問題冊子.pdf"
ANSWERS = "2026年度第2回_4級_解答.pdf"
HASHES = {
    BOOKLET: "25e2421399fa611194864adff49a40ed84ba7d55023881560fbc97452da68117",
    ANSWERS: "da29c4c27a4cfc7acd9c025daaeb9b7b464b572c59863f7aaa52f285127abdf5",
}
READING = [1, 1, 4, 3, 4, 1, 4, 2, 2, 1, 4, 1, 3, 3, 2,
           4, 1, 4, 3, 1,
           2, 1, 2, 2, 1,
           2, 2, 2, 4, 1, 3, 1, 3, 4, 1]
LISTENING = [3, 3, 1, 2, 3, 3, 3, 2, 3, 3,
             3, 4, 2, 1, 4, 3, 2, 1, 1, 1,
             4, 3, 2, 3, 3, 1, 4, 3, 1, 4]
# Frozen after the text-layer comparison: original text, choices, chunks, frames, passages.
SOURCE_PAYLOAD_HASH = "9e2ad6ee2c30ee84801345f79a2354f732c582aeed7e91eb73fee77b739f6e31"
COMPLETED = ["Peter practiced kicking the ball before the soccer game.",
             "You must be quiet in the library.",
             "I left home for school at five o'clock yesterday morning.",
             "That shop has many kinds of ice cream.",
             "This desk is too big for Jack."]
ORDER_PATTERNS = ["practiced kicking", "must be quiet", "left home for school", "many kinds of", "too big for"]
AUDIO_KEYS = ("questionAudio", "wordAudio", "exampleAudio", "audio", "sourceQuoteAudio", "audioFile")
AUDIO_COUNT = 105
PRACTICE_PAGES = 11
FRAGMENTS = {"Information from the School Nurse", "Write soon,", "Keep in touch,", "Tom", "Grandpa"}
COLORS = ["#4f8cff", "#34d399", "#a78bfa", "#f472b6"]


def compact(s):
    return re.sub(r"\s+", "", s)


def pdf_norm(text):
    text = unicodedata.normalize("NFKC", text)  # ligatures and full-width spaces/brackets
    text = text.replace("\u00ad", "-").replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    text = re.sub(r"[\x00-\x1f]", "", text)  # the booklet puts control characters between speaker and colon
    text = re.sub(r"\(\s*\d*\s*\)", "()", text)
    return re.sub(r"\s+", "", text)


def payload(d):
    def question(q):
        return {k: q[k] for k in ("number", "text", "question", "choices", "answer", "words", "correctOrder",
                                  "framePrefix", "frameSuffix", "answerSlots") if k in q}
    result = []
    for s in d["sections"]:
        item = {k: s[k] for k in ("name", "nameEn", "type", "instruction")}
        if "questions" in s:
            item["questions"] = [question(q) for q in s["questions"]]
        if "passages" in s:
            item["passages"] = [dict({k: p[k] for k in ("label", "title", "format", "instruction", "paragraphs") if k in p},
                                     questions=[question(q) for q in p["questions"]]) for p in s["passages"]]
        result.append(item)
    return result


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
    passages = sections[3]["passages"]
    qs = [q for s in sections for q in s.get("questions", [])] + [q for p in passages for q in p["questions"]]
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
        corpus = pdf_norm("\n".join(booklet[i].get_text() for i in range(1, 11)))
        fields = [line for q in qs[:20] for line in q["text"].split("\n")]
        fields += [c for q in qs if q["number"] <= 20 or q["number"] >= 26 for c in q["choices"]]
        fields += [q["question"] for q in qs if q.get("question")]
        fields += [w for q in orders for w in q["words"]] + [q[k] for q in orders for k in ("framePrefix", "frameSuffix") if q[k]]
        fields += [r[0] for p in passages for r in p["sentencePairs"]] + [passages[0]["title"], passages[2]["title"]]
        fields += [v for e in passages[1]["emails"] for v in e["meta"].values()]
        missing = [f for f in fields if pdf_norm(f) not in corpus]
        check(not missing, f"{len(missing)} English fields differ from the booklet text layer: {missing[:3]}")

    check(digest(d) == SOURCE_PAYLOAD_HASH, "frozen text-layer-verified source content")
    check((d["grade"], d["year"], d["exam"], d["session"]) == ("grade4", "2026", "2026-2", "2026-2"), "exam identity")
    check(d["title"] == "英検4級 2026年度 第2回", "exam title")
    check([s["type"] for s in sections] == ["vocabulary", "vocabulary", "sentence-order", "reading-comprehension"], "section types")
    check([len(s.get("questions", [])) or sum(len(p["questions"]) for p in s["passages"]) for s in sections] == [15, 5, 5, 10], "section counts")
    check([q["number"] for q in qs] == list(range(1, 36)), "Q1-Q35 sequence")
    check([q["answer"] for q in qs] == READING, "35 official answers")
    check([len(p["questions"]) for p in passages] == [2, 3, 5], "reading counts")
    for q in qs:
        n = q["number"]
        for field in ("choices", "choiceAnalysis", "choiceAnalysisSimple"):
            check(len(q[field]) == 4 and all(q[field]), f"Q{n} {field} count")
        for field in ("choiceAnalysis", "choiceAnalysisSimple"):
            check([i for i, a in enumerate(q[field], 1) if a.startswith("○")] == [q["answer"]], f"Q{n} {field} correct marker")
            check(all(len(a) >= 12 for a in q[field]), f"Q{n} {field} substantive")
            check(not any("。。" in a for a in q[field]), f"Q{n} {field} doubled period")
        check(len(q["grammar"]) >= 25 and len(q["grammarSimple"]) >= 25, f"Q{n} explanation depth")
        if n <= 20:
            check("(　)" in q["text"] and "(　)" in q["translation"], f"Q{n} retained bilingual blank")
            check(q["text"].count("\n") == q["translation"].count("\n"), f"Q{n} speaker lines")
        if n <= 20 or n >= 26:
            check(len(q["choiceTranslations"]) == 4, f"Q{n} choice translations")
        if n >= 26:
            p = next(p for p in passages if q in p["questions"])
            check(bool(q["questionTranslation"]), f"Q{n} stem translation")
            check(bool(q["sourceEvidence"]) and all(e in " ".join(p["paragraphs"]) for e in q["sourceEvidence"]), f"Q{n} literal reading evidence")

    o = load("g4_2026_2_order", ROOT / "gen_g4_2026-2_order.py")
    for q, expected, pattern in zip(orders, COMPLETED, ORDER_PATTERNS):
        n = q["number"]
        check(len(q["words"]) == 5 and sorted(q["correctOrder"]) == [1, 2, 3, 4, 5], f"Q{n} five intact chunks")
        check(q["answerSlots"] == [2, 4], f"Q{n} answer positions")
        pair = "−".join("①②③④⑤"[q["correctOrder"][slot - 1] - 1] for slot in q["answerSlots"])
        check(pair == q["choices"][q["answer"] - 1], f"Q{n} derived 2nd/4th answer vs official key")
        check(o.completed(q) == expected, f"Q{n} completed sentence")
        check(expected in q["grammar"] and pattern.lower() in q["grammar"].lower(), f"Q{n} construction explanation")
        check("2番目" in q["grammar"] and "4番目" in q["grammar"], f"Q{n} explained positions")
        check("translation" not in q and "choiceTranslations" not in q, f"Q{n} no misleading translation field")
        for c, a, e in zip(q["choices"], q["choiceAnalysis"], q["choiceAnalysisSimple"]):
            words = [q["words"]["①②③④⑤".index(token)] for token in c if token in "①②③④⑤"]
            check(all(w in a and w in e for w in words), f"Q{n} each actual candidate placement")
    check("2番目と4番目" in sections[2]["instruction"] and "小文字" in sections[2]["instruction"], "original word-order instruction")

    check([len(p["sentencePairs"]) for p in passages] == [7, 29, 16], "52 explicit bilingual rows, including title/headers")
    check([len(p["paragraphs"]) for p in passages] == [5, 4, 3], "notice 5 / e-mail 4 / story 3 paragraphs")
    check(passages[0]["paragraphs"][0] == passages[0]["title"], "notice title paragraph")
    check(passages[0]["paragraphs"][3] == "Time: From 3:30 p.m. to 4:30 p.m.\nPlace: The meeting room (next to the art room)", "notice time/place lines")
    for p in passages:
        pairs = p["sentencePairs"]
        check(len(p["paragraphs"]) == len(p["translations"]), p["label"] + " translations")
        check(compact(" ".join(p["paragraphs"])) == compact(" ".join(r[0] for r in pairs)), p["label"] + " ordered English coverage")
        check(compact(" ".join(p["translations"])) == compact(" ".join(r[1] for r in pairs)), p["label"] + " ordered Japanese coverage")
        for i, r in enumerate(pairs, 1):
            tag = f"{p['label']} sentence {i}"
            chunks = [s.split("|") for s in r[2].split("||")]
            check(len(r) == 4 and all(r[:3]) and all(len(c) == 2 and all(c) for c in chunks), tag + " bilingual slash units")
            check(compact(" ".join(c[0] for c in chunks)) == compact(r[0]), tag + " slash reconstruction")
            if r[3]:
                check(len(chunks) >= 2 and bool(re.search(r"\b" + re.escape(r[3]) + r"\b", r[0])), tag + " finite verb")
            else:
                check(r[0].startswith(("From:", "To:", "Date:", "Subject:", "Hi ", "Time:", "Place:", "How about")) or r[0] in FRAGMENTS, tag + " justified no finite verb")
    emails = passages[1]["emails"]
    check(passages[1]["format"] == "multi-email" and len(emails) == 2, "two native email cards")
    for i, email in enumerate(emails):
        check(email["body"] == passages[1]["paragraphs"][2 * i + 1], "email body parity")
        check(email["translation"] == passages[1]["translations"][2 * i + 1], "email translation parity")
        check(set(email["meta"]) == {"from", "to", "date", "subject"} and email["meta"]["date"] == "May 17", "four original email headers")
        check(len(email["body"].splitlines()) == 4, "separate greeting/body/sign-off/name")

    corpus = " ".join(q["text"].replace("(　)", q["choices"][q["answer"] - 1]) for q in qs if q["number"] <= 20) + " " + \
        " ".join(COMPLETED) + " " + " ".join(x for p in passages for x in [p["title"], *p["paragraphs"]])
    v = d["vocabulary"]
    check(len(v) == 30 and len({x["word"] for x in v}) == 30, "30 distinct vocabulary items")
    for x in v:
        check(x["sourceForm"].lower() in corpus.lower(), "source vocabulary " + x["word"])
        check(x["level"] == "4級" and len(set(x["distractors"])) == 3 and x["meaning"] not in x["distractors"], "vocabulary choices " + x["word"])
        check(bool(x["example"] and x["exampleJa"]), "vocabulary bilingual example " + x["word"])
        check(compact(x["example"]) not in compact(corpus), "vocabulary example is original " + x["word"])

    tts = load("g4_2026_2_tts", BASE / "_gen_tts.py")
    work = tts.jobs(d)
    jobmap = dict(work)
    for q, expected in zip(orders, COMPLETED):
        check(jobmap[f"audio/q{q['number']}.mp3"] == expected, f"Q{q['number']} audio reads the completed sentence")
    fps = d["lessonPlan"]["focusPoints"]
    check([f["id"] for f in fps] == ["fp1", "fp2", "fp3", "fp4"], "four focus points")
    check([f["highlightColor"] for f in fps] == COLORS, "standard Grade 4 colors")
    source_units = [q["text"].replace("(　)", q["choices"][q["answer"] - 1]) for q in qs if q["number"] <= 20] + COMPLETED + \
        [r[0] for p in passages for r in p["sentencePairs"]]
    spans = []
    for f in fps:
        check(all(f.get(k) for k in ("title", "subtitle", "explanation", "explanationSimple", "sourceQuote", "sourceLocation", "highlightColor", "highlightLabel")),
              f["id"] + " normal/easy lessons")
        check(len(f["examples"]) == 3 and all(all(e.get(k) for k in ("en", "ja", "note", "noteSimple")) for e in f["examples"]), f["id"] + " three bilingual examples")
        check(len(f["practiceQuestions"]) == len(f["practiceQuestionsSimple"]) == 3, f["id"] + " three normal/easy challenges")
        check(len(f["highlightPatterns"]) >= 3 and all(pattern.lower() in corpus.lower() for pattern in f["highlightPatterns"]), f["id"] + " literal highlights")
        for pattern in f["highlightPatterns"]:
            spans += [(m.start(), m.end(), f["id"], pattern) for m in re.finditer(re.escape(pattern), corpus)]
        check(all(compact(part) in compact(corpus) for part in f["sourceQuote"].split(" / ")), f["id"] + " literal source quote")
        for example in f["examples"]:
            check(compact(example["en"]) in compact(corpus), f["id"] + " source example")
        remaining = compact(re.sub(r"\[出典:.*?\]\n?", "", f["practicePassage"]["en"]))
        for unit in sorted(source_units, key=len, reverse=True):
            remaining = remaining.replace(compact(unit), "")
        check(not remaining, f["id"] + " practice made of intact original sentences")
        check(bool(f["practicePassage"]["ja"]), f["id"] + " practice translation")
        spoken = jobmap[f"audio/practice_pp{f['id'][2:]}.mp3"]
        check("[出典:" not in spoken and not re.search(r"(?m)^[A-Z][a-z]*(?: \d)?:", spoken), f["id"] + " spoken text excludes labels and speakers")
    for a in spans:
        for b in spans:
            if a[2] < b[2] and a[0] < b[1] and b[0] < a[1]:
                errors.append(f"highlight overlap across focus points: {a[2]} '{a[3]}' / {b[2]} '{b[3]}'")

    refs = [ref for ref, _ in work]
    check(len(refs) == len(set(refs)) == AUDIO_COUNT, f"{AUDIO_COUNT} audio jobs")
    linked = [q.get("questionAudio") for s in sections for q in s.get("questions", [])]
    linked += [r for x in v for r in (x.get("wordAudio"), x.get("exampleAudio"))]
    linked += [r for f in fps for r in [e.get("audio") for e in f["examples"]] + [f.get("sourceQuoteAudio"), f["practicePassage"].get("audioFile")]]
    if args.require_audio or any(linked):
        check(sorted(filter(None, linked)) == sorted(refs), f"{AUDIO_COUNT} linked audio references (run _gen_tts.py)")
        check(all("questionAudio" not in q for p in passages for q in p["questions"]), "no reading-question audio")
        actual = {p.relative_to(BASE).as_posix() for p in (BASE / "audio").rglob("*.mp3")} if (BASE / "audio").is_dir() else set()
        check(actual == set(refs), "audio files: no missing/orphans")
        for ref in refs:
            path = BASE / ref
            # A single word is about 11 KB at this voice/rate; a truncated stream once saved 2 KB.
            check(path.is_file() and path.stat().st_size >= 6000, "missing/truncated audio: " + ref)
    check([int(d["listening"][f"part{i // 10 + 1}"][str(i + 1)]) for i in range(30)] == LISTENING, "stored listening key")

    from pypdf import PdfReader
    pdf = ROOT / "output/pdf/ReadPass_EIKEN_Grade4_2026-2_Practice_Exam_Large_Type_v1.pdf"
    check(pdf.is_file(), "fixed exam PDF missing")
    if pdf.is_file():
        reader = PdfReader(pdf)
        check(len(reader.pages) == PRACTICE_PAGES, f"{PRACTICE_PAGES}-page practice PDF")
        printed = " ".join(p.extract_text() for p in reader.pages)
        for q in qs:
            if q["number"] <= 20:
                check(compact(q["text"].replace("(　)", "( )")) in compact(printed), f"PDF Q{q['number']} full stem")
            elif q["number"] >= 26:
                check(compact(q["question"]) in compact(printed), f"PDF Q{q['number']} stem")
            for c in q["choices"]:
                check(compact(c.replace("−", "-")) in compact(printed), f"PDF Q{q['number']} choice {c}")
        ordertext = reader.pages[4].extract_text()
        check(len(re.findall(r"(?m)^2番目$", ordertext)) == 5 and len(re.findall(r"(?m)^4番目$", ordertext)) == 5, "PDF highlighted 2nd/4th slot labels")
        for q in orders:
            check(all(compact(w) in compact(ordertext) for w in q["words"]), f"PDF Q{q['number']} intact chunks")
            check(compact(q["framePrefix"]) in compact(ordertext) and compact(q["frameSuffix"]) in compact(ordertext), f"PDF Q{q['number']} original frame")
        for p in passages:
            check(all(compact(para) in compact(printed) for para in p["paragraphs"]), p["label"] + " complete PDF passage")
        printedkey = {int(n): int(a) for n, a in re.findall(r"Q(\d\d)\s+([1-4])\s", reader.pages[-1].extract_text())}
        check(printedkey == dict(enumerate(READING, 1)), "PDF official key parity")

    guides = json.loads((ROOT / "output/pdf/grammar_guides.json").read_text(encoding="utf-8"))
    check("grade4/2026-2" in guides, "grammar guide PDF not built (scripts/build_grammar_guide_pdf.py)")
    top = (ROOT / "top.js").read_text(encoding="utf-8")
    prn = (ROOT / "print.js").read_text(encoding="utf-8")
    for name, text in (("top.js", top), ("print.js", prn)):
        start = text.index("exams: [", text.index("id: 'grade4'"))
        block = text[start:text.index("]", start)]
        check(block.count("{ id: '2026-2',") == 1, f"{name}: grade4 2026-2 entry must occur exactly once")
        check(block.find("{ id: '2026-1-sat'") < block.find("{ id: '2026-2',") < block.find("{ id: '2026-2-sat'"), f"{name}: 2026-2 order")
    check(prn.count("'grade4/2026-2': {") == 1 and f"pages: {PRACTICE_PAGES}" in prn[prn.index("'grade4/2026-2': {"):][:400], "print.js fixed PDF registration")
    for page, script in (("top.html", "top.js"), ("print.html", "print.js")):
        cache = re.search(re.escape(script) + r"\?v=(\d{8})-", (ROOT / page).read_text(encoding="utf-8"))
        check(bool(cache) and cache.group(1) >= "20261013", f"{page}: {script} cache version predates 2026-2")

    # Regenerate in isolation; audio references are added later by _gen_tts.py.
    with tempfile.TemporaryDirectory(prefix="readpass-g4-2026-2-") as folder:
        dest = Path(folder)
        for script in ROOT.glob("gen_g4_2026-2*.py"):
            if "_sat" not in script.name:
                shutil.copy2(script, dest / script.name)
        proc = subprocess.run([sys.executable, str(dest / "gen_g4_2026-2.py")], capture_output=True, text=True, encoding="utf-8")
        check(proc.returncode == 0, "isolated generator execution")
        if proc.returncode == 0:
            fresh = json.loads((dest / "data/grade4/2026-2/data.json").read_text(encoding="utf-8"))
            check(strip_audio(d) == fresh, "generator/JSON synchronization")
    for error in errors:
        print("ERROR:", error)
    audio_count = sum(1 for r in linked if r)
    print(f"Grade 4 2026-2: {len(qs)} questions / 5 word orders / {sum(len(p['sentencePairs']) for p in passages)} bilingual rows / "
          f"{len(v)} vocab / {len(fps)} focus points / audio {audio_count}/{AUDIO_COUNT}; {len(errors)} errors")
    if errors:
        raise SystemExit(1)
    print("AUDIT OK: grade4/2026-2; original PDFs, official answers, reproducible data, teaching fields"
          + (", audio" if audio_count else " (audio pending: run data/grade4/2026-2/_gen_tts.py)"))


if __name__ == "__main__":
    main()

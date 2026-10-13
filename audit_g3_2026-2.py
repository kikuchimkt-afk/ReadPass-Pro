"""Regression audit of Grade 3, 2026-2 (main venue, October 4).

The booklet has a text layer, so every English field (Part 1-2 text, choices,
question stems, passage sentences, e-mail headers, writing prompts) is compared
with the original PDF directly, and the official answer sheet is parsed
independently. After that check the source payload is frozen by SOURCE_PAYLOAD_HASH.
Use --skip-sources only on hosts without the local original PDFs, and
--require-audio once data/grade3/2026-2/_gen_tts.py has been run.
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
BASE = ROOT / "data/grade3/2026-2"
SOURCE = Path(r"D:\Files\英検過去問\3級\3級2026-2")
BOOKLET = "2026年度第2回_3級_問題冊子.pdf"
ANSWERS = "2026年度第2回_3級_解答.pdf"
HASHES = {
    BOOKLET: "6a26d0b6648ae58013fa5c71ddcb84638333556f89fbd7aff2ce6d06869f6b4c",
    ANSWERS: "3f5c32cc7a74ce270d44c9837be0885cc3b79c4f963caeb7890728a275ba47fe",
}
READING = [1, 3, 3, 2, 2, 3, 4, 4, 1, 2, 2, 3, 2, 1, 3,
           2, 3, 4, 1, 2,
           4, 1, 3, 1, 2, 4, 2, 1, 2, 3]
LISTENING = [2, 1, 3, 3, 1, 3, 2, 1, 3, 2,
             1, 2, 4, 4, 3, 1, 3, 1, 1, 2,
             2, 1, 2, 2, 1, 3, 2, 2, 3, 3]
# Frozen after the text-layer comparison: original text, choices, stems, passages, writing.
SOURCE_PAYLOAD_HASH = "2224eb619c4a61a1e436cd84840a807f399c30987973d7b80723ddbf9c792171"
AUDIO_KEYS = ("wordAudio", "audio", "sourceQuoteAudio", "audioFile")
AUDIO_COUNT = 50
PRACTICE_PAGES = 10
DATES = ["June 15", "June 15", "June 15"]
FRAGMENTS = {"Notice about Social Studies Homework", "Write soon,", "Keep in touch,", "See you tomorrow,", "Alex", "Grandpa"}
COLORS = ["#4f8cff", "#34d399", "#a78bfa", "#f472b6"]


def compact(s):
    return re.sub(r"\s+", "", s)


def pdf_norm(text):
    text = unicodedata.normalize("NFKC", text)  # ligatures and full-width spaces/brackets
    text = text.replace("\u00ad", "-").replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    text = re.sub(r"\(\s*\d*\s*\)", "()", text)
    return re.sub(r"\s+", "", text)


def digest(d):
    def q(x):
        return {k: x[k] for k in ("number", "text", "question", "choices", "answer") if k in x}
    sections = []
    for s in d["sections"]:
        item = {k: s[k] for k in ("name", "nameEn", "type", "instruction")}
        if "questions" in s:
            item["questions"] = [q(x) for x in s["questions"]]
        if "passages" in s:
            item["passages"] = [dict({k: p[k] for k in ("label", "title", "format", "instruction", "paragraphs", "emails") if k in p},
                                     questions=[q(x) for x in p["questions"]]) for p in s["passages"]]
        sections.append(item)
    return hashlib.sha256(json.dumps(dict(sections=sections, writing=d["writing"]), ensure_ascii=False,
                                     separators=(",", ":")).encode()).hexdigest()


def strip_audio(value):
    if isinstance(value, dict):
        return {k: strip_audio(v) for k, v in value.items() if k not in AUDIO_KEYS}
    if isinstance(value, list):
        return [strip_audio(v) for v in value]
    return value


def tts_module():
    spec = importlib.util.spec_from_file_location("g3_2026_2_tts", BASE / "_gen_tts.py")
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
    ps = sections[2]["passages"]
    qs = [q for s in sections[:2] for q in s["questions"]] + [q for p in ps for q in p["questions"]]
    writing = d["writing"]

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
        for w in writing.values():
            check(compact(w["sampleAnswer"]) in compact(answer), "official writing sample")
        booklet = fitz.open(SOURCE / BOOKLET)
        corpus = pdf_norm("\n".join(booklet[i].get_text() for i in range(1, 11)))
        fields = [line for q in qs[:20] for line in q["text"].split("\n")]
        fields += [c for q in qs for c in q["choices"]] + [q["question"] for q in qs if q.get("question")]
        fields += [r[0] for p in ps for r in p["sentencePairs"]] + [ps[0]["title"], ps[2]["title"]]
        fields += [v for e in ps[1]["emails"] for v in e["meta"].values()]
        fields += writing["section4"]["prompt"]["body"].split("\n") + [writing["section5"]["question"]]
        missing = [f for f in fields if pdf_norm(f) not in corpus]
        check(not missing, f"{len(missing)} English fields differ from the booklet text layer: {missing[:3]}")

    check(digest(d) == SOURCE_PAYLOAD_HASH, "frozen text-layer-verified source content")
    check((d["grade"], d["year"], d["exam"], d["session"]) == ("grade3", "2026", "2026-2", "2026-2"), "exam identity")
    check(d["title"] == "英検3級 2026年度 第2回", "exam title")
    check([s["type"] for s in sections] == ["vocabulary", "vocabulary", "reading-comprehension"], "Grade 3 section types; no word-order")
    check([len(sections[0]["questions"]), len(sections[1]["questions"]), sum(len(p["questions"]) for p in ps)] == [15, 5, 10], "15/5/10 questions")
    check([len(p["questions"]) for p in ps] == [2, 3, 5], "2/3/5 reading questions")
    check([q["number"] for q in qs] == list(range(1, 31)), "Q1-Q30 sequence")
    check([q["answer"] for q in qs] == READING, "all 30 official answers")
    for q in qs:
        tag = f"Q{q['number']}"
        for f in ("choices", "choiceTranslations", "choiceAnalysis", "choiceAnalysisSimple"):
            check(len(q[f]) == 4 and all(q[f]), tag + " four " + f)
        for f in ("choiceAnalysis", "choiceAnalysisSimple"):
            check([i for i, a in enumerate(q[f], 1) if a.startswith("○")] == [q["answer"]], tag + " correct marker " + f)
            check(all(len(a) >= 12 for a in q[f]), tag + " substantive " + f)
            check(not any("。。" in a for a in q[f]), tag + " doubled period " + f)
        check(len(q["grammar"]) >= 35 and len(q["grammarSimple"]) >= 35, tag + " normal/easy depth")
        check("questionAudio" not in q, tag + " established Grade 3 audio scope")
        if q["number"] <= 20:
            check("(　)" in q["text"] and "(　)" in q["translation"], tag + " bilingual blank")
            check(q["text"].count("\n") == q["translation"].count("\n"), tag + " speaker lines")
        else:
            p = next(p for p in ps if q in p["questions"])
            check(bool(q["questionTranslation"]), tag + " question translation")
            rows = {r[0] for r in p["sentencePairs"]}
            check(bool(q["sourceEvidence"]) and all(e in rows and e in " ".join(p["paragraphs"]) for e in q["sourceEvidence"]),
                  tag + " literal whole-sentence source evidence")
    check(all(c.endswith(",") for c in qs[17]["choices"]), "Q18 original comma before but")
    check("the most difficult part" in " ".join(qs[20]["sourceEvidence"]), "Q21 most difficult = hardest")
    check("absent in the morning" in " ".join(qs[21]["sourceEvidence"]), "Q22 morning absence")
    check("give me many fruits" in " ".join(qs[23]["sourceEvidence"]), "Q24 me = Grandpa")
    check("tomorrow morning" in " ".join(qs[24]["sourceEvidence"]), "Q25 morning versus afternoon")
    check([len(p["sentencePairs"]) for p in ps] == [10, 47, 20], "77 explicit bilingual rows, including title/headers")
    for p in ps:
        rows = p["sentencePairs"]
        bodyrows = rows[1:] if p["label"] == "A" else rows
        check(len(p["paragraphs"]) == len(p["translations"]), p["label"] + " paragraph translation parity")
        check(compact(" ".join(p["paragraphs"])) == compact(" ".join(r[0] for r in bodyrows)), p["label"] + " ordered English coverage")
        check(compact(" ".join(p["translations"])) == compact(" ".join(r[1] for r in bodyrows)), p["label"] + " ordered Japanese coverage")
        for i, r in enumerate(rows):
            tag = f"{p['label']} row {i}"
            chunks = [s.split("|") for s in r[2].split("||")]
            check(len(r) == 4 and all(r[:3]) and all(len(c) == 2 and all(c) for c in chunks), tag + " bilingual slash units")
            check(compact(" ".join(c[0] for c in chunks)) == compact(r[0]), tag + " slash reconstruction")
            if r[3]:
                check(len(chunks) >= 2 and bool(re.search(r"\b" + re.escape(r[3]) + r"\b", r[0])), tag + " finite verb")
            else:
                check(r[0].startswith(("From:", "To:", "Date:", "Subject:", "Dear ")) or r[0] in FRAGMENTS, tag + " justified no finite verb")
    check([len(p["paragraphs"]) for p in ps] == [5, 6, 4], "notice 5 / e-mail 6 / article 4 paragraphs")
    check(ps[0]["paragraphs"][3].count("\n") == 1, "notice interview questions on two lines")
    check(ps[1]["format"] == "multi-email" and len(ps[1]["emails"]) == 3, "three native email cards")
    for i, email in enumerate(ps[1]["emails"]):
        check(email["body"] == ps[1]["paragraphs"][2 * i + 1] and email["translation"] == ps[1]["translations"][2 * i + 1], "email bilingual body parity")
        check(set(email["meta"]) == {"from", "to", "date", "subject"} and email["meta"]["date"] == DATES[i], "four original email headers and dates")
        check(len(email["body"].splitlines()) == 4, "separate greeting/body/sign-off/name")
    check(set(writing) == {"section4", "section5"} and writing["section4"]["prompt"]["from"] == "James", "writing prompts")

    corpus = " ".join(q["text"].replace("(　)", q["choices"][q["answer"] - 1]) for q in qs[:20]) + " " + \
        " ".join(p["title"] + " " + " ".join(p["paragraphs"]) for p in ps)
    v = d["vocabulary"]
    check(len(v) == len({x["word"] for x in v}) == 30, "30 distinct vocabulary")
    for x in v:
        check(x["sourceForm"].lower() in corpus.lower(), "source vocabulary " + x["word"])
        check(x["level"] == "3級" and len(set(x["distractors"])) == 3 and x["meaning"] not in x["distractors"], "three distinct vocabulary distractors " + x["word"])
        check(bool(x["example"] and x["exampleJa"]) and "exampleAudio" not in x, "established bilingual vocab format " + x["word"])

    tts = tts_module()
    work = tts.jobs(d)
    jobmap = dict(work)
    fps = d["lessonPlan"]["focusPoints"]
    check([f["id"] for f in fps] == ["fp1", "fp2", "fp3", "fp4"], "four established Grade 3 focus points")
    check([f["highlightColor"] for f in fps] == COLORS, "standard Grade 3 colors")
    source_units = [q["text"].replace("(　)", q["choices"][q["answer"] - 1]) for q in qs[:20]] + [r[0] for p in ps for r in p["sentencePairs"]]
    spans = []
    for f in fps:
        check(all(f.get(k) for k in ("title", "subtitle", "explanation", "explanationSimple", "sourceQuote", "sourceLocation", "highlightColor", "highlightLabel")),
              f["id"] + " normal/easy lessons")
        check(len(f["examples"]) == 3 and all(all(e.get(k) for k in ("en", "ja", "note", "noteSimple")) for e in f["examples"]), f["id"] + " three bilingual examples")
        check(len(f["practiceQuestions"]) == len(f["practiceQuestionsSimple"]) == 3, f["id"] + " normal/easy challenges")
        check(all(pattern.lower() in corpus.lower() for pattern in f["highlightPatterns"]), f["id"] + " literal highlight patterns")
        for pattern in f["highlightPatterns"]:
            spans += [(m.start(), m.end(), f["id"], pattern) for m in re.finditer(re.escape(pattern), corpus)]
        check(all(compact(part) in compact(corpus) for part in f["sourceQuote"].split(" / ")), f["id"] + " literal source quote")
        for example in f["examples"]:
            check(compact(example["en"]) in compact(corpus), f["id"] + " source example, not metadata")
        practice = re.sub(r"\[出典:.*?\]\n?", "", f["practicePassage"]["en"])
        remaining = compact(practice)
        for unit in sorted(source_units, key=len, reverse=True):
            remaining = remaining.replace(compact(unit), "")
        check(not remaining, f["id"] + " source practice: intact original sentences, including noncontiguous excerpts")
        check(f["practicePassage"]["ja"] and "(　)" not in f["practicePassage"]["ja"], f["id"] + " practice translation")
        spoken = jobmap[f"audio/practice_pp{f['id'][2:]}.mp3"]
        check("[出典:" not in spoken and not re.search(r"(?m)^[A-Z][a-z]*(?: \d)?:", spoken), f["id"] + " spoken text excludes labels and speakers")
    for a in spans:
        for b in spans:
            if a[2] < b[2] and a[0] < b[1] and b[0] < a[1]:
                errors.append(f"highlight overlap across focus points: {a[2]} '{a[3]}' / {b[2]} '{b[3]}'")

    refs = [ref for ref, _ in work]
    check(len(refs) == len(set(refs)) == AUDIO_COUNT, f"{AUDIO_COUNT} audio jobs")
    linked = [x.get("wordAudio") for x in v] + [r for f in fps for r in [e.get("audio") for e in f["examples"]]
                                                 + [f.get("sourceQuoteAudio"), f["practicePassage"].get("audioFile")]]
    if args.require_audio or any(linked):
        check(sorted(filter(None, linked)) == sorted(refs), f"{AUDIO_COUNT} linked audio references (run _gen_tts.py)")
        actual = {p.relative_to(BASE).as_posix() for p in (BASE / "audio").rglob("*.mp3")} if (BASE / "audio").is_dir() else set()
        check(actual == set(refs), "audio files: no missing/orphans")
        for ref in refs:
            path = BASE / ref
            check(path.is_file() and path.stat().st_size >= 500, "missing/incomplete audio: " + ref)
    check([int(d["listening"][f"part{i // 10 + 1}"][str(i + 1)]) for i in range(30)] == LISTENING, "stored listening key")

    from pypdf import PdfReader
    pdf = ROOT / "output/pdf/ReadPass_EIKEN_Grade3_2026-2_Practice_Exam_Large_Type_v1.pdf"
    check(pdf.is_file(), "fixed exam PDF missing")
    if pdf.is_file():
        reader = PdfReader(pdf)
        printed = " ".join(p.extract_text() for p in reader.pages)
        check(len(reader.pages) == PRACTICE_PAGES, f"{PRACTICE_PAGES}-page practice PDF")
        for q in qs:
            text = q.get("text", q.get("question", "")).replace("(　)", "( )")
            check(compact(text) in compact(printed), f"PDF Q{q['number']} full stem")
            for c in q["choices"]:
                check(compact(c) in compact(printed), f"PDF Q{q['number']} choice {c}")
        for p in ps:
            check(all(compact(para) in compact(printed) for para in p["paragraphs"]), p["label"] + " complete PDF passage")
        printedkey = {int(n): int(a) for n, a in re.findall(r"Q(\d\d)\s+([1-4])\s", reader.pages[-1].extract_text())}
        check(printedkey == dict(enumerate(READING, 1)), "PDF official key parity")

    guides = json.loads((ROOT / "output/pdf/grammar_guides.json").read_text(encoding="utf-8"))
    check("grade3/2026-2" in guides, "grammar guide PDF not built (scripts/build_grammar_guide_pdf.py)")
    top = (ROOT / "top.js").read_text(encoding="utf-8")
    prn = (ROOT / "print.js").read_text(encoding="utf-8")
    for name, text in (("top.js", top), ("print.js", prn)):
        start = text.index("exams: [", text.index("id: 'grade3'"))
        block = text[start:text.index("]", start)]
        check(block.count("{ id: '2026-2',") == 1, f"{name}: grade3 2026-2 entry must occur exactly once")
        check(block.find("{ id: '2026-1-sat'") < block.find("{ id: '2026-2',") < block.find("{ id: '2026-2-sat'"), f"{name}: 2026-2 order")
    check(prn.count("'grade3/2026-2': {") == 1 and f"pages: {PRACTICE_PAGES}" in prn[prn.index("'grade3/2026-2': {"):][:400], "print.js fixed PDF registration")
    for page, script in (("top.html", "top.js"), ("print.html", "print.js")):
        cache = re.search(re.escape(script) + r"\?v=(\d{8})-", (ROOT / page).read_text(encoding="utf-8"))
        check(bool(cache) and cache.group(1) >= "20261013", f"{page}: {script} cache version predates 2026-2")

    # Regenerate in isolation; audio references are added later by _gen_tts.py.
    with tempfile.TemporaryDirectory(prefix="readpass-g3-2026-2-") as folder:
        dest = Path(folder)
        for script in ROOT.glob("gen_g3_2026-2*.py"):
            if "_sat" not in script.name:
                shutil.copy2(script, dest / script.name)
        proc = subprocess.run([sys.executable, str(dest / "gen_g3_2026-2.py")], capture_output=True, text=True, encoding="utf-8")
        check(proc.returncode == 0, "isolated generator execution")
        if proc.returncode == 0:
            fresh = json.loads((dest / "data/grade3/2026-2/data.json").read_text(encoding="utf-8"))
            check(strip_audio(d) == fresh, "generator/JSON synchronization")
    for error in errors:
        print("ERROR:", error)
    audio_count = sum(1 for r in linked if r)
    print(f"Grade 3 2026-2: {len(qs)} questions / {len(ps[1]['emails'])} emails / {sum(len(p['sentencePairs']) for p in ps)} bilingual rows / "
          f"{len(v)} vocab / {len(fps)} focus points / audio {audio_count}/{AUDIO_COUNT}; {len(errors)} errors")
    if errors:
        raise SystemExit(1)
    print("AUDIT OK: grade3/2026-2; original PDFs, official answers, reproducible data, teaching fields"
          + (", audio" if audio_count else " (audio pending: run data/grade3/2026-2/_gen_tts.py)"))


if __name__ == "__main__":
    main()

"""Regression audit of the source-verified Pre-2 Plus Saturday exam.

The source fingerprint is frozen after visual transcription against pp. 3-11.
OCR in this scanned booklet is unreliable, so it is NOT used to overwrite the
verified transcript. The separate official answer PDF is parsed independently.
Use --skip-sources only on hosts without the local original PDFs.
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

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "data/grade-pre2plus/2026-2-sat"
SOURCE = Path(r"D:\Files\英検過去問\土曜準会場\2026-2（土曜）")
HASHES = {
    "準2級プラス.pdf": "e145a55cfe76295cc9275b6e3efe4789949aba17ff813d0e5f71cdaf9eda1c83",
    "解答/準2級プラス_解答.pdf": "9c819a66466953b3805b762c4179db88aa999e87bff4b59602fa9feab45cf164",
}
READING = [2,4,3,3,3,4,3,2,3,1,3,3,2,4,4,1,3,4,1,4,1,2,4,2,1,4,3,2,4,2,1]
LISTENING = [3,2,1,2,3,2,1,4,2,4,2,2,4,1,1,1,4,1,3,4,1,2,1,3,3,4,1,4,2,2]
# Frozen image-verified original text, choices, question stems and instructions.
SOURCE_PAYLOAD_HASH = "6fdc660def3318640a8ac26c56aca1248316a08b23fc27b6d43e0a7045946485"


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


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    args = argparse.ArgumentParser()
    args.add_argument("--skip-sources", action="store_true")
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
    if not opts.skip_sources:
        from pypdf import PdfReader
        for path, digest in HASHES.items():
            actual = SOURCE / path
            check(actual.is_file(), f"missing original PDF: {path}")
            if actual.is_file():
                check(hashlib.sha256(actual.read_bytes()).hexdigest() == digest, f"source hash: {path}")
        answer_text = PdfReader(SOURCE / "解答/準2級プラス_解答.pdf").pages[0].extract_text()
        original_reading = {int(n): int(a) for n,a in re.findall(r"\((\d+)\)\s+([1-4])", answer_text)}
        original_listening = {int(n): int(a) for n,a in re.findall(r"No\.\s*(\d+)\s+([1-4])", answer_text)}
        check(original_reading == dict(enumerate(READING, 1)), "official reading answer PDF mismatch")
        check(original_listening == dict(enumerate(LISTENING, 1)), "official listening answer PDF mismatch")

    check((data["grade"], data["year"], data["session"]) == ("準2級プラス", "2026", "2-sat"), "exam identity")
    check(source_digest(data) == SOURCE_PAYLOAD_HASH, "immutable original content fingerprint")
    check([s["type"] for s in data["sections"]] == ["vocabulary", "passage-fill", "reading-comprehension"], "section types/order")
    passages = [p for s in data["sections"] for p in s.get("passages", [])]
    qs = data["sections"][0]["questions"] + [q for p in passages for q in p["questions"]]
    check([q["number"] for q in qs] == list(range(1,32)), "question sequence/count")
    check([q["answer"] for q in qs] == READING, "reading answers")
    check([len(p["questions"]) for p in passages] == [3,3,3,5], "passage question counts")
    lengths = []
    for q in qs:
        n = q["number"]
        for key in ("choices", "choiceTranslations", "choiceAnalysis"):
            check(len(q.get(key, [])) == 4, f"Q{n} {key} count")
        check(q.get("grammar", "").startswith("💡"), f"Q{n} grammar marker")
        for i, a in enumerate(q["choiceAnalysis"], 1):
            check(("→正解。💡" in a) == (i == q["answer"]), f"Q{n}/{i} correct marker")
            check(not a.startswith(("✅", "❌", "○")), f"Q{n}/{i} leading marker")
            lengths.append(len(a))
        if n <= 17:
            check(f"( {n} )" in q["text"] and f"( {n} )" in q["translation"], f"Q{n} bilingual blank")
        elif n <= 23:
            p = next(p for p in passages if q in p["questions"])
            check(f"( {n} )" in " ".join(p["paragraphs"]) and f"( {n} )" in " ".join(p["translations"]), f"Q{n} bilingual passage blank")
        else:
            check(bool(q.get("question") and q.get("questionTranslation")), f"Q{n} stem translation")
        if n >= 18:
            p = next(p for p in passages if q in p["questions"])
            check(bool(q.get("sourceEvidence")), f"Q{n} missing evidence")
            check(all(e in " ".join(p["paragraphs"]) for e in q["sourceEvidence"]), f"Q{n} nonliteral evidence")
    check(sum(lengths) / len(lengths) <= 65 and max(lengths) <= 120, "overlong choice analysis")

    expected = [("The Dying City",3,18), ("Honey",3,16), ("About your appointment at our clinic",4,17), ("Dogs and Heat",4,23)]
    check([(p["title"],len(p["paragraphs"]),len(p["sentencePairs"])) for p in passages] == expected, "passage shape")
    no_finite_verb = {"Dear Roy,", "Thank you for your message regarding the change to your appointment.",
                      "Thank you,", "Olivia King", "This fee ( 19 ).", "Several factors in honey ( 22 )."}
    for p in passages:
        name = p["title"]
        pairs = p["sentencePairs"]
        check(len(p["paragraphs"]) == len(p["translations"]), name + " paragraph translation count")
        check(compact(" ".join(p["paragraphs"])) == compact(" ".join(r[0] for r in pairs)), name + " full ordered English coverage")
        check(compact(" ".join(p["translations"])) == compact(" ".join(r[1] for r in pairs)), name + " full ordered Japanese coverage")
        for i,r in enumerate(pairs, 1):
            tag = f"{name}/{i}"
            check(len(r) == 4 and all(isinstance(x, str) for x in r) and all(r[:3]), tag + " four fields")
            chunks = [c.split("|") for c in r[2].split("||")]
            check(all(len(c)==2 and all(c) for c in chunks), tag + " bilingual slash format")
            check(compact(" ".join(c[0] for c in chunks)) == compact(r[0]), tag + " slash English reconstruction")
            if r[0] not in no_finite_verb:
                check(len(chunks)>=2, tag + " multiple reading units")
                check(bool(r[3]) and bool(re.search(r"(?<![A-Za-z])"+re.escape(r[3])+r"(?![A-Za-z])", r[0])), tag + " main verb token")
            else:
                check(r[3] == "", tag + " no fabricated finite verb")
    email = passages[2]
    check(email["paragraphs"][0].startswith("Dear Roy,\n"), "email greeting")
    check(email["paragraphs"][-1] == "Thank you,\nOlivia King", "email closing/signature")
    check(email["meta"] == {"from":"Olivia King <contact@drking-clinic.com>","to":"Roy Turner <roy.turner.0327@e.letters-world.com>","date":"August 12","subject":"About your appointment at our clinic"}, "email original headers")

    audio_refs = []
    vocab = data["vocabulary"]
    check(len(vocab) == 55 and len({v["word"] for v in vocab}) == 55, "55 unique balanced headwords")
    for section, selected in zip(data["sections"], [vocab[:25], vocab[25:40], vocab[40:55]]):
        original = " ".join(q["text"]+" "+" ".join(q["choices"]) for q in section.get("questions", []))
        for p in section.get("passages", []):
            original += " "+" ".join(p["paragraphs"])+" "+" ".join(c for q in p["questions"] for c in q["choices"])
        for v in selected:
            check(v["sourceForm"].lower() in original.lower(), "balanced source vocabulary: "+v["word"])
            check(v["example"] not in original, "vocabulary example must be original: "+v["word"])
    for v in vocab:
        check(all(v.get(k) for k in ("word","meaning","pos","level","example","distractors","wordAudio","exampleAudio","source","sourceForm")), "incomplete vocab: " + v["word"])
        check(v["level"] == "準2級プラス", "vocab level")
        check(len(v["distractors"]) == len(set(v["distractors"])) == 3 and v["meaning"] not in v["distractors"], "vocab distractors: " + v["word"])
        audio_refs.extend([v["wordAudio"],v["exampleAudio"]])
    fps = data["lessonPlan"]["focusPoints"]
    check([fp["id"] for fp in fps] == [f"fp{i}" for i in range(1,6)], "five focus-point ids")
    check(fps[-1]["title"] == "今回の重要なパラフレーズ", "FP5 required title")
    old_titles = {fp["title"] for file in BASE.parent.glob("*/data.json") if file.parent != BASE
                  for fp in json.loads(file.read_text(encoding="utf-8")).get("lessonPlan", {}).get("focusPoints", [])[:4]}
    check(all(fp["title"] not in old_titles for fp in fps[:4]), "new grammar topics, no duplicate titles")
    corpus = " ".join(" ".join(p["paragraphs"]) for p in passages)
    filled = corpus
    for q in qs[17:23]:
        filled = filled.replace(f"( {q['number']} )", q["choices"][q["answer"]-1])
    for fp, color in zip(fps,["#4f8cff","#f472b6","#34d399","#fbbf24","#f59e0b"]):
        tag=fp["id"]
        check(all(fp.get(k) for k in ("title","subtitle","explanation","sourceQuote","sourceLocation","examples","practicePassage","practiceQuestions","highlightPatterns","highlightColor","highlightLabel")), tag + " required fields")
        check(fp["highlightColor"] == color, tag + " standard color")
        check(len(fp["examples"])==3 and all(all(e.get(k) for k in ("en","ja","note")) for e in fp["examples"]), tag + " three bilingual examples")
        check(len(fp["practiceQuestions"])==4 and all(x.get("q") and x.get("a") for x in fp["practiceQuestions"]), tag + " four practice questions")
        check(len(fp["highlightPatterns"])>=3 and all(h in corpus for h in fp["highlightPatterns"]), tag + " literal highlight patterns")
        pp = fp["practicePassage"]
        check(pp["en"].startswith("[出典:") and bool(pp["ja"]), tag + " labeled bilingual practice")
        body=pp["en"].split("\n",1)[1]
        check(body in filled, tag + " contiguous original excerpt, blanks correctly filled")
        # Count explicit sentencePairs, preserving Dr. and p.m. abbreviations.
        chosen = [(passages[0],2),(passages[1],1),(passages[2],1),(passages[3],2),(passages[3],0)][int(tag[-1])-1]
        p, index = chosen
        paragraph = p["paragraphs"][index]
        completed = paragraph
        for q in p["questions"]:
            completed = completed.replace(f"( {q['number']} )",q["choices"][q["answer"]-1])
        check(body == completed, tag + " exactly one original paragraph")
        count = sum(row[0] in paragraph for row in p["sentencePairs"])
        check(5 <= count <= 7, tag + " five to seven explicit sentences")
        check(all(h in paragraph for h in fp["highlightPatterns"]), tag + " markers in selected paragraph")
        check(any(e["en"] in paragraph for e in fp["examples"]), tag + " source-derived example")
        audio_refs.append(pp["audioFile"])
    for ref in audio_refs:
        path=(BASE/ref).resolve()
        check(path.is_relative_to(BASE.resolve()) and path.is_file() and path.stat().st_size>=500, "missing/incomplete audio: " + ref)
        if path.is_file():
            check(path.read_bytes()[:3] == b"ID3" or path.read_bytes()[:1] == b"\xff", "invalid MP3: " + ref)
    check(len(audio_refs)==115 and len(set(audio_refs))==115, "115 unique audio references")
    listening = {"part1":dict(zip(map(str,range(1,16)),LISTENING[:15])), "part2":dict(zip(map(str,range(16,31)),LISTENING[15:]))}
    check(data["listening"] == listening, "listening answer map")

    from pypdf import PdfReader
    pdf = ROOT / "output/pdf/ReadPass_EIKEN_GradePre2Plus_2026-2-sat_Practice_Exam_Large_Type_v1.pdf"
    check(pdf.is_file(), "fixed exam PDF missing")
    if pdf.is_file():
        reader = PdfReader(pdf)
        check(len(reader.pages) == 11, "fixed PDF page count")
        printed = compact(" ".join(page.extract_text() for page in reader.pages))
        original_fields = [q.get("text", q.get("question", "")) for q in qs]
        original_fields += [c for q in qs for c in q["choices"]]
        original_fields += [row[0] for p in passages for row in p["sentencePairs"]]
        check(all(compact(field) in printed for field in original_fields), "fixed PDF must contain all 229 source fields")
        printed_answers = {int(n):int(a) for n,a in re.findall(r"Q(\d+)\s+([1-4])", reader.pages[-1].extract_text())}
        check(printed_answers == dict(enumerate(READING, 1)), "fixed PDF official answer map")

    # Regenerate in isolation; catches checked-in JSON diverging from authoring
    # scripts or audio references being added only by a post-processing step.
    with tempfile.TemporaryDirectory(prefix="readpass-pre2plus-2026-2-") as folder:
        dest=Path(folder)
        for file in ROOT.glob("gen_pre2plus_2026-2_sat*.py"):
            shutil.copyfile(file,dest/file.name)
        subprocess.run([sys.executable,str(dest/"gen_pre2plus_2026-2_sat.py")],check=True,capture_output=True)
        check((BASE/"data.json").read_bytes() == (dest/"data/grade-pre2plus/2026-2-sat/data.json").read_bytes(), "generator/JSON byte-for-byte synchronization")
    for e in errors:
        print("ERROR:",e)
    print(f"questions={len(qs)} vocabulary={len(vocab)} sentences={sum(len(p['sentencePairs']) for p in passages)} focus={len(fps)} audio={len(audio_refs)} analysis_avg={sum(lengths)/len(lengths):.1f} errors={len(errors)}")
    if errors:
        raise SystemExit(1)
    print("AUDIT OK: grade-pre2plus/2026-2-sat; original PDFs, official answers, reproducible data, teaching fields, audio")


if __name__ == "__main__":
    main()

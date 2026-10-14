"""Regression audit of Grade 4, 2025-2 Saturday sub-venue (土曜準会場, October 4).

The booklet carries an OCR text layer. Every English field (Part 1-2 text and
choices, word-order chunks and frames, notice/e-mail/story sentences, e-mail
headers, reading stems and choices) is compared with that layer word by word,
in both directions, after folding the scanner's character confusions
(l/1/I/i/|, o/0, y/v, accents). The words the layer garbles beyond that are
listed in UNREAD/NOISE; each was checked against the rendered page image, and
the lists must match exactly, so a new transcription error cannot hide behind
them. The word-order Japanese sentences are compared with the layer as well.
The official answer sheet is parsed independently (pypdf and PyMuPDF), and each
word-order answer is re-derived from the completed sentence. After that check
the source payload is frozen by SOURCE_PAYLOAD_HASH.
Use --skip-sources only on hosts without the local original PDFs, and
--require-audio once data/grade4/2025-2-sat/_gen_tts.py has been run.
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

ROOT=Path(__file__).resolve().parent
BASE=ROOT/"data/grade4/2025-2-sat"
SOURCE=Path(r"D:\Files\英検過去問\土曜準会場\2025-2（土曜）")
BOOKLET="4級.pdf"
ANSWERS="解答/4級.pdf"
HASHES={BOOKLET:"5aaa7634eae9e747a98ea101edba778f003fc6d88ccdd0c348b7827a1a66bf49",
        ANSWERS:"0f14d6396c89ab2708d3fff6b551fe1c0f631f86144b43f84b53d990cdbffef3"}
READING=[2,2,2,4,2,1,4,3,1,2,3,3,2,4,3,
         1,1,1,4,1,
         3,3,3,1,1,
         1,3,3,3,4,3,2,3,1,3]
LISTENING=[1,1,1,3,1,1,2,1,3,1,
           1,4,3,3,4,3,4,4,2,3,
           3,1,2,4,1,3,3,1,3,1]
# Frozen after the text-layer and page-image comparison.
SOURCE_PAYLOAD_HASH="0f86e5077122b43704f4f9e7430ea9cfa12bc2264bbc0db24b60d8373b3536f1"
COMPLETED=["Eri did not have time to see her aunt yesterday.",
           "I have many kinds of flowers in my garden.",
           "Thank you very much for the nice postcard.",
           "Kathy, do you need some help?",
           "I learned to cook from my mother."]
ORDER_PATTERNS=["have time to","many kinds of","Thank you very much","do you need","learned to cook"]
AUDIO_COUNT=105
PRACTICE_PAGES=11
PDF_NAME="ReadPass_EIKEN_Grade4_2025-2-sat_Practice_Exam_Large_Type_v1.pdf"
GUIDE_NAME="ReadPass_EIKEN_Grade4_2025-2-sat_Grammar_Guide_v1.pdf"
COLORS=["#4f8cff","#34d399","#a78bfa","#f472b6"]
SPEAKERS=r"(?:A|B|Mother|Son|Girl|Boy|Woman(?: [12])?|Man)"
NO_VERB=("From:","To:","Date:","Subject:","Hello ","Hi ","Your friend,","See you,","Place:","Time:")
FRAGMENTS={"Town Parade","Andy","Dave"}

# Booklet PDF page index (0-based; printed page = index + 1) of every field group.
# Words of the booklet that the text layer drops or garbles (folded form), each
# confirmed on the rendered page: e.g. p.2 "works/farm/scarf/cousin" read as
# "wolks/arm/scaIf/coIIsin"; p.4 speaker labels and "office"; p.5 "kinds/flowers/
# learned/mother" read as "hnds/Howers/leamed/mothem"; p.7, p.9 and p.11 print the
# shared first word of the four choices ("At", the numbers, "The curry") as columns.
UNREAD={(1,"works"),(1,"farm"),(1,"scarf"),(1,"cousln"),(2,"fujl"),
        (3,"mother"),(3,"glrl"),(3,"boy"),(3,"woman"),(3,"man"),(3,"offlce"),
        (4,"klnds"),(4,"flowers"),(4,"learned"),(4,"mother"),
        (6,"at"),(6,"perform"),(7,"looklng"),(7,"forward"),
        (8,"one"),(8,"two"),(8,"three"),(8,"four"),(10,"curry")}
# Text-layer words (folded, 3+ letters) with no transcribed counterpart: the
# "Grade 4" running head, the garbled readings above, circled numbers read as "O",
# answer-box rules read as "l", and quotation marks read as "G".
NOISE={(p,"grade") for p in range(1,11)}|{
    (1,"wolks"),(1,"scalf"),(1,"collsln"),(3,"bqy"),(3,"fbr"),(3,"tbd"),(3,"wbm"),
    (4,"hnds"),(4,"howers"),(4,"lhayel"),(4,"lll"),(4,"lmy"),(4,"mothem"),(4,"ohaye"),(4,"otlme"),(4,"oto"),
    (5,"lbwn"),(6,"perfbrm"),(7,"fbrward"),(7,"gyou"),(7,"loohng"),(7,"tdp"),(8,"mmm"),
    (9,"glet"),(10,"grandparentg"),(10,"llm")}
# Word-order Japanese: the layer reads お葉書 in (23) as お繕.
JA_LAYER={23:("お葉書","お繕")}
FOLD=str.maketrans({"1":"l","|":"l","!":"l","i":"l","0":"o","v":"y","$":"s"})


def compact(value): return re.sub(r"\s+","",value)


def fold(text):
    text=unicodedata.normalize("NFKD",unicodedata.normalize("NFKC",text))
    return "".join(c for c in text if not unicodedata.combining(c)).lower().translate(FOLD)


def words(text): return re.findall(r"[a-z0-9]+",fold(text))


def payload(d):
    def question(q):
        return {k:q[k] for k in ("number","text","question","choices","answer","words","correctOrder","framePrefix","frameSuffix","answerSlots") if k in q}
    result=[]
    for s in d["sections"]:
        item={k:s[k] for k in ("name","nameEn","type","instruction")}
        if "questions" in s: item["questions"]=[question(q) for q in s["questions"]]
        if "passages" in s:
            item["passages"]=[dict({k:p[k] for k in ("label","title","format","instruction","paragraphs") if k in p},questions=[question(q) for q in p["questions"]]) for p in s["passages"]]
        result.append(item)
    return result


def digest(d): return hashlib.sha256(json.dumps(payload(d),ensure_ascii=False,separators=(",",":")).encode()).hexdigest()


def english_fields(sections):
    """(booklet page index, field text) for every English field."""
    passages=sections[3]["passages"]
    fields=[]
    for q in sections[0]["questions"]+sections[1]["questions"]:
        page=1 if q["number"]<=8 else 2 if q["number"]<=15 else 3
        fields+=[(page,q["text"])]+[(page,c) for c in q["choices"]]
    for q in sections[2]["questions"]:
        fields+=[(4,w) for w in q["words"]]+[(4,q["framePrefix"]),(4,q["frameSuffix"])]
    for p,(text_page,question_page) in zip(passages,[(5,6),(7,8),(9,10)]):
        fields+=[(text_page,r[0]) for r in p["sentencePairs"]]+[(text_page,p["title"].split(" / ")[0])]
        for q in p["questions"]:
            fields+=[(question_page,q["question"])]+[(question_page,c) for c in q["choices"]]
    return fields


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    parser=argparse.ArgumentParser()
    parser.add_argument("--skip-sources",action="store_true")
    parser.add_argument("--require-audio",action="store_true")
    parser.add_argument("--show-source-hash",action="store_true")
    args=parser.parse_args()
    d=json.loads((BASE/"data.json").read_text(encoding="utf-8"))
    if args.show_source_hash: print(digest(d));return
    errors=[]
    def check(ok,msg):
        if not ok: errors.append(msg)
    from pypdf import PdfReader
    sections=d["sections"]
    passages=sections[3]["passages"]
    orders=sections[2]["questions"]
    qs=[q for s in sections for q in s.get("questions",[])]+[q for p in passages for q in p["questions"]]

    if not args.skip_sources:
        import fitz
        for name,expected in HASHES.items():
            path=SOURCE/name
            check(path.is_file() and hashlib.sha256(path.read_bytes()).hexdigest()==expected,"original PDF hash: "+name)
        for text in (PdfReader(SOURCE/ANSWERS).pages[0].extract_text(),fitz.open(SOURCE/ANSWERS)[0].get_text()):
            key={int(n):int(a) for n,a in re.findall(r"\((\d+)\)\s+([1-4])",text)}
            lkey={int(n):int(a) for n,a in re.findall(r"No\.\s*(\d+)\s+([1-4])",text)}
            check(key==dict(enumerate(READING,1)),"official reading key")
            check(lkey==dict(enumerate(LISTENING,1)),"official listening key")
        booklet=fitz.open(SOURCE/BOOKLET)
        layer={i:booklet[i].get_text() for i in range(1,11)}
        layer_words={i:set(words(t)) for i,t in layer.items()}
        layer_compact={i:"".join(words(t)) for i,t in layer.items()}
        fields=english_fields(sections)
        unread={(page,w) for page,text in fields for w in words(text)
                if w not in layer_words[page] and w not in layer_compact[page]}  # glued words count as present
        check(unread==UNREAD,f"English words differ from the booklet text layer: new {sorted(unread-UNREAD)[:6]}, stale {sorted(UNREAD-unread)[:6]}")
        mine={i:"".join(w for page,text in fields if page==i for w in words(text)) for i in layer}
        extra={(i,w) for i,t in layer.items() for w in words(t) if len(w)>=3 and w.isalpha() and w not in mine[i]}
        check(extra==NOISE,f"booklet text not transcribed: new {sorted(extra-NOISE)[:6]}, stale {sorted(NOISE-extra)[:6]}")
        for q in orders:
            ja=q["text"].replace(*JA_LAYER.get(q["number"],("","")))
            check(compact(ja) in compact(layer[4]),f"Q{q['number']} Japanese sentence vs text layer")
        check(len(fields)==235,f"{len(fields)} English fields compared")

    check(digest(d)==SOURCE_PAYLOAD_HASH,"frozen text-layer-verified source content")
    check((d["grade"],d["year"],d["exam"],d["session"])==("grade4","2025","2025-2-sat","2025-2-sat"),"exam identity")
    check(d["title"]=="英検4級 2025年度 第2回（土曜準会場）","exam title")
    check([s["type"] for s in sections]==["vocabulary","vocabulary","sentence-order","reading-comprehension"],"section types")
    check([len(s.get("questions",[])) or sum(len(p["questions"]) for p in s["passages"]) for s in sections]==[15,5,5,10],"section counts")
    check([q["number"] for q in qs]==list(range(1,36)),"Q1-Q35 sequence")
    check([q["answer"] for q in qs]==READING,"35 official answers")
    check([len(p["questions"]) for p in passages]==[2,3,5],"reading counts")
    for q in qs:
        n=q["number"]
        for field in ("choices","choiceAnalysis","choiceAnalysisSimple"):
            check(len(q[field])==4 and all(q[field]),f"Q{n} {field} count")
        for field in ("choiceAnalysis","choiceAnalysisSimple"):
            check([i for i,a in enumerate(q[field],1) if a.startswith("○")]==[q["answer"]],f"Q{n} {field} correct marker")
            check(all(len(a)>=12 for a in q[field]),f"Q{n} {field} substantive")
            check(not any("。。" in a for a in q[field]),f"Q{n} {field} doubled period")
        check(len(q["grammar"])>=25 and len(q["grammarSimple"])>=25,f"Q{n} explanation depth")
        check(bool(q.get("questionAudio"))==(n<=25),f"Q{n} question audio scope")
        if n<=20:
            check("(　)" in q["text"] and "(　)" in q["translation"],f"Q{n} retained bilingual blank")
            check(q["text"].count("\n")==q["translation"].count("\n"),f"Q{n} speaker lines")
        if n<=20 or n>=26:
            check(len(q["choiceTranslations"])==4 and all(q["choiceTranslations"]),f"Q{n} choice translations")
        if n>=26:
            p=next(p for p in passages if q in p["questions"])
            check(bool(q["questionTranslation"]),f"Q{n} stem translation")
            check(bool(q["sourceEvidence"]) and all(e in " ".join(p["paragraphs"]) for e in q["sourceEvidence"]),f"Q{n} literal reading evidence")

    spec=importlib.util.spec_from_file_location("order",ROOT/"gen_g4_2025-2_sat_order.py")
    o=importlib.util.module_from_spec(spec);spec.loader.exec_module(o)
    # Audio text verification without an edge-tts dependency.
    audio_source=(BASE/"_gen_tts.py").read_text(encoding="utf-8").replace("import edge_tts\n","")
    audio_namespace={"__file__":str(BASE/"_gen_tts.py"),"__name__":"audit_audio"}
    exec(compile(audio_source,str(BASE/"_gen_tts.py"),"exec"),audio_namespace)
    work=audio_namespace["jobs"](d)
    jobmap=dict(work)
    for q,expected,pattern in zip(orders,COMPLETED,ORDER_PATTERNS):
        n=q["number"]
        check(len(q["words"])==5 and sorted(q["correctOrder"])==[1,2,3,4,5],f"Q{n} five intact chunks")
        check(q["answerSlots"]==[2,4],f"Q{n} answer positions")
        pair="−".join("①②③④⑤"[q["correctOrder"][slot-1]-1] for slot in q["answerSlots"])
        check(pair==q["choices"][q["answer"]-1],f"Q{n} derived 2nd/4th answer vs official key")
        check(o.completed(q)==expected and jobmap[q["questionAudio"]]==expected,f"Q{n} full completed sentence/audio")
        check(expected in q["grammar"] and pattern.lower() in q["grammar"].lower(),f"Q{n} construction explanation")
        check("2番目" in q["grammar"] and "4番目" in q["grammar"],f"Q{n} explained positions")
        check("translation" not in q and "choiceTranslations" not in q,f"Q{n} no misleading translation field")
        for c,a,e in zip(q["choices"],q["choiceAnalysis"],q["choiceAnalysisSimple"]):
            chunks=[q["words"]["①②③④⑤".index(token)] for token in c if token in "①②③④⑤"]
            check(all(w in a and w in e for w in chunks),f"Q{n} each actual candidate placement")
    check("2番目と4番目" in sections[2]["instruction"] and "小文字" in sections[2]["instruction"],"original word-order instruction")

    check([len(p["sentencePairs"]) for p in passages]==[7,26,14],"47 explicit bilingual rows, including title/headers")
    check([len(p["paragraphs"]) for p in passages]==[4,4,3],"notice 4 / e-mail 4 / story 3 paragraphs")
    check(passages[0]["paragraphs"][0]==passages[0]["title"]=="Town Parade","notice title paragraph")
    check(passages[0]["paragraphs"][2]=="Place: Main Street\nTime: 1:00 p.m. to 4:00 p.m.","notice place/time lines")
    for p in passages:
        pairs=p["sentencePairs"]
        check(len(p["paragraphs"])==len(p["translations"]),p["label"]+" translations")
        check(compact(" ".join(p["paragraphs"]))==compact(" ".join(r[0] for r in pairs)),p["label"]+" ordered English coverage")
        check(compact(" ".join(p["translations"]))==compact(" ".join(r[1] for r in pairs)),p["label"]+" ordered Japanese coverage")
        for i,r in enumerate(pairs,1):
            tag=f"{p['label']} sentence {i}"
            chunks=[s.split("|") for s in r[2].split("||")]
            check(len(r)==4 and all(r[:3]) and all(len(c)==2 and all(c) for c in chunks),tag+" bilingual slash units")
            check(compact(" ".join(c[0] for c in chunks))==compact(r[0]),tag+" slash reconstruction")
            if r[3]: check(len(chunks)>=2 and bool(re.search(r"\b"+re.escape(r[3])+r"\b",r[0])),tag+" finite verb")
            else: check(r[0].startswith(NO_VERB) or r[0] in FRAGMENTS,tag+" justified no finite verb")
    emails=passages[1]["emails"]
    check(passages[0]["format"]=="notice" and passages[1]["format"]=="multi-email" and len(emails)==2,"native notice and two e-mail cards")
    for i,(email,date) in enumerate(zip(emails,["July 10","July 11"])):
        check(email["body"]==passages[1]["paragraphs"][2*i+1],"email body parity")
        check(email["translation"]==passages[1]["translations"][2*i+1],"email translation parity")
        check(set(email["meta"])=={"from","to","date","subject"} and email["meta"]["date"]==date,"four original email headers")
        check(len(email["body"].splitlines())==4,"separate greeting/body/sign-off/name")

    corpus=" ".join(q["text"].replace("(　)",q["choices"][q["answer"]-1]) for q in qs if q["number"]<=20)+" "+" ".join(COMPLETED)+" "+" ".join(x for p in passages for x in [p["title"],*p["paragraphs"]])
    v=d["vocabulary"]
    check(len(v)==30 and len({x["word"] for x in v})==30,"30 distinct vocabulary items")
    for x in v:
        check(x["sourceForm"].lower() in corpus.lower(),"source vocabulary "+x["word"])
        check(x["level"]=="4級" and len(set(x["distractors"]))==3 and x["meaning"] not in x["distractors"],"vocabulary choices "+x["word"])
        check(bool(x["example"] and x["exampleJa"]),"vocabulary bilingual example "+x["word"])
        check(compact(x["example"]) not in compact(corpus),"vocabulary example is original "+x["word"])
    fp=d["lessonPlan"]["focusPoints"]
    check([f["id"] for f in fp]==["fp1","fp2","fp3","fp4"],"four focus points")
    check([f["highlightColor"] for f in fp]==COLORS,"standard Grade 4 colors")
    units=[q["text"].replace("(　)",q["choices"][q["answer"]-1]) for q in qs if q["number"]<=20]+COMPLETED+[r[0] for p in passages for r in p["sentencePairs"]]
    spans=[]
    for f in fp:
        check(all(f.get(k) for k in ("title","subtitle","explanation","explanationSimple","sourceQuote","sourceLocation","highlightColor","highlightLabel")),f["id"]+" normal/easy lessons")
        check(len(f["examples"])==3 and all(all(e.get(k) for k in ("en","ja","note","noteSimple","audio")) for e in f["examples"]),f["id"]+" three bilingual examples")
        check(len(f["practiceQuestions"])==len(f["practiceQuestionsSimple"])==3,f["id"]+" three normal/easy challenges")
        check(len(f["highlightPatterns"])>=3 and all(pattern.lower() in corpus.lower() for pattern in f["highlightPatterns"]),f["id"]+" literal highlights")
        for pattern in f["highlightPatterns"]:
            spans+=[(m.start(),m.end(),f["id"],pattern) for m in re.finditer(re.escape(pattern),corpus)]
        check(all(compact(part) in compact(corpus) for part in f["sourceQuote"].split(" / ")),f["id"]+" literal source quote")
        check(all(compact(e["en"]) in compact(corpus) for e in f["examples"]),f["id"]+" source examples")
        remaining=compact(re.sub(r"\[出典:.*?\]\n?","",f["practicePassage"]["en"]))
        for unit in sorted(units,key=len,reverse=True): remaining=remaining.replace(compact(unit),"")
        check(not remaining,f["id"]+" practice made of intact original sentences")
        check(bool(f["practicePassage"]["ja"]),f["id"]+" practice translation")
        spoken=jobmap[f["practicePassage"]["audioFile"]]
        check("[出典:" not in spoken and not re.search(r"(?m)^"+SPEAKERS+":",spoken),f["id"]+" audio excludes labels and speakers")
    for a in spans:
        for b in spans:
            if a[2]<b[2] and a[0]<b[1] and b[0]<a[1]: errors.append(f"highlight overlap across focus points: {a[2]} '{a[3]}' / {b[2]} '{b[3]}'")

    refs=[p for p,t in work]
    check(len(refs)==len(set(refs))==AUDIO_COUNT,f"{AUDIO_COUNT} audio jobs")
    check(all("questionAudio" not in q for p in passages for q in p["questions"]),"no reading-question audio")
    actual={p.relative_to(BASE).as_posix() for p in (BASE/"audio").rglob("*.mp3")} if (BASE/"audio").is_dir() else set()
    if args.require_audio or actual:
        check(actual==set(refs),f"audio files: {len(set(refs)-actual)} missing, {len(actual-set(refs))} orphans (run _gen_tts.py)")
        for ref in refs:
            path=BASE/ref
            # A single word is about 11 KB at this voice/rate; a truncated stream once saved 2 KB.
            check(path.is_file() and path.stat().st_size>=6000,"missing/truncated audio: "+ref)
    l=[int(d["listening"][f"part{i//10+1}"][str(i+1)]) for i in range(30)]
    check(l==LISTENING,"stored listening key")

    pdf=ROOT/"output/pdf"/PDF_NAME
    check(pdf.is_file(),"fixed exam PDF missing (scripts/build_fixed_exam_pdf.py --output output/pdf/"+PDF_NAME+")")
    if pdf.is_file():
        reader=PdfReader(pdf)
        check(len(reader.pages)==PRACTICE_PAGES,f"{PRACTICE_PAGES}-page practice PDF")
        printed=" ".join(p.extract_text() for p in reader.pages)
        for q in qs:
            if q["number"]<=20: check(compact(q["text"].replace("(　)","( )")) in compact(printed),f"PDF Q{q['number']} full stem")
            elif q["number"]>=26: check(compact(q["question"]) in compact(printed),f"PDF Q{q['number']} stem")
            for c in q["choices"]: check(compact(c.replace("−","-")) in compact(printed),f"PDF Q{q['number']} choice {c}")
        ordertext=reader.pages[4].extract_text()
        check(len(re.findall(r"(?m)^2番目$",ordertext))==5 and len(re.findall(r"(?m)^4番目$",ordertext))==5,"PDF highlighted 2nd/4th slot labels")
        for q in orders:
            check(all(compact(w) in compact(ordertext) for w in q["words"]),f"PDF Q{q['number']} intact chunks")
            check(compact(q["framePrefix"]) in compact(ordertext) and compact(q["frameSuffix"]) in compact(ordertext),f"PDF Q{q['number']} original frame")
        for p in passages:
            check(all(compact(para) in compact(printed) for para in p["paragraphs"]),p["label"]+" complete PDF passage")
        printedkey={int(n):int(a) for n,a in re.findall(r"Q(\d\d)\s+([1-4])\s",reader.pages[-1].extract_text())}
        check(printedkey==dict(enumerate(READING,1)),"PDF official key parity")
    guide=ROOT/"output/pdf"/GUIDE_NAME
    check(guide.is_file() and len(PdfReader(guide).pages)>=4,"grammar guide PDF (scripts/build_grammar_guide_pdf.py --grade grade4 --exam 2025-2-sat)")

    notes=[]
    for name in ("top.js","print.js"):
        text=(ROOT/name).read_text(encoding="utf-8")
        start=text.index("exams: [",text.index("id: 'grade4'"))
        block=text[start:text.index("]",start)]
        check(block.count("{ id: '2025-2-sat',")==1,f"{name}: grade4 2025-2-sat entry must occur exactly once")
        check(block.find("{ id: '2025-2',")<block.find("{ id: '2025-2-sat',")<block.find("{ id: '2025-3',"),f"{name}: 2025-2-sat order")
    prn=(ROOT/"print.js").read_text(encoding="utf-8")
    if "'grade4/2025-2-sat': {" in prn:
        entry=prn[prn.index("'grade4/2025-2-sat': {"):][:400]
        check(PDF_NAME in entry and f"pages: {PRACTICE_PAGES}" in entry,"print.js FIXED_EXAM_PDFS registration")
    else:
        notes.append(f"print.js FIXED_EXAM_PDFS has no 'grade4/2025-2-sat' entry yet ({PRACTICE_PAGES} pages)")
    guides=json.loads((ROOT/"output/pdf/grammar_guides.json").read_text(encoding="utf-8"))
    if "grade4/2025-2-sat" not in guides: notes.append("output/pdf/grammar_guides.json has no grade4/2025-2-sat entry yet")

    with tempfile.TemporaryDirectory(prefix="grade4-2025-2-sat-") as temp:
        folder=Path(temp)
        for script in ROOT.glob("gen_g4_2025-2_sat*.py"): shutil.copy2(script,folder/script.name)
        proc=subprocess.run([sys.executable,str(folder/"gen_g4_2025-2_sat.py")],capture_output=True,text=True,encoding="utf-8")
        check(proc.returncode==0,"isolated generator execution")
        check(proc.returncode==0 and (folder/"data/grade4/2025-2-sat/data.json").read_bytes()==(BASE/"data.json").read_bytes(),"byte-identical regeneration")
    for error in errors: print("ERROR:",error)
    for note in notes: print("NOTE:",note)
    print(f"Grade 4 2025-2-sat: {len(qs)} questions / 5 word orders / {sum(len(p['sentencePairs']) for p in passages)} bilingual rows / "
          f"{len(v)} vocab / {len(fp)} focus points / audio {len(actual)}/{AUDIO_COUNT} / {PRACTICE_PAGES} PDF pages; {len(errors)} errors")
    if errors: raise SystemExit(1)


if __name__=="__main__": main()

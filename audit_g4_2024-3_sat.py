"""Regression audit of Grade 4, 2024-3 Saturday sub-venue (土曜準会場, January 25).

Unlike the 2025-2 booklet, this scan has no text layer at all, so every English
field (Part 1-2 text and choices, word-order chunks and frames, notice/e-mail/story
sentences, e-mail headers, reading stems and choices) was transcribed from 250-dpi
renders of booklet pp. 2-11. The cross-check layer is produced here by OCR:
rapidocr-onnxruntime (PP-OCRv3, angle classifier off, which otherwise flips the
lines that carry curly quotation marks) on 200-dpi renders of the same pages. It
is compared with the transcription word by word, in both directions, after folding
the scanner's character confusions (l/1/I/i/|, o/0, y/v, accents), exactly as the
2025-2 audit does with the text layer. The words OCR misses or garbles beyond that
are listed in UNREAD/NOISE and the lists must match exactly. Each English field must
also occur as one unbroken word sequence in the OCR reading order; the fields where
OCR splits a justified line out of order or drops a word are listed in OCR_SPLIT.
The word-order Japanese sentences are compared on their kanji (OCR does not read
kana reliably), with every OCR misreading listed in JA_OCR_MISREADS. Each list
entry was checked against the rendered page image.
The official answer sheet has a real text layer and is parsed independently (pypdf
and PyMuPDF), and each word-order answer is re-derived from the completed sentence.
After that check the source payload is frozen by SOURCE_PAYLOAD_HASH.
Use --skip-sources only on hosts without the local original PDFs, and
--require-audio once data/grade4/2024-3-sat/_gen_tts.py has been run.
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
BASE=ROOT/"data/grade4/2024-3-sat"
SOURCE=Path(r"D:\Files\英検過去問\土曜準会場\2024-3（土曜）")
BOOKLET="2024_3_英検4級問題.pdf"
ANSWERS="４級_解答.pdf"
HASHES={BOOKLET:"89204498845603d3732eedb4e15ab961684e70b7439ddec0f53e86025edf82d5",
        ANSWERS:"77432168e59565915011cab8e19a32f058c7dfe60ef05c803f3cb07b89dc8782"}
READING=[1,1,4,3,2,3,1,4,1,3,4,3,2,1,2,
         1,4,1,3,1,
         2,4,1,4,4,
         3,4,3,4,2,3,2,1,4,1]
LISTENING=[2,3,2,2,3,2,3,1,1,2,
           4,2,3,1,2,3,2,1,4,1,
           4,1,3,2,4,2,1,3,1,4]
# Frozen after the page-image transcription and the OCR comparison.
SOURCE_PAYLOAD_HASH="cf6eb18ae9614ff3aeebe2d83a161233e7b136e5d8033221d74ba587b0e019ef"
COMPLETED=["What time did you get home yesterday?",
           "I finished drawing a picture of my grandmother.",
           "I use this cup when I drink tea.",
           "My uncle took me to a museum today.",
           "Sally, please tell me about your spring vacation."]
ORDER_PATTERNS=["What time","finished drawing","when I drink","took me to","tell me about"]
AUDIO_COUNT=105
PRACTICE_PAGES=11
PDF_NAME="ReadPass_EIKEN_Grade4_2024-3-sat_Practice_Exam_Large_Type_v1.pdf"
GUIDE_NAME="ReadPass_EIKEN_Grade4_2024-3-sat_Grammar_Guide_v1.pdf"
COLORS=["#4f8cff","#34d399","#a78bfa","#f472b6"]
SPEAKERS=r"(?:A|B|Daughter|Mother|Boy|Girl|Teacher|Student|Father|Son)"
NO_VERB=("From:","To:","Date:","Subject:","Dear ","Hello ","Love,")
FRAGMENTS={"Jogging in the Gym","Mark","Grandma"}

# OCR settings; the lists below were made with rapidocr-onnxruntime 1.2.3 / PyMuPDF 1.27.
OCR_DPI=200
OCR_VERSION="1.2.3"
# Booklet PDF page index (0-based; printed page = index + 1) of every field group.
# Transcribed words that the OCR misses or garbles beyond FOLD (folded form): none.
UNREAD=set()
# OCR words (folded, 3+ letters) with no transcribed counterpart: the "Grade 4" running head.
NOISE={(p,"grade") for p in range(1,11)}
# English fields that do not occur as one unbroken OCR word sequence, each confirmed on
# the page image: p.2 Q2 and the p.6 notice body are justified lines that OCR cuts into
# boxes read out of order; on p.11 OCR drops the article of "1 A doctor." after the
# choice number. Their words are still covered by the word-set comparison.
OCR_SPLIT={(1,"Jenny's father works for a big computer (　). He loves computers, so he enjoys his job."),
           (5,"Students can jog in the school gym before school starts at 8:00 a.m."),
           (5,"You can run around the gym and listen to music for 20 minutes!"),
           (5,"Teachers will bring juice to drink."),
           (10,"A doctor.")}
# Word-order Japanese (p.5), compared on kanji: (question, printed kanji, OCR reading;
# "" = OCR drops it). OCR reads 時/連 as the simplified 时/连 and 飲 as the variant 飮.
JA_OCR_MISREADS=[(21,"時","时"),(21,"帰","爆"),(22,"絵","崧"),(22,"終","整"),
                 (23,"紅",""),(23,"飲","飮"),(24,"日",""),(24,"連","连"),(25,"休",""),(25,"話","")]
FOLD=str.maketrans({"1":"l","|":"l","!":"l","i":"l","0":"o","v":"y","$":"s"})


def compact(value): return re.sub(r"\s+","",value)


def fold(text):
    text=unicodedata.normalize("NFKD",unicodedata.normalize("NFKC",text))
    return "".join(c for c in text if not unicodedata.combining(c)).lower().translate(FOLD)


def words(text): return re.findall(r"[a-z0-9]+",fold(text))


def kanji(text): return "".join(c for c in text if "\u4e00"<=c<="\u9fff")


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


def ocr_layer(booklet):
    """OCR text of booklet pages 2-11 (index 1-10), one line per detected box."""
    import numpy as np
    from rapidocr_onnxruntime import RapidOCR
    engine=RapidOCR(use_angle_cls=False)
    layer={}
    for i in range(1,11):
        pix=booklet[i].get_pixmap(matrix=__import__("fitz").Matrix(OCR_DPI/72,OCR_DPI/72))
        image=np.frombuffer(pix.samples,dtype=np.uint8).reshape(pix.height,pix.width,pix.n)[:,:,::-1].copy()
        result,_=engine(image)
        layer[i]="\n".join(box[1] for box in result or [])
    return layer


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
    notes=[]
    def check(ok,msg):
        if not ok: errors.append(msg)
    from pypdf import PdfReader
    sections=d["sections"]
    passages=sections[3]["passages"]
    orders=sections[2]["questions"]
    qs=[q for s in sections for q in s.get("questions",[])]+[q for p in passages for q in p["questions"]]

    if not args.skip_sources:
        import fitz
        from importlib import metadata
        for name,expected in HASHES.items():
            path=SOURCE/name
            check(path.is_file() and hashlib.sha256(path.read_bytes()).hexdigest()==expected,"original PDF hash: "+name)
        for text in (PdfReader(SOURCE/ANSWERS).pages[0].extract_text(),fitz.open(SOURCE/ANSWERS)[0].get_text()):
            key={int(n):int(a) for n,a in re.findall(r"\((\d+)\)\s+([1-4])",text)}
            lkey={int(n):int(a) for n,a in re.findall(r"No\.\s*(\d+)\s+([1-4])",text)}
            check(key==dict(enumerate(READING,1)),"official reading key")
            check(lkey==dict(enumerate(LISTENING,1)),"official listening key")
            check("1月25日" in text and "4級" in text,"answer sheet is the January 25 Grade 4 sheet")
        booklet=fitz.open(SOURCE/BOOKLET)
        check(booklet.page_count==16 and not any(page.get_text().strip() for page in booklet),
              "booklet has no text layer (if one appears, compare with it as the 2025-2 audit does)")
        version=metadata.version("rapidocr_onnxruntime")
        if version!=OCR_VERSION: notes.append(f"OCR lists were made with rapidocr-onnxruntime {OCR_VERSION}; this host has {version}")
        layer=ocr_layer(booklet)
        layer_words={i:set(words(t)) for i,t in layer.items()}
        layer_compact={i:"".join(words(t)) for i,t in layer.items()}
        fields=english_fields(sections)
        unread={(page,w) for page,text in fields for w in words(text)
                if w not in layer_words[page] and w not in layer_compact[page]}  # glued words count as present
        check(unread==UNREAD,f"English words differ from the booklet OCR: new {sorted(unread-UNREAD)[:6]}, stale {sorted(UNREAD-unread)[:6]}")
        mine={i:"".join(w for page,text in fields if page==i for w in words(text)) for i in layer}
        extra={(i,w) for i,t in layer.items() for w in words(t) if len(w)>=3 and w.isalpha() and w not in mine[i]}
        check(extra==NOISE,f"booklet text not transcribed: new {sorted(extra-NOISE)[:6]}, stale {sorted(NOISE-extra)[:6]}")
        split={(page,text) for page,text in fields if "".join(words(text)) not in layer_compact[page]}
        check(split==OCR_SPLIT,f"English fields not found as one OCR word sequence: new {sorted(split-OCR_SPLIT)[:3]}, stale {sorted(OCR_SPLIT-split)[:3]}")
        stream=kanji(layer[4])
        for q in orders:
            n=q["number"]
            expected=q["text"]
            for m,printed,read in JA_OCR_MISREADS:
                if m==n:
                    check(printed in expected and (not read or read in stream),f"stale JA_OCR_MISREADS entry: Q{n} {printed}->{read}")
                    expected=expected.replace(printed,read,1)
            check(bool(kanji(expected)) and kanji(expected) in stream,f"Q{n} Japanese sentence kanji vs OCR")
        check(len(fields)==238,f"{len(fields)} English fields compared")

    check(digest(d)==SOURCE_PAYLOAD_HASH,"frozen image-transcribed, OCR-checked source content")
    check((d["grade"],d["year"],d["exam"],d["session"])==("grade4","2024","2024-3-sat","2024-3-sat"),"exam identity")
    check(d["title"]=="英検4級 2024年度 第3回（土曜準会場）","exam title")
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

    spec=importlib.util.spec_from_file_location("order",ROOT/"gen_g4_2024-3_sat_order.py")
    o=importlib.util.module_from_spec(spec);spec.loader.exec_module(o)
    # Audio text verification without an edge-tts dependency.
    audio_source=(BASE/"_gen_tts.py").read_text(encoding="utf-8").replace("import edge_tts\n","").replace("from edge_tts import communicate, constants\n","")
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

    check([len(p["sentencePairs"]) for p in passages]==[6,26,18],"50 explicit bilingual rows, including title/headers")
    check([len(p["paragraphs"]) for p in passages]==[4,4,3],"notice 4 / e-mail 4 / story 3 paragraphs")
    check(passages[0]["paragraphs"][0]==passages[0]["title"]=="Jogging in the Gym","notice title paragraph")
    check(passages[0]["paragraphs"][1]=="Are you interested in jogging?","notice question line")
    check(passages[0]["paragraphs"][3]=="If you want to join, please arrive at the school gym at 7:30 a.m.","notice closing request")
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
    for i,(email,date) in enumerate(zip(emails,["October 11","October 12"])):
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
    for q in qs:
        if q["number"]<=20:
            check(not re.search(r"(?m)^"+SPEAKERS+":",jobmap[q["questionAudio"]]),f"Q{q['number']} audio excludes speaker labels")

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
    check(guide.is_file() and len(PdfReader(guide).pages)>=4,"grammar guide PDF (build_grammar_guide_pdf.build('grade4', '2024-3-sat', ...))")

    for name in ("top.js","print.js"):
        text=(ROOT/name).read_text(encoding="utf-8")
        start=text.index("exams: [",text.index("id: 'grade4'"))
        block=text[start:text.index("]",start)]
        check(block.count("{ id: '2024-3-sat',")==1,f"{name}: grade4 2024-3-sat entry must occur exactly once")
        check(block.find("{ id: '2024-3',")<block.find("{ id: '2024-3-sat',")<block.find("{ id: '2025-1',"),f"{name}: 2024-3-sat order")
    prn=(ROOT/"print.js").read_text(encoding="utf-8")
    if "'grade4/2024-3-sat': {" in prn:
        entry=prn[prn.index("'grade4/2024-3-sat': {"):][:400]
        check(PDF_NAME in entry and f"pages: {PRACTICE_PAGES}" in entry,"print.js FIXED_EXAM_PDFS registration")
    else:
        notes.append(f"print.js FIXED_EXAM_PDFS has no 'grade4/2024-3-sat' entry yet ({PRACTICE_PAGES} pages)")
    guides=json.loads((ROOT/"output/pdf/grammar_guides.json").read_text(encoding="utf-8"))
    if "grade4/2024-3-sat" not in guides: notes.append("output/pdf/grammar_guides.json has no grade4/2024-3-sat entry yet")

    with tempfile.TemporaryDirectory(prefix="grade4-2024-3-sat-") as temp:
        folder=Path(temp)
        for script in ROOT.glob("gen_g4_2024-3_sat*.py"): shutil.copy2(script,folder/script.name)
        proc=subprocess.run([sys.executable,str(folder/"gen_g4_2024-3_sat.py")],capture_output=True,text=True,encoding="utf-8")
        check(proc.returncode==0,"isolated generator execution")
        check(proc.returncode==0 and (folder/"data/grade4/2024-3-sat/data.json").read_bytes()==(BASE/"data.json").read_bytes(),"byte-identical regeneration")
    for error in errors: print("ERROR:",error)
    for note in notes: print("NOTE:",note)
    print(f"Grade 4 2024-3-sat: {len(qs)} questions / 5 word orders / {sum(len(p['sentencePairs']) for p in passages)} bilingual rows / "
          f"{len(v)} vocab / {len(fp)} focus points / audio {len(actual)}/{AUDIO_COUNT} / {PRACTICE_PAGES} PDF pages; {len(errors)} errors")
    if errors: raise SystemExit(1)


if __name__=="__main__": main()

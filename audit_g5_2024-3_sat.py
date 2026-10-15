"""Grade 5 2024-3 Saturday: image-verified source, OCR cross-check, independent official key.

The booklet is a ScanSnap scan with NO text layer at all (every page is a single image).
The transcript (Part 1-2 stems and choices, word-order chunks, frames and Japanese
sentences) was verified against 200/300-dpi renders of booklet pp. 2-5 and is frozen by
SOURCE_PAYLOAD_HASH. Because there is no OCR layer to compare with, this audit OCRs the
same 300-dpi renders itself: Tesseract (eng) for every English field, and Windows.Media.Ocr
(ja) for the Part 3 Japanese sentences, the circled answer pairs and the cover. Reading
order is rebuilt from the word boxes, OCR look-alike letters are folded together, and
every OCR misreading that differs from the transcript must be listed in OCR_MISREADS /
JA_OCR_MISREADS after a visual check; any other difference fails. The official answer
sheet has a real text layer and is parsed independently; each word-order answer is
re-derived from the completed sentence. Use --skip-sources only on hosts without the
local original PDFs (or without the two OCR engines), and --require-audio once
data/grade5/2024-3-sat/_gen_tts.py has been run.
"""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata

ROOT=Path(__file__).resolve().parent
BASE=ROOT/"data/grade5/2024-3-sat"
SOURCE=Path(r"D:\Files\英検過去問\土曜準会場\2024-3（土曜）")
BOOKLET="2024_3_英検5級問題.pdf"
ANSWERS="５級_解答.pdf"
READING=[1,2,1,3,1,3,2,2,1,4,4,1,3,1,4,3,4,3,1,1,2,2,3,2,2]
LISTENING=[2,3,3,1,1,2,3,1,3,2,2,3,3,4,1,2,1,1,2,2,1,3,1,2,1]
HASHES={BOOKLET:"13947a4babeabf7d965829cc00942f58e3c23ec8a25b80cc6c07d9b2da7566ec",
        ANSWERS:"f1f60a35ffc36213e0d16cb20e64ad5b5ed3c061aca0bce841d8f9735180b21e"}
SOURCE_PAYLOAD_HASH="68f3d97a2554b1c629fa228edad5aae93dec1e8006490aafc29c46a4c65c0b0f"
COMPLETED=["Who are those boys over there?","I do my homework before dinner.",
           "Let's make spaghetti for lunch.","I know Mr. Tanner's telephone number.",
           "Whose baseball cap is this?"]
PATTERNS=["those boys","do my homework","Let's＋動詞の原形","主語 I＋動詞 know","Whose＋名詞"]
# Booklet page (0-based) of each question: Q1-7 p.2, Q8-15 p.3, Q16-20 p.4, Q21-25 p.5.
PAGE_OF={**{n:1 for n in range(1,8)},**{n:2 for n in range(8,16)},**{n:3 for n in range(16,21)},**{n:4 for n in range(21,26)}}
OCR_DPI=300
LINE_TOLERANCE=4*OCR_DPI/72
TESSERACT=Path(os.environ.get("TESSERACT_EXE",r"C:\Program Files\Tesseract-OCR\tesseract.exe"))
# Tesseract text -> what the scan shows (each checked against the rendered page). Spelled
# as the OCR wrote it; the audit fails if an entry no longer occurs (stale) and if any
# other English field disagrees with the OCR.
OCR_MISREADS=[
    # "sunny" is printed slightly below the rest of the Q7 choice row, so its box forms its own line.
    (1,"1 2 exciting 3 high 4 near sunny","1 sunny 2 exciting 3 high 4 near"),
]
# Windows OCR (ja) text, whitespace removed -> what the scan shows.
JA_OCR_MISREADS=[
    (4,"昼食にスパゲッティを作りましよう。","昼食にスパゲッティを作りましょう。"),
]
SPEAKER=re.compile(r"^(?:A|B|Teacher|Student|Boy|Girl(?: [12])?|Woman|Man):\s*")
AUDIO_COUNT=80
PRACTICE_PAGES=6
GUIDE_PAGES=3
COLORS=["#4f8cff","#34d399","#a78bfa"]
# Windows.Media.Ocr through PowerShell 5.1: one "x<TAB>y<TAB>w<TAB>h<TAB>text" row per word.
WINDOWS_OCR=r"""param([string]$Path)
$ErrorActionPreference='Stop'
[Console]::OutputEncoding=[System.Text.Encoding]::UTF8
Add-Type -AssemblyName System.Runtime.WindowsRuntime
$asTask=([System.WindowsRuntimeSystemExtensions].GetMethods()|Where-Object{$_.Name -eq 'AsTask' -and $_.GetParameters().Count -eq 1 -and $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncOperation`1'})[0]
function Await($op,$type){$t=$asTask.MakeGenericMethod($type).Invoke($null,@($op));$t.Wait(-1)|Out-Null;$t.Result}
[void][Windows.Storage.StorageFile,Windows.Storage,ContentType=WindowsRuntime]
[void][Windows.Media.Ocr.OcrEngine,Windows.Foundation,ContentType=WindowsRuntime]
[void][Windows.Graphics.Imaging.BitmapDecoder,Windows.Graphics,ContentType=WindowsRuntime]
[void][Windows.Globalization.Language,Windows.Globalization,ContentType=WindowsRuntime]
$file=Await ([Windows.Storage.StorageFile]::GetFileFromPathAsync($Path)) ([Windows.Storage.StorageFile])
$stream=Await ($file.OpenAsync([Windows.Storage.FileAccessMode]::Read)) ([Windows.Storage.Streams.IRandomAccessStream])
$decoder=Await ([Windows.Graphics.Imaging.BitmapDecoder]::CreateAsync($stream)) ([Windows.Graphics.Imaging.BitmapDecoder])
$bitmap=Await ($decoder.GetSoftwareBitmapAsync()) ([Windows.Graphics.Imaging.SoftwareBitmap])
$engine=[Windows.Media.Ocr.OcrEngine]::TryCreateFromLanguage([Windows.Globalization.Language]::new('ja'))
if($engine -eq $null){throw 'Windows OCR: Japanese recognizer not installed'}
$result=Await ($engine.RecognizeAsync($bitmap)) ([Windows.Media.Ocr.OcrResult])
foreach($line in $result.Lines){foreach($w in $line.Words){$r=$w.BoundingRect;[Console]::WriteLine(("{0:F1}`t{1:F1}`t{2:F1}`t{3:F1}`t{4}" -f $r.X,$r.Y,$r.Width,$r.Height,$w.Text))}}
"""

def compact(s): return re.sub(r"\s+","",s)
def digest(d):
    result=[]
    for s in d["sections"]:
        item={k:s[k] for k in ("name","nameEn","type","instruction")}
        item["questions"]=[{k:q[k] for k in ("number","text","choices","answer","words","correctOrder","framePrefix","frameSuffix","answerSlots") if k in q} for q in s["questions"]]
        result.append(item)
    return hashlib.sha256(json.dumps(result,ensure_ascii=False,separators=(",",":")).encode()).hexdigest()

def fold(s):
    """OCR-tolerant comparison key: letters/digits only, OCR look-alikes merged (1/l/i, y/v)."""
    s=re.sub(r"[①②③④]","",s)
    s=unicodedata.normalize("NFKC",s).lower().replace("’","'")
    s=re.sub(r"[^a-z0-9]","",s)
    return s.translate(str.maketrans({"1":"l","i":"l","y":"v"}))

def reading_lines(words):
    """Rebuild reading order from word boxes (x0, y0, x1, y1, text) in pixels."""
    lines=[]
    for w in sorted(words,key=lambda w:((w[1]+w[3])/2,w[0])):
        y=(w[1]+w[3])/2
        if lines and abs(lines[-1][0]-y)<LINE_TOLERANCE: lines[-1][1].append(w)
        else: lines.append([y,[w]])
    return [" ".join(w[4] for w in sorted(ws,key=lambda w:w[0])) for _,ws in lines]

def boxes(rows):
    words=[]
    for x,y,w,h,text in rows:
        x,y,w,h=map(float,(x,y,w,h));words.append((x,y,x+w,y+h,text))
    return words

def tesseract_lines(png):
    out=subprocess.run([str(TESSERACT),str(png),"stdout","-l","eng","tsv"],capture_output=True,text=True,encoding="utf-8",check=True).stdout
    rows=[r.split("\t") for r in out.splitlines()[1:]]
    return reading_lines(boxes([r[6:10]+[r[11]] for r in rows if len(r)==12 and r[0]=="5" and r[11].strip()]))

def windows_ocr_lines(png,script):
    out=subprocess.run(["powershell","-NoProfile","-ExecutionPolicy","Bypass","-File",str(script),"-Path",str(png)],
                       capture_output=True,text=True,encoding="utf-8",check=True).stdout
    return reading_lines(boxes([r.split("\t",4) for r in out.splitlines() if r.count("\t")>=4]))

def ocr_check(booklet,qs,check,folder):
    script=folder/"windows_ocr.ps1";script.write_text(WINDOWS_OCR,encoding="utf-8-sig")
    images={}
    for p in [0,*sorted(set(PAGE_OF.values()))]:
        images[p]=folder/f"p{p+1}.png";booklet[p].get_pixmap(dpi=OCR_DPI).save(images[p])
    cover=unicodedata.normalize("NFKC",compact("".join(windows_ocr_lines(images[0],script))))
    check(all(s in cover for s in ("2024-3","5級","土曜日準会場","2025年1月25日(土)実施")),"booklet cover identity (Windows OCR)")
    pages={}
    for p in sorted(set(PAGE_OF.values())):
        lines=tesseract_lines(images[p])
        # Circled ①-④ come out as standalone "@", "®", "©", "O" or "0" in the chunk lists.
        text=fold(" ".join(re.sub(r"(?<!\S)[O0@®©]+(?!\S)"," ",line) for line in lines))
        for page,wrong,right in OCR_MISREADS:
            if page==p:
                check(fold(wrong) in text,f"stale OCR_MISREADS entry on page {p+1}: {wrong}")
                text=text.replace(fold(wrong),fold(right))
        pages[p]=text
    ja_lines=windows_ocr_lines(images[4],script)
    ja=unicodedata.normalize("NFKC",compact("".join(ja_lines)))
    for page,wrong,right in JA_OCR_MISREADS:
        check(page==4 and wrong in ja,f"stale JA_OCR_MISREADS entry on page {page+1}: {wrong}")
        ja=ja.replace(wrong,right)
    missing=[]
    for q in qs:
        n=q["number"];text=pages[PAGE_OF[n]]
        if "words" in q:
            fields=["".join(q["words"]),q["framePrefix"],q["frameSuffix"]]
            if unicodedata.normalize("NFKC",compact(q["text"])) not in ja: missing.append(f"Q{n} Japanese sentence")
        else:
            fields=[f for line in q["text"].split("\n") for part in SPEAKER.sub("",line).split("(　)")
                    for f in re.split(r"(?<=[.?!])\s+",part)]
            fields.append("".join(f"{i} {c} " for i,c in enumerate(q["choices"],1)))
        missing+=[f"Q{n} {f!r}" for f in fields if fold(f) not in text]
    check(not missing,f"{len(missing)} fields differ from the booklet OCR (after OCR_MISREADS): {missing[:4]}")
    pairs=re.findall(r"([①②③④])\s*[－一‐−\-ー]\s*([①②③④])","\n".join(ja_lines))
    check(["−".join(p) for p in pairs]==[c for q in qs[20:] for c in q["choices"]],"word-order choice pairs vs booklet (Windows OCR)")

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module

def main():
    sys.stdout.reconfigure(encoding="utf-8")
    parser=argparse.ArgumentParser();parser.add_argument("--skip-sources",action="store_true")
    parser.add_argument("--require-audio",action="store_true");parser.add_argument("--show-source-hash",action="store_true")
    args=parser.parse_args();d=json.loads((BASE/"data.json").read_text(encoding="utf-8"))
    if args.show_source_hash: print(digest(d));return
    errors=[];pending=[]
    def check(ok,msg):
        if not ok: errors.append(msg)
    sections=d["sections"];qs=[q for s in sections for q in s["questions"]]
    from pypdf import PdfReader
    if not args.skip_sources:
        import fitz
        for file,expected in HASHES.items():
            path=SOURCE/file
            check(path.is_file(),"missing original PDF "+file)
            if path.is_file():check(hashlib.sha256(path.read_bytes()).hexdigest()==expected,"unchanged original "+file)
        text="\n".join(p.extract_text() for p in PdfReader(SOURCE/ANSWERS).pages)
        check("2024年度 第3回" in text and "1月25日（土）" in text and "5級" in text,"official answer sheet identity")
        check({int(n):int(a) for n,a in re.findall(r"\((\d+)\)\s+([1-4])",text)}==dict(enumerate(READING,1)),"independently parsed official reading key")
        check({int(n):int(a) for n,a in re.findall(r"No\.\s*(\d+)\s+([1-4])",text)}==dict(enumerate(LISTENING,1)),"independently parsed official listening key")
        booklet=fitz.open(SOURCE/BOOKLET)
        check(len(booklet)==11 and not "".join(p.get_text() for p in booklet).strip(),"booklet is the 11-page image-only scan")
        check(TESSERACT.is_file(),f"Tesseract OCR not found at {TESSERACT} (set TESSERACT_EXE)")
        if TESSERACT.is_file():
            with tempfile.TemporaryDirectory(prefix="grade5-2024-3-sat-ocr-") as temp:
                ocr_check(booklet,qs,check,Path(temp))
    check(digest(d)==SOURCE_PAYLOAD_HASH,"immutable image-verified transcript")
    check((d["grade"],d["year"],d["exam"],d["session"])==("grade5","2024","2024-3-sat","2024-3-sat"),"grade/session metadata")
    check(d["title"]==d["lessonPlan"]["title"]=="英検5級 2024年度 第3回（土曜準会場）","exam title")
    check([s["type"] for s in sections]==["vocabulary","vocabulary","sentence-order"],"original sections")
    check([len(s["questions"]) for s in sections]==[15,5,5],"section counts")
    check([q["number"] for q in qs]==list(range(1,26)),"Q1-Q25 sequence")
    check([q["answer"] for q in qs]==READING,"25 official answers")
    for q in qs:
        n=q["number"]
        for field in ("choices","choiceAnalysis","choiceAnalysisSimple"):
            check(len(q[field])==4 and all(q[field]),f"Q{n} {field} count")
        for field in ("choiceAnalysis","choiceAnalysisSimple"):
            check([i for i,a in enumerate(q[field],1) if a.startswith("○")]==[q["answer"]],f"Q{n} {field} correct marker")
            check(all(len(a)>=12 for a in q[field]),f"Q{n} {field} substantive")
            check(not any("。。" in a or "、。" in a for a in q[field]),f"Q{n} {field} doubled punctuation")
        check(len(q["grammar"])>=25 and len(q["grammarSimple"])>=25,f"Q{n} normal/easy explanation")
        check(q["questionAudio"]==f"audio/q{n}.mp3",f"Q{n} question audio")
        if n<=20:
            check("(　)" in q["text"] and "(　)" in q["translation"],f"Q{n} retained bilingual blank")
            check(q["text"].count("\n")==q["translation"].count("\n"),f"Q{n} speaker lines")
            check(len(q["choiceTranslations"])==4 and all(q["choiceTranslations"]),f"Q{n} four option meanings")
    o=load("order",ROOT/"gen_g5_2024-3_sat_order.py")
    tts=(BASE/"_gen_tts.py").read_text(encoding="utf-8").replace("import edge_tts\n","")
    namespace={"__file__":str(BASE/"_gen_tts.py"),"__name__":"audit_audio"}
    exec(compile(tts,str(BASE/"_gen_tts.py"),"exec"),namespace)
    work=namespace["jobs"](d);jobmap=dict(work)
    for q,expected,pattern in zip(sections[2]["questions"],COMPLETED,PATTERNS):
        n=q["number"]
        check(len(q["words"])==4 and sorted(q["correctOrder"])==[1,2,3,4],f"Q{n} four intact chunks")
        check(q["answerSlots"]==[1,3],f"Q{n} first/third answer positions")
        pair="−".join("①②③④"[q["correctOrder"][slot-1]-1] for slot in q["answerSlots"])
        check(pair==q["choices"][q["answer"]-1],f"Q{n} derived answer vs official key")
        check(o.completed(q)==expected and jobmap[q["questionAudio"]]==expected,f"Q{n} fixed-frame completion/audio")
        check(expected in q["grammar"] and pattern.lower() in q["grammar"].lower(),f"Q{n} construction rationale")
        check("1番目" in q["grammar"] and "3番目" in q["grammar"],f"Q{n} explained positions")
        check(q["translation"]==q["text"] and "choiceTranslations" not in q,f"Q{n} existing Grade 5 schema")
        for c,a,e in zip(q["choices"],q["choiceAnalysis"],q["choiceAnalysisSimple"]):
            words=[q["words"]["①②③④".index(t)] for t in c if t in "①②③④"]
            check(all(w in a and w in e for w in words),f"Q{n} candidate-specific placements")
    check("1番目と3番目" in sections[2]["instruction"] and "①から④" in sections[2]["instruction"] and "小文字" in sections[2]["instruction"],"original word-order instructions")
    units=[q["text"].replace("(　)",q["choices"][q["answer"]-1]) for q in qs[:20]]+COMPLETED
    corpus=" ".join(units)
    vocab=d["vocabulary"]
    check(len(vocab)==len({v["word"] for v in vocab})==20,"20 distinct vocabulary items")
    for v in vocab:
        check(v["sourceForm"].lower() in corpus.lower(),"source vocabulary "+v["word"])
        check(v["level"]=="5級" and len(set(v["distractors"]))==3 and v["meaning"] not in v["distractors"],"vocabulary options "+v["word"])
        check(bool(v["example"] and v["exampleJa"]),"bilingual example "+v["word"])
        check(compact(v["example"]) not in compact(corpus),"vocabulary example is a new sentence "+v["word"])
    fps=d["lessonPlan"]["focusPoints"]
    check([f["id"] for f in fps]==["fp1","fp2","fp3"],"three existing-format focus points")
    check([f["highlightColor"] for f in fps]==COLORS,"standard Grade 5 colors")
    spans=[]
    for f in fps:
        check(all(f.get(k) for k in ("title","subtitle","explanation","explanationSimple","sourceQuote","sourceLocation","highlightColor","highlightLabel")),f["id"]+" normal/easy lesson")
        check(len(f["examples"])==3 and all(all(e.get(k) for k in ("en","ja","note","noteSimple","audio")) for e in f["examples"]),f["id"]+" three bilingual examples")
        check(len(f["practiceQuestions"])==len(f["practiceQuestionsSimple"])==3,f["id"]+" three normal/easy challenges")
        check(len(f["highlightPatterns"])>=3 and all(p.lower() in corpus.lower() for p in f["highlightPatterns"]),f["id"]+" literal highlights")
        for p in f["highlightPatterns"]:
            spans+=[(m.start(),m.end(),f["id"],p) for m in re.finditer(re.escape(p),corpus)]
        check(all(compact(part) in compact(corpus) for part in f["sourceQuote"].split(" / ")),f["id"]+" literal source quote")
        check(all(compact(e["en"]) in compact(corpus) for e in f["examples"]),f["id"]+" original examples")
        remaining=compact(re.sub(r"\[出典:.*?\]\n?","",f["practicePassage"]["en"]))
        for unit in sorted(units,key=len,reverse=True):remaining=remaining.replace(compact(unit),"")
        check(not remaining,f["id"]+" practice made of intact original sentences")
        spoken=jobmap[f["practicePassage"]["audioFile"]]
        check("[出典:" not in spoken and not re.search(r"(?m)^[A-Z][a-z]*(?: \d)?:",spoken),f["id"]+" audio excludes source labels and speakers")
    for a in spans:
        for b in spans:
            if a[2]<b[2] and a[0]<b[1] and b[0]<a[1]:errors.append(f"highlight overlap across focus points: {a[2]} '{a[3]}' / {b[2]} '{b[3]}'")
    refs=[p for p,t in work]
    linked=[q["questionAudio"] for q in qs]+[r for v in vocab for r in (v["wordAudio"],v["exampleAudio"])]
    linked+=[r for f in fps for r in [e["audio"] for e in f["examples"]]+[f["sourceQuoteAudio"],f["practicePassage"]["audioFile"]]]
    check(len(refs)==len(set(refs))==AUDIO_COUNT and sorted(linked)==sorted(refs),f"{AUDIO_COUNT} audio references")
    actual={p.relative_to(BASE).as_posix() for p in (BASE/"audio").rglob("*.mp3")} if (BASE/"audio").is_dir() else set()
    if args.require_audio or actual:
        check(actual==set(refs),"audio files: no missing/orphans (run data/grade5/2024-3-sat/_gen_tts.py)")
        for ref in refs:
            path=BASE/ref
            # A single word is about 11 KB at this voice/rate; a truncated stream once saved 2 KB.
            check(path.is_file() and path.stat().st_size>=6000,"missing/truncated audio: "+ref)
    else:pending.append("audio not generated yet: run data/grade5/2024-3-sat/_gen_tts.py, then --require-audio")
    check([len(d["listening"][f"part{i}"]) for i in range(1,4)]==[10,5,10],"original listening partitions")
    check([a for i in range(1,4) for a in d["listening"][f"part{i}"].values()]==LISTENING,"listening key")
    pdf=ROOT/"output/pdf/ReadPass_EIKEN_Grade5_2024-3-sat_Practice_Exam_Large_Type_v1.pdf"
    check(pdf.is_file(),"fixed exam PDF missing")
    if pdf.is_file():
        reader=PdfReader(pdf)
        check(len(reader.pages)==PRACTICE_PAGES,f"{PRACTICE_PAGES}-page PDF")
        printed=" ".join(p.extract_text() for p in reader.pages)
        for q in qs:
            if q["number"]<=20:check(compact(q["text"].replace("(　)","( )")) in compact(printed),f"PDF Q{q['number']} full stem")
            for c in q["choices"]:check(compact(c.replace("−","-")) in compact(printed),f"PDF Q{q['number']} choice {c}")
        ordertext=reader.pages[4].extract_text()
        check(len(re.findall(r"(?m)^1番目$",ordertext))==5 and len(re.findall(r"(?m)^3番目$",ordertext))==5,"PDF first/third highlighted slots")
        for q in qs[20:]:
            check(all(compact(w) in compact(ordertext) for w in q["words"]),f"PDF Q{q['number']} intact chunks")
            check(all(compact(q[k]) in compact(ordertext) for k in ("text","framePrefix","frameSuffix")),f"PDF Q{q['number']} Japanese/fixed frame")
        key={int(n):int(a) for n,a in re.findall(r"Q(\d\d)\s+([1-4])\s",reader.pages[-1].extract_text())}
        check(key==dict(enumerate(READING,1)),"PDF official answer key")
    guide=ROOT/"output/pdf/ReadPass_EIKEN_Grade5_2024-3-sat_Grammar_Guide_v1.pdf"
    check(guide.is_file() and len(PdfReader(guide).pages)==GUIDE_PAGES,f"{GUIDE_PAGES}-page grammar guide PDF (scripts/build_grammar_guide_pdf.py)")
    guides=json.loads((ROOT/"output/pdf/grammar_guides.json").read_text(encoding="utf-8"))
    if "grade5/2024-3-sat" in guides:
        entry=guides["grade5/2024-3-sat"]
        check(entry["downloadName"]==guide.name and entry["pages"]==entry["focusPoints"]==GUIDE_PAGES,"grammar guide manifest entry")
        if guide.is_file():check(entry["path"].endswith("?v="+hashlib.sha256(guide.read_bytes()).hexdigest()[:10]),"grammar guide manifest version matches the PDF")
    else:pending.append("output/pdf/grammar_guides.json has no grade5/2024-3-sat entry yet")
    top=(ROOT/"top.js").read_text(encoding="utf-8");prn=(ROOT/"print.js").read_text(encoding="utf-8")
    for name,text in (("top.js",top),("print.js",prn)):
        start=text.index("exams: [",text.index("id: 'grade5'"));block=text[start:text.index("]",start)]
        check(block.count("{ id: '2024-3-sat',")==1,f"{name}: grade5 2024-3-sat entry must occur exactly once")
        check(block.find("{ id: '2024-3',")<block.find("{ id: '2024-3-sat',")<block.find("{ id: '2025-1',"),f"{name}: grade5 2024-3-sat order")
    if "'grade5/2024-3-sat': {" in prn:
        reg=prn[prn.index("'grade5/2024-3-sat': {"):][:500]
        check(f"pages: {PRACTICE_PAGES}" in reg and pdf.name in reg,"print.js fixed PDF registration")
    else:pending.append("print.js FIXED_EXAM_PDFS has no 'grade5/2024-3-sat' entry yet")
    with tempfile.TemporaryDirectory(prefix="grade5-2024-3-sat-") as temp:
        folder=Path(temp)
        for script in ROOT.glob("gen_g5_2024-3_sat*.py"):shutil.copy2(script,folder/script.name)
        proc=subprocess.run([sys.executable,str(folder/"gen_g5_2024-3_sat.py")],capture_output=True,text=True,encoding="utf-8")
        check(proc.returncode==0,"isolated generation")
        check(proc.returncode==0 and (folder/"data/grade5/2024-3-sat/data.json").read_bytes()==(BASE/"data.json").read_bytes(),"byte-identical regeneration")
    for error in errors:print("ERROR:",error)
    for note in pending:print("PENDING:",note)
    print(f"Grade 5 2024-3-sat: {len(qs)} questions / 5 four-chunk orders / {len(vocab)} vocabulary / {len(fps)} focus points / "
          f"audio {len(actual)}/{AUDIO_COUNT} / {PRACTICE_PAGES} PDF pages; {len(errors)} errors")
    if errors:raise SystemExit(1)
    print("AUDIT OK: grade5/2024-3-sat; original PDFs, OCR cross-check (Tesseract eng + Windows OCR ja), official answers, reproducible data, teaching fields"
          +(", audio" if actual else " (audio pending)"))

if __name__=="__main__":main()

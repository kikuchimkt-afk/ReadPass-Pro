"""Grade 4 regression audit, including the repaired word-order representation.

The transcript was visually verified against booklet pages 2-11. OCR is not
trusted to overwrite scanned source text. Parse the official key independently.
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

ROOT=Path(__file__).resolve().parent
BASE=ROOT/"data/grade4/2026-2-sat"
SOURCE=Path(r"D:\Files\英検過去問\土曜準会場\2026-2（土曜）")
READING=[4,1,2,1,2,2,1,4,1,4,3,3,3,1,1,2,3,2,3,2,4,3,1,1,3,4,4,4,2,3,2,3,1,4,2]
LISTENING=[3,3,1,3,3,2,3,2,3,2,4,2,3,4,2,2,3,2,3,4,2,3,4,3,1,1,2,4,1,3]
HASHES={"4級.pdf":"67602a4ab67aabfc808cf46eb4615ca3901acfc5d1c283f450a82bc205710f8d",
        "解答/4級_解答.pdf":"c36f80dba09869559c5120645837c752aee287062c5b3fc1e949ddb42f650cb8"}
SOURCE_PAYLOAD_HASH="e50e4a73680f371bbe0ea862b6ad4c5aff4236bec3b4e385c7d1bcad614490bf"
COMPLETED=["Who is the tallest in your class?",
           "Ian rode his bike to school when he was in junior high school.",
           "Stop watching TV and go to bed, Mike.",
           "The students began to sing their school song.",
           "Ryan was drinking a glass of water in the kitchen."]
ORDER_PATTERNS=["the tallest","rode his bike","Stop watching TV","began to sing","a glass of water"]


def compact(value): return re.sub(r"\s+","",value)


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


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    parser=argparse.ArgumentParser()
    parser.add_argument("--skip-sources",action="store_true")
    parser.add_argument("--show-source-hash",action="store_true")
    args=parser.parse_args()
    d=json.loads((BASE/"data.json").read_text(encoding="utf-8"))
    if args.show_source_hash: print(digest(d));return
    errors=[]
    def check(ok,msg):
        if not ok: errors.append(msg)
    from pypdf import PdfReader
    if not args.skip_sources:
        for f,expected in HASHES.items():
            check(hashlib.sha256((SOURCE/f).read_bytes()).hexdigest()==expected,f"original PDF hash: {f}")
        answer=PdfReader(SOURCE/"解答/4級_解答.pdf").pages[0].extract_text()
        key={int(n):int(a) for n,a in re.findall(r"\((\d+)\)\s+([1-4])",answer)}
        lkey={int(n):int(a) for n,a in re.findall(r"No\.\s*(\d+)\s+([1-4])",answer)}
        check(key==dict(enumerate(READING,1)),"official reading key")
        check(lkey==dict(enumerate(LISTENING,1)),"official listening key")
    check(digest(d)==SOURCE_PAYLOAD_HASH,"frozen image-verified source content")
    check((d["grade"],d["year"],d["exam"],d["session"])==("grade4","2026","2026-2-sat","2026-2-sat"),"exam identity")
    sections=d["sections"]
    passages=sections[3]["passages"]
    qs=[q for s in sections for q in s.get("questions",[])]+[q for p in passages for q in p["questions"]]
    check([s["type"] for s in sections]==["vocabulary","vocabulary","sentence-order","reading-comprehension"],"section types")
    check([len(s.get("questions",[])) or sum(len(p["questions"]) for p in s["passages"]) for s in sections]==[15,5,5,10],"section counts")
    check([q["number"] for q in qs]==list(range(1,36)),"Q1-Q35 sequence")
    check([q["answer"] for q in qs]==READING,"35 answers")
    check([len(p["questions"]) for p in passages]==[2,3,5],"reading counts")
    for q in qs:
        n=q["number"]
        for field in ("choices","choiceAnalysis","choiceAnalysisSimple"):
            check(len(q[field])==4,f"Q{n} {field} count")
        for field in ("choiceAnalysis","choiceAnalysisSimple"):
            check([i for i,a in enumerate(q[field],1) if a.startswith("○")]==[q["answer"]],f"Q{n} {field} correct marker")
            check(all(len(a)>=12 for a in q[field]),f"Q{n} {field} substantive")
        check(len(q["grammar"])>=25 and len(q["grammarSimple"])>=25,f"Q{n} explanation depth")
        check(bool(q.get("questionAudio"))==(n<=25),f"Q{n} question audio scope")
        if n<=20:
            check("(　)" in q["text"] and "(　)" in q["translation"],f"Q{n} retained bilingual blank")
        if n<=20 or n>=26:
            check(len(q["choiceTranslations"])==4,f"Q{n} choice translations")
        if n>=26:
            p=next(p for p in passages if q in p["questions"])
            check(bool(q["questionTranslation"]),f"Q{n} stem translation")
            check(bool(q["sourceEvidence"]) and all(e in " ".join(p["paragraphs"]) for e in q["sourceEvidence"]),f"Q{n} literal reading evidence")
    spec=importlib.util.spec_from_file_location("order",ROOT/"gen_g4_2026-2_sat_order.py")
    o=importlib.util.module_from_spec(spec);spec.loader.exec_module(o)
    spec=importlib.util.spec_from_file_location("tts",BASE/"_gen_tts.py")
    # Audio text verification without an EdgeTTS dependency.
    audio_source=(BASE/"_gen_tts.py").read_text(encoding="utf-8").replace("import edge_tts\n","")
    audio_namespace={"__file__":str(BASE/"_gen_tts.py"),"__name__":"audit_audio"}
    exec(compile(audio_source,str(BASE/"_gen_tts.py"),"exec"),audio_namespace)
    work=audio_namespace["jobs"](d)
    jobmap=dict(work)
    for q,expected,pattern in zip(sections[2]["questions"],COMPLETED,ORDER_PATTERNS):
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
            words=[q["words"]["①②③④⑤".index(token)] for token in c if token in "①②③④⑤"]
            check(all(w in a and w in e for w in words),f"Q{n} each actual candidate placement")
    check("2番目と4番目" in sections[2]["instruction"] and "小文字" in sections[2]["instruction"],"original word-order instruction")
    check([len(p["sentencePairs"]) for p in passages]==[7,26,15],"full passage sentence counts")
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
            else: check(r[0].startswith(("From:","To:","Date:","Subject:","Hi ","Your friend,","How about")) or r[0] in ["William","Charlotte","Weekend Sale at Market Town Sports Store","Dates: August 28 and August 29"],tag+" justified no finite verb")
    for i,email in enumerate(passages[1]["emails"]):
        check(email["body"]==passages[1]["paragraphs"][2*i+1],"email body parity")
        check(email["translation"]==passages[1]["translations"][2*i+1],"email translation parity")
        check(set(email["meta"])=={"from","to","date","subject"},"four original email headers")
    corpus=" ".join(q["text"].replace("(　)",q["choices"][q["answer"]-1]) for q in qs if q["number"]<=20)+" "+" ".join(COMPLETED)+" "+" ".join(x for p in passages for x in p["paragraphs"])
    v=d["vocabulary"]
    check(len(v)==30 and len({x["word"] for x in v})==30,"30 distinct vocabulary items")
    for x in v:
        check(x["sourceForm"].lower() in corpus.lower(),"source vocabulary "+x["word"])
        check(x["level"]=="4級" and len(x["distractors"])==3 and x["meaning"] not in x["distractors"],"vocabulary choices "+x["word"])
        check(bool(x["example"] and x["exampleJa"]),"vocabulary bilingual example "+x["word"])
    fp=d["lessonPlan"]["focusPoints"]
    check([f["id"] for f in fp]==["fp1","fp2","fp3","fp4"],"four focus points")
    for f in fp:
        check(all(f.get(k) for k in ("explanation","explanationSimple","sourceQuote","sourceLocation","highlightColor")),f["id"]+" normal/easy lessons")
        check(len(f["examples"])==3 and all(all(e.get(k) for k in ("en","ja","note","noteSimple","audio")) for e in f["examples"]),f["id"]+" three bilingual examples")
        check(len(f["practiceQuestions"])==len(f["practiceQuestionsSimple"])==3,f["id"]+" three normal/easy challenges")
        check(len(f["highlightPatterns"])>=3 and all(pattern.lower() in corpus.lower() for pattern in f["highlightPatterns"]),f["id"]+" literal highlights")
        practice=re.sub(r"\[出典:.*?\]\n?","",f["practicePassage"]["en"])
        check(all(compact(s) in compact(corpus) for s in practice.splitlines() if s.strip()),f["id"]+" sourced practice text")
        check("[出典:" not in jobmap[f["practicePassage"]["audioFile"]],f["id"]+" audio excludes labels")
    refs=[p for p,t in work]
    actual={p.relative_to(BASE).as_posix() for p in (BASE/"audio").rglob("*.mp3")}
    check(len(refs)==len(set(refs))==105 and actual==set(refs),"105 audio references: no missing or orphan files")
    check(all((BASE/p).stat().st_size>=500 for p in refs),"non-empty audio files")
    l=[int(d["listening"][f"part{i//10+1}"][str(i+1)]) for i in range(30)]
    check(l==LISTENING,"stored listening key")
    pdf=ROOT/"output/pdf/ReadPass_EIKEN_Grade4_2026-2-sat_Practice_Exam_Large_Type_v1.pdf"
    reader=PdfReader(pdf)
    check(len(reader.pages)==11,"11-page practice PDF")
    printed=" ".join(p.extract_text() for p in reader.pages)
    for q in qs:
        if q["number"]<=20: check(compact(q["text"].replace("(　)","( )")) in compact(printed),f"PDF Q{q['number']} full stem")
        elif q["number"]>=26: check(compact(q["question"]) in compact(printed),f"PDF Q{q['number']} stem")
        for c in q["choices"]: check(compact(c.replace("−","-")) in compact(printed),f"PDF Q{q['number']} choice {c}")
    ordertext=reader.pages[4].extract_text()
    check(len(re.findall(r"(?m)^2番目$",ordertext))==5 and len(re.findall(r"(?m)^4番目$",ordertext))==5,"PDF highlighted 2nd/4th slot labels")
    for q in sections[2]["questions"]:
        check(all(compact(w) in compact(ordertext) for w in q["words"]),f"PDF Q{q['number']} intact chunks")
        check(compact(q["framePrefix"]) in compact(ordertext) and compact(q["frameSuffix"]) in compact(ordertext),f"PDF Q{q['number']} original frame")
    for p in passages:
        check(all(compact(para) in compact(printed) for para in p["paragraphs"]),p["label"]+" complete PDF passage")
    printedkey={int(n):int(a) for n,a in re.findall(r"Q(\d\d)\s+([1-4])\s",reader.pages[-1].extract_text())}
    check(printedkey==dict(enumerate(READING,1)),"PDF official key parity")
    with tempfile.TemporaryDirectory(prefix="grade4-reproduction-") as temp:
        folder=Path(temp)
        for script in ROOT.glob("gen_g4_2026-2_sat*.py"): shutil.copy2(script,folder/script.name)
        proc=subprocess.run([sys.executable,str(folder/"gen_g4_2026-2_sat.py")],capture_output=True,text=True,encoding="utf-8")
        check(proc.returncode==0,"isolated generator execution")
        check((folder/"data/grade4/2026-2-sat/data.json").read_bytes()==(BASE/"data.json").read_bytes(),"byte-identical regeneration")
    for error in errors: print("ERROR:",error)
    print(f"Grade 4: 35 questions / 5 repaired-format orders / 30 vocabulary / 48 sentence pairs / 4 focus points / 105 audio / 11 PDF pages; {len(errors)} errors")
    if errors: raise SystemExit(1)


if __name__=="__main__": main()

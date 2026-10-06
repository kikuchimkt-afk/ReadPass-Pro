"""Image-verified source, independent official key, four-chunk regression audit."""
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
BASE=ROOT/"data/grade5/2026-2-sat"
SOURCE=Path(r"D:\Files\英検過去問\土曜準会場\2026-2（土曜）")
READING=[4,1,4,4,1,4,1,2,1,1,2,2,4,4,2,2,4,4,4,1,4,3,4,2,4]
LISTENING=[1,1,1,2,1,1,2,2,3,2,4,4,2,4,4,2,1,2,1,2,3,3,1,1,3]
HASHES={"5級.pdf":"4b656e835a8c2df4c3775f94b96db6e53190dc64c276f7c063d3b68972e42aa6",
        "解答/5級_解答.pdf":"b2db3ee96448f3405a59b82121fc523669933f28fda5147f9a2484a17cb7934a"}
SOURCE_PAYLOAD_HASH="15a1db52ca65c734a1a3b0c44003c53bc99daf2d48381cef445a3fea911be5a0"
COMPLETED=["Let's listen to this CD in my room.","Mr. Adams goes running before lunch.",
           "My brother has a lot of comic books.","Grandpa, it's time for tea.",
           "Does your brother have a digital camera?"]
PATTERNS=["listen to","goes running","a lot of","time for","動詞の原形"]

def compact(s): return re.sub(r"\s+","",s)
def digest(d):
    result=[]
    for s in d["sections"]:
        item={k:s[k] for k in ("name","nameEn","type","instruction")}
        item["questions"]=[{k:q[k] for k in ("number","text","choices","answer","words","correctOrder","framePrefix","frameSuffix","answerSlots") if k in q} for q in s["questions"]]
        result.append(item)
    return hashlib.sha256(json.dumps(result,ensure_ascii=False,separators=(",",":")).encode()).hexdigest()

def main():
    sys.stdout.reconfigure(encoding="utf-8")
    parser=argparse.ArgumentParser();parser.add_argument("--skip-sources",action="store_true");parser.add_argument("--show-source-hash",action="store_true")
    args=parser.parse_args();d=json.loads((BASE/"data.json").read_text(encoding="utf-8"))
    if args.show_source_hash: print(digest(d));return
    errors=[]
    def check(ok,msg):
        if not ok: errors.append(msg)
    from pypdf import PdfReader
    if not args.skip_sources:
        for file,expected in HASHES.items():check(hashlib.sha256((SOURCE/file).read_bytes()).hexdigest()==expected,"unchanged original "+file)
        text="\n".join(p.extract_text() for p in PdfReader(SOURCE/"解答/5級_解答.pdf").pages)
        check({int(n):int(a) for n,a in re.findall(r"\((\d+)\)\s+([1-4])",text)}==dict(enumerate(READING,1)),"independently parsed official reading key")
        check({int(n):int(a) for n,a in re.findall(r"No\.\s*(\d+)\s+([1-4])",text)}==dict(enumerate(LISTENING,1)),"independently parsed official listening key")
    check(digest(d)==SOURCE_PAYLOAD_HASH,"immutable image-verified transcript")
    sections=d["sections"];qs=[q for s in sections for q in s["questions"]]
    check(d["grade"]=="grade5" and d["exam"]==d["session"]=="2026-2-sat","grade/session metadata")
    check([s["type"] for s in sections]==["vocabulary","vocabulary","sentence-order"],"original sections")
    check([len(s["questions"]) for s in sections]==[15,5,5],"section counts")
    check([q["number"] for q in qs]==list(range(1,26)),"Q1-Q25 sequence")
    check([q["answer"] for q in qs]==READING,"25 official answers")
    for q in qs:
        n=q["number"]
        for field in ("choices","choiceAnalysis","choiceAnalysisSimple"):
            check(len(q[field])==4,f"Q{n} {field} count")
        for field in ("choiceAnalysis","choiceAnalysisSimple"):
            check([i for i,a in enumerate(q[field],1) if a.startswith("○")]==[q["answer"]],f"Q{n} {field} correct marker")
            check(all(len(a)>=12 for a in q[field]),f"Q{n} {field} substantive")
        check(len(q["grammar"])>=25 and len(q["grammarSimple"])>=25,f"Q{n} normal/easy explanation")
        check(q["questionAudio"]==f"audio/q{n}.mp3",f"Q{n} question audio")
        if n<=20:
            check("(　)" in q["text"] and "(　)" in q["translation"],f"Q{n} retained bilingual blank")
            check(len(q["choiceTranslations"])==4,f"Q{n} four option meanings")
    spec=importlib.util.spec_from_file_location("order",ROOT/"gen_g5_2026-2_sat_order.py")
    o=importlib.util.module_from_spec(spec);spec.loader.exec_module(o)
    audio_source=(BASE/"_gen_tts.py").read_text(encoding="utf-8").replace("import edge_tts\n","")
    namespace={"__file__":str(BASE/"_gen_tts.py"),"__name__":"audit_audio"}
    exec(compile(audio_source,str(BASE/"_gen_tts.py"),"exec"),namespace)
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
    corpus=" ".join(q["text"].replace("(　)",q["choices"][q["answer"]-1]) for q in qs[:20])+" "+" ".join(COMPLETED)
    vocab=d["vocabulary"]
    check(len(vocab)==len({v["word"] for v in vocab})==20,"20 distinct vocabulary items")
    for v in vocab:
        check(v["sourceForm"].lower() in corpus.lower(),"source vocabulary "+v["word"])
        check(v["level"]=="5級" and len(set(v["distractors"]))==3 and v["meaning"] not in v["distractors"],"vocabulary options "+v["word"])
        check(bool(v["example"] and v["exampleJa"]),"bilingual example "+v["word"])
    fps=d["lessonPlan"]["focusPoints"]
    check([f["id"] for f in fps]==["fp1","fp2","fp3"],"three existing-format focus points")
    for f in fps:
        check(all(f.get(k) for k in ("explanation","explanationSimple","sourceQuote","sourceLocation","highlightColor")),f["id"]+" normal/easy lesson")
        check(len(f["examples"])==3 and all(all(e.get(k) for k in ("en","ja","note","noteSimple","audio")) for e in f["examples"]),f["id"]+" three bilingual examples")
        check(len(f["practiceQuestions"])==len(f["practiceQuestionsSimple"])==3,f["id"]+" three normal/easy challenges")
        check(len(f["highlightPatterns"])>=3 and all(p.lower() in corpus.lower() for p in f["highlightPatterns"]),f["id"]+" literal highlights")
        practice=re.sub(r"\[出典:.*?\]\n?","",f["practicePassage"]["en"])
        check(all(compact(s) in compact(corpus) for s in practice.splitlines() if s.strip()),f["id"]+" original practice sentences")
        check(all(compact(e["en"]) in compact(corpus) for e in f["examples"]),f["id"]+" original examples")
        check("[出典:" not in jobmap[f["practicePassage"]["audioFile"]],f["id"]+" audio excludes source labels")
    refs=[p for p,t in work];actual={p.relative_to(BASE).as_posix() for p in (BASE/"audio").rglob("*.mp3")}
    check(len(refs)==len(set(refs))==80 and actual==set(refs),"80 audio references without missing/orphans")
    check(all((BASE/p).is_file() and (BASE/p).stat().st_size>=500 for p in refs),"non-empty audio")
    check([len(d["listening"][f"part{i}"]) for i in range(1,4)]==[10,5,10],"original listening partitions")
    check([a for i in range(1,4) for a in d["listening"][f"part{i}"].values()]==LISTENING,"listening key")
    reader=PdfReader(ROOT/"output/pdf/ReadPass_EIKEN_Grade5_2026-2-sat_Practice_Exam_Large_Type_v1.pdf")
    check(len(reader.pages)==6,"six-page PDF")
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
    with tempfile.TemporaryDirectory(prefix="grade5-reproduction-") as temp:
        folder=Path(temp)
        for script in ROOT.glob("gen_g5_2026-2_sat*.py"):shutil.copy2(script,folder/script.name)
        proc=subprocess.run([sys.executable,str(folder/"gen_g5_2026-2_sat.py")],capture_output=True,text=True,encoding="utf-8")
        check(proc.returncode==0,"isolated generation")
        check((folder/"data/grade5/2026-2-sat/data.json").read_bytes()==(BASE/"data.json").read_bytes(),"byte-identical regeneration")
    for error in errors:print("ERROR:",error)
    print(f"Grade 5: 25 questions / 5 repaired four-chunk orders / 20 vocabulary / 3 focus points / 80 audio / 6 PDF pages; {len(errors)} errors")
    if errors:raise SystemExit(1)

if __name__=="__main__":main()

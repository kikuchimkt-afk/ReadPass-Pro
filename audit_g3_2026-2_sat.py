"""Independent official-key audit and frozen, visually verified source payload.

Booklet pp. 2-11 and the answer sheet were inspected as rendered images;
unreliable scanned-text OCR must not replace this transcript.
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

ROOT=Path(__file__).resolve().parent
BASE=ROOT/"data/grade3/2026-2-sat"
SOURCE=Path(r"D:\Files\英検過去問\土曜準会場\2026-2（土曜）")
READING=[4,4,4,3,1,4,1,2,4,1,3,1,4,2,3,3,3,1,2,1,2,3,2,3,3,1,2,2,4,2]
LISTENING=[1,1,1,2,1,2,2,2,3,2,1,1,1,4,1,2,4,1,2,2,3,1,2,3,1,4,1,1,4,2]
HASHES={"3級.pdf":"e12dab9129ec25726534c5cdae76b57c99ca6923d417c66f805a70af28405133",
        "解答/3級_解答.pdf":"c2489ba8a65f61dcac79f6e7813746bc34532d185533669ed25aec54acb1a0f3"}
SOURCE_PAYLOAD_HASH="ef4d46935d807961e90c8fd7f991b9e1f991a16a5b88d81b5d8f698205fbddfd"

def compact(s):return re.sub(r"\s+","",s)
def digest(d):
    def q(x):return {k:x[k] for k in ("number","text","question","choices","answer") if k in x}
    sections=[]
    for s in d["sections"]:
        item={k:s[k] for k in ("name","nameEn","type","instruction")}
        if "questions" in s:item["questions"]=[q(x) for x in s["questions"]]
        if "passages" in s:item["passages"]=[dict({k:p[k] for k in ("label","title","format","instruction","paragraphs","emails") if k in p},questions=[q(x) for x in p["questions"]]) for p in s["passages"]]
        sections.append(item)
    return hashlib.sha256(json.dumps(dict(sections=sections,writing=d["writing"]),ensure_ascii=False,separators=(",",":")).encode()).hexdigest()

def main():
    sys.stdout.reconfigure(encoding="utf-8")
    parser=argparse.ArgumentParser()
    parser.add_argument("--skip-sources",action="store_true")
    parser.add_argument("--show-source-hash",action="store_true")
    args=parser.parse_args()
    d=json.loads((BASE/"data.json").read_text(encoding="utf-8"))
    if args.show_source_hash:print(digest(d));return
    errors=[]
    def check(ok,msg):
        if not ok:errors.append(msg)
    from pypdf import PdfReader
    if not args.skip_sources:
        for f,h in HASHES.items():check(hashlib.sha256((SOURCE/f).read_bytes()).hexdigest()==h,"original PDF hash: "+f)
        answer=PdfReader(SOURCE/"解答/3級_解答.pdf").pages[0].extract_text()
        key={int(n):int(a) for n,a in re.findall(r"\((\d+)\)\s+([1-4])",answer)}
        lkey={int(n):int(a) for n,a in re.findall(r"No\.\s*(\d+)\s+([1-4])",answer)}
        check(key==dict(enumerate(READING,1)),"official reading key")
        check(lkey==dict(enumerate(LISTENING,1)),"official listening key")
        for w in d["writing"].values():check(compact(w["sampleAnswer"]) in compact(answer),"official writing sample")
    check(digest(d)==SOURCE_PAYLOAD_HASH,"frozen image-verified source content")
    check((d["grade"],d["year"],d["exam"],d["session"])==("grade3","2026","2026-2-sat","2026-2-sat"),"exam identity")
    sections=d["sections"];ps=sections[2]["passages"]
    qs=[q for s in sections[:2] for q in s["questions"]]+[q for p in ps for q in p["questions"]]
    check([s["type"] for s in sections]==["vocabulary","vocabulary","reading-comprehension"],"new Grade 3 section types; no word-order")
    check([len(sections[0]["questions"]),len(sections[1]["questions"]),sum(len(p["questions"]) for p in ps)]==[15,5,10],"15/5/10 questions")
    check([len(p["questions"]) for p in ps]==[2,3,5],"2/3/5 reading questions")
    check([q["number"] for q in qs]==list(range(1,31)),"Q1-Q30 sequence")
    check([q["answer"] for q in qs]==READING,"all 30 official answers")
    for q in qs:
        tag=f"Q{q['number']}"
        for f in ("choices","choiceTranslations","choiceAnalysis","choiceAnalysisSimple"):
            check(len(q[f])==4 and all(q[f]),tag+" four "+f)
        for f in ("choiceAnalysis","choiceAnalysisSimple"):
            check([i for i,a in enumerate(q[f],1) if a.startswith("○")]==[q["answer"]],tag+" correct marker "+f)
            check(all(len(a)>=12 for a in q[f]),tag+" substantive "+f)
        check(len(q["grammar"])>=35 and len(q["grammarSimple"])>=35,tag+" normal/easy depth")
        check("questionAudio" not in q,tag+" established Grade 3 audio scope")
        if q["number"]<=20:check("(　)" in q["text"] and "(　)" in q["translation"],tag+" bilingual blank")
        else:
            p=next(p for p in ps if q in p["questions"])
            check(bool(q["questionTranslation"]),tag+" question translation")
            check(bool(q["sourceEvidence"]) and all(e in " ".join(p["paragraphs"]) for e in q["sourceEvidence"]),tag+" literal source evidence")
    check(all(c.endswith(",") for c in qs[17]["choices"]),"Q18 original comma before but")
    check("twenty years ago" in qs[23]["sourceEvidence"][1] and "当時の年齢" in qs[23]["grammar"],"Q24 age versus years ago")
    check("in the morning on Saturday" in qs[24]["sourceEvidence"][0],"Q25 morning versus afternoon")
    check("was given a medal" in qs[28]["sourceEvidence"][0] and "1955" in qs[28]["grammar"],"Q29 medal versus death")
    check([len(p["sentencePairs"]) for p in ps]==[12,44,22],"78 explicit bilingual rows, including headers/title")
    fragments={"Anton Bell Cookie Shop's Opening Sale","Special Ticket and Birthday Gift Card","Love,","Your aunt,","See you soon,","Marie","Jill"}
    for p in ps:
        rows=p["sentencePairs"];bodyrows=rows[1:] if p["label"]=="A" else rows
        check(len(p["paragraphs"])==len(p["translations"]),p["label"]+" paragraph translation parity")
        check(compact(" ".join(p["paragraphs"]))==compact(" ".join(r[0] for r in bodyrows)),p["label"]+" ordered English coverage")
        check(compact(" ".join(p["translations"]))==compact(" ".join(r[1] for r in bodyrows)),p["label"]+" ordered Japanese coverage")
        for i,r in enumerate(rows):
            tag=f"{p['label']} row {i}"
            chunks=[s.split("|") for s in r[2].split("||")]
            check(len(r)==4 and all(r[:3]) and all(len(c)==2 and all(c) for c in chunks),tag+" bilingual slash units")
            check(compact(" ".join(c[0] for c in chunks))==compact(r[0]),tag+" slash reconstruction")
            if r[3]:check(len(chunks)>=2 and bool(re.search(r"\b"+re.escape(r[3])+r"\b",r[0])),tag+" finite verb")
            else:check(r[0].startswith(("From:","To:","Date:","Time:","Subject:","Hi ")) or r[0] in fragments,tag+" justified no finite verb")
    check(ps[2]["sentencePairs"][5][3]=="met" and ps[2]["sentencePairs"][16][3]=="came" and ps[2]["sentencePairs"][20][3]=="studied","main clauses, not relative/subordinate verbs")
    check(ps[1]["format"]=="multi-email" and len(ps[1]["emails"])==3,"three native email cards")
    for i,email in enumerate(ps[1]["emails"]):
        check(email["body"]==ps[1]["paragraphs"][2*i+1] and email["translation"]==ps[1]["translations"][2*i+1],"email bilingual body parity")
        check(set(email["meta"])=={"from","to","date","subject"} and email["meta"]["date"]==["September 18","September 18","September 19"][i],"four original email headers and dates")
        check(len(email["body"].splitlines())==4,"separate greeting/body/sign-off/name")
    corpus=" ".join(q["text"].replace("(　)",q["choices"][q["answer"]-1]) for q in qs[:20])+" "+" ".join(p["title"]+" "+" ".join(p["paragraphs"]) for p in ps)
    v=d["vocabulary"]
    check(len(v)==len({x["word"] for x in v})==30,"30 distinct vocabulary")
    for x in v:
        check(x["sourceForm"].lower() in corpus.lower(),"source vocabulary "+x["word"])
        check(x["level"]=="3級" and len(set(x["distractors"]))==3 and x["meaning"] not in x["distractors"],"three distinct vocabulary distractors "+x["word"])
        check(bool(x["example"] and x["exampleJa"]) and "exampleAudio" not in x,"established bilingual vocab format "+x["word"])
    audio_source=(BASE/"_gen_tts.py").read_text(encoding="utf-8").replace("import edge_tts\n","")
    ns={"__file__":str(BASE/"_gen_tts.py"),"__name__":"audit_audio"}
    exec(compile(audio_source,str(BASE/"_gen_tts.py"),"exec"),ns)
    work=ns["jobs"](d);jobmap=dict(work)
    fps=d["lessonPlan"]["focusPoints"]
    check([f["id"] for f in fps]==["fp1","fp2","fp3","fp4"],"four established Grade 3 focus points")
    for f in fps:
        check(all(f.get(k) for k in ("explanation","explanationSimple","sourceQuote","sourceLocation","highlightColor")),f["id"]+" normal/easy lessons")
        check(len(f["examples"])==3 and all(all(e.get(k) for k in ("en","ja","note","noteSimple","audio")) for e in f["examples"]),f["id"]+" three bilingual examples")
        check(len(f["practiceQuestions"])==len(f["practiceQuestionsSimple"])==3,f["id"]+" normal/easy challenges")
        check(all(pattern.lower() in corpus.lower() for pattern in f["highlightPatterns"]),f["id"]+" literal highlight patterns")
        for example in f["examples"]:check(compact(example["en"]) in compact(corpus),f["id"]+" source example, not metadata")
        practice=re.sub(r"\[出典:.*?\]\n?","",f["practicePassage"]["en"])
        remaining=compact(practice)
        source_units=[q["text"].replace("(　)",q["choices"][q["answer"]-1]) for q in qs[:20]]+[r[0] for p in ps for r in p["sentencePairs"]]
        for unit in sorted(source_units,key=len,reverse=True):remaining=remaining.replace(compact(unit),"")
        check(not remaining,f["id"]+" source practice: intact original sentences, including noncontiguous excerpts")
        check("[出典:" not in jobmap[f["practicePassage"]["audioFile"]],f["id"]+" spoken text excludes labels")
    check(fps[2]["examples"][2]["en"]=="I first heard that song when I was ten years old. That was twenty years ago!","FP3 actual age/time sentences, not headers")
    check("in the morning on Saturday" in fps[2]["practicePassage"]["en"] and "After eating lunch at my house" in fps[2]["practicePassage"]["en"],"FP3 original morning/afternoon practice")
    refs=[p for p,t in work];actual={p.relative_to(BASE).as_posix() for p in (BASE/"audio").rglob("*.mp3")}
    check(len(refs)==len(set(refs))==50 and actual==set(refs),"50 audio refs, no missing/orphans")
    check(all((BASE/p).is_file() and (BASE/p).stat().st_size>=500 for p in refs),"all audio non-empty")
    check([int(d["listening"][f"part{i//10+1}"][str(i+1)]) for i in range(30)]==LISTENING,"stored listening key")
    pdf=ROOT/"output/pdf/ReadPass_EIKEN_Grade3_2026-2-sat_Practice_Exam_Large_Type_v1.pdf"
    reader=PdfReader(pdf);printed=" ".join(p.extract_text() for p in reader.pages)
    check(len(reader.pages)==10,"10-page practice PDF")
    for q in qs:
        text=q.get("text",q.get("question","")).replace("(　)","( )")
        check(compact(text) in compact(printed),f"PDF Q{q['number']} full stem")
        for c in q["choices"]:check(compact(c) in compact(printed),f"PDF Q{q['number']} choice {c}")
    for p in ps:check(all(compact(para) in compact(printed) for para in p["paragraphs"]),p["label"]+" complete PDF passage")
    printedkey={int(n):int(a) for n,a in re.findall(r"Q(\d\d)\s+([1-4])\s",reader.pages[-1].extract_text())}
    check(printedkey==dict(enumerate(READING,1)),"PDF official key parity")
    with tempfile.TemporaryDirectory(prefix="grade3-reproduction-") as temp:
        folder=Path(temp)
        for script in ROOT.glob("gen_g3_2026-2_sat*.py"):shutil.copy2(script,folder/script.name)
        proc=subprocess.run([sys.executable,str(folder/"gen_g3_2026-2_sat.py")],capture_output=True,text=True,encoding="utf-8")
        check(proc.returncode==0,"isolated generator execution")
        check((folder/"data/grade3/2026-2-sat/data.json").read_bytes()==(BASE/"data.json").read_bytes(),"byte-identical regeneration")
    for error in errors:print("ERROR:",error)
    print(f"Grade 3: 30 questions / 3 complete emails / 78 bilingual rows / 30 vocab / 4 focus points / 50 audio / 10 PDF pages; {len(errors)} errors")
    if errors:raise SystemExit(1)

if __name__=="__main__":main()

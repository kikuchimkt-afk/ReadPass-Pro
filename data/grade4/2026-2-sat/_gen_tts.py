"""Existing Grade 4 audio content; atomic/retryable generation, no JSON mutation."""
import asyncio
import json
from pathlib import Path
import re
import sys
import edge_tts

BASE=Path(__file__).resolve().parent
VOICE="en-US-JennyNeural"
RATE="-15%"


def completed(q):
    s=" ".join([q["framePrefix"],*[q["words"][i-1] for i in q["correctOrder"]],q["frameSuffix"]]).strip()
    s=re.sub(r"\s+([.,?!])",r"\1",s)
    return s[0].upper()+s[1:]


def jobs(data):
    result=[]
    for section in data["sections"]:
        for q in section.get("questions",[]):
            if section["type"]=="sentence-order": text=completed(q)
            else:
                # Do not read dialogue speaker labels as part of a speaker's line.
                text=re.sub(r"(?m)^(?:A|B|Daughter|Mother|Father|Man(?: [12])?|Woman|Boy|Girl):\s*","",q["text"])
                text=text.replace("(　)"," blank ").replace("\n"," ... ")
                text+=" ... "+" ... ".join(f"{i}. {c}" for i,c in enumerate(q["choices"],1))
            result.append((q["questionAudio"],text))
    for v in data["vocabulary"]:
        result.extend([(v["wordAudio"],v["word"]),(v["exampleAudio"],v["example"])])
    for fp in data["lessonPlan"]["focusPoints"]:
        result.extend((e["audio"],e["en"]) for e in fp["examples"])
        result.append((fp["sourceQuoteAudio"],fp["sourceQuote"].replace(" / "," ... ")))
        text=re.sub(r"\[出典:.*?\]\n?","",fp["practicePassage"]["en"])
        text=re.sub(r"(?m)^(?:A|B|Daughter|Mother|Father|Man(?: [12])?|Woman|Boy|Girl):\s*","",text)
        result.append((fp["practicePassage"]["audioFile"],text))
    return result


async def main():
    data=json.loads((BASE/"data.json").read_text(encoding="utf-8"))
    work=jobs(data)
    assert len(work)==105 and len({p for p,t in work})==105
    semaphore=asyncio.Semaphore(3)
    async def generate(ref,text):
        out=BASE/ref
        if out.is_file() and out.stat().st_size>=500: return
        async with semaphore:
            out.parent.mkdir(parents=True,exist_ok=True)
            partial=out.with_suffix(".mp3.tmp")
            for attempt in range(3):
                try:
                    await edge_tts.Communicate(text,VOICE,rate=RATE).save(str(partial))
                    if partial.stat().st_size<500: raise ValueError("empty audio")
                    partial.replace(out)
                    print(ref,flush=True)
                    return
                except Exception:
                    if partial.exists(): partial.unlink()
                    if attempt==2: raise
                    await asyncio.sleep(2*(attempt+1))
    await asyncio.gather(*(generate(p,t) for p,t in work))
    print(f"Audio OK: {len(work)} files",flush=True)


if __name__=="__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    asyncio.run(main())

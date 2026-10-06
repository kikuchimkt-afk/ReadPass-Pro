"""Established Grade 3 audio scope; atomic generation, no JSON mutation."""
import asyncio
import json
from pathlib import Path
import re
import sys
import edge_tts

BASE=Path(__file__).resolve().parent
VOICE="en-US-JennyNeural"
RATE="-15%"

def spoken(text):
    return re.sub(r"(?m)^(?:A|B|Customer|Clerk|Husband|Wife|Teacher|Student|Son|Mother):\s*","",text)

def jobs(data):
    result=[(v["wordAudio"],v["word"]) for v in data["vocabulary"]]
    for fp in data["lessonPlan"]["focusPoints"]:
        result.extend((e["audio"],spoken(e["en"])) for e in fp["examples"])
        result.append((fp["sourceQuoteAudio"],fp["sourceQuote"].replace(" / "," ... ")))
        text=re.sub(r"\[出典:.*?\]\n?","",fp["practicePassage"]["en"])
        result.append((fp["practicePassage"]["audioFile"],spoken(text)))
    return result

async def main():
    data=json.loads((BASE/"data.json").read_text(encoding="utf-8"))
    work=jobs(data)
    assert len(work)==len({p for p,t in work})==50
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

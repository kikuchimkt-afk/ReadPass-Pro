"""Existing Grade 4 audio content; atomic/retryable generation, no JSON mutation."""
import asyncio
import json
import os
from pathlib import Path
import re
import sys
import edge_tts
from edge_tts import communicate, constants

# The service changed its token in Oct 2026 (rany2/edge-tts#490); edge-tts 7.3.0+ sends the new
# "2-" token and needs nothing more. For older releases ("1-" token) present the locally installed
# Edge version instead (or EDGE_TTS_EDGE_VERSION).
EDGE_DIRS=[Path(r"C:\Program Files (x86)\Microsoft\Edge\Application"),
           Path(r"C:\Program Files\Microsoft\Edge\Application")]


def edge_version():
    if os.environ.get("EDGE_TTS_EDGE_VERSION"):
        return os.environ["EDGE_TTS_EDGE_VERSION"]
    found=[p.name for d in EDGE_DIRS if d.is_dir() for p in d.iterdir()
           if re.fullmatch(r"\d+\.\d+\.\d+\.\d+",p.name)]
    return max(found,key=lambda v:tuple(map(int,v.split(".")))) if found else None


def present_edge_version(full):
    major=full.split(".",1)[0]
    communicate.SEC_MS_GEC_VERSION=f"1-{full}"
    for headers in (constants.WSS_HEADERS,constants.VOICE_HEADERS,constants.BASE_HEADERS):
        for key,value in list(headers.items()):
            headers[key]=value.replace(constants.CHROMIUM_MAJOR_VERSION,major)

BASE=Path(__file__).resolve().parent
VOICE="en-US-JennyNeural"
RATE="-15%"
# A single word is about 11 KB at this voice/rate; a truncated stream once saved 2 KB.
MIN_BYTES=6000


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
                text=re.sub(r"(?m)^(?:A|B|Daughter|Mother|Boy|Girl|Teacher|Student|Father|Son):\s*","",q["text"])
                text=text.replace("(　)"," blank ").replace("\n"," ... ")
                text+=" ... "+" ... ".join(f"{i}. {c}" for i,c in enumerate(q["choices"],1))
            result.append((q["questionAudio"],text))
    for v in data["vocabulary"]:
        result.extend([(v["wordAudio"],v["word"]),(v["exampleAudio"],v["example"])])
    for fp in data["lessonPlan"]["focusPoints"]:
        result.extend((e["audio"],e["en"]) for e in fp["examples"])
        result.append((fp["sourceQuoteAudio"],fp["sourceQuote"].replace(" / "," ... ")))
        text=re.sub(r"\[出典:.*?\]\n?","",fp["practicePassage"]["en"])
        text=re.sub(r"(?m)^(?:A|B|Daughter|Mother|Boy|Girl|Teacher|Student|Father|Son):\s*","",text)
        result.append((fp["practicePassage"]["audioFile"],text))
    return result


async def main():
    data=json.loads((BASE/"data.json").read_text(encoding="utf-8"))
    work=jobs(data)
    assert len(work)==105 and len({p for p,t in work})==105
    semaphore=asyncio.Semaphore(3)
    async def generate(ref,text):
        out=BASE/ref
        if out.is_file() and out.stat().st_size>=MIN_BYTES: return
        async with semaphore:
            out.parent.mkdir(parents=True,exist_ok=True)
            partial=out.with_suffix(".mp3.tmp")
            for attempt in range(3):
                try:
                    await edge_tts.Communicate(text,VOICE,rate=RATE).save(str(partial))
                    if partial.stat().st_size<MIN_BYTES: raise ValueError("truncated audio")
                    partial.replace(out)
                    print(ref,flush=True)
                    return
                except Exception:
                    if partial.exists(): partial.unlink()
                    if attempt==2: raise
                    await asyncio.sleep(2*(attempt+1))
                except BaseException:
                    # A failed sibling cancels this job; leave no partial file behind.
                    if partial.exists(): partial.unlink()
                    raise
    await asyncio.gather(*(generate(p,t) for p,t in work))
    print(f"Audio OK: {len(work)} files",flush=True)


if __name__=="__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    version=edge_version()
    if version and communicate.SEC_MS_GEC_VERSION.startswith("1-"):
        present_edge_version(version)
    asyncio.run(main())

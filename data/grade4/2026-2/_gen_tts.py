"""Generate the 105 learning-audio files for Grade 4 2026-2 and link them in data.json.

Established Grade 4 scope and voice (en-US-JennyNeural, -15%): Q1-Q25 (stem and
choices, or the completed word-order sentence), 30 headwords and their examples, and
per focus point three examples, the source quote and the practice passage. Completed
files are skipped, so the script can be rerun after a failure. Only after every file
exists are questionAudio / wordAudio / exampleAudio / examples[].audio /
sourceQuoteAudio / practicePassage.audioFile written into data.json.

edge-tts 7.2.8 announces Edge 143, which the service refuses with 403 (Oct 2026);
edge-tts 7.3.0+ sends the new "2-" token (rany2/edge-tts#490) and needs no patch.
With an older release ("1-" token):
The script therefore presents the locally installed Edge version (or the
EDGE_TTS_EDGE_VERSION environment variable) and retries short 403 bursts with a
fresh connection.
"""
import asyncio
import json
import os
from pathlib import Path
import re
import sys

import aiohttp
import edge_tts
from edge_tts import communicate, constants

BASE = Path(__file__).resolve().parent
VOICE = "en-US-JennyNeural"
RATE = "-15%"
EDGE_DIRS = [Path(r"C:\Program Files (x86)\Microsoft\Edge\Application"),
             Path(r"C:\Program Files\Microsoft\Edge\Application")]
SPEAKERS = re.compile(r"(?m)^(?:A|B|Boy|Girl|Uncle|Daughter|Father|Son|Woman \d):\s*")


def edge_version():
    if os.environ.get("EDGE_TTS_EDGE_VERSION"):
        return os.environ["EDGE_TTS_EDGE_VERSION"]
    found = [p.name for d in EDGE_DIRS if d.is_dir() for p in d.iterdir()
             if re.fullmatch(r"\d+\.\d+\.\d+\.\d+", p.name)]
    return max(found, key=lambda v: tuple(map(int, v.split(".")))) if found else None


def present_edge_version(full):
    major = full.split(".", 1)[0]
    communicate.SEC_MS_GEC_VERSION = f"1-{full}"
    for headers in (constants.WSS_HEADERS, constants.VOICE_HEADERS, constants.BASE_HEADERS):
        for key, value in list(headers.items()):
            headers[key] = value.replace(constants.CHROMIUM_MAJOR_VERSION, major)


def slug(word):
    return re.sub(r"[^a-z0-9]+", "_", word.lower()).strip("_")


def completed(q):
    s = " ".join([q["framePrefix"], *[q["words"][i - 1] for i in q["correctOrder"]], q["frameSuffix"]]).strip()
    s = re.sub(r"\s+([.,?!])", r"\1", s)
    return s[0].upper() + s[1:]


def jobs(data):
    """(reference, spoken text) for every file, in a fixed order."""
    result = []
    for section in data["sections"]:
        for q in section.get("questions", []):
            if section["type"] == "sentence-order":
                text = completed(q)
            else:
                # Dialogue speaker labels are not read as part of a line.
                text = SPEAKERS.sub("", q["text"]).replace("(　)", " blank ").replace("\n", " ... ")
                text += " ... " + " ... ".join(f"{i}. {c}" for i, c in enumerate(q["choices"], 1))
            result.append((f"audio/q{q['number']}.mp3", text))
    for i, v in enumerate(data["vocabulary"], 1):
        result += [(f"audio/vocab/w_{i:03d}_{slug(v['word'])}.mp3", v["word"]),
                   (f"audio/vocab/ex_{i:03d}_{slug(v['word'])}.mp3", v["example"])]
    for n, fp in enumerate(data["lessonPlan"]["focusPoints"], 1):
        result += [(f"audio/fp{n}_ex{i}.mp3", SPEAKERS.sub("", e["en"])) for i, e in enumerate(fp["examples"], 1)]
        result.append((f"audio/fp{n}_source.mp3", fp["sourceQuote"].replace(" / ", " ... ")))
        text = re.sub(r"\[出典:.*?\]\n?", "", fp["practicePassage"]["en"])
        result.append((f"audio/practice_pp{n}.mp3", SPEAKERS.sub("", text)))
    return result


def link(data):
    refs = iter(ref for ref, _ in jobs(data))
    for section in data["sections"]:
        for q in section.get("questions", []):
            q["questionAudio"] = next(refs)
    for v in data["vocabulary"]:
        v["wordAudio"] = next(refs)
        v["exampleAudio"] = next(refs)
    for fp in data["lessonPlan"]["focusPoints"]:
        for e in fp["examples"]:
            e["audio"] = next(refs)
        fp["sourceQuoteAudio"] = next(refs)
        fp["practicePassage"]["audioFile"] = next(refs)


async def save(text, temp):
    for attempt in range(8):
        try:
            # A Communicate stream can only be consumed once, so retry with a new one.
            await edge_tts.Communicate(text, VOICE, rate=RATE).save(str(temp))
            return
        except aiohttp.WSServerHandshakeError as error:
            if error.status != 403 or attempt == 7:
                raise
            await asyncio.sleep(5 * (attempt + 1))


async def main():
    version = edge_version()
    if version and communicate.SEC_MS_GEC_VERSION.startswith("1-"):
        present_edge_version(version)
    data = json.loads((BASE / "data.json").read_text(encoding="utf-8"))
    work = jobs(data)
    assert len(work) == len({ref for ref, _ in work}) == 105
    for reference, text in work:
        out = BASE / reference
        if out.is_file() and out.stat().st_size >= 500:
            continue
        out.parent.mkdir(parents=True, exist_ok=True)
        temp = out.with_suffix(".tmp.mp3")
        try:
            await save(text, temp)
            if temp.stat().st_size < 500:
                raise RuntimeError(f"incomplete audio: {reference}")
            temp.replace(out)
            print(reference, flush=True)
        finally:
            temp.unlink(missing_ok=True)

    link(data)
    (BASE / "data.json").write_text(json.dumps(data, ensure_ascii=False, indent=4) + "\n", encoding="utf-8")
    print(f"AUDIO OK: {len(work)} files ({VOICE}, {RATE}, token {communicate.SEC_MS_GEC_VERSION})")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    asyncio.run(main())

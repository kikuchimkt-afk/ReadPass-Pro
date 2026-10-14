"""Generate the 50 learning-audio files for Grade 3 2026-2 and link them in data.json.

Established Grade 3 scope and voice (en-US-JennyNeural, -15%): 30 headwords, and per
focus point three examples, the source quote and the practice passage. Completed
files are skipped, so the script can be rerun after a failure. Only after every file
exists are wordAudio / examples[].audio / sourceQuoteAudio / practicePassage.audioFile
written into data.json.

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


def spoken(text):
    # Dialogue examples are read without their speaker labels.
    text = re.sub(r"(?m)^(?:A|B|Woman \d|Boy \d|Boy|Girl|Mother|Father|Son):\s*", "", text)
    return re.sub(r"\[出典:.*?\]\n?", "", text)


def jobs(data):
    """(reference, spoken text) for every file, in a fixed order."""
    result = [(f"audio/vocab/w_{i:03d}_{slug(v['word'])}.mp3", v["word"]) for i, v in enumerate(data["vocabulary"], 1)]
    for n, fp in enumerate(data["lessonPlan"]["focusPoints"], 1):
        result += [(f"audio/fp{n}_ex{i}.mp3", spoken(e["en"])) for i, e in enumerate(fp["examples"], 1)]
        result.append((f"audio/fp{n}_source.mp3", fp["sourceQuote"].replace(" / ", " ... ")))
        result.append((f"audio/practice_pp{n}.mp3", spoken(fp["practicePassage"]["en"])))
    return result


def link(data):
    refs = iter(ref for ref, _ in jobs(data))
    for v in data["vocabulary"]:
        v["wordAudio"] = next(refs)
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
    assert len(work) == len({ref for ref, _ in work}) == 50
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

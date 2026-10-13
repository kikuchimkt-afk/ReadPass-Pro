"""Generate the 115 learning-audio files for Grade Pre-2 Plus 2026-2 and link them in data.json.

Same voice/rate as the other ReadPass audio (en-US-JennyNeural, -15%). Completed
files are skipped, so the script can be rerun after a failure. Only after every
file exists are wordAudio / exampleAudio / practicePassage.audioFile written into data.json.

edge-tts 7.2.8 announces Edge 143, which the service refuses with 403 (Oct 2026).
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
    if version:
        present_edge_version(version)
    data = json.loads((BASE / "data.json").read_text(encoding="utf-8"))
    vocab_refs = [f"audio/vocab/w_{i:03d}_{slug(v['word'])}.mp3" for i, v in enumerate(data["vocabulary"], 1)]
    example_refs = [f"audio/vocab/ex_{i:03d}_{slug(v['word'])}.mp3" for i, v in enumerate(data["vocabulary"], 1)]
    focus_points = data["lessonPlan"]["focusPoints"]
    practice_refs = [f"audio/practice_pp{i}.mp3" for i in range(1, len(focus_points) + 1)]
    jobs = [(v["word"], ref) for v, ref in zip(data["vocabulary"], vocab_refs)]
    jobs += [(v["example"], ref) for v, ref in zip(data["vocabulary"], example_refs)]
    jobs += [(re.sub(r"^\[出典:.*?\]\n", "", fp["practicePassage"]["en"]), ref)
             for fp, ref in zip(focus_points, practice_refs)]

    for text, reference in jobs:
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

    for item, ref, example_ref in zip(data["vocabulary"], vocab_refs, example_refs):
        item["wordAudio"] = ref
        item["exampleAudio"] = example_ref
    for fp, ref in zip(focus_points, practice_refs):
        fp["practicePassage"]["audioFile"] = ref
    (BASE / "data.json").write_text(json.dumps(data, ensure_ascii=False, indent=4) + "\n", encoding="utf-8")
    print(f"AUDIO OK: {len(jobs)} files ({VOICE}, {RATE}, Edge {version or constants.CHROMIUM_FULL_VERSION})")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    asyncio.run(main())

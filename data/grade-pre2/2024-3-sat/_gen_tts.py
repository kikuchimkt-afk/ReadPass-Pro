"""Generate the 45 TTS files used by 2024-3-sat pre2."""

import asyncio
import json
import os
import re
import sys
from pathlib import Path

import edge_tts
from edge_tts import communicate, constants


sys.stdout.reconfigure(encoding="utf-8")

VOICE = "en-US-JennyNeural"
RATE = "-15%"
BASE = Path(__file__).resolve().parent
DATA_PATH = BASE / "data.json"
VOCAB_DIR = BASE / "audio" / "vocab"
# A single word is about 11 KB at this voice/rate; a truncated stream once saved 2 KB.
MIN_BYTES = 6000
ATTEMPTS = 3

# The service changed its token in Oct 2026 (rany2/edge-tts#490); edge-tts 7.3.0+ sends the
# new "2-" token and needs nothing more. For older releases ("1-" token) present the locally
# installed Edge version instead (or EDGE_TTS_EDGE_VERSION).
EDGE_DIRS = [
    Path(r"C:\Program Files (x86)\Microsoft\Edge\Application"),
    Path(r"C:\Program Files\Microsoft\Edge\Application"),
]


def edge_version() -> str | None:
    if os.environ.get("EDGE_TTS_EDGE_VERSION"):
        return os.environ["EDGE_TTS_EDGE_VERSION"]
    found = [
        path.name
        for folder in EDGE_DIRS
        if folder.is_dir()
        for path in folder.iterdir()
        if re.fullmatch(r"\d+\.\d+\.\d+\.\d+", path.name)
    ]
    return max(found, key=lambda v: tuple(map(int, v.split(".")))) if found else None


def present_edge_version(full: str) -> None:
    major = full.split(".", 1)[0]
    communicate.SEC_MS_GEC_VERSION = f"1-{full}"
    for headers in (constants.WSS_HEADERS, constants.VOICE_HEADERS, constants.BASE_HEADERS):
        for key, value in list(headers.items()):
            headers[key] = value.replace(constants.CHROMIUM_MAJOR_VERSION, major)


async def generate_audio(text: str, output_path: Path) -> None:
    partial = output_path.with_suffix(".mp3.tmp")
    for attempt in range(ATTEMPTS):
        try:
            await edge_tts.Communicate(text, VOICE, rate=RATE).save(str(partial))
            if partial.stat().st_size < MIN_BYTES:
                raise ValueError(f"truncated audio ({partial.stat().st_size} bytes)")
            partial.replace(output_path)
            return
        except Exception as error:
            if partial.exists():
                partial.unlink()
            if attempt == ATTEMPTS - 1:
                raise
            print(f"retry {attempt + 1}: {output_path.name}: {error}", flush=True)
            await asyncio.sleep(2 * (attempt + 1))


def safe_slug(word: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", word.lower()).strip("_")


def needs_audio(path: Path) -> bool:
    return not path.exists() or path.stat().st_size < MIN_BYTES


def main() -> None:
    version = edge_version()
    if version and communicate.SEC_MS_GEC_VERSION.startswith("1-"):
        present_edge_version(version)
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    VOCAB_DIR.mkdir(parents=True, exist_ok=True)

    generated_practice = 0
    for index, focus in enumerate(data["lessonPlan"]["focusPoints"], start=1):
        passage = focus["practicePassage"]
        text = re.sub(r"\[出典:.*?\]\n?", "", passage["en"]).strip()
        output_path = BASE / "audio" / f"practice_pp{index}.mp3"
        passage["audioFile"] = f"audio/practice_pp{index}.mp3"
        if text and needs_audio(output_path):
            asyncio.run(generate_audio(text, output_path))
            generated_practice += 1
            print(f"practice: {output_path.name}", flush=True)

    generated_words = 0
    for index, item in enumerate(data["vocabulary"], start=1):
        slug = safe_slug(item["word"])
        filename = f"w_{index:03d}_{slug}.mp3"
        output_path = VOCAB_DIR / filename
        item["wordAudio"] = f"audio/vocab/{filename}"
        if needs_audio(output_path):
            asyncio.run(generate_audio(item["word"], output_path))
            generated_words += 1
            print(f"word: {filename}", flush=True)

    DATA_PATH.write_text(
        json.dumps(data, ensure_ascii=False, indent=4) + "\n",
        encoding="utf-8",
    )
    print(
        f"Done: {generated_practice} practice / {generated_words} word audio",
        flush=True,
    )


if __name__ == "__main__":
    main()

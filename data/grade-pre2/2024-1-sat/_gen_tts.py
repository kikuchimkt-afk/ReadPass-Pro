"""Generate the 45 TTS files used by 2024-1-sat pre2."""

import asyncio
import json
import re
import sys
from pathlib import Path

import edge_tts


sys.stdout.reconfigure(encoding="utf-8")

VOICE = "en-US-JennyNeural"
RATE = "-15%"
BASE = Path(__file__).resolve().parent
DATA_PATH = BASE / "data.json"
VOCAB_DIR = BASE / "audio" / "vocab"


async def generate_audio(text: str, output_path: Path) -> None:
    await edge_tts.Communicate(text, VOICE, rate=RATE).save(str(output_path))


def safe_slug(word: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", word.lower()).strip("_")


def needs_audio(path: Path) -> bool:
    return not path.exists() or path.stat().st_size < 500


def main() -> None:
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

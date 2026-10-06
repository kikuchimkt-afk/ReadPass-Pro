"""Existing ReadPass voice/rate, deterministic references, retryable generation.

Requires edge-tts. This script never edits data.json. Only complete audio files
are published; rerunning skips completed files and retries missing ones.
"""
import asyncio
import json
from pathlib import Path
import re
import sys

import edge_tts

BASE = Path(__file__).resolve().parent
VOICE = "en-US-JennyNeural"
RATE = "-15%"


async def main():
    data = json.loads((BASE / "data.json").read_text(encoding="utf-8"))
    jobs = [(v["word"], v["wordAudio"]) for v in data["vocabulary"]]
    jobs += [(re.sub(r"^\[出典:.*?\]\n", "", fp["practicePassage"]["en"]),
              fp["practicePassage"]["audioFile"])
             for fp in data["lessonPlan"]["focusPoints"]]
    semaphore = asyncio.Semaphore(3)

    async def generate(text, reference):
        out = BASE / reference
        if out.is_file() and out.stat().st_size >= 500:
            return
        out.parent.mkdir(parents=True, exist_ok=True)
        temp = out.with_suffix(".tmp.mp3")
        async with semaphore:
            for attempt in range(3):
                try:
                    await edge_tts.Communicate(text, VOICE, rate=RATE).save(str(temp))
                    if temp.stat().st_size < 500:
                        raise RuntimeError("incomplete audio")
                    temp.replace(out)
                    print(reference, flush=True)
                    return
                except Exception:
                    temp.unlink(missing_ok=True)
                    if attempt == 2:
                        raise
                    await asyncio.sleep(2 * (attempt + 1))

    await asyncio.gather(*(generate(text, ref) for text, ref in jobs))
    print(f"AUDIO OK: {len(jobs)} files ({VOICE}, {RATE})")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    asyncio.run(main())

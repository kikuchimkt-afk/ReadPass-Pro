"""Generate the established word/example/practice MP3s without editing JSON.

Install edge-tts, then run this script. Voice/rate match 2026-1-sat.
Only data.json references are used; temporary files are replaced atomically.
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
    d = json.loads((BASE / "data.json").read_text(encoding="utf-8"))
    jobs = [(v["word"], v["wordAudio"]) for v in d["vocabulary"]]
    jobs += [(v["example"], v["exampleAudio"]) for v in d["vocabulary"]]
    jobs += [(re.sub(r"^\[出典:.*?\]\s*", "", fp["practicePassage"]["en"]),
              fp["practicePassage"]["audioFile"]) for fp in d["lessonPlan"]["focusPoints"]]
    gate = asyncio.Semaphore(3)
    async def generate(text, ref):
        out = (BASE / ref).resolve()
        if not out.is_relative_to(BASE.resolve()):
            raise ValueError(ref)
        if out.is_file() and out.stat().st_size >= 500:
            return
        out.parent.mkdir(parents=True, exist_ok=True)
        temp = out.with_suffix(".tmp.mp3")
        async with gate:
            for attempt in range(3):
                try:
                    await edge_tts.Communicate(text, VOICE, rate=RATE).save(str(temp))
                    if temp.stat().st_size < 500:
                        raise ValueError("incomplete MP3")
                    temp.replace(out)
                    print(ref, flush=True)
                    return
                except Exception:
                    if attempt == 2:
                        raise
                    await asyncio.sleep(2 * (attempt + 1))
    await asyncio.gather(*(generate(text, ref) for text, ref in jobs))
    print(f"OK: {len(jobs)} word/example/practice audio files; JSON unchanged")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    asyncio.run(main())

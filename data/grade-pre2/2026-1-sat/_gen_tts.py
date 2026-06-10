"""Generate TTS audio for vocabulary words and example sentences - 2026-1-sat pre2"""
import json
import os
import asyncio
import re
import sys

import edge_tts

sys.stdout.reconfigure(encoding="utf-8")

VOICE = "en-US-JennyNeural"
RATE = "-15%"

BASE = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(BASE, "data.json")
d = json.load(open(data_path, encoding="utf-8"))

vocab_dir = os.path.join(BASE, "audio", "vocab")
os.makedirs(vocab_dir, exist_ok=True)


async def gen_tts(text, outpath):
    c = edge_tts.Communicate(text, VOICE, rate=RATE)
    await c.save(outpath)


def safe_slug(word):
    return re.sub(r"[^a-zA-Z0-9_]", "_", word.lower()).strip("_")


vocab = d.get("vocabulary", [])
word_count = 0
ex_count = 0

for i, v in enumerate(vocab):
    word = v["word"]
    example = v.get("example", "")
    slug = safe_slug(word)

    w_fname = f"w_{i + 1:03d}_{slug}.mp3"
    w_out = os.path.join(vocab_dir, w_fname)
    if not os.path.exists(w_out) or os.path.getsize(w_out) < 500:
        asyncio.run(gen_tts(word, w_out))
        word_count += 1
        print(f"  word: {w_fname}", flush=True)
    v["wordAudio"] = f"audio/vocab/{w_fname}"

    if example:
        ex_fname = f"ex_{i + 1:03d}_{slug}.mp3"
        ex_out = os.path.join(vocab_dir, ex_fname)
        if not os.path.exists(ex_out) or os.path.getsize(ex_out) < 500:
            asyncio.run(gen_tts(example, ex_out))
            ex_count += 1
            print(f"  example: {ex_fname}", flush=True)
        v["exampleAudio"] = f"audio/vocab/{ex_fname}"

with open(data_path, "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=4)

print(f"\nDone: {word_count} new word / {ex_count} new example / {len(vocab)} total")

# -*- coding: utf-8 -*-
"""Generate TTS audio for vocabulary words - 2026-1 pre2plus (本会場, EdgeTTS)"""
import asyncio
import json
import os
import re
import sys

import edge_tts

sys.stdout.reconfigure(encoding="utf-8")

VOICE = "en-US-JennyNeural"
RATE = "-15%"

base = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base, "data.json")
audio_dir = os.path.join(base, "audio")
vocab_dir = os.path.join(audio_dir, "vocab")
os.makedirs(vocab_dir, exist_ok=True)

d = json.load(open(data_path, encoding="utf-8"))


async def gen_tts(text, outpath):
    c = edge_tts.Communicate(text, VOICE, rate=RATE)
    await c.save(outpath)


fps = d.get("lessonPlan", {}).get("focusPoints", [])
pp_count = 0
for i, fp in enumerate(fps):
    pp = fp.get("practicePassage", {})
    en = pp.get("en", "")
    en_clean = re.sub(r"\[出典:.*?\]\n?", "", en).strip()
    fname = f"practice_pp{i + 1}.mp3"
    outpath = os.path.join(audio_dir, fname)
    if en_clean and (not os.path.exists(outpath) or os.path.getsize(outpath) < 500):
        asyncio.run(gen_tts(en_clean, outpath))
        pp_count += 1
        print(f"  practice: {fname}", flush=True)
    if en_clean:
        pp["audioFile"] = f"audio/{fname}"

vocab = d.get("vocabulary", [])
count = 0
for i, v in enumerate(vocab):
    word = v["word"]
    safe = re.sub(r"[^a-zA-Z0-9_]", "_", word.lower()).strip("_")
    fname = f"w_{i + 1:03d}_{safe}.mp3"
    outpath = os.path.join(vocab_dir, fname)
    if not os.path.exists(outpath) or os.path.getsize(outpath) < 500:
        asyncio.run(gen_tts(word, outpath))
        count += 1
        print(f"  {fname}", flush=True)
    v["wordAudio"] = f"audio/vocab/{fname}"

with open(data_path, "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=4)
print(f"\nDone: practice {pp_count} new, vocab {count} new / {len(vocab)} total")

# -*- coding: utf-8 -*-
"""Generate TTS audio for vocabulary and lessonPlan - 2026-1-sat grade3"""
import asyncio
import json
import os
import re
import sys

import edge_tts

sys.stdout.reconfigure(encoding="utf-8")

VOICE = "en-US-JennyNeural"
RATE = "-15%"

BASE = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(BASE, "data.json")
d = json.load(open(data_path, encoding="utf-8"))

audio_dir = os.path.join(BASE, "audio")
vocab_dir = os.path.join(audio_dir, "vocab")
os.makedirs(vocab_dir, exist_ok=True)


async def gen_tts(text, outpath):
    c = edge_tts.Communicate(text, VOICE, rate=RATE)
    await c.save(outpath)


def safe_slug(word):
    return re.sub(r"[^a-zA-Z0-9_]", "_", word.lower()).strip("_")


def needs_gen(path):
    return not os.path.exists(path) or os.path.getsize(path) < 500


vocab_count = 0
for i, v in enumerate(d.get("vocabulary", [])):
    word = v["word"]
    slug = safe_slug(word)
    w_fname = f"w_{i + 1:03d}_{slug}.mp3"
    w_out = os.path.join(vocab_dir, w_fname)
    if needs_gen(w_out):
        asyncio.run(gen_tts(word, w_out))
        vocab_count += 1
        print(f"  vocab: {w_fname}", flush=True)
    v["wordAudio"] = f"audio/vocab/{w_fname}"

lp_count = 0
fps = d.get("lessonPlan", {}).get("focusPoints", [])
for fi, fp in enumerate(fps):
    fp_id = fp.get("id", f"fp{fi + 1}")
    for ei, ex in enumerate(fp.get("examples", [])):
        en = ex.get("en", "").strip()
        if not en:
            continue
        fname = f"{fp_id}_ex{ei + 1}.mp3"
        outpath = os.path.join(audio_dir, fname)
        if needs_gen(outpath):
            asyncio.run(gen_tts(en, outpath))
            lp_count += 1
            print(f"  example: {fname}", flush=True)
        ex["audio"] = f"audio/{fname}"

    pp = fp.get("practicePassage", {})
    en = pp.get("en", "")
    en_clean = re.sub(r"\[出典:.*?\]\n?", "", en).strip()
    pp_fname = f"practice_pp{fi + 1}.mp3"
    pp_out = os.path.join(audio_dir, pp_fname)
    if en_clean and needs_gen(pp_out):
        asyncio.run(gen_tts(en_clean, pp_out))
        lp_count += 1
        print(f"  practice: {pp_fname}", flush=True)
    if en_clean:
        pp["audioFile"] = f"audio/{pp_fname}"

    sq = fp.get("sourceQuote", "")
    if sq:
        sq_fname = f"{fp_id}_source.mp3"
        sq_out = os.path.join(audio_dir, sq_fname)
        if needs_gen(sq_out):
            asyncio.run(gen_tts(sq, sq_out))
            lp_count += 1
            print(f"  sourceQuote: {sq_fname}", flush=True)
        fp["sourceQuoteAudio"] = f"audio/{sq_fname}"

with open(data_path, "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=4)

print(f"\nDone: {vocab_count} vocab / {lp_count} lessonPlan audio")

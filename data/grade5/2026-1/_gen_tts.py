# -*- coding: utf-8 -*-
"""Generate TTS audio - 2026-1 grade5（本会場, EdgeTTS）"""
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


def sentence_order_tts_text(q):
    words = q.get("words", [])
    order = q.get("correctOrder", [])
    if not words or not order or len(words) != len(order):
        return None
    ordered = [words[i - 1] for i in order]
    prefix = (q.get("framePrefix") or "").strip()
    suffix = (q.get("frameSuffix") or "").strip()
    parts = []
    if prefix:
        parts.append(prefix)
    parts.extend(ordered)
    sentence = " ".join(parts)
    if suffix:
        if suffix.startswith((".", "?", "!")):
            sentence += suffix
        else:
            sentence += " " + suffix
    sentence = sentence.strip()
    if sentence and not prefix:
        sentence = sentence[0].upper() + sentence[1:]
    return sentence


def question_tts_text(q):
    if q.get("words") and q.get("correctOrder"):
        so = sentence_order_tts_text(q)
        if so:
            return so
    raw = (q.get("text") or "").replace("(　)", " blank ").replace("\u3000", " blank ")
    raw = raw.replace("\n", " ... ").strip()
    choices = q.get("choices", [])
    if choices:
        opts = " ... ".join(f"{i + 1}. {c}" for i, c in enumerate(choices))
        return f"{raw} ... {opts}"
    return raw


def iter_section_questions(sec):
    for q in sec.get("questions", []):
        yield q
    for pa in sec.get("passages", []):
        for q in pa.get("questions", []):
            yield q


q_count = 0
for sec in d.get("sections", []):
    for q in iter_section_questions(sec):
        qa = q.get("questionAudio")
        if not qa:
            continue
        out = os.path.join(BASE, qa.replace("/", os.sep))
        os.makedirs(os.path.dirname(out), exist_ok=True)
        if needs_gen(out):
            asyncio.run(gen_tts(question_tts_text(q), out))
            q_count += 1
            print(f"  question: {qa}", flush=True)

word_count = 0
ex_count = 0
for i, v in enumerate(d.get("vocabulary", [])):
    word = v["word"]
    example = v.get("example", "")
    slug = safe_slug(word)
    w_fname = f"w_{i + 1:03d}_{slug}.mp3"
    w_out = os.path.join(vocab_dir, w_fname)
    if needs_gen(w_out):
        asyncio.run(gen_tts(word, w_out))
        word_count += 1
        print(f"  word: {w_fname}", flush=True)
    v["wordAudio"] = f"audio/vocab/{w_fname}"
    if example:
        ex_fname = f"ex_{i + 1:03d}_{slug}.mp3"
        ex_out = os.path.join(vocab_dir, ex_fname)
        if needs_gen(ex_out):
            asyncio.run(gen_tts(example, ex_out))
            ex_count += 1
            print(f"  example: {ex_fname}", flush=True)
        v["exampleAudio"] = f"audio/vocab/{ex_fname}"

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

print(f"\nDone: {q_count} question / {word_count} word / {ex_count} example / {lp_count} lessonPlan audio")

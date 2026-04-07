"""Generate TTS audio for Grade 5 2021-2"""
import json, os, asyncio, re
import edge_tts

VOICE = "en-US-JennyNeural"
RATE = "-30%"  # 5級は-30%

base = r"g:\マイドライブ\ReadPass Pro\data\grade5\2021-2"
data_path = os.path.join(base, "data.json")
d = json.load(open(data_path, encoding="utf-8"))

audio_dir = os.path.join(base, "audio")
os.makedirs(audio_dir, exist_ok=True)

async def gen_tts(text, outpath):
    c = edge_tts.Communicate(text, VOICE, rate=RATE)
    await c.save(outpath)

# 1. Practice passage audio (FPs)
fps = d.get("lessonPlan", {}).get("focusPoints", [])
for i, fp in enumerate(fps):
    pp = fp.get("practicePassage", {})
    en = pp.get("en", "")
    en_clean = re.sub(r'\[出典:.*?\]\n?', '', en).strip()
    fname = f"practice_pp{i+1}.mp3"
    outpath = os.path.join(audio_dir, fname)
    if not os.path.exists(outpath) or os.path.getsize(outpath) < 500:
        print(f"  Generating {fname}...", flush=True)
        asyncio.run(gen_tts(en_clean, outpath))
        print(f"  Done: {fname} ({os.path.getsize(outpath)} bytes)", flush=True)
    else:
        print(f"  Skip {fname} (exists)", flush=True)
    pp["audioFile"] = f"audio/{fname}"

print(f"\nPractice passages: {len(fps)} files")

# 2. Vocabulary word audio
vocab = d.get("vocabulary", [])
for i, v in enumerate(vocab):
    word = v["word"]
    safe = re.sub(r"[^a-zA-Z0-9_]", "_", word.lower()).strip("_")
    fname = f"word_{safe}.mp3"
    outpath = os.path.join(audio_dir, fname)
    if not os.path.exists(outpath) or os.path.getsize(outpath) < 500:
        asyncio.run(gen_tts(word, outpath))
        print(f"  {fname}", flush=True)
    v["wordAudio"] = f"audio/{fname}"

print(f"\nVocabulary audio: {len(vocab)} files")

# 3. Question audio (Q1-Q25) - 5級固有
for sec in d["sections"]:
    for q in sec["questions"]:
        n = q["number"]
        fname = f"q{n}.mp3"
        outpath = os.path.join(audio_dir, fname)
        
        if sec["type"] == "sentence-order":
            # 大問3: 完成文を読み上げ
            order = q.get("correctOrder", [])
            words = q.get("words", [])
            ordered = [words[idx-1] for idx in order]
            prefix = q.get("framePrefix", "").strip()
            suffix = q.get("frameSuffix", "").strip()
            parts = []
            if prefix: parts.append(prefix)
            parts.extend(ordered)
            if suffix: parts.append(suffix)
            tts_text = " ".join(parts)
        else:
            # 大問1-2: 問題文+選択肢
            text = q["text"].replace("(　)", "... ...").replace("( )", "... ...")
            choices_text = ". ".join([f"{i+1}, {c}" for i, c in enumerate(q["choices"])])
            tts_text = f"{text}. {choices_text}"
        
        if not os.path.exists(outpath) or os.path.getsize(outpath) < 500:
            asyncio.run(gen_tts(tts_text, outpath))
            print(f"  {fname}", flush=True)
        q["questionAudio"] = f"audio/{fname}"

print(f"\nQuestion audio: 25 files")

# 4. FP sourceQuote + examples audio
for i, fp in enumerate(fps):
    # sourceQuote
    sq = fp.get("sourceQuote", "")
    if sq:
        fname = f"sq_fp{i+1}.mp3"
        outpath = os.path.join(audio_dir, fname)
        if not os.path.exists(outpath) or os.path.getsize(outpath) < 500:
            asyncio.run(gen_tts(sq, outpath))
            print(f"  {fname}", flush=True)
        fp["sourceQuoteAudio"] = f"audio/{fname}"
    
    # examples
    for j, ex in enumerate(fp.get("examples", [])):
        fname = f"ex_fp{i+1}_{j+1}.mp3"
        outpath = os.path.join(audio_dir, fname)
        if not os.path.exists(outpath) or os.path.getsize(outpath) < 500:
            asyncio.run(gen_tts(ex["en"], outpath))
            print(f"  {fname}", flush=True)
        ex["audio"] = f"audio/{fname}"

print(f"\nFP audio: done")

# Save updated data.json
with open(data_path, "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=4)
print(f"\ndata.json updated with audio paths")

# Count total MP3s
mp3_count = len([f for f in os.listdir(audio_dir) if f.endswith('.mp3')])
print(f"\nTotal MP3 files: {mp3_count}")

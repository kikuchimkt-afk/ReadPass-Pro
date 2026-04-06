"""Generate TTS audio for practice passages and vocabulary - 2021-3"""
import json, os, asyncio, re
import edge_tts

VOICE = "en-US-JennyNeural"
RATE = "-15%"

base = r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade-pre2\2021-3"
data_path = os.path.join(base, "data.json")
d = json.load(open(data_path, encoding="utf-8"))

audio_dir = os.path.join(base, "audio")
os.makedirs(audio_dir, exist_ok=True)
vocab_dir = os.path.join(audio_dir, "vocab")
os.makedirs(vocab_dir, exist_ok=True)

async def gen_tts(text, outpath):
    c = edge_tts.Communicate(text, VOICE, rate=RATE)
    await c.save(outpath)

# 1. Practice passage audio
fps = d.get("lessonPlan", {}).get("focusPoints", [])
for i, fp in enumerate(fps):
    pp = fp.get("practicePassage", {})
    en = pp.get("en", "")
    # Remove [出典:...] tag
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

# 2. Vocabulary audio
vocab = d.get("vocabulary", [])
for i, v in enumerate(vocab):
    word = v["word"]
    safe = re.sub(r"[^a-zA-Z0-9_]", "_", word.lower()).strip("_")
    fname = f"w_{i+1:03d}_{safe}.mp3"
    outpath = os.path.join(vocab_dir, fname)
    if not os.path.exists(outpath) or os.path.getsize(outpath) < 500:
        asyncio.run(gen_tts(word, outpath))
        print(f"  {fname}", flush=True)
    v["wordAudio"] = f"audio/vocab/{fname}"

print(f"\nVocabulary audio: {len(vocab)} files")

# Save updated data.json
with open(data_path, "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=4)
print(f"\ndata.json updated with audio paths")

"""準2級 2023-1 TTS + vocab audio generation (local)"""
import json, os, asyncio, re
import edge_tts

VOICE = "en-US-JennyNeural"
RATE = "-20%"

def clean_tts_text(text):
    return re.sub(r'\[出典:\s*.+?\]\s*\n?', '', text).strip()

async def gen(text, out):
    c = edge_tts.Communicate(clean_tts_text(text), VOICE, rate=RATE)
    await c.save(out)

path = r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade-pre2\2023-1\data.json"
d = json.load(open(path, "r", encoding="utf-8"))
base = os.path.dirname(path)
audio_dir = os.path.join(base, "audio")
os.makedirs(audio_dir, exist_ok=True)
os.makedirs(os.path.join(audio_dir, "vocab"), exist_ok=True)

# 1. Practice passage TTS
fps = d["lessonPlan"]["focusPoints"]
for i, fp in enumerate(fps):
    pp = fp.get("practicePassage", {})
    en = pp.get("en", "")
    if not en: continue
    fname = f"practice_pp{i+1}.mp3"
    out = os.path.join(audio_dir, fname)
    asyncio.run(gen(en, out))
    pp["audioFile"] = f"audio/{fname}"
    size_kb = os.path.getsize(out) / 1024
    print(f"  ✅ {fname} ({size_kb:.0f}KB)")

# 2. Vocab audio
vocab = d.get("vocabulary", [])
for i, v in enumerate(vocab):
    word = v["word"]
    safe = re.sub(r"[^a-zA-Z0-9_]", "_", word.lower()).strip("_")
    fname = f"w_{i+1:03d}_{safe}.mp3"
    out = os.path.join(audio_dir, "vocab", fname)
    if not os.path.exists(out) or os.path.getsize(out) < 500:
        asyncio.run(gen(word, out))
    v["wordAudio"] = f"audio/vocab/{fname}"

# Save
with open(path, "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=4)
print(f"\n✅ TTS: {len(fps)} passages, {len(vocab)} vocab words")

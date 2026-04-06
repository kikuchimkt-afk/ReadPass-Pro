import json, os, asyncio, re
import edge_tts

VOICE = "en-US-JennyNeural"
RATE = "-15%"

async def gen(word, out):
    c = edge_tts.Communicate(word, VOICE, rate=RATE)
    await c.save(out)

path = r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade-pre2\2023-2\data.json"
d = json.load(open(path, encoding="utf-8"))
vocab = d.get("vocabulary", [])
audio_dir = os.path.join(os.path.dirname(path), "audio", "vocab")
os.makedirs(audio_dir, exist_ok=True)

count = 0
for i, v in enumerate(vocab):
    word = v["word"]
    safe = re.sub(r"[^a-zA-Z0-9_]", "_", word.lower()).strip("_")
    fname = f"w_{i+1:03d}_{safe}.mp3"
    out = os.path.join(audio_dir, fname)
    if not os.path.exists(out) or os.path.getsize(out) < 500:
        asyncio.run(gen(word, out))
        count += 1
        print(f"  {fname}", flush=True)
    v["wordAudio"] = f"audio/vocab/{fname}"

with open(path, "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=4)
print(f"\nDone: {count} new / {len(vocab)} total words")

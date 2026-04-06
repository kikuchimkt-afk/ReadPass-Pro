"""
ローカル data.json から全FPのpracticePassage TTS音声を再生成
generate_tts.py はGDrive側を参照するため、ローカル用に直接生成する
"""
import json, os, asyncio, re, hashlib
import edge_tts

VOICE = "en-US-JennyNeural"
RATE = "-20%"  # grade-pre2 rate

def clean_tts_text(text):
    return re.sub(r'\[出典:\s*.+?\]\s*\n?', '', text).strip()

async def gen(text, out):
    cleaned = clean_tts_text(text)
    c = edge_tts.Communicate(cleaned, VOICE, rate=RATE)
    await c.save(out)
    return cleaned

path = r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade-pre2\2023-2\data.json"
d = json.load(open(path, "r", encoding="utf-8"))
fps = d["lessonPlan"]["focusPoints"]
audio_dir = os.path.join(os.path.dirname(path), "audio")
os.makedirs(audio_dir, exist_ok=True)

for i, fp in enumerate(fps):
    pp = fp.get("practicePassage", {})
    en = pp.get("en", "")
    if not en:
        print(f"  FP{i+1}: NO en text, skipping")
        continue
    
    fname = f"practice_pp{i+1}.mp3"
    out = os.path.join(audio_dir, fname)
    
    cleaned = asyncio.run(gen(en, out))
    size_kb = os.path.getsize(out) / 1024
    pp["audioFile"] = f"audio/{fname}"
    
    # Show first 80 chars of cleaned text for verification
    preview = cleaned[:80].replace('\n', ' ')
    print(f"  ✅ {fname} ({size_kb:.0f}KB)")
    print(f"     Text: {preview}...")

with open(path, "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=4)
print(f"\n✅ {len(fps)}件のTTS音声を再生成しました")

"""Generate all TTS audio for grade5 2022-2 (~65 files)"""
import json, os, asyncio, re, sys
sys.stdout.reconfigure(encoding='utf-8')

try:
    import edge_tts
except ImportError:
    os.system("pip install edge-tts")
    import edge_tts

BASE = r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade5\2022-2"
AUDIO = os.path.join(BASE, "audio")
os.makedirs(AUDIO, exist_ok=True)

DATA = json.load(open(os.path.join(BASE, "data.json"), "r", encoding="utf-8"))
RATE = "-30%"
VOICE = "en-US-JennyNeural"
VOICE_JA = "ja-JP-NanamiNeural"

generated = 0
skipped = 0

async def tts(text, path, voice=VOICE, rate=RATE):
    global generated, skipped
    if os.path.exists(path):
        skipped += 1
        return
    c = edge_tts.Communicate(text, voice, rate=rate)
    await c.save(path)
    generated += 1

async def main():
    global generated, skipped
    tasks = []

    # 1. Question audio (q1-q25)
    for sec in DATA["sections"]:
        for q in sec.get("questions", []):
            num = q["number"]
            path = os.path.join(AUDIO, f"q{num}.mp3")
            if sec["type"] == "sentence-order":
                # Read completed sentence
                words = q.get("words", [])
                order = q.get("correctOrder", [])
                prefix = q.get("framePrefix", "")
                suffix = q.get("frameSuffix", "")
                ordered = [words[i-1] for i in order]
                sentence = f"{prefix} {' '.join(ordered)} {suffix}".strip()
                text = sentence
            else:
                # Read question + choices
                raw = q["text"].replace("(　)", "... ...").replace("(\u3000)", "... ...")
                raw = raw.replace("\\n", "\n").replace("\n", " ... ")
                choices = q.get("choices", [])
                choice_text = " ... ".join([f"{i+1}. {c}" for i, c in enumerate(choices)])
                text = f"{raw} ... {choice_text}"
            tasks.append(tts(text, path))

    # 2. Word audio
    for v in DATA.get("vocabulary", []):
        word = v["word"]
        safe = re.sub(r'[^a-zA-Z0-9_]', '_', word)
        path = os.path.join(AUDIO, f"word_{safe}.mp3")
        tasks.append(tts(word, path))

    # 3. FP sourceQuote + examples audio
    fps = DATA.get("lessonPlan", {}).get("focusPoints", [])
    for fp in fps:
        fid = fp["id"]
        sq = fp.get("sourceQuote", "")
        if sq:
            path = os.path.join(AUDIO, f"sq_{fid}.mp3")
            tasks.append(tts(sq, path))
        for i, ex in enumerate(fp.get("examples", []), 1):
            en = ex.get("en", "")
            if en:
                path = os.path.join(AUDIO, f"ex_{fid}_{i}.mp3")
                tasks.append(tts(en, path))

    # 4. Practice passage audio
    for i, fp in enumerate(fps, 1):
        pp = fp.get("practicePassage", {})
        paragraphs = pp.get("paragraphs", [])
        if paragraphs:
            text = " ".join(paragraphs)
            path = os.path.join(AUDIO, f"practice_pp{i}.mp3")
            tasks.append(tts(text, path))

    # Run all
    for t in tasks:
        await t

    print(f"Generated: {generated}, Skipped: {skipped}, Total: {generated + skipped}")

asyncio.run(main())

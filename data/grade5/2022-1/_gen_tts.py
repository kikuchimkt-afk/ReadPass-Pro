"""Generate TTS audio for Grade 5 2022-1"""
import json, os, asyncio, re
import edge_tts

VOICE = "en-US-JennyNeural"
RATE = "-30%"

base = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base, "data.json")
d = json.load(open(data_path, encoding="utf-8"))

audio_dir = os.path.join(base, "audio")
os.makedirs(audio_dir, exist_ok=True)

async def gen_tts(text, outpath):
    c = edge_tts.Communicate(text, VOICE, rate=RATE)
    await c.save(outpath)

fps = d.get("lessonPlan", {}).get("focusPoints", [])
for i, fp in enumerate(fps):
    pp = fp.get("practicePassage", {})
    en = pp.get("en", "").strip()
    fname = f"practice_pp{i+1}.mp3"
    outpath = os.path.join(audio_dir, fname)
    if not os.path.exists(outpath) or os.path.getsize(outpath) < 500:
        print(f"  {fname}...", flush=True)
        asyncio.run(gen_tts(en, outpath))
    pp["audioFile"] = f"audio/{fname}"

for v in d.get("vocabulary", []):
    safe = re.sub(r"[^a-zA-Z0-9_]", "_", v["word"].lower()).strip("_")
    fname = f"word_{safe}.mp3"
    outpath = os.path.join(audio_dir, fname)
    if not os.path.exists(outpath) or os.path.getsize(outpath) < 500:
        asyncio.run(gen_tts(v["word"], outpath))
        print(f"  {fname}", flush=True)
    v["wordAudio"] = f"audio/{fname}"

for sec in d["sections"]:
    for q in sec["questions"]:
        n = q["number"]
        fname = f"q{n}.mp3"
        outpath = os.path.join(audio_dir, fname)
        if sec["type"] == "sentence-order":
            order = q.get("correctOrder", [])
            words = q.get("words", [])
            ordered = [words[idx-1] for idx in order]
            parts = []
            if q.get("framePrefix","").strip(): parts.append(q["framePrefix"].strip())
            parts.extend(ordered)
            if q.get("frameSuffix","").strip(): parts.append(q["frameSuffix"].strip())
            tts_text = " ".join(parts)
        else:
            text = q["text"].replace("(　)", "... ...").replace("( )", "... ...")
            choices_text = ". ".join([f"{i+1}, {c}" for i, c in enumerate(q["choices"])])
            tts_text = f"{text}. {choices_text}"
        if not os.path.exists(outpath) or os.path.getsize(outpath) < 500:
            asyncio.run(gen_tts(tts_text, outpath))
            print(f"  {fname}", flush=True)
        q["questionAudio"] = f"audio/{fname}"

for i, fp in enumerate(fps):
    sq = fp.get("sourceQuote", "")
    if sq:
        fname = f"sq_fp{i+1}.mp3"
        outpath = os.path.join(audio_dir, fname)
        if not os.path.exists(outpath) or os.path.getsize(outpath) < 500:
            asyncio.run(gen_tts(sq, outpath))
            print(f"  {fname}", flush=True)
        fp["sourceQuoteAudio"] = f"audio/{fname}"
    for j, ex in enumerate(fp.get("examples", [])):
        fname = f"ex_fp{i+1}_{j+1}.mp3"
        outpath = os.path.join(audio_dir, fname)
        if not os.path.exists(outpath) or os.path.getsize(outpath) < 500:
            asyncio.run(gen_tts(ex["en"], outpath))
            print(f"  {fname}", flush=True)
        ex["audio"] = f"audio/{fname}"

with open(data_path, "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=4)

mp3s = len([f for f in os.listdir(audio_dir) if f.endswith('.mp3')])
print(f"\nDone! {mp3s} MP3 files total")

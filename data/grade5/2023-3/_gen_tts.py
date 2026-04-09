"""Generate ALL TTS audio for 2023-1: questions, vocab, FP sourceQuotes, FP examples, practice passages"""
import json, os, asyncio, sys, subprocess, shutil
sys.stdout.reconfigure(encoding='utf-8')

try:
    import edge_tts
except ImportError:
    os.system("pip install edge-tts")
    import edge_tts

ROOT = r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade5\2023-3"
RATE = "-30%"
VOICE = "en-US-JennyNeural"

async def tts_to_file(text, path, voice=VOICE, rate=RATE, retries=3):
    for attempt in range(retries):
        try:
            c = edge_tts.Communicate(text, voice, rate=rate)
            await c.save(path)
            return True
        except Exception as e:
            if attempt < retries - 1:
                await asyncio.sleep(2)
            else:
                print(f"    ⚠ TTS failed: {text[:40]}... -> {e}")
                return False

def generate_silence(path, duration_ms=500):
    subprocess.run(["ffmpeg", "-y", "-f", "lavfi", "-i", f"anullsrc=r=24000:cl=mono",
        "-t", str(duration_ms / 1000), "-c:a", "libmp3lame", "-q:a", "9", path], capture_output=True)

def concat_mp3_files(parts, output_path):
    list_path = output_path + ".list.txt"
    with open(list_path, "w", encoding="utf-8") as f:
        for p in parts:
            f.write(f"file '{p}'\n")
    subprocess.run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", list_path,
        "-c:a", "libmp3lame", "-q:a", "2", output_path], capture_output=True)
    os.remove(list_path)

_PHONETIC_MAP = {'a': 'uh'}

def fix_trailing(text):
    words = text.split()
    if not words:
        return text
    last = words[-1].rstrip('.,!?;:')
    if last.lower() in _PHONETIC_MAP:
        punct = words[-1][len(last):]
        words[-1] = _PHONETIC_MAP[last.lower()] + punct
    return ' '.join(words)

def clean(text):
    text = text.replace("\\n", "\n").replace("\n", " ... ")
    text = text.strip()
    if text and all(c in '.,!?;: ' for c in text):
        return ""
    return text

async def gen_segment(text, path, tmp_dir, seg_id):
    cleaned = clean(text)
    if not cleaned or len(cleaned) <= 1:
        return False
    cleaned = fix_trailing(cleaned)
    return await tts_to_file(cleaned, path)

async def main():
    data = json.load(open(os.path.join(ROOT, "data.json"), "r", encoding="utf-8"))
    audio_dir = os.path.join(ROOT, "audio")
    vocab_dir = os.path.join(audio_dir, "vocab")
    os.makedirs(audio_dir, exist_ok=True)
    os.makedirs(vocab_dir, exist_ok=True)
    tmp_dir = os.path.join(audio_dir, "_tmp")
    os.makedirs(tmp_dir, exist_ok=True)

    count = 0

    # === 1. Question audio (q1-q25) ===
    print("=== Question Audio ===")
    silence_path = os.path.join(tmp_dir, "silence_500ms.mp3")
    generate_silence(silence_path)

    for sec in data["sections"]:
        for q in sec.get("questions", []):
            num = q["number"]
            out = os.path.join(audio_dir, f"q{num}.mp3")

            if sec["type"] == "sentence-order":
                words = q.get("words", [])
                order = q.get("correctOrder", [])
                prefix = q.get("framePrefix", "")
                suffix = q.get("frameSuffix", "")
                ordered = [words[i-1] for i in order]
                sentence = f"{prefix} {' '.join(ordered)} {suffix}".strip()
                await tts_to_file(sentence, out)
                count += 1
                print(f"  ✓ q{num}.mp3 (sentence-order)")
            else:
                raw = q["text"]
                choices = q.get("choices", [])
                choice_text = " ... ".join([f"{i+1}. {c}" for i, c in enumerate(choices)])
                has_blank = "(　)" in raw or "(\u3000)" in raw

                if has_blank:
                    raw_norm = raw.replace("(\u3000)", "(　)")
                    parts = raw_norm.split("(　)")
                    seg_files = []
                    for i, part in enumerate(parts):
                        seg_path = os.path.join(tmp_dir, f"q{num}_seg{i}.mp3")
                        ok = await gen_segment(part, seg_path, tmp_dir, f"q{num}_seg{i}")
                        if ok:
                            seg_files.append(seg_path)
                        if i < len(parts) - 1:
                            seg_files.append(silence_path)
                    if choices:
                        cp = os.path.join(tmp_dir, f"q{num}_choices.mp3")
                        await tts_to_file(choice_text, cp)
                        seg_files.append(silence_path)
                        seg_files.append(cp)
                    concat_mp3_files(seg_files, out)
                    for f in seg_files:
                        if f != silence_path and os.path.exists(f):
                            os.remove(f)
                    count += 1
                    print(f"  ✓ q{num}.mp3 (blank pause)")
                else:
                    cleaned = clean(raw)
                    full = f"{cleaned} ... {choice_text}" if choices else cleaned
                    await tts_to_file(full, out)
                    count += 1
                    print(f"  ✓ q{num}.mp3 (no blank)")

    # === 2. Vocabulary audio ===
    print("\n=== Vocabulary Audio ===")
    for v in data.get("vocabulary", []):
        word = v["word"]
        audio_path = os.path.join(ROOT, v["wordAudio"])
        os.makedirs(os.path.dirname(audio_path), exist_ok=True)
        await tts_to_file(word, audio_path)
        count += 1
        print(f"  ✓ {v['wordAudio']}")

    # === 3. FP sourceQuote audio ===
    print("\n=== FP Source Quote Audio ===")
    for fp in data.get("lessonPlan", {}).get("focusPoints", []):
        sq = fp.get("sourceQuote", "")
        sq_audio = fp.get("sourceQuoteAudio", "")
        if sq and sq_audio:
            await tts_to_file(sq, os.path.join(ROOT, sq_audio))
            count += 1
            print(f"  ✓ {sq_audio}")

        # FP example audio
        for j, ex in enumerate(fp.get("examples", [])):
            ex_audio_path = f"audio/ex_{fp['id']}_{j+1}.mp3"
            await tts_to_file(ex["en"], os.path.join(ROOT, ex_audio_path))
            count += 1
            print(f"  ✓ {ex_audio_path}")

    # === 4. Practice Passage LP audio ===
    print("\n=== Practice Passage Audio ===")
    for i, fp in enumerate(data.get("lessonPlan", {}).get("focusPoints", [])):
        pp = fp.get("practicePassage", {})
        if pp and pp.get("en"):
            pp_audio_path = f"audio/practice_pp{i+1}.mp3"
            await tts_to_file(pp["en"], os.path.join(ROOT, pp_audio_path))
            count += 1
            print(f"  ✓ {pp_audio_path}")

    # Cleanup
    shutil.rmtree(tmp_dir, ignore_errors=True)
    print(f"\n=== Total: {count} files generated ===")

asyncio.run(main())

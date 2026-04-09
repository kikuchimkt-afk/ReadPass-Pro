"""
Regenerate ONLY question audio (q1-q25) for ALL grade5 exams,
inserting a 0.5s silence where (　) blank appears.

Strategy:
- Split text at (　), generate each segment via edge-tts, concat with silence
- For segments ending with articles/prepositions (a, an, the, to, etc.):
  Append dummy word "thing" to force correct pronunciation, then trim off
  the dummy word portion using ffmpeg duration subtraction.
- For sentence-order questions (大問3): generate full sentence (no blank).
- For questions without (　) (e.g. 大問2 some): generate normally.

Usage: python _regen_question_audio.py
"""
import json, os, asyncio, re, sys, subprocess, tempfile, shutil
sys.stdout.reconfigure(encoding='utf-8')

try:
    import edge_tts
except ImportError:
    os.system("pip install edge-tts")
    import edge_tts

ROOT = r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade5"
EXAMS = ["2021-1", "2021-2", "2021-3", "2022-1", "2022-2", "2022-3"]
RATE = "-30%"
VOICE = "en-US-JennyNeural"
SILENCE_MS = 500  # 0.5 seconds
DUMMY_WORD = "thing"  # Appended to articles to fix pronunciation

generated = 0

async def tts_to_file(text, path, voice=VOICE, rate=RATE, retries=3):
    """Generate TTS for text and save to path, with retry."""
    for attempt in range(retries):
        try:
            c = edge_tts.Communicate(text, voice, rate=rate)
            await c.save(path)
            return True
        except Exception as e:
            if attempt < retries - 1:
                await asyncio.sleep(2)
            else:
                print(f"    ⚠ TTS failed for: {text[:40]}... -> {e}")
                return False

def generate_silence(path, duration_ms=500):
    subprocess.run([
        "ffmpeg", "-y", "-f", "lavfi", "-i",
        f"anullsrc=r=24000:cl=mono",
        "-t", str(duration_ms / 1000),
        "-c:a", "libmp3lame", "-q:a", "9",
        path
    ], capture_output=True)

def concat_mp3_files(parts, output_path):
    list_path = output_path + ".list.txt"
    with open(list_path, "w", encoding="utf-8") as f:
        for p in parts:
            f.write(f"file '{p}'\n")
    subprocess.run([
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", list_path,
        "-c:a", "libmp3lame", "-q:a", "2",
        output_path
    ], capture_output=True)
    os.remove(list_path)

def get_mp3_duration(path):
    """Get duration of mp3 file in seconds using ffprobe."""
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", path],
        capture_output=True, text=True
    )
    try:
        return float(result.stdout.strip())
    except:
        return 0

def trim_mp3(input_path, output_path, duration):
    """Trim mp3 to specified duration."""
    subprocess.run([
        "ffmpeg", "-y", "-i", input_path,
        "-t", str(duration),
        "-c:a", "libmp3lame", "-q:a", "2", output_path
    ], capture_output=True)

def clean_text_for_tts(text):
    text = text.replace("\\n", "\n").replace("\n", " ... ")
    text = text.strip()
    if text and all(c in '.,!?;: ' for c in text):
        return ""
    return text

# Words that get mispronounced when isolated at the end of a TTS segment
_TRAILING_WORDS = {
    'a', 'an', 'the', 'to', 'or', 'of', 'in', 'on', 'at', 'by',
    'is', 'am', 'are', 'do', 'my', 'no', 'so', 'for', 'his', 'her',
    'its', 'our', 'your', 'be', 'me', 'us', 'we', 'it'
}

def needs_dummy_word(text):
    """Check if cleaned text ends with a word that needs a dummy word appended."""
    words = text.split()
    if not words:
        return False
    last = words[-1].rstrip('.,!?;:')
    return last.lower() in _TRAILING_WORDS

async def generate_segment_audio(text, output_path, tmp_dir, seg_id):
    """Generate TTS for a segment, handling trailing articles with dummy word trick."""
    cleaned = clean_text_for_tts(text)
    if not cleaned or len(cleaned) <= 1:
        return False

    if needs_dummy_word(cleaned):
        # Generate with dummy word to force correct pronunciation
        text_with_dummy = f"{cleaned} {DUMMY_WORD}"
        with_path = os.path.join(tmp_dir, f"{seg_id}_with.mp3")
        dummy_path = os.path.join(tmp_dir, f"{seg_id}_dummy.mp3")

        ok1 = await tts_to_file(text_with_dummy, with_path)
        ok2 = await tts_to_file(DUMMY_WORD, dummy_path)

        if ok1 and ok2:
            dur_with = get_mp3_duration(with_path)
            dur_dummy = get_mp3_duration(dummy_path)
            trim_to = max(0.5, dur_with - dur_dummy * 0.4)  # standalone includes ~60% padding
            trim_mp3(with_path, output_path, trim_to)
            os.remove(with_path)
            os.remove(dummy_path)
            return True
        return False
    else:
        return await tts_to_file(cleaned, output_path)


async def generate_question_audio(q, sec_type, audio_dir, tmp_dir):
    global generated
    num = q["number"]
    output_path = os.path.join(audio_dir, f"q{num}.mp3")

    if sec_type == "sentence-order":
        words = q.get("words", [])
        order = q.get("correctOrder", [])
        prefix = q.get("framePrefix", "")
        suffix = q.get("frameSuffix", "")
        ordered = [words[i-1] for i in order]
        sentence = f"{prefix} {' '.join(ordered)} {suffix}".strip()
        await tts_to_file(sentence, output_path)
        generated += 1
        print(f"  ✓ q{num}.mp3 (sentence-order)")
        return

    raw = q["text"]
    choices = q.get("choices", [])
    choice_text = " ... ".join([f"{i+1}. {c}" for i, c in enumerate(choices)])

    has_blank = "(　)" in raw or "(\u3000)" in raw

    if has_blank:
        raw_norm = raw.replace("(\u3000)", "(　)")
        parts = raw_norm.split("(　)")

        seg_files = []
        silence_path = os.path.join(tmp_dir, "silence_500ms.mp3")
        if not os.path.exists(silence_path):
            generate_silence(silence_path, SILENCE_MS)

        for i, part in enumerate(parts):
            seg_path = os.path.join(tmp_dir, f"q{num}_seg{i}.mp3")
            ok = await generate_segment_audio(part, seg_path, tmp_dir, f"q{num}_seg{i}")
            if ok:
                seg_files.append(seg_path)
            if i < len(parts) - 1:
                seg_files.append(silence_path)

        if choices:
            choice_seg_path = os.path.join(tmp_dir, f"q{num}_choices.mp3")
            await tts_to_file(choice_text, choice_seg_path)
            seg_files.append(silence_path)
            seg_files.append(choice_seg_path)

        concat_mp3_files(seg_files, output_path)

        for f in seg_files:
            if f != silence_path and os.path.exists(f):
                os.remove(f)

        generated += 1
        print(f"  ✓ q{num}.mp3 (split+trim pause)")

    else:
        cleaned = clean_text_for_tts(raw)
        full_text = f"{cleaned} ... {choice_text}" if choices else cleaned
        await tts_to_file(full_text, output_path)
        generated += 1
        print(f"  ✓ q{num}.mp3 (no blank)")


async def main():
    global generated

    for exam in EXAMS:
        exam_dir = os.path.join(ROOT, exam)
        data_path = os.path.join(exam_dir, "data.json")
        if not os.path.exists(data_path):
            print(f"SKIP: {exam} (no data.json)")
            continue

        audio_dir = os.path.join(exam_dir, "audio")
        os.makedirs(audio_dir, exist_ok=True)

        data = json.load(open(data_path, "r", encoding="utf-8"))
        tmp_dir = os.path.join(audio_dir, "_tmp")
        os.makedirs(tmp_dir, exist_ok=True)

        print(f"\n=== {exam} ===")
        exam_gen = 0

        for sec in data["sections"]:
            for q in sec.get("questions", []):
                existing = os.path.join(audio_dir, f"q{q['number']}.mp3")
                if os.path.exists(existing):
                    os.remove(existing)
                await generate_question_audio(q, sec["type"], audio_dir, tmp_dir)
                exam_gen += 1

        shutil.rmtree(tmp_dir, ignore_errors=True)
        print(f"  Generated {exam_gen} question audio files for {exam}")

    print(f"\n=== Grand Total ===")
    print(f"Generated: {generated}")

asyncio.run(main())

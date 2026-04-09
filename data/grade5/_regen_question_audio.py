"""
Regenerate ONLY question audio (q1-q25) for ALL grade5 exams,
inserting a 0.5s silence where (　) blank appears.

Strategy:
- For questions with (　): split text at (　), generate each segment,
  then concat with 0.5s silence via ffmpeg.
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

generated = 0
skipped = 0

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
    """Generate a silence mp3 file of given duration using ffmpeg."""
    subprocess.run([
        "ffmpeg", "-y", "-f", "lavfi", "-i",
        f"anullsrc=r=24000:cl=mono",
        "-t", str(duration_ms / 1000),
        "-c:a", "libmp3lame", "-q:a", "9",
        path
    ], capture_output=True)

def concat_mp3_files(parts, output_path):
    """Concatenate a list of mp3 files using ffmpeg concat demuxer."""
    # Create a temp file list
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

def clean_text_for_tts(text):
    """Clean text for TTS: remove line breaks, normalize."""
    text = text.replace("\\n", "\n").replace("\n", " ... ")
    # Remove trailing/leading punctuation-only remnants
    text = text.strip()
    # If only punctuation remains, return empty
    if text and all(c in '.,!?;: ' for c in text):
        return ""
    return text

# Words that get mispronounced when isolated at the end of a TTS segment
_TRAILING_WORDS = {
    'a', 'an', 'the', 'to', 'or', 'of', 'in', 'on', 'at', 'by',
    'is', 'am', 'are', 'do', 'my', 'no', 'so', 'for', 'his', 'her',
    'its', 'our', 'your', 'be', 'me', 'us', 'we', 'it'
}

def fix_segment_boundaries(parts):
    """Fix segments ending with short articles/prepositions that TTS mispronounces.
    Instead of moving words, append '...' so TTS reads them as mid-sentence
    (e.g. 'a' reads as article 'ア' not letter 'エイ').
    e.g. ['She goes to a', 'with her mom'] -> ['She goes to a...', 'with her mom']
    """
    fixed = list(parts)
    for i in range(len(fixed) - 1):
        seg = fixed[i].strip()
        if not seg:
            continue
        words = seg.split()
        if not words:
            continue
        last = words[-1].rstrip('.,!?;:')
        if last.lower() in _TRAILING_WORDS:
            # Append ellipsis so TTS treats this as mid-sentence trailing off
            fixed[i] = seg + '...'
    return fixed

async def generate_question_audio(q, sec_type, audio_dir, tmp_dir):
    """Generate audio for a single question."""
    global generated
    num = q["number"]
    output_path = os.path.join(audio_dir, f"q{num}.mp3")

    if sec_type == "sentence-order":
        # Read the completed sentence (no blank)
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

    # Check if question has a blank (　)
    has_blank = "(　)" in raw or "(\u3000)" in raw

    if has_blank:
        # Split at blank
        # Normalize blank marker
        raw_norm = raw.replace("(\u3000)", "(　)")
        parts = raw_norm.split("(　)")

        # Fix trailing articles/prepositions
        parts = fix_segment_boundaries(parts)

        # Generate each text segment and silence
        seg_files = []
        silence_path = os.path.join(tmp_dir, "silence_500ms.mp3")
        if not os.path.exists(silence_path):
            generate_silence(silence_path, SILENCE_MS)

        for i, part in enumerate(parts):
            cleaned = clean_text_for_tts(part)
            if cleaned and len(cleaned) > 1:
                seg_path = os.path.join(tmp_dir, f"q{num}_seg{i}.mp3")
                ok = await tts_to_file(cleaned, seg_path)
                if not ok:
                    continue
                seg_files.append(seg_path)
            # Add silence between segments (not after the last part)
            if i < len(parts) - 1:
                seg_files.append(silence_path)

        # Add choices after a pause
        if choices:
            choice_seg_path = os.path.join(tmp_dir, f"q{num}_choices.mp3")
            await tts_to_file(choice_text, choice_seg_path)
            seg_files.append(silence_path)
            seg_files.append(choice_seg_path)

        # Concatenate all segments
        concat_mp3_files(seg_files, output_path)

        # Cleanup temp segments (but keep silence for reuse)
        for f in seg_files:
            if f != silence_path and os.path.exists(f):
                os.remove(f)

        generated += 1
        print(f"  ✓ q{num}.mp3 (with 0.5s blank pause)")

    else:
        # No blank - straightforward generation
        cleaned = clean_text_for_tts(raw)
        full_text = f"{cleaned} ... {choice_text}" if choices else cleaned
        await tts_to_file(full_text, output_path)
        generated += 1
        print(f"  ✓ q{num}.mp3 (no blank)")


async def main():
    global generated, skipped

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
                # Delete existing file to force regeneration
                existing = os.path.join(audio_dir, f"q{q['number']}.mp3")
                if os.path.exists(existing):
                    os.remove(existing)
                await generate_question_audio(q, sec["type"], audio_dir, tmp_dir)
                exam_gen += 1

        # Clean up tmp dir
        shutil.rmtree(tmp_dir, ignore_errors=True)
        print(f"  Generated {exam_gen} question audio files for {exam}")

    print(f"\n=== Grand Total ===")
    print(f"Generated: {generated}")

asyncio.run(main())

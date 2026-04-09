#!/usr/bin/env python3
"""Generate TTS audio for Grade 5 - 2024-1"""
import json, os, sys, asyncio, re, subprocess
sys.stdout.reconfigure(encoding='utf-8')

import edge_tts

ROOT = os.path.dirname(__file__)
DATA = json.load(open(os.path.join(ROOT, "data.json"), 'r', encoding='utf-8'))
AUDIO_DIR = os.path.join(ROOT, "audio")
VOCAB_DIR = os.path.join(AUDIO_DIR, "vocab")
os.makedirs(VOCAB_DIR, exist_ok=True)

RATE = "-30%"
VOICE = "en-US-JennyNeural"

def clean_text(text):
    text = re.sub(r'[（）\(　\)]', ' ', text)
    text = re.sub(r'[\u3000-\u9fff\uff00-\uffef]+', '', text)
    text = re.sub(r'\\n', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    # Fix 'a' article pronunciation
    text = re.sub(r'\ba\b(?=\s+[bcdfghjklmnpqrstvwxyz])', 'uh', text)
    return text

async def gen(text, path):
    if os.path.exists(path):
        return False
    cleaned = clean_text(text)
    if not cleaned or len(cleaned) < 2:
        return False
    try:
        comm = edge_tts.Communicate(cleaned, VOICE, rate=RATE)
        await comm.save(path)
        return True
    except Exception as e:
        print(f"  ERR: {e}")
        return False

async def main():
    count = 0
    
    # 1. Question audio (q1-q25)
    for sec in DATA['sections']:
        for q in sec['questions']:
            audio = q.get('questionAudio', '')
            if audio:
                path = os.path.join(ROOT, audio)
                text = q['text']
                if sec['type'] == 'sentence-order':
                    # For sentence-order, read the full sentence
                    words = q.get('words', [])
                    order = q.get('correctOrder', [])
                    prefix = q.get('framePrefix', '')
                    suffix = q.get('frameSuffix', '')
                    ordered = [words[i-1] for i in order]
                    text = f"{prefix} {' '.join(ordered)} {suffix}".strip()
                if await gen(text, path):
                    count += 1
                    print(f"  ✓ {audio}")
    
    # 2. Vocabulary audio
    for v in DATA['vocabulary']:
        audio = v.get('wordAudio', '')
        if audio:
            path = os.path.join(ROOT, audio)
            if await gen(v['word'], path):
                count += 1
                print(f"  ✓ {audio}")
    
    # 3. FP examples, sourceQuote, practice passages, challenges
    for fp in DATA['lessonPlan']['focusPoints']:
        # Source quote
        sq = fp.get('sourceQuoteAudio', '')
        if sq:
            path = os.path.join(ROOT, sq)
            if await gen(fp.get('sourceQuote', ''), path):
                count += 1
                print(f"  ✓ {sq}")
        
        # Examples
        for ex in fp.get('examples', []):
            audio = ex.get('audio', '')
            if audio:
                path = os.path.join(ROOT, audio)
                if await gen(ex['en'], path):
                    count += 1
                    print(f"  ✓ {audio}")
        
        # Practice passage
        pp = fp.get('practicePassage')
        if pp and pp.get('audioFile'):
            audio = pp['audioFile']
            path = os.path.join(ROOT, audio)
            if await gen(pp['en'], path):
                count += 1
                print(f"  ✓ {audio}")
        
        # Challenge questions
        for pqs_key in ['practiceQuestions', 'practiceQuestionsSimple']:
            for q in fp.get(pqs_key, []):
                audio = q.get('audio', '')
                if audio:
                    path = os.path.join(ROOT, audio)
                    ans = q.get('a', '')
                    if await gen(ans, path):
                        count += 1
                        print(f"  ✓ {audio}")
    
    print(f"\n=== Generated {count} audio files ===")

asyncio.run(main())

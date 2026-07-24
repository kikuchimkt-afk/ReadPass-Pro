# -*- coding: utf-8 -*-
"""英検4級 音声生成（EdgeTTS）。他回(2025-1)と同じ命名・内容規則。
   - 問題音声: 大問1-3 のみ（大問4は音声なし）
   - 並べかえは正しい語順の英文を読み上げ
   - 語彙 / FP例文 / 練習パッセージ / 出典 / challenge(設問内の英語フレーズ)
"""
import asyncio, json, os, re, sys
import edge_tts

sys.stdout.reconfigure(encoding="utf-8")
VOICE = "en-US-JennyNeural"
VOICE_JA = "ja-JP-NanamiNeural"
RATE = "-15%"
BASE = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(BASE, "data.json")
d = json.load(open(data_path, encoding="utf-8"))
os.makedirs(os.path.join(BASE, "audio"), exist_ok=True)


def pick_voice(text):
    # 英字を含めば英語音声、なければ日本語音声で読み上げる
    return VOICE if re.search(r"[A-Za-z]", text) else VOICE_JA


async def gen(text, out):
    await edge_tts.Communicate(text, pick_voice(text), rate=RATE).save(out)


def needs(out):
    return not os.path.exists(out) or os.path.getsize(out) < 500


def out_of(rel):
    p = os.path.join(BASE, rel.replace("/", os.sep))
    os.makedirs(os.path.dirname(p), exist_ok=True)
    return p


def sentence_order_text(q):
    ordered = [q["words"][i - 1] for i in q["correctOrder"]]
    parts = []
    if q.get("framePrefix", "").strip():
        parts.append(q["framePrefix"].strip())
    parts += ordered
    if q.get("frameSuffix", "").strip():
        parts.append(q["frameSuffix"].strip())
    return " ".join(parts)


def question_text(q, sec_type):
    if sec_type == "sentence-order":
        return sentence_order_text(q)
    raw = (q.get("text") or q.get("question") or "").replace("(\u3000)", " blank ").replace("\u3000", " blank ")
    raw = raw.replace("\n", " ... ").strip()
    ch = q.get("choices", [])
    if ch:
        opts = " ... ".join(f"{i + 1}. {c}" for i, c in enumerate(ch))
        return f"{raw} ... {opts}"
    return raw


def jp_bracket_en(text):
    m = re.search(r"\u300c(.+?)\u300d", text)
    return m.group(1) if m else text

n = 0
# 問題音声（questionAudio が付いている設問のみ = 大問1-3）
for sec in d["sections"]:
    for q in sec.get("questions", []):
        qa = q.get("questionAudio")
        if not qa:
            continue
        o = out_of(qa)
        if needs(o):
            asyncio.run(gen(question_text(q, sec["type"]), o)); n += 1
            print("q:", qa, flush=True)

# 語彙
for v in d["vocabulary"]:
    wa = v.get("wordAudio")
    if wa:
        o = out_of(wa)
        if needs(o):
            asyncio.run(gen(v["word"], o)); n += 1
            print("w:", wa, flush=True)

# FP: 例文 / 練習パッセージ / 出典 / challenge
for fp in d["lessonPlan"]["focusPoints"]:
    for ex in fp.get("examples", []):
        a = ex.get("audio")
        if a:
            o = out_of(a)
            if needs(o):
                asyncio.run(gen(ex["en"], o)); n += 1
                print("ex:", a, flush=True)
    pp = fp.get("practicePassage", {})
    af = pp.get("audioFile")
    if af:
        o = out_of(af)
        if needs(o):
            en = re.sub(r"\[\u51fa\u5178:.*?\]\n?", "", pp.get("en", "")).strip()
            asyncio.run(gen(en, o)); n += 1
            print("pp:", af, flush=True)
    sqa = fp.get("sourceQuoteAudio")
    if sqa:
        o = out_of(sqa)
        if needs(o):
            asyncio.run(gen(fp.get("sourceQuote", ""), o)); n += 1
            print("sq:", sqa, flush=True)
    for pq in fp.get("practiceQuestions", []):
        a = pq.get("audio")
        if a:
            o = out_of(a)
            if needs(o):
                asyncio.run(gen(jp_bracket_en(pq.get("q", "")), o)); n += 1
                print("ch:", a, flush=True)

print(f"\nDone: {n} files generated")

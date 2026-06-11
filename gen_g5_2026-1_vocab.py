# -*- coding: utf-8 -*-
"""
2026年度 第1回（土曜準会場）英検5級 data.json
vocabulary（単語カード・単語クイズ）20語
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade5", "2026-1-sat",
)
OUT = os.path.join(BASE, "data.json")

with open(OUT, encoding="utf-8") as f:
    data = json.load(f)

vocab = []

# ============================================================
# 大問1 正答語（15語）
# ============================================================

vocab.append({
    "word": "think",
    "meaning": "思う",
    "pos": "動詞",
    "level": "5級",
    "example": "I think so, too.",
    "distractors": ["話す", "住む", "歌う"],
})
vocab.append({
    "word": "doctor",
    "meaning": "医者",
    "pos": "名詞",
    "level": "5級",
    "example": "Dan's mother is a doctor. She works at the hospital.",
    "distractors": ["選手", "王", "農夫"],
})
vocab.append({
    "word": "locker",
    "meaning": "ロッカー",
    "pos": "名詞",
    "level": "5級",
    "example": "I put my books in my locker before I go to class.",
    "distractors": ["飲み物", "辞書", "箸"],
})
vocab.append({
    "word": "cute",
    "meaning": "かわいい",
    "pos": "形容詞",
    "level": "5級",
    "example": "Your sister's dress is very cute.",
    "distractors": ["雨の", "背が高い", "速い"],
})
vocab.append({
    "word": "vacation",
    "meaning": "休暇",
    "pos": "名詞",
    "level": "5級",
    "example": "When does your summer vacation start?",
    "distractors": ["新聞", "歌", "キャンディ"],
})
vocab.append({
    "word": "basketball",
    "meaning": "バスケットボール",
    "pos": "名詞",
    "level": "5級",
    "example": "I play basketball after school.",
    "distractors": ["自転車", "本", "いちご"],
})
vocab.append({
    "word": "different",
    "meaning": "違う",
    "pos": "形容詞",
    "level": "5級",
    "example": "Tonight he is watching a different TV show.",
    "distractors": ["同じ", "高い", "若い"],
})
vocab.append({
    "word": "to",
    "meaning": "〜に（方向）",
    "pos": "前置詞",
    "level": "5級",
    "example": "Can you come to my house at three this afternoon?",
    "distractors": ["〜の", "〜のために", "〜の外へ"],
})
vocab.append({
    "word": "night",
    "meaning": "夜",
    "pos": "名詞",
    "level": "5級",
    "example": "Do you wash the dishes every night?",
    "distractors": ["カップ", "手", "硬貨"],
})
vocab.append({
    "word": "glass",
    "meaning": "コップ（1杯）",
    "pos": "名詞",
    "level": "5級",
    "example": "Can I have a glass of apple juice?",
    "distractors": ["皿", "ナイフ", "フォーク"],
})
vocab.append({
    "word": "much",
    "meaning": "いくら（How much）",
    "pos": "副詞",
    "level": "5級",
    "example": "How much is it? It's only $5.",
    "distractors": ["背が低い", "若い", "悲しい"],
})
vocab.append({
    "word": "from",
    "meaning": "〜出身",
    "pos": "前置詞",
    "level": "5級",
    "example": "Jenny is from France.",
    "distractors": ["〜の中に", "〜の", "〜に（時刻）"],
})
vocab.append({
    "word": "Me",
    "meaning": "私（Me, too.）",
    "pos": "代名詞",
    "level": "5級",
    "example": "I like this movie. Me, too.",
    "distractors": ["彼", "彼ら", "私たち"],
})
vocab.append({
    "word": "be",
    "meaning": "〜でありなさい（命令）",
    "pos": "動詞",
    "level": "5級",
    "example": "Alice, be quiet!",
    "distractors": ["〜である（am）", "〜である（are）", "〜である（is）"],
})
vocab.append({
    "word": "Whose",
    "meaning": "誰の",
    "pos": "疑問詞",
    "level": "5級",
    "example": "Whose phone is this? It's Bill's.",
    "distractors": ["いつ", "どこ", "どう"],
})

# ============================================================
# 大問3 並べ替えのキーワード（5語）
# ============================================================

vocab.append({
    "word": "sister",
    "meaning": "姉・妹",
    "pos": "名詞",
    "level": "5級",
    "source": "大問3",
    "example": "My sister washes the dishes every day.",
    "distractors": ["お皿", "洗う", "毎日"],
})
vocab.append({
    "word": "skiing",
    "meaning": "スキー",
    "pos": "名詞",
    "level": "5級",
    "source": "大問3",
    "example": "Bill and I go skiing in winter.",
    "distractors": ["行く", "そして", "冬"],
})
vocab.append({
    "word": "umbrella",
    "meaning": "かさ",
    "pos": "名詞",
    "level": "5級",
    "source": "大問3",
    "example": "Take your umbrella to school.",
    "distractors": ["学校", "持って行く", "〜へ"],
})
vocab.append({
    "word": "soccer team",
    "meaning": "サッカーチーム",
    "pos": "名詞",
    "level": "5級",
    "source": "大問3",
    "example": "Mike's soccer team has three coaches.",
    "distractors": ["コーチ", "3人", "持つ"],
})
vocab.append({
    "word": "school",
    "meaning": "学校",
    "pos": "名詞",
    "level": "5級",
    "source": "大問3",
    "example": "We don't have school today.",
    "distractors": ["持つ", "しない", "今日"],
})

assert len(vocab) == 20, f"Expected 20 words, got {len(vocab)}"

old_vocab = {v["word"]: v for v in data.get("vocabulary", [])}
for v in vocab:
    ov = old_vocab.get(v["word"], {})
    for key in ("wordAudio", "exampleAudio"):
        if ov.get(key):
            v[key] = ov[key]

data["vocabulary"] = vocab

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Wrote {len(vocab)} vocabulary items to {OUT}")

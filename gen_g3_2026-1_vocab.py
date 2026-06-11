# -*- coding: utf-8 -*-
"""
2026年度 第1回（土曜準会場）英検3級 data.json
vocabulary（単語カード・単語クイズ）30語
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade3", "2026-1-sat",
)
OUT = os.path.join(BASE, "data.json")

with open(OUT, encoding="utf-8") as f:
    data = json.load(f)

vocab = []

# ============================================================
# 大問1 正答語（15語）
# ============================================================

vocab.append({
    "word": "kite",
    "meaning": "たこ",
    "pos": "名詞",
    "level": "3級",
    "example": "I'm going to the park to fly my kite.",
    "distractors": ["市場", "渡す", "疲れた"],
})
vocab.append({
    "word": "pass",
    "meaning": "渡す",
    "pos": "動詞",
    "level": "3級",
    "example": "Can you pass me the ball, please?",
    "distractors": ["たこ", "退屈な", "運動する"],
})
vocab.append({
    "word": "boring",
    "meaning": "退屈な",
    "pos": "形容詞",
    "level": "3級",
    "example": "The movie was very boring. Lucy fell asleep in the theater.",
    "distractors": ["疲れた", "市場", "感じる"],
})
vocab.append({
    "word": "tired",
    "meaning": "疲れた",
    "pos": "形容詞",
    "level": "3級",
    "example": "Yoko is tired today. She studied English for five hours yesterday.",
    "distractors": ["退屈な", "大学", "描かれた"],
})
vocab.append({
    "word": "exercise",
    "meaning": "運動する",
    "pos": "動詞",
    "level": "3級",
    "example": "My coach says I need to exercise for three hours every day.",
    "distractors": ["渡す", "教えた", "腹痛"],
})
vocab.append({
    "word": "market",
    "meaning": "市場",
    "pos": "名詞",
    "level": "3級",
    "example": "Jim saw some people buying fresh fish and meat at the market.",
    "distractors": ["たこ", "彼自身で", "公演"],
})
vocab.append({
    "word": "college",
    "meaning": "大学・専門学校",
    "pos": "名詞",
    "level": "3級",
    "example": "Meg is a student at a large college. She is studying to be a nurse.",
    "distractors": ["市場", "野菜", "選手"],
})
vocab.append({
    "word": "take care of",
    "meaning": "世話をする",
    "pos": "句動詞",
    "level": "3級",
    "example": "I always take care of my little sister when my mother is out.",
    "distractors": ["〜を待つ", "着る", "屋内で"],
})
vocab.append({
    "word": "himself",
    "meaning": "彼自身で",
    "pos": "代名詞",
    "level": "3級",
    "example": "No, he did it all by himself.",
    "distractors": ["感じる", "材料", "コメディ"],
})
vocab.append({
    "word": "wait for",
    "meaning": "〜を待つ",
    "pos": "句動詞",
    "level": "3級",
    "example": "We'll have to wait for 30 minutes until the next train comes.",
    "distractors": ["世話をする", "練習するために", "選手権大会"],
})
vocab.append({
    "word": "feel",
    "meaning": "感じる",
    "pos": "動詞",
    "level": "3級",
    "example": "I feel much better this morning. I slept really well last night.",
    "distractors": ["描かれた", "手伝う", "緊張した"],
})
vocab.append({
    "word": "look around",
    "meaning": "あちこちを見て回る",
    "pos": "句動詞",
    "level": "3級",
    "example": "They looked around downtown, but everything was too small.",
    "distractors": ["〜を待つ", "ウェブサイト", "アイススケート"],
})
vocab.append({
    "word": "painted",
    "meaning": "描かれた",
    "pos": "動詞",
    "level": "3級",
    "example": "Some of the art in this airport was painted by a famous artist.",
    "distractors": ["教えた", "公演", "渡す"],
})
vocab.append({
    "word": "taught",
    "meaning": "教えた",
    "pos": "動詞",
    "level": "3級",
    "example": "Dr. Kobayashi taught at a university for many years.",
    "distractors": ["練習した", "疲れた", "〜にあいさつを伝える"],
})
vocab.append({
    "word": "to practice",
    "meaning": "練習するために",
    "pos": "不定詞",
    "level": "3級",
    "example": "I'm going to the park to practice basketball.",
    "distractors": ["運動する", "着る", "選手"],
})

# ============================================================
# 大問2 会話のキーフレーズ（5語）
# ============================================================

vocab.append({
    "word": "help",
    "meaning": "手伝う",
    "pos": "動詞",
    "level": "3級",
    "example": "I'll help you soon. This TV show will finish in 10 minutes.",
    "distractors": ["感じる", "市場", "コメディ"],
})
vocab.append({
    "word": "ice-skating",
    "meaning": "アイススケート",
    "pos": "名詞",
    "level": "3級",
    "example": "I want to go ice-skating with my friends.",
    "distractors": ["公演", "たこ", "腹痛"],
})
vocab.append({
    "word": "wear",
    "meaning": "着る",
    "pos": "動詞",
    "level": "3級",
    "example": "I'm going to wear it today. I have practice at three.",
    "distractors": ["世話をする", "教えた", "屋内で"],
})
vocab.append({
    "word": "stomachache",
    "meaning": "腹痛",
    "pos": "名詞",
    "level": "3級",
    "example": "I can't go to baseball practice today. I have a stomachache.",
    "distractors": ["疲れた", "選手権大会", "野菜"],
})
vocab.append({
    "word": "say hello to",
    "meaning": "〜にあいさつを伝える",
    "pos": "句動詞",
    "level": "3級",
    "example": "Say hello to him for me.",
    "distractors": ["〜を待つ", "練習するために", "ウェブサイト"],
})

# ============================================================
# 大問3A 料理教室（3語）
# ============================================================

vocab.append({
    "word": "ingredients",
    "meaning": "材料",
    "pos": "名詞",
    "level": "3級",
    "example": "We will prepare all of the ingredients.",
    "distractors": ["野菜", "公演", "彼自身で"],
})
vocab.append({
    "word": "vegetables",
    "meaning": "野菜",
    "pos": "名詞",
    "level": "3級",
    "example": "You can learn how to make delicious meals using vegetables from our farm.",
    "distractors": ["材料", "選手", "退屈な"],
})
vocab.append({
    "word": "website",
    "meaning": "ウェブサイト",
    "pos": "名詞",
    "level": "3級",
    "example": "For more information about our vegetables, please check our website.",
    "distractors": ["市場", "コメディ", "手伝う"],
})

# ============================================================
# 大問3B ドラマ部（4語）
# ============================================================

vocab.append({
    "word": "performance",
    "meaning": "公演",
    "pos": "名詞",
    "level": "3級",
    "example": "I wanted to remind you about my drama club performance next week.",
    "distractors": ["練習した", "アイススケート", "大学"],
})
vocab.append({
    "word": "practiced",
    "meaning": "練習した",
    "pos": "動詞",
    "level": "3級",
    "example": "The drama club practiced a lot, and now the play is finally ready.",
    "distractors": ["教えた", "公演", "着る"],
})
vocab.append({
    "word": "nervous",
    "meaning": "緊張した",
    "pos": "形容詞",
    "level": "3級",
    "example": "I'm still a little nervous, but it will be fine.",
    "distractors": ["退屈な", "疲れた", "描かれた"],
})
vocab.append({
    "word": "comedy",
    "meaning": "コメディ",
    "pos": "名詞",
    "level": "3級",
    "example": "Is it a comedy? I like comedy plays the best!",
    "distractors": ["公演", "選手権大会", "たこ"],
})

# ============================================================
# 大問3C 卓球（3語）
# ============================================================

vocab.append({
    "word": "indoors",
    "meaning": "屋内で",
    "pos": "副詞",
    "level": "3級",
    "example": "It was a fun way to stay active indoors.",
    "distractors": ["あちこちを見て回る", "世話をする", "渡す"],
})
vocab.append({
    "word": "championships",
    "meaning": "選手権大会",
    "pos": "名詞",
    "level": "3級",
    "example": "In 1926, the first world championships for table tennis were held.",
    "distractors": ["公演", "市場", "腹痛"],
})
vocab.append({
    "word": "athlete",
    "meaning": "選手",
    "pos": "名詞",
    "level": "3級",
    "example": "An American athlete missed his bus and got on the Chinese team's bus instead.",
    "distractors": ["大学", "材料", "感じる"],
})

assert len(vocab) == 30, f"Expected 30 words, got {len(vocab)}"

data["vocabulary"] = vocab

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Wrote {len(vocab)} vocabulary items to {OUT}")

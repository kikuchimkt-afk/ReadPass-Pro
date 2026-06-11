# -*- coding: utf-8 -*-
"""2026年度 第1回（本会場）英検5級 vocabulary 20語"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade5", "2026-1",
)
OUT = os.path.join(BASE, "data.json")

with open(OUT, encoding="utf-8") as f:
    data = json.load(f)

vocab = [
    {"word": "newspaper", "meaning": "新聞", "pos": "名詞", "level": "5級",
     "example": "I read a newspaper every day.", "distractors": ["音楽", "絵の具", "昼食"]},
    {"word": "people", "meaning": "人々", "pos": "名詞", "level": "5級",
     "example": "Many people are waiting for the new pink train.", "distractors": ["本", "歯", "果物"]},
    {"word": "racket", "meaning": "ラケット", "pos": "名詞", "level": "5級",
     "example": "Where is your tennis racket? It's in my bag.", "distractors": ["フォーク", "辞書", "たこ"]},
    {"word": "drink", "meaning": "飲む", "pos": "動詞", "level": "5級",
     "example": "Please drink your coffee before you go to school.", "distractors": ["眠る", "着く", "話す"]},
    {"word": "mountain", "meaning": "山", "pos": "名詞", "level": "5級",
     "example": "He goes to the mountain near his house every winter.", "distractors": ["プール", "駅", "図書館"]},
    {"word": "tall", "meaning": "高い", "pos": "形容詞", "level": "5級",
     "example": "How tall is that building? It's 200 meters.", "distractors": ["速い", "寒い", "若い"]},
    {"word": "leave", "meaning": "帰る・去る", "pos": "動詞", "level": "5級",
     "example": "Can I go home now? Yes, you can leave now.", "distractors": ["知る", "取る", "食べる"]},
    {"word": "see", "meaning": "わかる（I see.）", "pos": "動詞", "level": "5級",
     "example": "I can't go to the movie today. Oh, I see.", "distractors": ["見る", "遊ぶ", "立つ"]},
    {"word": "at", "meaning": "〜で（at home）", "pos": "前置詞", "level": "5級",
     "example": "Do you often eat fruit at home?", "distractors": ["〜の下で", "〜と一緒に", "〜について"]},
    {"word": "go", "meaning": "行く", "pos": "動詞", "level": "5級",
     "example": "Can we go hiking tomorrow?", "distractors": ["欲しい", "閉める", "遊ぶ"]},
    {"word": "after", "meaning": "〜の後", "pos": "前置詞", "level": "5級",
     "example": "Taro goes to the swimming pool after school.", "distractors": ["〜について", "下へ", "〜の上に"]},
    {"word": "wake", "meaning": "起きる", "pos": "動詞", "level": "5級",
     "example": "I wake up at seven every morning.", "distractors": ["歌う", "話す", "閉める"]},
    {"word": "his", "meaning": "彼の", "pos": "代名詞", "level": "5級",
     "example": "We like his class very much.", "distractors": ["彼（主格）", "彼（目的格）", "私たちの"]},
    {"word": "mine", "meaning": "私のもの", "pos": "代名詞", "level": "5級",
     "example": "Can I use yours? Yes, you can use mine.", "distractors": ["私（主格）", "私の", "私を"]},
    {"word": "study", "meaning": "勉強する", "pos": "動詞", "level": "5級",
     "example": "Yes, he is studying there.", "distractors": ["教える", "読む", "書く"]},
    {"word": "English", "meaning": "英語", "pos": "名詞", "level": "5級", "source": "大問3",
     "example": "When is your English test?", "distractors": ["いつ", "あなたの", "ですか"]},
    {"word": "time", "meaning": "時間・時刻", "pos": "名詞", "level": "5級", "source": "大問3",
     "example": "What time is it in London?", "distractors": ["〜で", "です", "それ"]},
    {"word": "homeroom", "meaning": "ホームルーム（学級）", "pos": "名詞", "level": "5級", "source": "大問3",
     "example": "Our homeroom teacher is Mr. Endo.", "distractors": ["私たちの", "先生", "です"]},
    {"word": "pizza", "meaning": "ピザ", "pos": "名詞", "level": "5級", "source": "大問3",
     "example": "Kazuki wants some pizza for dinner.", "distractors": ["欲しい", "夕食に", "一樹"]},
    {"word": "lunch", "meaning": "昼食", "pos": "名詞", "level": "5級", "source": "大問3",
     "example": "What are you making for lunch?", "distractors": ["何", "作る", "あなたは"]},
]

assert len(vocab) == 20

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

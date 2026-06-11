# -*- coding: utf-8 -*-
"""
2026年度 第1回（土曜準会場）英検4級 data.json
vocabulary（単語カード・単語クイズ）30語
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade4", "2026-1-sat",
)
OUT = os.path.join(BASE, "data.json")

with open(OUT, encoding="utf-8") as f:
    data = json.load(f)

vocab = []

# ============================================================
# 大問1 正答語（15語）
# ============================================================

vocab.append({
    "word": "building",
    "meaning": "建物",
    "pos": "名詞",
    "level": "4級",
    "example": "What is that tall building? It's a new school.",
    "distractors": ["硬貨", "単語", "メートル"],
})
vocab.append({
    "word": "wash",
    "meaning": "洗う",
    "pos": "動詞",
    "level": "4級",
    "example": "Do you wash your hands before you eat?",
    "distractors": ["読む", "飲む", "持ってくる"],
})
vocab.append({
    "word": "long",
    "meaning": "長い",
    "pos": "形容詞",
    "level": "4級",
    "example": "The pool is fifteen meters long.",
    "distractors": ["高い", "うるさい", "乾いた"],
})
vocab.append({
    "word": "lake",
    "meaning": "湖",
    "pos": "名詞",
    "level": "4級",
    "example": "I saw a big fish in the lake.",
    "distractors": ["駅", "帽子", "サンドイッチ"],
})
vocab.append({
    "word": "invited",
    "meaning": "招待した",
    "pos": "動詞",
    "level": "4級",
    "example": "She invited all her friends to her house.",
    "distractors": ["見た", "決めた", "望んだ"],
})
vocab.append({
    "word": "news",
    "meaning": "ニュース",
    "pos": "名詞",
    "level": "4級",
    "example": "Lucas watches the news on TV every morning.",
    "distractors": ["夜", "壁", "名前"],
})
vocab.append({
    "word": "cousins",
    "meaning": "いとこ",
    "pos": "名詞",
    "level": "4級",
    "example": "I have six cousins. We're all going to the beach.",
    "distractors": ["歯", "シャツ", "葉"],
})
vocab.append({
    "word": "at",
    "meaning": "〜に（場所）",
    "pos": "前置詞",
    "level": "4級",
    "example": "We'll stay at my friend's place.",
    "distractors": ["〜として", "〜へ", "〜の上に"],
})
vocab.append({
    "word": "wakes",
    "meaning": "起きる",
    "pos": "動詞",
    "level": "4級",
    "example": "Kyoko always wakes up early in the morning.",
    "distractors": ["捕まえる", "忘れる", "保つ"],
})
vocab.append({
    "word": "minute",
    "meaning": "分（時間）",
    "pos": "名詞",
    "level": "4級",
    "example": "Wait a minute. I forgot our baseball caps.",
    "distractors": ["数字", "理由", "人"],
})
vocab.append({
    "word": "in",
    "meaning": "〜で（寝ている）",
    "pos": "前置詞",
    "level": "4級",
    "example": "She's still sick in bed, but she's better.",
    "distractors": ["〜の下で", "〜と一緒に", "〜に（時刻）"],
})
vocab.append({
    "word": "to",
    "meaning": "〜に（be kind to）",
    "pos": "前置詞",
    "level": "4級",
    "example": "Be kind to your brother.",
    "distractors": ["〜の上に", "〜に（時刻）", "〜の中に"],
})
vocab.append({
    "word": "knew",
    "meaning": "知っていた",
    "pos": "動詞",
    "level": "4級",
    "example": "She knew the names of many trees and flowers.",
    "distractors": ["知る", "知っている", "知るために"],
})
vocab.append({
    "word": "playing",
    "meaning": "（ゲームなどを）している",
    "pos": "動詞（〜ing）",
    "level": "4級",
    "example": "Stop playing the video game and go to bed.",
    "distractors": ["遊ぶ", "遊んだ", "やめる"],
})
vocab.append({
    "word": "clean",
    "meaning": "掃除する",
    "pos": "動詞",
    "level": "4級",
    "example": "You must clean your bedroom first.",
    "distractors": ["掃除する（三人称）", "掃除している", "掃除した"],
})

# ============================================================
# 大問2 会話のキーフレーズ（5語）
# ============================================================

vocab.append({
    "word": "on the phone",
    "meaning": "電話中",
    "pos": "表現",
    "level": "4級",
    "example": "She's on the phone. She's talking with Aunt Jill.",
    "distractors": ["店に行く", "アイデアがある", "料理が嫌い"],
})
vocab.append({
    "word": "come",
    "meaning": "来る",
    "pos": "動詞",
    "level": "4級",
    "example": "I'm going to the video shop. Do you want to come?",
    "distractors": ["元気ですか", "いくらですか", "新しいですか"],
})
vocab.append({
    "word": "going to work",
    "meaning": "仕事に行くところ",
    "pos": "表現",
    "level": "4級",
    "example": "Sorry, Lisa. I'm going to work now.",
    "distractors": ["小さすぎる", "家にいる", "あなたのものではない"],
})
vocab.append({
    "word": "red and white",
    "meaning": "赤と白の",
    "pos": "表現",
    "level": "4級",
    "example": "What does your umbrella look like? It's red and white.",
    "distractors": ["もちろん", "残念だね", "それだけ"],
})
vocab.append({
    "word": "can't find",
    "meaning": "見つけられない",
    "pos": "表現",
    "level": "4級",
    "example": "I looked in every room, but I can't find it.",
    "distractors": ["なかった", "私のものではなかった", "好きではなかった"],
})

# ============================================================
# 大問3 並べ替えのキーワード（5語）
# ============================================================

vocab.append({
    "word": "uniform",
    "meaning": "制服",
    "pos": "名詞",
    "level": "4級",
    "example": "I don't have to wear my uniform today.",
    "distractors": ["持つ", "着る", "するために"],
})
vocab.append({
    "word": "spaghetti",
    "meaning": "スパゲッティ",
    "pos": "名詞",
    "level": "4級",
    "example": "How about spaghetti for dinner?",
    "distractors": ["夕食", "〜について", "〜のために"],
})
vocab.append({
    "word": "interesting",
    "meaning": "面白い",
    "pos": "形容詞",
    "level": "4級",
    "example": "That TV program was not interesting at all.",
    "distractors": ["テレビ番組", "〜ではない", "〜だった"],
})
vocab.append({
    "word": "easy",
    "meaning": "簡単な",
    "pos": "形容詞",
    "level": "4級",
    "example": "The math test was not so easy for me.",
    "distractors": ["数学のテスト", "とても", "〜のために"],
})
vocab.append({
    "word": "choose",
    "meaning": "選ぶ",
    "pos": "動詞",
    "level": "4級",
    "example": "Paul, why did you choose this school?",
    "distractors": ["あなた", "した", "この"],
})

# ============================================================
# 大問4A 遠足のお知らせ（1語）
# ============================================================

vocab.append({
    "word": "museum",
    "meaning": "博物館",
    "pos": "名詞",
    "level": "4級",
    "example": "We will go to the Rainbow Museum instead if it rains.",
    "distractors": ["動物園", "劇場", "別の学校"],
})
# ============================================================
# 大問4B バスケのメール（2語）
# ============================================================

vocab.append({
    "word": "coach",
    "meaning": "コーチ",
    "pos": "名詞",
    "level": "4級",
    "example": "We can meet our new coach at the meeting!",
    "distractors": ["チームメイト", "キャプテン", "選手"],
})
vocab.append({
    "word": "headache",
    "meaning": "頭痛",
    "pos": "名詞",
    "level": "4級",
    "example": "I had a headache yesterday afternoon.",
    "distractors": ["熱", "風邪", "腹痛"],
})
# ============================================================
# 大問4C Kate's Story（2語）
# ============================================================

vocab.append({
    "word": "hospital",
    "meaning": "病院",
    "pos": "名詞",
    "level": "4級",
    "example": "Her grandmother is in the hospital now.",
    "distractors": ["家", "学校", "図書館"],
})
vocab.append({
    "word": "notebook",
    "meaning": "ノート",
    "pos": "名詞",
    "level": "4級",
    "example": "Kate gave her grandmother a notebook.",
    "distractors": ["歴史の本", "雑誌", "絵"],
})

assert len(vocab) == 30, f"Expected 30 words, got {len(vocab)}"

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

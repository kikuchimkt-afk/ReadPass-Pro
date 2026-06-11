# -*- coding: utf-8 -*-
"""
2026年度 第1回（本会場）英検4級 data.json
vocabulary（単語カード・単語クイズ）30語
一次ソース: 2026-1(本会場）/4級.pdf
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade4", "2026-1",
)
OUT = os.path.join(BASE, "data.json")

with open(OUT, encoding="utf-8") as f:
    data = json.load(f)

vocab = []

# ============================================================
# 大問1 正答語（15語）
# ============================================================

vocab.append({
    "word": "eggs",
    "meaning": "卵",
    "pos": "名詞",
    "level": "4級",
    "source": "大問1",
    "example": "I want to make some pancakes for breakfast, but we don't have any eggs.",
    "distractors": ["花", "本", "スポーツ"],
})
vocab.append({
    "word": "use",
    "meaning": "使う",
    "pos": "動詞",
    "level": "4級",
    "source": "大問1",
    "example": "I want to call my mother, but I don't have a phone. You can use my phone.",
    "distractors": ["登る", "去る", "送る"],
})
vocab.append({
    "word": "cut",
    "meaning": "切る",
    "pos": "動詞",
    "level": "4級",
    "source": "大問1",
    "example": "Mom, I want to make some cookies. All right, but please cut this carrot first.",
    "distractors": ["着く", "打つ", "走る"],
})
vocab.append({
    "word": "country",
    "meaning": "国",
    "pos": "名詞",
    "level": "4級",
    "source": "大問1",
    "example": "Is it warm in your country now? Yes, it's spring.",
    "distractors": ["切符", "動物", "道路"],
})
vocab.append({
    "word": "contest",
    "meaning": "コンテスト・大会",
    "pos": "名詞",
    "level": "4級",
    "source": "大問1",
    "example": "Taro enjoyed the chorus contest on TV yesterday.",
    "distractors": ["壁", "趣味", "旅行"],
})
vocab.append({
    "word": "open",
    "meaning": "開いている",
    "pos": "形容詞",
    "level": "4級",
    "source": "大問1",
    "example": "Can I study in the library today? Yes, it's open now.",
    "distractors": ["寒い", "遅い", "お気に入りの"],
})
vocab.append({
    "word": "city",
    "meaning": "都市・街",
    "pos": "名詞",
    "level": "4級",
    "source": "大問1",
    "example": "Sally went to eat Chinese food in a big city last weekend.",
    "distractors": ["単語", "体", "点"],
})
vocab.append({
    "word": "idea",
    "meaning": "アイデア",
    "pos": "名詞",
    "level": "4級",
    "source": "大問1",
    "example": "I have an idea. Let's go to the aquarium.",
    "distractors": ["終わり", "腕", "消しゴム"],
})
vocab.append({
    "word": "think",
    "meaning": "思う（think of 〜）",
    "pos": "動詞",
    "level": "4級",
    "source": "大問1",
    "example": "These are my new glasses. What do you think of them?",
    "distractors": ["見る", "言う", "終える"],
})
vocab.append({
    "word": "for",
    "meaning": "〜にとって（Good for you）",
    "pos": "前置詞",
    "level": "4級",
    "source": "大問1",
    "example": "Good for you. You practiced a lot.",
    "distractors": ["〜と一緒に", "〜の中で", "〜の後に"],
})
vocab.append({
    "word": "hear",
    "meaning": "聞く（hear about）",
    "pos": "動詞",
    "level": "4級",
    "source": "大問1",
    "example": "Did you hear about Dan? He's going to move back to England.",
    "distractors": ["待つ", "走る", "望む"],
})
vocab.append({
    "word": "share",
    "meaning": "分け合う",
    "pos": "動詞",
    "level": "4級",
    "source": "大問1",
    "example": "Here are four cookies, Bob. Please share them with your sister.",
    "distractors": ["答える", "泣く", "走る"],
})
vocab.append({
    "word": "cheaper",
    "meaning": "より安い",
    "pos": "形容詞",
    "level": "4級",
    "source": "大問1",
    "example": "Today, apples are cheaper than bananas.",
    "distractors": ["安い", "最も安い", "一番安い"],
})
vocab.append({
    "word": "swam",
    "meaning": "泳いだ",
    "pos": "動詞",
    "level": "4級",
    "source": "大問1",
    "example": "The students swam 50 meters in the school pool yesterday.",
    "distractors": ["泳ぐ", "泳いでいる", "泳ぐために"],
})
vocab.append({
    "word": "must",
    "meaning": "〜しなければならない",
    "pos": "助動詞",
    "level": "4級",
    "source": "大問1",
    "example": "You must read this book before the test next Monday.",
    "distractors": ["〜している", "〜である", "〜だった"],
})

# ============================================================
# 大問2 会話のキーフレーズ（5語）
# ============================================================

vocab.append({
    "word": "borrow",
    "meaning": "借りる",
    "pos": "動詞",
    "level": "4級",
    "source": "大問2",
    "example": "I forgot my red pen. Can I borrow yours?",
    "distractors": ["すぐ家に帰る？", "色は大丈夫？", "書くのは好き？"],
})
vocab.append({
    "word": "too tall",
    "meaning": "高すぎる",
    "pos": "句",
    "level": "4級",
    "source": "大問2",
    "example": "I want to climb this tree. It's too tall. Let's climb the one over there.",
    "distractors": ["花がきれい", "庭が大きい", "家がとてもきれい"],
})
vocab.append({
    "word": "how much",
    "meaning": "いくら",
    "pos": "句",
    "level": "4級",
    "source": "大問2",
    "example": "I want to buy these socks. How much are they?",
    "distractors": ["元気ですか", "いくつ持っていますか", "身長はどのくらい"],
})
vocab.append({
    "word": "kitchen table",
    "meaning": "キッチンのテーブル",
    "pos": "名詞",
    "level": "4級",
    "source": "大問2",
    "example": "I can't find my social studies textbook. It's on the kitchen table.",
    "distractors": ["難しい科目だ", "とても面白かった", "弟のものだ"],
})
vocab.append({
    "word": "Are you OK",
    "meaning": "大丈夫？",
    "pos": "句",
    "level": "4級",
    "source": "大問2",
    "example": "Jenny, you don't look well today. Are you OK?",
    "distractors": ["家に帰っていい？", "私を呼んだ？", "お母さんは医者？"],
})

# ============================================================
# 大問3 並べ替えのキーワード（5語）
# ============================================================

vocab.append({
    "word": "get up",
    "meaning": "起きる",
    "pos": "句動詞",
    "level": "4級",
    "source": "大問3",
    "example": "Why did you get up so early this morning?",
    "distractors": ["座る", "寝る", "走る"],
})
vocab.append({
    "word": "call",
    "meaning": "電話する",
    "pos": "動詞",
    "level": "4級",
    "source": "大問3",
    "example": "May I call you this afternoon?",
    "distractors": ["訪ねる", "書く", "待つ"],
})
vocab.append({
    "word": "mountains",
    "meaning": "山（複数）",
    "pos": "名詞",
    "level": "4級",
    "source": "大問3",
    "example": "You can see lots of high mountains in Nepal.",
    "distractors": ["川", "海", "森"],
})
vocab.append({
    "word": "leave",
    "meaning": "出発する・（家を）出る",
    "pos": "動詞",
    "level": "4級",
    "source": "大問3",
    "example": "I leave home for school at seven o'clock every morning.",
    "distractors": ["着く", "帰る", "待つ"],
})
vocab.append({
    "word": "coffee cups",
    "meaning": "コーヒーカップ",
    "pos": "名詞",
    "level": "4級",
    "source": "大問3",
    "example": "Could you wash these coffee cups, please?",
    "distractors": ["お茶", "皿", "フォーク"],
})

# ============================================================
# 大問4A ピアニストの訪問（1語）
# ============================================================

vocab.append({
    "word": "speech",
    "meaning": "スピーチ・演説",
    "pos": "名詞",
    "level": "4級",
    "source": "大問4A",
    "example": "He will first give a speech in the gym.",
    "distractors": ["歌を歌う", "おやつをもらう", "ダンスをする"],
})

# ============================================================
# 大問4B 猫のメール（2語）
# ============================================================

vocab.append({
    "word": "babies",
    "meaning": "赤ちゃん（子猫）",
    "pos": "名詞",
    "level": "4級",
    "source": "大問4B",
    "example": "She has three babies, and they are very cute.",
    "distractors": ["友達", "写真", "メール"],
})
vocab.append({
    "word": "next month",
    "meaning": "来月",
    "pos": "句",
    "level": "4級",
    "source": "大問4B",
    "example": "Can I visit your home next month?",
    "distractors": ["明日", "来週", "来年の夏"],
})

# ============================================================
# 大問4C 歴史博物館（2語）
# ============================================================

vocab.append({
    "word": "textbooks",
    "meaning": "教科書",
    "pos": "名詞",
    "level": "4級",
    "source": "大問4C",
    "example": "He liked looking at the textbooks most because they were so old.",
    "distractors": ["机", "地図", "黒板"],
})
vocab.append({
    "word": "history",
    "meaning": "歴史",
    "pos": "名詞",
    "level": "4級",
    "source": "大問4C",
    "example": "Now his favorite is history. George wants to go to more museums with his sister.",
    "distractors": ["数学", "英語", "音楽"],
})

assert len(vocab) == 30, f"Expected 30 words, got {len(vocab)}"

old_vocab = {v["word"]: v for v in data.get("vocabulary", [])}
for v in vocab:
    ov = old_vocab.get(v["word"], {})
    if ov.get("wordAudio"):
        v["wordAudio"] = ov["wordAudio"]

data["vocabulary"] = vocab

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Wrote {len(vocab)} vocabulary items to {OUT}")

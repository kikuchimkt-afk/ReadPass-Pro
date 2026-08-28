# -*- coding: utf-8 -*-
"""
2026年度 第1回（本会場）英検3級 data.json
vocabulary（単語カード・単語クイズ）30語
一次ソース: 2026-1(本会場）/3級.pdf
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade3", "2026-1",
)
OUT = os.path.join(BASE, "data.json")

with open(OUT, encoding="utf-8") as f:
    data = json.load(f)

vocab = []

# ============================================================
# 大問1 正答語（15語）
# ============================================================

vocab.append({
    "word": "relax",
    "meaning": "のんびりする・くつろぐ",
    "pos": "動詞",
    "level": "3級",
    "source": "大問1",
    "example": "I like to relax at home. I often watch a movie.",
    "distractors": ["動く", "計画する", "育てる"],
})
vocab.append({
    "word": "dirty",
    "meaning": "汚い",
    "pos": "形容詞",
    "level": "3級",
    "source": "大問1",
    "example": "Your shoes are so dirty. I have to clean them.",
    "distractors": ["賢い", "一般的な", "ばかな"],
})
vocab.append({
    "word": "accident",
    "meaning": "事故",
    "pos": "名詞",
    "level": "3級",
    "source": "大問1",
    "example": "I had an accident. I fell down the stairs this morning.",
    "distractors": ["助言", "大人", "追加"],
})
vocab.append({
    "word": "symbol",
    "meaning": "象徴",
    "pos": "名詞",
    "level": "3級",
    "source": "大問1",
    "example": "It's the library. It's a symbol of our city.",
    "distractors": ["砂", "状態", "瓶"],
})
vocab.append({
    "word": "ordered",
    "meaning": "注文した",
    "pos": "動詞",
    "level": "3級",
    "source": "大問1",
    "example": "He ordered some cake for dessert.",
    "distractors": ["到着した", "教えた", "信じた"],
})
vocab.append({
    "word": "taste",
    "meaning": "〜の味がする",
    "pos": "動詞",
    "level": "3級",
    "source": "大問1",
    "example": "The tomato soup that Mike made didn't taste good. It was too salty.",
    "distractors": ["運ぶ", "見つける", "出す"],
})
vocab.append({
    "word": "curtain",
    "meaning": "カーテン",
    "pos": "名詞",
    "level": "3級",
    "source": "大問1",
    "example": "It is a nice day today. Open the curtain, John.",
    "distractors": ["文", "スタジアム", "花屋"],
})
vocab.append({
    "word": "enough",
    "meaning": "十分に",
    "pos": "副詞",
    "level": "3級",
    "source": "大問1",
    "example": "I want a computer that is small enough to put in my backpack.",
    "distractors": ["再び", "もっと", "決して〜ない"],
})
vocab.append({
    "word": "throw",
    "meaning": "投げる（throw awayで「捨てる」）",
    "pos": "動詞",
    "level": "3級",
    "source": "大問1",
    "example": "Why did you throw away your green sweater? It was really old.",
    "distractors": ["落ちる", "望む", "買い物をする"],
})
vocab.append({
    "word": "get off",
    "meaning": "降りる",
    "pos": "句動詞",
    "level": "3級",
    "source": "大問1",
    "example": "Jack gets off the bus before his stop. He likes to walk for 30 minutes.",
    "distractors": ["乗る", "起きる", "中に入る"],
})
vocab.append({
    "word": "hand",
    "meaning": "手（give ... a handで「手伝い」）",
    "pos": "名詞（慣用句）",
    "level": "3級",
    "source": "大問1",
    "example": "Dad, can you give me a hand with my new TV? I need to bring it upstairs.",
    "distractors": ["顔", "脚", "足"],
})
vocab.append({
    "word": "from",
    "meaning": "〜から（far fromで「〜から遠く」）",
    "pos": "前置詞",
    "level": "3級",
    "source": "大問1",
    "example": "Ethan lives far from school, so he has to take the bus.",
    "distractors": ["沿って", "より下に", "〜の下に"],
})
vocab.append({
    "word": "cleaning",
    "meaning": "掃除すること",
    "pos": "動名詞",
    "level": "3級",
    "source": "大問1",
    "example": "Jack finished cleaning his room and then went to his friend's house.",
    "distractors": ["掃除する（原形）", "掃除した（過去形）", "掃除する（三人称単数）"],
})
vocab.append({
    "word": "to go",
    "meaning": "行くこと・行くように",
    "pos": "to不定詞",
    "level": "3級",
    "source": "大問1",
    "example": "His mother told him to go to bed earlier.",
    "distractors": ["行っている（動名詞）", "行った（過去形）", "行く（三人称単数）"],
})
vocab.append({
    "word": "cooking",
    "meaning": "料理すること",
    "pos": "動名詞",
    "level": "3級",
    "source": "大問1",
    "example": "Ellen is good at cooking. Her friends enjoy eating her delicious food.",
    "distractors": ["料理するために（to不定詞）", "料理した（過去形）", "料理する（三人称単数）"],
})

# ============================================================
# 大問2 会話のキーフレーズ（5語）
# ============================================================

vocab.append({
    "word": "ever",
    "meaning": "これまでに",
    "pos": "副詞",
    "level": "3級",
    "source": "大問2",
    "example": "I'm planning to go to Paris this summer. Have you ever been there?",
    "distractors": ["いくらですか", "かばんは見つかりましたか", "いくつか欲しいですか"],
})
vocab.append({
    "word": "sounds great",
    "meaning": "いいですね",
    "pos": "句",
    "level": "3級",
    "source": "大問2",
    "example": "Why don't we play tennis together on Saturday? That sounds great.",
    "distractors": ["楽しんでね", "すぐここに来るよ", "わかりません"],
})
vocab.append({
    "word": "in a minute",
    "meaning": "すぐに",
    "pos": "句",
    "level": "3級",
    "source": "大問2",
    "example": "Dinner is ready. Come downstairs. I'll be there in a minute.",
    "distractors": ["忙しすぎる", "すぐ電話する", "明日行く"],
})
vocab.append({
    "word": "matter",
    "meaning": "どうしたの（問題）",
    "pos": "名詞",
    "level": "3級",
    "source": "大問2",
    "example": "You're not eating your breakfast. What's the matter?",
    "distractors": ["友達ですか", "一人でできますか", "何かありますか"],
})
vocab.append({
    "word": "sorry",
    "meaning": "ごめんなさい",
    "pos": "形容詞",
    "level": "3級",
    "source": "大問2",
    "example": "Oh, I'm very sorry. It looks like mine.",
    "distractors": ["どういたしまして", "行くことにした", "今彼に話す"],
})

# ============================================================
# 大問3A 料理教室（3語）
# ============================================================

vocab.append({
    "word": "apron",
    "meaning": "エプロン",
    "pos": "名詞",
    "level": "3級",
    "source": "大問3A",
    "example": "Remember to bring an apron and a notebook.",
    "distractors": ["ノート", "レシピ", "シェフ"],
})
vocab.append({
    "word": "notebook",
    "meaning": "ノート",
    "pos": "名詞",
    "level": "3級",
    "source": "大問3A",
    "example": "What should the members of the classes do? Bring a notebook.",
    "distractors": ["エプロン", "皿洗い", "中国語"],
})
vocab.append({
    "word": "contest",
    "meaning": "コンテスト・大会",
    "pos": "名詞",
    "level": "3級",
    "source": "大問3A",
    "example": "Mr. Chen has won some international cooking contests.",
    "distractors": ["オンライン授業", "土曜の朝", "友達を招待"],
})

# ============================================================
# 大問3B 冬のセール（4語）
# ============================================================

vocab.append({
    "word": "scarf",
    "meaning": "マフラー",
    "pos": "名詞",
    "level": "3級",
    "source": "大問3B",
    "example": "I saw a nice scarf and bought it for you!",
    "distractors": ["財布", "コート", "セーター"],
})
vocab.append({
    "word": "wallet",
    "meaning": "財布",
    "pos": "名詞",
    "level": "3級",
    "source": "大問3B",
    "example": "Thank you for giving me a lovely present last month. I really like the wallet!",
    "distractors": ["マフラー", "コート", "ケーキ"],
})
vocab.append({
    "word": "department store",
    "meaning": "デパート",
    "pos": "名詞",
    "level": "3級",
    "source": "大問3B",
    "example": "Yesterday, I visited a department store near the station.",
    "distractors": ["公園", "博物館", "ケーキ屋"],
})
vocab.append({
    "word": "story",
    "meaning": "物語",
    "pos": "名詞",
    "level": "3級",
    "source": "大問3B",
    "example": "Linda often told me stories when you were cooking in the kitchen.",
    "distractors": ["ケーキ", "公園", "台所の手伝い"],
})

# ============================================================
# 大問3C Never Too Late（3語）
# ============================================================

vocab.append({
    "word": "artist",
    "meaning": "画家（芸術家）",
    "pos": "名詞",
    "level": "3級",
    "source": "大問3C",
    "example": "Anna Mary Robertson Moses was an American artist.",
    "distractors": ["農家", "料理人", "博物館の職員"],
})
vocab.append({
    "word": "painting",
    "meaning": "絵を描くこと",
    "pos": "動名詞",
    "level": "3級",
    "source": "大問3C",
    "example": "She decided to try painting instead. She was already over seventy-five years old then.",
    "distractors": ["写真を撮ること", "父への贈り物を買うこと", "家の中で遊ぶこと"],
})
vocab.append({
    "word": "museum",
    "meaning": "美術館（博物館）",
    "pos": "名詞",
    "level": "3級",
    "source": "大問3C",
    "example": "Even today, many people come to see her paintings in museums.",
    "distractors": ["農場", "料理教室", "絵を描くこと"],
})

assert len(vocab) == 30, f"Expected 30 words, got {len(vocab)}"

for i, item in enumerate(vocab, start=1):
    slug = item["word"].lower().replace(" ", "_")
    item["wordAudio"] = f"audio/vocab/w_{i:03d}_{slug}.mp3"

data["vocabulary"] = vocab

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Wrote {len(vocab)} vocabulary items to {OUT}")

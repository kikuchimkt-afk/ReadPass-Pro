# -*- coding: utf-8 -*-
"""
2026年度 第1回（本会場）英検準2級 data.json
vocabulary（単語カード・単語クイズ）40語
一次ソース: 2026-1(本会場）/準2級.pdf
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade-pre2", "2026-1",
)
OUT = os.path.join(BASE, "data.json")

with open(OUT, encoding="utf-8") as f:
    data = json.load(f)

vocab = []

# ============================================================
# 大問1 正答語・熟語（15語）
# ============================================================

vocab.append({
    "word": "absolutely",
    "meaning": "絶対に・非常に",
    "pos": "副詞",
    "level": "準2級",
    "source": "大問1",
    "example": "Michael, this meal is absolutely delicious! It's the best pasta that I've ever eaten.",
    "distractors": ["神経質に", "めったに", "別々に"],
})
vocab.append({
    "word": "transferred",
    "meaning": "異動させられた",
    "pos": "動詞",
    "level": "準2級",
    "source": "大問1",
    "example": "Dennis was recently transferred to his company's New York office.",
    "distractors": ["減らされた", "提案された", "謝罪した"],
})
vocab.append({
    "word": "dangers",
    "meaning": "危険",
    "pos": "名詞",
    "level": "準2級",
    "source": "大問1",
    "example": "Today, Mr. Carter taught his students about the dangers of smoking.",
    "distractors": ["宮殿", "市場", "美術館"],
})
vocab.append({
    "word": "reasonable",
    "meaning": "妥当な・手頃な",
    "pos": "形容詞",
    "level": "準2級",
    "source": "大問1",
    "example": "It had good reviews, and the price seemed reasonable compared to other options.",
    "distractors": ["木製の", "退屈な", "かわいい"],
})
vocab.append({
    "word": "announcement",
    "meaning": "発表・告知",
    "pos": "名詞",
    "level": "準2級",
    "source": "大問1",
    "example": "At the start of the lesson, Mr. Harris made an announcement.",
    "distractors": ["賞", "通路", "試み"],
})
vocab.append({
    "word": "statues",
    "meaning": "彫像",
    "pos": "名詞",
    "level": "準2級",
    "source": "大問1",
    "example": "The mayor has asked several local artists to create statues that will be put in the city's parks.",
    "distractors": ["方針", "毛布", "昆虫"],
})
vocab.append({
    "word": "receipt",
    "meaning": "領収書",
    "pos": "名詞",
    "level": "準2級",
    "source": "大問1",
    "example": "When Adam buys expensive items, he always keeps the receipt in a safe place.",
    "distractors": ["電池", "ウェブサイト", "額縁"],
})
vocab.append({
    "word": "trust",
    "meaning": "信頼する",
    "pos": "動詞",
    "level": "準2級",
    "source": "大問1",
    "example": "People can trust their friends to support them during difficult times.",
    "distractors": ["貼り付ける", "責める", "かく"],
})
vocab.append({
    "word": "score",
    "meaning": "得点を取る",
    "pos": "動詞",
    "level": "準2級",
    "source": "大問1",
    "example": "How many points did you score in the math test?",
    "distractors": ["入る", "従事する", "主張する"],
})
vocab.append({
    "word": "ache",
    "meaning": "痛む",
    "pos": "動詞",
    "level": "準2級",
    "source": "大問1",
    "example": "After running ten kilometers, Evan's legs started to ache.",
    "distractors": ["和らげる", "押す", "集める"],
})
vocab.append({
    "word": "except for",
    "meaning": "〜を除いて",
    "pos": "熟語",
    "level": "準2級",
    "source": "大問1",
    "example": "Almost all the pets in the shelter found homes, except for one dog that was still waiting for a family.",
    "distractors": ["〜の隣に", "〜の向かいに", "〜まで"],
})
vocab.append({
    "word": "Look out",
    "meaning": "気をつけて",
    "pos": "熟語",
    "level": "準2級",
    "source": "大問1",
    "example": "Look out! There's a bee near your face!",
    "distractors": ["乗る", "脱ぐ", "あきらめる"],
})
vocab.append({
    "word": "out of the question",
    "meaning": "ありえない・不可能",
    "pos": "熟語",
    "level": "準2級",
    "source": "大問1",
    "example": "No, that's out of the question, Megan. Your birthday is next month.",
    "distractors": ["未決定の", "機嫌がいい", "あなたの知ることではない"],
})
vocab.append({
    "word": "make up my mind",
    "meaning": "決心する",
    "pos": "熟語",
    "level": "準2級",
    "source": "大問1",
    "example": "No. I can't make up my mind. They all seem so interesting.",
    "distractors": ["うるさくする", "航海に出る", "明かりを消す"],
})
vocab.append({
    "word": "take a look at",
    "meaning": "見てみる",
    "pos": "熟語",
    "level": "準2級",
    "source": "大問1",
    "example": "Before buying a new smartphone, you should take a look at several different ones.",
    "distractors": ["〜に取りかかる", "〜のためにする", "〜と話をする"],
})

# ============================================================
# 大問2 会話完成（10語）
# ============================================================

vocab.append({
    "word": "take you there",
    "meaning": "そこへ連れて行ってあげる",
    "pos": "句",
    "level": "準2級",
    "source": "大問2",
    "example": "Well, I'm going in the same direction, so I can take you there. Please follow me.",
    "distractors": ["間違った道を行く", "たどり着けない", "もう会えない"],
})
vocab.append({
    "word": "volunteer",
    "meaning": "ボランティアの",
    "pos": "形容詞",
    "level": "準2級",
    "source": "大問2",
    "example": "I'd like to sign up for one of the volunteer programs this summer.",
    "distractors": ["有料の", "義務的な", "専門的な"],
})
vocab.append({
    "word": "librarian",
    "meaning": "司書",
    "pos": "名詞",
    "level": "準2級",
    "source": "大問2",
    "example": "Is \"Let's Work as a Librarian\" still open? I believe it begins on August 10.",
    "distractors": ["教師", "医者", "弁護士"],
})
vocab.append({
    "word": "cafeteria",
    "meaning": "学食・食堂",
    "pos": "名詞",
    "level": "準2級",
    "source": "大問2",
    "example": "From today, the cafeteria will be closed for repairs, and everyone must bring their own lunch.",
    "distractors": ["図書館", "教室", "体育館"],
})
vocab.append({
    "word": "bakery",
    "meaning": "パン屋",
    "pos": "名詞",
    "level": "準2級",
    "source": "大問2",
    "example": "OK. I'll stop by my favorite bakery.",
    "distractors": ["レストラン", "スーパー", "薬局"],
})
vocab.append({
    "word": "on your way",
    "meaning": "行き道で",
    "pos": "熟語",
    "level": "準2級",
    "source": "大問2",
    "example": "Can you buy something on your way today?",
    "distractors": ["帰り道で", "すぐに", "後で"],
})
vocab.append({
    "word": "repairs",
    "meaning": "修理",
    "pos": "名詞",
    "level": "準2級",
    "source": "大問2",
    "example": "The cafeteria will be closed for repairs.",
    "distractors": ["掃除", "建設", "閉鎖"],
})
vocab.append({
    "word": "fill out",
    "meaning": "記入する",
    "pos": "句動詞",
    "level": "準2級",
    "source": "大問2",
    "example": "Please go ahead and fill out this form.",
    "distractors": ["捨てる", "破る", "隠す"],
})
vocab.append({
    "word": "available",
    "meaning": "空いている・利用できる",
    "pos": "形容詞",
    "level": "準2級",
    "source": "大問2",
    "example": "Yes, it's still available.",
    "distractors": ["満席の", "高価な", "危険な"],
})
vocab.append({
    "word": "supermarket",
    "meaning": "スーパーマーケット",
    "pos": "名詞",
    "level": "準2級",
    "source": "大問2",
    "example": "I go to the one next to the supermarket, but there's a new one closer to your place.",
    "distractors": ["映画館", "公園", "病院"],
})

# ============================================================
# 大問3「The Advice」（5語）
# ============================================================

vocab.append({
    "word": "embarrassed",
    "meaning": "恥ずかしい思いをする",
    "pos": "形容詞",
    "level": "準2級",
    "source": "大問3",
    "example": "He worried that he might be embarrassed if his English was wrong.",
    "distractors": ["誇らしい", "退屈な", "怒った"],
})
vocab.append({
    "word": "attitude",
    "meaning": "態度",
    "pos": "名詞",
    "level": "準2級",
    "source": "大問3",
    "example": "Thanks to her, Haruto's attitude toward speaking English changed.",
    "distractors": ["能力", "成績", "計画"],
})
vocab.append({
    "word": "nervous",
    "meaning": "緊張した",
    "pos": "形容詞",
    "level": "準2級",
    "source": "大問3",
    "example": "He stood up and spoke clearly, despite feeling nervous.",
    "distractors": ["自信のある", "眠い", "空腹な"],
})
vocab.append({
    "word": "speech",
    "meaning": "スピーチ・発表",
    "pos": "名詞",
    "level": "準2級",
    "source": "大問3",
    "example": "When he finished the whole speech, however, Ms. Sato smiled and said his speech was very good.",
    "distractors": ["宿題", "試験", "手紙"],
})
vocab.append({
    "word": "making mistakes",
    "meaning": "間違えること",
    "pos": "名詞句",
    "level": "準2級",
    "source": "大問3",
    "example": "She told him that there was nothing wrong with making mistakes.",
    "distractors": ["英語を話すこと", "一生懸命やること", "諦めること"],
})

# ============================================================
# 大問4A「About joining my band」（5語）
# ============================================================

vocab.append({
    "word": "guitarist",
    "meaning": "ギタリスト",
    "pos": "名詞",
    "level": "準2級",
    "source": "大問4A",
    "example": "It is great to hear that you are interested in joining our band as a guitarist.",
    "distractors": ["歌手", "ドラマー", "ピアニスト"],
})
vocab.append({
    "word": "original music",
    "meaning": "オリジナル曲",
    "pos": "名詞句",
    "level": "準2級",
    "source": "大問4A",
    "example": "While they do not cover famous songs, they perform original music.",
    "distractors": ["有名な曲", "クラシック音楽", "ジャズ"],
})
vocab.append({
    "word": "campus",
    "meaning": "キャンパス",
    "pos": "名詞",
    "level": "準2級",
    "source": "大問4A",
    "example": "They usually practice on weekends in the music room on campus.",
    "distractors": ["市内", "スタジオ", "自宅"],
})
vocab.append({
    "word": "recommend",
    "meaning": "勧める・推薦する",
    "pos": "動詞",
    "level": "準2級",
    "source": "大問4A",
    "example": "What is true about the band members that Andrea recommends?",
    "distractors": ["拒否する", "批判する", "無視する"],
})
vocab.append({
    "word": "practice",
    "meaning": "練習",
    "pos": "名詞",
    "level": "準2級",
    "source": "大問4A",
    "example": "Then, you can go watch one of their practices to see if you like their music.",
    "distractors": ["コンサート", "試験", "面接"],
})

# ============================================================
# 大問4B「Pig Beach」（5語）
# ============================================================

vocab.append({
    "word": "native",
    "meaning": "原産の・自生の",
    "pos": "形容詞",
    "level": "準2級",
    "source": "大問4B",
    "example": "These pigs are not native to the island, and nobody knows exactly how they arrived there.",
    "distractors": ["野生の", "珍しい", "危険な"],
})
vocab.append({
    "word": "tourist",
    "meaning": "観光客",
    "pos": "名詞",
    "level": "準2級",
    "source": "大問4B",
    "example": "This has led many tourists to visit the island to see this unique sight.",
    "distractors": ["住民", "農家", "船員"],
})
vocab.append({
    "word": "harmful",
    "meaning": "有害な",
    "pos": "形容詞",
    "level": "準2級",
    "source": "大問4B",
    "example": "Some reports said that pigs ate harmful items, such as plastic.",
    "distractors": ["有益な", "安全な", "美味しい"],
})
vocab.append({
    "word": "campaign",
    "meaning": "キャンペーン",
    "pos": "名詞",
    "level": "準2級",
    "source": "大問4B",
    "example": "They have started campaigns to educate tourists on how to behave properly around the swimming pigs.",
    "distractors": ["法律", "罰金", "禁止"],
})
vocab.append({
    "word": "eco-friendly",
    "meaning": "環境に優しい",
    "pos": "形容詞",
    "level": "準2級",
    "source": "大問4B",
    "example": "They aim to improve the situation for both the pigs and the environment through more eco-friendly tourism.",
    "distractors": ["高価な", "危険な", "古い"],
})

assert len(vocab) == 40, f"Expected 40 words, got {len(vocab)}"

for i, v in enumerate(vocab):
    safe = v["word"].replace(" ", "_").replace("'", "").replace("-", "_").lower()
    v["wordAudio"] = f"audio/vocab/w_{i + 1:03d}_{safe}.mp3"
    v["exampleAudio"] = f"audio/vocab/ex_{i + 1:03d}_{safe}.mp3"

data["vocabulary"] = vocab

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Wrote {len(vocab)} vocabulary items to {OUT}")
print(f"  大問1: {len([v for v in vocab if v['source'] == '大問1'])}語")
print(f"  大問2: {len([v for v in vocab if v['source'] == '大問2'])}語")
print(f"  大問3: {len([v for v in vocab if v['source'] == '大問3'])}語")
print(f"  大問4A: {len([v for v in vocab if v['source'] == '大問4A'])}語")
print(f"  大問4B: {len([v for v in vocab if v['source'] == '大問4B'])}語")

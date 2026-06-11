# -*- coding: utf-8 -*-
"""
2026年度 第1回（本会場）英検準2級プラス data.json
vocabulary（単語カード・単語クイズ）55語
一次ソース: 2026-1(本会場）/準2級プラス解答.pdf
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade-pre2plus", "2026-1",
)
OUT = os.path.join(BASE, "data.json")

with open(OUT, encoding="utf-8") as f:
    data = json.load(f)

vocab = []

# ============================================================
# 大問1 正答語・熟語（17語）
# ============================================================

vocab.append({
    "word": "inventory",
    "meaning": "在庫",
    "pos": "名詞",
    "level": "準2級プラス",
    "source": "大問1",
    "example": "Let me check our inventory. One moment, please.",
    "distractors": ["許可", "観客", "地平線"],
})
vocab.append({
    "word": "religion",
    "meaning": "宗教",
    "pos": "名詞",
    "level": "準2級プラス",
    "source": "大問1",
    "example": "Many people in Japan do not follow any religion.",
    "distractors": ["状態", "熱意", "進歩"],
})
vocab.append({
    "word": "emission",
    "meaning": "排出",
    "pos": "名詞",
    "level": "準2級プラス",
    "source": "大問1",
    "example": "Scientists are worried about the emission of gases from cars.",
    "distractors": ["校長", "不足", "習慣"],
})
vocab.append({
    "word": "ensure",
    "meaning": "確実にする",
    "pos": "動詞",
    "level": "準2級プラス",
    "source": "大問1",
    "example": "I bought extra batteries to ensure that we don't run out.",
    "distractors": ["表現する", "じっと見る", "挨拶する"],
})
vocab.append({
    "word": "entertain",
    "meaning": "もてなす",
    "pos": "動詞",
    "level": "準2級プラス",
    "source": "大問1",
    "example": "I'm going to entertain some friends at my house.",
    "distractors": ["修理する", "さまよう", "説明する"],
})
vocab.append({
    "word": "survival",
    "meaning": "サバイバル・生存",
    "pos": "名詞",
    "level": "準2級プラス",
    "source": "大問1",
    "example": "We learned about the survival skills needed for camping.",
    "distractors": ["保証", "富", "愛情"],
})
vocab.append({
    "word": "convert",
    "meaning": "両替する・変換する",
    "pos": "動詞",
    "level": "準2級プラス",
    "source": "大問1",
    "example": "You should convert some Japanese yen to Canadian dollars before you go.",
    "distractors": ["保護する", "想像する", "検出する"],
})
vocab.append({
    "word": "portray",
    "meaning": "描く・表現する",
    "pos": "動詞",
    "level": "準2級プラス",
    "source": "大問1",
    "example": "He can portray their emotions so well in his drawings.",
    "distractors": ["除外する", "撃つ", "治す"],
})
vocab.append({
    "word": "steadier",
    "meaning": "より安定した",
    "pos": "形容詞",
    "level": "準2級プラス",
    "source": "大問1",
    "example": "You have to go at a steadier pace, Mike.",
    "distractors": ["より勇敢な", "より自由な", "より丁寧な"],
})
vocab.append({
    "word": "extremely",
    "meaning": "極めて",
    "pos": "副詞",
    "level": "準2級プラス",
    "source": "大問1",
    "example": "The weather in Russia is extremely cold in winter.",
    "distractors": ["公に", "短く", "まもなく"],
})
vocab.append({
    "word": "break down",
    "meaning": "故障する",
    "pos": "熟語",
    "level": "準2級プラス",
    "source": "大問1",
    "example": "I hope my computer doesn't break down before I finish my report.",
    "distractors": ["着飾る", "見回る", "振り払う"],
})
vocab.append({
    "word": "go through",
    "meaning": "調べる・経験する",
    "pos": "熟語",
    "level": "準2級プラス",
    "source": "大問1",
    "example": "Before writing his novel, Michael had to go through a lot of research.",
    "distractors": ["決める", "生じる", "同意する"],
})
vocab.append({
    "word": "So far",
    "meaning": "これまでのところ",
    "pos": "熟語",
    "level": "準2級プラス",
    "source": "大問1",
    "example": "So far, the changes seem to be working well.",
    "distractors": ["無料で", "同様に", "無駄に"],
})
vocab.append({
    "word": "even if",
    "meaning": "たとえ〜でも",
    "pos": "熟語",
    "level": "準2級プラス",
    "source": "大問1",
    "example": "I'll go to the beach even if he says no.",
    "distractors": ["まるで〜のように", "〜の場合のみ", "〜の時だけ"],
})
vocab.append({
    "word": "by way of",
    "meaning": "〜経由で",
    "pos": "熟語",
    "level": "準2級プラス",
    "source": "大問1",
    "example": "It is easy to get to Ironton by way of a new highway.",
    "distractors": ["〜を恐れて", "〜のために", "〜の場合に"],
})
vocab.append({
    "word": "next to",
    "meaning": "〜の隣に",
    "pos": "熟語",
    "level": "準2級プラス",
    "source": "大問1",
    "example": "Just sit next to me, and I'll show you how to play.",
    "distractors": ["〜を意識して", "〜の一部として", "〜が不足して"],
})
vocab.append({
    "word": "feel free",
    "meaning": "遠慮なく",
    "pos": "熟語",
    "level": "準2級プラス",
    "source": "大問1",
    "example": "Feel free to borrow my car if you want to.",
    "distractors": ["一生懸命やる", "専念する", "交代する"],
})

# ============================================================
# 大問2A「Guide Signs Without Words」（9語）
# ============================================================

vocab.append({
    "word": "pictogram",
    "meaning": "象形図・ピクトグラム",
    "pos": "名詞",
    "level": "準2級プラス",
    "source": "大問2A",
    "example": "Pictograms are a type of guide sign that use images instead of words.",
    "distractors": ["地図", "標語", "看板"],
})
vocab.append({
    "word": "transportation",
    "meaning": "交通",
    "pos": "名詞",
    "level": "準2級プラス",
    "source": "大問2A",
    "example": "Pictograms can be found in many fields, such as transportation and tourism.",
    "distractors": ["観光", "天気", "教育"],
})
vocab.append({
    "word": "complex",
    "meaning": "複雑な",
    "pos": "形容詞",
    "level": "準2級プラス",
    "source": "大問2A",
    "example": "Early pictograms were often too complex in style and too detailed.",
    "distractors": ["簡単な", "明確な", "小さな"],
})
vocab.append({
    "word": "detailed",
    "meaning": "詳細な",
    "pos": "形容詞",
    "level": "準2級プラス",
    "source": "大問2A",
    "example": "They were too detailed, which made them difficult to understand quickly.",
    "distractors": ["大まかな", "短い", "古い"],
})
vocab.append({
    "word": "athlete",
    "meaning": "選手",
    "pos": "名詞",
    "level": "準2級プラス",
    "source": "大問2A",
    "example": "The new pictograms were used to guide visitors, athletes, and staff members.",
    "distractors": ["観客", "審判", "記者"],
})
vocab.append({
    "word": "effective",
    "meaning": "効果的な",
    "pos": "形容詞",
    "level": "準2級プラス",
    "source": "大問2A",
    "example": "Their success demonstrated how effective simple visual communication could be.",
    "distractors": ["無効な", "高価な", "危険な"],
})
vocab.append({
    "word": "international",
    "meaning": "国際的な",
    "pos": "形容詞",
    "level": "準2級プラス",
    "source": "大問2A",
    "example": "This showed the need for simpler visual communication at international events.",
    "distractors": ["国内の", "地域の", "個人的な"],
})
vocab.append({
    "word": "standard",
    "meaning": "標準",
    "pos": "名詞",
    "level": "準2級プラス",
    "source": "大問2A",
    "example": "In this way, a new standard for pictograms was set.",
    "distractors": ["例外", "伝統", "問題"],
})
vocab.append({
    "word": "visual",
    "meaning": "視覚的な",
    "pos": "形容詞",
    "level": "準2級プラス",
    "source": "大問2A",
    "example": "The design team tried to create simpler pictograms while still showing the meaning without words.",
    "distractors": ["聴覚的な", "物理的な", "感情的な"],
})

# ============================================================
# 大問2B「Attention Span」（10語）
# ============================================================

vocab.append({
    "word": "attention span",
    "meaning": "注意力の持続時間",
    "pos": "名詞句",
    "level": "準2級プラス",
    "source": "大問2B",
    "example": "Humans have shorter attention spans than they did in the past.",
    "distractors": ["記憶力", "学習速度", "集中力の欠如"],
})
vocab.append({
    "word": "focus",
    "meaning": "集中する",
    "pos": "動詞",
    "level": "準2級プラス",
    "source": "大問2B",
    "example": "The study suggests people cannot focus as long as a goldfish.",
    "distractors": ["眠る", "逃げる", "話す"],
})
vocab.append({
    "word": "platform",
    "meaning": "プラットフォーム",
    "pos": "名詞",
    "level": "準2級プラス",
    "source": "大問2B",
    "example": "Many people use social media platforms that show short videos and messages.",
    "distractors": ["アプリ", "広告", "記事"],
})
vocab.append({
    "word": "teenager",
    "meaning": "十代の若者",
    "pos": "名詞",
    "level": "準2級プラス",
    "source": "大問2B",
    "example": "About 30 percent of teenagers reported difficulty focusing in class.",
    "distractors": ["大人", "幼児", "教師"],
})
vocab.append({
    "word": "maintain",
    "meaning": "維持する",
    "pos": "動詞",
    "level": "準2級プラス",
    "source": "大問2B",
    "example": "Some experts suggest solutions to help people maintain a longer attention span.",
    "distractors": ["失う", "減らす", "中断する"],
})
vocab.append({
    "word": "mental",
    "meaning": "精神的な",
    "pos": "形容詞",
    "level": "準2級プラス",
    "source": "大問2B",
    "example": "It is important to avoid a state where people get mentally too tired.",
    "distractors": ["肉体的な", "一時的な", "感情的な"],
})
vocab.append({
    "word": "regular",
    "meaning": "定期的な",
    "pos": "形容詞",
    "level": "準2級プラス",
    "source": "大問2B",
    "example": "A simple approach is to take regular breaks.",
    "distractors": ["長い", "突然の", "最後の"],
})
vocab.append({
    "word": "rhythm",
    "meaning": "リズム",
    "pos": "名詞",
    "level": "準2級プラス",
    "source": "大問2B",
    "example": "Understanding personal attention rhythms is considered helpful.",
    "distractors": ["習慣", "計画", "目標"],
})
vocab.append({
    "word": "conduct",
    "meaning": "実施する",
    "pos": "動詞",
    "level": "準2級プラス",
    "source": "大問2B",
    "example": "According to a study conducted by an IT company, humans have shorter attention spans.",
    "distractors": ["報告する", "中止する", "拒否する"],
})
vocab.append({
    "word": "report",
    "meaning": "報告する",
    "pos": "動詞",
    "level": "準2級プラス",
    "source": "大問2B",
    "example": "About 30 percent of teenagers reported difficulty focusing in class.",
    "distractors": ["忘れる", "隠す", "否定する"],
})

# ============================================================
# 大問3A「Apartment viewing information」（6語）
# ============================================================

vocab.append({
    "word": "apartment",
    "meaning": "アパート・マンション",
    "pos": "名詞",
    "level": "準2級プラス",
    "source": "大問3A",
    "example": "We found an apartment that we thought would suit you well.",
    "distractors": ["ホテル", "オフィス", "店舗"],
})
vocab.append({
    "word": "neighborhood",
    "meaning": "近所・地区",
    "pos": "名詞",
    "level": "準2級プラス",
    "source": "大問3A",
    "example": "It is in a quiet neighborhood with good access to public transportation.",
    "distractors": ["建物", "部屋", "階段"],
})
vocab.append({
    "word": "balcony",
    "meaning": "バルコニー",
    "pos": "名詞",
    "level": "準2級プラス",
    "source": "大問3A",
    "example": "The balcony is a bit small, but it gets plenty of light.",
    "distractors": ["庭", "屋根", "玄関"],
})
vocab.append({
    "word": "rent",
    "meaning": "家賃",
    "pos": "名詞",
    "level": "準2級プラス",
    "source": "大問3A",
    "example": "The rent is $850 per month, and it includes the Internet.",
    "distractors": ["敷金", "保険", "税金"],
})
vocab.append({
    "word": "electricity",
    "meaning": "電気",
    "pos": "名詞",
    "level": "準2級プラス",
    "source": "大問3A",
    "example": "The rent includes the Internet, but not water or electricity.",
    "distractors": ["水道", "ガス", "暖房"],
})
vocab.append({
    "word": "agreement",
    "meaning": "契約・合意",
    "pos": "名詞",
    "level": "準2級プラス",
    "source": "大問3A",
    "example": "You will need to follow the next steps, including signing the agreement.",
    "distractors": ["予約", "見学", "返信"],
})

# ============================================================
# 大問3B「A Fifteen-Minute City」（13語）
# ============================================================

vocab.append({
    "word": "concept",
    "meaning": "概念",
    "pos": "名詞",
    "level": "準2級プラス",
    "source": "大問3B",
    "example": "This concept is based on the idea that important places should be located close to people's homes.",
    "distractors": ["計画", "法律", "問題"],
})
vocab.append({
    "word": "carbon dioxide",
    "meaning": "二酸化炭素",
    "pos": "名詞",
    "level": "準2級プラス",
    "source": "大問3B",
    "example": "Paris is working to lower the amount of carbon dioxide released.",
    "distractors": ["酸素", "窒素", "水素"],
})
vocab.append({
    "word": "pollution",
    "meaning": "汚染",
    "pos": "名詞",
    "level": "準2級プラス",
    "source": "大問3B",
    "example": "Paris wants to reduce the level of harmful air pollution.",
    "distractors": ["温暖化", "減少", "保護"],
})
vocab.append({
    "word": "citizen",
    "meaning": "市民",
    "pos": "名詞",
    "level": "準2級プラス",
    "source": "大問3B",
    "example": "Through the fifteen-minute city concept, citizens can get around the city more easily.",
    "distractors": ["観光客", "政治家", "建築家"],
})
vocab.append({
    "word": "utilize",
    "meaning": "活用する",
    "pos": "動詞",
    "level": "準2級プラス",
    "source": "大問3B",
    "example": "The city uses unique approaches to utilize empty spaces.",
    "distractors": ["破壊する", "無視する", "売却する"],
})
vocab.append({
    "word": "rooftop garden",
    "meaning": "屋上庭園",
    "pos": "名詞句",
    "level": "準2級プラス",
    "source": "大問3B",
    "example": "The building now offers a market, a hotel, restaurants, and even a rooftop garden.",
    "distractors": ["地下駐車場", "公園", "遊歩道"],
})
vocab.append({
    "word": "bicycle lane",
    "meaning": "自転車専用道路",
    "pos": "名詞句",
    "level": "準2級プラス",
    "source": "大問3B",
    "example": "Bicycle lanes were introduced on a large scale as part of the project.",
    "distractors": ["歩道", "高速道路", "駐車場"],
})
vocab.append({
    "word": "climate change",
    "meaning": "気候変動",
    "pos": "名詞句",
    "level": "準2級プラス",
    "source": "大問3B",
    "example": "These efforts may help solve the global problem of climate change today.",
    "distractors": ["経済成長", "人口増加", "都市化"],
})
vocab.append({
    "word": "quality of life",
    "meaning": "生活の質",
    "pos": "名詞句",
    "level": "準2級プラス",
    "source": "大問3B",
    "example": "The project can lead to a better quality of life for people.",
    "distractors": ["生活費", "生活習慣", "生活水準の低下"],
})
vocab.append({
    "word": "access",
    "meaning": "アクセス・利用しやすさ",
    "pos": "名詞",
    "level": "準2級プラス",
    "source": "大問3B",
    "example": "The project helps provide improved access to services necessary for daily life.",
    "distractors": ["費用", "距離", "制限"],
})
vocab.append({
    "word": "spread",
    "meaning": "広がる",
    "pos": "動詞",
    "level": "準2級プラス",
    "source": "大問3B",
    "example": "The fifteen-minute city project is spreading to other cities around the world.",
    "distractors": ["縮小する", "停止する", "拒否する"],
})
vocab.append({
    "word": "scale",
    "meaning": "規模",
    "pos": "名詞",
    "level": "準2級プラス",
    "source": "大問3B",
    "example": "It is possible to achieve important changes on a city scale.",
    "distractors": ["速度", "高度", "深さ"],
})
vocab.append({
    "word": "encourage",
    "meaning": "奨励する",
    "pos": "動詞",
    "level": "準2級プラス",
    "source": "大問3B",
    "example": "One way to do this is by encouraging people to use cars less.",
    "distractors": ["禁止する", "強制する", "無視する"],
})

assert len(vocab) == 55, f"Expected 55 words, got {len(vocab)}"

for i, v in enumerate(vocab):
    safe = v["word"].replace(" ", "_").replace("'", "").replace("-", "_").lower()
    v["wordAudio"] = f"audio/vocab/w_{i + 1:03d}_{safe}.mp3"

data["vocabulary"] = vocab

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Wrote {len(vocab)} vocabulary items to {OUT}")
print(f"  大問1: {len([v for v in vocab if v['source'] == '大問1'])}語")
print(f"  大問2A: {len([v for v in vocab if v['source'] == '大問2A'])}語")
print(f"  大問2B: {len([v for v in vocab if v['source'] == '大問2B'])}語")
print(f"  大問3A: {len([v for v in vocab if v['source'] == '大問3A'])}語")
print(f"  大問3B: {len([v for v in vocab if v['source'] == '大問3B'])}語")

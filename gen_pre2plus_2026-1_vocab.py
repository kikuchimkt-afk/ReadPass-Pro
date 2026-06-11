# -*- coding: utf-8 -*-
"""
2026年度 第1回（土曜準会場）英検準2級プラス data.json
Step 1: vocabulary（単語カード・単語クイズ）55語
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade-pre2plus", "2026-1-sat",
)
OUT = os.path.join(BASE, "data.json")
os.makedirs(BASE, exist_ok=True)

if os.path.exists(OUT):
    with open(OUT, encoding="utf-8") as f:
        data = json.load(f)
else:
    data = {}

data.update({
    "grade": "grade-pre2plus",
    "year": 2026,
    "session": "2026-1-sat",
    "title": "2026年度 第1回（土曜準会場）",
    "sections": data.get("sections", []),
    "lessonPlan": data.get("lessonPlan", {}),
})

vocab = []

# ============================================================
# 大問1 正答語・熟語（17語）
# ============================================================

vocab.append({
    "word": "revise",
    "meaning": "修正する・見直す",
    "pos": "動詞",
    "level": "準2級プラス",
    "source": "大問1",
    "example": "The teacher told the students to revise their essays before handing them in.",
    "distractors": ["分ける", "減らす", "挨拶する"],
})
vocab.append({
    "word": "acknowledge",
    "meaning": "認める・評価する",
    "pos": "動詞",
    "level": "準2級プラス",
    "source": "大問1",
    "example": "She made sure to acknowledge the students who had worked especially hard.",
    "distractors": ["苦労する", "絞る", "出版する"],
})
vocab.append({
    "word": "aid",
    "meaning": "援助する",
    "pos": "動詞",
    "level": "準2級プラス",
    "source": "大問1",
    "example": "The charity concert raised money to aid the people affected by the earthquake.",
    "distractors": ["横たわる", "報酬を与える", "称える"],
})
vocab.append({
    "word": "distinction",
    "meaning": "違い・区別",
    "pos": "名詞",
    "level": "準2級プラス",
    "source": "大問1",
    "example": "There is no distinction between the computers in the office.",
    "distractors": ["比率", "挑戦", "お買い得"],
})
vocab.append({
    "word": "author",
    "meaning": "作家・著者",
    "pos": "名詞",
    "level": "準2級プラス",
    "source": "大問1",
    "example": "Kellan Storme is my favorite author. He wrote many interesting stories.",
    "distractors": ["役人", "俳優", "技師"],
})
vocab.append({
    "word": "insert",
    "meaning": "挿入する",
    "pos": "動詞",
    "level": "準2級プラス",
    "source": "大問1",
    "example": "You can insert some pictures from the Internet into your report.",
    "distractors": ["溶かす", "さまよう", "折る"],
})
vocab.append({
    "word": "majority",
    "meaning": "大多数",
    "pos": "名詞",
    "level": "準2級プラス",
    "source": "大問1",
    "example": "The majority of students thought that the history test was too difficult.",
    "distractors": ["方法", "関係", "可能性"],
})
vocab.append({
    "word": "nightmare",
    "meaning": "悪夢",
    "pos": "名詞",
    "level": "準2級プラス",
    "source": "大問1",
    "example": "I had a horrible nightmare about getting lost in a dark forest.",
    "distractors": ["市民", "展示", "場所"],
})
vocab.append({
    "word": "humble",
    "meaning": "謙虚な",
    "pos": "形容詞",
    "level": "準2級プラス",
    "source": "大問1",
    "example": "I try to stay humble and focused on my work.",
    "distractors": ["空の", "痛い", "残酷な"],
})
vocab.append({
    "word": "commonly",
    "meaning": "一般的に",
    "pos": "副詞",
    "level": "準2級プラス",
    "source": "大問1",
    "example": "Cinnamon and nutmeg are commonly used in pumpkin pie.",
    "distractors": ["親切に", "合法的に", "専門的に"],
})
vocab.append({
    "word": "drop by",
    "meaning": "立ち寄る",
    "pos": "熟語",
    "level": "準2級プラス",
    "source": "大問1",
    "example": "If you drop by the bookstore, could you get me a fashion magazine?",
    "distractors": ["あきらめる", "理解する", "転ぶ"],
})
vocab.append({
    "word": "be short of",
    "meaning": "〜が不足している",
    "pos": "熟語",
    "level": "準2級プラス",
    "source": "大問1",
    "example": "We might be short of some supplies in the stationery cupboard.",
    "distractors": ["〜を確信している", "〜がない", "〜の種類である"],
})
vocab.append({
    "word": "leave it alone",
    "meaning": "そのままにしておく",
    "pos": "熟語",
    "level": "準2級プラス",
    "source": "大問1",
    "example": "Leave it alone. Its mother will come back for it.",
    "distractors": ["追い払う", "捨てる", "引き継ぐ"],
})
vocab.append({
    "word": "see off",
    "meaning": "見送る",
    "pos": "熟語",
    "level": "準2級プラス",
    "source": "大問1",
    "example": "Thank you for coming to the airport to see off my cousin.",
    "distractors": ["見せびらかす", "配る", "連れてくる"],
})
vocab.append({
    "word": "Before long",
    "meaning": "まもなく",
    "pos": "熟語",
    "level": "準2級プラス",
    "source": "大問1",
    "example": "Before long, he made some new friends and started to enjoy living there.",
    "distractors": ["無料で", "需要が高い", "平均して"],
})
vocab.append({
    "word": "reminds her of",
    "meaning": "〜を思い出させる",
    "pos": "熟語",
    "level": "準2級プラス",
    "source": "大問1",
    "example": "The smell of fresh bread always reminds her of her childhood.",
    "distractors": ["〜から学ぶ", "〜について聞く", "〜を説得する"],
})
vocab.append({
    "word": "turned out",
    "meaning": "結局〜だった",
    "pos": "熟語",
    "level": "準2級プラス",
    "source": "大問1",
    "example": "It turned out to be sunny, even though rain was forecast all day.",
    "distractors": ["使い果たした", "消した", "配った"],
})

# ============================================================
# 大問2A「A Christmas Tradition」（9語）
# ============================================================

vocab.append({
    "word": "tradition",
    "meaning": "伝統",
    "pos": "名詞",
    "level": "準2級プラス",
    "source": "大問2A",
    "example": "Throwing soft toys onto the field has become a wonderful tradition.",
    "distractors": ["試合", "規則", "祝日"],
})
vocab.append({
    "word": "volunteer",
    "meaning": "ボランティア",
    "pos": "名詞",
    "level": "準2級プラス",
    "source": "大問2A",
    "example": "The toys are collected by volunteers and delivered to children in need.",
    "distractors": ["選手", "観客", "審判"],
})
vocab.append({
    "word": "eventually",
    "meaning": "最終的に",
    "pos": "副詞",
    "level": "準2級プラス",
    "source": "大問2A",
    "example": "Eventually, these toys are delivered to children who are in need.",
    "distractors": ["対照的に", "一方で", "にもかかわらず"],
})
vocab.append({
    "word": "fortunate",
    "meaning": "恵まれた",
    "pos": "形容詞",
    "level": "準2級プラス",
    "source": "大問2A",
    "example": "They wanted to help local children who were less fortunate than others.",
    "distractors": ["有名な", "裕福な", "幸運な"],
})
vocab.append({
    "word": "gesture",
    "meaning": "親切な行い",
    "pos": "名詞",
    "level": "準2級プラス",
    "source": "大問2A",
    "example": "Many people have been touched by the kind gesture of the club and its fans.",
    "distractors": ["贈り物", "約束", "計画"],
})
vocab.append({
    "word": "stadium",
    "meaning": "スタジアム",
    "pos": "名詞",
    "level": "準2級プラス",
    "source": "大問2A",
    "example": "Fans come to the stadium not only to watch a match but also to throw soft toys.",
    "distractors": ["公園", "劇場", "博物館"],
})
vocab.append({
    "word": "overseas",
    "meaning": "海外の",
    "pos": "形容詞",
    "level": "準2級プラス",
    "source": "大問2A",
    "example": "Some toys are sent to children overseas during the Christmas season.",
    "distractors": ["国内の", "地域の", "近隣の"],
})
vocab.append({
    "word": "in need",
    "meaning": "困っている",
    "pos": "句",
    "level": "準2級プラス",
    "source": "大問2A",
    "example": "The toys are delivered to children who are in need.",
    "distractors": ["余裕がある", "健康な", "幸せな"],
})
vocab.append({
    "word": "collect",
    "meaning": "集める",
    "pos": "動詞",
    "level": "準2級プラス",
    "source": "大問2A",
    "example": "Tens of thousands of soft toys are thrown and then immediately collected.",
    "distractors": ["投げる", "配る", "捨てる"],
})

# ============================================================
# 大問2B「Traveling for Dental Care」（10語）
# ============================================================

vocab.append({
    "word": "dental tourism",
    "meaning": "歯科ツーリズム",
    "pos": "名詞句",
    "level": "準2級プラス",
    "source": "大問2B",
    "example": "People visit other countries to get their teeth treated. This is known as dental tourism.",
    "distractors": ["観光旅行", "医療保険", "歯科検診"],
})
vocab.append({
    "word": "treatment",
    "meaning": "治療",
    "pos": "名詞",
    "level": "準2級プラス",
    "source": "大問2B",
    "example": "Some types of dental care in Australia cost more than twice as much as in Thailand.",
    "distractors": ["診断", "予防", "手術"],
})
vocab.append({
    "word": "appointment",
    "meaning": "予約",
    "pos": "名詞",
    "level": "準2級プラス",
    "source": "大問2B",
    "example": "Around 20 percent could not book a clinic visit or see a dentist.",
    "distractors": ["治療", "診察", "手術"],
})
vocab.append({
    "word": "survey",
    "meaning": "調査",
    "pos": "名詞",
    "level": "準2級プラス",
    "source": "大問2B",
    "example": "In a 2024 survey of more than 2,000 people, many could not see a dentist.",
    "distractors": ["報告", "実験", "会議"],
})
vocab.append({
    "word": "unnecessary",
    "meaning": "不必要な",
    "pos": "形容詞",
    "level": "準2級プラス",
    "source": "大問2B",
    "example": "There is a possibility of receiving unnecessary treatment abroad.",
    "distractors": ["必要な", "安全な", "専門的な"],
})
vocab.append({
    "word": "legal",
    "meaning": "法的な",
    "pos": "形容詞",
    "level": "準2級プラス",
    "source": "大問2B",
    "example": "They may not receive enough legal support if something goes wrong.",
    "distractors": ["医学的な", "経済的な", "技術的な"],
})
vocab.append({
    "word": "abroad",
    "meaning": "海外で",
    "pos": "副詞",
    "level": "準2級プラス",
    "source": "大問2B",
    "example": "People travel abroad not only for fun but also for dental care.",
    "distractors": ["国内で", "近くで", "地元で"],
})
vocab.append({
    "word": "access",
    "meaning": "利用しやすさ・アクセス",
    "pos": "名詞",
    "level": "準2級プラス",
    "source": "大問2B",
    "example": "The trend highlights the importance of providing easy access to dental care.",
    "distractors": ["費用", "品質", "距離"],
})
vocab.append({
    "word": "material",
    "meaning": "材料",
    "pos": "名詞",
    "level": "準2級プラス",
    "source": "大問2B",
    "example": "Some patients may get treatment using low-quality materials.",
    "distractors": ["機械", "薬", "技術"],
})
vocab.append({
    "word": "expert",
    "meaning": "専門家",
    "pos": "名詞",
    "level": "準2級プラス",
    "source": "大問2B",
    "example": "According to experts, people should be careful about the dangers of dental tourism.",
    "distractors": ["患者", "医者", "旅行者"],
})

# ============================================================
# 大問3A「Dog Sitting Email」（6語）
# ============================================================

vocab.append({
    "word": "available",
    "meaning": "利用可能な・空いている",
    "pos": "形容詞",
    "level": "準2級プラス",
    "source": "大問3A",
    "example": "I am happy to tell you I am available on the dates you mentioned.",
    "distractors": ["忙しい", "不在の", "予約済みの"],
})
vocab.append({
    "word": "experience",
    "meaning": "経験",
    "pos": "名詞",
    "level": "準2級プラス",
    "source": "大問3A",
    "example": "I have five years of experience as a dog sitter.",
    "distractors": ["資格", "趣味", "希望"],
})
vocab.append({
    "word": "comfortable",
    "meaning": "快適な・安心できる",
    "pos": "形容詞",
    "level": "準2級プラス",
    "source": "大問3A",
    "example": "I am confident that your dog will feel safe and comfortable with me.",
    "distractors": ["不安な", "退屈な", "空腹な"],
})
vocab.append({
    "word": "fee",
    "meaning": "料金",
    "pos": "名詞",
    "level": "準2級プラス",
    "source": "大問3A",
    "example": "The daily fee is fifty dollars.",
    "distractors": ["割引", "返金", "税金"],
})
vocab.append({
    "word": "payment",
    "meaning": "支払い",
    "pos": "名詞",
    "level": "準2級プラス",
    "source": "大問3A",
    "example": "Payment is required before the service.",
    "distractors": ["予約", "返信", "確認"],
})
vocab.append({
    "word": "respond",
    "meaning": "返事する",
    "pos": "動詞",
    "level": "準2級プラス",
    "source": "大問3A",
    "example": "Please respond by June 22 if you wish to use my services.",
    "distractors": ["支払う", "訪問する", "キャンセルする"],
})

# ============================================================
# 大問3B「Avocado Production」（13語）
# ============================================================

vocab.append({
    "word": "avocado",
    "meaning": "アボカド",
    "pos": "名詞",
    "level": "準2級プラス",
    "source": "大問3B",
    "example": "Avocados have been a popular food in many countries around the world.",
    "distractors": ["トマト", "バナナ", "レモン"],
})
vocab.append({
    "word": "import",
    "meaning": "輸入する",
    "pos": "動詞",
    "level": "準2級プラス",
    "source": "大問3B",
    "example": "These countries import a lot of avocados from other nations.",
    "distractors": ["輸出する", "栽培する", "消費する"],
})
vocab.append({
    "word": "demand",
    "meaning": "需要",
    "pos": "名詞",
    "level": "準2級プラス",
    "source": "大問3B",
    "example": "France and the United Kingdom have already experienced high demand.",
    "distractors": ["供給", "価格", "品質"],
})
vocab.append({
    "word": "shortage",
    "meaning": "不足",
    "pos": "名詞",
    "level": "準2級プラス",
    "source": "大問3B",
    "example": "Increased demand has created water shortage problems in production areas.",
    "distractors": ["余剰", "豊富", "増加"],
})
vocab.append({
    "word": "eco-friendly",
    "meaning": "環境に優しい",
    "pos": "形容詞",
    "level": "準2級プラス",
    "source": "大問3B",
    "example": "The mark means the avocados are produced in an eco-friendly way.",
    "distractors": ["高価な", "手作りの", "有機の"],
})
vocab.append({
    "word": "fair",
    "meaning": "公正な・適正な",
    "pos": "形容詞",
    "level": "準2級プラス",
    "source": "大問3B",
    "example": "Farmers receive a fair amount of money for their avocados.",
    "distractors": ["安い", "高い", "固定の"],
})
vocab.append({
    "word": "consumer",
    "meaning": "消費者",
    "pos": "名詞",
    "level": "準2級プラス",
    "source": "大問3B",
    "example": "Consumers can choose to buy avocados with the FAIRTRADE Mark.",
    "distractors": ["生産者", "農家", "輸入業者"],
})
vocab.append({
    "word": "production",
    "meaning": "生産",
    "pos": "名詞",
    "level": "準2級プラス",
    "source": "大問3B",
    "example": "There are several problems with avocado production due to increasing demand.",
    "distractors": ["消費", "輸送", "販売"],
})
vocab.append({
    "word": "plant-based",
    "meaning": "植物ベースの",
    "pos": "形容詞",
    "level": "準2級プラス",
    "source": "大問3B",
    "example": "Their health value is attractive to people whose diets are based on plants.",
    "distractors": ["肉中心の", "砂糖入りの", "加工された"],
})
vocab.append({
    "word": "heart disease",
    "meaning": "心臓病",
    "pos": "名詞句",
    "level": "準2級プラス",
    "source": "大問3B",
    "example": "Researchers say avocados can help reduce the risk of heart disease.",
    "distractors": ["糖尿病", "高血圧", "肥満"],
})
vocab.append({
    "word": "supply",
    "meaning": "供給",
    "pos": "名詞",
    "level": "準2級プラス",
    "source": "大問3B",
    "example": "Too much supply can lead to reduced prices for avocados.",
    "distractors": ["需要", "消費", "廃棄"],
})
vocab.append({
    "word": "responsible",
    "meaning": "責任ある",
    "pos": "形容詞",
    "level": "準2級プラス",
    "source": "大問3B",
    "example": "The industry is working to promote responsible farming for the future.",
    "distractors": ["違法な", "危険な", "一時的な"],
})
vocab.append({
    "word": "FAIRTRADE",
    "meaning": "フェアトレード",
    "pos": "名詞",
    "level": "準2級プラス",
    "source": "大問3B",
    "example": "Consumers can choose avocados with the FAIRTRADE Mark.",
    "distractors": ["有機栽培", "地元産", "割引販売"],
})

assert len(vocab) == 55, f"Expected 55 words, got {len(vocab)}"

data["vocabulary"] = vocab

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Wrote {len(vocab)} vocabulary items to {OUT}")

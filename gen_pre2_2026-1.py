# -*- coding: utf-8 -*-
"""
2026年度 第1回（土曜準会場）英検準2級 data.json 生成スクリプト
Step 1: vocabulary（単語カード・単語クイズ）40語
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "grade-pre2", "2026-1-sat")
OUT = os.path.join(BASE, "data.json")
os.makedirs(BASE, exist_ok=True)

data = {
    "grade": "準2級",
    "year": "2026",
    "session": "1",
    "title": "2026年度 第1回（土曜準会場） 英語資格検定準2級 リーディング",
    "vocabulary": [],
    "sections": [],
    "lessonPlan": {},
}

vocab = []

# ============================================================
# 大問1 正答＋熟語＋重要誤答（17語）
# ============================================================

vocab.append({
    "word": "appealing",
    "meaning": "魅力的な",
    "pos": "形容詞",
    "level": "準2級",
    "example": "The colorful poster looks very appealing to children.",
    "distractors": ["きつい", "退屈な", "かすかな"],
})
vocab.append({
    "word": "appearance",
    "meaning": "外見",
    "pos": "名詞",
    "level": "準2級",
    "example": "She takes great care of her appearance before meetings.",
    "distractors": ["入口", "違い", "知性"],
})
vocab.append({
    "word": "conference",
    "meaning": "会議",
    "pos": "名詞",
    "level": "準2級",
    "example": "The team held a conference to discuss the new plan.",
    "distractors": ["苦情", "記録", "治療"],
})
vocab.append({
    "word": "director",
    "meaning": "監督",
    "pos": "名詞",
    "level": "準2級",
    "example": "The director gave instructions to all the actors.",
    "distractors": ["患者", "甥", "消防士"],
})
vocab.append({
    "word": "insects",
    "meaning": "昆虫",
    "pos": "名詞",
    "level": "準2級",
    "example": "Many insects live in the garden behind our house.",
    "distractors": ["砂漠", "惑星", "幽霊"],
})
vocab.append({
    "word": "promote",
    "meaning": "促進する",
    "pos": "動詞",
    "level": "準2級",
    "example": "The school promotes healthy eating habits among students.",
    "distractors": ["印をつける", "関与させる", "持ち上げる"],
})
vocab.append({
    "word": "awfully",
    "meaning": "とても（強調）",
    "pos": "副詞",
    "level": "準2級",
    "example": "I am awfully sorry for being late.",
    "distractors": ["定期的に", "ほとんど～ない", "優しく"],
})
vocab.append({
    "word": "wondered",
    "meaning": "～かどうか思った",
    "pos": "動詞",
    "level": "準2級",
    "example": "I wondered whether the store would still be open.",
    "distractors": ["思い出した", "返事した", "準備した"],
})
vocab.append({
    "word": "judge",
    "meaning": "判断する",
    "pos": "動詞",
    "level": "準2級",
    "example": "You should not judge people only by their clothes.",
    "distractors": ["発表する", "練習する", "完成させる"],
})
vocab.append({
    "word": "occupied",
    "meaning": "使われている・占有された",
    "pos": "形容詞",
    "level": "準2級",
    "example": "All the seats on the train were occupied.",
    "distractors": ["広がった", "期待された", "考慮された"],
})
vocab.append({
    "word": "in the near future",
    "meaning": "近い将来に",
    "pos": "副詞句",
    "level": "準2級",
    "example": "We plan to move to a bigger house in the near future.",
    "distractors": ["当分の間", "同時に", "昔々"],
})
vocab.append({
    "word": "a sort of",
    "meaning": "一種の",
    "pos": "句",
    "level": "準2級",
    "example": "It was a sort of picnic, but we ate indoors.",
    "distractors": ["一片の", "たくさんの", "二、三の"],
})
vocab.append({
    "word": "known as",
    "meaning": "～として知られている",
    "pos": "句動詞",
    "level": "準2級",
    "example": "Kyoto is known as a city with many temples.",
    "distractors": ["かつて～だった", "～の代金を払った", "～に分けられた"],
})
vocab.append({
    "word": "find fault with",
    "meaning": "～の文句を言う",
    "pos": "句動詞",
    "level": "準2級",
    "example": "My boss always finds fault with my reports.",
    "distractors": ["～を我慢する", "～を楽しみにする", "～に参加する"],
})
vocab.append({
    "word": "help yourself",
    "meaning": "ご自由にどうぞ",
    "pos": "句",
    "level": "準2級",
    "example": "There is cake on the table, so please help yourself.",
    "distractors": ["確かめる", "気をつける", "知り合う"],
})
vocab.append({
    "word": "boring",
    "meaning": "退屈な",
    "pos": "形容詞",
    "level": "準2級",
    "example": "The lecture was so boring that I almost fell asleep.",
    "distractors": ["魅力的な", "きつい", "かすかな"],
})
vocab.append({
    "word": "intelligence",
    "meaning": "知性",
    "pos": "名詞",
    "level": "準2級",
    "example": "She showed great intelligence in solving the puzzle.",
    "distractors": ["外見", "入口", "違い"],
})

# ============================================================
# 大問2 会話完成（5語）
# ============================================================

vocab.append({
    "word": "go straight there",
    "meaning": "まっすぐそこへ行く",
    "pos": "句動詞",
    "level": "準2級",
    "example": "This bus goes straight there without any stops.",
    "distractors": ["たくさん停まる", "より多くの乗客を載せる", "夜遅く運行する"],
})
vocab.append({
    "word": "sticker",
    "meaning": "ステッカー",
    "pos": "名詞",
    "level": "準2級",
    "example": "She put a name sticker on her swim bag.",
    "distractors": ["荷物", "店", "名前"],
})
vocab.append({
    "word": "mountain jacket",
    "meaning": "マウンテンジャケット",
    "pos": "名詞句",
    "level": "準2級",
    "example": "A warm mountain jacket is useful when camping.",
    "distractors": ["バックパック", "水着", "懐中電灯"],
})
vocab.append({
    "word": "arrival area",
    "meaning": "到着エリア",
    "pos": "名詞句",
    "level": "準2級",
    "example": "Please wait for me in the arrival area at the airport.",
    "distractors": ["出発ロビー", "駐車場", "待合室"],
})
vocab.append({
    "word": "pick up",
    "meaning": "取りに来る・受け取る",
    "pos": "句動詞",
    "level": "準2級",
    "example": "I will pick up my package at the store tomorrow.",
    "distractors": ["置き去りにする", "送る", "探す"],
})

# ============================================================
# 大問3「A Lost Dog」（6語）
# ============================================================

vocab.append({
    "word": "poster",
    "meaning": "ポスター",
    "pos": "名詞",
    "level": "準2級",
    "example": "He made posters to find his lost cat.",
    "distractors": ["手紙", "地図", "写真"],
})
vocab.append({
    "word": "nowhere",
    "meaning": "どこにも～ない",
    "pos": "副詞",
    "level": "準2級",
    "example": "I looked everywhere, but my keys were nowhere to be found.",
    "distractors": ["どこでも", "いつも", "すぐに"],
})
vocab.append({
    "word": "accept",
    "meaning": "受け入れる",
    "pos": "動詞",
    "level": "準2級",
    "example": "She had to accept that she could not change the result.",
    "distractors": ["拒否する", "忘れる", "探す"],
})
vocab.append({
    "word": "similar",
    "meaning": "似ている",
    "pos": "形容詞",
    "level": "準2級",
    "example": "Your bag looks similar to mine.",
    "distractors": ["異なる", "新しい", "古い"],
})
vocab.append({
    "word": "hurry",
    "meaning": "急ぐ",
    "pos": "動詞",
    "level": "準2級",
    "example": "We had to hurry to catch the last train.",
    "distractors": ["待つ", "休む", "歩く"],
})
vocab.append({
    "word": "missing",
    "meaning": "行方不明の",
    "pos": "形容詞",
    "level": "準2級",
    "example": "The missing dog was found safe two days later.",
    "distractors": ["安全な", "元気な", "眠っている"],
})

# ============================================================
# 大問4 リーディング（12語）
# ============================================================

vocab.append({
    "word": "opportunity",
    "meaning": "機会",
    "pos": "名詞",
    "level": "準2級",
    "example": "This job is a great opportunity to learn new skills.",
    "distractors": ["問題", "責任", "約束"],
})
vocab.append({
    "word": "interview",
    "meaning": "面接",
    "pos": "名詞",
    "level": "準2級",
    "example": "She has an online interview next Monday.",
    "distractors": ["試験", "会議", "旅行"],
})
vocab.append({
    "word": "equipment",
    "meaning": "装備・器材",
    "pos": "名詞",
    "level": "準2級",
    "example": "You can rent skiing equipment at the resort.",
    "distractors": ["食事", "部屋", "地図"],
})
vocab.append({
    "word": "cafeteria",
    "meaning": "食堂",
    "pos": "名詞",
    "level": "準2級",
    "example": "Students eat lunch in the school cafeteria.",
    "distractors": ["図書館", "教室", "事務所"],
})
vocab.append({
    "word": "freely",
    "meaning": "自由に",
    "pos": "副詞",
    "level": "準2級",
    "example": "On days off, you can use the rest of the week freely.",
    "distractors": ["速く", "静かに", "慎重に"],
})
vocab.append({
    "word": "mental health",
    "meaning": "精神的健康",
    "pos": "名詞句",
    "level": "準2級",
    "example": "Talking with friends is good for your mental health.",
    "distractors": ["身体的健康", "食生活", "睡眠"],
})
vocab.append({
    "word": "social media",
    "meaning": "ソーシャルメディア",
    "pos": "名詞",
    "level": "準2級",
    "example": "Many teenagers use social media every day.",
    "distractors": ["新聞", "テレビ", "ラジオ"],
})
vocab.append({
    "word": "influence",
    "meaning": "影響を与える",
    "pos": "動詞",
    "level": "準2級",
    "example": "Good teachers can positively influence their students.",
    "distractors": ["妨げる", "無視する", "拒否する"],
})
vocab.append({
    "word": "accepted",
    "meaning": "受け入れられた",
    "pos": "形容詞",
    "level": "準2級",
    "example": "She felt accepted by her new classmates.",
    "distractors": ["拒否された", "忘れられた", "批判された"],
})
vocab.append({
    "word": "connected",
    "meaning": "つながった",
    "pos": "形容詞",
    "level": "準2級",
    "example": "Online groups help people feel connected to others.",
    "distractors": ["孤立した", "混乱した", "疲れた"],
})
vocab.append({
    "word": "expert",
    "meaning": "専門家",
    "pos": "名詞",
    "level": "準2級",
    "example": "You should get advice from an expert in the field.",
    "distractors": ["学生", "初心者", "観光客"],
})
vocab.append({
    "word": "professional",
    "meaning": "専門的な",
    "pos": "形容詞",
    "level": "準2級",
    "example": "Only professional advice should be trusted for health issues.",
    "distractors": ["個人的な", "古い", "無料の"],
})

assert len(vocab) == 40, f"Expected 40 words, got {len(vocab)}"

data["vocabulary"] = vocab

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Wrote {len(vocab)} vocabulary items to {OUT}")

# -*- coding: utf-8 -*-
"""
2026年度 第1回（準会場）英検2級 data.json 生成スクリプト
Step 1: vocabulary（単語カード・単語クイズ）
"""
import json, os

data = {
    "grade": "2級",
    "year": "2026",
    "session": "1-sat",
    "title": "2026年度 第1回（準会場）英語資格検定2級 リーディング",
    "vocabulary": [],
    "sections": [],
    "lessonPlan": {}
}

vocab = []

# ============================================================
# 大問1 正答＋重要誤答（25語）
# ============================================================

# --- Q1: incidents(正答3), arguments(誤1), outcomes(誤4) ---
vocab.append({
    "word": "incident",
    "meaning": "出来事、事件",
    "pos": "名詞",
    "level": "2級",
    "example": "There was a minor incident at the station this morning.",
    "distractors": ["口論", "結果", "印象"]
})
vocab.append({
    "word": "argument",
    "meaning": "口論、議論",
    "pos": "名詞",
    "level": "2級",
    "example": "They had a heated argument about the new policy.",
    "distractors": ["出来事", "結果", "印象"]
})
vocab.append({
    "word": "outcome",
    "meaning": "結果、成果",
    "pos": "名詞",
    "level": "2級",
    "example": "The outcome of the experiment was surprising.",
    "distractors": ["出来事", "口論", "印象"]
})

# --- Q2: quantity(正答2), sacrifice(誤3), achievement(誤4) ---
vocab.append({
    "word": "quantity",
    "meaning": "量",
    "pos": "名詞",
    "level": "2級",
    "example": "We need a large quantity of paper for the project.",
    "distractors": ["犠牲", "業績", "目的地"]
})
vocab.append({
    "word": "sacrifice",
    "meaning": "犠牲、犠牲にする",
    "pos": "名詞",
    "level": "2級",
    "example": "She made a great sacrifice for her family.",
    "distractors": ["量", "業績", "目的地"]
})

# --- Q3: stir(正答3), resemble(誤2) ---
vocab.append({
    "word": "stir",
    "meaning": "かき混ぜる",
    "pos": "動詞",
    "level": "2級",
    "example": "Please stir the sauce so it doesn't burn.",
    "distractors": ["こぼす", "似ている", "楽しませる"]
})
vocab.append({
    "word": "resemble",
    "meaning": "〜に似ている",
    "pos": "動詞",
    "level": "2級",
    "example": "She closely resembles her older sister.",
    "distractors": ["かき混ぜる", "こぼす", "楽しませる"]
})

# --- Q4: favored(正答3) ---
vocab.append({
    "word": "favor",
    "meaning": "好む、支持する",
    "pos": "動詞",
    "level": "2級",
    "example": "Most customers favor this brand over others.",
    "distractors": ["脅かす", "増やす", "救出する"]
})

# --- Q5: cables(正答1) ---
vocab.append({
    "word": "cable",
    "meaning": "ケーブル、電線",
    "pos": "名詞",
    "level": "2級",
    "example": "The internet cable was damaged during the storm.",
    "distractors": ["跳躍", "雑誌", "調査"]
})

# --- Q6: appreciation(正答3), preference(誤1) ---
vocab.append({
    "word": "appreciation",
    "meaning": "感謝、鑑賞",
    "pos": "名詞",
    "level": "2級",
    "example": "I want to express my appreciation for your help.",
    "distractors": ["好み", "勝利", "失望"]
})
vocab.append({
    "word": "preference",
    "meaning": "好み、選好",
    "pos": "名詞",
    "level": "2級",
    "example": "Do you have any preference for the seating arrangement?",
    "distractors": ["感謝", "勝利", "失望"]
})

# --- Q7: scolded(正答3), detected(誤1) ---
vocab.append({
    "word": "scold",
    "meaning": "叱る",
    "pos": "動詞",
    "level": "2級",
    "example": "The mother scolded her child for lying.",
    "distractors": ["検出する", "感染させる", "つかむ"]
})
vocab.append({
    "word": "detect",
    "meaning": "検出する、発見する",
    "pos": "動詞",
    "level": "2級",
    "example": "The sensor can detect small changes in temperature.",
    "distractors": ["叱る", "感染させる", "つかむ"]
})

# --- Q8: estimate(正答1), decline(誤2), neglect(誤4) ---
vocab.append({
    "word": "estimate",
    "meaning": "見積もる、推定する",
    "pos": "動詞",
    "level": "2級",
    "example": "It is difficult to estimate the total cost at this point.",
    "distractors": ["断る", "刺激する", "怠る"]
})
vocab.append({
    "word": "decline",
    "meaning": "断る、減少する",
    "pos": "動詞",
    "level": "2級",
    "example": "She politely declined the invitation to dinner.",
    "distractors": ["見積もる", "刺激する", "怠る"]
})
vocab.append({
    "word": "neglect",
    "meaning": "怠る、無視する",
    "pos": "動詞",
    "level": "2級",
    "example": "Don't neglect your health even when you are busy.",
    "distractors": ["見積もる", "断る", "刺激する"]
})

# --- Q9: patiently(正答4) ---
vocab.append({
    "word": "patiently",
    "meaning": "辛抱強く",
    "pos": "副詞",
    "level": "2級",
    "example": "She waited patiently for her turn at the hospital.",
    "distractors": ["合法的に", "大まかに", "かろうじて"]
})

# --- Q10: current(正答3) ---
vocab.append({
    "word": "current",
    "meaning": "現在の、今の",
    "pos": "形容詞",
    "level": "2級",
    "example": "What is the current status of the project?",
    "distractors": ["否定的な", "不在の", "突然の"]
})

# --- Q11: Up until now(正答3) ---
vocab.append({
    "word": "up until now",
    "meaning": "今まで、これまでずっと",
    "pos": "熟語",
    "level": "2級",
    "example": "Up until now, I have never traveled abroad.",
    "distractors": ["途中で", "結局は", "〜のために"]
})

# --- Q12: Needless to say(正答3) ---
vocab.append({
    "word": "needless to say",
    "meaning": "言うまでもなく",
    "pos": "熟語",
    "level": "2級",
    "example": "Needless to say, practice is the key to improvement.",
    "distractors": ["それどころか", "念のために", "言い換えれば"]
})

# --- Q13: lose one's temper(正答4) ---
vocab.append({
    "word": "lose one's temper",
    "meaning": "かっとなる、怒りを抑えられなくなる",
    "pos": "熟語",
    "level": "2級",
    "example": "He tends to lose his temper when things don't go well.",
    "distractors": ["道を切り開く", "息を止める", "〜の代わりをする"]
})

# --- Q14: keep one's fingers crossed(正答2) ---
vocab.append({
    "word": "keep one's fingers crossed",
    "meaning": "幸運を祈る、うまくいくよう願う",
    "pos": "熟語",
    "level": "2級",
    "example": "I'm keeping my fingers crossed for good weather tomorrow.",
    "distractors": ["手に入る", "息をのむ", "決心する"]
})

# --- Q15: confident of(正答3) ---
vocab.append({
    "word": "confident of",
    "meaning": "〜に自信がある",
    "pos": "熟語",
    "level": "2級",
    "example": "She is confident of passing the entrance exam.",
    "distractors": ["〜を申し訳なく思う", "〜に似ている", "〜にうんざりしている"]
})

# --- Q16: keep to(正答1) ---
vocab.append({
    "word": "keep to",
    "meaning": "〜に従う、〜から離れない",
    "pos": "句動詞",
    "level": "2級",
    "example": "Visitors should keep to the main path in the park.",
    "distractors": ["引き渡す", "やり遂げる", "横になる"]
})

# --- Q17: effect on(正答1) ---
vocab.append({
    "word": "effect on",
    "meaning": "〜への影響",
    "pos": "熟語",
    "level": "2級",
    "example": "Lack of sleep can have a negative effect on your health.",
    "distractors": ["〜との比較", "〜に対する責任", "〜に対する反応"]
})

# ============================================================
# 大問2A "Child-Friendly City" パッセージからの重要語（11語）
# ============================================================

vocab.append({
    "word": "effort",
    "meaning": "努力、取り組み",
    "pos": "名詞",
    "level": "2級",
    "example": "Their effort to reduce waste has been very successful.",
    "distractors": ["目標", "計画", "報酬"]
})
vocab.append({
    "word": "surround",
    "meaning": "取り囲む",
    "pos": "動詞",
    "level": "2級",
    "example": "Beautiful mountains surround the small village.",
    "distractors": ["支える", "妨げる", "導く"]
})
vocab.append({
    "word": "trial",
    "meaning": "試み、試験",
    "pos": "名詞",
    "level": "2級",
    "example": "The new medicine is currently in a clinical trial.",
    "distractors": ["許可", "条件", "発表"]
})
vocab.append({
    "word": "permanently",
    "meaning": "永久に、恒久的に",
    "pos": "副詞",
    "level": "2級",
    "example": "The exhibit will be permanently displayed at the museum.",
    "distractors": ["一時的に", "定期的に", "部分的に"]
})
vocab.append({
    "word": "indicate",
    "meaning": "示す、指し示す",
    "pos": "動詞",
    "level": "2級",
    "example": "The sign indicates the direction to the exit.",
    "distractors": ["設計する", "記録する", "除外する"]
})
vocab.append({
    "word": "observation",
    "meaning": "観察、意見",
    "pos": "名詞",
    "level": "2級",
    "example": "His careful observation led to an important discovery.",
    "distractors": ["比較", "仮定", "紹介"]
})
vocab.append({
    "word": "urban",
    "meaning": "都市の",
    "pos": "形容詞",
    "level": "2級",
    "example": "Urban areas tend to have more public transportation.",
    "distractors": ["農村の", "沿岸の", "産業の"]
})
vocab.append({
    "word": "improvement",
    "meaning": "改善、向上",
    "pos": "名詞",
    "level": "2級",
    "example": "There has been a great improvement in air quality.",
    "distractors": ["悪化", "維持", "削減"]
})
vocab.append({
    "word": "reflect",
    "meaning": "反映する、映す",
    "pos": "動詞",
    "level": "2級",
    "example": "The results reflect the hard work of the entire team.",
    "distractors": ["無視する", "中断する", "分類する"]
})
vocab.append({
    "word": "community",
    "meaning": "地域社会、コミュニティ",
    "pos": "名詞",
    "level": "2級",
    "example": "The community came together to clean up the park.",
    "distractors": ["委員会", "企業", "施設"]
})
vocab.append({
    "word": "ban",
    "meaning": "禁止する",
    "pos": "動詞",
    "level": "2級",
    "example": "The city decided to ban smoking in public places.",
    "distractors": ["許可する", "奨励する", "制限する"]
})

# ============================================================
# 大問2B "Dead Trees" パッセージからの重要語（10語）
# ============================================================

vocab.append({
    "word": "habitat",
    "meaning": "生息地",
    "pos": "名詞",
    "level": "2級",
    "example": "The forest provides a natural habitat for many species.",
    "distractors": ["食物連鎖", "気候", "生態系"]
})
vocab.append({
    "word": "creature",
    "meaning": "生き物",
    "pos": "名詞",
    "level": "2級",
    "example": "Many strange creatures live deep in the ocean.",
    "distractors": ["植物", "化石", "細胞"]
})
vocab.append({
    "word": "absorb",
    "meaning": "吸収する",
    "pos": "動詞",
    "level": "2級",
    "example": "Plants absorb sunlight to produce energy.",
    "distractors": ["排出する", "蓄積する", "分解する"]
})
vocab.append({
    "word": "substance",
    "meaning": "物質",
    "pos": "名詞",
    "level": "2級",
    "example": "This substance is harmful if swallowed.",
    "distractors": ["表面", "構造", "現象"]
})
vocab.append({
    "word": "moisture",
    "meaning": "湿気、水分",
    "pos": "名詞",
    "level": "2級",
    "example": "The plants need moisture to grow properly.",
    "distractors": ["日光", "温度", "圧力"]
})
vocab.append({
    "word": "eventually",
    "meaning": "最終的に、結局",
    "pos": "副詞",
    "level": "2級",
    "example": "She eventually decided to accept the job offer.",
    "distractors": ["直ちに", "頻繁に", "めったに〜ない"]
})
vocab.append({
    "word": "bark",
    "meaning": "樹皮",
    "pos": "名詞",
    "level": "2級",
    "example": "The bark of this tree is rough and thick.",
    "distractors": ["枝", "根", "種"]
})
vocab.append({
    "word": "element",
    "meaning": "要素、元素",
    "pos": "名詞",
    "level": "2級",
    "example": "Teamwork is an essential element of success.",
    "distractors": ["段階", "原因", "基準"]
})
vocab.append({
    "word": "maintain",
    "meaning": "維持する、保つ",
    "pos": "動詞",
    "level": "2級",
    "example": "It is important to maintain a healthy diet.",
    "distractors": ["削減する", "変更する", "中止する"]
})
vocab.append({
    "word": "cycle",
    "meaning": "循環、周期",
    "pos": "名詞",
    "level": "2級",
    "example": "The water cycle is an important part of nature.",
    "distractors": ["原理", "傾向", "過程"]
})

# ============================================================
# 大問3A "Email（工場見学）" パッセージからの重要語（5語）
# ============================================================

vocab.append({
    "word": "manufacturing",
    "meaning": "製造、製造業",
    "pos": "名詞",
    "level": "2級",
    "example": "The manufacturing of electric cars is increasing rapidly.",
    "distractors": ["流通", "広告", "輸入"]
})
vocab.append({
    "word": "impress",
    "meaning": "感動させる、印象づける",
    "pos": "動詞",
    "level": "2級",
    "example": "Her presentation really impressed the audience.",
    "distractors": ["混乱させる", "退屈させる", "怒らせる"]
})
vocab.append({
    "word": "research",
    "meaning": "調査、研究",
    "pos": "名詞",
    "level": "2級",
    "example": "He spent months doing research for his paper.",
    "distractors": ["実験", "講義", "議論"]
})
vocab.append({
    "word": "permit",
    "meaning": "許可する",
    "pos": "動詞",
    "level": "2級",
    "example": "Photography is not permitted inside the building.",
    "distractors": ["禁止する", "要求する", "推薦する"]
})
vocab.append({
    "word": "consideration",
    "meaning": "配慮、考慮",
    "pos": "名詞",
    "level": "2級",
    "example": "Thank you for your kind consideration.",
    "distractors": ["説明", "確認", "提案"]
})

# ============================================================
# 大問3B "The Lost City" パッセージからの重要語（10語）
# ============================================================

vocab.append({
    "word": "conveniently",
    "meaning": "便利に、都合よく",
    "pos": "副詞",
    "level": "2級",
    "example": "The hotel is conveniently located near the station.",
    "distractors": ["不便に", "偶然に", "正式に"]
})
vocab.append({
    "word": "restore",
    "meaning": "回復する、修復する",
    "pos": "動詞",
    "level": "2級",
    "example": "They plan to restore the old castle to its original state.",
    "distractors": ["破壊する", "移転する", "拡張する"]
})
vocab.append({
    "word": "ancient",
    "meaning": "古代の、大昔の",
    "pos": "形容詞",
    "level": "2級",
    "example": "Archaeologists discovered an ancient temple in the desert.",
    "distractors": ["現代の", "中世の", "最近の"]
})
vocab.append({
    "word": "collapse",
    "meaning": "崩壊する、崩れる",
    "pos": "動詞",
    "level": "2級",
    "example": "The bridge collapsed after the earthquake.",
    "distractors": ["建設する", "拡大する", "固定する"]
})
vocab.append({
    "word": "gradually",
    "meaning": "徐々に、だんだんと",
    "pos": "副詞",
    "level": "2級",
    "example": "The temperature gradually increased throughout the day.",
    "distractors": ["急激に", "完全に", "わずかに"]
})
vocab.append({
    "word": "investigation",
    "meaning": "調査、捜査",
    "pos": "名詞",
    "level": "2級",
    "example": "The police began an investigation into the case.",
    "distractors": ["交渉", "声明", "指示"]
})
vocab.append({
    "word": "sculpture",
    "meaning": "彫刻",
    "pos": "名詞",
    "level": "2級",
    "example": "A beautiful marble sculpture stands in the park.",
    "distractors": ["建築", "絵画", "陶芸"]
})
vocab.append({
    "word": "underwater",
    "meaning": "水中の、海中の",
    "pos": "形容詞",
    "level": "2級",
    "example": "Underwater photography requires special equipment.",
    "distractors": ["地上の", "空中の", "地下の"]
})
vocab.append({
    "word": "explore",
    "meaning": "探検する、調査する",
    "pos": "動詞",
    "level": "2級",
    "example": "We explored the caves along the coastline.",
    "distractors": ["避難する", "占領する", "観察する"]
})
vocab.append({
    "word": "ruins",
    "meaning": "遺跡、廃墟",
    "pos": "名詞",
    "level": "2級",
    "example": "Tourists visit the ancient ruins every year.",
    "distractors": ["港", "城壁", "記念碑"]
})

# ============================================================
# wordAudio パス付与 & 保存
# ============================================================

for i, v in enumerate(vocab):
    safe_word = v['word'].replace(' ', '_').replace("'", '').lower()
    v["wordAudio"] = f"audio/vocab/w_{i+1:03d}_{safe_word}.mp3"

data["vocabulary"] = vocab

# 保存先
output_dir = r"G:\マイドライブ\ReadPass Pro\data\grade2\2026-1-sat"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "data.json")

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"✅ 保存完了: {output_path}")
print(f"   語彙数: {len(vocab)}")

# 出典別カウント
p1 = [v for v in vocab[:25]]
p2a = [v for v in vocab[25:36]]
p2b = [v for v in vocab[36:46]]
p3a = [v for v in vocab[46:51]]
p3b = [v for v in vocab[51:]]
print(f"   大問1: {len(p1)}語")
print(f"   大問2A: {len(p2a)}語")
print(f"   大問2B: {len(p2b)}語")
print(f"   大問3A: {len(p3a)}語")
print(f"   大問3B: {len(p3b)}語")

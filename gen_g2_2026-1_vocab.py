# -*- coding: utf-8 -*-
"""
2026年度 第1回（本会場）英検2級 data.json
Step: vocabulary（単語カード・単語クイズ）61語
一次ソース: 2026-1(本会場）/2級.pdf
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade2", "2026-1",
)
OUT = os.path.join(BASE, "data.json")

with open(OUT, encoding="utf-8") as f:
    data = json.load(f)

vocab = []

# ============================================================
# 大問1 正答＋重要誤答（25語）
# ============================================================

# --- Q1: bride(正答4), lawyer(誤1), surgeon(誤3) ---
vocab.append({
    "word": "bride",
    "meaning": "花嫁",
    "pos": "名詞",
    "level": "2級",
    "source": "大問1",
    "example": "In many countries, the bride wears a white dress at a wedding.",
    "distractors": ["弁護士", "戦士", "外科医"],
})
vocab.append({
    "word": "lawyer",
    "meaning": "弁護士",
    "pos": "名詞",
    "level": "2級",
    "source": "大問1",
    "example": "She decided to consult a lawyer before signing the contract.",
    "distractors": ["花嫁", "戦士", "外科医"],
})
vocab.append({
    "word": "surgeon",
    "meaning": "外科医",
    "pos": "名詞",
    "level": "2級",
    "source": "大問1",
    "example": "The surgeon performed the operation successfully.",
    "distractors": ["花嫁", "弁護士", "戦士"],
})

# --- Q2: globe(正答2), branch(誤1) ---
vocab.append({
    "word": "globe",
    "meaning": "地球儀",
    "pos": "名詞",
    "level": "2級",
    "source": "大問1",
    "example": "The teacher asked her students to find Argentina on a globe.",
    "distractors": ["枝", "はかり", "小道"],
})
vocab.append({
    "word": "branch",
    "meaning": "枝、支店",
    "pos": "名詞",
    "level": "2級",
    "source": "大問1",
    "example": "A bird was sitting on a branch of the tree.",
    "distractors": ["地球儀", "はかり", "小道"],
})

# --- Q3: difficulty(正答3), glory(誤1) ---
vocab.append({
    "word": "difficulty",
    "meaning": "困難、難しさ",
    "pos": "名詞",
    "level": "2級",
    "source": "大問1",
    "example": "She can already read the newspaper without any difficulty.",
    "distractors": ["栄光", "バランス", "優先事項"],
})
vocab.append({
    "word": "glory",
    "meaning": "栄光、名誉",
    "pos": "名詞",
    "level": "2級",
    "source": "大問1",
    "example": "The team returned home in glory after winning the championship.",
    "distractors": ["困難", "バランス", "優先事項"],
})

# --- Q4: tendency(正答1), discrimination(誤2) ---
vocab.append({
    "word": "tendency",
    "meaning": "傾向",
    "pos": "名詞",
    "level": "2級",
    "source": "大問1",
    "example": "You have a tendency to be quiet when you're worried.",
    "distractors": ["差別", "避難所", "内容"],
})
vocab.append({
    "word": "discrimination",
    "meaning": "差別",
    "pos": "名詞",
    "level": "2級",
    "source": "大問1",
    "example": "The law prohibits discrimination based on age or gender.",
    "distractors": ["傾向", "避難所", "内容"],
})

# --- Q5: foster(正答2) ---
vocab.append({
    "word": "foster",
    "meaning": "育む、促進する",
    "pos": "動詞",
    "level": "2級",
    "source": "大問1",
    "example": "Teachers try to foster leadership qualities in their students.",
    "distractors": ["憎む", "分ける", "発音する"],
})

# --- Q6: typical(正答3), gradual(誤1) ---
vocab.append({
    "word": "typical",
    "meaning": "典型的な、いつもの",
    "pos": "形容詞",
    "level": "2級",
    "source": "大問1",
    "example": "On a typical Saturday night, they order pizza and watch TV together.",
    "distractors": ["徐々の", "化学の", "偽の"],
})
vocab.append({
    "word": "gradual",
    "meaning": "徐々の、漸進的な",
    "pos": "形容詞",
    "level": "2級",
    "source": "大問1",
    "example": "There has been a gradual improvement in her English skills.",
    "distractors": ["典型的な", "化学の", "偽の"],
})

# --- Q7: weep(正答4), occur(誤1) ---
vocab.append({
    "word": "weep",
    "meaning": "泣く",
    "pos": "動詞",
    "level": "2級",
    "source": "大問1",
    "example": "When the movie ended, many people in the theater began to weep.",
    "distractors": ["起こる", "膨らむ", "軽くたたく"],
})
vocab.append({
    "word": "occur",
    "meaning": "起こる、生じる",
    "pos": "動詞",
    "level": "2級",
    "source": "大問1",
    "example": "The accident occurred near the station.",
    "distractors": ["泣く", "膨らむ", "軽くたたく"],
})

# --- Q8: illustrate(正答3), occupy(誤1) ---
vocab.append({
    "word": "illustrate",
    "meaning": "説明する、図解する",
    "pos": "動詞",
    "level": "2級",
    "source": "大問1",
    "example": "He wanted to illustrate how cells work.",
    "distractors": ["占める", "磨く", "祝う"],
})
vocab.append({
    "word": "occupy",
    "meaning": "占める、占領する",
    "pos": "動詞",
    "level": "2級",
    "source": "大問1",
    "example": "The new building will occupy the empty lot downtown.",
    "distractors": ["説明する", "磨く", "祝う"],
})

# --- Q9: barely(正答3) ---
vocab.append({
    "word": "barely",
    "meaning": "かろうじて、ほとんど〜ない",
    "pos": "副詞",
    "level": "2級",
    "source": "大問1",
    "example": "The Green Wolves barely won when they scored a goal in the last seconds.",
    "distractors": ["こっそり", "優しく", "繰り返し"],
})

# --- Q10: frowned(正答1) ---
vocab.append({
    "word": "frown",
    "meaning": "眉をひそめる",
    "pos": "動詞",
    "level": "2級",
    "source": "大問1",
    "example": "When the teacher said there would be a test next week, the students frowned.",
    "distractors": ["滑る", "推測する", "這う"],
})

# --- Q11: As a general rule(正答4) ---
vocab.append({
    "word": "as a general rule",
    "meaning": "一般に、概して",
    "pos": "熟語",
    "level": "2級",
    "source": "大問1",
    "example": "As a general rule, people should drink eight glasses of water a day.",
    "distractors": ["新たな始まりに", "特定の機会に", "緊急の場合に"],
})

# --- Q12: on his own(正答4) ---
vocab.append({
    "word": "on his own",
    "meaning": "一人で、自力で",
    "pos": "熟語",
    "level": "2級",
    "source": "大問1",
    "example": "Now he has to do everything on his own, like cooking and cleaning.",
    "distractors": ["放送中で", "離れて", "驚いたことに"],
})

# --- Q13: go along with(正答2) ---
vocab.append({
    "word": "go along with",
    "meaning": "〜に賛成する、〜に従う",
    "pos": "熟語",
    "level": "2級",
    "source": "大問1",
    "example": "The president said that he could not go along with the plan to expand the office.",
    "distractors": ["奪い去る", "引き出す", "注意する"],
})

# --- Q14: a series of(正答1) ---
vocab.append({
    "word": "a series of",
    "meaning": "一連の",
    "pos": "熟語",
    "level": "2級",
    "source": "大問1",
    "example": "After a series of tests, the doctors discovered that he had a rare illness.",
    "distractors": ["〜の端", "〜の一員", "〜の裏側"],
})

# --- Q15: In other words(正答1) ---
vocab.append({
    "word": "in other words",
    "meaning": "言い換えれば",
    "pos": "熟語",
    "level": "2級",
    "source": "大問1",
    "example": "In other words, we are going to be very busy!",
    "distractors": ["最初に", "行ったり来たり", "それどころか"],
})

# --- Q16: distinct from(正答1) ---
vocab.append({
    "word": "distinct from",
    "meaning": "〜と明確に異なる",
    "pos": "熟語",
    "level": "2級",
    "source": "大問1",
    "example": "The two paintings looked distinct from each other at first.",
    "distractors": ["〜で構成された", "〜から欠席している", "〜を脅かす"],
})

# --- Q17: lay off(正答2) ---
vocab.append({
    "word": "lay off",
    "meaning": "解雇する",
    "pos": "熟語",
    "level": "2級",
    "source": "大問1",
    "example": "The company had to lay off some of its workers because it was losing money.",
    "distractors": ["ひっくり返す", "引き起こす", "追いつく"],
})

# ============================================================
# 大問2A "Efforts at a Village" パッセージからの重要語（11語）
# ============================================================

vocab.append({
    "word": "rural",
    "meaning": "田舎の、農村の",
    "pos": "形容詞",
    "level": "2級",
    "source": "大問2A",
    "example": "El Pital is a rural village in Honduras.",
    "distractors": ["都市の", "沿岸の", "工業の"],
})
vocab.append({
    "word": "literacy",
    "meaning": "読み書き能力",
    "pos": "名詞",
    "level": "2級",
    "source": "大問2A",
    "example": "Literacy rates were low in the community.",
    "distractors": ["識字率調査", "入学率", "卒業証書"],
})
vocab.append({
    "word": "motivate",
    "meaning": "動機づける、やる気を起こさせる",
    "pos": "動詞",
    "level": "2級",
    "source": "大問2A",
    "example": "Motivated by this, children began writing stories.",
    "distractors": ["禁止する", "無視する", "批判する"],
})
vocab.append({
    "word": "costume",
    "meaning": "衣装、仮装",
    "pos": "名詞",
    "level": "2級",
    "source": "大問2A",
    "example": "Costumes were created, rumors were spread, and dramatic scenes were performed.",
    "distractors": ["道具", "舞台", "脚本"],
})
vocab.append({
    "word": "rumor",
    "meaning": "うわさ、噂",
    "pos": "名詞",
    "level": "2級",
    "source": "大問2A",
    "example": "Rumors were spread to make children believe that Bibliobandido was real.",
    "distractors": ["事実", "報告", "証拠"],
})
vocab.append({
    "word": "dramatic",
    "meaning": "劇的な、印象的な",
    "pos": "形容詞",
    "level": "2級",
    "source": "大問2A",
    "example": "Dramatic scenes were performed to bring him to life.",
    "distractors": ["静かな", "平凡な", "単調な"],
})
vocab.append({
    "word": "community",
    "meaning": "地域社会、共同体",
    "pos": "名詞",
    "level": "2級",
    "source": "大問2A",
    "example": "This activity turned a writing task into an exciting community event.",
    "distractors": ["委員会", "政府", "市場"],
})
vocab.append({
    "word": "spread",
    "meaning": "広がる、広める",
    "pos": "動詞",
    "level": "2級",
    "source": "大問2A",
    "example": "The story of Bibliobandido spread to other places.",
    "distractors": ["縮小する", "隠す", "中止する"],
})
vocab.append({
    "word": "superhero",
    "meaning": "スーパーヒーロー",
    "pos": "名詞",
    "level": "2級",
    "source": "大問2A",
    "example": "La Dama Violeta was created as a subway superhero.",
    "distractors": ["悪役", "観光客", "司書"],
})
vocab.append({
    "word": "creative",
    "meaning": "創造的な",
    "pos": "形容詞",
    "level": "2級",
    "source": "大問2A",
    "example": "This character added a creative twist to public reading while traveling.",
    "distractors": ["伝統的な", "消極的な", "形式的な"],
})
vocab.append({
    "word": "starve",
    "meaning": "飢える、餓死する",
    "pos": "動詞",
    "level": "2級",
    "source": "大問2A",
    "example": "Children were asked to create new stories so that he would not starve.",
    "distractors": ["眠る", "逃げる", "笑う"],
})

# ============================================================
# 大問2B "The Science of Fear" パッセージからの重要語（10語）
# ============================================================

vocab.append({
    "word": "emotion",
    "meaning": "感情",
    "pos": "名詞",
    "level": "2級",
    "source": "大問2B",
    "example": "Fear is a natural emotion that helps protect people from danger.",
    "distractors": ["理性", "記憶", "反射"],
})
vocab.append({
    "word": "dangerous",
    "meaning": "危険な",
    "pos": "形容詞",
    "level": "2級",
    "source": "大問2B",
    "example": "When people see dangerous animals, fear quickly makes the brain react.",
    "distractors": ["安全な", "穏やかな", "普通の"],
})
vocab.append({
    "word": "breathing",
    "meaning": "呼吸",
    "pos": "名詞",
    "level": "2級",
    "source": "大問2B",
    "example": "This reaction causes changes such as quicker breathing and tense muscles.",
    "distractors": ["心拍", "体温", "血圧"],
})
vocab.append({
    "word": "muscle",
    "meaning": "筋肉",
    "pos": "名詞",
    "level": "2級",
    "source": "大問2B",
    "example": "Fear causes quicker breathing and tense muscles.",
    "distractors": ["骨", "神経", "皮膚"],
})
vocab.append({
    "word": "fight-or-flight",
    "meaning": "闘争・逃走反応",
    "pos": "名詞句",
    "level": "2級",
    "source": "大問2B",
    "example": "This is called the fight-or-flight response to fear or stress.",
    "distractors": ["睡眠反応", "消化反応", "免疫反応"],
})
vocab.append({
    "word": "fascinated",
    "meaning": "夢中になった、強く引かれた",
    "pos": "形容詞",
    "level": "2級",
    "source": "大問2B",
    "example": "Some people are even fascinated by this feeling.",
    "distractors": ["恐怖した", "退屈した", "混乱した"],
})
vocab.append({
    "word": "intensely",
    "meaning": "激しく、強く",
    "pos": "副詞",
    "level": "2級",
    "source": "大問2B",
    "example": "Some people feel fear too often or too intensely.",
    "distractors": ["穏やかに", "わずかに", "偶然に"],
})
vocab.append({
    "word": "overwhelming",
    "meaning": "圧倒的な、手に負えない",
    "pos": "形容詞",
    "level": "2級",
    "source": "大問2B",
    "example": "This intense fear can make everyday activities feel overwhelming.",
    "distractors": ["簡単な", "退屈な", "軽微な"],
})
vocab.append({
    "word": "mechanism",
    "meaning": "仕組み、機構",
    "pos": "名詞",
    "level": "2級",
    "source": "大問2B",
    "example": "Recent studies have identified specific brain mechanisms that allow people to control learned fears.",
    "distractors": ["症状", "治療法", "診断"],
})
vocab.append({
    "word": "treatment",
    "meaning": "治療、処置",
    "pos": "名詞",
    "level": "2級",
    "source": "大問2B",
    "example": "The research offers hope for more effective treatments.",
    "distractors": ["予防", "検査", "診断"],
})

# ============================================================
# 大問3A "Your service" パッセージからの重要語（5語）
# ============================================================

vocab.append({
    "word": "facility",
    "meaning": "施設",
    "pos": "名詞",
    "level": "2級",
    "source": "大問3A",
    "example": "We are looking for an outdoor facility where we can hold an athletic event.",
    "distractors": ["道具", "許可証", "契約書"],
})
vocab.append({
    "word": "athletic",
    "meaning": "運動の、体育の",
    "pos": "形容詞",
    "level": "2級",
    "source": "大問3A",
    "example": "Our athletic event will take place on a weekday in September or October.",
    "distractors": ["学術的な", "音楽の", "科学の"],
})
vocab.append({
    "word": "coworker",
    "meaning": "同僚",
    "pos": "名詞",
    "level": "2級",
    "source": "大問3A",
    "example": "One of my coworkers recommended your facility and suggested I contact you.",
    "distractors": ["上司", "顧客", "隣人"],
})
vocab.append({
    "word": "access",
    "meaning": "アクセス、接近",
    "pos": "名詞",
    "level": "2級",
    "source": "大問3A",
    "example": "Your facility is appealing because it is easy to access from several train stations.",
    "distractors": ["料金", "規模", "装飾"],
})
vocab.append({
    "word": "suitable",
    "meaning": "適した、ふさわしい",
    "pos": "形容詞",
    "level": "2級",
    "source": "大問3A",
    "example": "Could you please let me know which date might be suitable for our event?",
    "distractors": ["高価な", "遠い", "狭い"],
})

# ============================================================
# 大問3B "The Humboldt Brothers" パッセージからの重要語（10語）
# ============================================================

vocab.append({
    "word": "wealthy",
    "meaning": "裕福な",
    "pos": "形容詞",
    "level": "2級",
    "source": "大問3B",
    "example": "They were born into a wealthy family.",
    "distractors": ["貧しい", "有名な", "厳格な"],
})
vocab.append({
    "word": "adventure",
    "meaning": "冒険",
    "pos": "名詞",
    "level": "2級",
    "source": "大問3B",
    "example": "Alexander had been deeply interested in adventure since early childhood.",
    "distractors": ["研究", "教育", "政治"],
})
vocab.append({
    "word": "tutor",
    "meaning": "家庭教師、個別指導する",
    "pos": "名詞",
    "level": "2級",
    "source": "大問3B",
    "example": "She hired famous educators and experts in various fields to tutor them.",
    "distractors": ["秘書", "管理人", "観光客"],
})
vocab.append({
    "word": "proposal",
    "meaning": "提案、計画書",
    "pos": "名詞",
    "level": "2級",
    "source": "大問3B",
    "example": "The proposal he wrote for the university has influenced the German university system.",
    "distractors": ["結果", "反対", "批評"],
})
vocab.append({
    "word": "perceive",
    "meaning": "認識する、知覚する",
    "pos": "動詞",
    "level": "2級",
    "source": "大問3B",
    "example": "Language was a means that allowed people to perceive the world.",
    "distractors": ["説明する", "忘れる", "拒否する"],
})
vocab.append({
    "word": "individuality",
    "meaning": "個性、独自性",
    "pos": "名詞",
    "level": "2級",
    "source": "大問3B",
    "example": "Language reflected the culture and individuality of its speakers.",
    "distractors": ["普遍性", "形式", "規則"],
})
vocab.append({
    "word": "intellectual",
    "meaning": "知的な、知識の",
    "pos": "形容詞",
    "level": "2級",
    "source": "大問3B",
    "example": "Their wealthy background gave them early access to rich intellectual opportunities.",
    "distractors": ["肉体的な", "感情的な", "商業的な"],
})
vocab.append({
    "word": "impact",
    "meaning": "影響、衝撃",
    "pos": "名詞",
    "level": "2級",
    "source": "大問3B",
    "example": "The environment gave them opportunities to achieve something with a lasting impact.",
    "distractors": ["障害", "偶然", "矛盾"],
})
vocab.append({
    "word": "indirectly",
    "meaning": "間接的に",
    "pos": "副詞",
    "level": "2級",
    "source": "大問3B",
    "example": "Many people have indirectly received benefits from their work.",
    "distractors": ["直接に", "偶然に", "正式に"],
})
vocab.append({
    "word": "economics",
    "meaning": "経済学",
    "pos": "名詞",
    "level": "2級",
    "source": "大問3B",
    "example": "Their education covered many academic subjects, such as mathematics, languages, history, and economics.",
    "distractors": ["生物学", "物理学", "心理学"],
})

assert len(vocab) == 61, f"Expected 61 words, got {len(vocab)}"

for i, v in enumerate(vocab):
    safe_word = v["word"].replace(" ", "_").replace("'", "").replace("-", "_").lower()
    v["wordAudio"] = f"audio/vocab/w_{i+1:03d}_{safe_word}.mp3"

data["vocabulary"] = vocab

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"✅ 保存完了: {OUT}")
print(f"   語彙数: {len(vocab)}")
print(f"   大問1: {len([v for v in vocab if v['source'] == '大問1'])}語")
print(f"   大問2A: {len([v for v in vocab if v['source'] == '大問2A'])}語")
print(f"   大問2B: {len([v for v in vocab if v['source'] == '大問2B'])}語")
print(f"   大問3A: {len([v for v in vocab if v['source'] == '大問3A'])}語")
print(f"   大問3B: {len([v for v in vocab if v['source'] == '大問3B'])}語")

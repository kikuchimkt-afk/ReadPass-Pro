# -*- coding: utf-8 -*-
"""
2026年度 第1回（土曜準会場）英検4級
推論なしOCR原本 → data.json（リーディング Q1〜35）
一次ソース: 2026-1-sat_4級.pdf / 2026-1-sat_4級_解答.pdf
"""
import json
import os
import sys
from collections import OrderedDict

sys.stdout.reconfigure(encoding="utf-8")

OUT_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade4", "2026-1-sat",
)
OUT_PATH = os.path.join(OUT_DIR, "data.json")

# 公式解答（解答PDF リーディング）
ANSWERS = {
    1: 2, 2: 3, 3: 4, 4: 1, 5: 2, 6: 2, 7: 3, 8: 4, 9: 3, 10: 3,
    11: 3, 12: 1, 13: 2, 14: 4, 15: 1,
    16: 2, 17: 2, 18: 1, 19: 4, 20: 3,
    21: 1, 22: 1, 23: 3, 24: 4, 25: 2,
    26: 3, 27: 4, 28: 4, 29: 1, 30: 2,
    31: 2, 32: 2, 33: 1, 34: 4, 35: 4,
}

section1_questions = [
    {
        "number": 1,
        "text": "A: What is that tall (　)?\nB: It's a new school.",
        "choices": ["meter", "building", "coin", "word"],
    },
    {
        "number": 2,
        "text": "A: Do you (　) your hands before you eat?\nB: Yes, I do. It's important.",
        "choices": ["read", "drink", "wash", "bring"],
    },
    {
        "number": 3,
        "text": "The pool is fifteen meters (　). It is also very deep.",
        "choices": ["high", "loud", "dry", "long"],
    },
    {
        "number": 4,
        "text": "A: Did you go fishing yesterday, Paul?\nB: Yes. I saw a big fish in the (　).",
        "choices": ["lake", "station", "hat", "sandwich"],
    },
    {
        "number": 5,
        "text": "Sara's birthday party was on Saturday. She (　) all her friends to her house.",
        "choices": ["looked", "invited", "decided", "hoped"],
    },
    {
        "number": 6,
        "text": "Lucas watches the (　) on TV every morning at seven o'clock.",
        "choices": ["night", "news", "wall", "name"],
    },
    {
        "number": 7,
        "text": "A: How many (　) do you have, Kim?\nB: I have six. We're all going to go to the beach this weekend.",
        "choices": ["teeth", "shirts", "cousins", "leaves"],
    },
    {
        "number": 8,
        "text": "A: Will you be in Vancouver for the weekend?\nB: Yes, we'll stay (　) my friend's place.",
        "choices": ["as", "to", "on", "at"],
    },
    {
        "number": 9,
        "text": "Kyoko always (　) up early in the morning. She makes her lunch before she goes to work.",
        "choices": ["catches", "forgets", "wakes", "keeps"],
    },
    {
        "number": 10,
        "text": "A: Do we have everything for the picnic on the beach?\nB: Wait a (　). I forgot our baseball caps.",
        "choices": ["number", "reason", "minute", "person"],
    },
    {
        "number": 11,
        "text": "A: How's Ellen, Ms. Simpson?\nB: She's still sick (　) bed, but she's better.",
        "choices": ["at", "under", "in", "with"],
    },
    {
        "number": 12,
        "text": "A: Be kind (　) your brother.\nB: Yes, Mom.",
        "choices": ["to", "on", "at", "in"],
    },
    {
        "number": 13,
        "text": "I went to the park with my grandmother yesterday. She (　) the names of many trees and flowers there.",
        "choices": ["know", "knew", "knowing", "to know"],
    },
    {
        "number": 14,
        "text": "Steve, it's already eleven o'clock. Stop (　) the video game and go to bed.",
        "choices": ["play", "plays", "played", "playing"],
    },
    {
        "number": 15,
        "text": "A: Can I play video games today, Dad?\nB: Yes, but you must (　) your bedroom first.",
        "choices": ["clean", "cleans", "is cleaning", "cleaned"],
    },
]

section2_questions = [
    {
        "number": 16,
        "text": "Father: Eric, it's dinnertime. Please tell Mom.\nSon: (　) She's talking with Aunt Jill.",
        "choices": [
            "I'll go to the store.",
            "She's on the phone.",
            "I have an idea.",
            "She doesn't like cooking.",
        ],
    },
    {
        "number": 17,
        "text": "Father: I'm going to the video shop. (　)\nDaughter: Yes. I'll get my bag.",
        "choices": [
            "How are you doing?",
            "Do you want to come?",
            "How much is it?",
            "Is it new?",
        ],
    },
    {
        "number": 18,
        "text": "Daughter: Can you take me to the supermarket today, Dad?\nFather: Sorry, Lisa. (　) now.",
        "choices": [
            "I'm going to work",
            "It's too small",
            "She's at home",
            "That's not yours",
        ],
    },
    {
        "number": 19,
        "text": "Girl 1: I'm looking for my umbrella.\nGirl 2: What does it look like?\nGirl 1: (　)",
        "choices": [
            "Of course.",
            "That's too bad.",
            "That's all.",
            "It's red and white.",
        ],
    },
    {
        "number": 20,
        "text": "Daughter: What's wrong, Dad?\nFather: I'm looking for my wallet. I looked in every room, but (　)\nDaughter: I'll help you.",
        "choices": [
            "there wasn't any.",
            "it wasn't mine.",
            "I can't find it.",
            "you didn't like it.",
        ],
    },
]

section3_questions = [
    {
        "number": 21,
        "text": "今日は制服を着る必要はありません。",
        "choices": ["①−③", "④−②", "⑤−①", "③−⑤"],
        "words": ["have", "my", "wear", "don't", "to"],
        "correctOrder": [4, 1, 5, 3, 2],
        "framePrefix": "I",
        "frameSuffix": "uniform today.",
        "answerSlots": [2, 4],
    },
    {
        "number": 22,
        "text": "夕食にスパゲッティはどうですか。",
        "choices": ["⑤−③", "⑤−①", "②−④", "③−④"],
        "words": ["dinner", "how", "for", "spaghetti", "about"],
        "correctOrder": [2, 5, 4, 3, 1],
        "framePrefix": "",
        "frameSuffix": "?",
        "answerSlots": [2, 4],
    },
    {
        "number": 23,
        "text": "そのテレビ番組はまったく面白くありませんでした。",
        "choices": ["③−④", "①−⑤", "⑤−④", "②−①"],
        "words": ["at", "not", "that TV program", "interesting", "was"],
        "correctOrder": [3, 5, 2, 4, 1],
        "framePrefix": "",
        "frameSuffix": "all.",
        "answerSlots": [2, 4],
    },
    {
        "number": 24,
        "text": "数学のテストは私にはそれほど簡単ではありませんでした。",
        "choices": ["⑤−④", "①−③", "③−④", "①−②"],
        "words": ["not", "easy", "for", "was", "so"],
        "correctOrder": [4, 1, 5, 2, 3],
        "framePrefix": "The math test",
        "frameSuffix": "me.",
        "answerSlots": [2, 4],
    },
    {
        "number": 25,
        "text": "ポール，あなたはなぜこの学校を選んだのですか。",
        "choices": ["④−③", "②−④", "①−③", "④−①"],
        "words": ["you", "did", "this", "choose", "why"],
        "correctOrder": [5, 2, 1, 4, 3],
        "framePrefix": "Paul,",
        "frameSuffix": "school?",
        "answerSlots": [2, 4],
    },
]

passage_4a = {
    "label": "A",
    "title": "Field Trip",
    "format": "notice",
    "paragraphs": [
        "Field Trip",
        "Third-grade students will go to the Rainbow Zoo on a school trip by bus.",
        "Date: Friday, June 20\nMeeting Time: 8:00 a.m.",
        "The bus ride to the Rainbow Zoo will take about two hours.\nWe will go to the Rainbow Museum instead if it rains.\nWe will come back to the school at 3:30 p.m.",
    ],
    "questions": [
        {
            "number": 26,
            "question": "If it rains, the students will go to",
            "choices": [
                "the Rainbow Zoo.",
                "another school.",
                "the Rainbow Museum.",
                "the theater.",
            ],
        },
        {
            "number": 27,
            "question": "What time will the students come back to the school?",
            "choices": [
                "At 8:00 a.m.",
                "At 2:00 p.m.",
                "At 3:00 p.m.",
                "At 3:30 p.m.",
            ],
        },
    ],
}

passage_4b = {
    "label": "B",
    "title": "About next week",
    "paragraphs": [
        "From: Ted Miller\nTo: Leo Smith\nDate: October 10\nSubject: About next week",
        "Hi Leo,\nYou were not at basketball practice yesterday, right? Are you OK? We will have a meeting in room 203 next Monday, and we can meet our new coach at the meeting! Can you come to the meeting? Also, you can get your new uniform after practice next Friday!\nYour teammate,\nTed",
        "From: Leo Smith\nTo: Ted Miller\nDate: October 10\nSubject: Thank you!",
        "Hi Ted,\nI did not have a fever, but I had a headache yesterday afternoon. So, I could not go to practice. However, I am feeling better now. I will go to the meeting, and I am excited to meet our new coach! By the way, my friend David is interested in joining our team. Can I go to practice with him next Wednesday?\nBye,\nLeo",
    ],
    "questions": [
        {
            "number": 28,
            "question": "What can Ted and Leo do at the meeting?",
            "choices": [
                "Get their new shoes.",
                "Meet their new teammate.",
                "Get their new uniform.",
                "Meet their new coach.",
            ],
        },
        {
            "number": 29,
            "question": "Yesterday afternoon, Leo",
            "choices": [
                "had a headache.",
                "had a fever.",
                "met his team's captain.",
                "played basketball with Ted.",
            ],
        },
        {
            "number": 30,
            "question": "When does Leo want to go to practice with David?",
            "choices": [
                "Next Monday.",
                "Next Wednesday.",
                "Next Friday.",
                "Next Saturday.",
            ],
        },
    ],
}

passage_4c = {
    "label": "C",
    "title": "Kate's Story",
    "paragraphs": [
        "Kate is sixteen years old and loves her grandmother. Her grandmother always made fun stories for Kate. Kate enjoyed visiting her grandmother's house with her parents and listening to her grandmother's stories. Then, she also began to write her own stories.",
        "Kate's grandmother got sick a year ago, so she is in the hospital now. One day, Kate's father said, \"Let's go to see your grandma next Sunday!\" Kate said, \"Sure! Should I buy some flowers or cookies as a present?\" Kate's father said, \"No. You're good at writing stories! You should write a story for her.\" Kate said, \"Good idea! I'll try it.\"",
        "When Kate and her father visited the hospital, they saw three novels, four history books, and two magazines around her grandmother's bed. Kate gave her grandmother a notebook. Kate's grandmother looked in the notebook and said, \"You wrote a story! This is a wonderful present!\" Kate was so happy.",
    ],
    "questions": [
        {
            "number": 31,
            "question": "What did Kate's grandmother always do for Kate?",
            "choices": [
                "She visited Kate's house.",
                "She made fun stories.",
                "She listened to Kate's stories.",
                "She bought many books.",
            ],
        },
        {
            "number": 32,
            "question": "Where is Kate's grandmother now?",
            "choices": [
                "In Kate's house.",
                "In the hospital.",
                "At her friend's house.",
                "At her own house.",
            ],
        },
        {
            "number": 33,
            "question": "What did Kate's father say to Kate about the present for her grandmother?",
            "choices": [
                "Kate should write a story.",
                "Kate should make some cookies.",
                "Kate should bring some flowers.",
                "Kate should buy some fun books.",
            ],
        },
        {
            "number": 34,
            "question": "How many history books did Kate see around her grandmother's bed?",
            "choices": ["One.", "Two.", "Three.", "Four."],
        },
        {
            "number": 35,
            "question": "What did Kate give her grandmother?",
            "choices": [
                "Some history books.",
                "A picture.",
                "Some magazines.",
                "A notebook.",
            ],
        },
    ],
}


def attach_answers(questions):
    for q in questions:
        q["answer"] = ANSWERS[q["number"]]


for q in section1_questions:
    attach_answers([q])
for q in section2_questions:
    attach_answers([q])
for q in section3_questions:
    attach_answers([q])
for pa in (passage_4a, passage_4b, passage_4c):
    attach_answers(pa["questions"])

data = {
    "title": "英検4級 2026年度 第1回（土曜準会場）",
    "grade": "grade4",
    "exam": "2026-1-sat",
    "year": 2026,
    "session": "2026-1-sat",
    "sections": [
        {
            "name": "大問1",
            "nameEn": "Part 1",
            "type": "vocabulary",
            "instruction": "次の(1)から(15)までの( )に入れるのに最も適切なものを1, 2, 3, 4の中から一つ選び、その番号のマーク欄をぬりつぶしなさい。",
            "questions": section1_questions,
        },
        {
            "name": "大問2",
            "nameEn": "Part 2",
            "type": "vocabulary",
            "instruction": "次の(16)から(20)までの会話について、( )に入れるのに最も適切なものを1, 2, 3, 4の中から一つ選び、その番号のマーク欄をぬりつぶしなさい。",
            "questions": section2_questions,
        },
        {
            "name": "大問3",
            "nameEn": "Part 3",
            "type": "sentence-order",
            "instruction": "次の(21)から(25)までの日本文の意味を表すように①から⑤までを並べかえて( )の中に入れなさい。",
            "questions": section3_questions,
        },
        {
            "name": "大問4",
            "nameEn": "Part 4",
            "type": "reading-comprehension",
            "passages": [passage_4a, passage_4b, passage_4c],
        },
    ],
    "listening": {
        "part1": {1: 1, 2: 1, 3: 1, 4: 2, 5: 2, 6: 1, 7: 2, 8: 2, 9: 1, 10: 2},
        "part2": {11: 4, 12: 3, 13: 4, 14: 2, 15: 4, 16: 3, 17: 3, 18: 4, 19: 1, 20: 2},
        "part3": {21: 1, 22: 3, 23: 1, 24: 1, 25: 1, 26: 3, 27: 3, 28: 3, 29: 2, 30: 3},
    },
}

os.makedirs(OUT_DIR, exist_ok=True)

if os.path.exists(OUT_PATH):
    with open(OUT_PATH, encoding="utf-8") as f:
        existing = json.load(f)
    for key in ("vocabulary", "lessonPlan"):
        if key in existing:
            data[key] = existing[key]
    for i, new_sec in enumerate(data["sections"]):
        if i >= len(existing.get("sections", [])):
            continue
        old_sec = existing["sections"][i]
        if old_sec.get("name") != new_sec.get("name"):
            continue
        if new_sec.get("type") == "vocabulary":
            old_qs = {q["number"]: q for q in old_sec.get("questions", [])}
            merged = []
            for q in new_sec["questions"]:
                oq = old_qs.get(q["number"], {})
                if oq.get("grammar"):
                    merged.append(oq)
                else:
                    merged.append(q)
            new_sec["questions"] = merged
        elif new_sec.get("type") == "sentence-order":
            old_qs = {q["number"]: q for q in old_sec.get("questions", [])}
            merged = []
            for q in new_sec["questions"]:
                oq = old_qs.get(q["number"], {})
                if oq.get("grammar"):
                    merged.append(oq)
                else:
                    merged.append(q)
            new_sec["questions"] = merged
        elif new_sec.get("type") == "reading-comprehension":
            old_ps = {p.get("label"): p for p in old_sec.get("passages", [])}
            for p in new_sec.get("passages", []):
                op = old_ps.get(p.get("label"), {})
                if op.get("translations"):
                    p["translations"] = op["translations"]
                old_qq = {q["number"]: q for q in op.get("questions", [])}
                for q in p.get("questions", []):
                    oq = old_qq.get(q["number"], {})
                    if oq.get("grammar"):
                        q.clear()
                        q.update(oq)

order = (
    "grade", "year", "session", "title", "exam",
    "sections", "listening", "vocabulary", "lessonPlan",
)
out = OrderedDict()
for k in order:
    if k in data:
        out[k] = data[k]
for k in data:
    if k not in out:
        out[k] = data[k]

with open(OUT_PATH, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=4)

print(f"Wrote {OUT_PATH}")
print(f"  sections: {len(data['sections'])}")
print(f"  reading questions: 35")

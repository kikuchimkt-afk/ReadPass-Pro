# -*- coding: utf-8 -*-
"""
2026年度 第1回（土曜準会場）英検5級
推論なしOCR原本 → data.json（リーディング Q1〜25）
一次ソース: 2026-1-sat_5級.pdf / 2026-1-sat_5級_解答.pdf
"""
import json
import os
import sys
from collections import OrderedDict

sys.stdout.reconfigure(encoding="utf-8")

OUT_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade5", "2026-1-sat",
)
OUT_PATH = os.path.join(OUT_DIR, "data.json")

# 公式解答（解答PDF リーディング）
ANSWERS = {
    1: 2, 2: 1, 3: 1, 4: 2, 5: 3, 6: 4, 7: 2, 8: 3, 9: 1, 10: 1,
    11: 3, 12: 1, 13: 3, 14: 3, 15: 3,
    16: 1, 17: 3, 18: 1, 19: 3, 20: 3,
    21: 4, 22: 4, 23: 3, 24: 3, 25: 4,
}

section1_questions = [
    {
        "number": 1,
        "text": "A: This baseball game is great.\nB: I (　) so, too.",
        "choices": ["speak", "think", "live", "sing"],
    },
    {
        "number": 2,
        "text": "Dan's mother is a (　). She works at the hospital from Monday to Friday.",
        "choices": ["doctor", "player", "king", "farmer"],
    },
    {
        "number": 3,
        "text": "I put my books in my (　) before I go to class.",
        "choices": ["locker", "drink", "dictionary", "chopsticks"],
    },
    {
        "number": 4,
        "text": "A: Your sister's dress is very (　).\nB: Yes. She likes it very much.",
        "choices": ["rainy", "cute", "tall", "fast"],
    },
    {
        "number": 5,
        "text": "A: When does your summer (　) start?\nB: On July 20.",
        "choices": ["newspaper", "song", "vacation", "candy"],
    },
    {
        "number": 6,
        "text": "A: What do you do after school, Cindy?\nB: I play (　).",
        "choices": ["bike", "book", "strawberry", "basketball"],
    },
    {
        "number": 7,
        "text": "Kengo usually watches the news on TV after dinner, but tonight he is watching a (　) TV show.",
        "choices": ["same", "different", "high", "young"],
    },
    {
        "number": 8,
        "text": "A: Can you come (　) my house at three this afternoon?\nB: Sorry, I can't.",
        "choices": ["of", "for", "to", "out"],
    },
    {
        "number": 9,
        "text": "A: Do you wash the dishes every (　), Tim?\nB: No, only on weekends.",
        "choices": ["night", "cup", "hand", "coin"],
    },
    {
        "number": 10,
        "text": "A: Can I have a (　) of apple juice, Mom?\nB: Yes. Here you are.",
        "choices": ["glass", "plate", "knife", "fork"],
    },
    {
        "number": 11,
        "text": "A: That doll is very nice. How (　) is it?\nB: It's only $5.",
        "choices": ["short", "young", "much", "sad"],
    },
    {
        "number": 12,
        "text": "A: Jenny is a new student. She is (　) France.\nB: That's great. I love France.",
        "choices": ["from", "in", "of", "at"],
    },
    {
        "number": 13,
        "text": "A: I like this movie.\nB: (　), too.",
        "choices": ["He", "Them", "Me", "We"],
    },
    {
        "number": 14,
        "text": "A: Alice, (　) quiet!\nB: Sorry, Dad.",
        "choices": ["am", "are", "be", "is"],
    },
    {
        "number": 15,
        "text": "A: (　) phone is this?\nB: It's Bill's.",
        "choices": ["When", "Where", "Whose", "How"],
    },
]

section2_questions = [
    {
        "number": 16,
        "text": "Woman: I'm a nurse. What do you do?\nMan: (　)",
        "choices": [
            "I'm a cook.",
            "At school.",
            "I like it.",
            "For seven years.",
        ],
    },
    {
        "number": 17,
        "text": "Boy: Happy birthday, Linda. (　)\nGirl: Oh, thank you, Mike. They're beautiful.",
        "choices": [
            "I'm cold.",
            "See you.",
            "These flowers are for you.",
            "Help me, please.",
        ],
    },
    {
        "number": 18,
        "text": "Mother: What do you want for lunch, Tom?\nBoy: (　)",
        "choices": [
            "A sandwich, please.",
            "At twelve o'clock.",
            "I'm always hungry.",
            "I can't cook.",
        ],
    },
    {
        "number": 19,
        "text": "Mother: Is your history test today, John?\nBoy: No, (　)",
        "choices": [
            "I study history.",
            "in my room.",
            "it's tomorrow.",
            "it's cloudy today.",
        ],
    },
    {
        "number": 20,
        "text": "Man 1: Hi, Bill. (　)\nMan 2: Good, thanks.",
        "choices": [
            "When do you go?",
            "How old are you?",
            "How are you doing?",
            "What are you doing?",
        ],
    },
]

section3_questions = [
    {
        "number": 21,
        "text": "私の姉は毎日お皿を洗います。",
        "choices": ["③ ─ ②", "④ ─ ③", "① ─ ④", "② ─ ③"],
        "words": ["the dishes", "my", "washes", "sister"],
        "correctOrder": [2, 4, 3, 1],
        "framePrefix": "",
        "frameSuffix": "every day.",
        "answerSlots": [1, 3],
    },
    {
        "number": 22,
        "text": "ビルと私は冬にスキーに行きます。",
        "choices": ["② ─ ③", "④ ─ ③", "① ─ ④", "③ ─ ②"],
        "words": ["skiing", "go", "and", "I"],
        "correctOrder": [3, 4, 2, 1],
        "framePrefix": "Bill",
        "frameSuffix": "in winter.",
        "answerSlots": [1, 3],
    },
    {
        "number": 23,
        "text": "学校にかさを持って行きなさい。",
        "choices": ["④ ─ ③", "② ─ ④", "① ─ ③", "② ─ ①"],
        "words": ["take", "school", "to", "your umbrella"],
        "correctOrder": [1, 4, 3, 2],
        "framePrefix": "",
        "frameSuffix": ".",
        "answerSlots": [1, 3],
    },
    {
        "number": 24,
        "text": "マイクのサッカーチームには3人のコーチがいます。",
        "choices": ["① ─ ②", "④ ─ ②", "② ─ ③", "③ ─ ④"],
        "words": ["coaches", "soccer team", "three", "has"],
        "correctOrder": [2, 4, 3, 1],
        "framePrefix": "Mike's",
        "frameSuffix": ".",
        "answerSlots": [1, 3],
    },
    {
        "number": 25,
        "text": "今日は学校がありません。",
        "choices": ["④ ─ ②", "① ─ ②", "② ─ ①", "③ ─ ④"],
        "words": ["don't", "school", "we", "have"],
        "correctOrder": [3, 1, 4, 2],
        "framePrefix": "",
        "frameSuffix": "today.",
        "answerSlots": [1, 3],
    },
]


def attach_answers(questions):
    for q in questions:
        q["answer"] = ANSWERS[q["number"]]


for q in section1_questions:
    attach_answers([q])
for q in section2_questions:
    attach_answers([q])
for q in section3_questions:
    attach_answers([q])

data = {
    "title": "英検5級 2026年度 第1回（土曜準会場）",
    "grade": "grade5",
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
            "instruction": "次の(21)から(25)までの日本文の意味を表すように①から④までを並べかえて( )の中に入れなさい。そして、1番目と3番目にくるものの最も適切な組合せを1, 2, 3, 4の中から一つ選び、その番号のマーク欄をぬりつぶしなさい。※ただし、( )の中では、文のはじめにくる語も小文字になっています。",
            "questions": section3_questions,
        },
    ],
    "listening": {
        "part1": {1: 2, 2: 3, 3: 1, 4: 1, 5: 2, 6: 3, 7: 2, 8: 1, 9: 3, 10: 3},
        "part2": {11: 2, 12: 1, 13: 3, 14: 3, 15: 1},
        "part3": {
            16: 2, 17: 1, 18: 1, 19: 2, 20: 3,
            21: 1, 22: 1, 23: 2, 24: 2, 25: 1,
        },
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
        if new_sec.get("type") in ("vocabulary", "sentence-order"):
            old_qs = {q["number"]: q for q in old_sec.get("questions", [])}
            merged = []
            for q in new_sec["questions"]:
                oq = old_qs.get(q["number"], {})
                if oq.get("grammar"):
                    merged.append(oq)
                else:
                    merged.append(q)
            new_sec["questions"] = merged

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
print(f"  reading questions: 25")

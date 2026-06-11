# -*- coding: utf-8 -*-
"""
2026年度 第1回（本会場）英検5級
推論なしOCR原本 → data.json（リーディング Q1〜25）
一次ソース: 2026-1(本会場）/5級.pdf / 5級解答.pdf
"""
import json
import os
import sys
from collections import OrderedDict

sys.stdout.reconfigure(encoding="utf-8")

OUT_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade5", "2026-1",
)
OUT_PATH = os.path.join(OUT_DIR, "data.json")

ANSWERS = {
    1: 3, 2: 4, 3: 4, 4: 2, 5: 4, 6: 4, 7: 2, 8: 2, 9: 4, 10: 1,
    11: 1, 12: 4, 13: 1, 14: 4, 15: 1,
    16: 1, 17: 2, 18: 1, 19: 1, 20: 1,
    21: 3, 22: 3, 23: 1, 24: 1, 25: 1,
}

section1_questions = [
    {
        "number": 1,
        "text": "A: What do you do in your free time, John?\nB: I read a (　) every day.",
        "choices": ["music", "paint", "newspaper", "lunch"],
    },
    {
        "number": 2,
        "text": "Many (　) are waiting for the new pink train. It's very popular.",
        "choices": ["books", "teeth", "fruits", "people"],
    },
    {
        "number": 3,
        "text": "A: Where is your tennis (　), Hiroki?\nB: It's in my bag, Mom.",
        "choices": ["fork", "dictionary", "kite", "racket"],
    },
    {
        "number": 4,
        "text": "A: Mike, please (　) your coffee before you go to school.\nB: OK, Mom.",
        "choices": ["sleep", "drink", "arrive", "talk"],
    },
    {
        "number": 5,
        "text": "Taro likes skiing. He goes to the (　) near his house every winter.",
        "choices": ["pool", "station", "library", "mountain"],
    },
    {
        "number": 6,
        "text": "A: Mike, how (　) is that building?\nB: It's 200 meters.",
        "choices": ["fast", "cold", "young", "tall"],
    },
    {
        "number": 7,
        "text": "A: Excuse me, Ms. Brown. Can I go home now?\nB: Yes, John. You can (　) now.",
        "choices": ["know", "leave", "take", "eat"],
    },
    {
        "number": 8,
        "text": "A: Sorry, Mike. I can't go to the movie with you today.\nB: Oh, I (　).",
        "choices": ["look", "see", "play", "stand"],
    },
    {
        "number": 9,
        "text": "A: Do you often eat fruit (　) home?\nB: No.",
        "choices": ["under", "with", "about", "at"],
    },
    {
        "number": 10,
        "text": "A: Dad, can we (　) hiking tomorrow?\nB: Sure.",
        "choices": ["go", "want", "close", "play"],
    },
    {
        "number": 11,
        "text": "Taro goes to the swimming pool (　) school.",
        "choices": ["after", "about", "down", "on"],
    },
    {
        "number": 12,
        "text": "I (　) up at seven every morning. Then, I have breakfast with my mother.",
        "choices": ["sing", "talk", "close", "wake"],
    },
    {
        "number": 13,
        "text": "Mr. Ford teaches English. We like (　) class very much.",
        "choices": ["his", "he", "him", "us"],
    },
    {
        "number": 14,
        "text": "A: Nancy, I can't find my eraser. Can I use yours?\nB: Yes. You can use (　).",
        "choices": ["I", "my", "me", "mine"],
    },
    {
        "number": 15,
        "text": "A: Is Kent in the library?\nB: Yes, he (　) there.",
        "choices": ["is studying", "are studying", "am studying", "studying"],
    },
]

section2_questions = [
    {
        "number": 16,
        "text": "Girl 1: Is Ken in your class this year?\nGirl 2: (　) I like him a lot.",
        "choices": [
            "Yes, he is.",
            "Please come back.",
            "Sit down.",
            "No, I don't.",
        ],
    },
    {
        "number": 17,
        "text": "Boy: I enjoy basketball.\nGirl: (　) I often play it on Sundays.",
        "choices": [
            "No, I don't.",
            "I do, too.",
            "That's OK.",
            "You're welcome.",
        ],
    },
    {
        "number": 18,
        "text": "Teacher: Does your sister work at a hospital, Sally?\nGirl: Yes. (　)",
        "choices": [
            "She's a nurse.",
            "I like volleyball.",
            "I'm so fast.",
            "She has a dog.",
        ],
    },
    {
        "number": 19,
        "text": "Man: Let's go to that hamburger shop.\nWoman: (　) I'm hungry.",
        "choices": [
            "Good idea.",
            "See you.",
            "That's all.",
            "It's sunny today.",
        ],
    },
    {
        "number": 20,
        "text": "Man: Are you from Australia?\nWoman: (　)",
        "choices": [
            "Yes, I am.",
            "Yes, I can.",
            "Yes, it is.",
            "Yes, it does.",
        ],
    },
]

section3_questions = [
    {
        "number": 21,
        "text": "あなたの英語のテストはいつですか。",
        "choices": ["④ ─ ②", "③ ─ ①", "② ─ ④", "① ─ ④"],
        "words": ["is", "when", "English", "your"],
        "correctOrder": [2, 1, 4, 3],
        "framePrefix": "",
        "frameSuffix": "test?",
        "answerSlots": [1, 3],
    },
    {
        "number": 22,
        "text": "ロンドンは何時ですか。",
        "choices": ["③ ─ ①", "④ ─ ②", "③ ─ ④", "② ─ ①"],
        "words": ["in", "is", "time", "it"],
        "correctOrder": [3, 2, 4, 1],
        "framePrefix": "What",
        "frameSuffix": "London?",
        "answerSlots": [1, 3],
    },
    {
        "number": 23,
        "text": "私たちの担任は遠藤先生です。",
        "choices": ["① ─ ③", "④ ─ ②", "③ ─ ④", "① ─ ②"],
        "words": ["our", "is", "teacher", "homeroom"],
        "correctOrder": [1, 4, 3, 2],
        "framePrefix": "",
        "frameSuffix": "Mr. Endo.",
        "answerSlots": [1, 3],
    },
    {
        "number": 24,
        "text": "一樹は夕食にピザが欲しいです。",
        "choices": ["④ ─ ②", "② ─ ①", "③ ─ ④", "① ─ ③"],
        "words": ["wants", "some pizza", "for", "Kazuki"],
        "correctOrder": [4, 1, 2, 3],
        "framePrefix": "",
        "frameSuffix": "dinner.",
        "answerSlots": [1, 3],
    },
    {
        "number": 25,
        "text": "あなたは昼食に何を作っていますか。",
        "choices": ["③ ─ ④", "① ─ ②", "② ─ ③", "④ ─ ①"],
        "words": ["are", "making", "what", "you"],
        "correctOrder": [3, 1, 4, 2],
        "framePrefix": "",
        "frameSuffix": "for lunch?",
        "answerSlots": [1, 3],
    },
]


def attach_answers(questions):
    for q in questions:
        q["answer"] = ANSWERS[q["number"]]


attach_answers(section1_questions)
attach_answers(section2_questions)
attach_answers(section3_questions)

data = {
    "grade": "grade5",
    "year": 2026,
    "session": "2026-1",
    "title": "英検5級 2026年度 第1回",
    "exam": "2026-1",
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
        "part1": {1: 3, 2: 1, 3: 3, 4: 1, 5: 2, 6: 3, 7: 2, 8: 1, 9: 3, 10: 3},
        "part2": {11: 2, 12: 1, 13: 1, 14: 2, 15: 2},
        "part3": {
            16: 3, 17: 2, 18: 3, 19: 3, 20: 2,
            21: 3, 22: 1, 23: 2, 24: 1, 25: 3,
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

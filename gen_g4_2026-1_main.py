# -*- coding: utf-8 -*-
"""
2026年度 第1回（本会場）英検4級
推論なしOCR原本 → data.json（リーディング Q1〜35）
一次ソース: 2026-1(本会場）/4級.pdf / 4級解答.pdf
"""
import json
import os
import sys
from collections import OrderedDict

sys.stdout.reconfigure(encoding="utf-8")

OUT_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade4", "2026-1",
)
OUT_PATH = os.path.join(OUT_DIR, "data.json")

# 公式解答（解答PDF リーディング）
ANSWERS = {
    1: 2, 2: 3, 3: 1, 4: 1, 5: 3, 6: 2, 7: 1, 8: 2, 9: 2, 10: 1,
    11: 1, 12: 1, 13: 4, 14: 2, 15: 3,
    16: 4, 17: 2, 18: 4, 19: 3, 20: 3,
    21: 2, 22: 1, 23: 2, 24: 3, 25: 3,
    26: 1, 27: 2, 28: 3, 29: 3, 30: 1,
    31: 3, 32: 3, 33: 4, 34: 1, 35: 3,
}

section1_questions = [
    {
        "number": 1,
        "text": "A: I want to make some pancakes for breakfast, but we don't have any (　).\nB: I'll go to the store and get some.",
        "choices": ["flowers", "eggs", "books", "sports"],
    },
    {
        "number": 2,
        "text": "A: I want to call my mother, but I don't have a phone.\nB: You can (　) my phone.",
        "choices": ["climb", "leave", "use", "send"],
    },
    {
        "number": 3,
        "text": "A: Mom, I want to make some cookies.\nB: All right, but please (　) this carrot first.",
        "choices": ["cut", "arrive", "hit", "run"],
    },
    {
        "number": 4,
        "text": "A: Is it warm in your (　) now?\nB: Yes, it's spring.",
        "choices": ["country", "ticket", "animal", "road"],
    },
    {
        "number": 5,
        "text": "Taro enjoyed the chorus (　) on TV yesterday. He wants to join a chorus at school.",
        "choices": ["wall", "hobby", "contest", "trip"],
    },
    {
        "number": 6,
        "text": "A: Can I study in the library today?\nB: Yes, it's (　) now.",
        "choices": ["cold", "open", "late", "favorite"],
    },
    {
        "number": 7,
        "text": "Sally went to eat Chinese food in a big (　) last weekend.",
        "choices": ["city", "word", "body", "point"],
    },
    {
        "number": 8,
        "text": "A: What do you want to do tomorrow afternoon?\nB: I have an (　). Let's go to the aquarium.",
        "choices": ["end", "idea", "arm", "eraser"],
    },
    {
        "number": 9,
        "text": "A: These are my new glasses. What do you (　) of them?\nB: They're really nice, Grandma.",
        "choices": ["watch", "think", "tell", "finish"],
    },
    {
        "number": 10,
        "text": "A: Mom, I'm going to play in the soccer game tomorrow.\nB: Good (　) you. You practiced a lot.",
        "choices": ["for", "with", "in", "after"],
    },
    {
        "number": 11,
        "text": "A: Did you (　) about Dan?\nB: Yes. He's going to move back to England.",
        "choices": ["hear", "wait", "run", "want"],
    },
    {
        "number": 12,
        "text": "A: Here are four cookies, Bob. Please (　) them with your sister.\nB: OK. I'll give her two of them.",
        "choices": ["share", "answer", "cry", "run"],
    },
    {
        "number": 13,
        "text": "A: Today, apples are (　) than bananas.\nB: OK. Let's get some apples.",
        "choices": ["cheap", "cheapest", "the cheapest", "cheaper"],
    },
    {
        "number": 14,
        "text": "The students (　) 50 meters in the school pool yesterday.",
        "choices": ["swim", "swam", "swimming", "to swim"],
    },
    {
        "number": 15,
        "text": "A: You (　) read this book before the test next Monday.\nB: OK, Mr. Peterson.",
        "choices": ["have", "be", "must", "were"],
    },
]

section2_questions = [
    {
        "number": 16,
        "text": "Girl: I forgot my red pen. (　)\nBoy: Of course you can. Here you are.",
        "choices": [
            "Will you go home soon?",
            "Is the color OK?",
            "Do you like writing?",
            "Can I borrow yours?",
        ],
    },
    {
        "number": 17,
        "text": "Girl 1: I want to climb this tree.\nGirl 2: (　) Let's climb the one over there.\nGirl 1: OK.",
        "choices": [
            "These flowers are pretty.",
            "It's too tall.",
            "My garden is big.",
            "Your house is very nice.",
        ],
    },
    {
        "number": 18,
        "text": "Man: Excuse me. I want to buy these socks. (　)\nClerk: Two dollars.",
        "choices": [
            "How are you doing?",
            "How many do you have?",
            "How tall are you?",
            "How much are they?",
        ],
    },
    {
        "number": 19,
        "text": "Daughter: Dad, I can't find my social studies textbook.\nFather: (　)\nDaughter: Thanks.",
        "choices": [
            "It's a difficult subject.",
            "It was very interesting.",
            "It's on the kitchen table.",
            "It's for your brother.",
        ],
    },
    {
        "number": 20,
        "text": "Girl 1: Jenny, you don't look well today. (　)\nGirl 2: I'm fine. I'm just a little tired.",
        "choices": [
            "Can I go home?",
            "Did you call me?",
            "Are you OK?",
            "Is your mother a doctor?",
        ],
    },
]

section3_questions = [
    {
        "number": 21,
        "text": "なぜあなたは今朝、そんなに早く起きたのですか。",
        "choices": ["①−②", "⑤−③", "③−⑤", "④−①"],
        "words": ["you", "up", "get", "why", "did"],
        "correctOrder": [4, 5, 1, 3, 2],
        "framePrefix": "",
        "frameSuffix": "so early this morning?",
        "answerSlots": [2, 4],
    },
    {
        "number": 22,
        "text": "今日の午後、あなたに電話してもいいですか。",
        "choices": ["④−③", "①−③", "⑤−①", "③−①"],
        "words": ["this", "may", "you", "I", "call"],
        "correctOrder": [2, 4, 5, 3, 1],
        "framePrefix": "",
        "frameSuffix": "afternoon?",
        "answerSlots": [2, 4],
    },
    {
        "number": 23,
        "text": "ネパールではたくさんの高い山を見ることができます。",
        "choices": ["④−②", "③−⑤", "④−③", "⑤−③"],
        "words": ["see", "you", "can", "high mountains", "lots of"],
        "correctOrder": [2, 3, 1, 5, 4],
        "framePrefix": "",
        "frameSuffix": "in Nepal.",
        "answerSlots": [2, 4],
    },
    {
        "number": 24,
        "text": "私は毎朝７時に家を出て学校へ向かいます。",
        "choices": ["⑤−③", "③−④", "⑤−②", "③−⑤"],
        "words": ["at", "school", "leave", "for", "home"],
        "correctOrder": [3, 5, 4, 2, 1],
        "framePrefix": "I",
        "frameSuffix": "seven o'clock every morning.",
        "answerSlots": [2, 4],
    },
    {
        "number": 25,
        "text": "これらのコーヒーカップを洗ってくれますか。",
        "choices": ["④−⑤", "③−①", "②−⑤", "①−②"],
        "words": ["wash", "you", "coffee cups", "could", "these"],
        "correctOrder": [4, 2, 1, 5, 3],
        "framePrefix": "",
        "frameSuffix": ", please?",
        "answerSlots": [2, 4],
    },
]

passage_4a = {
    "label": "A",
    "title": "Musician Will Visit Our School",
    "format": "notice",
    "paragraphs": [
        "Musician Will Visit Our School",
        "The famous piano player Mr. Stevens will visit the school on Friday afternoon for one hour.",
        "He will first give a speech in the gym and then play three songs in the music room. After this performance, students can eat snacks in the cafeteria.",
        "Date: February 12\nTime: 4:00 p.m. to 5:00 p.m.",
    ],
    "questions": [
        {
            "number": 26,
            "question": "What will happen in the gym?",
            "choices": [
                "A piano player will give a speech.",
                "Students will receive free snacks.",
                "A piano player will play songs.",
                "Students will dance.",
            ],
        },
        {
            "number": 27,
            "question": "How many songs will Mr. Stevens play?",
            "choices": [
                "Two songs.",
                "Three songs.",
                "Four songs.",
                "Five songs.",
            ],
        },
    ],
}

passage_4b = {
    "label": "B",
    "title": "How are your cats?",
    "paragraphs": [
        "From: Jimmy Cook\nTo: Cathy Cook\nDate: July 7\nSubject: How are your cats?",
        "Dear Grandma,\nLast summer was so much fun! I enjoyed spending two weeks at your home. How is your cat, Lily? She had some babies, right? Dad told me about it. How many babies does she have? I really want to see them! Can I visit your home next month? I can stay for four days then!\nWrite soon,\nJimmy",
        "From: Cathy Cook\nTo: Jimmy Cook\nDate: July 7\nSubject: They are fine!",
        "Dear Jimmy,\nOf course, come and see my cat Lily and her babies next month! She has three babies, and they are very cute. Yesterday, one of my friends visited me and saw them, too! I'll send you a picture of the babies by email tomorrow!\nLove,\nGrandma",
    ],
    "questions": [
        {
            "number": 28,
            "question": "When can Jimmy visit his grandmother's home?",
            "choices": [
                "Tomorrow.",
                "Next week.",
                "Next month.",
                "Next summer.",
            ],
        },
        {
            "number": 29,
            "question": "How many babies does Lily have?",
            "choices": ["One.", "Two.", "Three.", "Four."],
        },
        {
            "number": 30,
            "question": "Who visited Jimmy's grandmother yesterday?",
            "choices": [
                "Her friend.",
                "Her daughter.",
                "Jimmy.",
                "Jimmy's father.",
            ],
        },
    ],
}

passage_4c = {
    "label": "C",
    "title": "A Visit to a History Museum",
    "paragraphs": [
        "George is thirteen years old. Recently, his sister wanted to go to a history museum. So, his family went to the museum last Saturday. The museum was in an old building. It was eighty years old. In the museum, he saw many interesting things. The best part was an old classroom.",
        "George walked into the classroom and saw an old blackboard. The blackboard was forty years old. He was surprised because the blackboard was green. He also saw desks and chairs. They were dark brown. Then, George saw some old history textbooks. He saw a lot of interesting things in the classroom. He liked looking at the textbooks most because they were so old.",
        "The history museum was very fun. George's favorite subjects in school were English and math before, but now his favorite is history. George wants to go to more museums with his sister.",
    ],
    "questions": [
        {
            "number": 31,
            "question": "Why did George's family go to the museum last Saturday?",
            "choices": [
                "George's father had four tickets.",
                "George's mother works there.",
                "George's sister wanted to go.",
                "George likes history.",
            ],
        },
        {
            "number": 32,
            "question": "How old was the blackboard?",
            "choices": [
                "Thirteen years old.",
                "Twenty years old.",
                "Forty years old.",
                "Eighty years old.",
            ],
        },
        {
            "number": 33,
            "question": "What color were the desks?",
            "choices": ["Black.", "Green.", "Light brown.", "Dark brown."],
        },
        {
            "number": 34,
            "question": "What did George like most in the classroom?",
            "choices": [
                "The textbooks.",
                "The desks.",
                "The map.",
                "The blackboard.",
            ],
        },
        {
            "number": 35,
            "question": "Now, George's favorite subject is",
            "choices": ["math.", "English.", "history.", "music."],
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
    "title": "英検4級 2026年度 第1回",
    "grade": "grade4",
    "exam": "2026-1",
    "year": 2026,
    "session": "2026-1",
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
        "part1": {1: 1, 2: 3, 3: 2, 4: 1, 5: 1, 6: 1, 7: 3, 8: 1, 9: 3, 10: 2},
        "part2": {11: 1, 12: 2, 13: 3, 14: 4, 15: 4, 16: 3, 17: 4, 18: 3, 19: 4, 20: 1},
        "part3": {21: 2, 22: 3, 23: 3, 24: 4, 25: 2, 26: 4, 27: 1, 28: 3, 29: 1, 30: 4},
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

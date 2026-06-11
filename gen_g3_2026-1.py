# -*- coding: utf-8 -*-
"""
2026年度 第1回（土曜準会場）英検3級
推論なしOCR原本 → data.json（リーディング Q1〜30）
一次ソース: 2026-1‐sat_3級.pdf / 2026-1‐sat_3級_解答.pdf
"""
import json
import os
import sys
from collections import OrderedDict

sys.stdout.reconfigure(encoding="utf-8")

OUT_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade3", "2026-1-sat",
)
OUT_PATH = os.path.join(OUT_DIR, "data.json")

# 公式解答（解答PDF リーディング）
ANSWERS = {
    1: 2, 2: 4, 3: 1, 4: 4, 5: 1, 6: 4, 7: 3, 8: 4, 9: 4, 10: 4,
    11: 3, 12: 4, 13: 3, 14: 3, 15: 2,
    16: 3, 17: 3, 18: 3, 19: 1, 20: 2,
    21: 3, 22: 1, 23: 1, 24: 4, 25: 3,
    26: 3, 27: 1, 28: 2, 29: 3, 30: 4,
}

section1_questions = [
    {
        "number": 1,
        "text": "A: What are you going to do next Sunday?\nB: I'm going to the park to fly my (　).",
        "choices": ["field", "kite", "lock", "university"],
    },
    {
        "number": 2,
        "text": "A: Can you (　) me the ball, please?\nB: Here you are.",
        "choices": ["imagine", "remember", "waste", "pass"],
    },
    {
        "number": 3,
        "text": "The movie was very (　). Lucy fell asleep in the theater.",
        "choices": ["boring", "clever", "colorful", "absent"],
    },
    {
        "number": 4,
        "text": "Yoko is (　) today. She studied English for five hours yesterday.",
        "choices": ["sad", "bright", "alive", "tired"],
    },
    {
        "number": 5,
        "text": "A: Do you want to be a good swimmer?\nB: Sure. My coach says I need to (　) for three hours every day.",
        "choices": ["exercise", "invite", "wrap", "follow"],
    },
    {
        "number": 6,
        "text": "Jim saw some people who were buying fresh fish and meat at the (　).",
        "choices": ["promise", "cousin", "novel", "market"],
    },
    {
        "number": 7,
        "text": "Meg is a student at a large (　). She is studying to be a nurse.",
        "choices": ["mall", "moon", "college", "example"],
    },
    {
        "number": 8,
        "text": "I always (　) care of my little sister when my mother is out. She likes to listen to my stories.",
        "choices": ["make", "give", "pick", "take"],
    },
    {
        "number": 9,
        "text": "A: Did Roger need help with the math homework?\nB: No, he did it all by (　).",
        "choices": ["him", "he", "his", "himself"],
    },
    {
        "number": 10,
        "text": "A: Oh no! The train has just left. We'll have to wait (　) 30 minutes until the next one comes.\nB: That's OK. Let's get a drink at the store.",
        "choices": ["into", "from", "at", "for"],
    },
    {
        "number": 11,
        "text": "I couldn't sleep on the flight from New York, but I (　) much better this morning. I slept really well last night.",
        "choices": ["cover", "brush", "feel", "share"],
    },
    {
        "number": 12,
        "text": "Jerry and Betty wanted to buy a new house. They looked (　) downtown, but everything was too small. They found a nice home outside of town.",
        "choices": ["off", "out", "beside", "around"],
    },
    {
        "number": 13,
        "text": "Some of the art in this airport was (　) by a famous artist.",
        "choices": ["painting", "paints", "painted", "paint"],
    },
    {
        "number": 14,
        "text": "Dr. Kobayashi (　) at a university for many years. All the students enjoyed her classes.",
        "choices": ["teaching", "to teach", "taught", "teach"],
    },
    {
        "number": 15,
        "text": "A: Are you going out, Paul?\nB: Yes. I'm going to the park (　) basketball.",
        "choices": ["practiced", "to practice", "practice", "practices"],
    },
]

section2_questions = [
    {
        "number": 16,
        "text": "Sister: Jim, could you show me how to use your computer?\nBrother: (　) This TV show will finish in 10 minutes.",
        "choices": [
            "I've played that before.",
            "It's my favorite game.",
            "I'll help you soon.",
            "It's too easy for you.",
        ],
    },
    {
        "number": 17,
        "text": "Father: Your birthday is next Saturday. (　)\nSon: I want to go ice-skating with my friends.",
        "choices": [
            "What happened at your party?",
            "How many people will come?",
            "What would you like to do?",
            "How old will you be?",
        ],
    },
    {
        "number": 18,
        "text": "Mother: Why is your baseball cap on the sofa? Take it to your room.\nSon: (　) I have practice at three.",
        "choices": [
            "We won again.",
            "Did you look for it over there?",
            "I'm going to wear it today.",
            "Will you come and watch?",
        ],
    },
    {
        "number": 19,
        "text": "Student: Mr. Clark, I can't go to baseball practice today. (　)\nTeacher: That's too bad. Please go home and rest.",
        "choices": [
            "I have a stomachache.",
            "I bought a new bat.",
            "I think we'll win.",
            "I arrived on time.",
        ],
    },
    {
        "number": 20,
        "text": "Mother: Uncle Joe will come to visit us on Sunday morning, John.\nSon: Sorry, Mom. I have baseball practice then. (　)\nMother: OK, I will.",
        "choices": [
            "Have a nice trip.",
            "Say hello to him for me.",
            "He has just left.",
            "I know he doesn't.",
        ],
    },
]

passage_3a = {
    "label": "A",
    "title": "Free Cooking Class",
    "format": "notice",
    "paragraphs": [
        "Free Cooking Class",
        "There will be a fun and free cooking class at Sunny Brook Farm. You can learn how to make delicious meals using vegetables from our farm. This class is perfect for anyone who likes cooking.",
        "Date: Saturday, June 15\nTime: 10:00 a.m. to 12:30 p.m.\nPlace: Sunny Brook Farm",
        "You do not have to bring anything with you. We will prepare all of the ingredients. To join the cooking class, please send an email to cookingclassinfo@sunnybrookfarm12345.com or call us at 555-5555-5555.",
        "For more information about our vegetables, please check our website.",
        "Let's cook with fresh vegetables and eat healthy food!",
    ],
    "questions": [
        {
            "number": 21,
            "question": "What is this notice for?",
            "choices": [
                "To introduce a new farm.",
                "To find cooking class teachers.",
                "To introduce a cooking event.",
                "To ask people to bring food.",
            ],
        },
        {
            "number": 22,
            "question": "How can people get information about the vegetables?",
            "choices": [
                "By looking at a website.",
                "By sending an email.",
                "By calling the farm.",
                "By going to a workshop.",
            ],
        },
    ],
}

passage_3b = {
    "label": "B",
    "title": "Drama club performance",
    "format": "multi-email",
    "emails": [
        {
            "meta": {
                "from": "Emma Suzuki",
                "to": "Mia Johnson",
                "date": "September 25",
                "subject": "Drama club performance",
            },
            "body": (
                "Hi Mia,\n"
                "I hope you're doing well! I wanted to remind you about my drama club performance next week. "
                "I'm so excited! The drama club practiced a lot, and now the play is finally ready. "
                "We practiced for two hours every day at school, and I practiced at home every day for an hour, too. "
                "I practiced with my dad. I'm still a little nervous, but it will be fine. "
                "The performance will be on Friday at 5 p.m. at the local theater. Can you still come? "
                "I want you to see the performance! My mom and brother are coming, too, so you can sit together. "
                "The drama club will sell snacks and drinks before the play, so my family will arrive at 4:30 p.m. "
                "and buy some snacks. I think it will be a lot of fun!\n"
                "Your friend,\n"
                "Emma"
            ),
        },
        {
            "meta": {
                "from": "Mia Johnson",
                "to": "Emma Suzuki",
                "date": "September 25",
                "subject": "Sounds fun!",
            },
            "body": (
                "Hi Emma,\n"
                "I'm doing great! Thanks for reminding me about the performance. Of course, I will go! "
                "I'm so excited! You practiced so much, so I am sure it will be very nice. "
                "What is the play about? Is it a comedy? I like comedy plays the best! "
                "My sister wants to come, too. Can we sit with your family? "
                "Also, when do we buy the tickets? Do we buy them in the theater on Friday, or before Friday? "
                "I want to buy some snacks, too, so my sister and I will arrive at 4:15 p.m. "
                "We will take the bus to the theater, and our mom will drive us home. "
                "When will the performance end?\n"
                "Your friend,\n"
                "Mia"
            ),
        },
    ],
    "questions": [
        {
            "number": 23,
            "question": "What did Emma do at home?",
            "choices": [
                "She practiced the play.",
                "She ate snacks and drank juice.",
                "She studied for a test.",
                "She played games with her father.",
            ],
        },
        {
            "number": 24,
            "question": "Who will go to the performance?",
            "choices": [
                "Mia's mother.",
                "Mia's brother.",
                "Emma's father.",
                "Emma's brother.",
            ],
        },
        {
            "number": 25,
            "question": "How will Mia go to the theater on Friday?",
            "choices": [
                "Her mother will drive her.",
                "She will walk.",
                "She will take the bus.",
                "She will take the train.",
            ],
        },
    ],
}

passage_3c = {
    "label": "C",
    "title": "Table Tennis",
    "paragraphs": [
        "Table tennis is a sport that started in England. In the 1880s, people in England played table tennis instead of tennis when the weather was bad because it was a fun way to stay active indoors. Many people enjoyed the game, and it became very popular. Soon, more people started playing table tennis in England, and then people from other countries started to play it as well.",
        "In 1926, the first world championships for table tennis were held. Players from different countries, such as Hungary, Germany, and India, went to England and played in the table tennis championships. This tournament spread the sport around the world. From around 1950, countries in Asia started playing table tennis, too. It became popular there.",
        "Table tennis became popular in many countries because it was easy to start playing. It did not cost a lot of money because it could be played with cheap items. The sport was fun for everyone, and people of all ages could play. There have been many professional table tennis players from Asia, and they have won many medals in the Olympics.",
        "In 1971, an important moment in table tennis history happened. At one of the table tennis championships in Japan, an American athlete missed his bus and got on the Chinese team's bus instead. A Chinese athlete on the bus gave him a drawing of the mountains in his country. This was a special moment for the players from both countries. Table tennis helped people from many countries to become friends.",
    ],
    "questions": [
        {
            "number": 26,
            "question": "Why did people in England play table tennis in the 1880s?",
            "choices": [
                "It was already popular in other countries.",
                "It was the only sport in England.",
                "They wanted to stay active inside.",
                "They wanted to enjoy the nice weather outside.",
            ],
        },
        {
            "number": 27,
            "question": "The first table tennis world championships were held in",
            "choices": ["England.", "Germany.", "Hungary.", "India."],
        },
        {
            "number": 28,
            "question": "Why did table tennis become popular in many countries?",
            "choices": [
                "It was a sport for only young people.",
                "It was easy for people to start playing.",
                "It was the first Olympic sport.",
                "Tickets to the competitions were very cheap.",
            ],
        },
        {
            "number": 29,
            "question": "What did a Chinese athlete do at the table tennis championship in 1971?",
            "choices": [
                "He missed his bus.",
                "He climbed a mountain.",
                "He gave an athlete a drawing.",
                "He trained an American athlete.",
            ],
        },
        {
            "number": 30,
            "question": "What is this story about?",
            "choices": [
                "Different sports in England.",
                "A famous athlete.",
                "How to learn Chinese.",
                "The history of a sport.",
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
for pa in (passage_3a, passage_3b, passage_3c):
    attach_answers(pa["questions"])

data = {
    "title": "英検3級 2026年度 第1回（土曜準会場）",
    "grade": "grade3",
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
            "type": "reading-comprehension",
            "instruction": "次のA，B，Cの内容に関して，質問に対して最も適切なもの，または文を完成させるのに最も適切なものを1，2，3，4の中から一つ選びなさい。",
            "passages": [passage_3a, passage_3b, passage_3c],
        },
    ],
    "writing": {
        "section4": {
            "type": "email-reply",
            "title": "ライティング（Eメール）",
            "prompt": {
                "from": "James",
                "body": (
                    "Hi,\n"
                    "Thank you for your e-mail.\n"
                    "Your mother says that you often write letters to your grandparents.\n"
                    "I have some questions. How many times a year do you write letters to them? "
                    "And what do you write about in your letters?\n"
                    "Your friend,\n"
                    "James"
                ),
            },
            "sampleAnswer": (
                "I write letters to my grandparents four times a year. "
                "I write about my school life. "
                "I hope they enjoy reading my letters."
            ),
        },
        "section5": {
            "type": "composition",
            "title": "ライティング（英作文）",
            "question": "Do you like to invite friends to your home?",
            "sampleAnswer": (
                "Yes, I do. I have two reasons. First, I like to play video games with my friends at home. "
                "Second, it is fun for me to do our homework together in my room."
            ),
        },
    },
    "listening": {
        "part1": {1: 3, 2: 2, 3: 2, 4: 3, 5: 2, 6: 1, 7: 2, 8: 3, 9: 3, 10: 3},
        "part2": {11: 1, 12: 4, 13: 1, 14: 4, 15: 4, 16: 2, 17: 3, 18: 3, 19: 1, 20: 3},
        "part3": {21: 2, 22: 1, 23: 4, 24: 1, 25: 4, 26: 1, 27: 2, 28: 1, 29: 2, 30: 2},
    },
}

os.makedirs(OUT_DIR, exist_ok=True)

# 既存のリッチデータ（解説・語彙・FP）を保持してマージ
if os.path.exists(OUT_PATH):
    with open(OUT_PATH, encoding="utf-8") as f:
        existing = json.load(f)
    for key in ("vocabulary", "lessonPlan"):
        if key in existing:
            data[key] = existing[key]
    # 各セクションは grammar 等があれば上書きしない
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
        elif new_sec.get("type") == "reading-comprehension":
            old_ps = {p.get("label"): p for p in old_sec.get("passages", [])}
            for p in new_sec.get("passages", []):
                op = old_ps.get(p.get("label"), {})
                if op.get("translations"):
                    p["translations"] = op["translations"]
                if op.get("paragraphs"):
                    p["paragraphs"] = op["paragraphs"]
                for em, oe in zip(p.get("emails", []), op.get("emails", [])):
                    if oe.get("translation"):
                        em["translation"] = oe["translation"]
                old_qq = {q["number"]: q for q in op.get("questions", [])}
                for q in p.get("questions", []):
                    oq = old_qq.get(q["number"], {})
                    if oq.get("grammar"):
                        q.clear()
                        q.update(oq)

order = (
    "grade", "year", "session", "title", "exam",
    "sections", "writing", "listening", "vocabulary", "lessonPlan",
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
print(f"  reading questions: 30")
if "vocabulary" in data:
    print(f"  vocabulary: {len(data['vocabulary'])} (preserved)")
if "lessonPlan" in data:
    print(f"  lessonPlan: {len(data['lessonPlan'].get('focusPoints', []))} FPs (preserved)")

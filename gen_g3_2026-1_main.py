# -*- coding: utf-8 -*-
"""
2026年度 第1回（本会場）英検3級
推論なしOCR原本 → data.json（リーディング Q1〜30）
一次ソース: 2026-1(本会場）/3級.pdf / 3級解答.pdf
"""
import json
import os
import sys
from collections import OrderedDict

sys.stdout.reconfigure(encoding="utf-8")

OUT_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade3", "2026-1",
)
OUT_PATH = os.path.join(OUT_DIR, "data.json")

# 公式解答（解答PDF リーディング）
ANSWERS = {
    1: 3, 2: 3, 3: 1, 4: 2, 5: 2, 6: 1, 7: 4, 8: 4, 9: 2, 10: 2,
    11: 1, 12: 4, 13: 3, 14: 3, 15: 1,
    16: 2, 17: 3, 18: 4, 19: 2, 20: 4,
    21: 1, 22: 4,
    23: 1, 24: 2, 25: 3,
    26: 1, 27: 2, 28: 4, 29: 3, 30: 2,
}

section1_questions = [
    {
        "number": 1,
        "text": "A: What do you like to do on weekends, Bob?\nB: I like to (　) at home. I often watch a movie.",
        "choices": ["move", "plan", "relax", "grow"],
    },
    {
        "number": 2,
        "text": "A: Your shoes are so (　), John.\nB: I know. I have to clean them.",
        "choices": ["clever", "common", "dirty", "foolish"],
    },
    {
        "number": 3,
        "text": "A: What happened to your leg, Bob?\nB: I had an (　). I fell down the stairs this morning.",
        "choices": ["accident", "advice", "adult", "addition"],
    },
    {
        "number": 4,
        "text": "A: What is that building?\nB: It's the library. It's a (　) of our city.",
        "choices": ["sand", "symbol", "condition", "bottle"],
    },
    {
        "number": 5,
        "text": "Mr. Jones went to a nice restaurant with his family. He (　) some cake for dessert.",
        "choices": ["arrived", "ordered", "taught", "believed"],
    },
    {
        "number": 6,
        "text": "The tomato soup that Mike made didn't (　) good. It was too salty.",
        "choices": ["taste", "carry", "find", "serve"],
    },
    {
        "number": 7,
        "text": "A: It is a nice day today. Open the (　), John.\nB: OK, Mom.",
        "choices": ["sentence", "stadium", "florist", "curtain"],
    },
    {
        "number": 8,
        "text": "I want a computer that is small (　) to put in my backpack.",
        "choices": ["again", "more", "never", "enough"],
    },
    {
        "number": 9,
        "text": "A: Why did you (　) away your green sweater?\nB: It was really old.",
        "choices": ["fall", "throw", "hope", "shop"],
    },
    {
        "number": 10,
        "text": "On his way home from work, Jack gets (　) the bus before his stop. He likes to walk for 30 minutes after sitting all day.",
        "choices": ["again", "off", "up", "in"],
    },
    {
        "number": 11,
        "text": "A: Dad, can you give me a (　) with my new TV? I need to bring it upstairs.\nB: Just a minute.",
        "choices": ["hand", "face", "leg", "foot"],
    },
    {
        "number": 12,
        "text": "Ethan lives far (　) school, so he has to take the bus.",
        "choices": ["along", "below", "under", "from"],
    },
    {
        "number": 13,
        "text": "Jack finished (　) his room and then went to his friend's house.",
        "choices": ["clean", "cleaned", "cleaning", "cleans"],
    },
    {
        "number": 14,
        "text": "Ken watched TV until twelve o'clock last night. His mother told him (　) to bed earlier.",
        "choices": ["going", "went", "to go", "goes"],
    },
    {
        "number": 15,
        "text": "Ellen is good at (　). Her friends enjoy going to her house and eating her delicious food.",
        "choices": ["cooking", "to cook", "cooked", "cooks"],
    },
]

section2_questions = [
    {
        "number": 16,
        "text": "Boy: I'm planning to go to Paris this summer. (　)\nGirl: Yes, it's a very beautiful place.",
        "choices": [
            "Would you like some?",
            "Have you ever been there?",
            "Did you find your bag?",
            "How much are the tickets?",
        ],
    },
    {
        "number": 17,
        "text": "Man: Why don't we play tennis together on Saturday?\nWoman: (　) I was thinking the same thing.",
        "choices": [
            "Have a nice time.",
            "It'll be here soon.",
            "That sounds great.",
            "I can't understand.",
        ],
    },
    {
        "number": 18,
        "text": "Mother: Samantha, dinner is ready. Come downstairs.\nDaughter: OK, Mom. (　)",
        "choices": [
            "I'm too busy.",
            "I'll call you soon.",
            "I'm going tomorrow.",
            "I'll be there in a minute.",
        ],
    },
    {
        "number": 19,
        "text": "Wife: You're not eating your breakfast. (　)\nHusband: I'm just not hungry.",
        "choices": [
            "Are they your friends?",
            "What's the matter?",
            "Can you do it alone?",
            "Do you have any?",
        ],
    },
    {
        "number": 20,
        "text": "Man 1: Excuse me. I think you're wearing my jacket.\nMan 2: Oh, (　) It looks like mine.",
        "choices": [
            "it's my pleasure.",
            "I decided to go.",
            "I'll speak to him now.",
            "I'm very sorry.",
        ],
    },
]

passage_3a = {
    "label": "A",
    "title": "Mr. Chen's Cooking Classes",
    "format": "notice",
    "paragraphs": [
        "Mr. Chen's Cooking Classes",
        "Are you interested in traditional Chinese dishes?",
        "Next March, Evansfield Cultural Center will hold cooking classes for people who want to learn about Chinese recipes. We will invite Mr. Chen as a special teacher.",
        "●Remember to bring an apron and a notebook.",
        "Place\nEvansfield Cultural Center",
        "Classes\n(For adults) Fridays, 7:00 p.m. to 9:00 p.m.\n(For teenagers) Saturdays, 2:00 p.m. to 3:30 p.m.",
        "About the teacher\nMr. Chen is one of the best chefs in our city. He has won some international cooking contests. He was also chosen as Great Young Chef of the Year last year.",
    ],
    "questions": [
        {
            "number": 21,
            "question": "What should the members of the classes do?",
            "choices": [
                "Bring a notebook.",
                "Wash the dishes after cooking.",
                "Buy Mr. Chen's recipe book.",
                "Learn to speak Chinese.",
            ],
        },
        {
            "number": 22,
            "question": "Mr. Chen is a chef who",
            "choices": [
                "gave lessons to students online.",
                "taught teenagers on Saturday mornings.",
                "invited his friends to the cooking classes.",
                "won some cooking contests.",
            ],
        },
    ],
}

passage_3b = {
    "label": "B",
    "title": "Winter sale",
    "format": "multi-email",
    "emails": [
        {
            "meta": {
                "from": "Judy Smith",
                "to": "Ann Smith",
                "date": "December 8",
                "subject": "Winter sale",
            },
            "body": (
                "Dear Grandma,\n"
                "Thank you for giving me a lovely present last month. I really like the wallet!\n"
                "Yesterday, I visited a department store near the station. They were having a winter sale! "
                "You said you wanted a brown sweater, right? I looked for one, but I couldn't find any brown ones. "
                "However, I saw a nice scarf and bought it for you! I also bought a coat for myself. "
                "Can I bring the scarf to you? Will you be home this Saturday?\n"
                "Write back soon,\n"
                "Judy"
            ),
        },
        {
            "meta": {
                "from": "Ann Smith",
                "to": "Judy Smith",
                "date": "December 8",
                "subject": "Thank you!",
            },
            "body": (
                "Dear Judy,\n"
                "I am glad to hear that you like the wallet. I found it at a shopping mall next to the museum. "
                "Thank you for the scarf! Yes, I will be home this Saturday, and my old friend Linda will also visit my house that day! "
                "I have not seen her since she moved to another city two years ago. Do you remember her? "
                "You often met her at my house when you were little. You can see her this Saturday if you come here. "
                "By the way, will your mom come with you that day?\n"
                "Love,\n"
                "Grandma"
            ),
        },
        {
            "meta": {
                "from": "Judy Smith",
                "to": "Ann Smith",
                "date": "December 8",
                "subject": "Great!",
            },
            "body": (
                "Dear Grandma,\n"
                "Yes, I remember Linda! She was very kind to me! Linda often told me stories when you were cooking in the kitchen. "
                "They were so interesting! I want to meet her, too! But my mom cannot come with me that day because she has to work. "
                "I will visit you alone by bus. Yesterday, I also found a new cake shop near the park, "
                "so I will buy some cakes for you and Linda before I visit your house.\n"
                "See you soon,\n"
                "Judy"
            ),
        },
    ],
    "questions": [
        {
            "number": 23,
            "question": "What did Judy do at the department store yesterday?",
            "choices": [
                "She bought a coat and a scarf.",
                "She found a nice wallet.",
                "She bought a brown sweater.",
                "She worked as a staff member.",
            ],
        },
        {
            "number": 24,
            "question": "Judy's grandmother bought the wallet",
            "choices": [
                "at a shop in the park.",
                "at a shopping mall beside the museum.",
                "at a shop next to her house.",
                "at a department store in Linda's city.",
            ],
        },
        {
            "number": 25,
            "question": "What did Judy often do when her grandmother was cooking?",
            "choices": [
                "She shared a cake with Linda.",
                "She visited a park with her mother.",
                "She listened to Linda's stories.",
                "She helped her grandmother in the kitchen.",
            ],
        },
    ],
}

passage_3c = {
    "label": "C",
    "title": "Never Too Late",
    "paragraphs": [
        "Anna Mary Robertson Moses, also known as Grandma Moses, was an American artist. She was born in 1860 on a farm in New York. As a girl, Anna worked hard on the farm and took care of her family. She liked to play outside with her brothers in her free time. She also loved making things with her hands. She often enjoyed drawing pictures on paper her father bought for her.",
        "Anna married Thomas Moses in 1887 and lived on the local farm she loved. Even after Thomas died in 1927, she kept working on her farm with the help of her youngest son. But when she got older, it was hard for her to do some things on the farm because her hands hurt. So, she decided to try painting instead. She was already over seventy-five years old then.",
        "Anna painted all the things she loved from her farm life. She often painted green fields, snowy winters, and happy people living in nature. Her paintings were so unique and full of happiness that a lot of people wanted to see them. They felt so warm and happy when they saw her works painted in a simple way with many colors.",
        "Anna kept painting until about 1960. She created more than 1,500 works of art in her life, and her paintings became popular across the country. Even today, many people come to see her paintings in museums. Anna and her paintings show that anyone can try something new at any time in their life.",
    ],
    "questions": [
        {
            "number": 26,
            "question": "What did Anna like when she was a child?",
            "choices": [
                "Drawing on paper.",
                "Taking pictures.",
                "Buying gifts for her father.",
                "Playing games at home.",
            ],
        },
        {
            "number": 27,
            "question": "Why did Anna begin painting?",
            "choices": [
                "She had to teach art to her son.",
                "She had a problem with her hands.",
                "She did not want to look old.",
                "She did not enjoy living on her farm.",
            ],
        },
        {
            "number": 28,
            "question": "The paintings Anna created",
            "choices": [
                "made her much poorer.",
                "made people free.",
                "were sold to farmers.",
                "had a lot of colors.",
            ],
        },
        {
            "number": 29,
            "question": "What did Anna do in her life?",
            "choices": [
                "She tried to travel across America.",
                "She invented new colors.",
                "She created many works of art.",
                "She built a famous museum.",
            ],
        },
        {
            "number": 30,
            "question": "What is this story about?",
            "choices": [
                "A woman who loved her grandmother.",
                "A popular artist in America.",
                "How to live on a farm.",
                "How to help older people.",
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
    "title": "英検3級 2026年度 第1回",
    "grade": "grade3",
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
                    "I heard that you came back from India yesterday. I have some questions for you. "
                    "What did you do during your flight from India? And what time did you return to your house yesterday?\n"
                    "Your friend,\n"
                    "James"
                ),
            },
            "sampleAnswer": (
                "I watched some movies during my flight from India. "
                "I returned home at ten o'clock last night. "
                "I had a good time on the flight."
            ),
        },
        "section5": {
            "type": "composition",
            "title": "ライティング（英作文）",
            "question": "Do you like to get up early in winter?",
            "sampleAnswer": (
                "Yes, I do. I have two reasons. First, I can study better on quiet early mornings in winter. "
                "Second, I feel good when I spend time in the park on sunny winter mornings."
            ),
        },
    },
    "listening": {
        "part1": {1: 1, 2: 1, 3: 2, 4: 2, 5: 1, 6: 2, 7: 3, 8: 1, 9: 3, 10: 2},
        "part2": {11: 2, 12: 3, 13: 3, 14: 3, 15: 1, 16: 4, 17: 3, 18: 3, 19: 1, 20: 1},
        "part3": {21: 1, 22: 4, 23: 1, 24: 1, 25: 4, 26: 1, 27: 3, 28: 2, 29: 2, 30: 4},
    },
}

os.makedirs(OUT_DIR, exist_ok=True)

if os.path.exists(OUT_PATH):
    with open(OUT_PATH, encoding="utf-8") as f:
        existing = json.load(f)
    for key in ("vocabulary", "lessonPlan"):
        if key in existing:
            data[key] = existing[key]

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

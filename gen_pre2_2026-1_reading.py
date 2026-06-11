# -*- coding: utf-8 -*-
"""
2026年度 第1回（本会場）英検準2級
推論なしOCR原本 → data.json（リーディング Q1〜29 + リスニング正答）
一次ソース: 2026-1(本会場）/準2級.pdf / 準2級解答.pdf
"""
import json
import os
import sys
from collections import OrderedDict

sys.stdout.reconfigure(encoding="utf-8")

OUT_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade-pre2", "2026-1",
)
OUT_PATH = os.path.join(OUT_DIR, "data.json")

ANSWERS = {
    1: 2, 2: 1, 3: 1, 4: 4, 5: 4, 6: 3, 7: 2, 8: 3, 9: 4, 10: 1,
    11: 2, 12: 4, 13: 1, 14: 1, 15: 2,
    16: 1, 17: 3, 18: 2, 19: 1, 20: 3,
    21: 4, 22: 1, 23: 3, 24: 4, 25: 3, 26: 3, 27: 4, 28: 2, 29: 3,
}

DIALOGUE_19_20 = (
    "A : Dad, where's my lunch? I need to take it to school today.\n"
    "B : Lunch? But you ( 19 ). Why do you need to bring your own?\n"
    "A : From today, the cafeteria will be closed for repairs, and everyone must bring their own lunch. "
    "Didn't you see the letter from school? I gave it to you last week.\n"
    "B : Hmm. Maybe I missed it. When will the cafeteria open again?\n"
    "A : Not until next Monday. So, do you have time to make it now?\n"
    "B : I don't think so. Can you ( 20 ) today?\n"
    "A : OK. I'll stop by my favorite bakery. But please don't forget to make my lunch for the rest of the week.\n"
    "B : Alright, I won't."
)

section1_questions = [
    {
        "number": 1,
        "text": "A: Michael, this meal is ( ) delicious! It's the best pasta that I've ever eaten.\nB: Really? I'm glad you like it.",
        "choices": ["nervously", "absolutely", "rarely", "separately"],
    },
    {
        "number": 2,
        "text": "Dennis was recently ( ) to his company's New York office. He likes his new apartment and is slowly finding out about the city.",
        "choices": ["transferred", "reduced", "proposed", "apologized"],
    },
    {
        "number": 3,
        "text": "Today, Mr. Carter taught his students about the ( ) of smoking. The students learned about the health problems it can cause.",
        "choices": ["dangers", "palaces", "markets", "galleries"],
    },
    {
        "number": 4,
        "text": "A: Why did you choose that hotel for our vacation?\nB: It had good reviews, and the price seemed ( ) compared to other options.",
        "choices": ["wooden", "boring", "cute", "reasonable"],
    },
    {
        "number": 5,
        "text": "At the start of the lesson, Mr. Harris made an ( ). He told the class that a student teacher would be teaching his lessons for the next few weeks.",
        "choices": ["award", "aisle", "attempt", "announcement"],
    },
    {
        "number": 6,
        "text": "The mayor has asked several local artists to create ( ) that will be put in the city's parks. The artists have been told that they can use either metal or stone.",
        "choices": ["policies", "blankets", "statues", "insects"],
    },
    {
        "number": 7,
        "text": "When Adam buys expensive items, he always keeps the ( ) in a safe place. That way, he can return an item if it has a problem.",
        "choices": ["battery", "receipt", "website", "frame"],
    },
    {
        "number": 8,
        "text": "People can ( ) their friends to support them during difficult times and help them find solutions.",
        "choices": ["paste", "blame", "trust", "scratch"],
    },
    {
        "number": 9,
        "text": "A: How many points did you ( ) in the math test?\nB: Only 50 out of 100. I did really badly.",
        "choices": ["enter", "engage", "claim", "score"],
    },
    {
        "number": 10,
        "text": "After running ten kilometers, Evan's legs started to ( ). He sat down to rest and did some leg stretching exercises.",
        "choices": ["ache", "soothe", "push", "gather"],
    },
    {
        "number": 11,
        "text": "Almost all the pets in the shelter found homes, ( ) one dog that was still waiting for a family.",
        "choices": ["next to", "except for", "across from", "up to"],
    },
    {
        "number": 12,
        "text": "A: ( )! There's a bee near your face!\nB: Oh, I didn't see it. Thanks for letting me know.",
        "choices": ["Get on", "Take off", "Give up", "Look out"],
    },
    {
        "number": 13,
        "text": "A: Dad, can I have a new smartphone for my birthday this year?\nB: No, that's ( ), Megan. Your birthday is next month, and you just got a new one last month.",
        "choices": ["out of the question", "up in the air", "in a good temper", "none of your business"],
    },
    {
        "number": 14,
        "text": "A: Have you decided which club to join, Chris?\nB: No. I can't ( ). They all seem so interesting.",
        "choices": ["make up my mind", "get off my back", "go on a voyage", "put out the light"],
    },
    {
        "number": 15,
        "text": "Before buying a new smartphone, you should ( ) several different ones. That way, you can find one that is right for you.",
        "choices": ["make a start on", "take a look at", "do a favor for", "have a word with"],
    },
]

section2_questions = [
    {
        "number": 16,
        "text": (
            "A: Excuse me. Do you know the way to the Greenlake Theater?\n"
            "B: Yes. Go straight down this street, then turn right at the second light. After that, walk for about five minutes. The theater will be on your left.\n"
            "A: Thanks. I'm not sure if I can get there, but I'll try.\n"
            "B: Well, I'm going in the same direction, so ( 16 ). Please follow me."
        ),
        "choices": [
            "I can take you there",
            "I can take the wrong way",
            "you won't make it",
            "you won't see me again",
        ],
    },
    {
        "number": 17,
        "text": (
            "A: Lucas, which gym do you go to? I'm thinking about joining one.\n"
            "B: That's great! I go to the one next to the supermarket, but there's a new one closer to your place. It just opened last month.\n"
            "A: Oh, where is it?\n"
            "B: It's right across from the movie theater. It's ( 17 ). I haven't been there, but people say it's good."
        ),
        "choices": [
            "the closest to the supermarket",
            "only about one year old",
            "about five minutes from your house",
            "too noisy and small for real training",
        ],
    },
    {
        "number": 18,
        "text": (
            "A: Hello. I'd like to sign up for one of the volunteer programs this summer.\n"
            "B: Of course! May I ask ( 18 )? We have plenty to choose from.\n"
            "A: Sure. Is \"Let's Work as a Librarian\" still open? I believe it begins on August 10.\n"
            "B: Let me check. Yes, it's still available. Please go ahead and fill out this form."
        ),
        "choices": [
            "how you learned about our programs",
            "which program you're interested in",
            "what kinds of books you enjoy reading",
            "when your summer vacation finishes",
        ],
    },
    {
        "number": 19,
        "text": DIALOGUE_19_20,
        "choices": [
            "usually eat at the cafeteria",
            "always make your own lunch",
            "didn't wake up early enough",
            "don't have school today",
        ],
    },
    {
        "number": 20,
        "text": DIALOGUE_19_20,
        "choices": [
            "ask your teacher to make it",
            "eat at the school cafeteria",
            "buy something on your way",
            "make something by yourself",
        ],
    },
]

passage_3 = {
    "label": "",
    "title": "The Advice",
    "paragraphs": [
        "Haruto is a high school student in Tokyo. Although he enjoyed studying English, he was always afraid to speak the language. He worried that he might be embarrassed if his English was wrong. One day, he talked with his older sister, who spoke English very well. She told him that there was ( 21 ). She even explained that it was a necessary step to improve his skills. Thanks to her, Haruto's attitude toward speaking English changed.",
        "One day, his teacher, Ms. Sato, gave a speech activity in her English class. Haruto still felt worried, but he decided to do his best. When his turn came, he stood up and spoke clearly, despite feeling nervous. He knew that ( 22 ). When he finished the whole speech, however, Ms. Sato smiled and said his speech was very good. She also explained how he could make it even better. From that day, he began to enjoy speaking English.",
    ],
    "questions": [
        {
            "number": 21,
            "choices": [
                "no need to speak English",
                "only one way for language learning",
                "something more important than trying hard",
                "nothing wrong with making mistakes",
            ],
        },
        {
            "number": 22,
            "choices": [
                "his speech was not perfect",
                "his classmate made the same mistake",
                "he could not continue his speech",
                "he had forgotten his speech",
            ],
        },
    ],
}

passage_4a = {
    "label": "A",
    "title": "About joining my band",
    "format": "email",
    "meta": {
        "from": "Andrea Patterson <andrea123@ground-mail.com>",
        "to": "Travis Longman <t.j.longman-0428@skyhigh-message.com>",
        "date": "February 20",
        "subject": "About joining my band",
    },
    "paragraphs": [
        "Dear Travis,\nThis is Andrea Patterson. Thanks for your message. It is great to hear that you are interested in joining our band as a guitarist. As you said in your email, we were looking for a new member. However, we just found someone last week. So, unfortunately, we will not be able to include you in our band. I am sorry to say that because I know how well you can play the guitar.",
        "However, I do have some good news for you. I know another band whose members are still looking for a good guitarist. They are also students at our college. While they do not cover famous songs, they perform original music. The band started last year, but last week, the guitarist had to quit the band because he needed to focus on his studies. They usually practice on weekends in the music room on campus.",
        "If you are interested, you can give me your phone number, and I will pass it to them. You could also exchange emails if you prefer, but I think it might be easier to talk with them directly on the phone. They can tell you more about the band. Then, you can go watch one of their practices to see if you like their music. Let me know what you think.\nThank you,\nAndrea Patterson",
    ],
    "questions": [
        {
            "number": 23,
            "question": "Travis Longman cannot join Andrea Patterson's band because",
            "choices": [
                "she thinks he is not good enough for her band.",
                "her band is only looking for a singer, not a guitarist.",
                "she has already found a new member for the band.",
                "her band had already broken up by the time he asked.",
            ],
        },
        {
            "number": 24,
            "question": "What is true about the band members that Andrea recommends?",
            "choices": [
                "They prefer to play songs from other bands.",
                "They have been active for several years.",
                "They practice in a studio outside the campus.",
                "They have been seeking a new guitarist.",
            ],
        },
        {
            "number": 25,
            "question": "What will Travis probably do right after reading this email?",
            "choices": [
                "Send an email to one of the band members.",
                "Go check out the practice of the recommended band.",
                "Provide his phone number to Andrea.",
                "Call Andrea for information about the band.",
            ],
        },
    ],
}

passage_4b = {
    "label": "B",
    "title": "Pig Beach",
    "paragraphs": [
        "Big Major Cay in the country of the Bahamas is a small island with a beautiful beach known as Pig Beach. On this island, visitors can see and sometimes play with pigs swimming near the beach. In recent years, these pigs have gained popularity worldwide because of social media. This has led many tourists to visit the island to see this unique sight. As a result, this has had some negative impact on these animals.",
        "These pigs are not native to the island, and nobody knows exactly how they arrived there. One story says that old sailors left their pigs on the island. Another story suggests that the pigs swam to the island after escaping from a broken ship. Some people believe the pigs were brought there by farmers from a nearby island. In any case, after these pigs learned that humans, especially tourists today, would feed them, they made the place their home.",
        "Today, tourists who come to see the pigs sometimes cause problems. They often give the pigs various kinds of food, but much of it is not good for their health. This could make the pigs sick. Some reports said that pigs ate harmful items, such as plastic. In the past, some of the pigs died after people fed them on the beach, as they had also eaten too much sand with the food.",
        "To protect the pigs, several organizations and the local government are taking action. For example, they have started campaigns to educate tourists on how to behave properly around the swimming pigs. They are also cleaning up the beach and making stricter rules on feeding the pigs. They aim to improve the situation for both the pigs and the environment through more eco-friendly tourism. These events have also made people reconsider how humans should interact with wild animals.",
    ],
    "questions": [
        {
            "number": 26,
            "question": "What is true about Big Major Cay?",
            "choices": [
                "Social media has made it famous for its large, beautiful beach.",
                "There are pigs living there without any contact with humans.",
                "This island, where pigs live, offers tourists a very unusual view.",
                "It experienced a drop in tourists in recent years due to the pigs.",
            ],
        },
        {
            "number": 27,
            "question": "One possible explanation for the pigs being on the island is that",
            "choices": [
                "people brought them to attract tourists.",
                "a broken ship landed there with them inside.",
                "they originally came from this island.",
                "sailors brought them but left them behind.",
            ],
        },
        {
            "number": 28,
            "question": "How are the pigs affected by tourists?",
            "choices": [
                "They feel stressed when tourists touch them carelessly.",
                "They are fed food that is not good for them to eat.",
                "Their homes are being destroyed because of plastic trash.",
                "Too many tourists drive them away from their homes.",
            ],
        },
        {
            "number": 29,
            "question": "What was done to protect the pigs on the island?",
            "choices": [
                "The government provided locals with information on how to handle them.",
                "The government made a rule that no tourists could go to the island.",
                "Some groups were working to teach tourists how to treat them correctly.",
                "Some groups were cleaning the beach without the help of the government.",
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
attach_answers(passage_3["questions"])
for pa in (passage_4a, passage_4b):
    attach_answers(pa["questions"])

data = {
    "title": "2026年度 第1回 英語資格検定準2級 リーディング",
    "grade": "準2級",
    "exam": "2026-1",
    "year": "2026",
    "session": "1",
    "sections": [
        {
            "name": "大問1",
            "nameEn": "Part 1",
            "type": "vocabulary",
            "instruction": "次の(1)から(15)までの(　)に入れるのに最も適切なものを1, 2, 3, 4の中から一つ選び、その番号を解答用紙の所定欄にマークしなさい。",
            "questions": section1_questions,
        },
        {
            "name": "大問2",
            "nameEn": "Part 2",
            "type": "vocabulary",
            "instruction": "次の四つの会話文を完成させるために，(16)から(20)に入るものとして最も適切なものを1，2，3，4の中から一つ選びなさい。",
            "questions": section2_questions,
        },
        {
            "name": "大問3",
            "nameEn": "Part 3",
            "type": "passage-fill",
            "instruction": "次の英文を読み，その文意にそって(21)と(22)の(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選びなさい。",
            "passages": [passage_3],
        },
        {
            "name": "大問4",
            "nameEn": "Part 4",
            "type": "reading-comprehension",
            "instruction": "次の英文Ａ，Ｂの内容に関して，(23)から(29)までの質問に対して最も適切なもの，または文を完成させるのに最も適切なものを1，2，3，4の中から一つ選びなさい。",
            "passages": [passage_4a, passage_4b],
        },
    ],
    "listening": {
        "part1": {
            1: 1, 2: 1, 3: 1, 4: 3, 5: 2, 6: 1, 7: 3, 8: 3, 9: 3, 10: 1,
        },
        "part2": {
            11: 3, 12: 3, 13: 4, 14: 1, 15: 4, 16: 2, 17: 1, 18: 2, 19: 1, 20: 4,
        },
        "part3": {
            21: 3, 22: 3, 23: 2, 24: 2, 25: 2, 26: 1, 27: 2, 28: 2, 29: 3, 30: 4,
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

order = ("grade", "year", "session", "title", "exam", "sections", "listening", "vocabulary", "lessonPlan")
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
print("  reading questions: 29")

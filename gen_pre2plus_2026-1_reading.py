# -*- coding: utf-8 -*-
"""
2026年度 第1回（本会場）英検準2級プラス
推論なしOCR原本 → data.json（リーディング Q1〜31 + リスニング正答）
一次ソース:
  試験24頁 → 2026-1(本会場）/準2級プラス解答.pdf
  解答1頁 → 2026-1(本会場）/準2級プラス.pdf
"""
import json
import os
import sys
from collections import OrderedDict

sys.stdout.reconfigure(encoding="utf-8")

OUT_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade-pre2plus", "2026-1",
)
OUT_PATH = os.path.join(OUT_DIR, "data.json")

ANSWERS = {
    1: 4, 2: 1, 3: 3, 4: 4, 5: 4, 6: 4, 7: 3, 8: 4, 9: 1, 10: 4,
    11: 1, 12: 3, 13: 1, 14: 3, 15: 4, 16: 3, 17: 3,
    18: 2, 19: 4, 20: 3, 21: 1, 22: 2, 23: 4,
    24: 3, 25: 2, 26: 3, 27: 1, 28: 4, 29: 3, 30: 4, 31: 2,
}

section1_questions = [
    {
        "number": 1,
        "text": "A: Excuse me. I wanted to buy a pair of tennis shoes, but I couldn't find any on the shelf.\nB: Let me check our ( ). One moment, please.",
        "choices": ["permission", "audience", "horizon", "inventory"],
    },
    {
        "number": 2,
        "text": "Many people in Japan do not follow any ( ), but they often take part in traditional festivals that come from the beliefs of ancient Japanese people.",
        "choices": ["religion", "condition", "enthusiasm", "progress"],
    },
    {
        "number": 3,
        "text": "Scientists are worried about the ( ) of gases from cars. They think that these gases are bad for the environment.",
        "choices": ["principal", "shortage", "emission", "custom"],
    },
    {
        "number": 4,
        "text": "A: Did you buy batteries for the camera?\nB: Yes, and I also bought some extra ones to ( ) that we don't run out.",
        "choices": ["express", "stare", "greet", "ensure"],
    },
    {
        "number": 5,
        "text": "A: What are you going to do this weekend, Karen?\nB: I'm going to ( ) some friends at my house. We're going to have a party.",
        "choices": ["repair", "wander", "explain", "entertain"],
    },
    {
        "number": 6,
        "text": "A: What did you do in your camping class today, Bill?\nB: We learned about the ( ) skills needed for camping, like building a shelter and starting a fire.",
        "choices": ["guarantee", "wealth", "affection", "survival"],
    },
    {
        "number": 7,
        "text": "A: I'm going to go to Canada next month. I hope I don't have any problems with the money.\nB: You should ( ) some Japanese yen to Canadian dollars before you go.",
        "choices": ["protect", "imagine", "convert", "detect"],
    },
    {
        "number": 8,
        "text": "Tom is very good at drawing people's faces. He can ( ) their emotions so well that it is easy to see how each person was feeling when Tom drew them.",
        "choices": ["exclude", "shoot", "cure", "portray"],
    },
    {
        "number": 9,
        "text": "A: Look at the man. He fell off his bicycle.\nB: He was going too fast. You have to go at a ( ) pace, Mike.",
        "choices": ["steadier", "braver", "freer", "politer"],
    },
    {
        "number": 10,
        "text": "The weather in Russia is ( ) cold in winter. In Moscow, the average temperature in January is around -10 degrees Celsius.",
        "choices": ["publicly", "briefly", "shortly", "extremely"],
    },
    {
        "number": 11,
        "text": "A: My computer is really old. I hope it doesn't ( ) before I finish my report.\nB: I hope so, too. It would be a disaster.",
        "choices": ["break down", "dress up", "look around", "shake off"],
    },
    {
        "number": 12,
        "text": "Before writing his novel, Michael had to ( ) a lot of research. He spent many hours reading books and searching on the Internet.",
        "choices": ["decide on", "come up", "go through", "consent to"],
    },
    {
        "number": 13,
        "text": "The new president has made some changes to the way the company is run. ( ), the changes seem to be working well.",
        "choices": ["So far", "For free", "As well", "In vain"],
    },
    {
        "number": 14,
        "text": "A: What will you do if your boss says no when you ask for time off?\nB: I'll go to the beach ( ) he says no. I need a break!",
        "choices": ["as though", "only if", "even if", "only when"],
    },
    {
        "number": 15,
        "text": "The city of Ironton is not very big, but it is easy to get to ( ) a new highway that connects it to the larger city of Winsterville.",
        "choices": ["for fear of", "for the sake of", "in case of", "by way of"],
    },
    {
        "number": 16,
        "text": "A: I'm sorry. I'm not very good at this game.\nB: It's OK. Just sit ( ) me, and I'll show you how to play.",
        "choices": ["aware of", "apart of", "next to", "short of"],
    },
    {
        "number": 17,
        "text": "A: I'm going to the supermarket. Do you need anything?\nB: No, thanks. But ( ) to borrow my car if you want to.",
        "choices": ["try hard", "devote yourself", "feel free", "take turns"],
    },
]

passage_2a = {
    "label": "A",
    "title": "Guide Signs Without Words",
    "paragraphs": [
        "Pictograms are a type of guide sign. They do not depend on language. This is because they use images instead of words to share information. Therefore, problems ( 18 ) can be avoided. This makes pictograms useful for people around the world because they can easily and quickly understand what the images mean. Today, pictograms can be found in many fields of daily life, such as transportation, tourism, and weather. One of the most common situations where they appear is at the Olympic Games.",
        "Pictograms were first used as signs for many sports and some events in the Olympic Games many years ago. For example, the Games in Paris in 1924 and London in 1948 used pictograms on tickets and programs. However, there was one ( 19 ). They were often too complex in style and too detailed, which made them difficult to understand quickly. This fact clearly showed the need for simpler and more effective visual communication at international events.",
        "A major change in pictograms was introduced at the 1964 Tokyo Olympic Games. Unlike earlier versions, the design team at the time tried to create much simpler pictograms while still showing the meaning without words. These new pictograms were used to guide visitors, athletes, and staff members throughout the event. Their success demonstrated how effective simple visual communication could be. ( 20 ), a new standard for pictograms was set. Since then, pictograms have continued to play an important role in supporting the Olympic Games.",
    ],
    "questions": [
        {
            "number": 18,
            "choices": [
                "influenced through social media",
                "caused by language differences",
                "shown in large pictures",
                "related to written construction",
            ],
        },
        {
            "number": 19,
            "choices": [
                "celebration of the Olympic spirit",
                "example of modern art",
                "reason for using colors",
                "issue with the early designs",
            ],
        },
        {
            "number": 20,
            "choices": ["To begin with", "Most of all", "In this way", "Especially"],
        },
    ],
}

passage_2b = {
    "label": "B",
    "title": "Attention Span",
    "paragraphs": [
        "According to a study conducted by an IT company, humans have shorter attention spans than they did in the past. In fact, the study suggests people cannot focus as long as a goldfish. One key reason for this is mobile phones. Today, many people use social media platforms that show short videos and messages. These platforms hardly require a long attention span. ( 21 ), the human brain becomes used to receiving only small amounts of information. People find it hard to stop using these platforms. This makes the problem even worse.",
        "The impact of shorter attention spans on young students seems very large. Another study showed that about 30 percent of teenagers reported difficulty focusing in class because they often checked their mobile phones. The negative effects of mobile-phone use are also seen in other parts of people's lives. Problems can even occur when people are ( 22 ). For example, people who often use their mobile phones are less likely to stay focused on reading books or remembering information, and giving up is getting easier for them.",
        "Some experts suggest a few solutions to help people maintain a longer attention span. A simple approach is to take regular breaks. It is said to be important to avoid a state where people get mentally too tired and lose control of their attention. In addition, understanding ( 23 ) is considered helpful. This means people should know when they can and cannot focus during the day. That will help people plan their day and perform their tasks successfully.",
    ],
    "questions": [
        {
            "number": 21,
            "choices": ["As a result", "Even so", "On the other hand", "Fortunately"],
        },
        {
            "number": 22,
            "choices": [
                "not studying at home",
                "not using their phones",
                "sleeping well at night",
                "trying to find their phones",
            ],
        },
        {
            "number": 23,
            "choices": [
                "their sleeping patterns",
                "their preferred study location",
                "personal eating habits",
                "personal attention rhythms",
            ],
        },
    ],
}

passage_3a = {
    "label": "A",
    "title": "Apartment viewing information",
    "format": "email",
    "meta": {
        "from": "Lucy Henderson <service@cmw-apartments.com>",
        "to": "Nick King <n.king-0328@zero-borders.com>",
        "date": "July 29",
        "subject": "Apartment viewing information",
    },
    "paragraphs": [
        "Dear Nick,\nMy name is Lucy Henderson, and I work for CMW Apartments. Thank you for contacting us. Your email mentioned that you were looking for a quiet apartment to live alone because you would start college in September. We understand that you prefer a safe neighborhood with good access to public transportation. Although the kitchen is not very important, you said having some private outdoor space was necessary.",
        "We found an apartment that we thought would suit you well. It is in a quiet neighborhood, and the living room is separate from the bedroom. There are some shops and restaurants nearby. A bus stop is just two minutes away. The rent is $850 per month, and it includes the Internet, but not water or electricity. The apartment will be available by late August. The balcony is a bit small, but it gets plenty of light.",
        "If this apartment sounds good, please let us know when you are free to come and see it. As the apartment might be rented soon by someone else, we recommend arranging a viewing as soon as possible. If you decide to rent it after your visit, you will need to follow the next steps, including signing the agreement. We recommend finishing this process at our office before August 10.\nThank you,\nLucy Henderson",
    ],
    "questions": [
        {
            "number": 24,
            "question": "Nick King is looking for an apartment that",
            "choices": [
                "offers a big indoor area to live in with some roommates.",
                "includes some outdoor space that is shared with others.",
                "sits in a quiet area with easy access to local transport options.",
                "has a kitchen that is big enough for a single person to cook.",
            ],
        },
        {
            "number": 25,
            "question": "What is true about the apartment that Lucy Henderson offers?",
            "choices": [
                "It has a living room that is also used as a bedroom.",
                "It comes with a balcony that gets good sunlight.",
                "It includes the water and electricity fees in the rent.",
                "It is ready for Nick to move anytime in August.",
            ],
        },
        {
            "number": 26,
            "question": "What does Nick need to do to rent the apartment?",
            "choices": [
                "Attend a viewing on August 10 as a first step.",
                "Visit Lucy's office before a viewing.",
                "Sign the agreement by August 10 after a viewing.",
                "Make an appointment for a viewing after August 10.",
            ],
        },
    ],
}

passage_3b = {
    "label": "B",
    "title": "A Fifteen-Minute City",
    "paragraphs": [
        "In recent years, a new city planning project has begun in Paris, France. It is called the \"fifteen-minute city.\" This concept is based on the idea that important places for daily life, such as schools, hospitals, offices, and parks, should be located close to people's homes. This means that the city should have a system that allows people to walk or ride a bicycle to these places easily. Since the project began, the city has seen huge changes.",
        "There is a strong reason why this idea was proposed. Today, Paris is working to lower the amount of carbon dioxide released to reduce the level of harmful air pollution. One way to do this is by encouraging people to use cars less. Through the fifteen-minute city concept, citizens can expect to get around the city more easily. The project helps provide improved access to services necessary for daily life. Therefore, it can lead to a better quality of life for people.",
        "As part of the fifteen-minute city project, bicycle lanes were introduced on a large scale. Also, the city uses unique approaches to utilize empty spaces. For example, a building once used by the government is now a space offering a market, a hotel, restaurants, and even a rooftop garden. Parking areas that were not often used were replaced with houses. An old hospital was turned into a school with a library and a sports ground that local people can use after school and on school holidays.",
        "The fifteen-minute city project in Paris is getting attention around the world and is spreading to other cities. Cities such as Busan in South Korea and Cleveland in the United States are now trying similar plans. In fact, the city of Utrecht in the Netherlands is aiming to become a \"ten-minute city.\" The efforts of these cities may prove that it is possible to achieve important changes on a city scale to help solve the global problem of climate change today.",
    ],
    "questions": [
        {
            "number": 27,
            "question": "What idea is the concept of \"the fifteen-minute city\" based on?",
            "choices": [
                "The city should be designed to give people easy access to important services.",
                "Local people should travel more to see different parts of the city.",
                "Better parking is needed to get to schools and offices easily.",
                "More people should live at least fifteen minutes away from the city.",
            ],
        },
        {
            "number": 28,
            "question": "Why did Paris start the project of the fifteen-minute city?",
            "choices": [
                "To create more space for nature to improve air quality in the city.",
                "To grow the economy by attracting more cars entering the city.",
                "To bring in businesses related to everyday life to make the city better.",
                "To encourage people to drive less to solve environmental problems.",
            ],
        },
        {
            "number": 29,
            "question": "As part of creating the fifteen-minute city of Paris,",
            "choices": [
                "a rooftop garden was created to encourage farming in the city.",
                "some of the old local services were replaced with government services.",
                "a former medical institution became a school with some services for local people.",
                "some parking areas were open to the local people during the holidays.",
            ],
        },
        {
            "number": 30,
            "question": "What impact has Paris's fifteen-minute city project had?",
            "choices": [
                "Cleveland has already developed itself in the same way as Paris.",
                "Utrecht followed Paris and successfully achieved the fifteen-minute city project.",
                "Busan has found it hard to start a similar project.",
                "Some cities in other countries are trying similar plans.",
            ],
        },
        {
            "number": 31,
            "question": "What do we learn from the passage?",
            "choices": [
                "The Paris example shows how personal efforts can solve environmental problems.",
                "Adding bicycle lanes and using empty spaces can help make the fifteen-minute city a reality.",
                "The project will take a while to attract interest around the world.",
                "The project caused a drop in the number of houses in Paris.",
            ],
        },
    ],
}


def attach_answers(questions):
    for q in questions:
        q["answer"] = ANSWERS[q["number"]]


for q in section1_questions:
    attach_answers([q])
for pa in (passage_2a, passage_2b):
    attach_answers(pa["questions"])
for pa in (passage_3a, passage_3b):
    attach_answers(pa["questions"])

data = {
    "title": "2026年度 第1回 英語資格検定準2級プラス リーディング",
    "grade": "準2級プラス",
    "exam": "2026-1",
    "year": "2026",
    "session": "1",
    "sections": [
        {
            "name": "大問1",
            "nameEn": "Part 1",
            "type": "vocabulary",
            "instruction": "次の(1)から(17)までの(　)に入れるのに最も適切なものを1, 2, 3, 4の中から一つ選び、その番号を解答用紙の所定欄にマークしなさい。",
            "questions": section1_questions,
        },
        {
            "name": "大問2",
            "nameEn": "Part 2",
            "type": "passage-fill",
            "instruction": "次の英文 A, B を読み、その文意にそって (18) から (23) までの ( ) に入れるのに最も適切なものを 1, 2, 3, 4 の中から一つ選び、その番号を解答用紙の所定欄にマークしなさい。",
            "passages": [passage_2a, passage_2b],
        },
        {
            "name": "大問3",
            "nameEn": "Part 3",
            "type": "reading-comprehension",
            "instruction": "次の英文 A, B の内容に関して, (24) から (31) までの質問に対して最も適切なもの, または文を完成させるのに最も適切なものを 1, 2, 3, 4 の中から一つ選び, その番号を解答用紙の所定欄にマークしなさい。",
            "passages": [passage_3a, passage_3b],
        },
    ],
    "listening": {
        "part1": {
            1: 3, 2: 3, 3: 3, 4: 1, 5: 2, 6: 2, 7: 2, 8: 4, 9: 3, 10: 1,
            11: 4, 12: 2, 13: 1, 14: 1, 15: 1,
        },
        "part2": {
            16: 4, 17: 3, 18: 2, 19: 2, 20: 4, 21: 4, 22: 3, 23: 4, 24: 2, 25: 1,
            26: 3, 27: 3, 28: 1, 29: 1, 30: 3,
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
print("  reading questions: 31")

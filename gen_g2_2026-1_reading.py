# -*- coding: utf-8 -*-
"""
2026年度 第1回（本会場）英検2級
推論なしOCR原本 → data.json（リーディング Q1〜31）
一次ソース: 2026-1(本会場）/2級.pdf / 2級解答.pdf
"""
import json
import os
import sys
from collections import OrderedDict

sys.stdout.reconfigure(encoding="utf-8")

OUT_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade2", "2026-1",
)
OUT_PATH = os.path.join(OUT_DIR, "data.json")

# 公式解答（解答PDF リーディング）
ANSWERS = {
    1: 4, 2: 2, 3: 3, 4: 1, 5: 2, 6: 3, 7: 4, 8: 3, 9: 3, 10: 1,
    11: 4, 12: 4, 13: 2, 14: 1, 15: 1, 16: 1, 17: 2,
    18: 1, 19: 1, 20: 3, 21: 2, 22: 1, 23: 4,
    24: 3, 25: 1, 26: 4, 27: 3, 28: 1, 29: 3, 30: 1, 31: 4,
}

section1_questions = [
    {
        "number": 1,
        "text": "In many countries, the ( ) wears a white dress at a wedding. However, in some countries, she may wear a red dress.",
        "choices": ["lawyer", "warrior", "surgeon", "bride"],
    },
    {
        "number": 2,
        "text": "The teacher asked her students to find Argentina on a ( ). She wanted them to learn about countries that are far away from Japan.",
        "choices": ["branch", "globe", "scale", "trail"],
    },
    {
        "number": 3,
        "text": "Yuki only started studying Korean two years ago, but she can already read the newspaper without any ( ). Everyone is surprised by how quickly she has learned the language.",
        "choices": ["glory", "balance", "difficulty", "priority"],
    },
    {
        "number": 4,
        "text": "A: Are you all right? You have a ( ) to be quiet when you're worried.\nB: Do I? I never realized I was like that. I'm fine. I just don't have much to say today.",
        "choices": ["tendency", "discrimination", "shelter", "content"],
    },
    {
        "number": 5,
        "text": "Teachers at Billings Academy try to ( ) leadership qualities in their students. They teach the students how to communicate, make decisions, and take responsibility.",
        "choices": ["hate", "foster", "divide", "pronounce"],
    },
    {
        "number": 6,
        "text": "On a ( ) Saturday night, Mr. and Mrs. Nelson order pizza and watch TV together. But sometimes, they go out to a restaurant.",
        "choices": ["gradual", "chemical", "typical", "false"],
    },
    {
        "number": 7,
        "text": "When the movie ended, many people in the theater began to ( ). The story was very sad.",
        "choices": ["occur", "swell", "tap", "weep"],
    },
    {
        "number": 8,
        "text": "The biology professor showed his students some videos of living cells. He wanted to ( ) how cells work.",
        "choices": ["occupy", "polish", "illustrate", "congratulate"],
    },
    {
        "number": 9,
        "text": "The Green Wolves and the Blue Stars were very evenly matched in the championship game. The Green Wolves ( ) won when they scored a goal in the last seconds of the game.",
        "choices": ["secretly", "gently", "barely", "repeatedly"],
    },
    {
        "number": 10,
        "text": "When the teacher said there would be a test next week, the students ( ). They had hoped that they would have more time to study.",
        "choices": ["frowned", "slipped", "guessed", "crawled"],
    },
    {
        "number": 11,
        "text": "( ), people should drink eight glasses of water a day to stay healthy. However, some people may need more or less than this.",
        "choices": [
            "For a fresh start",
            "On a specific occasion",
            "In case of emergency",
            "As a general rule",
        ],
    },
    {
        "number": 12,
        "text": "Ben moved out of his parents' house and into an apartment last week. Now, he has to do everything ( ), like cooking and cleaning.",
        "choices": ["on the air", "at a distance", "to his surprise", "on his own"],
    },
    {
        "number": 13,
        "text": "In the meeting, the president said that he could not ( ) the plan to expand the office because it would be too expensive.",
        "choices": ["take away from", "go along with", "bring out in", "watch out for"],
    },
    {
        "number": 14,
        "text": "After ( ) tests, the doctors discovered that Masahiro had a rare illness. They immediately started treating him.",
        "choices": ["a series of", "the edge of", "a member of", "the back of"],
    },
    {
        "number": 15,
        "text": "A: Our presentation next week will include a lot of data. It will take a lot of work to prepare.\nB: ( ), we are going to be very busy! Let's get started right away.",
        "choices": ["In other words", "In the beginning", "Back and forth", "On the contrary"],
    },
    {
        "number": 16,
        "text": "The two paintings looked ( ) each other at first, but when John looked more closely, he saw that they were very similar in one way.",
        "choices": ["distinct from", "composed of", "absent from", "threatening to"],
    },
    {
        "number": 17,
        "text": "The company had to ( ) some of its workers because it was losing money. It was a very difficult decision to make.",
        "choices": ["flip over", "lay off", "bring about", "catch up"],
    },
]

passage_2a = {
    "label": "A",
    "title": "Efforts at a Village",
    "paragraphs": [
        "El Pital is a rural village in Honduras. Like many places in this country, it faced ( 18 ). Literacy rates were low in the community, and few students had access to books. To solve this problem, an artist and young people worked together to invent a special character named Bibliobandido. They did this to help children enjoy learning to read and write. This character wore a mask and went around the village. Children were told that he would get hungry unless they fed him their stories. Motivated by this, children began writing stories.",
        "Efforts were made to make children believe that Bibliobandido was real. Costumes were created, rumors were spread, and dramatic scenes were performed to bring him to life. During one visit, Bibliobandido appeared in the village on a horse, and children were asked to create new stories within an hour so that he would not starve. This activity turned a writing task into an exciting community event. This was possible because ( 19 ) to make the event successful. Their efforts brought people of different ages together.",
        "The story of Bibliobandido spread to other places and led to some interesting developments. In North America, the idea was changed to fit different places and cultures. For example, in New York, a female character called La Dama Violeta was created as a subway superhero. She protected passengers from having the newspapers and books they were reading stolen by Bibliobandido. ( 20 ), this character added a creative twist to public reading while traveling and reminded people of the joy of reading.",
    ],
    "questions": [
        {
            "number": 18,
            "choices": [
                "a lack of educational resources",
                "a decline in the number of children",
                "the loss of safe school routes",
                "poor cooperation among villagers",
            ],
        },
        {
            "number": 19,
            "choices": [
                "many people worked behind the scenes",
                "some children watched quietly from home",
                "almost no children waited to meet him",
                "several students talked about the costumes",
            ],
        },
        {
            "number": 20,
            "choices": ["To begin with", "Unfortunately", "In this way", "On the other hand"],
        },
    ],
}

passage_2b = {
    "label": "B",
    "title": "The Science of Fear",
    "paragraphs": [
        "Fear is a natural emotion that helps protect people from danger. When people see dangerous animals or hear a sudden loud noise, fear quickly makes the brain react and send a message to the body. This reaction causes changes such as a faster heart rate, quicker breathing, and tense muscles. These changes ( 21 ). This is called the \"fight-or-flight\" response to fear or stress, which gets the body ready to act immediately. Fear has been helping humans survive for millions of years.",
        "Sometimes, people feel fear even when they are not facing real danger. For example, some people feel afraid when they watch a scary scene in a movie, although they are in a safe place. The brain uses memories and past experiences to predict possible danger and generate fear, causing the body to react strongly and become more alert. Some people ( 22 ). They like scary things and seek excitement. This also explains why many people enjoy activities such as riding roller coasters.",
        "However, fear is not always enjoyable. Some people feel fear too often or too intensely. In such cases, the brain treats normal events as dangerous, which can lead to problems. ( 23 ), this intense fear can make everyday activities feel overwhelming and difficult. Recent studies have identified specific brain mechanisms that allow people to control learned fears, offering hope for more effective treatments. Currently, scientists are studying how fear is generated in the brain and seeking solutions for those who suffer from it.",
    ],
    "questions": [
        {
            "number": 21,
            "choices": [
                "make people feel sleepy and calm",
                "prepare people for escape or defense",
                "stop people from moving their bodies",
                "help people pretend they are not scared",
            ],
        },
        {
            "number": 22,
            "choices": [
                "are even fascinated by this feeling",
                "are often afraid of opening their eyes",
                "forget fear soon after it happens",
                "love surprising their friends and family",
            ],
        },
        {
            "number": 23,
            "choices": ["On the other hand", "Fortunately", "Without this", "In particular"],
        },
    ],
}

passage_3a = {
    "label": "A",
    "title": "Your service",
    "format": "email",
    "meta": {
        "from": "Matthew Watts <mwatts@polarvillageelementary.edu>",
        "to": "Mary Carter <mcarter@trackfitrentals.com>",
        "date": "May 27",
        "subject": "Your service",
    },
    "paragraphs": [
        "Dear Mary Carter,\nMy name is Matthew Watts, and I am a teacher at Polar Village Elementary School. We are looking for an outdoor facility where we can hold an athletic event this fall. One of my coworkers recommended your facility and suggested I contact you. She used one of the grounds for an event at the school where she had previously worked. Also, your facility is appealing because it is easy to access from several train stations.",
        "Although the exact date has not been set, our athletic event will take place on a weekday in September or October. We hope to use the large ground from 8 a.m. to 3 p.m. Currently, we expect about 150 people to attend the event, including some parents and teachers. According to the website, this is about the number of people your facility can hold.",
        "Could you please let me know which date might be suitable for our event? It would be great if you could provide a few possible dates. We can meet to discuss the details of the event as needed. Our school is close to your main office, and we have enough teachers and staff. Therefore, we can easily adjust our schedules to make sure at least one person can visit for the meeting before 5 p.m. on the day you choose.",
        "Sincerely,\nMatthew Watts\nPolar Village Elementary School",
    ],
    "questions": [
        {
            "number": 24,
            "question": "What is one reason Matthew Watts is interested in the facility?",
            "choices": [
                "The ground is perfect for camping.",
                "The staff working there is helpful.",
                "It is located near public transportation.",
                "It is popular among schoolchildren.",
            ],
        },
        {
            "number": 25,
            "question": "Regarding the event that is being planned,",
            "choices": [
                "the number of people will likely be appropriate for the space.",
                "it will happen only on weekends this September or October.",
                "only the students from the school will attend this year.",
                "it will last all day until the end of the year.",
            ],
        },
        {
            "number": 26,
            "question": "Why does Matthew mention the location of the school and the number of staff to Mary Carter?",
            "choices": [
                "To suggest changing the time of the event to the morning.",
                "To ask if the facility staff can help prepare for the event.",
                "To explain that the school needs more teachers than it has.",
                "To show that visiting her in the office is not too difficult.",
            ],
        },
    ],
}

passage_3b = {
    "label": "B",
    "title": "The Humboldt Brothers",
    "paragraphs": [
        "Alexander and Wilhelm von Humboldt were born in the late eighteenth century in what is now Germany into a wealthy family. When Alexander was just a child, their father passed away. Even before his death, their parents wanted to ensure that their sons received a good education. Following his death, the brothers were raised mainly by their mother, who held strict and serious religious beliefs. She took charge of their education, hiring famous educators and experts in various fields to tutor them. The brothers' education covered many academic subjects, such as mathematics, languages, history, and economics.",
        "The younger of the two, Alexander, had been deeply interested in adventure since early childhood. The money he received after his mother's death made his dream of traveling to South America come true. He spent several years there studying plants, animals, and the natural features of the land. Alexander wrote books about what he had learned there after the trip. One of his most famous books is Kosmos, in which he tried to explain how everything in the natural world worked and how things were connected to each other.",
        "On the other hand, Wilhelm's passion was education and language. He served as the education director of the Ministry of the Interior in Prussia and helped found a university. The proposal he wrote for the university has influenced the German university system ever since. He is also known for his studies of language. He considered language to be something whose structure and character reflected the culture and individuality of its speakers. According to him, language was not just a collection of words but a means that allowed people to perceive the world.",
        "It is clear that the environment in which the Humboldt brothers grew up gave them opportunities to achieve something with a lasting impact. They enjoyed a life that not everyone could have, growing up around great leaders, scientists, and writers. Their wealthy background gave them early access to quality education and rich intellectual opportunities. These experiences helped shape ideas that continue to influence society today. While not many people in the world may know their names, many people have indirectly received benefits from their work.",
    ],
    "questions": [
        {
            "number": 27,
            "question": "To provide a great education for the Humboldt brothers, their mother",
            "choices": [
                "took them to Berlin to learn languages through their travels.",
                "chose to send them to a famous school for wealthy families.",
                "arranged private lessons with academic experts for them.",
                "had their own parents decide what the brothers should study.",
            ],
        },
        {
            "number": 28,
            "question": "What made it possible for Alexander von Humboldt to travel to South America?",
            "choices": [
                "The money left to him after his mother passed away.",
                "The sales of the book he wrote about the natural world.",
                "An invitation from his brother to travel to new places.",
                "Support given by a group of scientists in South America.",
            ],
        },
        {
            "number": 29,
            "question": "What did Wilhelm von Humboldt believe about language?",
            "choices": [
                "It developed in similar ways across different cultures and societies.",
                "It reflected both the German cultural background and educational systems.",
                "It was a tool that helped individuals see and understand the world around them.",
                "It was closely related to education and played a role in creating university systems.",
            ],
        },
        {
            "number": 30,
            "question": "What is one reason the Humboldt brothers could focus on their achievements?",
            "choices": [
                "Their childhood provided them with access to knowledge and learning.",
                "Their jobs were flexible enough to allow them a lot of free time for research.",
                "They had a lot of volunteer workers who were willing to work for them.",
                "They worked with teams of several great assistants on each project.",
            ],
        },
        {
            "number": 31,
            "question": "Which of the following statements is true?",
            "choices": [
                "Alexander finished writing a book about the functions of nature before he went on a journey.",
                "The Humboldt brothers desired to become rich and chose their own study subjects accordingly.",
                "The Humboldts' father wanted to teach them piano himself and took steps to make it happen.",
                "Wilhelm wrote a proposal that has had a great impact on the German university system.",
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
    "title": "2026年度 第1回 英語資格検定2級 リーディング",
    "grade": "2級",
    "exam": "2026-1",
    "year": "2026",
    "session": "1",
    "sections": [
        {
            "name": "大問1",
            "nameEn": "Part 1",
            "type": "vocabulary",
            "instruction": "次の(1)から(17)までの（　　）に入れるのに最も適切なものを1, 2, 3, 4の中から一つ選び、その番号を解答用紙の所定欄にマークしなさい。",
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
            "instruction": "次の英文 [A], [B] の内容に関して, (24) から (31) までの質問に対して最も適切なもの, または文を完成させるのに最も適切なものを 1, 2, 3, 4 の中から一つ選び, その番号を解答用紙の所定欄にマークしなさい。",
            "passages": [passage_3a, passage_3b],
        },
    ],
    "listening": {
        "part1": {
            1: 3, 2: 4, 3: 3, 4: 1, 5: 2, 6: 3, 7: 1, 8: 2, 9: 1, 10: 4,
            11: 4, 12: 1, 13: 4, 14: 3, 15: 2,
        },
        "part2": {
            16: 1, 17: 2, 18: 1, 19: 1, 20: 1, 21: 3, 22: 2, 23: 1, 24: 4, 25: 2,
            26: 2, 27: 4, 28: 1, 29: 2, 30: 2,
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
print(f"  reading questions: 31")

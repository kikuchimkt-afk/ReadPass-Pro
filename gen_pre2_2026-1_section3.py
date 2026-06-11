# -*- coding: utf-8 -*-
"""
2026年度 第1回（土曜準会場）英検準2級 data.json
Step C: 大問3（passage-fill型）Q21〜22「A Lost Dog」
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade-pre2", "2026-1-sat", "data.json",
)

section3 = {
    "name": "大問3",
    "nameEn": "Part 3",
    "type": "passage-fill",
    "instruction": "次の英文を読み，その文意にそって(21)と(22)の(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選びなさい。",
    "passages": [
        {
            "label": "",
            "title": "A Lost Dog",
            "paragraphs": [
                "Max was a high school student who had a dog named Leo. One day, while they were taking their usual walk in the mountains, Leo suddenly ran off. Max looked for him for hours, but the dog was nowhere to be found. Max ( 21 ). He made posters, gave them to neighbors, and called dog shelters. Still, Leo was missing. In the end, he had to accept that Leo had gone.",
                "A few years later, Max was in college and living in another city. One afternoon, he got a call from his mother. She told him that a dog very similar to Leo had appeared and was sitting in front of their house. Max was ( 22 ). He hurried back to his home in his hometown. Max believed Leo had found his way home through smell and memory. When he saw Leo sitting there, Max ran to him, hugged him, and started crying.",
            ],
            "translations": [
                "マックスはレオという犬を飼っている高校生でした。ある日、いつものように山を散歩していると、レオが突然走り去ってしまいました。マックスは何時間も探しましたが、犬の姿はどこにもありませんでした。マックスは( 21 )。ポスターを作り、近所の人に配り、犬の保護施設にも電話しました。それでもレオは行方不明のままでした。結局、レオがいなくなったことを受け入れなければなりませんでした。",
                "数年後、マックスは大学に通い、別の都市に住んでいました。ある午後、母親から電話がありました。レオにとても似た犬が現れて家の前に座っていると言われました。マックスは( 22 )。故郷の実家に急いで戻りました。マックスは、レオが匂いと記憶で帰ってきたのだと信じました。そこに座っているレオを見て、マックスは走り寄り、抱きしめ、泣き始めました。",
            ],
            "sentencePairs": [
                [
                    "Max was a high school student who had a dog named Leo.",
                    "マックスはレオという犬を飼っている高校生でした。",
                ],
                [
                    "One day, while they were taking their usual walk in the mountains, Leo suddenly ran off.",
                    "ある日、いつものように山を散歩していると、レオが突然走り去ってしまいました。",
                ],
                [
                    "Max looked for him for hours, but the dog was nowhere to be found.",
                    "マックスは何時間も探しましたが、犬の姿はどこにもありませんでした。",
                ],
                [
                    "He made posters, gave them to neighbors, and called dog shelters.",
                    "ポスターを作り、近所の人に配り、犬の保護施設にも電話しました。",
                ],
                [
                    "Still, Leo was missing.",
                    "それでもレオは行方不明のままでした。",
                ],
                [
                    "In the end, he had to accept that Leo had gone.",
                    "結局、レオがいなくなったことを受け入れなければなりませんでした。",
                ],
                [
                    "A few years later, Max was in college and living in another city.",
                    "数年後、マックスは大学に通い、別の都市に住んでいました。",
                ],
                [
                    "She told him that a dog very similar to Leo had appeared and was sitting in front of their house.",
                    "レオにとても似た犬が現れて家の前に座っていると言われました。",
                ],
                [
                    "He hurried back to his home in his hometown.",
                    "故郷の実家に急いで戻りました。",
                ],
                [
                    "Max believed Leo had found his way home through smell and memory.",
                    "マックスは、レオが匂いと記憶で帰ってきたのだと信じました。",
                ],
                [
                    "When he saw Leo sitting there, Max ran to him, hugged him, and started crying.",
                    "そこに座っているレオを見て、マックスは走り寄り、抱きしめ、泣き始めました。",
                ],
            ],
            "questions": [
                {
                    "number": 21,
                    "choices": [
                        "decided to do that all by himself",
                        "gave up on seeing the dog again",
                        "found the dog a few days later",
                        "did everything that he could",
                    ],
                    "choiceTranslations": [
                        "それをすべて一人でやることにした",
                        "もう犬に会えないとあきらめた",
                        "数日後に犬を見つけた",
                        "できる限りのことをした",
                    ],
                    "answer": 4,
                    "choiceAnalysis": [
                        "❌ decided to do that all by himself＝一人でやることにした。gave them to neighbors, and called dog shelters（近所に配り、保護施設に電話）とあり、一人だけではない",
                        "❌ gave up on seeing the dog again＝もう会えないとあきらめた。In the end, he had to accept that Leo had gone（結局受け入れた）はその後の話で、空所の直後はまだ努力の描写",
                        "❌ found the dog a few days later＝数日後に見つけた。直後はポスター作成などの捜索活動。Still, Leo was missing（まだ行方不明）とも合わない",
                        "✅ did everything that he could＝できる限りのことをした。He made posters, gave them to neighbors, and called dog shelters（ポスター・近所・保護施設）を総括→正解",
                    ],
                    "sourceEvidence": [
                        "He made posters, gave them to neighbors, and called dog shelters.",
                        "Max looked for him for hours, but the dog was nowhere to be found.",
                    ],
                    "grammar": "💡 do everything (that) one can＝できる限りのことをする。nowhere to be found＝どこにも見つからない。",
                },
                {
                    "number": 22,
                    "choices": [
                        "surprised to hear that",
                        "sure it was a different dog",
                        "angry at his mother's news",
                        "sad to leave the city",
                    ],
                    "choiceTranslations": [
                        "それを聞いて驚いた",
                        "別の犬だと確信していた",
                        "母親の知らせに怒った",
                        "街を離れるのが悲しかった",
                    ],
                    "answer": 1,
                    "choiceAnalysis": [
                        "✅ surprised to hear that＝それを聞いて驚いた。a dog very similar to Leo had appeared（レオに似た犬が現れた）という予想外の知らせ。He hurried back（急いで戻った）と一致→正解",
                        "❌ sure it was a different dog＝別の犬だと確信。He hurried back to his home（故郷へ急ぎ）・hugged him, and started crying（抱きしめて泣いた）と矛盾",
                        "❌ angry at his mother's news＝母親の知らせに怒った。ran to him, hugged him（走り寄り抱きしめた）再会の喜びの場面と矛盾",
                        "❌ sad to leave the city＝街を離れるのが悲しい。living in another city から hometown へ戻る話で、街を離れる悲しみとは無関係",
                    ],
                    "sourceEvidence": [
                        "a dog very similar to Leo had appeared and was sitting in front of their house.",
                        "He hurried back to his home in his hometown.",
                    ],
                    "grammar": "💡 be surprised to hear that ～＝～と聞いて驚く。similar to ～＝～に似た。find one's way home＝帰り道を見つける。",
                },
            ],
        }
    ],
}

for pa in section3["passages"]:
    for q in pa["questions"]:
        marked = []
        for i, t in enumerate(q["choiceAnalysis"]):
            if t.startswith(("✅", "❌")):
                marked.append(t)
            else:
                marked.append(("✅ " if i + 1 == q["answer"] else "❌ ") + t)
        q["choiceAnalysis"] = marked

with open(DATA_PATH, encoding="utf-8") as f:
    data = json.load(f)

if len(data.get("sections", [])) < 2:
    raise SystemExit("sections 0-1 not found — run section1/2 scripts first")

data["sections"] = [data["sections"][0], data["sections"][1], section3]

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Wrote section3 ({len(section3['passages'][0]['questions'])} questions) to {DATA_PATH}")

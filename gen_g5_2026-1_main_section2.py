# -*- coding: utf-8 -*-
"""2026年度 第1回（本会場）英検5級 data.json 大問2 Q16〜20"""
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade5", "2026-1", "data.json",
)


def mark_ca(items, answer):
    out = []
    for i, text in enumerate(items):
        cleaned = re.sub(r"^[○✅❌]\s*", "", text)
        prefix = "✅" if i + 1 == answer else "❌"
        out.append(f"{prefix} {cleaned}")
    return out


section2 = {
    "name": "大問2",
    "nameEn": "Part 2",
    "type": "vocabulary",
    "instruction": "次の(16)から(20)までの会話について、( )に入れるのに最も適切なものを1, 2, 3, 4の中から一つ選び、その番号のマーク欄をぬりつぶしなさい。",
    "questions": [
        {
            "number": 16,
            "text": "Girl 1: Is Ken in your class this year?\nGirl 2: (　) I like him a lot.",
            "choices": ["Yes, he is.", "Please come back.", "Sit down.", "No, I don't."],
            "answer": 1,
            "grammar": "Yes, he is.＝「はい、彼は（クラスに）います」。Is Ken in your class? への肯定の答え。",
            "grammarSimple": "Yes, he is. は「うん、ケンは（クラスに）いるよ」。そのあと I like him a lot. とつながる！",
            "choiceAnalysis": [
                "Yes, he is.＝ケンがクラスにいるかへの「はい」。I like him a lot. と自然につながる。",
                "Please come back.＝「戻ってきて」。クラスにいるかの質問への答えにならない。",
                "Sit down.＝「座って」。質問への答えとして不自然。",
                "No, I don't.＝「いいえ、（好きでは）ない」。I like him a lot. と矛盾する。",
            ],
            "choiceAnalysisSimple": [
                "○「うん、いるよ」がぴったり！そのあと「すき」って言ってる！",
                "「もどってきて」は合わないよ。",
                "「すわって」は合わないよ。",
                "「いいえ」はあとに「すき」と矛盾するよ。",
            ],
            "questionAudio": "audio/q16.mp3",
            "translation": "女の子1：ケンは今年、あなたのクラスにいる？\n女の子2：（　）彼のことがとても好きなの。",
            "choiceTranslations": ["うん、いるよ。", "戻ってきて。", "座って。", "いいえ、好きじゃない。"],
        },
        {
            "number": 17,
            "text": "Boy: I enjoy basketball.\nGirl: (　) I often play it on Sundays.",
            "choices": ["No, I don't.", "I do, too.", "That's OK.", "You're welcome."],
            "answer": 2,
            "grammar": "I do, too.＝「私も（バスケが好き）」。I enjoy basketball. への同意。",
            "grammarSimple": "I do, too. は「わたしもだよ」。バスケがすき、に「わたしも！」って言ってる！",
            "choiceAnalysis": [
                "No, I don't.＝否定。I often play it on Sundays.（日曜によくやる）と矛盾。",
                "I do, too.＝「私も（バスケが好き）」。I enjoy basketball. と呼応。",
                "That's OK.＝「大丈夫」。好きかどうかの返答にならない。",
                "You're welcome.＝「どういたしまして」。感謝への返事で、同意ではない。",
            ],
            "choiceAnalysisSimple": [
                "「いいえ」はあとに「よくやる」と矛盾するよ。",
                "○「わたしも！」がぴったり！",
                "「だいじょうぶ」は合わないよ。",
                "「どういたしまして」は合わないよ。",
            ],
            "questionAudio": "audio/q17.mp3",
            "translation": "男の子：バスケットボールが好きなんだ。\n女の子：（　）日曜日によくやるの。",
            "choiceTranslations": ["いいえ、好きじゃない。", "私もだよ。", "大丈夫だよ。", "どういたしまして。"],
        },
        {
            "number": 18,
            "text": "Teacher: Does your sister work at a hospital, Sally?\nGirl: Yes. (　)",
            "choices": ["She's a nurse.", "I like volleyball.", "I'm so fast.", "She has a dog."],
            "answer": 1,
            "grammar": "She's a nurse.＝「彼女は看護師です」。病院で働く姉の職業を説明。",
            "grammarSimple": "She's a nurse. は「かんごしなんだ」。びょういんではたらうってことだよ！",
            "choiceAnalysis": [
                "She's a nurse.＝看護師。work at a hospital の具体的な職業。",
                "I like volleyball.＝「バレーボールが好き」。姉の仕事の説明にならない。",
                "I'm so fast.＝「私はとても速い」。病院の仕事とは無関係。",
                "She has a dog.＝「犬を飼っている」。病院で働く話とずれる。",
            ],
            "choiceAnalysisSimple": [
                "○「かんごし」がぴったり！",
                "「バレーすき」は仕事の話じゃないよ。",
                "「はやい」は合わないよ。",
                "「いぬ」は合わないよ。",
            ],
            "questionAudio": "audio/q18.mp3",
            "translation": "先生：サリー、お姉さんは病院で働いているの？\n女の子：うん。（　）",
            "choiceTranslations": ["彼女は看護師だよ。", "バレーボールが好き。", "私はとても速い。", "彼女は犬を飼っている。"],
        },
        {
            "number": 19,
            "text": "Man: Let's go to that hamburger shop.\nWoman: (　) I'm hungry.",
            "choices": ["Good idea.", "See you.", "That's all.", "It's sunny today."],
            "answer": 1,
            "grammar": "Good idea.＝「いい考えだね」。提案への同意。I'm hungry. とつながる。",
            "grammarSimple": "Good idea. は「いいね！」。ハンバーガー店に行こう、に「いいよ！」って言ってる！",
            "choiceAnalysis": [
                "Good idea.＝提案への同意。I'm hungry.（お腹が空いた）と自然につながる。",
                "See you.＝「じゃあね」。店に行く提案への返答として不自然。",
                "That's all.＝「それだけ」。提案への返答にならない。",
                "It's sunny today.＝「今日は晴れ」。お腹が空いた理由の説明にならない。",
            ],
            "choiceAnalysisSimple": [
                "○「いいね！」がぴったり！「おなかすいた」って言ってる！",
                "「じゃあね」は合わないよ。",
                "「それだけ」は合わないよ。",
                "「はれてる」は合わないよ。",
            ],
            "questionAudio": "audio/q19.mp3",
            "translation": "男：あのハンバーガー店に行こう。\n女：（　）お腹が空いたわ。",
            "choiceTranslations": ["いい考えだね。", "じゃあね。", "それだけよ。", "今日は晴れているわ。"],
        },
        {
            "number": 20,
            "text": "Man: Are you from Australia?\nWoman: (　)",
            "choices": ["Yes, I am.", "Yes, I can.", "Yes, it is.", "Yes, it does."],
            "answer": 1,
            "grammar": "Yes, I am.＝「はい、（オーストラリア出身）です」。Are you from ～? への答え。",
            "grammarSimple": "Yes, I am. は「うん、そうだよ」。オーストラリア出身？に「うん！」だよ。",
            "choiceAnalysis": [
                "Yes, I am.＝Are you from Australia? への正しい肯定。",
                "Yes, I can.＝「はい、できます」。出身の質問への答えにならない。",
                "Yes, it is.＝「はい、それは〜です」。人への質問に it は使わない。",
                "Yes, it does.＝「はい、それは〜します」。出身の質問に合わない。",
            ],
            "choiceAnalysisSimple": [
                "○「うん、そうだよ」がぴったり！",
                "「できる」は合わないよ。",
                "「それは〜だ」は人の質問に使わないよ。",
                "「それは〜する」は合わないよ。",
            ],
            "questionAudio": "audio/q20.mp3",
            "translation": "男：あなたはオーストラリア出身ですか？\n女：（　）",
            "choiceTranslations": ["はい、そうです。", "はい、できます。", "はい、そうです（it）。", "はい、そうします。"],
        },
    ],
}

for q in section2["questions"]:
    q["choiceAnalysis"] = mark_ca(q["choiceAnalysis"], q["answer"])

with open(DATA_PATH, encoding="utf-8") as f:
    data = json.load(f)

sections = []
replaced = False
for sec in data.get("sections", []):
    if sec.get("name") == "大問2":
        sections.append(section2)
        replaced = True
    else:
        sections.append(sec)
if not replaced:
    out = []
    for sec in sections:
        out.append(sec)
        if sec.get("name") == "大問1":
            out.append(section2)
    sections = out

data["sections"] = sections
with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Wrote section2 ({len(section2['questions'])} questions) to {DATA_PATH}")

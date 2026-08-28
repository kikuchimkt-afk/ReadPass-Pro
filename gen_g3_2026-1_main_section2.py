# -*- coding: utf-8 -*-
"""
2026年度 第1回（本会場）英検3級 data.json
大問2（会話補充）Q16〜20 — 解説・和訳付き
一次ソース: 2026-1(本会場）/3級.pdf / 3級解答.pdf
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade3", "2026-1", "data.json",
)

section2 = {
    "name": "大問2",
    "nameEn": "Part 2",
    "type": "vocabulary",
    "instruction": "次の(16)から(20)までの会話について、( )に入れるのに最も適切なものを1, 2, 3, 4の中から一つ選び、その番号のマーク欄をぬりつぶしなさい。",
    "questions": [
        {
            "number": 16,
            "text": "Boy: I'm planning to go to Paris this summer. (　)\nGirl: Yes, it's a very beautiful place.",
            "choices": [
                "Would you like some?",
                "Have you ever been there?",
                "Did you find your bag?",
                "How much are the tickets?",
            ],
            "answer": 2,
            "grammar": "Have you ever been there?＝「そこへ行ったことがある？」。パリ旅行の話→相手の経験を聞く質問。",
            "grammarSimple": "Have you ever been there? は「そこに行ったことある？」。パリのはなしだから、行ったことがあるかきいてるよ。",
            "choiceAnalysis": [
                "Would you like some?＝「いくつか欲しい？」。パリ旅行の話題に合わない。",
                "○ Have you ever been there?＝「そこへ行ったことがある？」。Yes, it's beautiful. という答えと自然につながる。",
                "Did you find your bag?＝「かばんは見つかった？」。旅行の話題と無関係。",
                "How much are the tickets?＝「チケットはいくら？」。相手の経験を聞く流れとずれる。",
            ],
            "choiceAnalysisSimple": [
                "「いくつかほしい？」はパリのはなしと合わないよ。",
                "○「そこに行ったことある？」きれいなところだよ、というこたえとつながる！",
                "「かばんみつかった？」ははなしがずれるよ。",
                "「チケットいくら？」はちがうよ。",
            ],
            "translation": "男の子：この夏、パリに行く予定なんだ。（　）\n女の子：うん、とても美しい場所だよ。",
            "choiceTranslations": [
                "いくつか欲しい？",
                "そこへ行ったことがある？",
                "かばんは見つかった？",
                "チケットはいくら？",
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
            "answer": 3,
            "grammar": "That sounds great＝「いいですね」。I was thinking the same thing（私も同じことを考えていた）と呼応。",
            "grammarSimple": "That sounds great は「いいね」。わたしもおなじことかんがえてた、というつづきだよ。",
            "choiceAnalysis": [
                "Have a nice time.＝「楽しんでね」。出かける人へのあいさつで、一緒にテニスをしようという提案への返答にならない。",
                "It'll be here soon.＝「すぐここに来るよ」。テニスの提案と無関係。",
                "○ That sounds great.＝「いいですね」。同じことを考えていた、という肯定的な返答。",
                "I can't understand.＝「わかりません」。提案を受け入れる文脈と矛盾。",
            ],
            "choiceAnalysisSimple": [
                "「たのしんでね」は出かける人へのあいさつで、提案へのこたえにならないよ。",
                "「すぐくるよ」はテニスとは関係ないよ。",
                "○「いいね！」わたしもおなじことかんがえてた！",
                "「わからない」はちがうよ。",
            ],
            "translation": "男：土曜日に一緒にテニスをしない？\n女：（　）私も同じことを考えていたわ。",
            "choiceTranslations": [
                "楽しんでね。",
                "すぐここに来るよ。",
                "いいですね。",
                "わかりません。",
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
            "answer": 4,
            "grammar": "I'll be there in a minute＝「すぐ行くよ」。夕食の用意ができた→階下に降りてくる返答。",
            "grammarSimple": "I'll be there in a minute は「すぐいくよ」。ごはんのじゅんびができたから、すぐおりてくるよ。",
            "choiceAnalysis": [
                "I'm too busy.＝「忙しすぎる」。夕食に来るよう言われた場面と矛盾。",
                "I'll call you soon.＝「すぐ電話する」。下に来るよう言われたことへの返答にならない。",
                "I'm going tomorrow.＝「明日行く」。今すぐ降りてこいという指示と合わない。",
                "○ I'll be there in a minute.＝「すぐ行くよ」。Come downstairs への自然な返答。",
            ],
            "choiceAnalysisSimple": [
                "「いそがしすぎる」はごはんにこないことになるよ。",
                "「すぐでんわする」は、下におりてくるこたえにならないよ。",
                "「あしたいく」は「いますぐ」とちがうよ。",
                "○「すぐいくよ！」おりてくるね！",
            ],
            "translation": "母：サマンサ、夕食の用意ができたわ。下に降りてきて。\n娘：わかった、ママ。（　）",
            "choiceTranslations": [
                "忙しすぎるよ。",
                "すぐ電話するね。",
                "明日行くよ。",
                "すぐ行くよ。",
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
            "answer": 2,
            "grammar": "What's the matter?＝「どうしたの？」。I'm just not hungry（ただお腹が空いていないだけ）という理由の説明とつながる。",
            "grammarSimple": "What's the matter? は「どうしたの？」。おなかがすいてないだけ、というこたえにつながるよ。",
            "choiceAnalysis": [
                "Are they your friends?＝「彼らは友達？」。朝食を食べない理由を聞く質問にならない。",
                "○ What's the matter?＝「どうしたの？」。not hungry という状態の説明とぴったり。",
                "Can you do it alone?＝「一人でできる？」。食事の場面と無関係。",
                "Do you have any?＝「何か持っている？」。文脈に合わない。",
            ],
            "choiceAnalysisSimple": [
                "「ともだち？」はあさごはんのはなしと関係ないよ。",
                "○「どうしたの？」おなかがすいてないだけ、というこたえだね！",
                "「ひとりでできる？」は合わないよ。",
                "「なにかもってる？」は合わないよ。",
            ],
            "translation": "妻：朝食を食べていないわね。（　）\n夫：ただお腹が空いていないだけなんだ。",
            "choiceTranslations": [
                "彼らは友達なの？",
                "どうしたの？",
                "一人でできるの？",
                "何か持っているの？",
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
            "answer": 4,
            "grammar": "I'm very sorry＝「本当にすみません」。相手のジャケットを自分の物と思って着てしまい、謝る場面。",
            "grammarSimple": "I'm very sorry は「ほんとうにごめんなさい」。じゃけっとをまちがえてきちゃったからあやまるよ。",
            "choiceAnalysis": [
                "it's my pleasure.＝「どういたしまして」。謝罪の場面では使わない。",
                "I decided to go.＝「行くことにした」。ジャケットの取り違えへの返答にならない。",
                "I'll speak to him now.＝「今彼に話す」。二人の会話の流れとずれる。",
                "○ I'm very sorry.＝「本当にすみません」。It looks like mine.（私の物に見える）ため、取り違えたことを謝っている。",
            ],
            "choiceAnalysisSimple": [
                "「どういたしまして」はあやまるときには使わないよ。",
                "「いくことにした」は合わないよ。",
                "「いまはなす」ははなしがずれるよ。",
                "○「ほんとうにごめんなさい」。じゃけっとをまちがえたね！",
            ],
            "translation": "男1：すみません。君が着ているのは僕のジャケットだと思うんです。\n男2：ああ、（　）私の物に見えたんです。",
            "choiceTranslations": [
                "どういたしまして。",
                "行くことにしたよ。",
                "今彼に話すよ。",
                "本当にすみません。",
            ],
        },
    ],
}

with open(DATA_PATH, encoding="utf-8") as f:
    data = json.load(f)

sections = data.get("sections", [])
new_sections = []
replaced = False
for sec in sections:
    if sec.get("name") == "大問2":
        new_sections.append(section2)
        replaced = True
    else:
        new_sections.append(sec)
if not replaced:
    out = []
    for sec in new_sections:
        out.append(sec)
        if sec.get("name") == "大問1":
            out.append(section2)
    new_sections = out

def normalize_choice_analysis(q, key):
    normalized = []
    for i, t in enumerate(q.get(key, [])):
        t = t.strip().removeprefix("○").removeprefix("✅").removeprefix("❌").strip()
        normalized.append(("○ " if i + 1 == q["answer"] else "") + t)
    q[key] = normalized


for q in section2["questions"]:
    normalize_choice_analysis(q, "choiceAnalysis")
    normalize_choice_analysis(q, "choiceAnalysisSimple")

data["sections"] = new_sections

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Wrote section2 ({len(section2['questions'])} questions) to {DATA_PATH}")

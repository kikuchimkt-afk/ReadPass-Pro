# -*- coding: utf-8 -*-
"""
2026年度 第1回（本会場）英検4級 data.json
大問2（会話補充）Q16〜20 — 解説・和訳付き
一次ソース: 2026-1(本会場）/4級.pdf / 4級解答.pdf
"""
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")


def mark_ca(items, answer):
    out = []
    for i, text in enumerate(items):
        cleaned = re.sub(r"^[○✅❌]\s*", "", text)
        prefix = "✅" if i + 1 == answer else "❌"
        out.append(f"{prefix} {cleaned}")
    return out

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade4", "2026-1", "data.json",
)

section2 = {
    "name": "大問2",
    "nameEn": "Part 2",
    "type": "vocabulary",
    "instruction": "次の(16)から(20)までの会話について、( )に入れるのに最も適切なものを1, 2, 3, 4の中から一つ選び、その番号のマーク欄をぬりつぶしなさい。",
    "questions": [
        {
            "number": 16,
            "text": "Girl: I forgot my red pen. (　)\nBoy: Of course you can. Here you are.",
            "choices": [
                "Will you go home soon?",
                "Is the color OK?",
                "Do you like writing?",
                "Can I borrow yours?",
            ],
            "answer": 4,
            "grammar": "Can I borrow yours?＝「あなたのを借りていい？」。Of course you can. Here you are.（もちろん、はいどうぞ）が肯定の返答。",
            "grammarSimple": "Can I borrow yours? は「あなたのをかりていい？」。「もちろん！」ってあかペンをかしてくれるよ。",
            "choiceAnalysis": [
                "Will you go home soon?＝「すぐ家に帰る？」。ペンを借りる依頼への返答にならない。",
                "Is the color OK?＝「色は大丈夫？」。借りる許可を求める質問ではない。",
                "Do you like writing?＝「書くのは好き？」。Of course you can. への自然な前置きにならない。",
                "○ Can I borrow yours?＝「あなたのを借りていい？」。Here you are. とぴったりつながる。",
            ],
            "choiceAnalysisSimple": [
                "「すぐかえう？」はかりる話じゃないよ。",
                "「いろはだいじょうぶ？」はかりるおねがいじゃないよ。",
                "「かくのすき？」は合わないよ。",
                "○「あなたのをかりていい？」がぴったり！「はいどうぞ」ってこたえてる！",
            ],
            "questionAudio": "audio/q16.mp3",
            "translation": "女の子：赤いペンを忘れちゃった。（　）\n男の子：もちろんいいよ。はいどうぞ。",
            "choiceTranslations": [
                "すぐ家に帰る？",
                "色は大丈夫？",
                "書くのは好き？",
                "あなたのを借りていい？",
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
            "answer": 2,
            "grammar": "It's too tall.＝「高すぎる」。Let's climb the one over there.（あっちの木に登ろう）という別の木への提案とつながる。",
            "grammarSimple": "It's too tall. は「たかすぎる」。このきはたかすぎるから、あっちのきにのぼろうって言ってるよ。",
            "choiceAnalysis": [
                "These flowers are pretty.＝「花がきれい」。木に登る話題からずれる。",
                "○ It's too tall.＝「高すぎる」。別の木を提案する理由として自然。",
                "My garden is big.＝「庭が大きい」。登れない理由の説明にならない。",
                "Your house is very nice.＝「家がとてもきれい」。木に登る話題と無関係。",
            ],
            "choiceAnalysisSimple": [
                "「はながきれい」はきのはなしとずれるよ。",
                "○「たかすぎる」がぴったり！あっちのきにのぼろう！",
                "「にわがおおきい」はわけにならないよ。",
                "「いえがきれい」は合わないよ。",
            ],
            "questionAudio": "audio/q17.mp3",
            "translation": "女の子1：この木に登りたい。\n女の子2：（　）あっちの木に登ろう。\n女の子1：うん。",
            "choiceTranslations": [
                "この花はきれいだね。",
                "高すぎるよ。",
                "私の庭は大きいよ。",
                "あなたの家はとてもきれいだね。",
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
            "answer": 4,
            "grammar": "How much are they?＝「いくらですか？」。Two dollars.（2ドルです）が値段の答え。",
            "grammarSimple": "How much are they? は「いくら？」。Two dollars. で「2ドル」ってこたえてるよ！",
            "choiceAnalysis": [
                "How are you doing?＝「調子はどう？」。値段の質問ではない。",
                "How many do you have?＝「いくつ持っている？」。靴下の値段を聞く場面とずれる。",
                "How tall are you?＝「身長は？」。買い物の会話に合わない。",
                "○ How much are they?＝「いくらですか？」。Two dollars. とぴったり。",
            ],
            "choiceAnalysisSimple": [
                "「げんき？」はねだんの話じゃないよ。",
                "「いくつもってる？」はくつしたのねだんじゃないよ。",
                "「しんちょうは？」は合わないよ。",
                "○「いくら？」がぴったり！「2ドル」ってこたえてる！",
            ],
            "questionAudio": "audio/q18.mp3",
            "translation": "男：すみません。この靴下を買いたいんですが。（　）\n店員：2ドルです。",
            "choiceTranslations": [
                "調子はどうですか？",
                "いくつお持ちですか？",
                "身長はどのくらいですか？",
                "いくらですか？",
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
            "answer": 3,
            "grammar": "It's on the kitchen table.＝「キッチンのテーブルの上にある」。探している教科書の場所を教える。",
            "grammarSimple": "It's on the kitchen table. は「キッチンのテーブルのうえにあるよ」。きょうかしょのばしょをおしえてる！",
            "choiceAnalysis": [
                "It's a difficult subject.＝「難しい科目だ」。教科書の場所の答えにならない。",
                "It was very interesting.＝「とても面白かった」。探している本の場所を教えない。",
                "○ It's on the kitchen table.＝「キッチンのテーブルの上」。Thanks. への自然な答え。",
                "It's for your brother.＝「弟のためのもの」。場所の説明にならない。",
            ],
            "choiceAnalysisSimple": [
                "「むずかしいかもくだ」はばしょのこたえじゃないよ。",
                "「おもしろかった」はばしょを教えてないよ。",
                "○「キッチンのテーブルのうえ」がぴったり！ありがとうって言ってる！",
                "「おとうとのため」は合わないよ。",
            ],
            "questionAudio": "audio/q19.mp3",
            "translation": "娘：お父さん、社会の教科書が見つからないの。\n父：（　）\n娘：ありがとう。",
            "choiceTranslations": [
                "難しい科目だよ。",
                "とても面白かったよ。",
                "キッチンのテーブルの上にあるよ。",
                "弟のためのものだよ。",
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
            "answer": 3,
            "grammar": "Are you OK?＝「大丈夫？」。you don't look well（元気そうに見えない）への心配の質問。",
            "grammarSimple": "Are you OK? は「だいじょうぶ？」。げんきそうにみえないから、しんぱいしてきいてるよ。",
            "choiceAnalysis": [
                "Can I go home?＝「家に帰っていい？」。相手の体調を心配する質問ではない。",
                "Did you call me?＝「私を呼んだ？」。元気そうに見えない場面への自然な質問にならない。",
                "○ Are you OK?＝「大丈夫？」。I'm fine. I'm just a little tired. と呼応。",
                "Is your mother a doctor?＝「お母さんは医者？」。体調の心配として不自然。",
            ],
            "choiceAnalysisSimple": [
                "「かえっていい？」はあいてのげんきをきく話じゃないよ。",
                "「よんだ？」は合わないよ。",
                "○「だいじょうぶ？」がぴったり！「ちょっとつかれただけ」ってこたえてる！",
                "「おかあさんはいしゃ？」は合わないよ。",
            ],
            "questionAudio": "audio/q20.mp3",
            "translation": "女の子1：ジェニー、今日は元気そうに見えないね。（　）\n女の子2：大丈夫だよ。ちょっと疲れただけ。",
            "choiceTranslations": [
                "家に帰っていい？",
                "私を呼んだ？",
                "大丈夫？",
                "お母さんは医者？",
            ],
        },
    ],
}

for q in section2["questions"]:
    q["choiceAnalysis"] = mark_ca(q["choiceAnalysis"], q["answer"])

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
    for sec in sections:
        out.append(sec)
        if sec.get("name") == "大問1":
            out.append(section2)
    new_sections = out

data["sections"] = new_sections

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Wrote section2 ({len(section2['questions'])} questions) to {DATA_PATH}")

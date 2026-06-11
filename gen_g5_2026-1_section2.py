# -*- coding: utf-8 -*-
"""
2026年度 第1回（土曜準会場）英検5級 data.json
大問2（会話補充）Q16〜20 — 解説・和訳付き
会話の型ごとに解説の切り口を変えて単調さを避ける。
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade5", "2026-1-sat", "data.json",
)

section2 = {
    "name": "大問2",
    "nameEn": "Part 2",
    "type": "vocabulary",
    "instruction": "次の(16)から(20)までの会話について、( )に入れるのに最も適切なものを1, 2, 3, 4の中から一つ選び、その番号のマーク欄をぬりつぶしなさい。",
    "questions": [
        {
            "number": 16,
            "text": "Woman: I'm a nurse. What do you do?\nMan: (　)",
            "choices": [
                "I'm a cook.",
                "At school.",
                "I like it.",
                "For seven years.",
            ],
            "answer": 1,
            "grammar": "【職業を聞く質問】What do you do? には I'm a ～（職業）で答える。看護師に対して料理人と名乗る流れ。",
            "grammarSimple": "What do you do? は「しごとはなに？」。I'm a cook. で「りょうりにんです」とこたえるよ。",
            "choiceAnalysis": [
                "○ I'm a cook.＝「料理人です」。I'm a nurse. と同じ I'm a ～ の形で職業を答える。",
                "At school.＝「学校で（働く）」では職業名にならない。場所だけでは不十分。",
                "I like it.＝「それが好き」では職業の質問への答えにならない。",
                "For seven years.＝「7年間」は期間の答え。What do you do? には合わない。",
            ],
            "choiceAnalysisSimple": [
                "○「りょうりにんです」がぴったり！しょくぎょうでこたえよう！",
                "「がっこうで」はしょくぎょうのなまえじゃないよ。",
                "「すき」はしごとのこたえじゃないよ。",
                "「7ねんかん」は「どのくらい？」のこたえだよ。",
            ],
            "questionAudio": "audio/q16.mp3",
            "translation": "女性：私は看護師です。あなたのお仕事は？\n男性：（　）",
            "choiceTranslations": [
                "料理人です。",
                "学校で（働きます）。",
                "それが好きです。",
                "7年間です。",
            ],
        },
        {
            "number": 17,
            "text": "Boy: Happy birthday, Linda. (　)\nGirl: Oh, thank you, Mike. They're beautiful.",
            "choices": [
                "I'm cold.",
                "See you.",
                "These flowers are for you.",
                "Help me, please.",
            ],
            "answer": 3,
            "grammar": "【プレゼントの場面】次のセリフ They're beautiful.（きれいね）から、花を渡す言葉が必要。These flowers are for you. が自然。",
            "grammarSimple": "つぎに「きれいね」って言ってるから、花をあげるセリフだよ！These flowers are for you. は「この花をあげるよ」。",
            "choiceAnalysis": [
                "I'm cold.＝「寒い」。thank you / They're beautiful という返事の流れにならない。",
                "See you.＝「またね」。誕生日のプレゼントの場面では不自然。",
                "○ These flowers are for you.＝「この花はあなたへのもの」。beautiful とつながる。",
                "Help me, please.＝「助けて」。お祝いの場面に合わない。",
            ],
            "choiceAnalysisSimple": [
                "「さむい」じゃなくて、プレゼントの話だよ。",
                "「またね」はおいわいの場面じゃないよ。",
                "○「この花をあげるよ」がぴったり！「きれいね」につながる！",
                "「たすけて」は合わないよ。",
            ],
            "questionAudio": "audio/q17.mp3",
            "translation": "男の子：お誕生日おめでとう、リンダ。（　）\n女の子：ありがとう、マイク。とてもきれいね。",
            "choiceTranslations": [
                "寒いよ。",
                "またね。",
                "この花をあげるよ。",
                "助けてください。",
            ],
        },
        {
            "number": 18,
            "text": "Mother: What do you want for lunch, Tom?\nBoy: (　)",
            "choices": [
                "A sandwich, please.",
                "At twelve o'clock.",
                "I'm always hungry.",
                "I can't cook.",
            ],
            "answer": 1,
            "grammar": "【食べ物の注文】What do you want for lunch? には食べたいもの＋please が定番。サンドイッチをお願いする返答。",
            "grammarSimple": "What do you want for lunch? は「ひるごはんになにがほしい？」。A sandwich, please. で「サンドイッチください」！",
            "choiceAnalysis": [
                "○ A sandwich, please.＝「サンドイッチをください」。食べ物の注文としてぴったり。",
                "At twelve o'clock.＝「12時に」は時間の答え。何を食べたいかには答えていない。",
                "I'm always hungry.＝「いつもお腹が空いている」だけでは具体的な注文にならない。",
                "I can't cook.＝「料理ができない」。母が聞いているのは「何が食べたいか」。",
            ],
            "choiceAnalysisSimple": [
                "○「サンドイッチください」がぴったり！たべものをいおう！",
                "「12じ」はじかんのこたえだよ。",
                "「いつもおなかすいた」だけじゃ、なにをたべるかわからないよ。",
                "「りょうりできない」は質問とちがうよ。",
            ],
            "questionAudio": "audio/q18.mp3",
            "translation": "母：トム、お昼ごはんは何が食べたい？\n男の子：（　）",
            "choiceTranslations": [
                "サンドイッチをください。",
                "12時です。",
                "いつもお腹が空いています。",
                "料理ができません。",
            ],
        },
        {
            "number": 19,
            "text": "Mother: Is your history test today, John?\nBoy: No, (　)",
            "choices": [
                "I study history.",
                "in my room.",
                "it's tomorrow.",
                "it's cloudy today.",
            ],
            "answer": 3,
            "grammar": "【No のあとで訂正】今日テスト？→いいえ、明日です。today と tomorrow の対比がポイント。",
            "grammarSimple": "Is your test today? に No, と言ったあとは、正しい日を言うよ。it's tomorrow. で「あしただよ」！",
            "choiceAnalysis": [
                "I study history.＝「歴史を勉強する」。テストの日の話にならない。",
                "in my room.＝「自分の部屋で」は場所の答え。今日かどうかの訂正にならない。",
                "○ it's tomorrow.＝「明日だ」。No, で today を訂正する自然な答え。",
                "it's cloudy today.＝「今日は曇り」。天気の話で、テストの日には答えていない。",
            ],
            "choiceAnalysisSimple": [
                "「れきしをべんきょうする」は日にちの話じゃないよ。",
                "「へやのなかで」はばしょのこたえだよ。",
                "○「あしただよ」がぴったり！きょうじゃないって言ってるよ！",
                "「くもり」はてんきの話だよ。",
            ],
            "questionAudio": "audio/q19.mp3",
            "translation": "母：ジョン、歴史のテストは今日？\n男の子：ううん、（　）",
            "choiceTranslations": [
                "歴史を勉強します。",
                "自分の部屋で。",
                "明日です。",
                "今日は曇りです。",
            ],
        },
        {
            "number": 20,
            "text": "Man 1: Hi, Bill. (　)\nMan 2: Good, thanks.",
            "choices": [
                "When do you go?",
                "How old are you?",
                "How are you doing?",
                "What are you doing?",
            ],
            "answer": 3,
            "grammar": "【あいさつの決まり文句】Good, thanks. は How are you doing?（調子はどう？）への返事。近況を聞いてから元気と答える流れ。",
            "grammarSimple": "Good, thanks. は「げんきだよ、ありがとう」。だから前は How are you doing? 「げんき？」だよ！",
            "choiceAnalysis": [
                "When do you go?＝「いつ行く？」。Good, thanks. という返事には合わない。",
                "How old are you?＝「何歳？」。年齢の答えとして Good, thanks. は不自然。",
                "○ How are you doing?＝「調子はどう？」。Good, thanks. とセットのあいさつ。",
                "What are you doing?＝「何してる？」。今の行動を聞く質問で、返事の形が合わない。",
            ],
            "choiceAnalysisSimple": [
                "「いついく？」じゃないよ。",
                "「なんさい？」のこたえは Good, thanks. じゃないよ。",
                "○ How are you doing? がぴったり！「げんき？」→「げんきだよ」！",
                "「なにしてる？」はちがう質問だよ。",
            ],
            "questionAudio": "audio/q20.mp3",
            "translation": "男性1：やあ、ビル。（　）\n男性2：元気だよ、ありがとう。",
            "choiceTranslations": [
                "いつ行くの？",
                "何歳？",
                "調子はどう？",
                "何をしているの？",
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
    for sec in sections:
        out.append(sec)
        if sec.get("name") == "大問1":
            out.append(section2)
    new_sections = out

data["sections"] = new_sections

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Wrote section2 ({len(section2['questions'])} questions) to {DATA_PATH}")

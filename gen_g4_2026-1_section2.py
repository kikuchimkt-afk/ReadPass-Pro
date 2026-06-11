# -*- coding: utf-8 -*-
"""
2026年度 第1回（土曜準会場）英検4級 data.json
大問2（会話補充）Q16〜20 — 解説・和訳付き
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade4", "2026-1-sat", "data.json",
)

section2 = {
    "name": "大問2",
    "nameEn": "Part 2",
    "type": "vocabulary",
    "instruction": "次の(16)から(20)までの会話について、( )に入れるのに最も適切なものを1, 2, 3, 4の中から一つ選び、その番号のマーク欄をぬりつぶしなさい。",
    "questions": [
        {
            "number": 16,
            "text": "Father: Eric, it's dinnertime. Please tell Mom.\nSon: (　) She's talking with Aunt Jill.",
            "choices": [
                "I'll go to the store.",
                "She's on the phone.",
                "I have an idea.",
                "She doesn't like cooking.",
            ],
            "answer": 2,
            "grammar": "She's on the phone.＝「母さんは電話中だ」。talking with Aunt Jill（ジルおばさんと話している）とつながる。",
            "grammarSimple": "She's on the phone. は「ママはでんわちゅう」。ジルおばさんと話してるから、今は伝えられないよ。",
            "choiceAnalysis": [
                "I'll go to the store.＝「店に行くよ」。夕食の時間に母に伝える依頼への返答にならない。",
                "○ She's on the phone.＝「電話中だ」。Aunt Jill と話している理由の説明と一致。",
                "I have an idea.＝「いい考えがある」。母に伝えられない理由の説明にならない。",
                "She doesn't like cooking.＝「料理が嫌い」。dinnertime の話題とはずれる。",
            ],
            "choiceAnalysisSimple": [
                "「みせに行く」は合わないよ。",
                "○「でんわちゅう」がぴったり！ジルおばさんと話してるよ！",
                "「いいかんがえがある」はわけにならないよ。",
                "「りょうりがきらい」ははなしがずれるよ。",
            ],
            "questionAudio": "audio/q16.mp3",
            "translation": "父：エリック、夕食の時間だよ。お母さんに伝えて。\n息子：（　）ジルおばさんと話しているよ。",
            "choiceTranslations": [
                "店に行くよ。",
                "電話中だよ。",
                "いい考えがあるよ。",
                "料理が嫌いなんだ。",
            ],
        },
        {
            "number": 17,
            "text": "Father: I'm going to the video shop. (　)\nDaughter: Yes. I'll get my bag.",
            "choices": [
                "How are you doing?",
                "Do you want to come?",
                "How much is it?",
                "Is it new?",
            ],
            "answer": 2,
            "grammar": "Do you want to come?＝「一緒に行く？」。Yes. I'll get my bag.（うん、カバンを取ってくる）が肯定の返答。",
            "grammarSimple": "Do you want to come? は「いっしょに行く？」。「うん！」って言ってかばんをもってくるよ。",
            "choiceAnalysis": [
                "How are you doing?＝「調子はどう？」。一緒に行くかどうかの質問ではない。",
                "○ Do you want to come?＝「一緒に来たい？」。Yes と bag を取る行動とぴったり。",
                "How much is it?＝「いくら？」。値段の質問で、同行の返答にならない。",
                "Is it new?＝「新しい？」。文脈に合わない。",
            ],
            "choiceAnalysisSimple": [
                "「げんき？」はいっしょに行く話じゃないよ。",
                "○「いっしょに行く？」がぴったり！「うん！」ってかばんをもってくる！",
                "「いくら？」はねだんの話だよ。",
                "「あたらしい？」は合わないよ。",
            ],
            "questionAudio": "audio/q17.mp3",
            "translation": "父：ビデオ屋に行くんだ。（　）\n娘：うん。カバンを取ってくるね。",
            "choiceTranslations": [
                "調子はどう？",
                "一緒に行く？",
                "いくら？",
                "新しいの？",
            ],
        },
        {
            "number": 18,
            "text": "Daughter: Can you take me to the supermarket today, Dad?\nFather: Sorry, Lisa. (　) now.",
            "choices": [
                "I'm going to work",
                "It's too small",
                "She's at home",
                "That's not yours",
            ],
            "answer": 1,
            "grammar": "I'm going to work now.＝「今から仕事に行くところ」。スーパーに連れて行けない理由。",
            "grammarSimple": "I'm going to work は「しごとに行くところ」。きょうはスーパーに連れて行けないよ。",
            "choiceAnalysis": [
                "○ I'm going to work＝「仕事に行く」。Sorry と now で「今は無理」の流れ。",
                "It's too small＝「小さすぎる」。スーパーに行けない理由にならない。",
                "She's at home＝「彼女は家にいる」。父の都合の説明にならない。",
                "That's not yours＝「それは君のじゃない」。依頼への断りの理由として不自然。",
            ],
            "choiceAnalysisSimple": [
                "○「しごとに行く」がぴったり！ごめん、いまはむりだよ！",
                "「ちいさすぎる」はわけにならないよ。",
                "「かのじょはいえにいる」は合わないよ。",
                "「あなたのじゃない」は合わないよ。",
            ],
            "questionAudio": "audio/q18.mp3",
            "translation": "娘：お父さん、今日スーパーに連れて行ってくれる？\n父：ごめんね、リサ。（　）ところなんだ。",
            "choiceTranslations": [
                "仕事に行く",
                "小さすぎる",
                "彼女は家にいる",
                "それはあなたのじゃない",
            ],
        },
        {
            "number": 19,
            "text": "Girl 1: I'm looking for my umbrella.\nGirl 2: What does it look like?\nGirl 1: (　)",
            "choices": [
                "Of course.",
                "That's too bad.",
                "That's all.",
                "It's red and white.",
            ],
            "answer": 4,
            "grammar": "What does it look like?＝「どんな見た目？」。It's red and white.＝「赤と白だよ」が答え。",
            "grammarSimple": "What does it look like? は「どんなかんじ？」。It's red and white. で「あかとしろ」ってこたえるよ！",
            "choiceAnalysis": [
                "Of course.＝「もちろん」。見た目の説明にならない。",
                "That's too bad.＝「残念だね」。傘の色や形の説明にならない。",
                "That's all.＝「それだけ」。look like への答えにならない。",
                "○ It's red and white.＝「赤と白だ」。傘の見た目の説明として自然。",
            ],
            "choiceAnalysisSimple": [
                "「もちろん」はみためのこたえじゃないよ。",
                "「ざんねん」はみためのこたえじゃないよ。",
                "「それだけ」はこたえにならないよ。",
                "○「あかとしろ」がぴったり！かさのかんじを説明してる！",
            ],
            "questionAudio": "audio/q19.mp3",
            "translation": "女の子1：傘を探しているの。\n女の子2：どんな見た目？\n女の子1：（　）",
            "choiceTranslations": [
                "もちろん。",
                "残念だね。",
                "それだけ。",
                "赤と白だよ。",
            ],
        },
        {
            "number": 20,
            "text": "Daughter: What's wrong, Dad?\nFather: I'm looking for my wallet. I looked in every room, but (　)\nDaughter: I'll help you.",
            "choices": [
                "there wasn't any.",
                "it wasn't mine.",
                "I can't find it.",
                "you didn't like it.",
            ],
            "answer": 3,
            "grammar": "I can't find it.＝「見つけられない」。every room を探したのに財布が見つからない。",
            "grammarSimple": "I can't find it. は「みつけられない」。へやをぜんぶさがしたけど、さいふがみつからないよ。",
            "choiceAnalysis": [
                "there wasn't any.＝「何もなかった」。wallet は it で指すので I can't find it の方が自然。",
                "it wasn't mine.＝「私のものじゃなかった」。探している財布が自分のものでない、という話にはならない。",
                "○ I can't find it.＝「見つけられない」。looking for my wallet とつながる。",
                "you didn't like it.＝「君はそれが好きじゃなかった」。文脈に合わない。",
            ],
            "choiceAnalysisSimple": [
                "「なにもなかった」はさいふの話として不自然だよ。",
                "「ぼくのじゃなかった」は合わないよ。",
                "○「みつけられない」がぴったり！さいふがみつからない！",
                "「すきじゃなかった」は合わないよ。",
            ],
            "questionAudio": "audio/q20.mp3",
            "translation": "娘：どうしたの、お父さん？\n父：財布を探しているんだ。全部屋を探したけど、（　）\n娘：手伝うね。",
            "choiceTranslations": [
                "何もなかった。",
                "私のものじゃなかった。",
                "見つけられない。",
                "君はそれが好きじゃなかった。",
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

# -*- coding: utf-8 -*-
"""
2026年度 第1回（土曜準会場）英検3級 data.json
大問2（会話補充）Q16〜20 — 解説・和訳付き
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade3", "2026-1-sat", "data.json",
)

section2 = {
    "name": "大問2",
    "nameEn": "Part 2",
    "type": "vocabulary",
    "instruction": "次の(16)から(20)までの会話について、( )に入れるのに最も適切なものを1, 2, 3, 4の中から一つ選び、その番号のマーク欄をぬりつぶしなさい。",
    "questions": [
        {
            "number": 16,
            "text": "Sister: Jim, could you show me how to use your computer?\nBrother: (　) This TV show will finish in 10 minutes.",
            "choices": [
                "I've played that before.",
                "It's my favorite game.",
                "I'll help you soon.",
                "It's too easy for you.",
            ],
            "answer": 3,
            "grammar": "I'll help you soon＝「すぐ手伝うよ」。TV番組があと10分で終わる→そのあと手伝う。",
            "grammarSimple": "I'll help you soon は「すぐてつだうよ」。テレビが10ぷんでおわったらてつだうね。",
            "choiceAnalysis": [
                "I've played that before＝「前にやったことがある」。パソコンの使い方を教える依頼への返答にならない。",
                "It's my favorite game＝「それが一番好きなゲーム」。妹の質問に答えていない。",
                "○ I'll help you soon＝「すぐ手伝うよ」。10分後に手伝うという流れと一致。",
                "It's too easy for you＝「君には簡単すぎる」。文脈に合わず、不自然な返答。",
            ],
            "choiceAnalysisSimple": [
                "「まえにやったことある」は合わないよ。",
                "「いちばんすきなゲーム」は質問のこたえにならないよ。",
                "○「すぐてつだうよ」。10ぷんしたらてつだうね！",
                "「かんたんすぎる」はへんなこたえだよ。",
            ],
            "translation": "姉：ジム、パソコンの使い方を教えてくれない？\n兄：（　）このテレビ番組はあと10分で終わるよ。",
            "choiceTranslations": [
                "前にやったことがあるよ。",
                "それが一番好きなゲームだよ。",
                "すぐ手伝うよ。",
                "君には簡単すぎるよ。",
            ],
        },
        {
            "number": 17,
            "text": "Father: Your birthday is next Saturday. (　)\nSon: I want to go ice-skating with my friends.",
            "choices": [
                "What happened at your party?",
                "How many people will come?",
                "What would you like to do?",
                "How old will you be?",
            ],
            "answer": 3,
            "grammar": "What would you like to do?＝「何をしたい？」。誕生日の過ごし方を聞く質問。",
            "grammarSimple": "What would you like to do? は「なにをしたい？」。たんじょうびになにをしたいかきいてるよ。",
            "choiceAnalysis": [
                "What happened at your party?＝「パーティーで何があった？」。まだ誕生日は来ていないので過去の話になってしまう。",
                "How many people will come?＝「何人が来る？」。息子の答え「アイススケートに行きたい」とつながらない。",
                "○ What would you like to do?＝「何をしたい？」。ice-skating with my friends という答えとぴったり。",
                "How old will you be?＝「何歳になる？」。年齢ではなく活動の内容を答えている。",
            ],
            "choiceAnalysisSimple": [
                "「パーティーでなにがあった？」はまだたんじょうびじゃないよ。",
                "「なんにんくる？」はこたえとつながらないよ。",
                "○「なにをしたい？」アイススケートに行きたい！",
                "「なんさいになる？」はこたえがちがうよ。",
            ],
            "translation": "父：来週の土曜日は君の誕生日だね。（　）\n息子：友達とアイススケートに行きたいな。",
            "choiceTranslations": [
                "パーティーで何があったの？",
                "何人が来るの？",
                "何をしたい？",
                "何歳になるの？",
            ],
        },
        {
            "number": 18,
            "text": "Mother: Why is your baseball cap on the sofa? Take it to your room.\nSon: (　) I have practice at three.",
            "choices": [
                "We won again.",
                "Did you look for it over there?",
                "I'm going to wear it today.",
                "Will you come and watch?",
            ],
            "answer": 3,
            "grammar": "I'm going to wear it today＝「今日はそれをかぶるつもり」。3時の練習のため、部屋に片づけていない理由。",
            "grammarSimple": "I'm going to wear it today は「きょうかぶるよ」。3じのれんしゅうがあるから、へやにしまってないんだ。",
            "choiceAnalysis": [
                "We won again＝「また勝った」。帽子がソファにある理由の説明にならない。",
                "Did you look for it over there?＝「あそこで探した？」。母の質問への返答として不自然。",
                "○ I'm going to wear it today＝「今日はかぶるつもり」。practice at three とつながる。",
                "Will you come and watch?＝「見に来てくれる？」。帽子の話題からずれる。",
            ],
            "choiceAnalysisSimple": [
                "「またかった」はぼうしのわけにならないよ。",
                "「あそこでさがした？」はへんなこたえだよ。",
                "○「きょうかぶるよ」。3じのれんしゅうがあるから！",
                "「みにきてくれる？」ははなしがずれるよ。",
            ],
            "translation": "母：どうして野球帽がソファの上にあるの？部屋に持っていきなさい。\n息子：（　）3時に練習があるんだ。",
            "choiceTranslations": [
                "また勝ったよ。",
                "あそこで探した？",
                "今日はそれをかぶるつもりだよ。",
                "見に来てくれる？",
            ],
        },
        {
            "number": 19,
            "text": "Student: Mr. Clark, I can't go to baseball practice today. (　)\nTeacher: That's too bad. Please go home and rest.",
            "choices": [
                "I have a stomachache.",
                "I bought a new bat.",
                "I think we'll win.",
                "I arrived on time.",
            ],
            "answer": 1,
            "grammar": "I have a stomachache＝「お腹が痛い」。go home and rest（家に帰って休みなさい）とつながる。",
            "grammarSimple": "I have a stomachache は「おなかがいたい」。おうちにかえってねむるように言われるよ。",
            "choiceAnalysis": [
                "○ I have a stomachache＝「腹痛がある」。練習に行けない理由＋休むよう言われる流れと一致。",
                "I bought a new bat＝「新しいバットを買った」。練習を休む理由にならない。",
                "I think we'll win＝「勝てると思う」。練習に行けない理由の説明にならない。",
                "I arrived on time＝「時間通りに着いた」。練習に行けないという発言と矛盾。",
            ],
            "choiceAnalysisSimple": [
                "○「おなかがいたい」。れんしゅうにいけないし、ねむれって言われるよ。",
                "「あたらしいバットをかった」はやすむわけにならないよ。",
                "「かてるとおもう」はりゆうにならないよ。",
                "「じかんどおりについた」は「いけない」とちがうよ。",
            ],
            "translation": "生徒：クラーク先生、今日は野球の練習に行けません。（　）\n先生：それは残念だね。家に帰って休みなさい。",
            "choiceTranslations": [
                "お腹が痛いんです。",
                "新しいバットを買いました。",
                "勝てると思います。",
                "時間通りに着きました。",
            ],
        },
        {
            "number": 20,
            "text": "Mother: Uncle Joe will come to visit us on Sunday morning, John.\nSon: Sorry, Mom. I have baseball practice then. (　)\nMother: OK, I will.",
            "choices": [
                "Have a nice trip.",
                "Say hello to him for me.",
                "He has just left.",
                "I know he doesn't.",
            ],
            "answer": 2,
            "grammar": "Say hello to him for me＝「私の代わりにあいさつして」。母の OK, I will.（わかった、するね）と呼応。",
            "grammarSimple": "Say hello to him for me は「ぼくのかわりにあいさつして」。ママが「わかった、するね」とこたえるよ。",
            "choiceAnalysis": [
                "Have a nice trip＝「良い旅を」。ジョーおじさんは「訪ねてくる」ので旅のあいさつではない。",
                "○ Say hello to him for me＝「私の代わりにあいさつして」。練習で会えない→母が代わりにあいさつ。",
                "He has just left＝「彼はちょうど出て行った」。訪問予定の話と矛盾。",
                "I know he doesn't＝「来ないことは知っている」。文脈に合わない。",
            ],
            "choiceAnalysisSimple": [
                "「良い旅を」はおじさんが「きてくれる」から合わないよ。",
                "○「ぼくのかわりにあいさつして」。ママが「わかった、するね」！",
                "「ちょうどでかけた」ははなしとちがうよ。",
                "「こないってしってる」は合わないよ。",
            ],
            "translation": "母：ジョン、日曜の朝におじのジョーが遊びに来るわよ。\n息子：ごめん、ママ。その時間は野球の練習があるんだ。（　）\n母：わかった、そうするわね。",
            "choiceTranslations": [
                "良い旅を。",
                "私の代わりにあいさつして。",
                "彼はちょうど出て行ったよ。",
                "彼は来ないって知ってるよ。",
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
    # 大問1の直後に挿入
    out = []
    for sec in new_sections:
        out.append(sec)
        if sec.get("name") == "大問1":
            out.append(section2)
    new_sections = out

data["sections"] = new_sections

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Wrote section2 ({len(section2['questions'])} questions) to {DATA_PATH}")

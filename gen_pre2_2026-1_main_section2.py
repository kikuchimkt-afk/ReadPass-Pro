# -*- coding: utf-8 -*-
"""
2026年度 第1回（本会場）英検準2級 data.json
Step B: 大問2（vocabulary型・会話完成）Q16〜20 — リッチ解説
一次ソース: 2026-1(本会場）/準2級.pdf / 準2級解答.pdf
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade-pre2", "2026-1", "data.json",
)

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

section2 = {
    "name": "大問2",
    "nameEn": "Part 2",
    "type": "vocabulary",
    "instruction": "次の四つの会話文を完成させるために，(16)から(20)に入るものとして最も適切なものを1，2，3，4の中から一つ選びなさい。",
    "questions": [
        {
            "number": 16,
            "text": (
                "A: Excuse me. Do you know the way to the Greenlake Theater?\n"
                "B: Yes. Go straight down this street, then turn right at the second light. "
                "After that, walk for about five minutes. The theater will be on your left.\n"
                "A: Thanks. I'm not sure if I can get there, but I'll try.\n"
                "B: Well, I'm going in the same direction, so ( 16 ). Please follow me."
            ),
            "translation": (
                "A：すみません。グリーンレイク劇場への行き方をご存じですか？\n"
                "B：はい。この通りをまっすぐ行って、2つ目の信号を右に曲がってください。"
                "そのあと約5分歩くと、劇場は左側にあります。\n"
                "A：ありがとう。たどり着けるかわからないけど、やってみます。\n"
                "B：私も同じ方向に行くので、( 16 )。ついてきてください。"
            ),
            "choices": [
                "I can take you there",
                "I can take the wrong way",
                "you won't make it",
                "you won't see me again",
            ],
            "choiceTranslations": [
                "そこへ連れて行ってあげられる",
                "間違った道を行ける",
                "たどり着けないだろう",
                "もう会えないだろう",
            ],
            "answer": 1,
            "choiceAnalysis": [
                "✅ I can take you there＝そこへ連れて行ってあげられる。I'm going in the same direction（同じ方向に行く）＋Please follow me（ついてきて）が、案内して連れて行く申し出と一致→正解",
                "❌ I can take the wrong way＝間違った道を行ける。Please follow me（ついてきて）と案内する直前に、わざと道を間違えると言うのは会話の流れと合わない",
                "❌ you won't make it＝たどり着けないだろう。AはI'll try（やってみる）と前向き。Bが同じ方向に行くと言ったうえで見込みを否定するのは矛盾",
                "❌ you won't see me again＝もう会えないだろう。Please follow me（ついてきて）とセットで使えない。別れの場面の表現",
            ],
            "grammar": "💡 take 人 there＝人をそこへ連れて行く。in the same direction（同じ方向に）＋follow me（ついてきて）が「一緒に行って案内する」流れの決め手。",
        },
        {
            "number": 17,
            "text": (
                "A: Lucas, which gym do you go to? I'm thinking about joining one.\n"
                "B: That's great! I go to the one next to the supermarket, but there's a new one closer to your place. "
                "It just opened last month.\n"
                "A: Oh, where is it?\n"
                "B: It's right across from the movie theater. It's ( 17 ). "
                "I haven't been there, but people say it's good."
            ),
            "translation": (
                "A：ルーカス、どのジムに通ってるの？私も入会しようかなって思ってて。\n"
                "B：いいね！僕はスーパーの隣のところに通ってるけど、あなたの家の近くにもっと近い新しいところがあるよ。"
                "先月オープンしたんだ。\n"
                "A：へえ、どこにあるの？\n"
                "B：映画館の向かいだよ。( 17 )。まだ行ったことないけど、評判はいいって。"
            ),
            "choices": [
                "the closest to the supermarket",
                "only about one year old",
                "about five minutes from your house",
                "too noisy and small for real training",
            ],
            "choiceTranslations": [
                "スーパーに一番近い",
                "開いてから約1年しかたっていない",
                "あなたの家から約5分のところ",
                "本格的なトレーニングにはうるさくて狭すぎる",
            ],
            "answer": 3,
            "choiceAnalysis": [
                "❌ the closest to the supermarket＝スーパーに一番近い。Bは自分が通うのはスーパー隣のジムと言っており、紹介しているのはcloser to your place（あなたの家の近く）の新しいジム。聞き手の家からの距離が論点",
                "❌ only about one year old＝開いてから約1年。直前のIt just opened last month（先月オープン）と矛盾する",
                "✅ about five minutes from your house＝家から約5分のところ。closer to your place（あなたの家の近く）という紹介の続きとして、家からの距離を示す表現が自然→正解",
                "❌ too noisy and small for real training＝うるさくて狭すぎる。直後のpeople say it's good（評判はいい）と正反対のネガティブな内容",
            ],
            "grammar": "💡 closer to your place＝あなたの家の近く。会話の主題が「聞き手に便利なジムの場所」なので、from your house（家から）の距離が決め手。",
        },
        {
            "number": 18,
            "text": (
                "A: Hello. I'd like to sign up for one of the volunteer programs this summer.\n"
                "B: Of course! May I ask ( 18 )? We have plenty to choose from.\n"
                "A: Sure. Is \"Let's Work as a Librarian\" still open? I believe it begins on August 10.\n"
                "B: Let me check. Yes, it's still available. Please go ahead and fill out this form."
            ),
            "translation": (
                "A：こんにちは。この夏のボランティアプログラムのどれかに申し込みたいのですが。\n"
                "B：もちろんです！( 18 )お聞きしてもよろしいですか？選べるプログラムはたくさんありますよ。\n"
                "A：はい。「司書として働こう」はまだ空いていますか？8月10日からだと思うのですが。\n"
                "B：確認しますね。はい、まだ空いています。この用紙に記入してください。"
            ),
            "choices": [
                "how you learned about our programs",
                "which program you're interested in",
                "what kinds of books you enjoy reading",
                "when your summer vacation finishes",
            ],
            "choiceTranslations": [
                "プログラムをどうやって知ったか",
                "どのプログラムに興味があるか",
                "どんな本を読むのが好きか",
                "夏休みがいつ終わるか",
            ],
            "answer": 2,
            "choiceAnalysis": [
                "❌ how you learned about our programs＝どうやって知ったか。申し込みの場面で聞くことは可能だが、Aの返答が具体的なプログラム名（Let's Work as a Librarian）であることから、先に「どれに興味があるか」を聞いた流れが自然",
                "✅ which program you're interested in＝どのプログラムに興味があるか。We have plenty to choose from（たくさん選べる）→Aが特定のプログラム名を答える、という申し込みの定番の流れ→正解",
                "❌ what kinds of books you enjoy reading＝どんな本が好きか。Aの返答がIs \"Let's Work as a Librarian\" still open?（司書プログラムは空いているか）なので、先にどのプログラムかを聞く流れが自然",
                "❌ when your summer vacation finishes＝夏休みがいつ終わるか。申し込み時に必ずしも聞かない情報。Aの返答（プログラム名）とも結びつかない",
            ],
            "grammar": "💡 May I ask ～?＝～をお聞きしてもよろしいですか。plenty to choose from（選べるものがたくさん）→which program（どのプログラムか）の順序に注目。",
        },
        {
            "number": 19,
            "text": DIALOGUE_19_20,
            "translation": (
                "A：お父さん、お弁当はどこ？今日学校に持っていかなきゃいけないの。\n"
                "B：お弁当？でも君は( 19 )でしょ。なんで自分で持っていかなきゃいけないの？\n"
                "A：今日から学食は修理のため閉まっていて、みんな自分のお弁当を持ってこなきゃいけないの。"
                "学校からの手紙見なかった？先週渡したのに。\n"
                "B：うーん、見逃したかも。学食はいつまた開くの？\n"
                "A：来週の月曜日まで開かないよ。じゃあ、今作る時間ある？\n"
                "B：ないと思う。今日は( 20 )してくれる？\n"
                "A：わかった。お気に入りのパン屋に寄るね。でも今週の残りの日はお弁当作るの忘れないでね。\n"
                "B：わかった、忘れないよ。"
            ),
            "choices": [
                "usually eat at the cafeteria",
                "always make your own lunch",
                "didn't wake up early enough",
                "don't have school today",
            ],
            "choiceTranslations": [
                "たいてい学食で食べている",
                "いつも自分でお弁当を作っている",
                "十分に早く起きなかった",
                "今日は学校がない",
            ],
            "answer": 1,
            "choiceAnalysis": [
                "✅ usually eat at the cafeteria＝たいてい学食で食べている。Why do you need to bring your own?（なぜ持っていく必要があるの？）という父の驚きと一致。今日から学食が閉まるという突然の変化が理由→正解",
                "❌ always make your own lunch＝いつも自分で作っている。Why do you need to bring your own?（なぜ持っていく必要があるの？）と驚くなら、いつも持参している習慣とは合わない",
                "❌ didn't wake up early enough＝十分に早く起きなかった。お弁当を持っていく理由（学食が閉まっている）とは無関係",
                "❌ don't have school today＝今日は学校がない。AのI need to take it to school today（今日学校に持っていく）と矛盾",
            ],
            "grammar": "💡 usually eat at the cafeteria＝たいてい学食で食べる。But you ～（でも君は～でしょ）が「いつもの習慣」と「今日は持参」のギャップを示す。",
        },
        {
            "number": 20,
            "text": DIALOGUE_19_20,
            "translation": (
                "A：お父さん、お弁当はどこ？今日学校に持っていかなきゃいけないの。\n"
                "B：お弁当？でも君は( 19 )でしょ。なんで自分で持っていかなきゃいけないの？\n"
                "A：今日から学食は修理のため閉まっていて、みんな自分のお弁当を持ってこなきゃいけないの。"
                "学校からの手紙見なかった？先週渡したのに。\n"
                "B：うーん、見逃したかも。学食はいつまた開くの？\n"
                "A：来週の月曜日まで開かないよ。じゃあ、今作る時間ある？\n"
                "B：ないと思う。今日は( 20 )してくれる？\n"
                "A：わかった。お気に入りのパン屋に寄るね。でも今週の残りの日はお弁当作るの忘れないでね。\n"
                "B：わかった、忘れないよ。"
            ),
            "choices": [
                "ask your teacher to make it",
                "eat at the school cafeteria",
                "buy something on your way",
                "make something by yourself",
            ],
            "choiceTranslations": [
                "先生にお弁当を作ってもらう",
                "学校の学食で食べる",
                "行き道で何か買う",
                "自分で何か作る",
            ],
            "answer": 3,
            "choiceAnalysis": [
                "❌ ask your teacher to make it＝先生に作ってもらう。do you have time to make it now?（今作る時間はある？）という父娘の会話で、先生の登場はない",
                "❌ eat at the school cafeteria＝学食で食べる。the cafeteria will be closed for repairs（学食は修理で閉まっている）と矛盾",
                "✅ buy something on your way＝行き道で何か買う。I don't think so（今作る時間はない）→Can you ～ today?（今日は～してくれる？）→I'll stop by my favorite bakery（パン屋に寄る）が呼応→正解",
                "❌ make something by yourself＝自分で作る。Can you buy something on your way today?（今日は行き道で買ってくれる？）と頼む場面で、自分で作れという内容ではない",
            ],
            "grammar": "💡 on your way＝行き道で。stop by ～（～に寄る）とセットで「通りがかりに買う」流れ。今作る時間がない→買ってくる、という代替案。",
        },
    ],
}

with open(DATA_PATH, encoding="utf-8") as f:
    data = json.load(f)

section1 = next(s for s in data["sections"] if s["name"] == "大問1")
others = [s for s in data["sections"] if s["name"] not in ("大問1", "大問2")]
data["sections"] = [section1, section2] + others

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Wrote section2 ({len(section2['questions'])} questions) to {DATA_PATH}")

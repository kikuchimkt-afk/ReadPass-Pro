# -*- coding: utf-8 -*-
"""
2026年度 第1回（土曜準会場）英検準2級 data.json
Step B: 大問2（vocabulary型・会話完成）Q16〜20
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade-pre2", "2026-1-sat", "data.json",
)

DIALOGUE_19_20 = (
    "A : Thanks for calling. This is Ken from Tokyo Tours.\n"
    "B : Hello, Ken. This is Rachel Jones. I'm joining one of your tours today. "
    "I believe you're supposed to pick me up at the airport, but I don't see you.\n"
    "A : I'm sorry about that, Ms. Jones. I'm on my way. Can you tell me ( 19 )?\n"
    "B : Sure. I'm in the arrival area on the third floor. "
    "There's a big statue of a woman right in front of me.\n"
    "A : Ah, I think I know where that is. Do you see some chairs behind the statue?\n"
    "B : Yes, I do.\n"
    "A : Great! Please stay right there. ( 20 ).\n"
    "B : Thanks, Ken. I'll wait for you."
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
                "A : Excuse me, does this bus stop at the city museum?\n"
                "B : It does, but there's another bus that ( 16 ). It'll arrive here in five minutes.\n"
                "A : Oh, nice. I want to get there as soon as possible because the museum will close at 5:00 p.m.\n"
                "B : Yeah, and with that one, you won't have to worry about getting off at the wrong stop."
            ),
            "translation": (
                "A：すみません。このバスは市立博物館に停まりますか？\n"
                "B：停まりますが、( 16 )別のバスがあります。5分でここに来ますよ。\n"
                "A：いいですね。博物館は午後5時に閉まるので、できるだけ早く着きたいんです。\n"
                "B：そうだね。そのバスなら、降りるバス停を間違える心配もないよ。"
            ),
            "choices": [
                "goes straight there",
                "makes more stops",
                "holds more passengers",
                "runs late at night",
            ],
            "choiceTranslations": [
                "そこへ直行する",
                "もっとたくさん停まる",
                "より多くの乗客を載せる",
                "夜遅く運行する",
            ],
            "answer": 1,
            "choiceAnalysis": [
                "そこへ直行する。早く着け、降りる停留所を間違えない→正解。💡",
                "停車が増える。as soon as possibleという希望に反する",
                "乗客を多く乗せる。速さや降車場所とは関係がない",
                "夜遅く運行する。午後5時閉館の場面に合わない",
            ],
            "grammar": "💡 go straight there＝そこへ直行する。get off at the wrong stop＝降りる停留所を間違える。",
        },
        {
            "number": 17,
            "text": (
                "A : Hi, I'm calling because my daughter might have left her swim bag at your store today. "
                "It's a yellow one with a pink name sticker on it.\n"
                "B : Let me check. Yes, we have one like that here. May I ask her name?\n"
                "A : It's Emily Stone.\n"
                "B : Well, that ( 17 ). Please feel free to come and pick it up anytime."
            ),
            "translation": (
                "A：こんにちは。娘が今日お店に水泳バッグを忘れたかもしれないので電話しています。"
                "黄色でピンクの名前ステッカーがついているものです。\n"
                "B：確認しますね。はい、そういうのがここにあります。お名前を伺ってもよろしいですか？\n"
                "A：エミリー・ストーンです。\n"
                "B：それなら( 17 )。いつでも取りに来てください。"
            ),
            "choices": [
                "is the name written on the sticker",
                "sounds like someone else's name",
                "sticker is not sold at our store",
                "bag has been lost for a few days",
            ],
            "choiceTranslations": [
                "ステッカーに書かれている名前だ",
                "誰か別の人の名前のようだ",
                "ステッカーは当店では販売していない",
                "バッグは数日間行方不明だった",
            ],
            "answer": 1,
            "choiceAnalysis": [
                "ステッカーの名前とEmily Stoneが一致する→正解。💡",
                "別人の名前。バッグを渡してよいという続きと合わない",
                "ステッカーの販売。忘れ物の持ち主確認とは無関係",
                "数日前から紛失。todayと時期が合わない",
            ],
            "grammar": "💡 pick it up＝（忘れ物を）取りに来る。feel free to ～＝ご自由に～してください。May I ask ～?＝～を伺ってもよろしいですか。",
        },
        {
            "number": 18,
            "text": (
                "A : Amanda's birthday is coming up soon. What should we give her this year?\n"
                "B : Hmm. We're going camping next weekend, so maybe something for that. How about ( 18 )?\n"
                "A : That's a great idea. The one she has is getting too small.\n"
                "B : That's right. It'll keep her warm at night."
            ),
            "translation": (
                "A：アマンダの誕生日がもうすぐだね。今年は何をあげよう？\n"
                "B：うーん。来週末キャンプに行くから、それに使えるものがいいかもね。"
                "( 18 )はどう？\n"
                "A：いいアイデアね。今持っているのは小さくなりすぎてきたの。\n"
                "B：そうだね。夜暖かくしてくれるわ。"
            ),
            "choices": [
                "a new backpack",
                "a cute swimsuit",
                "a large flashlight",
                "a mountain jacket",
            ],
            "choiceTranslations": [
                "新しいバックパック",
                "かわいい水着",
                "大きな懐中電灯",
                "登山用ジャケット",
            ],
            "answer": 4,
            "choiceAnalysis": [
                "バックパック。keep her warm at nightの手がかりに合わない",
                "水着。キャンプの夜に体を暖かくする物ではない",
                "懐中電灯。getting too smallという衣服の説明に合わない",
                "登山用ジャケット。サイズと夜の防寒の両方に合う→正解。💡",
            ],
            "grammar": "💡 keep ～ warm＝～を暖かくする。get too small＝小さくなりすぎる。How about ～?＝～はどう？",
        },
        {
            "number": 19,
            "text": DIALOGUE_19_20,
            "translation": (
                "A：お電話ありがとうございます。東京ツアーズのケンです。\n"
                "B：こんにちは、ケン。レイチェル・ジョーンズです。今日ツアーに参加する予定ですが、"
                "空港で迎えに来てくれるはずなのに見当たりません。\n"
                "A：申し訳ありません、ジョーンズさん。向かっています。( 19 )教えていただけますか？\n"
                "B：はい。3階の到着エリアにいます。目の前に大きな女性の像があります。\n"
                "A：ああ、わかります。その像の後ろに椅子が見えますか？\n"
                "B：はい、見えます。\n"
                "A：よかった！その場所で待っていてください。( 20 )。\n"
                "B：ありがとう、ケン。待っています。"
            ),
            "choices": [
                "what's around you",
                "when you will arrive",
                "who you are with",
                "why you are here",
            ],
            "choiceTranslations": [
                "周りに何があるか",
                "いつ着くか",
                "誰と一緒にいるか",
                "なぜここにいるか",
            ],
            "answer": 1,
            "choiceAnalysis": [
                "周囲に何があるか。Bが到着エリアと女性像を答える→正解。💡",
                "いつ着くか。Bは自分の現在地を説明している",
                "誰といるか。返答に同行者は出てこない",
                "なぜいるか。ツアー参加だとすでに説明している",
            ],
            "grammar": "💡 Can you tell me ～?＝～を教えてくれますか。arrival area＝到着ロビー・到着エリア。right in front of ～＝～のすぐ前に。",
        },
        {
            "number": 20,
            "text": DIALOGUE_19_20,
            "translation": (
                "A：お電話ありがとうございます。東京ツアーズのケンです。\n"
                "B：こんにちは、ケン。レイチェル・ジョーンズです。今日ツアーに参加する予定ですが、"
                "空港で迎えに来てくれるはずなのに見当たりません。\n"
                "A：申し訳ありません、ジョーンズさん。向かっています。( 19 )教えていただけますか？\n"
                "B：はい。3階の到着エリアにいます。目の前に大きな女性の像があります。\n"
                "A：ああ、わかります。その像の後ろに椅子が見えますか？\n"
                "B：はい、見えます。\n"
                "A：よかった！その場所で待っていてください。( 20 )。\n"
                "B：ありがとう、ケン。待っています。"
            ),
            "choices": [
                "I'll call you back tomorrow",
                "I'll be there in five minutes",
                "Your flight is coming up",
                "Your plane is arriving soon",
            ],
            "choiceTranslations": [
                "明日また電話する",
                "5分でそこに着く",
                "搭乗便の時間が近い",
                "あなたの飛行機がもうすぐ到着する",
            ],
            "answer": 2,
            "choiceAnalysis": [
                "明日また電話する。今、空港へ迎えに向かう流れと合わない",
                "5分で着く。stay right thereとI'll wait for youに呼応する→正解。💡",
                "搭乗便の時間が近い。Rachelはすでに到着エリアにいる",
                "飛行機が到着する。Rachel自身はすでに空港にいる",
            ],
            "grammar": "💡 I'll be there in five minutes＝5分でそこに着きます。stay right there＝その場所で待っていて。pick ～ up＝～を迎えに行く。",
        },
    ],
}

with open(DATA_PATH, encoding="utf-8") as f:
    data = json.load(f)

if not data.get("sections"):
    raise SystemExit("section1 not found — run gen_pre2_2026-1_section1.py first")

data["sections"] = [data["sections"][0], section2]

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Wrote section2 ({len(section2['questions'])} questions) to {DATA_PATH}")

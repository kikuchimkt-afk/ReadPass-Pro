# -*- coding: utf-8 -*-
"""
2026年度 第1回（土曜準会場）英検5級 data.json
lessonPlan（focusPoints × 3）— 大問1〜3の要点をテーマ別にリッチ化
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade5", "2026-1-sat", "data.json",
)

fp1 = {
    "id": "fp1",
    "title": "空所の前後を読んで「セット」で選ぶ",
    "subtitle": "Context Clues & Set Phrases",
    "explanation": (
        "大問1では、空所の直前・直後の英語が最大のヒントです。"
        "great → I think so, too.（同意の決まり文句）、"
        "works at the hospital → doctor（職業は文脈で決まる）、"
        "play ～ → basketball（play のあとはスポーツ名）、"
        "come ～ my house → to（come to で「〜に来る」）、"
        "a ～ of apple juice → glass（a glass of で「1杯」）、"
        "$5 と答える → How much is it?（値段の質問）、"
        "new student → is from France（出身は be from）。"
        "Me, too. や Be quiet!、Whose phone もセットで覚えると速いです。"
    ),
    "explanationSimple": (
        "まえうしろのことばをよんでね！"
        "think so, too＝「わたしもそうおもう」、play basketball＝「バスケをする」、"
        "come to＝「〜にくる」、a glass of＝「1ぱい」、"
        "How much＝「いくら」、is from＝「〜しゅっしん」だよ！"
    ),
    "sourceQuote": (
        "I think so, too / play basketball / come to my house / "
        "a glass of apple juice / How much is it / is from France / Be quiet / Whose phone"
    ),
    "sourceLocation": "大問1 (1)〜(15)",
    "examples": [
        {
            "en": "A: This baseball game is great.\nB: I think so, too.",
            "ja": "A: この野球の試合、すばらしいね。\nB: 私もそう思う。",
            "note": "think so, too＝意見に同意する決まり文句。Q1の核心。",
            "noteSimple": "「すばらしいね」→「わたしも！」は I think so, too. だよ。",
        },
        {
            "en": "A: Can you come to my house at three this afternoon?\nB: Sorry, I can't.",
            "ja": "A: 今日の午後3時に、うちに来られる？\nB: ごめん、行けないんだ。",
            "note": "come to ～＝「〜に来る」。to が方向を示す。Q8。",
            "noteSimple": "come to my house は「いえにくる」。to をおぼえよう！",
        },
        {
            "en": "A: That doll is very nice. How much is it?\nB: It's only $5.",
            "ja": "A: あの人形、とてもきれいね。いくら？\nB: たった5ドルだよ。",
            "note": "How much is it?＝値段を聞く。$5 という答えがヒント。Q11。",
            "noteSimple": "How much は「いくら？」。お金のこたえがくるよ。",
        },
    ],
    "practicePassage": {
        "en": (
            "[出典: 大問1]\n"
            "A: This baseball game is great.\n"
            "B: I think so, too.\n\n"
            "Dan's mother is a doctor. She works at the hospital from Monday to Friday.\n\n"
            "A: What do you do after school, Cindy?\n"
            "B: I play basketball.\n\n"
            "Kengo usually watches the news on TV after dinner, but tonight he is watching a different TV show.\n\n"
            "A: Can you come to my house at three this afternoon?\n\n"
            "A: Can I have a glass of apple juice, Mom?\n\n"
            "A: How much is it?\n"
            "B: It's only $5.\n\n"
            "Jenny is a new student. She is from France.\n\n"
            "A: I like this movie.\n"
            "B: Me, too.\n\n"
            "A: Alice, be quiet!\n\n"
            "A: Whose phone is this?\n"
            "B: It's Bill's."
        ),
        "ja": (
            "野球の試合がすばらしい→私もそう思う。\n\n"
            "ダンの母は医者。病院で働く。\n\n"
            "放課後はバスケをする。\n\n"
            "今夜は違うテレビ番組を見ている。\n\n"
            "午後3時にうちに来られる？\n\n"
            "リンゴジュースを1杯ちょうだい。\n\n"
            "いくら？→5ドル。\n\n"
            "ジェニーはフランス出身の新入生。\n\n"
            "映画好き→私も。\n\n"
            "静かにしなさい！\n\n"
            "誰の電話？→ビルの。"
        ),
        "source": "大問1 (1)(2)(6)(7)(8)(10)(11)(12)(13)(14)(15)",
        "audioFile": "audio/practice_pp1.mp3",
    },
    "highlightPatterns": [
        "think so, too",
        "works at the hospital",
        "play basketball",
        "different TV show",
        "come to my house",
        "a glass of apple juice",
        "How much is it",
        "is from France",
        "Me, too",
        "be quiet",
        "Whose phone",
    ],
    "highlightColor": "#4f8cff",
    "highlightLabel": "文脈＋セット表現",
    "practiceQuestions": [
        {
            "q": "Q6で play bike が不正解なのはなぜ？正しい言い方は？",
            "a": "「自転車に乗る」は play ではなく ride a bike。play のあとに来るのはスポーツ・ゲーム名（basketball など）。",
        },
        {
            "q": "Q12で in France が合わない理由は？",
            "a": "「フランス出身」は be from France。in France は「フランスにいる（今そこにいる）」の意味で、出身とは違う。",
        },
        {
            "q": "Q14で be が正解になるのは、文全体がどんな文だから？",
            "a": "Be quiet! は命令文。命令文は動詞の原形 be で始まる。am / is / are は使わない。",
        },
    ],
    "practiceQuestionsSimple": [
        {"q": "I think so, too. って？", "a": "「わたしもそうおもう」だよ。"},
        {"q": "a glass of apple juice って？", "a": "「りんごジュースを1ぱい」だよ。"},
        {"q": "大問1のコツは？", "a": "まえうしろをよんで、セットのことばをさがすこと！"},
    ],
}

fp2 = {
    "id": "fp2",
    "title": "会話は「場面」と「次のセリフ」で選ぶ",
    "subtitle": "Dialogue Situations & Flow",
    "explanation": (
        "大問2は、会話の場面と次に続くセリフで空所を決めます。"
        "【職業】What do you do? → I'm a ～（職業名）。At school. や For seven years. は職業の答えにならない。"
        "【プレゼント】They're beautiful. から逆算して These flowers are for you."
        "【注文】What do you want for lunch? → A sandwich, please."
        "【訂正】Is your test today? → No, it's tomorrow.（today と tomorrow の対比）"
        "【あいさつ】Good, thanks. の前は How are you doing? がセット。"
        "場面の型を知ると、選択肢を1つずつ日本語に訳して試す手間が減ります。"
    ),
    "explanationSimple": (
        "かいわはばめんをかんがえよう！"
        "しごとをきかれたら I'm a ～、"
        "「きれいね」のまえは花をあげるセリフ、"
        "ひるごはんは sandwich, please、"
        "No, のあとは it's tomorrow、"
        "Good, thanks. のまえは How are you doing? だよ！"
    ),
    "sourceQuote": (
        "What do you do / These flowers are for you / A sandwich, please / "
        "it's tomorrow / How are you doing"
    ),
    "sourceLocation": "大問2 (16)〜(20)",
    "examples": [
        {
            "en": "Woman: I'm a nurse. What do you do?\nMan: I'm a cook.",
            "ja": "女性：私は看護師です。あなたのお仕事は？\n男性：料理人です。",
            "note": "What do you do? には I'm a ～ で職業を答える。Q16。",
            "noteSimple": "「しごとは？」→「りょうりにんです」だよ。",
        },
        {
            "en": "Boy: Happy birthday, Linda. These flowers are for you.\nGirl: Oh, thank you, Mike. They're beautiful.",
            "ja": "男の子：お誕生日おめでとう、リンダ。この花をあげるよ。\n女の子：ありがとう、マイク。とてもきれいね。",
            "note": "beautiful は花への返事。渡す言葉は These flowers are for you. Q17。",
            "noteSimple": "「きれいね」のまえは花をあげるセリフだよ！",
        },
        {
            "en": "Man 1: Hi, Bill. How are you doing?\nMan 2: Good, thanks.",
            "ja": "男性1：やあ、ビル。調子はどう？\n男性2：元気だよ、ありがとう。",
            "note": "How are you doing? ↔ Good, thanks. のあいさつセット。Q20。",
            "noteSimple": "How are you doing? に Good, thanks. がくるよ！",
        },
    ],
    "practicePassage": {
        "en": (
            "[出典: 大問2]\n"
            "Woman: I'm a nurse. What do you do?\n"
            "Man: I'm a cook.\n\n"
            "Boy: Happy birthday, Linda. These flowers are for you.\n"
            "Girl: Oh, thank you, Mike. They're beautiful.\n\n"
            "Mother: What do you want for lunch, Tom?\n"
            "Boy: A sandwich, please.\n\n"
            "Mother: Is your history test today, John?\n"
            "Boy: No, it's tomorrow.\n\n"
            "Man 1: Hi, Bill. How are you doing?\n"
            "Man 2: Good, thanks."
        ),
        "ja": (
            "看護師です。あなたの仕事は？→料理人です。\n\n"
            "誕生日おめでとう。花をあげる→きれいね、ありがとう。\n\n"
            "昼ごはんは何がいい？→サンドイッチください。\n\n"
            "テストは今日？→いいえ、明日です。\n\n"
            "調子はどう？→元気だよ、ありがとう。"
        ),
        "source": "大問2 (16)〜(20)",
        "audioFile": "audio/practice_pp2.mp3",
    },
    "highlightPatterns": [
        "What do you do",
        "I'm a cook",
        "These flowers are for you",
        "They're beautiful",
        "A sandwich, please",
        "it's tomorrow",
        "How are you doing",
        "Good, thanks",
    ],
    "highlightColor": "#34d399",
    "highlightLabel": "会話の場面",
    "practiceQuestions": [
        {
            "q": "Q16で At school. が合わない理由は？",
            "a": "What do you do? は職業を聞く質問。場所だけでは「何の仕事をしているか」に答えていない。",
        },
        {
            "q": "Q19で it's cloudy today. が合わない理由は？",
            "a": "母はテストの日を聞いている。No, のあとに来るのは日付の訂正（it's tomorrow）であって、天気ではない。",
        },
        {
            "q": "Q18で At twelve o'clock. が合わない理由は？",
            "a": "What do you want for lunch? は「何を食べたいか」を聞いている。12時は時間の答えで、食べ物の注文にならない。",
        },
    ],
    "practiceQuestionsSimple": [
        {"q": "What do you do? って？", "a": "「しごとはなに？」ときくよ。"},
        {"q": "A sandwich, please. って？", "a": "「サンドイッチください」だよ。"},
        {"q": "会話問題のコツは？", "a": "つぎのセリフをよんで、ばめんをかんがえること！"},
    ],
}

fp3 = {
    "id": "fp3",
    "title": "並べ替え——5つの「型」を先に思い出す",
    "subtitle": "Sentence Order Patterns (4 words)",
    "explanation": (
        "大問3は、日本文の意味から英文の型を思い出し、①〜④を並べる問題です。"
        "5級は4語・空所は1番目と3番目を選ぶ形式。"
        "① My sister washes the dishes.（主語＋三人称単数 washes）"
        "② Bill and I go skiing.（and で主語をつなぐ＋go skiing）"
        "③ Take your umbrella to school.（命令文 take ～ to ～）"
        "④ Mike's soccer team has three coaches.（三単現 has）"
        "⑤ We don't have school today.（否定 don't have）"
        "並べ終えたら、1番目と3番目の語が選択肢と一致するか最終確認します。"
    ),
    "explanationSimple": (
        "ならべかえは「かた」をおぼえよう！"
        "my sister washes＝おねえちゃんがあらう、"
        "Bill and I go skiing＝ビルといっしょにスキー、"
        "Take ... to school＝がっこうにもっていけ、"
        "has three coaches＝コーチが3にん、"
        "We don't have school＝きょうはがっこうがない、だよ。"
    ),
    "sourceQuote": (
        "My sister washes the dishes / Bill and I go skiing / "
        "Take your umbrella to school / has three coaches / We don't have school today"
    ),
    "sourceLocation": "大問3 (21)〜(25)",
    "examples": [
        {
            "en": "My sister washes the dishes every day.",
            "ja": "私の姉は毎日お皿を洗います。",
            "note": "主語 my sister のあとに washes（三人称単数）。Q21。",
            "noteSimple": "my sister washes で「おねえちゃんがあらう」だよ。",
        },
        {
            "en": "Take your umbrella to school.",
            "ja": "学校にかさを持って行きなさい。",
            "note": "命令文は動詞 take で始まる。take ～ to ～ の形。Q23。",
            "noteSimple": "Take ... to school. は「がっこうにもっていきなさい」！",
        },
        {
            "en": "We don't have school today.",
            "ja": "今日は学校がありません。",
            "note": "we ＋ don't have school。have school＝授業がある。Q25。",
            "noteSimple": "We don't have school は「きょうはがっこうがない」だよ。",
        },
    ],
    "practicePassage": {
        "en": (
            "[出典: 大問3]\n"
            "My sister washes the dishes every day.\n\n"
            "Bill and I go skiing in winter.\n\n"
            "Take your umbrella to school.\n\n"
            "Mike's soccer team has three coaches.\n\n"
            "We don't have school today."
        ),
        "ja": (
            "私の姉は毎日お皿を洗います。\n\n"
            "ビルと私は冬にスキーに行きます。\n\n"
            "学校にかさを持って行きなさい。\n\n"
            "マイクのサッカーチームには3人のコーチがいます。\n\n"
            "今日は学校がありません。"
        ),
        "source": "大問3 (21)〜(25)",
        "audioFile": "audio/practice_pp3.mp3",
    },
    "highlightPatterns": [
        "My sister washes",
        "the dishes every day",
        "Bill and I go skiing",
        "Take your umbrella to school",
        "soccer team has three coaches",
        "We don't have school today",
    ],
    "highlightColor": "#a78bfa",
    "highlightLabel": "並べ替えの型",
    "practiceQuestions": [
        {
            "q": "Q21で ②─③ が正解になる完成文は？1・3番目の語は？",
            "a": "My sister washes the dishes every day. 1番目 my（②）、3番目 washes（③）。",
        },
        {
            "q": "Q24で has が必要な理由は？主語は何？",
            "a": "Mike's soccer team が主語。チームは1つなので動詞は has（三単現）。have ではない。",
        },
        {
            "q": "Q22で Bill のあとに来るのはなぜ and ？",
            "a": "「ビルと私」＝Bill and I。and で2人をつなぎ、go skiing が動詞句になる。",
        },
    ],
    "practiceQuestionsSimple": [
        {"q": "my sister washes って？", "a": "「おねえちゃんがあらう」だよ。"},
        {"q": "Take ... to school. って？", "a": "「がっこうにもっていきなさい」だよ。"},
        {"q": "並べ替えのさいごのチェックは？", "a": "1ばんめと3ばんめが選択肢とあうかな？"},
    ],
}

with open(DATA_PATH, encoding="utf-8") as f:
    data = json.load(f)

new_fps = [fp1, fp2, fp3]
old_fps = {fp.get("id"): fp for fp in data.get("lessonPlan", {}).get("focusPoints", [])}
for fp in new_fps:
    old = old_fps.get(fp["id"], {})
    if old.get("sourceQuoteAudio"):
        fp["sourceQuoteAudio"] = old["sourceQuoteAudio"]
    pp = fp.get("practicePassage", {})
    if old.get("practicePassage", {}).get("audioFile"):
        pp["audioFile"] = old["practicePassage"]["audioFile"]
    for i, ex in enumerate(fp.get("examples", [])):
        oex = old.get("examples", [])
        if i < len(oex) and oex[i].get("audio"):
            ex["audio"] = oex[i]["audio"]

data["lessonPlan"] = {
    "title": "英検5級 2026年度 第1回（土曜準会場）",
    "focusPoints": new_fps,
}

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Wrote lessonPlan ({len(data['lessonPlan']['focusPoints'])} focusPoints) to {DATA_PATH}")

# -*- coding: utf-8 -*-
"""
2026年度 第1回（土曜準会場）英検3級 data.json
lessonPlan（focusPoints × 4）— 大問1〜3の要点をテーマ別にリッチ化
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade3", "2026-1-sat", "data.json",
)

fp1 = {
    "id": "fp1",
    "title": "句動詞・前置詞の「セット」で覚える",
    "subtitle": "Phrasal Verbs & Preposition Collocations",
    "explanation": (
        "大問1では単語単体ではなく、決まった組み合わせ（コロケーション）で覚えると正解率が上がります。"
        "take care of（〜の世話をする）、wait for 30 minutes（〜を30分待つ）、look around downtown（あちこち見て回る）は、"
        "空所の前後の語とセットで意味が決まります。by himself（一人で）のように、代名詞＋前置詞の形も頻出です。"
        "to practice basketball のように、目的を表す to 不定詞も大問1 Q15 の決め手になります。"
    ),
    "explanationSimple": (
        "たんごひとつじゃなく、セットでおぼえるといいよ。"
        "take care of は「せわをする」、wait for は「まつ」、look around は「あちこちみる」。"
        "by himself は「ひとりで」。to practice は「れんしゅうするために」だよ。"
    ),
    "sourceQuote": "I always take care of my little sister / We'll have to wait for 30 minutes / They looked around downtown",
    "sourceLocation": "大問1 (8)(10)(12)",
    "examples": [
        {
            "en": "I always take care of my little sister when my mother is out.",
            "ja": "母が外出しているとき、私はいつも妹の世話をしている。",
            "note": "take care of ～＝「～の世話をする」。make/give/pick care of は使わない。",
            "noteSimple": "take care of は「せわをする」。make や give じゃだめだよ。",
        },
        {
            "en": "We'll have to wait for 30 minutes until the next train comes.",
            "ja": "次の電車が来るまで30分待たなければならない。",
            "note": "wait for ～＝「～を待つ」。for の後ろに時間や人が来る。",
            "noteSimple": "wait for は「〜をまつ」。for をわすれないで！",
        },
        {
            "en": "They looked around downtown, but everything was too small.",
            "ja": "彼らはダウンタウンをあちこち見て回ったが、どれも小さすぎた。",
            "note": "look around＝「あちこち見て回る」。look out（気をつける）と混同しない。",
            "noteSimple": "look around は「あちこちみる」。look out は「きをつける」でちがうよ。",
        },
    ],
    "practicePassage": {
        "en": (
            "A: Can you pass me the ball, please? — Here you are.\n\n"
            "No, he did it all by himself.\n\n"
            "I always take care of my little sister when my mother is out.\n\n"
            "We'll have to wait for 30 minutes until the next one comes.\n\n"
            "They looked around downtown, but everything was too small.\n\n"
            "I'm going to the park to practice basketball."
        ),
        "ja": (
            "A: ボールを渡してもらえますか？ — はい、どうぞ。\n\n"
            "いいえ、彼は全部一人でやったよ。\n\n"
            "母が外出しているとき、私はいつも妹の世話をしている。\n\n"
            "次の電車が来るまで30分待たなければならない。\n\n"
            "彼らはダウンタウンをあちこち見て回ったが、どれも小さすぎた。\n\n"
            "公園にバスケットボールの練習をしに行くところだよ。"
        ),
        "source": "大問1 (2)(9)(8)(10)(12)(15)",
        "audioFile": "audio/practice_pp1.mp3",
    },
    "highlightPatterns": [
        "pass me the ball",
        "by himself",
        "take care of",
        "wait for",
        "looked around",
        "to practice basketball",
    ],
    "practiceQuestions": [
        {
            "q": "Q8で take が正解になる理由を、空所の直後から説明してください。",
            "a": "直後が care of my little sister。take care of が「世話をする」の定型句。make/give/pick ではこの句は成立しない。",
        },
        {
            "q": "Q10の wait ( ) 30 minutes で for が必要な理由は？",
            "a": "wait for ～＝「～を待つ」。30 minutes は待つ対象・期間を示すので for が入る。wait at/into/from では「待つ」の意味にならない。",
        },
        {
            "q": "Q15の to practice と practiced の違いは？",
            "a": "going to the park to practice＝「練習するために公園へ行く」（目的の不定詞）。practiced は過去形で文法的に合わない。",
        },
    ],
    "practiceQuestionsSimple": [
        {
            "q": "take care of ってどういう意味？",
            "a": "「せわをする」。いもうとのせわをする、というセットだよ。",
        },
        {
            "q": "wait for ってどういう意味？",
            "a": "「〜をまつ」。30ぷんまつ、は wait for 30 minutes だよ。",
        },
        {
            "q": "to practice ってどういう意味？",
            "a": "「れんしゅうするために」。公園に行く目的を言ってるよ。",
        },
    ],
}

fp2 = {
    "id": "fp2",
    "title": "会話の「前後のつながり」で選ぶ",
    "subtitle": "Dialogue Flow: Request → Response",
    "explanation": (
        "大問2は会話の流れを読む問題です。空所の直前・直後の発言が最大のヒントになります。"
        "「すぐ手伝うよ」＋「テレビが10分で終わる」→ I'll help you soon。"
        "誕生日の話のあと「アイススケートに行きたい」と答える → What would you like to do?。"
        "「練習があるから会えない」→ Say hello to him for me と母の OK, I will. がセットになります。"
        "選択肢を日本語に訳してから、会話の自然さで消去法するのが効果的です。"
    ),
    "explanationSimple": (
        "かいわはまえとうしろをよんでね。"
        "「10ぷんでテレビがおわる」→「すぐてつだうよ」。"
        "「たんじょうび」→「なにをしたい？」。"
        "「れんしゅうがある」→「ぼくのかわりにあいさつして」。"
    ),
    "sourceQuote": "I'll help you soon. This TV show will finish in 10 minutes.",
    "sourceLocation": "大問2 (16)",
    "examples": [
        {
            "en": "Sister: Could you show me how to use your computer?\nBrother: I'll help you soon. This TV show will finish in 10 minutes.",
            "ja": "姉：パソコンの使い方を教えて。\n兄：すぐ手伝うよ。このテレビはあと10分で終わる。",
            "note": "依頼への返答＋理由。soon と 10 minutes が呼応。",
            "noteSimple": "「すぐてつだう」＋「10ぷんでおわる」がセットだよ。",
        },
        {
            "en": "Father: Your birthday is next Saturday. What would you like to do?\nSon: I want to go ice-skating with my friends.",
            "ja": "父：来週土曜は誕生日だね。何をしたい？\n息子：友達とアイススケートに行きたい。",
            "note": "What would you like to do? → 活動の内容で答えるパターン。",
            "noteSimple": "「なにをしたい？」→「アイススケートに行きたい」！",
        },
        {
            "en": "Son: Sorry, Mom. I have baseball practice then. Say hello to him for me.\nMother: OK, I will.",
            "ja": "息子：ごめん、練習があるんだ。僕の代わりにあいさつして。\n母：わかった、するわね。",
            "note": "Say hello to ～ for me と OK, I will. が対になっている。",
            "noteSimple": "「かわりにあいさつして」→ママが「わかった」って言うよ。",
        },
    ],
    "practicePassage": {
        "en": (
            "Sister: Jim, could you show me how to use your computer?\n"
            "Brother: I'll help you soon. This TV show will finish in 10 minutes.\n\n"
            "Father: Your birthday is next Saturday. What would you like to do?\n"
            "Son: I want to go ice-skating with my friends.\n\n"
            "Mother: Why is your baseball cap on the sofa?\n"
            "Son: I'm going to wear it today. I have practice at three.\n\n"
            "Student: I can't go to baseball practice today. I have a stomachache.\n"
            "Teacher: That's too bad. Please go home and rest.\n\n"
            "Son: Sorry, Mom. I have baseball practice then. Say hello to him for me.\n"
            "Mother: OK, I will."
        ),
        "ja": (
            "姉：パソコンの使い方を教えて。\n"
            "兄：すぐ手伝うよ。テレビはあと10分で終わる。\n\n"
            "父：来週土曜は誕生日だね。何をしたい？\n"
            "息子：友達とアイススケートに行きたい。\n\n"
            "母：どうして帽子がソファにあるの？\n"
            "息子：今日はかぶるつもり。3時に練習があるんだ。\n\n"
            "生徒：今日は練習に行けません。お腹が痛いんです。\n"
            "先生：残念だね。家に帰って休みなさい。\n\n"
            "息子：ごめん、練習があるんだ。僕の代わりにあいさつして。\n"
            "母：わかった、するわね。"
        ),
        "source": "大問2 (16)〜(20)",
        "audioFile": "audio/practice_pp2.mp3",
    },
    "highlightPatterns": [
        "I'll help you soon",
        "What would you like to do",
        "I'm going to wear it today",
        "I have a stomachache",
        "Say hello to him for me",
        "OK, I will",
    ],
    "practiceQuestions": [
        {
            "q": "Q16で「It's too easy for you」が不適切な理由は？",
            "a": "妹はパソコンの使い方を教えてほしいと依頼している。兄はテレビが終わったら手伝うと言う流れが自然で、相手を見下す表現は文脈に合わない。",
        },
        {
            "q": "Q19で先生の Please go home and rest が示すヒントは？",
            "a": "休むよう言われる＝体調不良の理由が必要。I have a stomachache（腹痛）が最も自然。新しいバットや勝てると思うは理由にならない。",
        },
        {
            "q": "Q20で Have a nice trip が合わない理由は？",
            "a": "おじさんは「訪ねてくる」予定。旅に出かける人へのあいさつではない。代わりにあいさつを頼む Say hello to him for me が正解。",
        },
    ],
    "practiceQuestionsSimple": [
        {
            "q": "I'll help you soon はいつ使う？",
            "a": "「すぐてつだうよ」。ちょっとまってて、あとでてつだうね、というとき。",
        },
        {
            "q": "Say hello to him for me ってどういう意味？",
            "a": "「ぼくのかわりにあいさつして」。自分は会えないときに使うよ。",
        },
        {
            "q": "会話問題のコツは？",
            "a": "つぎのセリフをよんで、自然なやりとりかな？と考えること！",
        },
    ],
}

fp3 = {
    "id": "fp3",
    "title": "お知らせとメール——「何のための情報か」を見分ける",
    "subtitle": "Notice vs Email: Purpose of Information",
    "explanation": (
        "大問3Aのお知らせでは、同じ連絡先でも「目的」によって使い分けが書かれています。"
        "参加申し込み＝メールまたは電話、野菜の詳しい情報＝ウェブサイト、と読み分けることが Q22 の鍵です。"
        "大問3Bのメールでは、誰が・いつ・どこで・どうやって、を整理すると Q23〜25 が解けます。"
        "practiced at home（家で練習）、take the bus（バスで行く）、My mom and brother are coming（弟も来る）など、"
        "主語と動作をメモしながら読むと、似た選択肢を避けられます。"
    ),
    "explanationSimple": (
        "お知らせは「なんのためのじょうほうか」をわけるよ。"
        "さんか＝メール・電話、やさいのじょうほう＝ウェブサイト。"
        "メールはだれが・いつ・どうやって、をメモしながらよむといいよ。"
    ),
    "sourceQuote": "To join the cooking class, please send an email / For more information about our vegetables, please check our website.",
    "sourceLocation": "大問3A / 大問3B",
    "examples": [
        {
            "en": "To join the cooking class, please send an email or call us at 555-5555-5555.",
            "ja": "料理教室に参加するには、メールを送るか電話してください。",
            "note": "join the cooking class＝参加申し込みの連絡先。",
            "noteSimple": "教室にさんかするためのメールやでんわだよ。",
        },
        {
            "en": "For more information about our vegetables, please check our website.",
            "ja": "野菜についての詳しい情報は、ウェブサイトをご覧ください。",
            "note": "vegetables の情報＝website。メール・電話とは目的が違う。",
            "noteSimple": "やさいのじょうほうはウェブサイトを見てね。",
        },
        {
            "en": "I practiced at home every day for an hour, too. We will take the bus to the theater.",
            "ja": "家でも毎日1時間練習した。劇場にはバスで行く予定だ。",
            "note": "at home＝家での行動。take the bus＝劇場への交通手段（帰りは母の車）。",
            "noteSimple": "いえでれんしゅうした。劇場にはバスで行くよ。",
        },
    ],
    "practicePassage": {
        "en": (
            "There will be a fun and free cooking class at Sunny Brook Farm.\n"
            "You do not have to bring anything with you. We will prepare all of the ingredients.\n"
            "To join the cooking class, please send an email or call us.\n"
            "For more information about our vegetables, please check our website.\n\n"
            "I practiced at home every day for an hour, too. I practiced with my dad.\n"
            "The performance will be on Friday at 5 p.m. at the local theater.\n"
            "My mom and brother are coming, too.\n"
            "We will take the bus to the theater, and our mom will drive us home."
        ),
        "ja": (
            "サニーブルック農場で楽しい無料の料理教室があります。\n"
            "持ち物は不要。材料はすべて用意します。\n"
            "参加申し込みはメールまたは電話で。\n"
            "野菜の詳しい情報はウェブサイトをご覧ください。\n\n"
            "家でも毎日1時間練習した。お父さんと一緒に。\n"
            "公演は金曜午後5時、地元の劇場です。\n"
            "お母さんと弟も来ます。\n"
            "劇場にはバスで行き、帰りはお母さんが車で送ってくれます。"
        ),
        "source": "大問3A「Free Cooking Class」/ 大問3B「Drama club performance」",
        "audioFile": "audio/practice_pp3.mp3",
    },
    "highlightPatterns": [
        "send an email",
        "check our website",
        "practiced at home",
        "take the bus",
        "My mom and brother are coming",
        "drive us home",
    ],
    "practiceQuestions": [
        {
            "q": "Q22でメールや電話が不正解になる理由を説明してください。",
            "a": "メール・電話は To join the cooking class（参加申し込み）用。野菜の情報は For more information about our vegetables, please check our website と別目的で書かれている。",
        },
        {
            "q": "Q24で Mia's mother が不正解な理由は？",
            "a": "母は帰りに drive us home（車で送る）と書かれている。公演に「行く」と明記されているのは Emma's brother（My mom and brother are coming）。",
        },
        {
            "q": "Q25で Her mother will drive her が不正解な理由は？",
            "a": "劇場へ行く手段は take the bus。母の車は帰り（drive us home）の話。行きと帰りを混同しない。",
        },
    ],
    "practiceQuestionsSimple": [
        {
            "q": "野菜のじょうほうはどこで見る？",
            "a": "ウェブサイト！メールは教室にさんかするためだよ。",
        },
        {
            "q": "エマはいえでなにをした？",
            "a": "劇のれんしゅうをしたよ。1じかん、お父さんといっしょに。",
        },
        {
            "q": "ミアは劇場にどうやっていく？",
            "a": "バスで行くよ。お母さんの車はかえりだよ。",
        },
    ],
}

fp4 = {
    "id": "fp4",
    "title": "長文読解——キーワードと時系列で答えを選ぶ",
    "subtitle": "Reading Strategy: Keywords & Timeline",
    "explanation": (
        "大問3C「Table Tennis」は、時代順に卓球の歴史が述べられます。"
        "1880年代＝天気が悪いときに indoors で活動、1926年＝選手が England に行って選手権、"
        "人気の理由＝easy to start playing、1971年＝中国選手が drawing を贈った、と年代・因果を整理すると速いです。"
        "問題文の主語に注意：missed his bus はアメリカ選手、 gave a drawing は中国選手（Q29）。"
        "What is this story about? は冒頭から最後まで通じるテーマ（スポーツの歴史）を選びます。"
    ),
    "explanationSimple": (
        "長文はじかんじゅんにおぼえるといいよ。"
        "1880年代＝おくのなかでうんどう、1926年＝イングランドでしあい、"
        "にんきのわけ＝はじめやすい、1971年＝えをあげた。"
        "だれがなにをしたか、だれのはなしかよくみてね。"
    ),
    "sourceQuote": "when the weather was bad because it was a fun way to stay active indoors / went to England and played in the table tennis championships",
    "sourceLocation": "大問3C「Table Tennis」",
    "examples": [
        {
            "en": "In the 1880s, people played table tennis when the weather was bad because it was a fun way to stay active indoors.",
            "ja": "1880年代、天気が悪いときに屋内で活動的に過ごす楽しい方法として卓球をした。",
            "note": "stay active indoors＝屋内で体を動かす。Q26の根拠。",
            "noteSimple": "天気がわるいとき、おくのなかでうんどうしたんだよ。",
        },
        {
            "en": "Players from different countries went to England and played in the table tennis championships.",
            "ja": "さまざまな国の選手がイングランドに行き、卓球選手権で競った。",
            "note": "went to England＝開催地はイングランド。Q27の根拠。",
            "noteSimple": "選手がイングランドに行った＝そこで開かれたよ。",
        },
        {
            "en": "A Chinese athlete on the bus gave him a drawing of the mountains in his country.",
            "ja": "バスの中の中国の選手が、彼に自分の国の山の絵を贈った。",
            "note": "中国選手＝gave a drawing。アメリカ選手＝missed his bus（Q29の主語注意）。",
            "noteSimple": "中国の選手がえをあげた。バスにのりおくれたのはアメリカの選手だよ。",
        },
    ],
    "practicePassage": {
        "en": (
            "Table tennis is a sport that started in England. In the 1880s, people played table tennis when the weather was bad because it was a fun way to stay active indoors.\n\n"
            "In 1926, the first world championships for table tennis were held. Players from different countries went to England and played in the championships.\n\n"
            "Table tennis became popular in many countries because it was easy to start playing. It did not cost a lot of money because it could be played with cheap items.\n\n"
            "In 1971, an American athlete missed his bus and got on the Chinese team's bus instead. A Chinese athlete gave him a drawing of the mountains in his country."
        ),
        "ja": (
            "卓球はイングランドで始まったスポーツ。1880年代、天気が悪いときに屋内で活動的に過ごす方法として人々は卓球をした。\n\n"
            "1926年、初の世界選手権が開催された。各国の選手がイングランドに行き、選手権で競った。\n\n"
            "始めるのが簡単だったため、多くの国で人気になった。安い道具でできたのであまりお金がかからなかった。\n\n"
            "1971年、アメリカの選手がバスに乗り遅れ、中国チームのバスに乗った。中国の選手が山の絵を贈った。"
        ),
        "source": "大問3C「Table Tennis」",
        "audioFile": "audio/practice_pp4.mp3",
    },
    "highlightPatterns": [
        "stay active indoors",
        "went to England",
        "easy to start playing",
        "cheap items",
        "gave him a drawing",
        "missed his bus",
    ],
    "practiceQuestions": [
        {
            "q": "Q26で「外の良い天気を楽しみたかった」が不正解な理由は？",
            "a": "本文は when the weather was bad（天気が悪いとき）と書かれている。indoors（屋内）で活動するのが理由。",
        },
        {
            "q": "Q27で Germany / Hungary / India が不正解な理由は？",
            "a": "これらは参加国。went to England and played in the championships から、開催地はイングランド。",
        },
        {
            "q": "Q29で He missed his bus が不正解な理由は？",
            "a": "質問は a Chinese athlete did what?（中国選手は何をした？）。missed his bus は American athlete の行動。正解は gave an athlete a drawing。",
        },
    ],
    "practiceQuestionsSimple": [
        {
            "q": "1880年代になぜ卓球をした？",
            "a": "天気がわるくて、おくのなかでうんどうするためだよ。",
        },
        {
            "q": "はじめの世界選手権はどこで？",
            "a": "イングランド！いろいろな国の選手がイングランドに行ったよ。",
        },
        {
            "q": "1971年、中国の選手はなにをした？",
            "a": "アメリカの選手に山のえをあげたよ。",
        },
    ],
}

with open(DATA_PATH, encoding="utf-8") as f:
    data = json.load(f)

data["lessonPlan"] = {"focusPoints": [fp1, fp2, fp3, fp4]}

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Wrote lessonPlan ({len(data['lessonPlan']['focusPoints'])} focusPoints) to {DATA_PATH}")

# -*- coding: utf-8 -*-
"""
2026年度 第1回（本会場）英検準2級 data.json
Step E: lessonPlan（focusPoints × 5）
本文中に実在する構文のみ。practicePassage は試験本文の抜粋＋[出典: タイトル]。
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade-pre2", "2026-1", "data.json",
)

fp1 = {
    "id": "fp1",
    "title": "語彙・熟語の空所判断（absolutely / except for / make up my mind）",
    "subtitle": "Vocabulary & Idiom Fill-in: Context Clues",
    "explanation": (
        "大問1では、空所の直後・前後の文が最大の手がかりです。"
        "absolutely は形容詞 delicious を強調し、the best pasta that I've ever eaten と呼応します。"
        "except for は Almost all（ほとんどすべて）のあとに例外を示し、still waiting for a family とセットで頻出します。"
        "out of the question は断りの定型で、just got a new one last month など「理由」と対になります。"
        "make up my mind は decide ～? への No. I can't ～ の問答ペアとして覚えると会話空所にも応用できます。"
    ),
    "sourceQuote": "absolutely delicious / except for one dog / out of the question / make up my mind / trust their friends",
    "sourceLocation": "大問1 Q1, Q11, Q13, Q14, Q8",
    "examples": [
        {
            "en": "Michael, this meal is absolutely delicious! It's the best pasta that I've ever eaten.",
            "ja": "この料理は本当においしい！今まで食べた中で最高のパスタだ。",
            "note": "absolutely＝非常に（形容詞を強調）。最高級表現とセットで褒め言葉を構成。Q1。",
        },
        {
            "en": "Almost all the pets in the shelter found homes, except for one dog that was still waiting for a family.",
            "ja": "保護施設のペットはほとんどすべて家を見つけたが、まだ家族を待つ1匹を除いて。",
            "note": "Almost all ＋ except for ＝「大部分＋例外」の定型。Q11。",
        },
        {
            "en": "No. I can't make up my mind. They all seem so interesting.",
            "ja": "いいえ、決められない。どれもとてもおもしろそうなんだ。",
            "note": "make up one's mind＝決心する。Have you decided ～? への返答。Q14。",
        },
    ],
    "practicePassage": {
        "en": (
            "[出典: 大問1 語彙]\n"
            "A: Michael, this meal is absolutely delicious! It's the best pasta that I've ever eaten.\n"
            "Almost all the pets in the shelter found homes, except for one dog that was still waiting for a family.\n"
            "A: Dad, can I have a new smartphone for my birthday this year?\n"
            "B: No, that's out of the question, Megan. Your birthday is next month, and you just got a new one last month.\n"
            "A: Have you decided which club to join, Chris?\n"
            "B: No. I can't make up my mind. They all seem so interesting.\n"
            "People can trust their friends to support them during difficult times and help them find solutions."
        ),
        "ja": (
            "この料理は本当においしい！今までで最高のパスタだ。\n"
            "保護施設のペットはほとんどすべて家を見つけたが、まだ家族を待つ1匹を除いて。\n"
            "今年の誕生日に新しいスマホをもらえない？\n"
            "ダメよ、それはありえない。誕生日は来月だし、先月新しいのをもらったばかりでしょ。\n"
            "どのクラブに入るか決めた？\n"
            "ううん、決められない。どれもとてもおもしろそうなんだ。\n"
            "人は困難な時期に友人を信頼して支えてもらい、解決策を見つける手助けをしてもらえる。"
        ),
        "audioFile": "audio/practice_pp1.mp3",
    },
    "practiceQuestions": [
        {
            "q": "Q1で absolutely が正解になる根拠は何ですか？",
            "a": "delicious を強調し、It's the best pasta that I've ever eaten（今までで最高）という褒め言葉と一致するから。",
        },
        {
            "q": "Q11の except for は文のどの部分とセットで覚えますか？",
            "a": "Almost all（ほとんどすべて）＋ except for one dog（1匹を除いて）＋ still waiting（まだ待っている）。",
        },
        {
            "q": "Q13の out of the question の直後に続く「断る理由」は？",
            "a": "Your birthday is next month, and you just got a new one last month（先月もらったばかり）。",
        },
        {
            "q": "trust their friends to support them の構文の意味は？",
            "a": "友人を信頼して支えてもらう（trust 人 to do）。Q8の to 不定詞が期待する行動を示す。",
        },
    ],
    "highlightPatterns": [
        "the best pasta that I've ever eaten",
        "still waiting for a family",
        "out of the question",
        "make up my mind",
        "support them during difficult times",
    ],
    "highlightColor": "#4f8cff",
    "highlightLabel": "語彙・熟語",
}

fp2 = {
    "id": "fp2",
    "title": "会話完成の流れ（same direction / volunteer / cafeteria）",
    "subtitle": "Dialogue Completion: Offer, Sign-up & Daily Routine",
    "explanation": (
        "大問2は会話全体の「申し出・驚き・代替案」の流れを読む問題です。"
        "Q16では I'm going in the same direction（同じ方向）＋ Please follow me が I can take you there を選ばせます。"
        "Q18では We have plenty to choose from のあと、which program you're interested in と具体名の返答がペアになります。"
        "Q19〜20は But you usually eat at the cafeteria（いつもの習慣）と、closed for repairs（今日からの変化）のギャップが鍵です。"
        "作る時間がないとき Can you buy something on your way → stop by my favorite bakery と続きます。"
    ),
    "sourceQuote": "going in the same direction / volunteer programs / cafeteria will be closed for repairs / buy something on your way",
    "sourceLocation": "大問2 Q16〜20",
    "examples": [
        {
            "en": "Well, I'm going in the same direction, so I can take you there. Please follow me.",
            "ja": "私も同じ方向に行くので、そこへ連れて行ってあげられる。ついてきて。",
            "note": "take 人 there＝人をそこへ連れて行く。follow me とセット。Q16。",
        },
        {
            "en": "May I ask which program you're interested in? We have plenty to choose from.",
            "ja": "どのプログラムに興味がありますか？選べるものはたくさんあります。",
            "note": "May I ask ～?＝丁寧な質問。plenty to choose from → which program。Q18。",
        },
        {
            "en": "From today, the cafeteria will be closed for repairs, and everyone must bring their own lunch.",
            "ja": "今日から学食は修理のため閉まっており、全員が自分の昼食を持参しなければならない。",
            "note": "closed for repairs＝修理のため閉鎖。bring their own lunch と因果。Q19の背景。",
        },
    ],
    "practicePassage": {
        "en": (
            "[出典: 大問2 会話完成]\n"
            "B: Well, I'm going in the same direction, so I can take you there. Please follow me.\n"
            "A: Hello. I'd like to sign up for one of the volunteer programs this summer.\n"
            "B: Of course! May I ask which program you're interested in? We have plenty to choose from.\n"
            "B: Lunch? But you usually eat at the cafeteria. Why do you need to bring your own?\n"
            "A: From today, the cafeteria will be closed for repairs, and everyone must bring their own lunch.\n"
            "B: I don't think so. Can you buy something on your way today?\n"
            "A: OK. I'll stop by my favorite bakery."
        ),
        "ja": (
            "私も同じ方向に行くので、そこへ連れて行ってあげられる。ついてきて。\n"
            "この夏のボランティアプログラムに申し込みたいのですが。\n"
            "どのプログラムに興味がありますか？選べるものはたくさんあります。\n"
            "お弁当？でも君はたいてい学食で食べるでしょ。なぜ持っていく必要があるの？\n"
            "今日から学食は修理のため閉まっていて、全員持参しなければならない。\n"
            "今作る時間はないと思う。今日は行き道で何か買ってくれる？\n"
            "わかった。お気に入りのパン屋に寄るね。"
        ),
        "audioFile": "audio/practice_pp2.mp3",
    },
    "practiceQuestions": [
        {
            "q": "Q16で「間違った道を行ける」が誤答になる理由は？",
            "a": "道を教えたうえで同じ方向に行き follow me と案内する文脈。相手を助ける申し出と矛盾する。",
        },
        {
            "q": "Q19の But you ～ は何を驚かせていますか？",
            "a": "普段は学食で食べている（usually eat at the cafeteria）のに、今日は持参が必要という突然の変化。",
        },
        {
            "q": "Q20の正解が「自分で作る」ではない理由は？",
            "a": "子どもが父に Can you ～? と頼み、父は時間がない（I don't think so）。買う代替案が bakery と続く。",
        },
        {
            "q": "on your way と stop by はどう結びつきますか？",
            "a": "行き道で（on your way）パン屋に寄る（stop by）＝通りがかりに買う流れ。",
        },
    ],
    "highlightPatterns": [
        "going in the same direction",
        "volunteer programs",
        "We have plenty to choose from",
        "cafeteria will be closed for repairs",
        "stop by my favorite bakery",
    ],
    "highlightColor": "#f472b6",
    "highlightLabel": "会話完成",
}

fp3 = {
    "id": "fp3",
    "title": "長文空所「The Advice」（embarrassed / necessary step / even better）",
    "subtitle": "Passage Fill: Overcoming Fear of Speaking",
    "explanation": (
        "大問3は2段落の物語で、姉のアドバイス（第1段落）と学校のスピーチ（第2段落）が対になっています。"
        "Q21は afraid to speak と embarrassed if his English was wrong から、間違いへの恐れを乗り越える助言を読み取ります。"
        "a necessary step to improve his skills が空所の内容を補強します。"
        "Q22は He knew that ～ のあと、very good だが how he could make it even better という「良いが完璧ではない」流れが決め手です。"
    ),
    "sourceQuote": "afraid to speak / embarrassed if his English was wrong / a necessary step to improve his skills / how he could make it even better",
    "sourceLocation": "大問3「The Advice」Q21〜22",
    "examples": [
        {
            "en": "Although he enjoyed studying English, he was always afraid to speak the language.",
            "ja": "英語を勉強するのは楽しんでいたが、話すことはいつも怖かった。",
            "note": "Although ～, ...＝～だが…。enjoyed studying と afraid to speak の対比。",
        },
        {
            "en": "He worried that he might be embarrassed if his English was wrong.",
            "ja": "英語が間違っていたら恥ずかしい思いをするかもしれないと心配した。",
            "note": "be embarrassed if ～＝～なら恥ずかしい。Q21の悩みの核心。",
        },
        {
            "en": "She even explained that it was a necessary step to improve his skills.",
            "ja": "さらに、それはスキルを上げるために必要な段階だと説明した。",
            "note": "a necessary step to ～＝～するための必要な段階。Q21の直後の手がかり。",
        },
    ],
    "practicePassage": {
        "en": (
            "[出典: The Advice]\n"
            "Although he enjoyed studying English, he was always afraid to speak the language. He worried that he might be embarrassed if his English was wrong. One day, he talked with his older sister, who spoke English very well. She even explained that it was a necessary step to improve his skills. Thanks to her, Haruto's attitude toward speaking English changed.\n"
            "When his turn came, he stood up and spoke clearly, despite feeling nervous. When he finished the whole speech, however, Ms. Sato smiled and said his speech was very good. She also explained how he could make it even better. From that day, he began to enjoy speaking English."
        ),
        "ja": (
            "英語を勉強するのは楽しんでいたが、話すことはいつも怖かった。間違っていたら恥ずかしいかもしれないと心配していた。英語が上手な姉と話し、姉はスキルを上げるための必要な段階だと説明した。姉のおかげで、話すことへの態度が変わった。\n"
            "自分の番になると緊張しながらも立ち上がり、はっきり話した。スピーチを終えると佐藤先生は微笑み、とてもよいと言った。さらにもっとよくする方法も説明した。その日から、英語を話すことを楽しみ始めた。"
        ),
        "audioFile": "audio/practice_pp3.mp3",
    },
    "practiceQuestions": [
        {
            "q": "Q21で「英語を話す必要はない」が誤答になる理由は？",
            "a": "attitude toward speaking English changed（話すことへの態度が変わった）と矛盾。話すことを避ける助言ではない。",
        },
        {
            "q": "a necessary step は Q21 の空所とどう結びつきますか？",
            "a": "間違えること（making mistakes）を恐れずに話すことが、上達のための「必要な段階」だという姉の助言。",
        },
        {
            "q": "Q22で finished the whole speech と矛盾する誤答は？",
            "a": "he could not continue his speech（続けられなかった）／he had forgotten his speech（忘れていた）。",
        },
        {
            "q": "make it even better から空所を先読みする手順は？",
            "a": "very good だが even better がある → まだ改善の余地 → his speech was not perfect（完璧ではなかったと自覚）。",
        },
    ],
    "highlightPatterns": [
        "afraid to speak the language",
        "embarrassed if his English was wrong",
        "a necessary step to improve his skills",
        "his speech was very good",
        "how he could make it even better",
    ],
    "highlightColor": "#34d399",
    "highlightLabel": "長文空所",
}

fp4 = {
    "id": "fp4",
    "title": "メール読解「About joining my band」（found someone / still looking / phone number）",
    "subtitle": "Email Reading: Refusal, Referral & Next Step",
    "explanation": (
        "大問4Aは拒否→別バンドの紹介→次の行動、というメールの典型構成です。"
        "Q23は we just found someone last week が she has already found a new member の根拠です。"
        "I know how well you can play the guitar があるため、実力不足が理由ではないことに注意します。"
        "Q24は still looking for a good guitarist と the guitarist had to quit last week が一致します。"
        "Q25はメールで最初に示される具体的行動が give me your phone number であり、練習見学は Then, you can go watch の後です。"
    ),
    "sourceQuote": "we just found someone last week / still looking for a good guitarist / perform original music / give me your phone number",
    "sourceLocation": "大問4A「About joining my band」Q23〜25",
    "examples": [
        {
            "en": "However, we just found someone last week. So, unfortunately, we will not be able to include you in our band.",
            "ja": "しかし先週ちょうど誰かを見つけた。残念ながら、あなたをバンドに入れることはできない。",
            "note": "However＝転換。found someone → will not be able to include you。Q23。",
        },
        {
            "en": "I know another band whose members are still looking for a good guitarist.",
            "ja": "まだ良いギタリストを探している別のバンドを知っている。",
            "note": "still looking for ～＝まだ～を探している。Q24。",
        },
        {
            "en": "If you are interested, you can give me your phone number, and I will pass it to them.",
            "ja": "興味があれば電話番号を教えてください。彼らに伝えます。",
            "note": "give 人 your phone number / pass it to them。Q25の最初の一歩。",
        },
    ],
    "practicePassage": {
        "en": (
            "[出典: About joining my band]\n"
            "It is great to hear that you are interested in joining our band as a guitarist. However, we just found someone last week. So, unfortunately, we will not be able to include you in our band. I am sorry to say that because I know how well you can play the guitar.\n"
            "However, I do have some good news for you. I know another band whose members are still looking for a good guitarist. While they do not cover famous songs, they perform original music. The band started last year, but last week, the guitarist had to quit the band because he needed to focus on his studies.\n"
            "If you are interested, you can give me your phone number, and I will pass it to them. Then, you can go watch one of their practices to see if you like their music."
        ),
        "ja": (
            "ギタリストとしてバンドに入りたいと聞けてうれしい。しかし先週ちょうど誰かを見つけた。残念ながら入れられない。ギターの上手さはよく知っているので残念だ。\n"
            "良い知らせもある。まだギタリストを探している別のバンドを知っている。有名曲のカバーはせずオリジナル曲を演奏する。昨年始まったが、先週ギタリストが勉強のため辞めた。\n"
            "興味があれば電話番号を教えてほしい。彼らに伝える。その後、練習を見に行って音楽が気に入るか確かめられる。"
        ),
        "audioFile": "audio/practice_pp4.mp3",
    },
    "practiceQuestions": [
        {
            "q": "Q23で「実力が足りない」が誤答になる一文は？",
            "a": "I know how well you can play the guitar（ギターの上手さはよく知っている）。",
        },
        {
            "q": "Q24で「他バンドの曲が好き」が誤答になる一文は？",
            "a": "While they do not cover famous songs, they perform original music（カバーはせずオリジナル）。",
        },
        {
            "q": "Q25で練習を見に行くのが「直後の行動」でない理由は？",
            "a": "Then, you can go watch（その後）とあり、先に give me your phone number が必要。",
        },
        {
            "q": "perform original music の original は設問でどう言い換えられますか？",
            "a": "They do not cover famous songs（有名曲のカバーはしない）と対比で理解する。",
        },
    ],
    "highlightPatterns": [
        "we just found someone last week",
        "still looking for a good guitarist",
        "perform original music",
        "give me your phone number",
        "go watch one of their practices",
    ],
    "highlightColor": "#fbbf24",
    "highlightLabel": "メール読解",
}

fp5 = {
    "id": "fp5",
    "title": "論説読解とパラフレーズ（Pig Beach / unique sight / educate tourists）",
    "subtitle": "Expository Reading & Key Paraphrases",
    "explanation": (
        "大問4B「Pig Beach」は、人気の理由→豚の由来→観光客の悪影響→保護策、という論説構成です。"
        "Q26では unique sight が very unusual view に言い換えられます（豚が泳ぐ珍しい光景）。"
        "Q27では old sailors left their pigs on the island が sailors brought them but left them behind に対応します。"
        "Q28では not good for their health が fed food that is not good for them to eat です。"
        "Q29では educate tourists on how to behave properly が teach tourists how to treat them correctly です。"
        "本文の名詞・動詞を追い、形容詞の追加（unusual）や語順の変化に注意してください。"
    ),
    "sourceQuote": "unique sight / old sailors left their pigs / not good for their health / educate tourists on how to behave properly",
    "sourceLocation": "大問4B「Pig Beach」Q26〜29",
    "examples": [
        {
            "en": "This has led many tourists to visit the island to see this unique sight.",
            "ja": "多くの観光客が、この独特な光景を見るために島を訪れるようになった。",
            "note": "unique sight＝独特な光景。Q26のパラフレーズ very unusual view の根拠。",
        },
        {
            "en": "One story says that old sailors left their pigs on the island.",
            "ja": "一つの説では、古い船員が豚を島に残していったという。",
            "note": "leave ～ on the island＝島に残す。Q27の正解根拠。",
        },
        {
            "en": "they have started campaigns to educate tourists on how to behave properly around the swimming pigs.",
            "ja": "泳ぐ豚の周りで適切に行動するよう観光客に教育するキャンペーンを始めた。",
            "note": "educate 人 on how to ～＝～の仕方を教育する。Q29。",
        },
    ],
    "practicePassage": {
        "en": (
            "[出典: Pig Beach]\n"
            "In recent years, these pigs have gained popularity worldwide because of social media. This has led many tourists to visit the island to see this unique sight. As a result, this has had some negative impact on these animals.\n"
            "One story says that old sailors left their pigs on the island. Today, tourists who come to see the pigs sometimes cause problems. They often give the pigs various kinds of food, but much of it is not good for their health.\n"
            "To protect the pigs, several organizations and the local government are taking action. For example, they have started campaigns to educate tourists on how to behave properly around the swimming pigs. They are also cleaning up the beach and making stricter rules on feeding the pigs."
        ),
        "ja": (
            "近年、豚はソーシャルメディアで世界的に人気を得た。多くの観光客が独特な光景を見るために島を訪れる。結果、動物に悪影響を与えている。\n"
            "一つの説では古い船員が豚を島に残した。今日、観光客は問題を引き起こすことがある。さまざまな餌を与えるが、その多くは健康に良くない。\n"
            "保護のため団体と地方政府が行動している。泳ぐ豚の周りで適切に行動するよう観光客に教育するキャンペーンを始めた。ビーチの清掃や餌やりの厳しいルールも作っている。"
        ),
        "audioFile": "audio/practice_pp5.mp3",
    },
    "practiceQuestions": [
        {
            "q": "Q26で「観光客が減少した」が誤答になる一文は？",
            "a": "led many tourists to visit the island（多くの観光客が訪れるようになった）。",
        },
        {
            "q": "Q27で broken ship landed there が誤答になる理由は？",
            "a": "本文は pigs swam to the island after escaping（逃げて泳いだ）であり、船が着陸した話ではない。",
        },
        {
            "q": "Q28の正解パラフレーズを本文から説明してください。",
            "a": "much of it is not good for their health → They are fed food that is not good for them to eat。",
        },
        {
            "q": "Q29で入島禁止が誤答になる理由は？",
            "a": "making stricter rules on feeding（餌やりの厳しいルール）であり、観光客の入島禁止ではない。",
        },
    ],
    "highlightPatterns": [
        "unique sight",
        "old sailors left their pigs on the island",
        "not good for their health",
        "educate tourists on how to behave properly",
        "making stricter rules on feeding the pigs",
    ],
    "highlightColor": "#f59e0b",
    "highlightLabel": "論説・言い換え",
}

with open(DATA_PATH, encoding="utf-8") as f:
    data = json.load(f)

data["lessonPlan"] = {"focusPoints": [fp1, fp2, fp3, fp4, fp5]}

all_text = ""
for sec in data.get("sections", []):
    for q in sec.get("questions", []):
        all_text += q.get("text", "") + " "
        all_text += " ".join(q.get("choices", [])) + " "
    for p in sec.get("passages", []):
        all_text += " ".join(p.get("paragraphs", [])) + " "
        for qq in p.get("questions", []):
            all_text += " ".join(qq.get("choices", [])) + " "
            if qq.get("question"):
                all_text += qq.get("question", "") + " "

missing = []
for fp in data["lessonPlan"]["focusPoints"]:
    for pat in fp["highlightPatterns"]:
        if pat not in all_text:
            missing.append(f"{fp['id']}: {pat}")

if missing:
    print("本文に見つからないパターン:")
    for m in missing:
        print(" -", m)
    sys.exit(1)

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Wrote lessonPlan (5 focusPoints) to {DATA_PATH}")

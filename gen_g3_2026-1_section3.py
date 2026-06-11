# -*- coding: utf-8 -*-
"""
2026年度 第1回（土曜準会場）英検3級 data.json
大問3（reading-comprehension）Q21〜30 — 解説・和訳付き
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade3", "2026-1-sat", "data.json",
)

section3 = {
    "name": "大問3",
    "nameEn": "Part 3",
    "type": "reading-comprehension",
    "instruction": "次のA，B，Cの内容に関して，質問に対して最も適切なもの，または文を完成させるのに最も適切なものを1，2，3，4の中から一つ選びなさい。",
    "passages": [
        {
            "label": "A",
            "title": "Free Cooking Class",
            "format": "notice",
            "paragraphs": [
                "Free Cooking Class",
                "There will be a fun and free cooking class at Sunny Brook Farm. You can learn how to make delicious meals using vegetables from our farm. This class is perfect for anyone who likes cooking.",
                "Date: Saturday, June 15\nTime: 10:00 a.m. to 12:30 p.m.\nPlace: Sunny Brook Farm",
                "You do not have to bring anything with you. We will prepare all of the ingredients. To join the cooking class, please send an email to cookingclassinfo@sunnybrookfarm12345.com or call us at 555-5555-5555.",
                "For more information about our vegetables, please check our website.",
                "Let's cook with fresh vegetables and eat healthy food!",
            ],
            "translations": [
                "無料料理教室",
                "サニーブルック農場で楽しい無料の料理教室を開催します。農場の野菜を使っておいしい料理の作り方を学べます。料理が好きな方にぴったりのクラスです。",
                "日時：6月15日（土）\n時間：午前10時〜午後12時30分\n場所：サニーブルック農場",
                "持ち物は不要です。材料はすべてこちらで用意します。参加申し込みは cookingclassinfo@sunnybrookfarm12345.com へメールを送るか、555-5555-5555 へお電話ください。",
                "野菜についての詳しい情報は、ウェブサイトをご覧ください。",
                "新鮮な野菜で料理して、健康的な食事を楽しみましょう！",
            ],
            "questions": [
                {
                    "number": 21,
                    "question": "What is this notice for?",
                    "questionTranslation": "このお知らせの目的は何？",
                    "choices": [
                        "To introduce a new farm.",
                        "To find cooking class teachers.",
                        "To introduce a cooking event.",
                        "To ask people to bring food.",
                    ],
                    "answer": 3,
                    "sourceEvidence": "There will be a fun and free cooking class at Sunny Brook Farm.",
                    "grammar": "タイトル Free Cooking Class と、料理教室の開催案内が主題。",
                    "grammarSimple": "無料の料理教室のイベントを紹介するお知らせだよ。",
                    "choiceAnalysis": [
                        "新しい農場の紹介→農場は会場であって主題ではない。",
                        "先生を探す→参加者を募集している。",
                        "○ 料理イベント（教室）の紹介。",
                        "食べ物を持参→You do not have to bring anything と矛盾。",
                    ],
                    "choiceAnalysisSimple": [
                        "新しい農場の紹介じゃないよ。",
                        "先生をさがすお知らせじゃないよ。",
                        "○ 料理教室のイベントのお知らせ！",
                        "食べ物を持ってこいとは書いてないよ。",
                    ],
                    "choiceTranslations": [
                        "新しい農場を紹介するため。",
                        "料理教室の先生を探すため。",
                        "料理イベントを紹介するため。",
                        "食べ物を持参してもらうため。",
                    ],
                },
                {
                    "number": 22,
                    "question": "How can people get information about the vegetables?",
                    "questionTranslation": "野菜の情報はどうやって得られる？",
                    "choices": [
                        "By looking at a website.",
                        "By sending an email.",
                        "By calling the farm.",
                        "By going to a workshop.",
                    ],
                    "answer": 1,
                    "sourceEvidence": "For more information about our vegetables, please check our website.",
                    "grammar": "野菜の情報＝check our website。メール・電話は参加申し込み用。",
                    "grammarSimple": "野菜のことはウェブサイトを見てね。メールや電話は参加のためだよ。",
                    "choiceAnalysis": [
                        "○ ウェブサイトを見る。",
                        "メール→To join the cooking class（参加申し込み）。",
                        "電話→参加申し込み用。",
                        "ワークショップ→書かれていない。",
                    ],
                    "choiceAnalysisSimple": [
                        "○ ウェブサイトを見る！",
                        "メールは教室に参加するためだよ。",
                        "電話も参加のためだよ。",
                        "ワークショップとは書いてないよ。",
                    ],
                    "choiceTranslations": [
                        "ウェブサイトを見る。",
                        "メールを送る。",
                        "農場に電話する。",
                        "ワークショップに行く。",
                    ],
                },
            ],
        },
        {
            "label": "B",
            "title": "Drama club performance",
            "format": "multi-email",
            "emails": [
                {
                    "meta": {
                        "from": "Emma Suzuki",
                        "to": "Mia Johnson",
                        "date": "September 25",
                        "subject": "Drama club performance",
                    },
                    "body": "Hi Mia,\nI hope you're doing well! I wanted to remind you about my drama club performance next week. I'm so excited! The drama club practiced a lot, and now the play is finally ready. We practiced for two hours every day at school, and I practiced at home every day for an hour, too. I practiced with my dad. I'm still a little nervous, but it will be fine. The performance will be on Friday at 5 p.m. at the local theater. Can you still come? I want you to see the performance! My mom and brother are coming, too, so you can sit together. The drama club will sell snacks and drinks before the play, so my family will arrive at 4:30 p.m. and buy some snacks. I think it will be a lot of fun!\nYour friend,\nEmma",
                    "translation": "ミアへ\n元気？来週の演劇部の公演のことを思い出させたくて。すごく楽しみ！演劇部はたくさん練習して、やっと劇が完成したよ。学校では毎日2時間練習して、家でも毎日1時間練習した。お父さんと一緒に練習したんだ。まだちょっと緊張するけど大丈夫。公演は金曜の午後5時、地元の劇場だよ。まだ来られる？見に来てほしいな！お母さんと弟も来るから、一緒に座れるよ。演劇部が劇の前にスナックと飲み物を売るから、うちの家族は4:30に着いてスナックを買う予定。すごく楽しみ！\n友だちのエマより",
                },
                {
                    "meta": {
                        "from": "Mia Johnson",
                        "to": "Emma Suzuki",
                        "date": "September 25",
                        "subject": "Sounds fun!",
                    },
                    "body": "Hi Emma,\nI'm doing great! Thanks for reminding me about the performance. Of course, I will go! I'm so excited! You practiced so much, so I am sure it will be very nice. What is the play about? Is it a comedy? I like comedy plays the best! My sister wants to come, too. Can we sit with your family? Also, when do we buy the tickets? Do we buy them in the theater on Friday, or before Friday? I want to buy some snacks, too, so my sister and I will arrive at 4:15 p.m. We will take the bus to the theater, and our mom will drive us home. When will the performance end?\nYour friend,\nMia",
                    "translation": "エマへ\n元気だよ！公演のことを思い出させてくれてありがとう。もちろん行くよ！すごく楽しみ！たくさん練習したんだから、きっとすばらしい公演だよね。劇は何について？コメディ？コメディが一番好き！妹も来たいって。あなたの家族と一緒に座れる？チケットはいつ買うの？金曜に劇場で買うの？それとも前？私もスナックを買いたいから、妹と一緒に4:15に着く予定。劇場にはバスで行って、帰りはお母さんが車で送ってくれる。公演はいつ終わる？\n友だちのミアより",
                },
            ],
            "paragraphs": [
                "Emma reminds Mia about her drama club performance next Friday at the local theater.",
            ],
            "translations": [
                "エマはミアに、来週金曜の地元劇場での演劇部の公演を思い出させる。",
            ],
            "questions": [
                {
                    "number": 23,
                    "question": "What did Emma do at home?",
                    "questionTranslation": "エマは家で何をした？",
                    "choices": [
                        "She practiced the play.",
                        "She ate snacks and drank juice.",
                        "She studied for a test.",
                        "She played games with her father.",
                    ],
                    "answer": 1,
                    "sourceEvidence": "I practiced at home every day for an hour, too. I practiced with my dad.",
                    "grammar": "I practiced at home every day for an hour＝家で劇の練習をした。",
                    "grammarSimple": "家でまいにち1じかん、劇のれんしゅうをしたよ。お父さんといっしょに。",
                    "choiceAnalysis": [
                        "○ 劇の練習をした。",
                        "スナックとジュース→劇場で売られる話。",
                        "テスト勉強→書かれていない。",
                        "父とゲーム→practiced with my dad（練習した）。",
                    ],
                    "choiceAnalysisSimple": [
                        "○ 家で劇のれんしゅうをした！",
                        "スナックを食べた話じゃないよ。",
                        "テストのべんきょうとは書いてないよ。",
                        "ゲームじゃなくれんしゅうだよ。",
                    ],
                    "choiceTranslations": [
                        "劇の練習をした。",
                        "スナックを食べ、ジュースを飲んだ。",
                        "テストの勉強をした。",
                        "父とゲームをした。",
                    ],
                },
                {
                    "number": 24,
                    "question": "Who will go to the performance?",
                    "questionTranslation": "誰が公演に行く？",
                    "choices": [
                        "Mia's mother.",
                        "Mia's brother.",
                        "Emma's father.",
                        "Emma's brother.",
                    ],
                    "answer": 4,
                    "sourceEvidence": "My mom and brother are coming, too",
                    "grammar": "Emmaのメールで My mom and brother are coming とある。",
                    "grammarSimple": "エマのお母さんと弟が来るって書いてあるよ。",
                    "choiceAnalysis": [
                        "ミアの母→帰りに車で送るだけ。",
                        "ミアの弟→妹が来る話。",
                        "エマの父→練習に一緒だったが公演には言及なし。",
                        "○ エマの弟。",
                    ],
                    "choiceAnalysisSimple": [
                        "ミアのお母さんはかえりの車だよ。",
                        "ミアの弟じゃなく妹だよ。",
                        "エマのお父さんは公演に行くとは書いてないよ。",
                        "○ エマの弟が来る！",
                    ],
                    "choiceTranslations": [
                        "ミアの母。",
                        "ミアの弟。",
                        "エマの父。",
                        "エマの弟。",
                    ],
                },
                {
                    "number": 25,
                    "question": "How will Mia go to the theater on Friday?",
                    "questionTranslation": "ミアは金曜に劇場へどうやって行く？",
                    "choices": [
                        "Her mother will drive her.",
                        "She will walk.",
                        "She will take the bus.",
                        "She will take the train.",
                    ],
                    "answer": 3,
                    "sourceEvidence": "We will take the bus to the theater",
                    "grammar": "take the bus to the theater＝バスで劇場へ。帰りは母が車。",
                    "grammarSimple": "劇場にはバスで行くよ。かえりはお母さんの車。",
                    "choiceAnalysis": [
                        "母が車で送る→帰り（drive us home）。",
                        "歩く→書かれていない。",
                        "○ バスに乗る。",
                        "電車→書かれていない。",
                    ],
                    "choiceAnalysisSimple": [
                        "お母さんの車はかえりだよ。",
                        "あるいて行くとは書いてないよ。",
                        "○ バスで行く！",
                        "電車とは書いてないよ。",
                    ],
                    "choiceTranslations": [
                        "母が車で送る。",
                        "歩いて行く。",
                        "バスに乗る。",
                        "電車に乗る。",
                    ],
                },
            ],
        },
        {
            "label": "C",
            "title": "Table Tennis",
            "format": "passage",
            "paragraphs": [
                "Table tennis is a sport that started in England. In the 1880s, people in England played table tennis instead of tennis when the weather was bad because it was a fun way to stay active indoors. Many people enjoyed the game, and it became very popular. Soon, more people started playing table tennis in England, and then people from other countries started to play it as well.",
                "In 1926, the first world championships for table tennis were held. Players from different countries, such as Hungary, Germany, and India, went to England and played in the table tennis championships. This tournament spread the sport around the world. From around 1950, countries in Asia started playing table tennis, too. It became popular there.",
                "Table tennis became popular in many countries because it was easy to start playing. It did not cost a lot of money because it could be played with cheap items. The sport was fun for everyone, and people of all ages could play. There have been many professional table tennis players from Asia, and they have won many medals in the Olympics.",
                "In 1971, an important moment in table tennis history happened. At one of the table tennis championships in Japan, an American athlete missed his bus and got on the Chinese team's bus instead. A Chinese athlete on the bus gave him a drawing of the mountains in his country. This was a special moment for the players from both countries. Table tennis helped people from many countries to become friends.",
            ],
            "translations": [
                "卓球はイングランドで始まったスポーツです。1880年代、天気が悪いときにテニスの代わりに卓球をして、屋内で活動的に過ごす楽しい方法だったため、イングランドの人々は卓球をしました。多くの人がこのゲームを楽しみ、とても人気になりました。やがてイングランドでより多くの人が卓球を始め、他国の人々もプレイするようになりました。",
                "1926年、初の卓球世界選手権が開催されました。ハンガリー、ドイツ、インドなどさまざまな国の選手がイングランドに行き、卓球選手権で競いました。この大会がスポーツを世界中に広めました。1950年頃からアジアの国々でも卓球が始まり、そこでも人気になりました。",
                "卓球は始めるのが簡単だったため、多くの国で人気になりました。安い道具でできたので、あまりお金がかかりませんでした。このスポーツは誰にとっても楽しく、あらゆる年齢の人がプレイできました。アジアから多くのプロ卓球選手が出て、オリンピックで多くのメダルを獲得しています。",
                "1971年、卓球の歴史における重要な出来事がありました。日本で開催された卓球選手権のとき、アメリカの選手がバスに乗り遅れ、代わりに中国チームのバスに乗りました。バスの中の中国の選手が、彼に自分の国の山の絵を贈りました。両国の選手にとって特別な瞬間でした。卓球は多くの国の人々が友だちになるのを助けました。",
            ],
            "questions": [
                {
                    "number": 26,
                    "question": "Why did people in England play table tennis in the 1880s?",
                    "questionTranslation": "1880年代、イングランドの人々はなぜ卓球をした？",
                    "choices": [
                        "It was already popular in other countries.",
                        "It was the only sport in England.",
                        "They wanted to stay active inside.",
                        "They wanted to enjoy the nice weather outside.",
                    ],
                    "answer": 3,
                    "sourceEvidence": "when the weather was bad because it was a fun way to stay active indoors",
                    "grammar": "天気が悪いとき→屋内で活動的に過ごす（stay active indoors）。",
                    "grammarSimple": "天気がわるいとき、おくのなかでうんどうしたかったからだよ。",
                    "choiceAnalysis": [
                        "他国で人気→その後広まった話。",
                        "唯一のスポーツ→書かれていない。",
                        "○ 屋内で活動的に過ごしたかった。",
                        "外の良い天気→天気が悪いときの話。",
                    ],
                    "choiceAnalysisSimple": [
                        "他の国でにんきだったからじゃないよ。",
                        "いちばんだけのスポーツとは書いてないよ。",
                        "○ おくのなかでからだをうごかしたかった！",
                        "外の天気はわるかったよ。",
                    ],
                    "choiceTranslations": [
                        "すでに他国で人気だったから。",
                        "イングランドで唯一のスポーツだったから。",
                        "屋内で活動的に過ごしたかったから。",
                        "外の良い天気を楽しみたかったから。",
                    ],
                },
                {
                    "number": 27,
                    "question": "The first table tennis world championships were held in",
                    "questionTranslation": "初の卓球世界選手権はどこで開催された？",
                    "choices": [
                        "England.",
                        "Germany.",
                        "Hungary.",
                        "India.",
                    ],
                    "answer": 1,
                    "sourceEvidence": "went to England and played in the table tennis championships",
                    "grammar": "各国の選手が England に行って選手権で競った。",
                    "grammarSimple": "いろいろな国の選手がイングランドに行ってしあいをしたよ。",
                    "choiceAnalysis": [
                        "○ イングランド。",
                        "ドイツ→参加国。",
                        "ハンガリー→参加国。",
                        "インド→参加国。",
                    ],
                    "choiceAnalysisSimple": [
                        "○ イングランドで開かれた！",
                        "ドイツはさんかした国だよ。",
                        "ハンガリーもさんかした国だよ。",
                        "インドもさんかした国だよ。",
                    ],
                    "choiceTranslations": [
                        "イングランド。",
                        "ドイツ。",
                        "ハンガリー。",
                        "インド。",
                    ],
                },
                {
                    "number": 28,
                    "question": "Why did table tennis become popular in many countries?",
                    "questionTranslation": "なぜ卓球は多くの国で人気になった？",
                    "choices": [
                        "It was a sport for only young people.",
                        "It was easy for people to start playing.",
                        "It was the first Olympic sport.",
                        "Tickets to the competitions were very cheap.",
                    ],
                    "answer": 2,
                    "sourceEvidence": "because it was easy to start playing",
                    "grammar": "easy to start playing（始めるのが簡単）が理由。",
                    "grammarSimple": "はじめるのがかんたんだったからだよ。",
                    "choiceAnalysis": [
                        "若者だけ→people of all ages could play と矛盾。",
                        "○ 始めるのが簡単。",
                        "最初のオリンピック種目→書かれていない。",
                        "チケットが安い→書かれていない。",
                    ],
                    "choiceAnalysisSimple": [
                        "若い人だけじゃないよ。",
                        "○ はじめるのがかんたんだった！",
                        "さいしょのオリンピックじゃないよ。",
                        "チケットの話は書いてないよ。",
                    ],
                    "choiceTranslations": [
                        "若者だけのスポーツだったから。",
                        "始めるのが簡単だったから。",
                        "最初のオリンピック種目だったから。",
                        "大会のチケットがとても安かったから。",
                    ],
                },
                {
                    "number": 29,
                    "question": "What did a Chinese athlete do at the table tennis championship in 1971?",
                    "questionTranslation": "1971年の選手権で中国の選手は何をした？",
                    "choices": [
                        "He missed his bus.",
                        "He climbed a mountain.",
                        "He gave an athlete a drawing.",
                        "He trained an American athlete.",
                    ],
                    "answer": 3,
                    "sourceEvidence": "A Chinese athlete on the bus gave him a drawing of the mountains",
                    "grammar": "中国の選手が山の絵（drawing）を贈った。バスに乗り遅れたのはアメリカの選手。",
                    "grammarSimple": "中国の選手が、アメリカの選手に山のえをあげたよ。",
                    "choiceAnalysis": [
                        "バスに乗り遅れた→アメリカの選手。",
                        "山に登った→書かれていない。",
                        "○ 選手に絵を贈った。",
                        "アメリカ選手を指導→書かれていない。",
                    ],
                    "choiceAnalysisSimple": [
                        "バスにのりおくれたのはアメリカの選手だよ。",
                        "山にのぼった話じゃないよ。",
                        "○ えをあげた！",
                        "しつだんした話は書いてないよ。",
                    ],
                    "choiceTranslations": [
                        "バスに乗り遅れた。",
                        "山に登った。",
                        "選手に絵を贈った。",
                        "アメリカの選手を指導した。",
                    ],
                },
                {
                    "number": 30,
                    "question": "What is this story about?",
                    "questionTranslation": "この話は何について？",
                    "choices": [
                        "Different sports in England.",
                        "A famous athlete.",
                        "How to learn Chinese.",
                        "The history of a sport.",
                    ],
                    "answer": 4,
                    "sourceEvidence": "Table tennis is a sport that started in England",
                    "grammar": "卓球の起源・普及・1971年の出来事まで述べたスポーツの歴史。",
                    "grammarSimple": "卓球というスポーツの歴史のお話だよ。",
                    "choiceAnalysis": [
                        "イングランドのいろいろなスポーツ→卓球中心。",
                        "有名な選手→一部のエピソード。",
                        "中国語の学び方→書かれていない。",
                        "○ スポーツの歴史。",
                    ],
                    "choiceAnalysisSimple": [
                        "いろいろなスポーツじゃなく卓球の話だよ。",
                        "ゆうめいな選手の話だけじゃないよ。",
                        "中国語の学び方じゃないよ。",
                        "○ スポーツの歴史のお話！",
                    ],
                    "choiceTranslations": [
                        "イングランドのさまざまなスポーツ。",
                        "有名な選手。",
                        "中国語の学び方。",
                        "スポーツの歴史。",
                    ],
                },
            ],
        },
    ],
}

with open(DATA_PATH, encoding="utf-8") as f:
    data = json.load(f)

new_sections = []
replaced = False
for sec in data.get("sections", []):
    if sec.get("name") == "大問3":
        new_sections.append(section3)
        replaced = True
    else:
        new_sections.append(sec)
if not replaced:
    new_sections.append(section3)

data["sections"] = new_sections

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

q_count = sum(len(p["questions"]) for p in section3["passages"])
print(f"Wrote section3 ({q_count} questions, 3 passages) to {DATA_PATH}")

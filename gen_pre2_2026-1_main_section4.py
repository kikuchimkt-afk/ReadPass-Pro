# -*- coding: utf-8 -*-
"""
2026年度 第1回（本会場）英検準2級 data.json
Step D: 大問4（reading-comprehension型）Q23〜29 — リッチ解説
  4A About joining my band / 4B Pig Beach
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

section4 = {
    "name": "大問4",
    "nameEn": "Part 4",
    "type": "reading-comprehension",
    "instruction": "次の英文Ａ，Ｂの内容に関して，(23)から(29)までの質問に対して最も適切なもの，または文を完成させるのに最も適切なものを1，2，3，4の中から一つ選びなさい。",
    "passages": [
        {
            "label": "A",
            "title": "About joining my band",
            "format": "email",
            "meta": {
                "from": "Andrea Patterson <andrea123@ground-mail.com>",
                "to": "Travis Longman <t.j.longman-0428@skyhigh-message.com>",
                "date": "February 20",
                "subject": "About joining my band",
            },
            "paragraphs": [
                "Dear Travis,\nThis is Andrea Patterson. Thanks for your message. It is great to hear that you are interested in joining our band as a guitarist. As you said in your email, we were looking for a new member. However, we just found someone last week. So, unfortunately, we will not be able to include you in our band. I am sorry to say that because I know how well you can play the guitar.",
                "However, I do have some good news for you. I know another band whose members are still looking for a good guitarist. They are also students at our college. While they do not cover famous songs, they perform original music. The band started last year, but last week, the guitarist had to quit the band because he needed to focus on his studies. They usually practice on weekends in the music room on campus.",
                "If you are interested, you can give me your phone number, and I will pass it to them. You could also exchange emails if you prefer, but I think it might be easier to talk with them directly on the phone. They can tell you more about the band. Then, you can go watch one of their practices to see if you like their music. Let me know what you think.\nThank you,\nAndrea Patterson",
            ],
            "translations": [
                "トラヴィスへ\nアンドレア・パターソンです。メッセージありがとう。ギタリストとして私たちのバンドに入りたいと聞けてうれしいです。あなたのメールにもあったように、私たちは新メンバーを探していました。しかし、先週ちょうど誰かを見つけました。残念ながら、あなたをバンドに入れることはできません。ギターの上手さはよく知っているので、そう言うのは残念です。",
                "しかし、良い知らせもあります。まだ良いギタリストを探している別のバンドを知っています。彼らも私たちの大学の学生です。有名な曲のカバーはしませんが、オリジナル曲を演奏します。バンドは昨年始まりましたが、先週ギタリストが勉強に専念する必要がありバンドを辞めました。彼らは通常、週末にキャンパスの音楽室で練習しています。",
                "興味があれば、電話番号を教えてください。彼らに伝えます。メールのやり取りでも構いませんが、電話で直接話すほうが簡単かもしれません。バンドについてもっと教えてくれるでしょう。その後、練習を見に行って、音楽が気に入るか確かめられます。どう思うか教えてください。\nありがとう\nアンドレア・パターソン",
            ],
            "sentencePairs": [
                [
                    "However, we just found someone last week.",
                    "しかし、先週ちょうど誰かを見つけました。",
                ],
                [
                    "So, unfortunately, we will not be able to include you in our band.",
                    "残念ながら、あなたをバンドに入れることはできません。",
                ],
                [
                    "I know another band whose members are still looking for a good guitarist.",
                    "まだ良いギタリストを探している別のバンドを知っています。",
                ],
                [
                    "While they do not cover famous songs, they perform original music.",
                    "有名な曲のカバーはしませんが、オリジナル曲を演奏します。",
                ],
                [
                    "They usually practice on weekends in the music room on campus.",
                    "彼らは通常、週末にキャンパスの音楽室で練習しています。",
                ],
                [
                    "If you are interested, you can give me your phone number, and I will pass it to them.",
                    "興味があれば、電話番号を教えてください。彼らに伝えます。",
                ],
                [
                    "Then, you can go watch one of their practices to see if you like their music.",
                    "その後、練習を見に行って、音楽が気に入るか確かめられます。",
                ],
            ],
            "questions": [
                {
                    "number": 23,
                    "question": "Travis Longman cannot join Andrea Patterson's band because",
                    "questionTranslation": "トラヴィス・ロングマンがアンドレア・パターソンのバンドに入れない理由は？",
                    "choices": [
                        "she thinks he is not good enough for her band.",
                        "her band is only looking for a singer, not a guitarist.",
                        "she has already found a new member for the band.",
                        "her band had already broken up by the time he asked.",
                    ],
                    "choiceTranslations": [
                        "彼はバンドに十分な実力がないと彼女が思っているから。",
                        "バンドはギタリストではなく歌手だけを探しているから。",
                        "彼女はすでにバンドの新メンバーを見つけているから。",
                        "彼が頼んだ時点でバンドはすでに解散していたから。",
                    ],
                    "answer": 3,
                    "choiceAnalysis": [
                        "❌ she thinks he is not good enough＝十分な実力がないと思っている。I know how well you can play the guitar（ギターの上手さはよく知っている）と矛盾。実力不足が理由ではない",
                        "❌ only looking for a singer＝歌手だけを探している。interested in joining our band as a guitarist（ギタリストとして入りたい）と、もともとギタリストを探していた文脈と合わない",
                        "✅ she has already found a new member＝すでに新メンバーを見つけている。we just found someone last week（先週ちょうど誰かを見つけた）＋will not be able to include you（入れられない）が一致→正解",
                        "❌ band had already broken up＝すでに解散していた。we were looking for a new member（新メンバーを探していた）・別バンドを紹介している流れと合わない",
                    ],
                    "sourceEvidence": [
                        "However, we just found someone last week.",
                        "So, unfortunately, we will not be able to include you in our band.",
                    ],
                    "grammar": "💡 find someone＝（人を）見つける。include 人 in ～＝人を～に加える。However（しかし）以降が拒否の理由。",
                },
                {
                    "number": 24,
                    "question": "What is true about the band members that Andrea recommends?",
                    "questionTranslation": "アンドレアが勧めるバンドのメンバーについて正しいのはどれか？",
                    "choices": [
                        "They prefer to play songs from other bands.",
                        "They have been active for several years.",
                        "They practice in a studio outside the campus.",
                        "They have been seeking a new guitarist.",
                    ],
                    "choiceTranslations": [
                        "他のバンドの曲を演奏するのが好きだ。",
                        "数年間活動している。",
                        "キャンパス外のスタジオで練習している。",
                        "新しいギタリストを探している。",
                    ],
                    "answer": 4,
                    "choiceAnalysis": [
                        "❌ prefer to play songs from other bands＝他バンドの曲が好き。do not cover famous songs, they perform original music（有名曲のカバーはせずオリジナル曲）と正反対",
                        "❌ active for several years＝数年活動。The band started last year（昨年始まった）と矛盾",
                        "❌ studio outside the campus＝キャンパス外のスタジオ。practice on weekends in the music room on campus（キャンパスの音楽室）と矛盾",
                        "✅ seeking a new guitarist＝新しいギタリストを探している。still looking for a good guitarist（まだ良いギタリストを探している）＋the guitarist had to quit last week（先週ギタリストが辞めた）が一致→正解",
                    ],
                    "sourceEvidence": [
                        "I know another band whose members are still looking for a good guitarist.",
                        "last week, the guitarist had to quit the band because he needed to focus on his studies.",
                    ],
                    "grammar": "💡 still looking for ～＝まだ～を探している。cover famous songs＝有名曲をカバーする。perform original music＝オリジナル曲を演奏する。",
                },
                {
                    "number": 25,
                    "question": "What will Travis probably do right after reading this email?",
                    "questionTranslation": "トラヴィスはこのメールを読んだ直後、おそらく何をするか？",
                    "choices": [
                        "Send an email to one of the band members.",
                        "Go check out the practice of the recommended band.",
                        "Provide his phone number to Andrea.",
                        "Call Andrea for information about the band.",
                    ],
                    "choiceTranslations": [
                        "バンドメンバーの一人にメールを送る。",
                        "勧められたバンドの練習を見に行く。",
                        "アンドレアに自分の電話番号を伝える。",
                        "バンドの情報を得るためにアンドレアに電話する。",
                    ],
                    "answer": 3,
                    "choiceAnalysis": [
                        "❌ Send an email to band members＝メンバーにメール。exchange emails if you prefer（メールのやり取りも可）とあるが、まず最初のステップとしてAndreaが示すのは電話番号を渡すこと",
                        "❌ Go check out the practice＝練習を見に行く。Then, you can go watch one of their practices（その後、練習を見に行ける）とあり、電話番号を渡した後の流れ",
                        "✅ Provide his phone number to Andrea＝アンドレアに電話番号を伝える。If you are interested, you can give me your phone number, and I will pass it to them（興味があれば電話番号を教えて、彼らに伝える）が最初の具体的行動→正解",
                        "❌ Call Andrea for information＝アンドレアに電話する。I think it might be easier to talk with them directly on the phone（紹介先のバンドと直接話すほうが簡単）とあり、TravisがAndreaに電話する流れではない",
                    ],
                    "sourceEvidence": [
                        "If you are interested, you can give me your phone number, and I will pass it to them.",
                    ],
                    "grammar": "💡 give 人 your phone number＝人に電話番号を教える。pass it to them＝（番号を）彼らに伝える。right after reading＝読んだ直後の最初の一歩に注目。",
                },
            ],
        },
        {
            "label": "B",
            "title": "Pig Beach",
            "paragraphs": [
                "Big Major Cay in the country of the Bahamas is a small island with a beautiful beach known as Pig Beach. On this island, visitors can see and sometimes play with pigs swimming near the beach. In recent years, these pigs have gained popularity worldwide because of social media. This has led many tourists to visit the island to see this unique sight. As a result, this has had some negative impact on these animals.",
                "These pigs are not native to the island, and nobody knows exactly how they arrived there. One story says that old sailors left their pigs on the island. Another story suggests that the pigs swam to the island after escaping from a broken ship. Some people believe the pigs were brought there by farmers from a nearby island. In any case, after these pigs learned that humans, especially tourists today, would feed them, they made the place their home.",
                "Today, tourists who come to see the pigs sometimes cause problems. They often give the pigs various kinds of food, but much of it is not good for their health. This could make the pigs sick. Some reports said that pigs ate harmful items, such as plastic. In the past, some of the pigs died after people fed them on the beach, as they had also eaten too much sand with the food.",
                "To protect the pigs, several organizations and the local government are taking action. For example, they have started campaigns to educate tourists on how to behave properly around the swimming pigs. They are also cleaning up the beach and making stricter rules on feeding the pigs. They aim to improve the situation for both the pigs and the environment through more eco-friendly tourism. These events have also made people reconsider how humans should interact with wild animals.",
            ],
            "translations": [
                "バハマのビッグ・メジャー・ケイは、ピッグ・ビーチとして知られる美しいビーチがある小さな島です。この島では、訪問者はビーチの近くで泳ぐ豚を見たり、時には一緒に遊んだりできます。近年、これらの豚はソーシャルメディアのおかげで世界的に人気を得ました。これにより多くの観光客が、この独特な光景を見るために島を訪れるようになりました。その結果、これらの動物にいくつかの悪影響を与えています。",
                "これらの豚は島の原産ではなく、どのようにそこに到着したかは誰も正確には知りません。一つの説では、古い船員が豚を島に残していったと言われています。別の説では、壊れた船から逃げた後、豚が島まで泳いだとされています。近くの島の農家が連れてきたという人もいます。いずれにせよ、特に今日の観光客が餌を与えてくれることを豚が学んだ後、彼らはその場所を自分たちの住処にしました。",
                "今日、豚を見に来る観光客は時々問題を引き起こします。彼らはさまざまな種類の餌を豚に与えますが、その多くは健康に良くありません。これは豚を病気にする可能性があります。一部の報告では、豚がプラスチックなどの有害な物を食べたと言われています。過去には、ビーチで人々に餌を与えられた後、餌と一緒に砂を食べすぎたために死んだ豚もいました。",
                "豚を保護するため、いくつかの団体と地方政府が行動を起こしています。例えば、泳ぐ豚の周りで適切に行動するよう観光客に教育するキャンペーンを始めました。またビーチの清掃や、豚への餌やりに関するより厳しいルールを作っています。より環境に優しい観光を通じて、豚と環境の両方の状況を改善することを目指しています。これらの出来事は、人間が野生動物とどう関わるべきかを人々に考え直させました。",
            ],
            "sentencePairs": [
                [
                    "In recent years, these pigs have gained popularity worldwide because of social media.",
                    "近年、これらの豚はソーシャルメディアのおかげで世界的に人気を得ました。",
                ],
                [
                    "This has led many tourists to visit the island to see this unique sight.",
                    "多くの観光客が、この独特な光景を見るために島を訪れるようになりました。",
                ],
                [
                    "One story says that old sailors left their pigs on the island.",
                    "一つの説では、古い船員が豚を島に残していったと言われています。",
                ],
                [
                    "They often give the pigs various kinds of food, but much of it is not good for their health.",
                    "さまざまな種類の餌を豚に与えますが、その多くは健康に良くありません。",
                ],
                [
                    "Some reports said that pigs ate harmful items, such as plastic.",
                    "一部の報告では、豚がプラスチックなどの有害な物を食べたと言われています。",
                ],
                [
                    "For example, they have started campaigns to educate tourists on how to behave properly around the swimming pigs.",
                    "泳ぐ豚の周りで適切に行動するよう観光客に教育するキャンペーンを始めました。",
                ],
                [
                    "They are also cleaning up the beach and making stricter rules on feeding the pigs.",
                    "ビーチの清掃や、豚への餌やりに関するより厳しいルールを作っています。",
                ],
            ],
            "questions": [
                {
                    "number": 26,
                    "question": "What is true about Big Major Cay?",
                    "questionTranslation": "ビッグ・メジャー・ケイについて正しいのはどれか？",
                    "choices": [
                        "Social media has made it famous for its large, beautiful beach.",
                        "There are pigs living there without any contact with humans.",
                        "This island, where pigs live, offers tourists a very unusual view.",
                        "It experienced a drop in tourists in recent years due to the pigs.",
                    ],
                    "choiceTranslations": [
                        "ソーシャルメディアが大きく美しいビーチで有名にした。",
                        "人間と接触しない豚がそこに住んでいる。",
                        "豚が住むこの島は、観光客に非常に珍しい光景を提供している。",
                        "豚のせいで近年観光客が減少した。",
                    ],
                    "answer": 3,
                    "choiceAnalysis": [
                        "❌ famous for its large, beautiful beach＝大きく美しいビーチで有名。social mediaで有名になったのは豚（these pigs have gained popularity）であり、ビーチそのものの「大きさ」が主題ではない",
                        "❌ without any contact with humans＝人間と接触しない。visitors can see and sometimes play with pigs（見たり遊んだりできる）・tourists would feed them（餌を与える）と矛盾",
                        "✅ offers tourists a very unusual view＝非常に珍しい光景を提供している。see this unique sight（この独特な光景を見る）＋pigs swimming near the beach（ビーチ近くで泳ぐ豚）が一致→正解",
                        "❌ drop in tourists＝観光客の減少。led many tourists to visit the island（多くの観光客が訪れるようになった）と記述が逆",
                    ],
                    "sourceEvidence": [
                        "This has led many tourists to visit the island to see this unique sight.",
                        "visitors can see and sometimes play with pigs swimming near the beach.",
                    ],
                    "grammar": "💡 unique sight＝独特な光景。gain popularity＝人気を得る。As a result（その結果）以降のnegative impactは観客増の副作用。",
                },
                {
                    "number": 27,
                    "question": "One possible explanation for the pigs being on the island is that",
                    "questionTranslation": "豚が島にいることの説明の一つとして考えられるのは？",
                    "choices": [
                        "people brought them to attract tourists.",
                        "a broken ship landed there with them inside.",
                        "they originally came from this island.",
                        "sailors brought them but left them behind.",
                    ],
                    "choiceTranslations": [
                        "観光客を引き付けるために人々が連れてきた。",
                        "壊れた船が豚を乗せたままそこに着陸した。",
                        "もともとこの島原産だった。",
                        "船員が連れてきたが置き去りにした。",
                    ],
                    "answer": 4,
                    "choiceAnalysis": [
                        "❌ to attract tourists＝観光客を引き付けるため。these pigs have gained popularity worldwide because of social media（SNSで人気になってから）の話で、連れてきた理由の記述はない",
                        "❌ broken ship landed there with them inside＝壊れた船が着陸した。本文はpigs swam to the island after escaping from a broken ship（壊れた船から逃げて泳いだ）であり、船が着陸した話ではない",
                        "❌ originally came from this island＝この島原産。These pigs are not native to the island（原産ではない）と明記",
                        "✅ sailors brought them but left them behind＝船員が連れてきたが置き去りにした。One story says that old sailors left their pigs on the island（古い船員が豚を島に残した）と一致→正解",
                    ],
                    "sourceEvidence": [
                        "One story says that old sailors left their pigs on the island.",
                        "These pigs are not native to the island, and nobody knows exactly how they arrived there.",
                    ],
                    "grammar": "💡 be native to ～＝～の原産である。leave ～ on the island＝～を島に残す。One story says that ～＝一つの説では～だという。",
                },
                {
                    "number": 28,
                    "question": "How are the pigs affected by tourists?",
                    "questionTranslation": "観光客によって豚はどのような影響を受けているか？",
                    "choices": [
                        "They feel stressed when tourists touch them carelessly.",
                        "They are fed food that is not good for them to eat.",
                        "Their homes are being destroyed because of plastic trash.",
                        "Too many tourists drive them away from their homes.",
                    ],
                    "choiceTranslations": [
                        "観光客が不注意に触るとストレスを感じる。",
                        "食べるのに良くない餌を与えられている。",
                        "プラスチックゴミのせいで住処が破壊されている。",
                        "観光客が多すぎて住処から追い出されている。",
                    ],
                    "answer": 2,
                    "choiceAnalysis": [
                        "❌ stressed when tourists touch them carelessly＝不注意に触られるとストレス。visitors can see and sometimes play with pigs（見たり遊んだりできる）とあり、触ることへのストレスより餌の問題が中心",
                        "✅ fed food that is not good for them＝食べるのに良くない餌を与えられている。much of it is not good for their health（健康に良くない）＋could make the pigs sick（病気にする可能性）が一致→正解",
                        "❌ homes destroyed because of plastic trash＝プラスチックゴミで住処が破壊。pigs ate harmful items, such as plastic（有害物を食べた）はあるが、住処の破壊の話ではない",
                        "❌ drive them away from homes＝住処から追い出す。they made the place their home（その場所を住処にした）と、追い出されている描写はない",
                    ],
                    "sourceEvidence": [
                        "They often give the pigs various kinds of food, but much of it is not good for their health.",
                        "This could make the pigs sick.",
                    ],
                    "grammar": "💡 be not good for one's health＝健康に良くない。harmful items＝有害な物。cause problems（問題を引き起こす）の具体例が餌。",
                },
                {
                    "number": 29,
                    "question": "What was done to protect the pigs on the island?",
                    "questionTranslation": "島の豚を保護するために何が行われたか？",
                    "choices": [
                        "The government provided locals with information on how to handle them.",
                        "The government made a rule that no tourists could go to the island.",
                        "Some groups were working to teach tourists how to treat them correctly.",
                        "Some groups were cleaning the beach without the help of the government.",
                    ],
                    "choiceTranslations": [
                        "政府が地元の人に扱い方の情報を提供した。",
                        "政府が観光客の入島を禁止するルールを作った。",
                        "いくつかの団体が観光客に正しい接し方を教える活動をしていた。",
                        "いくつかの団体が政府の助けなしにビーチを清掃していた。",
                    ],
                    "answer": 3,
                    "choiceAnalysis": [
                        "❌ provided locals with information＝地元の人に情報提供。campaigns to educate tourists（観光客を教育する）であり、地元住民への情報提供の話ではない",
                        "❌ no tourists could go to the island＝観光客の入島禁止。making stricter rules on feeding（餌やりの厳しいルール）であり、入島禁止の記述はない",
                        "✅ teach tourists how to treat them correctly＝観光客に正しい接し方を教える。campaigns to educate tourists on how to behave properly around the swimming pigs（泳ぐ豚の周りで適切に行動するよう観光客に教育）と一致→正解",
                        "❌ cleaning the beach without the government＝政府なしで清掃。several organizations and the local government are taking action（団体と地方政府が行動）とあり、政府も関与している",
                    ],
                    "sourceEvidence": [
                        "For example, they have started campaigns to educate tourists on how to behave properly around the swimming pigs.",
                        "They are also cleaning up the beach and making stricter rules on feeding the pigs.",
                    ],
                    "grammar": "💡 educate 人 on how to ～＝人に～の仕方を教育する。behave properly＝適切に行動する。several organizations and the local government＝複数主体の協力に注目。",
                },
            ],
        },
    ],
}

with open(DATA_PATH, encoding="utf-8") as f:
    data = json.load(f)

sections = data["sections"]
section1 = next(s for s in sections if s["name"] == "大問1")
section2 = next(s for s in sections if s["name"] == "大問2")
section3 = next(s for s in sections if s["name"] == "大問3")
data["sections"] = [section1, section2, section3, section4]

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

q_count = sum(len(p["questions"]) for p in section4["passages"])
print(f"Wrote section4 ({q_count} questions) to {DATA_PATH}")

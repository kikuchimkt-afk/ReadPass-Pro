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
                "トラヴィスへ\nアンドレア・パターソンです。メッセージをありがとう。私たちのバンドにギタリストとして入りたいと思ってくれていると聞き、とてもうれしいです。あなたがメールに書いていたとおり、私たちは新しいメンバーを探していました。しかし、先週ちょうど新しいメンバーが見つかりました。そのため、残念ながらあなたを私たちのバンドに迎えることはできません。あなたがギターをとても上手に弾けることを知っているので、こうお伝えするのは残念です。",
                "ただ、あなたに良い知らせもあります。メンバーが今も上手なギタリストを探している別のバンドを知っています。そのメンバーも私たちの大学の学生です。有名な曲のカバーはしませんが、オリジナル曲を演奏します。そのバンドは昨年結成されましたが、先週、ギタリストが学業に専念する必要があり、バンドを辞めました。普段は週末に、キャンパス内の音楽室で練習しています。",
                "興味があれば、私に電話番号を教えてください。私から彼らに伝えます。希望すればメールをやり取りすることもできますが、電話で彼らと直接話すほうが簡単かもしれないと思います。彼らからバンドについてもっと詳しく聞けます。その後、彼らの練習を見に行き、その音楽が気に入るか確かめることができます。どう思うか教えてください。\nありがとう\nアンドレア・パターソン",
            ],
            "sentencePairs": [
                [
                    "This is Andrea Patterson.",
                    "アンドレア・パターソンです。",
                ],
                [
                    "Thanks for your message.",
                    "メッセージをありがとう。",
                ],
                [
                    "It is great to hear that you are interested in joining our band as a guitarist.",
                    "私たちのバンドにギタリストとして入りたいと思ってくれていると聞き、とてもうれしいです。",
                ],
                [
                    "As you said in your email, we were looking for a new member.",
                    "あなたがメールに書いていたとおり、私たちは新しいメンバーを探していました。",
                ],
                [
                    "However, we just found someone last week.",
                    "しかし、先週ちょうど新しいメンバーが見つかりました。",
                ],
                [
                    "So, unfortunately, we will not be able to include you in our band.",
                    "そのため、残念ながらあなたを私たちのバンドに迎えることはできません。",
                ],
                [
                    "I am sorry to say that because I know how well you can play the guitar.",
                    "あなたがギターをとても上手に弾けることを知っているので、こうお伝えするのは残念です。",
                ],
                [
                    "However, I do have some good news for you.",
                    "ただ、あなたに良い知らせもあります。",
                ],
                [
                    "I know another band whose members are still looking for a good guitarist.",
                    "メンバーが今も上手なギタリストを探している別のバンドを知っています。",
                ],
                [
                    "They are also students at our college.",
                    "そのメンバーも私たちの大学の学生です。",
                ],
                [
                    "While they do not cover famous songs, they perform original music.",
                    "有名な曲のカバーはしませんが、オリジナル曲を演奏します。",
                ],
                [
                    "The band started last year, but last week, the guitarist had to quit the band because he needed to focus on his studies.",
                    "そのバンドは昨年結成されましたが、先週、ギタリストが学業に専念する必要があり、バンドを辞めました。",
                ],
                [
                    "They usually practice on weekends in the music room on campus.",
                    "普段は週末に、キャンパス内の音楽室で練習しています。",
                ],
                [
                    "If you are interested, you can give me your phone number, and I will pass it to them.",
                    "興味があれば、私に電話番号を教えてください。私から彼らに伝えます。",
                ],
                [
                    "You could also exchange emails if you prefer, but I think it might be easier to talk with them directly on the phone.",
                    "希望すればメールをやり取りすることもできますが、電話で彼らと直接話すほうが簡単かもしれないと思います。",
                ],
                [
                    "They can tell you more about the band.",
                    "彼らからバンドについてもっと詳しく聞けます。",
                ],
                [
                    "Then, you can go watch one of their practices to see if you like their music.",
                    "その後、彼らの練習を見に行き、その音楽が気に入るか確かめることができます。",
                ],
                [
                    "Let me know what you think.",
                    "どう思うか教えてください。",
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
                        "not good enough＝実力不足。I know how well you can play the guitar（ギターがとても上手だと知っている）と反する。",
                        "only looking for a singer＝歌手だけを募集。本文はnew memberと述べており、歌手だけという記述はない。",
                        "already found a new member＝すでに新メンバーが見つかった。we just found someone last weekが直接の理由→正解。💡",
                        "had already broken up＝すでに解散していた。we just found someone last week（先週メンバーが見つかった）と合わない。",
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
                        "songs from other bands＝他のバンドの曲。do not cover famous songsとperform original musicに反する。",
                        "active for several years＝数年間活動。The band started last year（昨年始まった）と合わない。",
                        "outside the campus＝キャンパス外。in the music room on campus（キャンパス内の音楽室）と反する。",
                        "seeking a new guitarist＝新しいギタリストを探している。still looking for a good guitaristが一致→正解。💡",
                    ],
                    "sourceEvidence": [
                        "I know another band whose members are still looking for a good guitarist.",
                        "The band started last year, but last week, the guitarist had to quit the band because he needed to focus on his studies.",
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
                        "send an email＝メール送信。最初に求められるのはgive me your phone numberである。",
                        "go watch a practice＝練習を見に行く。Then, you can go watchとあり、電話番号を渡した後の行動である。",
                        "provide his phone number＝電話番号を伝える。give me your phone numberが最初の具体的な行動→正解。💡",
                        "call Andrea＝Andreaに電話する。talk with them directly on the phoneのthemは紹介先のバンドを指す。",
                    ],
                    "sourceEvidence": [
                        "If you are interested, you can give me your phone number, and I will pass it to them.",
                        "Then, you can go watch one of their practices to see if you like their music.",
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
                "バハマのビッグ・メジャー・ケイは、ピッグ・ビーチとして知られる美しいビーチがある小さな島です。この島では、訪問者はビーチの近くで泳ぐ豚を見たり、時には一緒に遊んだりできます。近年、これらの豚はソーシャルメディアによって世界中で人気を集めています。このことから、その珍しい光景を見るために多くの観光客が島を訪れるようになりました。その結果、観光客の増加が豚たちに悪影響を及ぼしています。",
                "これらの豚は島に元からいた動物ではなく、どのように島へ来たのかは誰にも正確には分かりません。一つの説では、昔の船乗りたちが豚を島に残していったと言われています。別の説では、豚は壊れた船から逃げた後、島まで泳いだとされています。近くの島の農家が豚を連れてきたと考える人もいます。いずれにせよ、豚たちは、人間、特に現在の観光客が餌をくれると知ると、その場所を自分たちの住みかにしました。",
                "現在、豚を見に来る観光客が問題を起こすことがあります。観光客はさまざまな食べ物を豚に与えますが、その多くは豚の健康に良くありません。そのため、豚が病気になるおそれがあります。一部の報告では、豚がプラスチックなどの有害な物を食べたとされています。過去には、ビーチで餌をもらった豚が、餌と一緒に砂まで食べすぎて死んだ例もありました。",
                "豚を守るため、いくつかの団体と地方政府が対策を進めています。例えば、泳ぐ豚の近くでどのように適切に行動すべきかを観光客に教える啓発活動を始めました。また、ビーチを清掃し、豚への餌やりについてより厳しいルールを設けています。より環境に配慮した観光を通して、豚と環境の両方にとって状況を改善することを目指しています。こうした取り組みにより、人々は、人間が野生動物とどう関わるべきかを考え直すようにもなりました。",
            ],
            "sentencePairs": [
                [
                    "Big Major Cay in the country of the Bahamas is a small island with a beautiful beach known as Pig Beach.",
                    "バハマのビッグ・メジャー・ケイは、ピッグ・ビーチとして知られる美しいビーチがある小さな島です。",
                ],
                [
                    "On this island, visitors can see and sometimes play with pigs swimming near the beach.",
                    "この島では、訪問者はビーチの近くで泳ぐ豚を見たり、時には一緒に遊んだりできます。",
                ],
                [
                    "In recent years, these pigs have gained popularity worldwide because of social media.",
                    "近年、これらの豚はソーシャルメディアによって世界中で人気を集めています。",
                ],
                [
                    "This has led many tourists to visit the island to see this unique sight.",
                    "このことから、その珍しい光景を見るために多くの観光客が島を訪れるようになりました。",
                ],
                [
                    "As a result, this has had some negative impact on these animals.",
                    "その結果、観光客の増加が豚たちに悪影響を及ぼしています。",
                ],
                [
                    "These pigs are not native to the island, and nobody knows exactly how they arrived there.",
                    "これらの豚は島に元からいた動物ではなく、どのように島へ来たのかは誰にも正確には分かりません。",
                ],
                [
                    "One story says that old sailors left their pigs on the island.",
                    "一つの説では、昔の船乗りたちが豚を島に残していったと言われています。",
                ],
                [
                    "Another story suggests that the pigs swam to the island after escaping from a broken ship.",
                    "別の説では、豚は壊れた船から逃げた後、島まで泳いだとされています。",
                ],
                [
                    "Some people believe the pigs were brought there by farmers from a nearby island.",
                    "近くの島の農家が豚を連れてきたと考える人もいます。",
                ],
                [
                    "In any case, after these pigs learned that humans, especially tourists today, would feed them, they made the place their home.",
                    "いずれにせよ、豚たちは、人間、特に現在の観光客が餌をくれると知ると、その場所を自分たちの住みかにしました。",
                ],
                [
                    "Today, tourists who come to see the pigs sometimes cause problems.",
                    "現在、豚を見に来る観光客が問題を起こすことがあります。",
                ],
                [
                    "They often give the pigs various kinds of food, but much of it is not good for their health.",
                    "観光客はさまざまな食べ物を豚に与えますが、その多くは豚の健康に良くありません。",
                ],
                [
                    "This could make the pigs sick.",
                    "そのため、豚が病気になるおそれがあります。",
                ],
                [
                    "Some reports said that pigs ate harmful items, such as plastic.",
                    "一部の報告では、豚がプラスチックなどの有害な物を食べたとされています。",
                ],
                [
                    "In the past, some of the pigs died after people fed them on the beach, as they had also eaten too much sand with the food.",
                    "過去には、ビーチで餌をもらった豚が、餌と一緒に砂まで食べすぎて死んだ例もありました。",
                ],
                [
                    "To protect the pigs, several organizations and the local government are taking action.",
                    "豚を守るため、いくつかの団体と地方政府が対策を進めています。",
                ],
                [
                    "For example, they have started campaigns to educate tourists on how to behave properly around the swimming pigs.",
                    "例えば、泳ぐ豚の近くでどのように適切に行動すべきかを観光客に教える啓発活動を始めました。",
                ],
                [
                    "They are also cleaning up the beach and making stricter rules on feeding the pigs.",
                    "また、ビーチを清掃し、豚への餌やりについてより厳しいルールを設けています。",
                ],
                [
                    "They aim to improve the situation for both the pigs and the environment through more eco-friendly tourism.",
                    "より環境に配慮した観光を通して、豚と環境の両方にとって状況を改善することを目指しています。",
                ],
                [
                    "These events have also made people reconsider how humans should interact with wild animals.",
                    "こうした取り組みにより、人々は、人間が野生動物とどう関わるべきかを考え直すようにもなりました。",
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
                        "ソーシャルメディアによって、この島は大きく美しいビーチで有名になった。",
                        "人間と接触しない豚がそこに住んでいる。",
                        "豚が住むこの島は、観光客に非常に珍しい光景を提供している。",
                        "豚のせいで近年観光客が減少した。",
                    ],
                    "answer": 3,
                    "choiceAnalysis": [
                        "famous for its large, beautiful beach＝大きく美しいビーチで有名。SNSで人気になったのはthese pigsである。",
                        "without any contact with humans＝人と接触しない。visitors can see and play with pigsに反する。",
                        "a very unusual view＝非常に珍しい光景。unique sight（珍しい光景）と泳ぐ豚の記述が一致→正解。💡",
                        "a drop in tourists＝観光客の減少。led many tourists to visit（多くの観光客が訪れるようになった）と反する。",
                    ],
                    "sourceEvidence": [
                        "This has led many tourists to visit the island to see this unique sight.",
                        "visitors can see and sometimes play with pigs swimming near the beach.",
                    ],
                    "grammar": "💡 unique sight＝珍しい光景。gain popularity＝人気を得る。As a result以降は、観光客の増加による悪影響を述べている。",
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
                        "豚を乗せた壊れた船がそこに着いた。",
                        "もともとこの島原産だった。",
                        "船乗りが連れてきたが、置き去りにした。",
                    ],
                    "answer": 4,
                    "choiceAnalysis": [
                        "to attract tourists＝観光客を呼ぶため。豚を島へ連れてきた目的として本文には述べられていない。",
                        "a broken ship landed there＝壊れた船がそこに着いた。本文は豚が船から逃げて島まで泳いだとしている。",
                        "originally came from this island＝この島の原産。not native to the island（島の原産ではない）と反する。",
                        "sailors brought them but left them behind＝船乗りが豚を残した。old sailors left their pigsと一致→正解。💡",
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
                        "豚の健康に良くない食べ物を与えられている。",
                        "プラスチックゴミのせいで住処が破壊されている。",
                        "観光客が多すぎて住処から追い出されている。",
                    ],
                    "answer": 2,
                    "choiceAnalysis": [
                        "feel stressed when touched＝触られるとストレスを感じる。不注意な接触やストレスについて本文に記述はない。",
                        "fed food that is not good for them＝健康に良くない食べ物を与えられる。not good for their healthと一致→正解。💡",
                        "homes destroyed by plastic trash＝住みかがプラスチックごみで壊される。本文では豚がplasticを食べたと述べている。",
                        "drive them away from their homes＝住みかから追い出す。観光客に追い出されたという記述はない。",
                    ],
                    "sourceEvidence": [
                        "They often give the pigs various kinds of food, but much of it is not good for their health.",
                        "This could make the pigs sick.",
                    ],
                    "grammar": "💡 not be good for one's health＝健康に良くない。harmful items＝有害な物。cause problemsの具体例が餌の問題である。",
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
                        "政府が地元住民に豚の扱い方について情報を提供した。",
                        "政府が観光客の入島を禁止するルールを作った。",
                        "いくつかの団体が観光客に正しい接し方を教える活動をしていた。",
                        "いくつかの団体が政府の助けなしにビーチを清掃していた。",
                    ],
                    "answer": 3,
                    "choiceAnalysis": [
                        "provided locals with information＝地元住民に情報を提供。本文で教育の対象になっているのはtourists（観光客）である。",
                        "no tourists could go to the island＝観光客の入島禁止。本文はstricter rules on feedingと述べている。",
                        "teach tourists＝観光客に教える。educate tourists on how to behave properlyと一致→正解。💡",
                        "without the government＝政府の助けなし。organizations and the local government are taking actionと反する。",
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

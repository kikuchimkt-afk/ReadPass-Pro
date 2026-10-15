"""Parts 3-4 of EIKEN Grade Pre-2 2024-2 Saturday sub-venue (October 5, 2024).

Loaded by gen_pre2_2024-2-sat.py, which passes its helper functions as ``h``.
Passages, e-mail headers, stems and choices are transcribed from the rendered
booklet pages (pp. 6-9). The magazine title NME is printed in italics.
"""

from __future__ import annotations


CAMP_PARAGRAPHS = [
    "Last summer, Tom was invited on a camping trip by his friend Sam. Tom lived in a big city and had never been camping before, so he was excited about going. Although he was excited, he was worried because he did not ( 21 ). However, Sam said that he had one that was big enough for both of them to sleep in. Sam's father was going to drive them to the campsite. Sam's father also had his own tent to sleep in.",
    "It took a long time to get to the campsite, which was by a beautiful lake. They made a fire outside their tents and cooked some food for their dinner. When they had finished eating, the sky was dark. Sam's father told Tom ( 22 ). Tom was surprised. There were so many, and they were so bright. He had never seen them so clearly before because the night sky in the city was not completely dark.",
]
CAMP_TRANSLATIONS = [
    "昨年の夏、トムは友達のサムにキャンプ旅行に誘われました。トムは大都市に住んでいて、それまでキャンプをしたことがなかったので、行くのを楽しみにしていました。わくわくしていたものの、トムは（21）わけではなかったので、心配していました。しかしサムは、二人とも中で寝られるくらい大きなものを持っていると言いました。サムの父親が、二人をキャンプ場まで車で送ってくれることになっていました。サムの父親も、自分が寝るためのテントを持っていました。",
    "美しい湖のそばにあるキャンプ場に着くまでには、長い時間がかかりました。彼らはテントの外で火をおこし、夕食の料理を作りました。食べ終わったときには、空は暗くなっていました。サムの父親はトムに（22）ように言いました。トムは驚きました。数がとても多く、とても明るかったのです。都会の夜空は完全には暗くならないので、トムはそれまでこれほどはっきりと見たことがなかったのです。",
]
CAMP_PAIRS = [
    ["Last summer, Tom was invited on a camping trip by his friend Sam.", "昨年の夏、トムは友達のサムにキャンプ旅行に誘われました。"],
    ["Tom lived in a big city and had never been camping before, so he was excited about going.", "トムは大都市に住んでいて、それまでキャンプをしたことがなかったので、行くのを楽しみにしていました。"],
    ["Although he was excited, he was worried because he did not ( 21 ).", "わくわくしていたものの、トムは（21）わけではなかったので、心配していました。"],
    ["However, Sam said that he had one that was big enough for both of them to sleep in.", "しかしサムは、二人とも中で寝られるくらい大きなものを持っていると言いました。"],
    ["Sam's father was going to drive them to the campsite.", "サムの父親が、二人をキャンプ場まで車で送ってくれることになっていました。"],
    ["Sam's father also had his own tent to sleep in.", "サムの父親も、自分が寝るためのテントを持っていました。"],
    ["It took a long time to get to the campsite, which was by a beautiful lake.", "美しい湖のそばにあるキャンプ場に着くまでには、長い時間がかかりました。"],
    ["They made a fire outside their tents and cooked some food for their dinner.", "彼らはテントの外で火をおこし、夕食の料理を作りました。"],
    ["When they had finished eating, the sky was dark.", "食べ終わったときには、空は暗くなっていました。"],
    ["Sam's father told Tom ( 22 ).", "サムの父親はトムに（22）ように言いました。"],
    ["Tom was surprised.", "トムは驚きました。"],
    ["There were so many, and they were so bright.", "数がとても多く、とても明るかったのです。"],
    ["He had never seen them so clearly before because the night sky in the city was not completely dark.", "都会の夜空は完全には暗くならないので、トムはそれまでこれほどはっきりと見たことがなかったのです。"],
]

EMAIL_PARAGRAPHS = [
    "Dear Customer Service, I'm writing to you about one of your employees at the downtown store. My grandmother has been going to your store for over twenty years. She always has nice things to say about your staff. The other day, she had left her glasses at home and was having trouble getting around the store and reading things. Your employee Mark Brown was a big help.",
    "Mark noticed she was having trouble and asked her if he could help. He helped her pick out her groceries. He even helped her find cheaper options. When she was finished, he took her cart to the cash register and helped her pay. When he found out that she was taking the bus by herself, he drove her home and carried the groceries into her apartment. He then made her promise to take her glasses with her next time.",
    "Our family has enjoyed shopping at your store for a long time. However, because of Mark's help, now we are even bigger fans of your store. I'm happy to know that there are people like Mark helping my grandmother. Please let him know that my family and I really want to say thank you for what he did for her. Best regards, Joyce Dixon",
]
EMAIL_TRANSLATIONS = [
    "カスタマーサービスご担当者様。ダウンタウン店の従業員の方のことでご連絡いたします。私の祖母は20年以上、そちらのお店に通っています。祖母はいつも、店員の皆さんのことをほめています。先日、祖母は眼鏡を家に置き忘れてしまい、店内を移動したり、文字を読んだりするのに苦労していました。そちらの従業員のマーク・ブラウンさんが、大いに助けてくださいました。",
    "マークさんは祖母が困っていることに気づき、何か手伝えることはないかと声をかけてくれました。祖母が食料品を選ぶのを手伝い、さらに、もっと安い商品を見つけるのまで手伝ってくれました。祖母が買い物を終えると、カートをレジまで運び、支払いを手伝ってくれました。祖母が一人でバスに乗って帰るところだと知ると、車で家まで送り、食料品をアパートの部屋の中まで運んでくれました。そして、次からは眼鏡を持って出かけると祖母に約束させました。",
    "私たち家族は長い間、そちらのお店での買い物を楽しんできました。でも、マークさんが助けてくださったおかげで、今ではますますそちらのお店のファンになりました。マークさんのような方が祖母を助けてくださっていると知って、うれしく思います。祖母にしてくださったことに対して、家族と私が心から感謝していると、マークさんにお伝えください。よろしくお願いいたします。ジョイス・ディクソン",
]
EMAIL_PAIRS = [
    ["I'm writing to you about one of your employees at the downtown store.", "ダウンタウン店の従業員の方のことでご連絡いたします。"],
    ["My grandmother has been going to your store for over twenty years.", "私の祖母は20年以上、そちらのお店に通っています。"],
    ["She always has nice things to say about your staff.", "祖母はいつも、店員の皆さんのことをほめています。"],
    ["The other day, she had left her glasses at home and was having trouble getting around the store and reading things.", "先日、祖母は眼鏡を家に置き忘れてしまい、店内を移動したり、文字を読んだりするのに苦労していました。"],
    ["Your employee Mark Brown was a big help.", "そちらの従業員のマーク・ブラウンさんが、大いに助けてくださいました。"],
    ["Mark noticed she was having trouble and asked her if he could help.", "マークさんは祖母が困っていることに気づき、何か手伝えることはないかと声をかけてくれました。"],
    ["He helped her pick out her groceries.", "祖母が食料品を選ぶのを手伝ってくれました。"],
    ["He even helped her find cheaper options.", "さらに、もっと安い商品を見つけるのまで手伝ってくれました。"],
    ["When she was finished, he took her cart to the cash register and helped her pay.", "祖母が買い物を終えると、カートをレジまで運び、支払いを手伝ってくれました。"],
    ["When he found out that she was taking the bus by herself, he drove her home and carried the groceries into her apartment.", "祖母が一人でバスに乗って帰るところだと知ると、車で家まで送り、食料品をアパートの部屋の中まで運んでくれました。"],
    ["He then made her promise to take her glasses with her next time.", "そして、次からは眼鏡を持って出かけると祖母に約束させました。"],
    ["Our family has enjoyed shopping at your store for a long time.", "私たち家族は長い間、そちらのお店での買い物を楽しんできました。"],
    ["However, because of Mark's help, now we are even bigger fans of your store.", "でも、マークさんが助けてくださったおかげで、今ではますますそちらのお店のファンになりました。"],
    ["I'm happy to know that there are people like Mark helping my grandmother.", "マークさんのような方が祖母を助けてくださっていると知って、うれしく思います。"],
    ["Please let him know that my family and I really want to say thank you for what he did for her.", "祖母にしてくださったことに対して、家族と私が心から感謝していると、マークさんにお伝えください。"],
]

MAGAZINE_PARAGRAPHS = [
    "The invention of the Internet caused many changes in society. Some changes were positive, such as being able to access news and information quickly. However, the Internet also brought some negative changes. The magazine publishing industry especially suffered from these changes. Many people stopped buying magazines when they realized they could read the same information online. Since 2012, the number of magazine companies in the United States has dropped by over 30 percent, and many magazines are no longer published at all.",
    "To survive, many magazine companies have stopped printing their magazines and publish online instead. Readers pay to access the magazine through their smartphones or computers. This is more convenient for readers because they no longer have to buy magazines from stores. It is also cheaper for the magazine company because there is no need for printing. Sales of online magazines are still high because people trust magazines more than blogs or social media.",
    "Another way for print magazines to survive is by improving quality. A good example is the UK music magazine NME. This magazine stopped being printed in 2018 because sales were too low. However, in 2023, a new version was published again with a higher price, better content, and more pages. The magazine was printed in small numbers and published only every two months. The new style of the magazine is popular with music fans because the magazine is considered special and rare. NME has become a valuable item for people who collect magazines.",
    "The content of a magazine also affects its popularity. Magazines about fashion or famous people did not survive because that information can be found easily on social media. Print magazines that are still successful are those that are written by experts and offer the readers something that cannot be found easily online. These are mainly magazines about business, news, and other global issues.",
]
MAGAZINE_TRANSLATIONS = [
    "インターネットの発明は、社会に多くの変化をもたらしました。ニュースや情報にすばやくアクセスできるようになったことなど、よい変化もありました。しかし、インターネットは悪い変化ももたらしました。特に雑誌出版業界は、こうした変化によって大きな打撃を受けました。多くの人が、同じ情報をインターネットで読めると気づいて、雑誌を買わなくなったのです。2012年以降、アメリカの雑誌会社の数は30パーセント以上減り、多くの雑誌がまったく発行されなくなりました。",
    "生き残るために、多くの雑誌会社は雑誌の印刷をやめ、代わりにオンラインで発行しています。読者は料金を払い、スマートフォンやコンピューターで雑誌を閲覧します。読者はもう店で雑誌を買う必要がないので、これは読者にとってより便利です。また、印刷の必要がないので、雑誌会社にとっても費用が安く済みます。人々はブログやソーシャルメディアよりも雑誌を信頼しているので、オンライン雑誌の売り上げは今でも高いのです。",
    "紙の雑誌が生き残るもう一つの方法は、質を高めることです。そのよい例が、イギリスの音楽雑誌『NME』です。この雑誌は売り上げが少なすぎたため、2018年に印刷されなくなりました。しかし2023年に、より高い価格で、よりよい内容と、より多くのページを備えた新しい版が再び発行されました。この雑誌は少部数だけ印刷され、2か月に1回しか発行されませんでした。特別で珍しいものと考えられているため、新しい形のこの雑誌は音楽ファンに人気があります。『NME』は、雑誌を収集する人々にとって価値のある品になっています。",
    "雑誌の内容も、その人気に影響します。ファッションや有名人についての雑誌は、そうした情報がソーシャルメディアで簡単に見つかるため、生き残れませんでした。今でも成功している紙の雑誌は、専門家によって書かれ、インターネットでは簡単に見つからないものを読者に提供している雑誌です。それらは主に、ビジネスやニュース、そのほかの世界的な問題を扱う雑誌です。",
]
MAGAZINE_PAIRS = [
    ["The invention of the Internet caused many changes in society.", "インターネットの発明は、社会に多くの変化をもたらしました。"],
    ["Some changes were positive, such as being able to access news and information quickly.", "ニュースや情報にすばやくアクセスできるようになったことなど、よい変化もありました。"],
    ["However, the Internet also brought some negative changes.", "しかし、インターネットは悪い変化ももたらしました。"],
    ["The magazine publishing industry especially suffered from these changes.", "特に雑誌出版業界は、こうした変化によって大きな打撃を受けました。"],
    ["Many people stopped buying magazines when they realized they could read the same information online.", "多くの人が、同じ情報をインターネットで読めると気づいて、雑誌を買わなくなったのです。"],
    ["Since 2012, the number of magazine companies in the United States has dropped by over 30 percent, and many magazines are no longer published at all.", "2012年以降、アメリカの雑誌会社の数は30パーセント以上減り、多くの雑誌がまったく発行されなくなりました。"],
    ["To survive, many magazine companies have stopped printing their magazines and publish online instead.", "生き残るために、多くの雑誌会社は雑誌の印刷をやめ、代わりにオンラインで発行しています。"],
    ["Readers pay to access the magazine through their smartphones or computers.", "読者は料金を払い、スマートフォンやコンピューターで雑誌を閲覧します。"],
    ["This is more convenient for readers because they no longer have to buy magazines from stores.", "読者はもう店で雑誌を買う必要がないので、これは読者にとってより便利です。"],
    ["It is also cheaper for the magazine company because there is no need for printing.", "また、印刷の必要がないので、雑誌会社にとっても費用が安く済みます。"],
    ["Sales of online magazines are still high because people trust magazines more than blogs or social media.", "人々はブログやソーシャルメディアよりも雑誌を信頼しているので、オンライン雑誌の売り上げは今でも高いのです。"],
    ["Another way for print magazines to survive is by improving quality.", "紙の雑誌が生き残るもう一つの方法は、質を高めることです。"],
    ["A good example is the UK music magazine NME.", "そのよい例が、イギリスの音楽雑誌『NME』です。"],
    ["This magazine stopped being printed in 2018 because sales were too low.", "この雑誌は売り上げが少なすぎたため、2018年に印刷されなくなりました。"],
    ["However, in 2023, a new version was published again with a higher price, better content, and more pages.", "しかし2023年に、より高い価格で、よりよい内容と、より多くのページを備えた新しい版が再び発行されました。"],
    ["The magazine was printed in small numbers and published only every two months.", "この雑誌は少部数だけ印刷され、2か月に1回しか発行されませんでした。"],
    ["The new style of the magazine is popular with music fans because the magazine is considered special and rare.", "特別で珍しいものと考えられているため、新しい形のこの雑誌は音楽ファンに人気があります。"],
    ["NME has become a valuable item for people who collect magazines.", "『NME』は、雑誌を収集する人々にとって価値のある品になっています。"],
    ["The content of a magazine also affects its popularity.", "雑誌の内容も、その人気に影響します。"],
    ["Magazines about fashion or famous people did not survive because that information can be found easily on social media.", "ファッションや有名人についての雑誌は、そうした情報がソーシャルメディアで簡単に見つかるため、生き残れませんでした。"],
    ["Print magazines that are still successful are those that are written by experts and offer the readers something that cannot be found easily online.", "今でも成功している紙の雑誌は、専門家によって書かれ、インターネットでは簡単に見つからないものを読者に提供している雑誌です。"],
    ["These are mainly magazines about business, news, and other global issues.", "それらは主に、ビジネスやニュース、そのほかの世界的な問題を扱う雑誌です。"],
]


def build_part3(h) -> dict:
    pq = h.passage_question
    return {
        "name": "大問3",
        "nameEn": "Part 3",
        "type": "passage-fill",
        "instruction": "次の英文を読み，その文意にそって(21)と(22)の(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選びなさい。",
        "passages": [
            {
                "label": "",
                "title": "First Camping Trip",
                "paragraphs": CAMP_PARAGRAPHS,
                "translations": CAMP_TRANSLATIONS,
                "sentencePairs": CAMP_PAIRS,
                "questions": [
                    pq(
                        21,
                        None,
                        None,
                        [
                            "like camping trips",
                            "plan the trip himself",
                            "have his own tent",
                            "know the way there",
                        ],
                        [
                            "キャンプ旅行が好きだ",
                            "自分で旅行を計画する",
                            "自分のテントを持っている",
                            "そこへの行き方を知っている",
                        ],
                        3,
                        [
                            "トムは初めてのキャンプを楽しみにしていたので、キャンプ旅行が好きではないという内容は合わない。次の文のone（サムが持っているもの）にもつながらない",
                            "自分で旅行を計画しないことは心配の理由にならず、次の文でサムが『大きなものを持っている』と答える流れにも合わない",
                            "自分のテントを持っている。次の文でサムが、二人とも中で寝られるくらい大きなもの（one）を持っていると言っているので、oneがtentを指し、トムはテントを持っていなかったとわかる",
                            "行き方を知らないことが心配なら、Howeverのあとで『二人とも中で寝られるくらい大きなもの』を持っているという答えにならない",
                        ],
                        "💡 oneは前に出た名詞と同じ種類のもの（ここではtent）を指す代名詞。big enough for A to do＝Aが～できるほど大きい。Although ～＝～だけれども。",
                    ),
                    pq(
                        22,
                        None,
                        None,
                        [
                            "to look up at the stars",
                            "to eat more vegetables",
                            "to get some warmer clothes",
                            "to help him wash the dishes",
                        ],
                        [
                            "星を見上げる",
                            "野菜をもっと食べる",
                            "もっと暖かい服を取ってくる",
                            "皿洗いを手伝う",
                        ],
                        1,
                        [
                            "星を見上げるように。直後のThere were so many, and they were so bright.や、都会の夜空は完全には暗くならないという説明から、空のたくさんの星を見たとわかる",
                            "野菜をもっと食べるように言われても、驚いて『数がとても多く、とても明るかった』と述べる流れにならない",
                            "暖かい服を取ってくることは、『とても明るかった』『夜空』という後の説明と結びつかない",
                            "皿洗いの手伝いは、後に続く夜空の話と関係がない",
                        ],
                        "💡 tell 人 to do＝人に～するように言う。look up at ～＝～を見上げる。had never seen＝（その時まで）一度も見たことがなかった（過去完了）。",
                    ),
                ],
            }
        ],
    }


def build_part4(h) -> dict:
    pq = h.passage_question
    return {
        "name": "大問4",
        "nameEn": "Part 4",
        "type": "reading-comprehension",
        "instruction": "次の英文Ａ，Ｂの内容に関して，(23)から(29)までの質問に対して最も適切なもの，または文を完成させるのに最も適切なものを1，2，3，4の中から一つ選びなさい。",
        "passages": [
            {
                "label": "A",
                "title": "Helpful employee",
                "format": "email",
                "meta": {
                    "from": "Joyce Dixon <joyce_dixon@goodmail.com>",
                    "to": "Customer Service <cusserv@tennmart.com>",
                    "date": "October 5",
                    "subject": "Helpful employee",
                },
                "paragraphs": EMAIL_PARAGRAPHS,
                "translations": EMAIL_TRANSLATIONS,
                "sentencePairs": EMAIL_PAIRS,
                "questions": [
                    pq(
                        23,
                        "Why is Joyce Dixon writing this e-mail?",
                        "ジョイス・ディクソンはなぜこのメールを書いているのですか。",
                        [
                            "To ask if the store has her grandmother's glasses.",
                            "To remind the store it has a long history.",
                            "She wants to know the name of an employee.",
                            "A staff member did something special.",
                        ],
                        [
                            "店に祖母の眼鏡があるかどうか尋ねるため。",
                            "店に長い歴史があることを思い出させるため。",
                            "ある従業員の名前を知りたいから。",
                            "ある店員が特別なことをしてくれたから。",
                        ],
                        4,
                        [
                            "祖母は眼鏡を家に置き忘れた（had left her glasses at home）のであり、店に忘れたとは書かれていない",
                            "祖母が20年以上通っていることや家族が長く買い物をしていることは書かれているが、店の歴史を伝えるためのメールではない",
                            "従業員の名前はMark Brownとすでに書いており、名前を尋ねてはいない",
                            "ある店員が特別なことをしてくれたから。従業員のマークが祖母の買い物を手伝い、車で家まで送ってくれたことを伝え、本人に感謝を伝えてほしいと書いている",
                        ],
                        "💡 Why ～?の答えは、To＋動詞（～するため）の形と、主語＋動詞（～だから）の形のどちらもある。メールの目的は、第1段落のI'm writing to you about ～とメール全体の内容から判断する。a staff member＝one of your employees。",
                    ),
                    pq(
                        24,
                        "Mark Brown helped Joyce's grandmother",
                        "マーク・ブラウンがジョイスの祖母を手伝ったのは",
                        [
                            "shop for her friend's groceries.",
                            "catch the bus to her home.",
                            "find items with lower prices.",
                            "buy some new glasses.",
                        ],
                        [
                            "友人の食料品を買うこと。",
                            "家に帰るバスに乗ること。",
                            "より安い値段の品物を見つけること。",
                            "新しい眼鏡を買うこと。",
                        ],
                        3,
                        [
                            "マークが手伝ったのは祖母自身の食料品（her groceries）を選ぶことで、友人の食料品を買ったとは書かれていない",
                            "祖母が一人でバスに乗ると知ったマークは、車で家まで送っている。バスに乗るのを手伝ったわけではない",
                            "より安い値段の品物を見つけること。He even helped her find cheaper options.の言い換え",
                            "祖母は眼鏡を家に置き忘れていただけで、新しい眼鏡を買うのを手伝ったとは書かれていない",
                        ],
                        "💡 cheaper options（より安い選択肢）→ items with lower prices（より低い値段の品物）の言い換え。help 人 do＝人が～するのを手伝う。",
                    ),
                    pq(
                        25,
                        "What does Joyce want the store to do for her and her family?",
                        "ジョイスは店に、自分と家族のために何をしてほしいと思っていますか。",
                        [
                            "Give them some coupons.",
                            "Thank Mark for them.",
                            "Watch her grandmother for them.",
                            "Introduce them to Mark.",
                        ],
                        [
                            "家族にクーポンをくれる。",
                            "家族に代わってマークにお礼を言う。",
                            "家族に代わって祖母を見守る。",
                            "家族をマークに紹介する。",
                        ],
                        2,
                        [
                            "クーポンを求めるという記述はない",
                            "家族に代わってマークにお礼を言う。Please let him know that my family and I really want to say thank you ...の言い換え",
                            "マークのような人が祖母を助けてくれてうれしいと述べているだけで、祖母を見守るよう店に頼んではいない",
                            "マークを紹介してほしいとは書かれていない。頼んでいるのは、感謝の気持ちを本人に伝えること",
                        ],
                        "💡 want 人 to do＝人に～してほしい。let 人 know＝人に知らせる。for them＝彼らに代わって。Please let him know that ... want to say thank you → Thank Mark for them.の言い換え。",
                    ),
                ],
            },
            {
                "label": "B",
                "title": "Magazines in the Digital Age",
                "paragraphs": MAGAZINE_PARAGRAPHS,
                "translations": MAGAZINE_TRANSLATIONS,
                "sentencePairs": MAGAZINE_PAIRS,
                "questions": [
                    pq(
                        26,
                        "The arrival of the Internet caused",
                        "インターネットの登場によって起きたのは",
                        [
                            "the number of magazine companies in the United States to decrease.",
                            "a rise in the number of people interested in writing for magazines.",
                            "people to read different kinds of magazines than before.",
                            "positive changes to the magazine industry in the United States.",
                        ],
                        [
                            "アメリカの雑誌会社の数が減ったこと。",
                            "雑誌に記事を書くことに興味を持つ人の数が増えたこと。",
                            "人々が以前とは違う種類の雑誌を読むようになったこと。",
                            "アメリカの雑誌業界によい変化が起きたこと。",
                        ],
                        1,
                        [
                            "アメリカの雑誌会社の数が減ったこと。Since 2012, the number of magazine companies in the United States has dropped by over 30 percentの言い換え（has dropped→to decrease）",
                            "雑誌に記事を書きたい人が増えたという記述はない",
                            "第4段落は生き残った雑誌の種類を説明しているが、インターネットによって人々が以前と違う種類の雑誌を読むようになったとは書かれていない",
                            "雑誌出版業界はこうした変化に苦しんだ（especially suffered from these changes）とあり、よい変化が起きたという内容は逆",
                        ],
                        "💡 cause A to do＝Aに～させる・Aが～する原因となる。has dropped（減った）→ to decrease（減少する）の言い換え。arrival（登場）は本文のinvention（発明）に対応する。",
                    ),
                    pq(
                        27,
                        "What is one reason why people read magazines online?",
                        "人々がオンラインで雑誌を読む理由の一つは何ですか。",
                        [
                            "They prefer to read magazines on a device for free.",
                            "They want to help the magazine company's work.",
                            "They think the online version provides more articles and information.",
                            "They believe the information is more likely to be true than other sources.",
                        ],
                        [
                            "端末で無料で雑誌を読むほうが好きだから。",
                            "雑誌会社の仕事を助けたいから。",
                            "オンライン版のほうが多くの記事や情報を提供していると思うから。",
                            "ほかの情報源よりも、その情報のほうが正しい可能性が高いと信じているから。",
                        ],
                        4,
                        [
                            "Readers pay to access the magazineとあり、オンライン雑誌も料金を払って読むので、無料ではない",
                            "雑誌会社を助けたいという理由は書かれていない。印刷が不要で安く済むのは会社側の利点",
                            "オンライン版のほうが記事や情報が多いとは書かれていない",
                            "ほかの情報源よりも、その情報のほうが正しい可能性が高いと信じているから。people trust magazines more than blogs or social mediaの言い換え",
                        ],
                        "💡 trust A more than B（BよりAを信頼する）→ believe the information is more likely to be true than other sources（ほかの情報源より正しい可能性が高いと信じる）の言い換え。be likely to do＝～しそうだ。",
                    ),
                    pq(
                        28,
                        "One reason the new NME magazine has become popular is that",
                        "新しい『NME』が人気になった理由の一つは",
                        [
                            "the company made it cheaper to buy.",
                            "the new version is smaller and easier to read.",
                            "there are only limited numbers available.",
                            "it is published more often than before.",
                        ],
                        [
                            "会社が安く買えるようにしたこと。",
                            "新しい版がより小さく、読みやすいこと。",
                            "限られた数しか手に入らないこと。",
                            "以前より頻繁に発行されていること。",
                        ],
                        3,
                        [
                            "新しい版はa higher price（より高い価格）で発行されたので、安くしたという内容は逆",
                            "新しい版はmore pages（より多くのページ）になったとあり、小さく読みやすくなったとは書かれていない",
                            "限られた数しか手に入らないこと。printed in small numbers（少部数で印刷された）や、considered special and rare（特別で珍しいと考えられている）の言い換え",
                            "published only every two months（2か月に1回だけ発行）とあり、以前より頻繁に発行されているとは書かれていない",
                        ],
                        "💡 printed in small numbers（少部数で印刷された）＋rare（珍しい）→ only limited numbers available（限られた数しか手に入らない）の言い換え。One reason ～ is that ...＝～の理由の一つは…ということだ。",
                    ),
                    pq(
                        29,
                        "What kinds of magazines are still popular today?",
                        "今でも人気があるのはどんな種類の雑誌ですか。",
                        [
                            "Magazines written by specialists about serious topics.",
                            "Magazines discussing the entertainment world.",
                            "Magazines containing similar information to websites.",
                            "Magazines that make good use of social media.",
                        ],
                        [
                            "専門家が書いた、まじめな話題についての雑誌。",
                            "芸能界を取り上げる雑誌。",
                            "ウェブサイトと似た情報を載せた雑誌。",
                            "ソーシャルメディアをうまく活用している雑誌。",
                        ],
                        1,
                        [
                            "専門家が書いた、まじめな話題についての雑誌。written by experts → written by specialists、business, news, and other global issues → serious topicsの言い換え",
                            "ファッションや有名人についての雑誌は生き残れなかったとあり、芸能界を取り上げる雑誌が今も人気だとは書かれていない",
                            "今でも成功しているのはインターネットで簡単に見つからないものを提供する雑誌で、ウェブサイトと似た情報を載せた雑誌とは逆",
                            "ソーシャルメディアを活用している雑誌という記述はない。ソーシャルメディアで情報が見つかる分野の雑誌は生き残れなかったと書かれている",
                        ],
                        "💡 experts＝specialists（専門家）。business, news, and other global issues（ビジネス・ニュース・世界的な問題）をserious topics（まじめな話題）とまとめて言い換えている。still successful → still popularの言い換え。",
                    ),
                ],
            },
        ],
    }

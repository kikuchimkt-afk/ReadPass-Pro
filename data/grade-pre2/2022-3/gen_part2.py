"""Generate sections 2-3 (大問3 + 大問4) and merge with Part 1, add vocabulary"""
import json, os

# Load Part 1
base = r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade-pre2\2022-3"
data = json.load(open(os.path.join(base, "_part1.json"), "r", encoding="utf-8"))

# =====================================================
# Section 2: 大問3（passage-fill型・旧形式 2パッセージ A:2問 B:3問）
# =====================================================
section3 = {
    "name": "大問3",
    "nameEn": "Part 3",
    "type": "passage-fill",
    "instruction": "次の英文A，Bを読み，その文意にそって(26)から(30)までの(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選びなさい。",
    "passages": [
        {
            "label": "A",
            "title": "The Costume Party",
            "paragraphs": [
                "The other day, Ryan invited Heather to his birthday party. Ryan said it was a costume party. He asked Heather to dress as her favorite cartoon character. Heather's favorite character is a witch who rides a broom and delivers mail. She wears a blue dress and a red ribbon in her hair. Heather did not have a blue dress, but her mom had some blue cloth. She told Heather ( 26 ) instead.",
                "Heather helped her mother, and soon, she had a dress exactly like the one the witch wears. On the day of Ryan's party, Heather remembered that she also needed a broom. She asked her mother, but her mother said that she did not have one. Then, Heather remembered seeing her neighbor, Mr. Jones, using one to sweep his yard. Heather ran to Mr. Jones's house to ask if she could ( 27 ). Luckily, Mr. Jones said yes. Heather was very happy because her costume was complete."
            ],
            "translations": [
                "先日、ライアンがヘザーを誕生日パーティーに招待した。ライアンはそれが仮装パーティーだと言った。彼はヘザーにお気に入りの漫画キャラクターに扮するよう頼んだ。ヘザーのお気に入りのキャラクターはほうきに乗って郵便を届ける魔女だ。その魔女は青いドレスと髪に赤いリボンをつけている。ヘザーは青いドレスを持っていなかったが、母親が青い布を持っていた。母親はヘザーに代わりに( 26 )と言った。",
                "ヘザーは母親を手伝い、まもなく魔女が着ているのとまったく同じドレスができた。ライアンのパーティーの日、ヘザーはほうきも必要だと思い出した。母親に聞いたが、持っていないと言われた。すると、ヘザーは隣人のジョーンズさんが庭を掃くのにほうきを使っているのを見たことを思い出した。ヘザーはジョーンズさんの家に走って行き、( 27 )かどうか聞いた。幸い、ジョーンズさんは承諾してくれた。ヘザーは衣装が完成したのでとても嬉しかった。"
            ],
            "sentencePairs": [
                ["The other day, Ryan invited Heather to his birthday party.", "先日、ライアンがヘザーを誕生日パーティーに招待した。"],
                ["Ryan said it was a costume party.", "ライアンはそれが仮装パーティーだと言った。"],
                ["He asked Heather to dress as her favorite cartoon character.", "彼はヘザーにお気に入りの漫画キャラクターに扮するよう頼んだ。"],
                ["Heather's favorite character is a witch who rides a broom and delivers mail.", "ヘザーのお気に入りのキャラクターはほうきに乗って郵便を届ける魔女だ。"],
                ["She wears a blue dress and a red ribbon in her hair.", "その魔女は青いドレスと髪に赤いリボンをつけている。"],
                ["Heather did not have a blue dress, but her mom had some blue cloth.", "ヘザーは青いドレスを持っていなかったが、母親が青い布を持っていた。"],
                ["Heather helped her mother, and soon, she had a dress exactly like the one the witch wears.", "ヘザーは母親を手伝い、まもなく魔女が着ているのとまったく同じドレスができた。"],
                ["On the day of Ryan's party, Heather remembered that she also needed a broom.", "ライアンのパーティーの日、ヘザーはほうきも必要だと思い出した。"],
                ["She asked her mother, but her mother said that she did not have one.", "母親に聞いたが、持っていないと言われた。"],
                ["Then, Heather remembered seeing her neighbor, Mr. Jones, using one to sweep his yard.", "すると、ヘザーは隣人のジョーンズさんが庭を掃くのにほうきを使っているのを見たことを思い出した。"],
                ["Luckily, Mr. Jones said yes.", "幸い、ジョーンズさんは承諾してくれた。"],
                ["Heather was very happy because her costume was complete.", "ヘザーは衣装が完成したのでとても嬉しかった。"]
            ],
            "questions": [
                {
                    "number": 26,
                    "choices": ["that she should stay home", "that they could make one", "to wear a green one", "to choose another character"],
                    "choiceTranslations": ["家にいるべきだ", "一つ作ることができる", "緑のを着る", "別のキャラクターを選ぶ"],
                    "answer": 2,
                    "choiceAnalysis": [
                        "家にいるべき→パーティーに行く文脈と矛盾",
                        "一つ作ることができる→正解。💡 青い布があるのでドレスを手作りできる。次の文でヘザーが母親を手伝いドレスが完成した",
                        "緑のを着る→魔女のドレスは青色なので矛盾",
                        "別のキャラクターを選ぶ→布を持っていることが解決策にならない"
                    ],
                    "grammar": "💡 tell someone (that) ～＝～と言う。instead＝代わりに。cloth＝布（不可算名詞）"
                },
                {
                    "number": 27,
                    "choices": ["borrow it", "hide there", "help him", "get her ball"],
                    "choiceTranslations": ["それを借りる", "そこに隠れる", "彼を手伝う", "彼女のボールを取る"],
                    "answer": 1,
                    "choiceAnalysis": [
                        "それを借りる→正解。💡 ジョーンズさんのほうきを借りてコスチュームを完成させる。itはbroomを指す",
                        "そこに隠れる→仮装パーティーの文脈に合わない",
                        "彼を手伝う→ほうきが必要な状況と無関係",
                        "彼女のボールを取る→ほうきの話題と無関係"
                    ],
                    "grammar": "💡 ask if ～＝～かどうか尋ねる。borrow＝借りる（無料で一時的に）。lend＝貸す"
                }
            ]
        },
        {
            "label": "B",
            "title": "Escher's Amazing Art",
            "paragraphs": [
                "Maurits Cornelis Escher was born in the Netherlands in 1898. After leaving high school, he went to college to study how to design buildings. However, he soon realized that he was not ( 28 ). In fact, he liked designing things that could not be built. He decided to study graphic art instead. A graphic artist is an artist who uses imagination, math, and tools like rulers to produce pictures.",
                "After Escher graduated, he traveled for a long time in Italy. He really liked the countryside and the old buildings there. He often drew the places that he saw there in his pictures. He also visited Spain. There, he went to a castle where the walls were covered with interesting patterns. They gave him ideas for his own patterns, and he would sometimes use the shapes of animals in these designs. His experiences ( 29 ) had a very big effect on his art.",
                "Escher's pictures often show things that are impossible in real life. In the picture Ascending and Descending, people are climbing stairs that return to the place where they started. In Drawing Hands, two hands are holding pencils and drawing each other. Escher's unusual art is ( 30 ). For example, about 200,000 visitors went to see an exhibition of his work in Tokyo in 2018. People in many countries like his pictures because they are beautiful and they make people think."
            ],
            "translations": [
                "マウリッツ・コルネリス・エッシャーは1898年にオランダで生まれた。高校を卒業した後、建物の設計を学ぶために大学に進んだ。しかし、彼はすぐに自分が( 28 )ことに気づいた。実際、彼は建てることができないものを設計するのが好きだった。代わりにグラフィックアートを学ぶことにした。グラフィックアーティストとは、想像力、数学、定規などの道具を使って絵を制作するアーティストのことである。",
                "エッシャーは卒業後、長い間イタリアを旅行した。彼はそこの田園風景や古い建物がとても気に入った。そこで見た場所をよく絵に描いた。彼はスペインも訪れた。そこでは壁が面白い模様で覆われた城を訪問した。それらは彼独自の模様のアイデアを与え、動物の形をデザインに使うこともあった。彼の( 29 )での経験は、彼の芸術に非常に大きな影響を与えた。",
                "エッシャーの絵はしばしば現実にはあり得ないものを描いている。「上昇と下降」という作品では、人々が出発点に戻ってくる階段を登っている。「描く手」では、2つの手が鉛筆を持ち、互いを描いている。エッシャーの独特な芸術は( 30 )。例えば、2018年に東京で開かれた彼の作品展には約20万人の来場者が訪れた。多くの国の人々が彼の絵を好むのは、それらが美しく、人々に考えさせるからである。"
            ],
            "sentencePairs": [
                ["Maurits Cornelis Escher was born in the Netherlands in 1898.", "マウリッツ・コルネリス・エッシャーは1898年にオランダで生まれた。"],
                ["After leaving high school, he went to college to study how to design buildings.", "高校を卒業した後、建物の設計を学ぶために大学に進んだ。"],
                ["However, he soon realized that he was not ( 28 ).", "しかし、彼はすぐに自分が( 28 )ことに気づいた。"],
                ["In fact, he liked designing things that could not be built.", "実際、彼は建てることができないものを設計するのが好きだった。"],
                ["He decided to study graphic art instead.", "代わりにグラフィックアートを学ぶことにした。"],
                ["A graphic artist is an artist who uses imagination, math, and tools like rulers to produce pictures.", "グラフィックアーティストとは、想像力、数学、定規などの道具を使って絵を制作するアーティストのことである。"],
                ["After Escher graduated, he traveled for a long time in Italy.", "エッシャーは卒業後、長い間イタリアを旅行した。"],
                ["He really liked the countryside and the old buildings there.", "彼はそこの田園風景や古い建物がとても気に入った。"],
                ["He often drew the places that he saw there in his pictures.", "そこで見た場所をよく絵に描いた。"],
                ["He also visited Spain.", "彼はスペインも訪れた。"],
                ["There, he went to a castle where the walls were covered with interesting patterns.", "そこでは壁が面白い模様で覆われた城を訪問した。"],
                ["They gave him ideas for his own patterns, and he would sometimes use the shapes of animals in these designs.", "それらは彼独自の模様のアイデアを与え、動物の形をデザインに使うこともあった。"],
                ["Escher's pictures often show things that are impossible in real life.", "エッシャーの絵はしばしば現実にはあり得ないものを描いている。"],
                ["In the picture Ascending and Descending, people are climbing stairs that return to the place where they started.", "「上昇と下降」という作品では、人々が出発点に戻ってくる階段を登っている。"],
                ["In Drawing Hands, two hands are holding pencils and drawing each other.", "「描く手」では、2つの手が鉛筆を持ち、互いを描いている。"],
                ["For example, about 200,000 visitors went to see an exhibition of his work in Tokyo in 2018.", "例えば、2018年に東京で開かれた彼の作品展には約20万人の来場者が訪れた。"],
                ["People in many countries like his pictures because they are beautiful and they make people think.", "多くの国の人々が彼の絵を好むのは、それらが美しく、人々に考えさせるからである。"]
            ],
            "questions": [
                {
                    "number": 28,
                    "choices": ["a creative person", "a clever teacher", "interested in construction", "good at drawing"],
                    "choiceTranslations": ["創造的な人", "賢い先生", "建設に興味がある", "絵が上手"],
                    "answer": 3,
                    "choiceAnalysis": [
                        "創造的な人→エッシャーは創造的だったので矛盾",
                        "賢い先生→教師についての文脈ではない",
                        "建設に興味がある→正解。💡 建てられないものの設計が好きだったので、実際の建設には興味がなかった。次の文のIn factが決め手",
                        "絵が上手→グラフィックアートを学んだのだから絵は上手"
                    ],
                    "grammar": "💡 be interested in ～＝～に興味がある。construction＝建設。realize (that) ～＝～に気づく"
                },
                {
                    "number": 29,
                    "choices": ["in these two countries", "from his early childhood", "of working with his father", "while learning new languages"],
                    "choiceTranslations": ["これら2つの国での", "幼少期からの", "父親と働いた", "新しい言語を学びながらの"],
                    "answer": 1,
                    "choiceAnalysis": [
                        "これら2つの国での→正解。💡 前段落のイタリアとスペインが「2つの国」。そこでの経験が芸術に影響を与えた",
                        "幼少期からの→イタリアとスペインの旅は卒業後の話",
                        "父親と働いた→父親についての言及はない",
                        "新しい言語を学びながらの→言語学習の言及はない"
                    ],
                    "grammar": "💡 have a big effect on ～＝～に大きな影響を与える。these two countries＝これら2つの国（イタリアとスペイン）"
                },
                {
                    "number": 30,
                    "choices": ["all kept in one place", "popular around the world", "not for sale anymore", "not nice to look at"],
                    "choiceTranslations": ["すべて1か所に保管されている", "世界中で人気がある", "もう売りに出されていない", "見て美しくない"],
                    "answer": 2,
                    "choiceAnalysis": [
                        "すべて1か所に保管→東京での展覧会は1か所保管と矛盾",
                        "世界中で人気がある→正解。💡 東京で20万人来場、多くの国の人が好むという次の文が根拠",
                        "もう売りに出されていない→人気の例として展覧会を挙げる文脈に合わない",
                        "見て美しくない→beautiful と明記されており矛盾"
                    ],
                    "grammar": "💡 popular around the world＝世界中で人気がある。exhibition＝展覧会。unusual＝珍しい、独特な"
                }
            ]
        }
    ]
}

# =====================================================
# Section 3: 大問4（reading-comprehension型・A:email3問 B:4問）
# =====================================================
section4 = {
    "name": "大問4",
    "nameEn": "Part 4",
    "type": "reading-comprehension",
    "instruction": "次の英文A，Bの内容に関して，(31)から(37)までの質問に対して最も適切なもの，または文を完成させるのに最も適切なものを1，2，3，4の中から一つ選びなさい。",
    "passages": [
        {
            "label": "A",
            "title": "Cooking Club Recipes",
            "format": "email",
            "meta": {
                "from": "Ariana Smith",
                "to": "Jane Jones",
                "date": "January 22",
                "subject": "Cooking club recipes"
            },
            "paragraphs": [
                "I really enjoy our weekly cooking club meetings at the community center. All the members are so friendly. It's nice that the members take turns teaching each other recipes. I get nervous when it's my turn to teach, but I'm always happy afterward. Also, I've learned how to make a really wide variety of dishes this way. It's much better than having just one cooking teacher.",
                "I was telling my friend David about our meetings. David works as a photographer and designer for a company that publishes books. He suggested that the cooking club members make a book of our favorite recipes. He said that he would help us to do it. We could make something to remember our meetings. A book of recipes would also be a great gift for friends and family members.",
                "I really like his idea. What do you think? We could ask each of the members to prepare recipes for a snack, a salad, a soup, a main dish, and a dessert. We can then choose the ones that sound the best and make them during our meetings. David said that he would be happy to come and take pictures of our food. He'd like to try some of it, too!"
            ],
            "translations": [
                "コミュニティセンターでの毎週の料理クラブの集まりがとても楽しいです。メンバーみんなとてもフレンドリーです。メンバーが交代でレシピを教え合うのが素敵ですね。自分が教える番になると緊張しますが、終わった後はいつも嬉しいです。また、この方法で本当にさまざまな料理の作り方を学びました。料理の先生が1人だけよりずっと良いです。",
                "友人のデイビッドに私たちの集まりのことを話していました。デイビッドは本を出版する会社でカメラマンとデザイナーとして働いています。彼は料理クラブのメンバーでお気に入りレシピの本を作ることを提案しました。彼が手伝ってくれると言ってくれました。集まりを記念するものを作れるし、レシピ本は友人や家族への素敵な贈り物にもなります。",
                "彼のアイデアがとても気に入りました。どう思いますか？各メンバーにおやつ、サラダ、スープ、メインディッシュ、デザートのレシピを準備してもらい、一番良さそうなものを選んで集まりの時に作ることができます。デイビッドは喜んで来て料理の写真を撮ると言っていました。料理を少し味見もしたいそうです！"
            ],
            "sentencePairs": [
                ["I really enjoy our weekly cooking club meetings at the community center.", "コミュニティセンターでの毎週の料理クラブの集まりがとても楽しいです。"],
                ["All the members are so friendly.", "メンバーみんなとてもフレンドリーです。"],
                ["It's nice that the members take turns teaching each other recipes.", "メンバーが交代でレシピを教え合うのが素敵ですね。"],
                ["I get nervous when it's my turn to teach, but I'm always happy afterward.", "自分が教える番になると緊張しますが、終わった後はいつも嬉しいです。"],
                ["Also, I've learned how to make a really wide variety of dishes this way.", "また、この方法で本当にさまざまな料理の作り方を学びました。"],
                ["It's much better than having just one cooking teacher.", "料理の先生が1人だけよりずっと良いです。"],
                ["I was telling my friend David about our meetings.", "友人のデイビッドに私たちの集まりのことを話していました。"],
                ["David works as a photographer and designer for a company that publishes books.", "デイビッドは本を出版する会社でカメラマンとデザイナーとして働いています。"],
                ["He suggested that the cooking club members make a book of our favorite recipes.", "彼は料理クラブのメンバーでお気に入りレシピの本を作ることを提案しました。"],
                ["He said that he would help us to do it.", "彼が手伝ってくれると言ってくれました。"],
                ["We could make something to remember our meetings.", "集まりを記念するものを作れます。"],
                ["A book of recipes would also be a great gift for friends and family members.", "レシピ本は友人や家族への素敵な贈り物にもなります。"],
                ["I really like his idea.", "彼のアイデアがとても気に入りました。"],
                ["We could ask each of the members to prepare recipes for a snack, a salad, a soup, a main dish, and a dessert.", "各メンバーにおやつ、サラダ、スープ、メインディッシュ、デザートのレシピを準備してもらえます。"],
                ["We can then choose the ones that sound the best and make them during our meetings.", "一番良さそうなものを選んで集まりの時に作ることができます。"],
                ["David said that he would be happy to come and take pictures of our food.", "デイビッドは喜んで来て料理の写真を撮ると言っていました。"],
                ["He'd like to try some of it, too!", "料理を少し味見もしたいそうです！"]
            ],
            "questions": [
                {
                    "number": 31,
                    "question": "What does Ariana say about the cooking club meetings?",
                    "questionTranslation": "アリアナは料理クラブの集まりについて何と言っていますか？",
                    "choices": [
                        "She thinks their cooking teacher is very friendly.",
                        "She likes the way that members teach each other.",
                        "She feels nervous when new members join.",
                        "She wants them to be moved to a community center."
                    ],
                    "choiceTranslations": [
                        "彼女は料理の先生がとてもフレンドリーだと思っている。",
                        "彼女はメンバー同士が教え合う方法が気に入っている。",
                        "新しいメンバーが加わると緊張する。",
                        "コミュニティセンターに移動させたいと思っている。"
                    ],
                    "answer": 2,
                    "choiceAnalysis": [
                        "料理の先生がフレンドリー→先生は1人ではなくメンバーが交代で教えている",
                        "メンバー同士が教え合う方法が気に入っている→正解。💡 \"It's nice that the members take turns teaching each other recipes\" が直接の根拠",
                        "新しいメンバーが加わると緊張→自分が教える番の時に緊張する",
                        "コミュニティセンターに移動させたい→すでにコミュニティセンターで開催中"
                    ],
                    "grammar": "💡 take turns ～ing＝交代で～する。each other＝お互いに"
                },
                {
                    "number": 32,
                    "question": "What has Ariana's friend David suggested?",
                    "questionTranslation": "アリアナの友人デイビッドは何を提案しましたか？",
                    "choices": [
                        "Food made at cooking club meetings could be sold.",
                        "Friends should be allowed to watch cooking club meetings.",
                        "The members of the cooking club should produce a book.",
                        "Ariana could get a job at his publishing company."
                    ],
                    "choiceTranslations": [
                        "料理クラブで作った食べ物を販売する。",
                        "友人が料理クラブの集まりを見学できるようにする。",
                        "料理クラブのメンバーが本を作るべきだ。",
                        "アリアナが彼の出版社で働ける。"
                    ],
                    "answer": 3,
                    "choiceAnalysis": [
                        "料理を販売→販売の話は本文にない",
                        "友人が見学→見学についての言及はない",
                        "メンバーが本を作るべき→正解。💡 \"He suggested that the cooking club members make a book of our favorite recipes\" が直接の根拠",
                        "出版社で働ける→就職の話はしていない"
                    ],
                    "grammar": "💡 suggest (that) ～＝～を提案する。produce＝作る、制作する。publish＝出版する"
                },
                {
                    "number": 33,
                    "question": "David has offered to",
                    "questionTranslation": "デイビッドは何を申し出ましたか？",
                    "choices": [
                        "think of new recipes for the cooking club.",
                        "choose the best dishes in a cooking competition.",
                        "teach Ariana and Jane how to cook various dishes.",
                        "take photos of food for the cooking club."
                    ],
                    "choiceTranslations": [
                        "料理クラブのために新しいレシピを考える。",
                        "料理コンテストで最高の料理を選ぶ。",
                        "アリアナとジェーンにさまざまな料理の作り方を教える。",
                        "料理クラブのために料理の写真を撮る。"
                    ],
                    "answer": 4,
                    "choiceAnalysis": [
                        "新しいレシピを考える→デイビッドはカメラマンであり料理人ではない",
                        "コンテストで最高の料理を選ぶ→料理コンテストの言及はない",
                        "料理の作り方を教える→教えるとは言っていない",
                        "料理の写真を撮る→正解。💡 \"David said that he would be happy to come and take pictures of our food\" が直接の根拠"
                    ],
                    "grammar": "💡 offer to ～＝～することを申し出る。take pictures of ～＝～の写真を撮る。would be happy to ～＝喜んで～する"
                }
            ]
        },
        {
            "label": "B",
            "title": "A Slow Life in the Trees",
            "paragraphs": [
                "A sloth is a kind of animal that lives in the jungles of Central and South America. Sloths look like monkeys and spend most of their time up in the branches of trees. However, unlike monkeys, sloths live alone, move very slowly, and make almost no noise. They sleep for up to 20 hours each day and only wake up during the night.",
                "Sloths' lazy lifestyles help them to survive. By sleeping most of the time and moving slowly, sloths do not have to use much energy. They do not have to travel long distances or run fast to get something to eat. High up in the trees, a tasty leaf is always just a few centimeters away. Even though leaves do not contain many calories, sloths get all they need by eating all the time during the short time that they are awake.",
                "Surprisingly, moving slowly also protects sloths from hungry meat eaters. Eagles and big cats live in the same jungles as sloths. However, these hunters search for movement, so they often do not notice sloths. Also, sloths do not clean their fur completely. As a result, tiny plants grow in it, and these make the fur look green. From the ground or the sky, a sloth in a tree's branches looks like a plant rather than something that an eagle or a big cat wants to eat.",
                "Sloths have long, hard claws on their toes. Usually, they use their claws to hang on to branches. However, if a sloth is attacked, it can use its claws to defend itself. Sloths' claws are so long that sloths find it difficult to walk on the ground. Because of this, a sloth usually only comes down from the branches about once a week."
            ],
            "translations": [
                "ナマケモノは中南米のジャングルに住む動物の一種だ。ナマケモノはサルに似ており、ほとんどの時間を木の枝の上で過ごす。しかし、サルとは異なり、ナマケモノは単独で生活し、非常にゆっくり動き、ほとんど音を立てない。一日最大20時間眠り、夜の間だけ目を覚ます。",
                "ナマケモノの怠惰な生活様式は生存に役立っている。ほとんどの時間を寝てゆっくり動くことで、ナマケモノは多くのエネルギーを使う必要がない。食べ物を得るために長距離を移動したり速く走ったりする必要がない。木の上高くでは、おいしい葉がいつもほんの数センチ先にある。葉にはカロリーが少ないが、ナマケモノは起きている短い時間の間ずっと食べ続けることで必要なものをすべて得ている。",
                "驚くことに、ゆっくり動くことはナマケモノを空腹の肉食動物からも守っている。ワシや大型の猫科動物はナマケモノと同じジャングルに住んでいる。しかし、これらの捕食者は動きを探すので、ナマケモノに気づかないことが多い。また、ナマケモノは毛皮を完全にきれいにしない。その結果、小さな植物が毛皮に生え、毛皮を緑色に見せる。地面や空からは、木の枝にいるナマケモノはワシや大型の猫科動物が食べたいものではなく、植物のように見える。",
                "ナマケモノの足の指には長く硬い爪がある。通常、爪を使って枝にぶら下がっている。しかし、ナマケモノが攻撃されると、爪を使って自分を守ることができる。ナマケモノの爪は非常に長いので、地面を歩くのが難しい。このため、ナマケモノは通常、週に約1回しか枝から降りてこない。"
            ],
            "sentencePairs": [
                ["A sloth is a kind of animal that lives in the jungles of Central and South America.", "ナマケモノは中南米のジャングルに住む動物の一種だ。"],
                ["Sloths look like monkeys and spend most of their time up in the branches of trees.", "ナマケモノはサルに似ており、ほとんどの時間を木の枝の上で過ごす。"],
                ["However, unlike monkeys, sloths live alone, move very slowly, and make almost no noise.", "しかし、サルとは異なり、ナマケモノは単独で生活し、非常にゆっくり動き、ほとんど音を立てない。"],
                ["They sleep for up to 20 hours each day and only wake up during the night.", "一日最大20時間眠り、夜の間だけ目を覚ます。"],
                ["By sleeping most of the time and moving slowly, sloths do not have to use much energy.", "ほとんどの時間を寝てゆっくり動くことで、ナマケモノは多くのエネルギーを使う必要がない。"],
                ["They do not have to travel long distances or run fast to get something to eat.", "食べ物を得るために長距離を移動したり速く走ったりする必要がない。"],
                ["High up in the trees, a tasty leaf is always just a few centimeters away.", "木の上高くでは、おいしい葉がいつもほんの数センチ先にある。"],
                ["Even though leaves do not contain many calories, sloths get all they need by eating all the time during the short time that they are awake.", "葉にはカロリーが少ないが、ナマケモノは起きている短い時間の間ずっと食べ続けることで必要なものをすべて得ている。"],
                ["Surprisingly, moving slowly also protects sloths from hungry meat eaters.", "驚くことに、ゆっくり動くことはナマケモノを空腹の肉食動物からも守っている。"],
                ["Eagles and big cats live in the same jungles as sloths.", "ワシや大型の猫科動物はナマケモノと同じジャングルに住んでいる。"],
                ["However, these hunters search for movement, so they often do not notice sloths.", "しかし、これらの捕食者は動きを探すので、ナマケモノに気づかないことが多い。"],
                ["Also, sloths do not clean their fur completely.", "また、ナマケモノは毛皮を完全にきれいにしない。"],
                ["As a result, tiny plants grow in it, and these make the fur look green.", "その結果、小さな植物が毛皮に生え、毛皮を緑色に見せる。"],
                ["From the ground or the sky, a sloth in a tree's branches looks like a plant rather than something that an eagle or a big cat wants to eat.", "地面や空からは、木の枝にいるナマケモノは植物のように見える。"],
                ["Sloths have long, hard claws on their toes.", "ナマケモノの足の指には長く硬い爪がある。"],
                ["Usually, they use their claws to hang on to branches.", "通常、爪を使って枝にぶら下がっている。"],
                ["However, if a sloth is attacked, it can use its claws to defend itself.", "しかし、ナマケモノが攻撃されると、爪を使って自分を守ることができる。"],
                ["Sloths' claws are so long that sloths find it difficult to walk on the ground.", "ナマケモノの爪は非常に長いので、地面を歩くのが難しい。"],
                ["Because of this, a sloth usually only comes down from the branches about once a week.", "このため、ナマケモノは通常、週に約1回しか枝から降りてこない。"]
            ],
            "questions": [
                {
                    "number": 34,
                    "question": "What is one way sloths are different from monkeys?",
                    "questionTranslation": "ナマケモノがサルと異なる点の一つは何ですか？",
                    "choices": [
                        "Sloths can be found in North America.",
                        "Sloths often make a lot of noise.",
                        "Sloths usually live by themselves.",
                        "Sloths are only awake during the day."
                    ],
                    "choiceTranslations": [
                        "ナマケモノは北アメリカにもいる。",
                        "ナマケモノはよく大きな音を立てる。",
                        "ナマケモノは通常単独で生活する。",
                        "ナマケモノは日中だけ起きている。"
                    ],
                    "answer": 3,
                    "choiceAnalysis": [
                        "北アメリカにもいる→中南米のジャングルに住むと記載されており矛盾",
                        "大きな音を立てる→make almost no noise（ほとんど音を立てない）と矛盾",
                        "通常単独で生活する→正解。💡 \"unlike monkeys, sloths live alone\" が直接の根拠",
                        "日中だけ起きている→only wake up during the night（夜だけ起きる）と矛盾"
                    ],
                    "grammar": "💡 unlike ～＝～とは異なり。live alone＝一人で暮らす。by themselves＝自分たちだけで（alone のパラフレーズ）"
                },
                {
                    "number": 35,
                    "question": "What is one reason that sloths move slowly?",
                    "questionTranslation": "ナマケモノがゆっくり動く理由の一つは何ですか？",
                    "choices": [
                        "To reduce the amount of energy that they use.",
                        "To allow them to travel very long distances.",
                        "To catch the things that they like to eat.",
                        "To avoid falling into holes made by other animals."
                    ],
                    "choiceTranslations": [
                        "使うエネルギーの量を減らすため。",
                        "非常に長い距離を移動できるようにするため。",
                        "好んで食べるものを捕まえるため。",
                        "他の動物が作った穴に落ちるのを避けるため。"
                    ],
                    "answer": 1,
                    "choiceAnalysis": [
                        "使うエネルギーを減らす→正解。💡 \"By sleeping most of the time and moving slowly, sloths do not have to use much energy\" が直接の根拠",
                        "長距離を移動できる→長距離移動の必要がないと記載",
                        "食べるものを捕まえる→葉を食べるので捕まえる必要なし",
                        "穴に落ちるのを避ける→穴に関する言及はない"
                    ],
                    "grammar": "💡 reduce＝減らす。By ～ing＝～することによって（手段・方法）。amount of ～＝～の量"
                },
                {
                    "number": 36,
                    "question": "Eagles and big cats",
                    "questionTranslation": "ワシや大型の猫科動物は",
                    "choices": [
                        "do not eat sloths because their fur tastes bad.",
                        "eat plants if they are not able to find meat.",
                        "hunt by looking for the movement of animals.",
                        "stay away from the jungles where sloths live."
                    ],
                    "choiceTranslations": [
                        "ナマケモノの毛皮の味が悪いので食べない。",
                        "肉が見つからなければ植物を食べる。",
                        "動物の動きを探して狩りをする。",
                        "ナマケモノが住むジャングルに近づかない。"
                    ],
                    "answer": 3,
                    "choiceAnalysis": [
                        "毛皮の味が悪い→味についての言及はない",
                        "肉がなければ植物を食べる→植物食についての言及はない",
                        "動物の動きを探して狩りをする→正解。💡 \"these hunters search for movement\" が直接の根拠",
                        "ジャングルに近づかない→同じジャングルに住んでいると明記"
                    ],
                    "grammar": "💡 search for ～＝～を探す。movement＝動き。hunt＝狩りをする。hunter＝狩猟者、捕食者"
                },
                {
                    "number": 37,
                    "question": "A sloth uses its long claws to",
                    "questionTranslation": "ナマケモノは長い爪を使って",
                    "choices": [
                        "cut open fruits that grow in the trees.",
                        "get insects that live inside wood.",
                        "jump from one tree to another.",
                        "help it to hold on to branches."
                    ],
                    "choiceTranslations": [
                        "木に実る果物を切り開く。",
                        "木の中に住む昆虫を捕まえる。",
                        "木から木へ飛び移る。",
                        "枝につかまるのに役立てる。"
                    ],
                    "answer": 4,
                    "choiceAnalysis": [
                        "果物を切り開く→果物についての言及はない",
                        "昆虫を捕まえる→昆虫食についての言及はない",
                        "木から木へ飛び移る→ジャンプについての言及はない",
                        "枝につかまるのに役立てる→正解。💡 \"they use their claws to hang on to branches\" が直接の根拠。hold on to は hang on to のパラフレーズ"
                    ],
                    "grammar": "💡 hang on to ～＝～にしがみつく、つかまる。hold on to ～ と同義。claw＝爪。defend oneself＝自分を守る"
                }
            ]
        }
    ]
}

data["sections"].append(section3)
data["sections"].append(section4)

# =====================================================
# Vocabulary (40語以上 — 全大問から均等抽出)
# =====================================================
data["vocabulary"] = [
    # 大問1から（15語）
    {"word": "dive", "meaning": "飛び込む", "pos": "動詞", "level": "準2級", "example": "The children love to dive into the lake on hot summer days.", "distractors": ["流れる", "溶かす", "発表する"]},
    {"word": "unlikely", "meaning": "ありそうにない", "pos": "形容詞", "level": "準2級", "example": "It is unlikely that we will finish the project by Friday.", "distractors": ["伝統的な", "似ている", "正直な"]},
    {"word": "author", "meaning": "著者、作家", "pos": "名詞", "level": "準2級", "example": "The author signed copies of her new novel at the bookstore.", "distractors": ["宇宙飛行士", "会計士", "運動選手"]},
    {"word": "chase", "meaning": "追いかける", "pos": "動詞", "level": "準2級", "example": "The police officer had to chase the thief through the park.", "distractors": ["挨拶する", "雇う", "共有する"]},
    {"word": "network", "meaning": "ネットワーク、網", "pos": "名詞", "level": "準2級", "example": "Tokyo has an excellent network of trains and subways.", "distractors": ["苦闘", "録音", "目的"]},
    {"word": "divide", "meaning": "分ける", "pos": "動詞", "level": "準2級", "example": "Please divide the cake into eight equal pieces.", "distractors": ["受け入れる", "温める", "怪我させる"]},
    {"word": "issue", "meaning": "問題、課題", "pos": "名詞", "level": "準2級", "example": "Climate change is one of the most important issues of our time.", "distractors": ["学位", "反応", "仲間"]},
    {"word": "in good spirits", "meaning": "機嫌がいい", "pos": "熟語", "level": "準2級", "example": "After receiving the good news, everyone was in good spirits.", "distractors": ["議論中", "コンテストで", "決断後"]},
    {"word": "apologize", "meaning": "謝罪する", "pos": "動詞", "level": "準2級", "example": "He apologized to his teacher for being late to class.", "distractors": ["輸出する", "制限する", "うなずく"]},
    {"word": "look alike", "meaning": "似て見える", "pos": "熟語", "level": "準2級", "example": "The twin sisters look alike, but their personalities are very different.", "distractors": ["前を見る", "流行する", "追いつく"]},
    {"word": "put out", "meaning": "（火を）消す", "pos": "句動詞", "level": "準2級", "example": "The firefighters quickly put out the fire before it spread.", "distractors": ["出てくる", "満たす", "後退する"]},
    {"word": "in need", "meaning": "困っている", "pos": "熟語", "level": "準2級", "example": "The charity provides food and shelter to people in need.", "distractors": ["続けて", "暗記して", "役に立つ"]},
    {"word": "on a diet", "meaning": "ダイエット中", "pos": "熟語", "level": "準2級", "example": "She has been on a diet for two months and lost three kilograms.", "distractors": ["気分転換に", "定位置に", "時間とともに"]},
    {"word": "known to", "meaning": "～で知られている", "pos": "熟語", "level": "準2級", "example": "Dolphins are known to be very intelligent animals.", "distractors": ["～を妬む", "～に属する", "～に当てはまる"]},
    {"word": "close to", "meaning": "～に近い", "pos": "熟語", "level": "準2級", "example": "Our hotel was close to the beach, so we could walk there easily.", "distractors": ["～を確信して", "～に適した", "～が苦手で"]},
    # 大問2から（6語）
    {"word": "serve", "meaning": "（料理を）出す、提供する", "pos": "動詞", "level": "準2級", "example": "This restaurant serves breakfast from 7:00 to 10:00.", "distractors": ["注文する", "予約する", "味わう"]},
    {"word": "discount", "meaning": "割引", "pos": "名詞", "level": "準2級", "example": "Students can get a 20 percent discount with their ID card.", "distractors": ["領収書", "料金", "税金"]},
    {"word": "promise", "meaning": "約束する", "pos": "動詞", "level": "準2級", "example": "I promise to call you as soon as I arrive.", "distractors": ["拒否する", "忘れる", "無視する"]},
    {"word": "used to", "meaning": "以前は～した", "pos": "熟語", "level": "準2級", "example": "I used to walk to school, but now I take the bus.", "distractors": ["～に慣れている", "～するのに使う", "～するべきだ"]},
    {"word": "half price", "meaning": "半額", "pos": "名詞句", "level": "準2級", "example": "All winter coats are available at half price during the February sale.", "distractors": ["定価", "二倍の価格", "無料"]},
    {"word": "address book", "meaning": "住所録、電話帳", "pos": "名詞", "level": "準2級", "example": "Let me check my address book for her phone number.", "distractors": ["教科書", "日記帳", "ノート"]},
    # 大問3から（7語）
    {"word": "costume", "meaning": "衣装、仮装", "pos": "名詞", "level": "準2級", "example": "The children wore colorful costumes for the Halloween party.", "distractors": ["制服", "アクセサリー", "ネクタイ"]},
    {"word": "borrow", "meaning": "借りる", "pos": "動詞", "level": "準2級", "example": "Can I borrow your umbrella? I forgot mine at home.", "distractors": ["貸す", "盗む", "返す"]},
    {"word": "graphic art", "meaning": "グラフィックアート", "pos": "名詞", "level": "準2級", "example": "She studied graphic art at college and became a professional designer.", "distractors": ["音楽理論", "演劇", "写真撮影"]},
    {"word": "imagination", "meaning": "想像力", "pos": "名詞", "level": "準2級", "example": "Children often have a wonderful imagination and can create amazing stories.", "distractors": ["記憶力", "集中力", "判断力"]},
    {"word": "exhibition", "meaning": "展覧会", "pos": "名詞", "level": "準2級", "example": "The museum is holding a special exhibition of modern art this month.", "distractors": ["競技会", "講演会", "卒業式"]},
    {"word": "pattern", "meaning": "模様、パターン", "pos": "名詞", "level": "準2級", "example": "The wallpaper has a beautiful flower pattern.", "distractors": ["素材", "表面", "質感"]},
    {"word": "countryside", "meaning": "田園地帯、地方", "pos": "名詞", "level": "準2級", "example": "Many people enjoy visiting the countryside on weekends to relax.", "distractors": ["都心部", "工業地帯", "商業街"]},
    # 大問4から（14語）
    {"word": "recipe", "meaning": "レシピ、調理法", "pos": "名詞", "level": "準2級", "example": "My grandmother gave me her secret recipe for chocolate cake.", "distractors": ["材料", "メニュー", "調味料"]},
    {"word": "variety", "meaning": "多様性、さまざまな種類", "pos": "名詞", "level": "準2級", "example": "The store offers a wide variety of organic vegetables.", "distractors": ["量", "品質", "割合"]},
    {"word": "suggest", "meaning": "提案する", "pos": "動詞", "level": "準2級", "example": "The doctor suggested that I get more exercise.", "distractors": ["要求する", "命令する", "拒否する"]},
    {"word": "photographer", "meaning": "写真家", "pos": "名詞", "level": "準2級", "example": "The photographer took beautiful pictures of the sunset.", "distractors": ["画家", "彫刻家", "建築家"]},
    {"word": "take turns", "meaning": "交代でする", "pos": "熟語", "level": "準2級", "example": "The students took turns reading paragraphs from the textbook.", "distractors": ["同時にする", "順番を飛ばす", "全員で一斉にする"]},
    {"word": "survive", "meaning": "生き残る", "pos": "動詞", "level": "準2級", "example": "Some animals can survive in extreme temperatures.", "distractors": ["繁殖する", "移住する", "適応する"]},
    {"word": "contain", "meaning": "含む", "pos": "動詞", "level": "準2級", "example": "This drink contains a lot of sugar, so you should drink it in moderation.", "distractors": ["除外する", "増加する", "吸収する"]},
    {"word": "protect", "meaning": "守る、保護する", "pos": "動詞", "level": "準2級", "example": "Sunscreen helps to protect your skin from harmful UV rays.", "distractors": ["傷つける", "さらす", "攻撃する"]},
    {"word": "fur", "meaning": "毛皮", "pos": "名詞", "level": "準2級", "example": "The cat's fur was soft and fluffy.", "distractors": ["羽毛", "うろこ", "ヒレ"]},
    {"word": "defend", "meaning": "守る、防御する", "pos": "動詞", "level": "準2級", "example": "The soldiers were ready to defend the city from the enemy.", "distractors": ["攻撃する", "降伏する", "逃げる"]},
    {"word": "claw", "meaning": "爪", "pos": "名詞", "level": "準2級", "example": "The eagle uses its sharp claws to catch fish from the river.", "distractors": ["くちばし", "翼", "尾"]},
    {"word": "branch", "meaning": "枝", "pos": "名詞", "level": "準2級", "example": "The bird built its nest on a high branch of the oak tree.", "distractors": ["根", "幹", "葉"]},
    {"word": "movement", "meaning": "動き", "pos": "名詞", "level": "準2級", "example": "The security camera detected a sudden movement in the hallway.", "distractors": ["音", "匂い", "光"]},
    {"word": "publish", "meaning": "出版する", "pos": "動詞", "level": "準2級", "example": "The company publishes over 200 books every year.", "distractors": ["翻訳する", "編集する", "印刷する"]}
]

# Save complete data (without lessonPlan)
output_path = os.path.join(base, "_part2.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

total_q = 0
for s in data["sections"]:
    total_q += len(s.get("questions", []))
    for p in s.get("passages", []):
        total_q += len(p.get("questions", []))

print(f"Part 2 saved: {total_q} total questions, {len(data['vocabulary'])} vocabulary words")
print(f"Sections: {[s['name'] for s in data['sections']]}")

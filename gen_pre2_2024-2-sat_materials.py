"""Vocabulary and lesson plan of EIKEN Grade Pre-2 2024-2 Saturday sub-venue.

Loaded by gen_pre2_2024-2-sat.py, which passes its helper functions as ``h``.
Vocabulary examples are original sentences (not copied from the exam); lesson
examples, source quotes and practice passages quote the exam with the official
answers filled in.
"""

from __future__ import annotations


VOCABULARY = [
    # Part 1 answers
    ("cotton", "綿・木綿", "名詞", "This T-shirt is made of soft cotton.", ["うわさ", "くぎ", "政治"]),
    ("promise", "約束する", "動詞", "I promised my mother that I would clean my room.", ["認める", "返す", "探す"]),
    ("annoying", "いらいらさせる・迷惑な", "形容詞", "The loud music from next door was really annoying.", ["社会の", "きちんとした", "空の"]),
    ("seal", "封をする", "動詞", "Please seal the box with tape before you send it.", ["失敗する", "焼く", "奪う"]),
    ("daily", "毎日", "副詞", "My grandfather walks in the park daily.", ["部分的に", "静かに", "そっと"]),
    ("assist", "手伝う・援助する", "動詞", "The nurse assisted the doctor during the operation.", ["推測する", "調べる", "指揮する"]),
    ("growth", "成長", "名詞", "Sleep is important for the growth of young children.", ["真実", "勇気", "不在"]),
    ("seek", "探し求める", "動詞", "Many students seek advice from their teachers.", ["説明する", "代表する", "引退する"]),
    ("prison", "刑務所", "名詞", "The thief spent three years in prison.", ["液体", "宇宙", "心"]),
    ("location", "場所・位置", "名詞", "This hotel is in a great location near the station.", ["予報", "毛布", "習慣"]),
    ("far from", "～から遠い", "句", "The beach is not far from my grandparents' house.", ["～まで", "乗車して", "～に基づいて"]),
    ("from now on", "これからは・今後は", "句", "From now on, I will go to bed before eleven.", ["放送中で", "ところで", "やりすぎの"]),
    ("make one's bed", "ベッドを整える", "句", "Please make your bed before you leave for school.", ["連絡を取り合う", "熱がある", "家に向かう"]),
    ("set up", "（機器などを）設定する", "句動詞", "My father set up the new TV in the living room.", ["～を願う", "～に勤める", "～をいっぱいにする"]),
    ("curious about", "～に興味がある", "句", "Small children are curious about everything around them.", ["～から離れた", "折れて取れた", "～に飽きた"]),
    # Part 2
    ("performance", "演奏・公演", "名詞", "The students gave a wonderful performance at the festival.", ["招待", "練習", "観客"]),
    ("book", "予約する", "動詞", "We booked a table at the restaurant for Friday night.", ["取り消す", "支払う", "変更する"]),
    ("run out", "なくなる・切れる", "句動詞", "We ran out of milk, so I went to the store.", ["印刷する", "補充する", "注文する"]),
    ("document", "書類・文書", "名詞", "Please sign this document and give it back to me.", ["写真", "封筒", "地図"]),
    ("expensive", "高価な", "形容詞", "This watch is too expensive for me to buy.", ["安い", "便利な", "珍しい"]),
    # Part 3
    ("invite", "招待する・誘う", "動詞", "Emma invited me to her birthday party.", ["断る", "案内する", "訪問する"]),
    ("worried", "心配して", "形容詞", "My mother was worried because I came home late.", ["興奮して", "驚いて", "退屈して"]),
    ("campsite", "キャンプ場", "名詞", "We set up our tent at the campsite before dark.", ["駐車場", "遊園地", "運動場"]),
    ("completely", "完全に", "副詞", "The snow completely covered the road.", ["部分的に", "ほとんど", "ゆっくりと"]),
    # Part 4A
    ("employee", "従業員", "名詞", "The company has about two hundred employees.", ["雇い主", "客", "経営者"]),
    ("staff", "職員・スタッフ", "名詞", "The hotel staff were very kind to us.", ["客", "商品", "設備"]),
    ("glasses", "眼鏡", "名詞", "I can't read small letters without my glasses.", ["手袋", "財布", "帽子"]),
    ("trouble", "苦労・困難", "名詞", "I had trouble finding the right bus stop.", ["楽しみ", "余裕", "習慣"]),
    ("groceries", "食料品・日用品", "名詞", "Dad carried the groceries from the car to the kitchen.", ["文房具", "家具", "衣類"]),
    ("option", "選択肢", "名詞", "There are several options for lunch at the school cafeteria.", ["値段", "意見", "予定"]),
    ("cash register", "レジ", "名詞", "The line at the cash register was very long.", ["入口", "倉庫", "案内所"]),
    ("find out", "知る・わかる", "句動詞", "I found out that my friend was moving to Osaka.", ["見落とす", "忘れる", "隠す"]),
    # Part 4B
    ("access", "（情報などを）利用する・アクセスする", "動詞", "You can access the library's website from home.", ["削除する", "保存する", "印刷する"]),
    ("suffer", "苦しむ・打撃を受ける", "動詞", "Many farmers suffered because there was no rain all summer.", ["回復する", "利益を得る", "満足する"]),
    ("survive", "生き残る", "動詞", "Most plants cannot survive without water.", ["成長する", "輸出する", "引退する"]),
    ("convenient", "便利な", "形容詞", "This small bag is convenient for traveling.", ["高価な", "危険な", "珍しい"]),
    ("quality", "質・品質", "名詞", "This shop sells shoes of high quality.", ["量", "値段", "流行"]),
    ("rare", "珍しい・まれな", "形容詞", "It is rare to see snow in this city.", ["ありふれた", "高価な", "新しい"]),
    ("valuable", "価値のある・貴重な", "形容詞", "This old coin is very valuable.", ["安価な", "ありふれた", "壊れやすい"]),
    ("expert", "専門家", "名詞", "We asked an expert about the health of our dog.", ["初心者", "読者", "収集家"]),
]


def build_vocabulary(h) -> list[dict]:
    return [h.vocab(index, *entry) for index, entry in enumerate(VOCABULARY, start=1)]


def build_lesson_plan(h) -> dict:
    fp = h.focus_point
    points = [
        fp(
            "fp1",
            "過去完了（経験）・enough to・関係代名詞which",
            "Past Perfect, enough to & Non-restrictive which",
            "had never been ～ beforeは過去完了で、『（過去のその時まで）一度も～したことがなかった』という経験を表します。形容詞＋enough for 人＋to doは『人が～できるほど…』という意味で、for 人がto不定詞の意味上の主語です。the campsite, which ...のコンマの後のwhichは、直前のthe campsiteに説明を付け加える関係代名詞（非制限用法）で、『そしてそこは～』と前から順に読み進められます。",
            "had never been camping before / big enough for both of them to sleep in / the campsite, which was by a beautiful lake / He had never seen them so clearly before",
            "大問3「First Camping Trip」第1・2段落",
            [
                {"en": "Tom lived in a big city and had never been camping before, so he was excited about going.", "ja": "トムは大都市に住んでいて、それまでキャンプをしたことがなかったので、行くのを楽しみにしていました。", "note": "had never been camping before＝（誘われた時点まで）一度もキャンプをしたことがなかった（過去完了の経験）。go camping→been campingの形になっている。"},
                {"en": "However, Sam said that he had one that was big enough for both of them to sleep in.", "ja": "しかしサムは、二人とも中で寝られるくらい大きなものを持っていると言いました。", "note": "形容詞＋enough for 人＋to do＝人が～できるほど…。oneはa tentの代わり。that was ...はoneを説明する関係代名詞節。"},
                {"en": "It took a long time to get to the campsite, which was by a beautiful lake.", "ja": "美しい湖のそばにあるキャンプ場に着くまでには、長い時間がかかりました。", "note": ", which ...は直前のthe campsiteに説明を付け加える（非制限用法）。It takes＋時間＋to do＝～するのに（時間）がかかる。"},
            ],
            "[出典: First Camping Trip 第1・2段落]\nLast summer, Tom was invited on a camping trip by his friend Sam. Tom lived in a big city and had never been camping before, so he was excited about going. Although he was excited, he was worried because he did not have his own tent. However, Sam said that he had one that was big enough for both of them to sleep in. It took a long time to get to the campsite, which was by a beautiful lake. When they had finished eating, the sky was dark. Sam's father told Tom to look up at the stars. Tom was surprised. There were so many, and they were so bright. He had never seen them so clearly before because the night sky in the city was not completely dark.",
            "昨年の夏、トムは友達のサムにキャンプ旅行に誘われました。トムは大都市に住んでいて、それまでキャンプをしたことがなかったので、行くのを楽しみにしていました。わくわくしていたものの、トムは自分のテントを持っていなかったので、心配していました。しかしサムは、二人とも中で寝られるくらい大きなものを持っていると言いました。美しい湖のそばにあるキャンプ場に着くまでには、長い時間がかかりました。食べ終わったときには、空は暗くなっていました。サムの父親はトムに、星を見上げるように言いました。トムは驚きました。星の数がとても多く、とても明るかったのです。都会の夜空は完全には暗くならないので、トムはそれまでこれほどはっきりと星を見たことがなかったのです。",
            ["had never been camping before", "big enough for both of them to sleep in", "which was by a beautiful lake", "had never seen them so clearly before"],
            "過去完了・enough",
            [
                {"q": "had never been camping beforeは、いつまでの経験を表していますか？", "a": "サムにキャンプに誘われた昨年の夏の時点までです。その時までに一度もキャンプをしたことがなかった、という過去完了です。"},
                {"q": "big enough for both of them to sleep inは、どのような意味ですか？", "a": "『二人とも中で寝られるほど大きい』という意味です。形容詞＋enough for 人＋to doで『人が～できるほど…』を表します。"},
                {"q": "the campsite, which was by a beautiful lakeのwhichは何を指しますか？", "a": "直前のthe campsiteです。コンマの後のwhichが、キャンプ場は美しい湖のそばにあったという説明を付け加えています。"},
                {"q": "He had never seen them so clearly beforeのthemは何を指しますか？", "a": "サムの父親に見上げるよう言われた星（the stars）です。都会の夜空は完全には暗くならないため、トムはそれまで星をこれほどはっきり見たことがなかったのです。"},
            ],
        ),
        fp(
            "fp2",
            "help／make／let＋人＋動詞の原形",
            "help, make & let + Person + Base Form",
            "help 人 do（人が～するのを手伝う）、make 人 do（人に～させる）、let 人 do（人に～させてあげる）は、『人』の後ろに動詞の原形が続きます（helpはhelp 人 to doの形も使えます）。このメールでは、マークがジョイスの祖母にしてくれたことが、helped her pick out ／ helped her find ／ helped her payのように並んでいます。原形の動詞の動作をするのは『人』の部分（her）だと押さえると、誰が何をしたのかを正確に読み取れます。",
            "He helped her pick out her groceries / He even helped her find cheaper options / He then made her promise to take her glasses with her next time / Please let him know",
            "大問4A メール第2・3段落",
            [
                {"en": "He even helped her find cheaper options.", "ja": "さらに、もっと安い商品を見つけるのまで手伝ってくれました。", "note": "help 人 do＝人が～するのを手伝う。見つけるのは祖母（her）で、マークはそれを手伝った。evenは『～まで・～さえ』。"},
                {"en": "When she was finished, he took her cart to the cash register and helped her pay.", "ja": "祖母が買い物を終えると、カートをレジまで運び、支払いを手伝ってくれました。", "note": "helped her pay＝彼女が支払うのを手伝った（payは原形）。be finished＝（人が）～を終えている。"},
                {"en": "He then made her promise to take her glasses with her next time.", "ja": "そして、次からは眼鏡を持って出かけると祖母に約束させました。", "note": "make 人 do＝人に～させる。promise to do＝～すると約束する。take ～ with 人＝～を持って行く。"},
            ],
            "[出典: Helpful employee 第2・3段落]\nMark noticed she was having trouble and asked her if he could help. He helped her pick out her groceries. He even helped her find cheaper options. When she was finished, he took her cart to the cash register and helped her pay. When he found out that she was taking the bus by herself, he drove her home and carried the groceries into her apartment. He then made her promise to take her glasses with her next time. Please let him know that my family and I really want to say thank you for what he did for her.",
            "マークさんは祖母が困っていることに気づき、何か手伝えることはないかと声をかけてくれました。祖母が食料品を選ぶのを手伝ってくれました。さらに、もっと安い商品を見つけるのまで手伝ってくれました。祖母が買い物を終えると、カートをレジまで運び、支払いを手伝ってくれました。祖母が一人でバスに乗って帰るところだと知ると、車で家まで送り、食料品をアパートの部屋の中まで運んでくれました。そして、次からは眼鏡を持って出かけると祖母に約束させました。祖母にしてくださったことに対して、家族と私が心から感謝していると、マークさんにお伝えください。",
            ["helped her pick out", "helped her find", "helped her pay", "made her promise to take her glasses", "let him know"],
            "使役・原形",
            [
                {"q": "He helped her pick out her groceries.で、食料品を選んだのは誰ですか？", "a": "祖母（her）です。help 人 doは『人が～するのを手伝う』なので、選んだのは祖母で、マークはそれを手伝いました。"},
                {"q": "helped her payのpayの前にtoがないのはなぜですか？", "a": "help 人 doの形では、人の後ろに動詞の原形を置けるからです。helped her to payとtoをつけて言うこともできます。"},
                {"q": "He then made her promise to take her glasses with her next time.は、どのような意味ですか？", "a": "『そしてマークは、次からは眼鏡を持って出かけると祖母に約束させた』という意味です。make 人 doは『人に～させる』です。"},
                {"q": "Please let him know that ...で、ジョイスは店に何を頼んでいますか？", "a": "家族とジョイスが心から感謝していることを、マークに伝えてほしいと頼んでいます。let 人 knowは『人に知らせる』です。"},
            ],
        ),
        fp(
            "fp3",
            "現在完了（継続）・evenの強調・感情の原因を表す不定詞",
            "Present Perfect, even + Comparative & Infinitive of Feeling",
            "has been going（現在完了進行形）やhas enjoyed（現在完了）は、この文章ではfor ～（～の間）と一緒に使われ、過去から今まで続いていることを表しています。even biggerのevenは比較級の前に置いて『さらに・いっそう』と差を強めます。I'm happy to know that ...のto不定詞は、うれしいと感じた原因（～を知って）を表します。お礼のメールでは、これらの表現で『長く利用してきたこと』と『今の気持ち』が伝えられています。",
            "My grandmother has been going to your store for over twenty years / Our family has enjoyed shopping at your store for a long time / now we are even bigger fans of your store / I'm happy to know that there are people like Mark helping my grandmother",
            "大問4A メール第1・3段落",
            [
                {"en": "My grandmother has been going to your store for over twenty years.", "ja": "私の祖母は20年以上、そちらのお店に通っています。", "note": "has been going＝ずっと通い続けている（現在完了進行形）。for over twenty years＝20年以上の間。"},
                {"en": "However, because of Mark's help, now we are even bigger fans of your store.", "ja": "でも、マークさんが助けてくださったおかげで、今ではますますそちらのお店のファンになりました。", "note": "even＋比較級＝さらに～・いっそう～。because of＋名詞＝～のおかげで・～のために。"},
                {"en": "I'm happy to know that there are people like Mark helping my grandmother.", "ja": "マークさんのような方が祖母を助けてくださっていると知って、うれしく思います。", "note": "be happy to do＝～してうれしい（不定詞が感情の原因を表す）。helping my grandmotherはpeople like Markを後ろから説明する現在分詞。"},
            ],
            "[出典: Helpful employee 第1・3段落]\nI'm writing to you about one of your employees at the downtown store. My grandmother has been going to your store for over twenty years. She always has nice things to say about your staff. Our family has enjoyed shopping at your store for a long time. However, because of Mark's help, now we are even bigger fans of your store. I'm happy to know that there are people like Mark helping my grandmother.",
            "ダウンタウン店の従業員の方のことでご連絡いたします。私の祖母は20年以上、そちらのお店に通っています。祖母はいつも、店員の皆さんのことをほめています。私たち家族は長い間、そちらのお店での買い物を楽しんできました。でも、マークさんが助けてくださったおかげで、今ではますますそちらのお店のファンになりました。マークさんのような方が祖母を助けてくださっていると知って、うれしく思います。",
            ["has been going to your store for over twenty years", "has enjoyed shopping at your store for a long time", "even bigger fans of your store", "I'm happy to know that"],
            "継続・強調",
            [
                {"q": "My grandmother has been going to your store for over twenty years.は、どのような意味ですか？", "a": "『祖母は20年以上、そちらのお店に通い続けています』という意味です。現在完了進行形で、過去から今まで続いていることを表しています。"},
                {"q": "Our family has enjoyed shopping at your store for a long time.から、ジョイスの家族についてどんなことがわかりますか？", "a": "長い間ずっと、その店での買い物を楽しんできたことがわかります。enjoy doingは『～するのを楽しむ』です。"},
                {"q": "even bigger fansのevenがあると、どのような意味になりますか？", "a": "『（もともとファンだったが）さらに大きなファンに』と、差が強調されます。前の文で長く買い物を楽しんできたと述べているので、もともとファンだったことがわかります。"},
                {"q": "I'm happy to know that ...のto knowは何を表していますか？", "a": "うれしいと感じた原因（～を知って）です。マークのような人が祖母を助けてくれていると知ってうれしい、という意味です。"},
            ],
        ),
        fp(
            "fp4",
            "いろいろな形の受け身",
            "Passive Voice in Different Forms",
            "受け身（be動詞＋過去分詞）は『～される』を表し、説明文でよく使われます。この文章では、are no longer published（もう発行されていない）、stopped being printed（印刷されなくなった：being＋過去分詞は動名詞の受け身）、was published again（再び発行された）、is considered ～（～だと考えられている）、can be found（見つけられる：助動詞＋be＋過去分詞）のように、さまざまな形で出てきます。be動詞や助動詞の部分で時制や意味を、過去分詞の部分で動作の内容をとらえましょう。",
            "many magazines are no longer published at all / This magazine stopped being printed in 2018 / the magazine is considered special and rare / that information can be found easily on social media",
            "大問4B「Magazines in the Digital Age」第1・3・4段落",
            [
                {"en": "This magazine stopped being printed in 2018 because sales were too low.", "ja": "この雑誌は売り上げが少なすぎたため、2018年に印刷されなくなりました。", "note": "stop doing＝～するのをやめる。being printedは動名詞の受け身（印刷されること）。"},
                {"en": "The new style of the magazine is popular with music fans because the magazine is considered special and rare.", "ja": "特別で珍しいものと考えられているため、新しい形のこの雑誌は音楽ファンに人気があります。", "note": "be considered＋形容詞＝～だと考えられている。be popular with ～＝～に人気がある。"},
                {"en": "Magazines about fashion or famous people did not survive because that information can be found easily on social media.", "ja": "ファッションや有名人についての雑誌は、そうした情報がソーシャルメディアで簡単に見つかるため、生き残れませんでした。", "note": "can be found＝見つけられる（助動詞＋be＋過去分詞）。that informationはファッションや有名人についての情報を指す。"},
            ],
            "[出典: Magazines in the Digital Age 第1・3・4段落]\nSince 2012, the number of magazine companies in the United States has dropped by over 30 percent, and many magazines are no longer published at all. Another way for print magazines to survive is by improving quality. A good example is the UK music magazine NME. This magazine stopped being printed in 2018 because sales were too low. However, in 2023, a new version was published again with a higher price, better content, and more pages. The new style of the magazine is popular with music fans because the magazine is considered special and rare. Magazines about fashion or famous people did not survive because that information can be found easily on social media.",
            "2012年以降、アメリカの雑誌会社の数は30パーセント以上減り、多くの雑誌がまったく発行されなくなりました。紙の雑誌が生き残るもう一つの方法は、質を高めることです。そのよい例が、イギリスの音楽雑誌『NME』です。この雑誌は売り上げが少なすぎたため、2018年に印刷されなくなりました。しかし2023年に、より高い価格で、よりよい内容と、より多くのページを備えた新しい版が再び発行されました。特別で珍しいものと考えられているため、新しい形のこの雑誌は音楽ファンに人気があります。ファッションや有名人についての雑誌は、そうした情報がソーシャルメディアで簡単に見つかるため、生き残れませんでした。",
            ["are no longer published at all", "stopped being printed in 2018", "was published again", "is considered special and rare", "can be found easily on social media"],
            "受け身",
            [
                {"q": "many magazines are no longer published at allは、どのような意味ですか？", "a": "『多くの雑誌がまったく発行されなくなった』という意味です。no longerは『もう～ない』、at allは否定を強めて『まったく』を表します。"},
                {"q": "stopped being printedと、第2段落のhave stopped printingは、どう違いますか？", "a": "have stopped printing their magazinesは『（会社が）雑誌を印刷するのをやめた』、stopped being printedは『（雑誌が）印刷されなくなった』という受け身の意味です。主語がThis magazineなので受け身になっています。"},
                {"q": "the magazine is considered special and rareのis consideredは、どのような意味ですか？", "a": "『～だと考えられている』という意味です。人々がこの雑誌を特別で珍しいものだと考えていることを、受け身で表しています。"},
                {"q": "that information can be found easily on social mediaのcan be foundは、どのような意味ですか？", "a": "『見つけることができる』という意味です。助動詞canの後にbe＋過去分詞が続いた受け身で、そうした情報がソーシャルメディアで簡単に見つかることを表しています。"},
            ],
        ),
        fp(
            "fp5",
            "今回の重要なパラフレーズ",
            "Key Paraphrases in This Exam",
            "大問4の正解の選択肢は、本文と同じ内容を別の語句で言い換えていることがよくあります。たとえばQ24のfind items with lower prices.は、He even helped her find cheaper options.の言い換えで、cheaper options（より安い選択肢）がitems with lower prices（より低い値段の品物）に変わっています。反対に、本文に出てくる語句（glasses, bus, social mediaなど）を使っていても、内容が本文と違う選択肢は不正解です。根拠の文と意味が同じかどうかを確かめて選びましょう。",
            "①Your employee Mark Brown was a big help → A staff member did something special.（従業員のマークが大いに助けてくれた→ある店員が特別なことをしてくれた）\n②He even helped her find cheaper options → find items with lower prices.（より安い選択肢を見つけるのを手伝った→より安い値段の品物を見つける）\n③my family and I really want to say thank you for what he did for her → Thank Mark for them.（家族と私が感謝を伝えたい→家族に代わってマークにお礼を言う）\n④the number of magazine companies in the United States has dropped by over 30 percent → the number of magazine companies in the United States to decrease.（30パーセント以上減った→減少する）\n⑤people trust magazines more than blogs or social media → They believe the information is more likely to be true than other sources.（ブログやソーシャルメディアより雑誌を信頼する→ほかの情報源より正しい可能性が高いと信じている）\n⑥The magazine was printed in small numbers → there are only limited numbers available.（少部数で印刷された→限られた数しか手に入らない）\n⑦written by experts → Magazines written by specialists about serious topics.（専門家によって書かれた→専門家が書いた、まじめな話題についての雑誌）",
            "大問4A・4B（Q23〜Q29）",
            [
                {"en": "Since 2012, the number of magazine companies in the United States has dropped by over 30 percent, and many magazines are no longer published at all.", "ja": "2012年以降、アメリカの雑誌会社の数は30パーセント以上減り、多くの雑誌がまったく発行されなくなりました。", "note": "Q26：has dropped（減った）→ to decrease（減少する）。The arrival of the Internet caused ～ to decrease.のcause A to doの形に合わせて言い換えられている。"},
                {"en": "Sales of online magazines are still high because people trust magazines more than blogs or social media.", "ja": "人々はブログやソーシャルメディアよりも雑誌を信頼しているので、オンライン雑誌の売り上げは今でも高いのです。", "note": "Q27：trust magazines more than blogs or social media → believe the information is more likely to be true than other sources。blogs or social media → other sources。"},
                {"en": "Print magazines that are still successful are those that are written by experts and offer the readers something that cannot be found easily online.", "ja": "今でも成功している紙の雑誌は、専門家によって書かれ、インターネットでは簡単に見つからないものを読者に提供している雑誌です。", "note": "Q29：written by experts → written by specialists。still successful → still popular。thoseはmagazinesの代わり。"},
            ],
            "[出典: Magazines in the Digital Age 第2〜4段落]\nTo survive, many magazine companies have stopped printing their magazines and publish online instead. Readers pay to access the magazine through their smartphones or computers. This is more convenient for readers because they no longer have to buy magazines from stores. It is also cheaper for the magazine company because there is no need for printing. Sales of online magazines are still high because people trust magazines more than blogs or social media. The magazine was printed in small numbers and published only every two months. The new style of the magazine is popular with music fans because the magazine is considered special and rare. NME has become a valuable item for people who collect magazines. Print magazines that are still successful are those that are written by experts and offer the readers something that cannot be found easily online. These are mainly magazines about business, news, and other global issues.",
            "生き残るために、多くの雑誌会社は雑誌の印刷をやめ、代わりにオンラインで発行しています。読者は料金を払い、スマートフォンやコンピューターで雑誌を閲覧します。読者はもう店で雑誌を買う必要がないので、これは読者にとってより便利です。また、印刷の必要がないので、雑誌会社にとっても費用が安く済みます。人々はブログやソーシャルメディアよりも雑誌を信頼しているので、オンライン雑誌の売り上げは今でも高いのです。（新しい『NME』は）少部数だけ印刷され、2か月に1回しか発行されませんでした。特別で珍しいものと考えられているため、新しい形のこの雑誌は音楽ファンに人気があります。『NME』は、雑誌を収集する人々にとって価値のある品になっています。今でも成功している紙の雑誌は、専門家によって書かれ、インターネットでは簡単に見つからないものを読者に提供している雑誌です。それらは主に、ビジネスやニュース、そのほかの世界的な問題を扱う雑誌です。",
            ["Mark Brown was a big help", "cheaper options", "really want to say thank you", "has dropped by over 30 percent", "people trust magazines more than blogs or social media", "printed in small numbers", "written by experts"],
            "パラフレーズ",
            [
                {"q": "Q27の正解They believe the information is more likely to be true than other sources.は、第2段落のどの表現の言い換えですか？", "a": "people trust magazines more than blogs or social mediaです。ブログやソーシャルメディアより雑誌を信頼している、という内容が、ほかの情報源より正しい可能性が高いと信じている、に言い換えられています。"},
                {"q": "Q27の『They prefer to read magazines on a device for free.』は正しいですか？", "a": "誤りです。Readers pay to access the magazineとあり、オンライン雑誌も料金を払って読みます。"},
                {"q": "Q28の正解there are only limited numbers available.は、第3段落のどの表現の言い換えですか？", "a": "The magazine was printed in small numbers（少部数だけ印刷された）です。the magazine is considered special and rare（特別で珍しいと考えられている）も根拠になります。"},
                {"q": "Q29の『Magazines discussing the entertainment world.』は正しいですか？", "a": "誤りです。ファッションや有名人についての雑誌は、その情報がソーシャルメディアで簡単に見つかるため生き残れなかったと書かれています。"},
            ],
        ),
    ]
    return {"focusPoints": points}

"""Generate lessonPlan with 5 focusPoints for Pre-Grade 2 2022-3"""
import json, os

base = r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade-pre2\2022-3"
data = json.load(open(os.path.join(base, "_part2.json"), "r", encoding="utf-8"))

# 既存FPトピック（重複回避）:
# 2023-1: 過去完了形, too...to/enough to, 接続副詞, 受動態
# 2023-2: 関係代名詞制限用法, 比較構文, 受動態と能動態, 結果・理由の接続
# 2023-3: 過去完了, 受動態, 使役構文make, 目的・理由の接続
# 2024-1~: 助言/因果, 目的/提案, 理由/結果, 逆接, etc.
#
# 2022-3で使える新しいトピック:
# FP1: 不定詞の名詞用法・副詞用法（大問3B, 4B）
# FP2: 動名詞の受動態と動詞＋動名詞（大問1 Q20, 大問4B）
# FP3: 関係副詞 where の用法（大問3B, 4A）
# FP4: so...that 構文（大問4B）

data["lessonPlan"] = {
    "focusPoints": [
        {
            "id": "fp1",
            "title": "不定詞の副詞用法（目的・結果）",
            "subtitle": "Infinitives as Adverbs (Purpose & Result)",
            "explanation": "不定詞（to + 動詞の原形）が「～するために」（目的）や「…した結果～」（結果）を表す用法です。文の中で副詞的な役割を果たし、動作の理由や結果を説明します。",
            "sourceQuote": "After leaving high school, he went to college to study how to design buildings.",
            "sourceLocation": "Part 3B 第1段落",
            "examples": [
                {
                    "en": "He went to college to study how to design buildings.",
                    "ja": "彼は建物の設計方法を学ぶために大学に進んだ。",
                    "note": "to study = 目的「～するために」"
                },
                {
                    "en": "Heather ran to Mr. Jones's house to ask if she could borrow it.",
                    "ja": "ヘザーはそれを借りられるか聞くためにジョーンズさんの家に走って行った。",
                    "note": "to ask = 目的「～するために」"
                },
                {
                    "en": "A graphic artist is an artist who uses imagination, math, and tools like rulers to produce pictures.",
                    "ja": "グラフィックアーティストとは、想像力、数学、定規などの道具を使って絵を制作するアーティストのことである。",
                    "note": "to produce = 目的「～するために」"
                }
            ],
            "practicePassage": {
                "en": "[出典: Escher's Amazing Art 第1段落]\nMaurits Cornelis Escher was born in the Netherlands in 1898. After leaving high school, he went to college to study how to design buildings. However, he soon realized that he was not interested in construction. In fact, he liked designing things that could not be built. He decided to study graphic art instead. A graphic artist is an artist who uses imagination, math, and tools like rulers to produce pictures.",
                "ja": "マウリッツ・コルネリス・エッシャーは1898年にオランダで生まれた。高校を卒業した後、建物の設計を学ぶために大学に進んだ。しかし、彼はすぐに自分が建設に興味がないことに気づいた。実際、彼は建てることができないものを設計するのが好きだった。代わりにグラフィックアートを学ぶことにした。グラフィックアーティストとは、想像力、数学、定規などの道具を使って絵を制作するアーティストのことである。",
                "audioFile": "audio/practice_pp1.mp3"
            },
            "practiceQuestions": [
                {"q": "エッシャーは何のために大学に行きましたか？", "a": "建物の設計方法を学ぶため（to study how to design buildings）"},
                {"q": "「to study」と「to produce」の不定詞はどちらも何を表していますか？", "a": "目的（～するために）を表す副詞用法"},
                {"q": "「He decided to study graphic art instead.」の to study は何用法ですか？", "a": "名詞用法（decided の目的語として「～すること」を表す）"},
                {"q": "不定詞の副詞用法と名詞用法の見分け方は？", "a": "「～するために」と訳せれば副詞用法、「～すること」と訳せれば名詞用法"}
            ],
            "highlightPatterns": [
                "he went to college to study how to design buildings",
                "He decided to study graphic art instead",
                "uses imagination, math, and tools like rulers to produce pictures",
                "Heather ran to Mr. Jones's house to ask if she could",
                "they use their claws to hang on to branches",
                "it can use its claws to defend itself"
            ],
            "highlightColor": "#4f8cff",
            "highlightLabel": "不定詞（目的）"
        },
        {
            "id": "fp2",
            "title": "動名詞の重要パターン",
            "subtitle": "Key Gerund Patterns",
            "explanation": "動名詞（～ing形）は動詞の名詞化で、主語・目的語・前置詞の目的語として使います。特に「hate/enjoy/remember + ～ing」や「By ～ing（～することによって）」などの重要パターンがよく出題されます。",
            "sourceQuote": "By sleeping most of the time and moving slowly, sloths do not have to use much energy.",
            "sourceLocation": "Part 4B 第2段落",
            "examples": [
                {
                    "en": "By sleeping most of the time and moving slowly, sloths do not have to use much energy.",
                    "ja": "ほとんどの時間を寝てゆっくり動くことで、ナマケモノは多くのエネルギーを使う必要がない。",
                    "note": "By ～ing = 「～することによって」手段・方法"
                },
                {
                    "en": "He hates being treated like a little child.",
                    "ja": "彼は小さな子供のように扱われるのが嫌いだ。",
                    "note": "hate + being + 過去分詞 = 動名詞の受動態"
                },
                {
                    "en": "Heather remembered seeing her neighbor using one to sweep his yard.",
                    "ja": "ヘザーは隣人がほうきを使って庭を掃いているのを見たことを思い出した。",
                    "note": "remember + ～ing = 「～したことを覚えている」"
                }
            ],
            "practicePassage": {
                "en": "[出典: A Slow Life in the Trees 第2段落]\nSloths' lazy lifestyles help them to survive. By sleeping most of the time and moving slowly, sloths do not have to use much energy. They do not have to travel long distances or run fast to get something to eat. High up in the trees, a tasty leaf is always just a few centimeters away. Even though leaves do not contain many calories, sloths get all they need by eating all the time during the short time that they are awake.",
                "ja": "ナマケモノの怠惰な生活様式は生存に役立っている。ほとんどの時間を寝てゆっくり動くことで、ナマケモノは多くのエネルギーを使う必要がない。食べ物を得るために長距離を移動したり速く走ったりする必要がない。木の上高くでは、おいしい葉がいつもほんの数センチ先にある。葉にはカロリーが少ないが、ナマケモノは起きている短い時間の間ずっと食べ続けることで必要なものをすべて得ている。",
                "audioFile": "audio/practice_pp2.mp3"
            },
            "practiceQuestions": [
                {"q": "「By sleeping most of the time」の By ～ing は何を表していますか？", "a": "手段・方法（～することによって）"},
                {"q": "「by eating all the time」も同じパターンですが、何を意味していますか？", "a": "ずっと食べ続けることによって（必要な栄養を得る手段）"},
                {"q": "remember ～ing と remember to ～ の違いは？", "a": "remember ～ing は「～したことを覚えている」（過去）、remember to ～は「～するのを忘れない」（未来）"},
                {"q": "動名詞の受動態（being + 過去分詞）の例を作ってみましょう", "a": "例: She doesn't like being called by her nickname.（彼女はあだ名で呼ばれるのが好きではない）"}
            ],
            "highlightPatterns": [
                "By sleeping most of the time and moving slowly",
                "sloths get all they need by eating all the time",
                "moving slowly also protects sloths from hungry meat eaters",
                "Heather remembered seeing her neighbor, Mr. Jones, using one to sweep his yard",
                "he liked designing things that could not be built"
            ],
            "highlightColor": "#34d399",
            "highlightLabel": "動名詞"
        },
        {
            "id": "fp3",
            "title": "関係代名詞 who / that / where",
            "subtitle": "Relative Pronouns & Adverbs",
            "explanation": "関係代名詞（who, which, that）は先行詞を修飾する節を導きます。whoは人、whichは物、thatは両方に使えます。関係副詞whereは場所を表す先行詞を修飾します。",
            "sourceQuote": "he went to a castle where the walls were covered with interesting patterns",
            "sourceLocation": "Part 3B 第2段落",
            "examples": [
                {
                    "en": "Heather's favorite character is a witch who rides a broom and delivers mail.",
                    "ja": "ヘザーのお気に入りのキャラクターはほうきに乗って郵便を届ける魔女だ。",
                    "note": "who = 人を表す先行詞(a witch)を修飾"
                },
                {
                    "en": "He went to a castle where the walls were covered with interesting patterns.",
                    "ja": "彼は壁が面白い模様で覆われた城を訪問した。",
                    "note": "where = 場所を表す先行詞(a castle)を修飾"
                },
                {
                    "en": "A sloth is a kind of animal that lives in the jungles of Central and South America.",
                    "ja": "ナマケモノは中南米のジャングルに住む動物の一種だ。",
                    "note": "that = 動物(an animal)を修飾する関係代名詞"
                }
            ],
            "practicePassage": {
                "en": "[出典: Escher's Amazing Art 第2段落]\nAfter Escher graduated, he traveled for a long time in Italy. He really liked the countryside and the old buildings there. He often drew the places that he saw there in his pictures. He also visited Spain. There, he went to a castle where the walls were covered with interesting patterns. They gave him ideas for his own patterns, and he would sometimes use the shapes of animals in these designs. His experiences in these two countries had a very big effect on his art.",
                "ja": "エッシャーは卒業後、長い間イタリアを旅行した。彼はそこの田園風景や古い建物がとても気に入った。そこで見た場所をよく絵に描いた。彼はスペインも訪れた。そこでは壁が面白い模様で覆われた城を訪問した。それらは彼独自の模様のアイデアを与え、動物の形をデザインに使うこともあった。彼のこれら2つの国での経験は、彼の芸術に非常に大きな影響を与えた。",
                "audioFile": "audio/practice_pp3.mp3"
            },
            "practiceQuestions": [
                {"q": "「the places that he saw there」の that は何を修飾していますか？", "a": "the places（場所）を修飾する関係代名詞"},
                {"q": "「a castle where the walls were covered」の where はなぜ使われていますか？", "a": "先行詞が場所（a castle）なので関係副詞 where を使う"},
                {"q": "who と that はどう使い分けますか？", "a": "who は人のみ、that は人・物両方に使える。日常会話では that がより一般的"},
                {"q": "「an artist who uses imagination」を that に置き換えられますか？", "a": "はい。an artist that uses imagination も正しい"}
            ],
            "highlightPatterns": [
                "a witch who rides a broom and delivers mail",
                "a castle where the walls were covered with interesting patterns",
                "A sloth is a kind of animal that lives in the jungles",
                "the places that he saw there in his pictures",
                "an artist who uses imagination, math, and tools like rulers",
                "people are climbing stairs that return to the place where they started"
            ],
            "highlightColor": "#f472b6",
            "highlightLabel": "関係代名詞/副詞"
        },
        {
            "id": "fp4",
            "title": "so...that構文と結果表現",
            "subtitle": "So...That Construction & Result Expressions",
            "explanation": "「so + 形容詞/副詞 + that ～」で「とても…なので～」という結果を表します。as a result（その結果）などの接続表現も結果を示します。",
            "sourceQuote": "Sloths' claws are so long that sloths find it difficult to walk on the ground.",
            "sourceLocation": "Part 4B 第4段落",
            "examples": [
                {
                    "en": "Sloths' claws are so long that sloths find it difficult to walk on the ground.",
                    "ja": "ナマケモノの爪は非常に長いので、地面を歩くのが難しい。",
                    "note": "so + 形容詞(long) + that ～ = とても長いので～"
                },
                {
                    "en": "Also, sloths do not clean their fur completely. As a result, tiny plants grow in it.",
                    "ja": "また、ナマケモノは毛皮を完全にきれいにしない。その結果、小さな植物が毛皮に生える。",
                    "note": "As a result = 結果を表す接続表現"
                },
                {
                    "en": "People in many countries like his pictures because they are beautiful and they make people think.",
                    "ja": "多くの国の人々が彼の絵を好むのは、それらが美しく、人々に考えさせるからである。",
                    "note": "because = 理由。make + O + V(原形) = 使役構文"
                }
            ],
            "practicePassage": {
                "en": "[出典: A Slow Life in the Trees 第3-4段落]\nSurprisingly, moving slowly also protects sloths from hungry meat eaters. Eagles and big cats live in the same jungles as sloths. However, these hunters search for movement, so they often do not notice sloths. Also, sloths do not clean their fur completely. As a result, tiny plants grow in it, and these make the fur look green. From the ground or the sky, a sloth in a tree's branches looks like a plant rather than something that an eagle or a big cat wants to eat. Sloths have long, hard claws on their toes. Usually, they use their claws to hang on to branches. However, if a sloth is attacked, it can use its claws to defend itself. Sloths' claws are so long that sloths find it difficult to walk on the ground. Because of this, a sloth usually only comes down from the branches about once a week.",
                "ja": "驚くことに、ゆっくり動くことはナマケモノを空腹の肉食動物からも守っている。ワシや大型の猫科動物はナマケモノと同じジャングルに住んでいる。しかし、これらの捕食者は動きを探すので、ナマケモノに気づかないことが多い。また、ナマケモノは毛皮を完全にきれいにしない。その結果、小さな植物が毛皮に生え、毛皮を緑色に見せる。地面や空からは、木の枝にいるナマケモノは植物のように見える。ナマケモノの足の指には長く硬い爪がある。通常、爪を使って枝にぶら下がっている。しかし、ナマケモノが攻撃されると、爪を使って自分を守ることができる。ナマケモノの爪は非常に長いので、地面を歩くのが難しい。このため、ナマケモノは通常、週に約1回しか枝から降りてこない。",
                "audioFile": "audio/practice_pp4.mp3"
            },
            "practiceQuestions": [
                {"q": "「so long that」構文を日本語で説明してください", "a": "「とても長いので～」。程度とその結果を表す構文"},
                {"q": "「As a result」の代わりに使える表現は？", "a": "Therefore, Consequently, Because of this, For this reason など"},
                {"q": "「Because of this」は何の結果を指していますか？", "a": "爪が長すぎて地面を歩けないこと。その結果、週1回しか降りてこない"},
                {"q": "so...that と too...to の違いは？", "a": "so...that は結果を述べる（できる/できない）、too...to は「～すぎて…できない」（否定的結果のみ）"}
            ],
            "highlightPatterns": [
                "are so long that sloths find it difficult to walk on the ground",
                "As a result, tiny plants grow in it",
                "Because of this, a sloth usually only comes down from the branches about once a week",
                "these hunters search for movement, so they often do not notice sloths",
                "they are beautiful and they make people think"
            ],
            "highlightColor": "#fbbf24",
            "highlightLabel": "結果表現"
        },
        {
            "id": "fp5",
            "title": "パラフレーズの読解力",
            "subtitle": "Paraphrase Reading Comprehension",
            "explanation": "英検では、本文中の表現が設問や選択肢で別の言葉に言い換え（パラフレーズ）されます。同じ意味を違う言葉で表現する力が読解の鍵です。",
            "sourceQuote": "sloths live alone → Sloths usually live by themselves",
            "sourceLocation": "Part 4B",
            "examples": [
                {
                    "en": "本文: sloths live alone → 選択肢: Sloths usually live by themselves.",
                    "ja": "live alone（単独で暮らす）= live by themselves（自分たちだけで暮らす）",
                    "note": "alone → by themselves のパラフレーズ"
                },
                {
                    "en": "本文: they use their claws to hang on to branches → 選択肢: help it to hold on to branches",
                    "ja": "hang on to（しがみつく）= hold on to（つかまる）",
                    "note": "hang on to → hold on to のパラフレーズ"
                },
                {
                    "en": "本文: sloths do not have to use much energy → 選択肢: reduce the amount of energy that they use",
                    "ja": "多くのエネルギーを使わなくてよい = エネルギー量を減らす",
                    "note": "not use much → reduce the amount of の言い換え"
                }
            ],
            "practicePassage": {
                "en": "[出典: Cooking Club Recipes 第1-2段落]\nI really enjoy our weekly cooking club meetings at the community center. All the members are so friendly. It's nice that the members take turns teaching each other recipes. I get nervous when it's my turn to teach, but I'm always happy afterward. Also, I've learned how to make a really wide variety of dishes this way. It's much better than having just one cooking teacher. I was telling my friend David about our meetings. David works as a photographer and designer for a company that publishes books. He suggested that the cooking club members make a book of our favorite recipes. He said that he would help us to do it.",
                "ja": "コミュニティセンターでの毎週の料理クラブの集まりがとても楽しいです。メンバーみんなとてもフレンドリーです。メンバーが交代でレシピを教え合うのが素敵ですね。自分が教える番になると緊張しますが、終わった後はいつも嬉しいです。また、この方法で本当にさまざまな料理の作り方を学びました。料理の先生が1人だけよりずっと良いです。友人のデイビッドに集まりのことを話していました。デイビッドは本を出版する会社でカメラマンとデザイナーとして働いています。彼は料理クラブのメンバーでお気に入りレシピの本を作ることを提案しました。",
                "audioFile": "audio/practice_pp5.mp3"
            },
            "practiceQuestions": [
                {"q": "「take turns teaching each other」を別の言葉で言い換えると？", "a": "members teach each other one by one / the way that members teach each other"},
                {"q": "「live alone」と「live by themselves」が同じ意味だと見抜くコツは？", "a": "alone = by oneself（自分自身で）は基本的なパラフレーズ。代名詞の変化に注意"},
                {"q": "「suggested that the members make a book」のパラフレーズを考えてみましょう", "a": "The members of the club should produce a book.（produce = make のパラフレーズ）"},
                {"q": "パラフレーズを見抜くための3つのポイントは？", "a": "1. 同義語の置き換え 2. 能動態⇔受動態の変換 3. 具体⇔抽象の言い換え"}
            ],
            "highlightPatterns": [
                "the members take turns teaching each other recipes",
                "He suggested that the cooking club members make a book",
                "sloths live alone, move very slowly",
                "they use their claws to hang on to branches",
                "sloths do not have to use much energy"
            ],
            "highlightColor": "#f59e0b",
            "highlightLabel": "パラフレーズ"
        }
    ]
}

# Save final data.json
output_path = os.path.join(base, "data.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"data.json saved to {output_path}")
print(f"FocusPoints: {len(data['lessonPlan']['focusPoints'])}")
for fp in data['lessonPlan']['focusPoints']:
    print(f"  {fp['id']}: {fp['title']} ({len(fp['highlightPatterns'])} patterns)")

"""Generate lessonPlan with 5 focusPoints for Pre-Grade 2 2022-2"""
import json, os

base = r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade-pre2\2022-2"
data = json.load(open(os.path.join(base, "_part2.json"), "r", encoding="utf-8"))

# 既存FPトピック（重複回避）:
# 2022-3: 不定詞副詞用法, 動名詞パターン, 関係代名詞who/that/where, so...that, パラフレーズ
# 2023-1: 過去完了形, too...to/enough to, 接続副詞, 受動態
# 2023-2: 関係代名詞制限用法, 比較構文, 受動態と能動態, 結果・理由の接続
# 2023-3: 過去完了, 受動態, 使役構文make, 目的・理由の接続
# → 2022-2で使える新しいトピック: 受動態+by, 比較級/最上級の応用, 接続詞as/while/after, 分詞(過去分詞の形容詞用法), 代名詞one/the others

data["lessonPlan"] = {
    "focusPoints": [
        {
            "id": "fp1",
            "title": "受動態の多様な形",
            "subtitle": "Various Forms of Passive Voice",
            "explanation": "受動態（be + 過去分詞）は「～される」を表しますが、進行形受動態（is being + 過去分詞）や完了形受動態（has been + 過去分詞）、助動詞付き受動態（can be + 過去分詞）など多様な形があります。",
            "sourceQuote": "new laws and special parks are being created to protect nature",
            "sourceLocation": "Part 3B 第1段落",
            "examples": [
                {"en": "New laws and special parks are being created to protect nature.", "ja": "自然を守るために新しい法律や特別な公園が作られている。", "note": "are being created = 現在進行形の受動態"},
                {"en": "It was invented in Ireland in the 1850s.", "ja": "1850年代にアイルランドで発明された。", "note": "was invented = 過去形の受動態 + by省略"},
                {"en": "Eight movies are going to be shown over two days.", "ja": "2日間で8本の映画が上映される予定だ。", "note": "are going to be shown = 未来の受動態"}
            ],
            "practicePassage": {
                "en": "[出典: Hungry Hikers 第1段落]\nPeople are having a bigger and bigger effect on wild animals. As a result, new laws and special parks are being created to protect nature. Some changes have been very successful. For example, there were about 170 wild elephants in 1980 in Yunnan, China. These days, experts think that there are around 300 elephants there. However, the elephants have less space to live in. As cities get bigger and more farms are needed to feed people, there are not as many places for animals like elephants.",
                "ja": "人々は野生動物にますます大きな影響を与えている。その結果、自然を守るために新しい法律や特別な公園が作られている。一部の変化は非常に成功している。例えば、1980年の中国雲南省には約170頭の野生の象がいた。現在、専門家はそこに約300頭の象がいると考えている。しかし、象は住む場所が減っている。都市が大きくなり人々を養うためにより多くの農地が必要になるにつれ、象のような動物の場所は減っている。",
                "audioFile": "audio/practice_pp1.mp3"
            },
            "practiceQuestions": [
                {"q": "「are being created」はどんな受動態ですか？", "a": "現在進行形の受動態（am/is/are + being + 過去分詞）。今まさに作られている最中を表す"},
                {"q": "「was invented」の by 以下が省略されている理由は？", "a": "行為者が不明または重要でない場合、by ～は省略できる"},
                {"q": "「are needed to feed people」を能動態に言い換えると？", "a": "People need more farms to feed people. → We need more farms to feed people."},
                {"q": "「are going to be shown」はどう訳しますか？", "a": "上映される予定だ（be going to + be + 過去分詞＝未来の受動態）"}
            ],
            "highlightPatterns": [
                "new laws and special parks are being created to protect nature",
                "It was invented in Ireland in the 1850s",
                "the type that is most popular today was created by a man called John McLaughlin",
                "Eight movies are going to be shown over two days at the festival",
                "They've all been chosen by the director of Burning Fist",
                "more farms are needed to feed people"
            ],
            "highlightColor": "#4f8cff",
            "highlightLabel": "受動態"
        },
        {
            "id": "fp2",
            "title": "時を表す接続詞 while / after / when",
            "subtitle": "Time Conjunctions: while, after, when",
            "explanation": "while（～している間に）、after（～した後に）、when（～した時に）は文と文をつなぐ接続詞です。whileは同時進行、afterは順序、whenは特定の時点を表します。",
            "sourceQuote": "While studying, he worked part-time at a drugstore.",
            "sourceLocation": "Part 4B 第1段落",
            "examples": [
                {"en": "While studying, he worked part-time at a drugstore.", "ja": "勉強しながら、ドラッグストアでアルバイトをしていた。", "note": "While ～ing = ～している間に（主語が同じ時の省略形）"},
                {"en": "After watching it last Saturday, my mom took me to a bookstore.", "ja": "先週の土曜日にそれを見た後、ママが本屋に連れて行ってくれた。", "note": "After ～ing = ～した後に"},
                {"en": "After she hangs up, she soon starts to miss them again.", "ja": "電話を切った後、またすぐに恋しくなる。", "note": "After + S + V = ～した後に（完全な節）"}
            ],
            "practicePassage": {
                "en": "[出典: Spicy Soda 第1段落]\nGinger ale is a spicy soft drink. It was invented in Ireland in the 1850s. However, the type that is most popular today was created by a man called John McLaughlin who lived in Toronto, Canada. After he graduated from college in Canada, he went to study in New York City. While studying, he worked part-time at a drugstore. He noticed that many people were buying soda water from the store and mixing it with different fruit flavors.",
                "ja": "ジンジャーエールはスパイシーな清涼飲料水だ。1850年代にアイルランドで発明された。しかし、今日最も人気のあるタイプは、カナダのトロントに住んでいたジョン・マクラフリンという男性によって作られた。カナダの大学を卒業した後、ニューヨーク市に留学した。勉強しながらドラッグストアでアルバイトをしていた。多くの人がソーダ水を買ってさまざまなフルーツフレーバーと混ぜていることに気づいた。",
                "audioFile": "audio/practice_pp2.mp3"
            },
            "practiceQuestions": [
                {"q": "「While studying」を省略しない形に書き換えると？", "a": "While he was studying（主語+be動詞が省略されている）"},
                {"q": "「After he graduated」と「After graduating」はどう違いますか？", "a": "意味は同じ。主語が同じ場合、After ～ingに短縮できる"},
                {"q": "while と during の違いは？", "a": "while は接続詞（後ろに節）、during は前置詞（後ろに名詞）。While I was sleeping = During my sleep"},
                {"q": "「When my parents were young」の when はどんな働きですか？", "a": "時を表す接続詞。「～した時」という意味で副詞節を導く"}
            ],
            "highlightPatterns": [
                "While studying, he worked part-time at a drugstore",
                "After watching it last Saturday, my mom took me to a bookstore",
                "After he graduated from college in Canada, he went to study in New York City",
                "While I was at the bookstore, I saw a poster for an action movie festival",
                "After she hangs up, she soon starts to miss them again",
                "When my parents were young, a milkman brought milk to their homes every day"
            ],
            "highlightColor": "#34d399",
            "highlightLabel": "時の接続詞"
        },
        {
            "id": "fp3",
            "title": "比較表現の応用パターン",
            "subtitle": "Advanced Comparison Patterns",
            "explanation": "比較級・最上級の応用表現には序数+最上級（the second-largest）、比較級+and+比較級（bigger and bigger）、not as...as（同程度でない）などがあります。",
            "sourceQuote": "People are having a bigger and bigger effect on wild animals.",
            "sourceLocation": "Part 3B 第1段落",
            "examples": [
                {"en": "People are having a bigger and bigger effect on wild animals.", "ja": "人々は野生動物にますます大きな影響を与えている。", "note": "比較級 and 比較級 = ますます～（変化の強調）"},
                {"en": "Barcelona is the second-largest city in Spain.", "ja": "バルセロナはスペインで2番目に大きい都市だ。", "note": "序数 + 最上級 = N番目に～な"},
                {"en": "There are not as many places for animals like elephants.", "ja": "象のような動物のための場所はそれほど多くない。", "note": "not as...as = ～ほど…ない"}
            ],
            "practicePassage": {
                "en": "[出典: Hungry Hikers 第2-3段落]\nBig animals can cause big problems for people. Because there is not enough food in protected areas, elephants often leave these areas to take food from farms. In fact, a group of about 14 elephants from Yunnan went on a 500-kilometer walk to look for food during 2020 and 2021. The elephants sometimes went through towns trying to find food. They appeared on the TV news and the Internet. As a result, they got a lot of attention in China. People were interested to find out what would happen to them next. Finally, the elephants returned to a protected area in Yunnan.",
                "ja": "大きな動物は人々に大きな問題を引き起こすことがある。保護区に十分な食料がないため、象はしばしば農場から食料を取る。実際、2020年と2021年に雲南省から約14頭の象が食料を探すために500キロの旅に出た。象は時に町を通り抜けて食料を探そうとした。テレビのニュースやインターネットに登場した。その結果、中国で大きな注目を集めた。人々は次に何が起こるか知りたがっていた。最終的に、象は雲南省の保護区に戻った。",
                "audioFile": "audio/practice_pp3.mp3"
            },
            "practiceQuestions": [
                {"q": "「bigger and bigger」のパターンで他の例を作ってみましょう", "a": "例: The weather is getting colder and colder.（天気はますます寒くなっている）"},
                {"q": "「the second-largest」と同じパターンで「3番目に古い」と言うと？", "a": "the third-oldest"},
                {"q": "「not as many places」を比較級で言い換えると？", "a": "fewer places（より少ない場所）= not as many places"},
                {"q": "「more and more + 名詞」の例を作ってみましょう", "a": "More and more people are working from home.（ますます多くの人が在宅勤務している）"}
            ],
            "highlightPatterns": [
                "People are having a bigger and bigger effect on wild animals",
                "Barcelona is the second-largest city in Spain",
                "there are not as many places for animals like elephants",
                "As cities get bigger and more farms are needed",
                "he had created a lighter, spicier drink"
            ],
            "highlightColor": "#f472b6",
            "highlightLabel": "比較表現"
        },
        {
            "id": "fp4",
            "title": "過去分詞の形容詞的用法",
            "subtitle": "Past Participles as Adjectives",
            "explanation": "過去分詞（-ed形、不規則変化形）は名詞を後ろから修飾する（後置修飾）ことができます。「called ～（～と呼ばれる）」「provided by ～（～が提供する）」など、受動の意味を持つ形容詞として機能します。",
            "sourceQuote": "a man called John McLaughlin who lived in Toronto",
            "sourceLocation": "Part 4B 第1段落",
            "examples": [
                {"en": "The type that is most popular today was created by a man called John McLaughlin.", "ja": "今日最も人気のあるタイプはジョン・マクラフリンという男性によって作られた。", "note": "called ～ = ～と呼ばれる（過去分詞の後置修飾）"},
                {"en": "The water provided by the city was dangerous.", "ja": "市が提供する水は危険だった。", "note": "provided by ～ = ～が提供する（過去分詞句の後置修飾）"},
                {"en": "He also made machines called soda fountains.", "ja": "彼はまたソーダファウンテンと呼ばれる機械を作った。", "note": "called ～ = ～と呼ばれる"}
            ],
            "practicePassage": {
                "en": "[出典: Spicy Soda 第2段落]\nMcLaughlin returned to Toronto in 1890 and started a soda water company. It became very successful. One reason was that his advertisements said the water provided by the city was dangerous and caused diseases. He recommended that people drink his fruit-flavored soda water instead. He also made machines called soda fountains. People could use them to buy McLaughlin's drinks. The machines became popular with shoppers in busy department stores, especially on hot summer days.",
                "ja": "マクラフリンは1890年にトロントに戻り、ソーダ水の会社を始めた。非常に成功した。一つの理由は、広告が市が提供する水は危険で病気を引き起こすと述べたことだ。代わりに自分のフルーツ味のソーダ水を飲むよう勧めた。彼はまたソーダファウンテンと呼ばれる機械も作った。人々はそれを使ってマクラフリンの飲み物を買うことができた。特に暑い夏の日には、忙しいデパートの買い物客に人気だった。",
                "audioFile": "audio/practice_pp4.mp3"
            },
            "practiceQuestions": [
                {"q": "「a man called John McLaughlin」の called を関係代名詞で書き換えると？", "a": "a man who is called John McLaughlin / a man who was called John McLaughlin"},
                {"q": "「the water provided by the city」を関係代名詞で書き換えると？", "a": "the water which was provided by the city"},
                {"q": "「fruit-flavored」はどんな構造ですか？", "a": "名詞+過去分詞の複合形容詞（フルーツで味付けされた）。hand-made（手作りの）と同じパターン"},
                {"q": "過去分詞と現在分詞（-ing）の形容詞用法の違いは？", "a": "過去分詞＝受動（～された）、現在分詞＝能動（～する/～している）。例: excited（興奮した）vs exciting（興奮させる）"}
            ],
            "highlightPatterns": [
                "a man called John McLaughlin who lived in Toronto",
                "the water provided by the city was dangerous and caused diseases",
                "machines called soda fountains",
                "a ship called the Fair Star",
                "fruit-flavored soda water"
            ],
            "highlightColor": "#fbbf24",
            "highlightLabel": "過去分詞修飾"
        },
        {
            "id": "fp5",
            "title": "代名詞 one / the other / the others",
            "subtitle": "Pronouns: one, the other, the others",
            "explanation": "one, another, the other, the others は数量を区別する重要な代名詞です。one...the other（2つの内1つ…もう1つ）、one...the others（複数の内1つ…残り全部）、some...others（一部…他の一部）を使い分けます。",
            "sourceQuote": "One is a high school student, and the others are elementary school students.",
            "sourceLocation": "Part 1 Q18",
            "examples": [
                {"en": "One is a high school student, and the others are elementary school students.", "ja": "1人は高校生で、残り（の3人）は小学生だ。", "note": "one...the others = 1つ…残り全部"},
                {"en": "Some of them are old action movies. There will also be some new movies, too.", "ja": "古いアクション映画もあるし、新しい映画もある。", "note": "some...some = 一部…一部"},
                {"en": "His mother is taking him shopping today to buy new ones.", "ja": "母親は新しいの（靴）を買いに連れて行く。", "note": "ones = 前出の複数名詞（shoes）の代わり"}
            ],
            "practicePassage": {
                "en": "[出典: Movie Festival 第3段落]\nEight movies are going to be shown over two days at the festival. They've all been chosen by the director of Burning Fist. Some of them are old action movies from the 1980s and 1990s. There will also be some new movies, too. I think it sounds great, so I'm definitely going to buy a ticket for the festival. Should I get one for you, too?",
                "ja": "フェスティバルでは2日間で8本の映画が上映される予定。全部バーニング・フィストの監督が選んだんだ。1980年代や1990年代の古いアクション映画もあるし、新しい映画もある。すごく面白そうだから、絶対チケットを買うつもり。君の分も買おうか？",
                "audioFile": "audio/practice_pp5.mp3"
            },
            "practiceQuestions": [
                {"q": "「the others」と「others」の違いは？", "a": "the others＝残り全部（特定の範囲）。others＝不特定の他の人/物"},
                {"q": "「Should I get one for you?」の one は何を指していますか？", "a": "a ticket（チケット1枚）を指す。特定のものではなく「1つ」を意味する代名詞"},
                {"q": "「one...another...the other」のパターンで3つのりんごを説明してみましょう", "a": "I have three apples. One is red, another is green, and the other is yellow."},
                {"q": "「buy new ones」の ones は何を指していますか？", "a": "shoes（靴）の複数形。既出の名詞の繰り返しを避ける代名詞"}
            ],
            "highlightPatterns": [
                "One is a high school student, and the others are elementary school students",
                "Some of them are old action movies from the 1980s and 1990s",
                "Should I get one for you, too",
                "His mother is taking him shopping today to buy new ones",
                "none of his shoes fit him"
            ],
            "highlightColor": "#a78bfa",
            "highlightLabel": "代名詞"
        }
    ]
}

# Save final data.json
output_path = os.path.join(base, "data.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"data.json saved. FocusPoints: {len(data['lessonPlan']['focusPoints'])}")
for fp in data['lessonPlan']['focusPoints']:
    print(f"  {fp['id']}: {fp['title']} ({len(fp['highlightPatterns'])} patterns)")

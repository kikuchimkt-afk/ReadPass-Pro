"""
準2級 2023-2 Phase 3: lessonPlan全面刷新
FP1-4: 文法・構文ベース（大問3-4パッセージから選定）
FP5: パラフレーズ
"""
import json

path = r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade-pre2\2023-2\data.json"
d = json.load(open(path, "r", encoding="utf-8"))

lesson_plan = {
    "focusPoints": [
        {
            "id": "fp1",
            "title": "関係代名詞の制限用法",
            "subtitle": "Relative Pronouns (Restrictive Use)",
            "explanation": "関係代名詞は、先行する名詞を詳しく説明するために使われます。who（人）、which（もの）、that（人・もの両方）の使い分けが重要です。準2級では特に長文で頻出し、文の意味を正確に読み取るカギになります。",
            "sourceQuote": "...people who use social media are often reminded about events.",
            "sourceLocation": "大問3B 第3段落",
            "examples": [
                {"en": "The boy who lives next door is very friendly.", "ja": "隣に住んでいる少年はとても友好的だ。", "note": "whoは人を先行詞にとる関係代名詞"},
                {"en": "The book which I borrowed from the library was interesting.", "ja": "図書館で借りた本は面白かった。", "note": "whichはもの（book）を先行詞にとる"},
                {"en": "The movie that we watched last night was exciting.", "ja": "昨夜見た映画はワクワクした。", "note": "thatは人にもものにも使える万能な関係代名詞"}
            ],
            "practicePassage": {
                "en": "[出典: The Return of Greeting Cards 第3段落]\nAlthough people once thought that the Internet might be bad for sales of greeting cards, it may actually be helping them. This is because people who use social media are often reminded about events. For example, they may be sent a message to tell them that one of their friends has a birthday or wedding anniversary soon. As a result, they remember to buy a greeting card and send it to their friend.",
                "ja": "[出典: The Return of Greeting Cards 第3段落]\nかつてインターネットがグリーティングカードの売上に悪影響を及ぼすかもしれないと考えられていたが、実際には売上を助けているかもしれない。これは、ソーシャルメディアを使う人々がしばしばイベントについて思い出させられるからだ。例えば、友人の誕生日や結婚記念日が近いことを知らせるメッセージが送られることがある。その結果、彼らはグリーティングカードを買って友人に送ることを思い出すのだ。"
            },
            "practiceQuestions": [
                {"q": "「people who use social media」のwhoの先行詞は何ですか？", "a": "people（ソーシャルメディアを使う人々）"},
                {"q": "関係代名詞のthatが使われている箇所はどこですか？", "a": "「they may be sent a message to tell them that one of their friends has a birthday」のthat（接続詞のthat）"},
                {"q": "「人」を説明する関係代名詞として通常使うものは何ですか？", "a": "who（またはthat）"}
            ],
            "highlightPatterns": [
                "people who use social media",
                "the children could run around and shout without bothering other people",
                "a message to tell them that one of their friends has a birthday or wedding anniversary soon",
                "movies that were older or less popular",
                "the town where he was born"
            ],
            "highlightColor": "#4f8cff",
            "highlightLabel": "関係代名詞"
        },
        {
            "id": "fp2",
            "title": "比較構文（比較級・最上級・原級比較）",
            "subtitle": "Comparative and Superlative Expressions",
            "explanation": "英語の比較表現には、比較級（-er / more）、最上級（-est / most）、原級比較（as...as）があります。長文では物事を対比するために頻繁に使われます。",
            "sourceQuote": "Sending an electronic message by e-mail or through social media is quicker and easier than sending a paper greeting card.",
            "sourceLocation": "大問3B 第1段落",
            "examples": [
                {"en": "This bag is heavier than that one.", "ja": "このバッグはあのバッグより重い。", "note": "形容詞の比較級 + than で「〜より〜だ」"},
                {"en": "She is as tall as her brother.", "ja": "彼女は兄と同じくらいの身長だ。", "note": "as + 原級 + as で「〜と同じくらい」"},
                {"en": "Mt. Fuji is the highest mountain in Japan.", "ja": "富士山は日本で一番高い山だ。", "note": "the + 最上級 + in/of で「〜の中で最も」"}
            ],
            "practicePassage": {
                "en": "[出典: The Return of Greeting Cards 第1段落]\nDuring the 20th century, people often sent paper greeting cards to friends and family members on birthdays or at other special times. Greeting cards usually have a picture on the front and a message inside. In the 1990s, however, people began communicating online. Sending an electronic message by e-mail or through social media is quicker and easier than sending a paper greeting card. In addition, most greeting cards are thrown away. This creates a lot of trash. As a result, some people prefer online communication because they think it is better for the environment.",
                "ja": "[出典: The Return of Greeting Cards 第1段落]\n20世紀には、人々は誕生日やその他の特別な時に友人や家族に紙のグリーティングカードをよく送った。グリーティングカードの表には通常絵が描かれ、中にメッセージが書かれている。しかし1990年代に、人々はオンラインでコミュニケーションを取り始めた。Eメールやソーシャルメディアで電子メッセージを送るのは、紙のグリーティングカードを送るよりも速くて簡単だ。さらに、ほとんどのグリーティングカードは捨てられてしまう。これは大量のゴミを生む。その結果、環境に良いと考えてオンラインコミュニケーションを好む人もいる。"
            },
            "practiceQuestions": [
                {"q": "「quicker and easier than」はどのような比較構文ですか？", "a": "比較級 + than の構文。二つのものを比べて「〜より速くて簡単だ」と表現している。"},
                {"q": "「better for the environment」のbetterは何の比較級ですか？", "a": "good の比較級（good → better → best の不規則変化）"},
                {"q": "原級比較 as...as を使って「Eメールは手紙と同じくらい人気がある」を英語にしてください。", "a": "E-mail is as popular as letters."}
            ],
            "highlightPatterns": [
                "quicker and easier than sending a paper greeting card",
                "she might be more comfortable if she could watch movies",
                "movie companies got more money from indoor theaters"
            ],
            "highlightColor": "#34d399",
            "highlightLabel": "比較構文"
        },
        {
            "id": "fp3",
            "title": "受動態と能動態の使い分け",
            "subtitle": "Passive Voice vs Active Voice",
            "explanation": "受動態（be + 過去分詞）は、動作を受ける側を主語にする表現です。「〜される」という意味になり、動作主が不明・不要・文脈から明らかな場合に使われます。長文では客観的な説明や事実の記述に多用されます。",
            "sourceQuote": "most greeting cards are thrown away",
            "sourceLocation": "大問3B 第1段落",
            "examples": [
                {"en": "The window was broken by the storm.", "ja": "窓は嵐で壊された。", "note": "受動態: be + 過去分詞 + by 〜（動作主）"},
                {"en": "English is spoken in many countries.", "ja": "英語は多くの国で話されている。", "note": "動作主が一般的・不要な場合は by 〜 を省略"},
                {"en": "The cake was made by my sister.", "ja": "ケーキは姉が作った。", "note": "能動態: My sister made the cake. と書き換え可能"}
            ],
            "practicePassage": {
                "en": "[出典: Drive-in Movie Theaters 第3-4段落]\nAt first, these theaters had large speakers near the screen. The sound was not good, so some theaters put a speaker by every car. However, there were other problems for drive-in movie theaters. One was that drive-in movie theaters could only show movies in the evening after it became dark. Also, movie companies got more money from indoor theaters, so many of them did not let drive-in movie theaters show their best movies. Drive-in movie theaters often had to show movies that were older or less popular.",
                "ja": "[出典: Drive-in Movie Theaters 第3-4段落]\n最初、これらの映画館はスクリーンの近くに大きなスピーカーがあった。音質が良くなかったので、車ごとにスピーカーを設置する映画館もあった。しかし、ドライブインシアターには他の問題もあった。一つは、暗くなった夕方以降しか映画を上映できなかったことだ。また、映画会社は屋内の映画館からより多くの収入を得ていたので、ドライブインシアターに最高の映画を上映させない会社が多かった。ドライブインシアターは、古い映画や人気の低い映画を上映しなければならないことが多かった。"
            },
            "practiceQuestions": [
                {"q": "「most greeting cards are thrown away」の受動態を能動態に書き換えてください。", "a": "People throw away most greeting cards.（主語が一般の人々）"},
                {"q": "「they may be sent a message」のbe sentの態は何ですか？", "a": "受動態。「メッセージを送られるかもしれない」という意味。"},
                {"q": "「His idea was copied by other people」のリライトを能動態でしてください。", "a": "Other people copied his idea."}
            ],
            "highlightPatterns": [
                "most greeting cards are thrown away",
                "they may be sent a message to tell them",
                "Other people copied his idea",
                "He put a screen and some speakers in his yard and invited his family and neighbors"
            ],
            "highlightColor": "#f472b6",
            "highlightLabel": "受動態"
        },
        {
            "id": "fp4",
            "title": "結果・理由を表す接続表現",
            "subtitle": "Cause and Effect Connectors",
            "explanation": "英語の長文では、因果関係を示す接続表現が頻繁に使われます。because（〜なので）、so（だから）、as a result（その結果）、because of this（このため）などを理解することで、文章の論理展開を正確に追えるようになります。",
            "sourceQuote": "As a result, some people prefer online communication because they think it is better for the environment.",
            "sourceLocation": "大問3B 第1段落",
            "examples": [
                {"en": "She was late because the train was delayed.", "ja": "電車が遅れたので、彼女は遅刻した。", "note": "because + 主語 + 動詞 で原因を説明"},
                {"en": "It rained a lot, so the game was canceled.", "ja": "たくさん雨が降ったので、試合は中止になった。", "note": "so は結果を導く接続詞（前が原因、後が結果）"},
                {"en": "As a result, many stores had to close.", "ja": "その結果、多くの店が閉店しなければならなかった。", "note": "As a result は文頭で使い、前文の結果を示す"}
            ],
            "practicePassage": {
                "en": "[出典: Drive-in Movie Theaters 第2段落]\nHollingshead opened a bigger drive-in movie theater in 1933, but he did not make much money from it. Other people copied his idea, though, and drive-in movie theaters soon became popular, especially with people with small children. One reason was that the children could run around and shout without bothering other people. Some drive-in movie theaters even had playgrounds, so children could enjoy themselves while they waited for the movies to start.",
                "ja": "[出典: Drive-in Movie Theaters 第2段落]\nホリングスヘッドは1933年にもっと大きなドライブインシアターをオープンしたが、あまりお金を稼ぐことはできなかった。しかし、他の人々が彼のアイデアを真似し、ドライブインシアターはすぐに人気になった。特に小さな子供がいる家庭に人気だった。一つの理由は、子供たちが他の人を気にせず走り回ったり叫んだりできたからだ。ドライブインシアターの中には遊び場があるところもあり、子供たちは映画が始まるのを待つ間楽しむことができた。"
            },
            "practiceQuestions": [
                {"q": "「As a result」と同じ意味で使える表現を挙げてください。", "a": "Therefore, Consequently, Because of this, For this reason"},
                {"q": "大問3Bの第2段落で「Because of this」が導く結果は何ですか？", "a": "アメリカ人が今でも毎年約65億枚のグリーティングカードを購入していること"},
                {"q": "「so」と「because」の違いは何ですか？", "a": "soは結果を導き（原因→so→結果）、becauseは原因を導く（結果←because←原因）"}
            ],
            "highlightPatterns": [
                "As a result, some people prefer online communication because they think",
                "Because of this, Americans still buy around 6.5 billion greeting cards",
                "As a result, they remember to buy a greeting card",
                "so children could enjoy themselves while they waited for the movies to start",
                "because people could rent videos to watch at home"
            ],
            "highlightColor": "#fbbf24",
            "highlightLabel": "因果表現"
        },
        {
            "id": "fp5",
            "title": "パラフレーズの読解力",
            "subtitle": "Paraphrase Reading Comprehension",
            "explanation": "英検の読解問題では、本文の表現が選択肢で別の言い方（パラフレーズ）に置き換えられます。同じ内容を異なる語句で表現する力が、正解を見つけるカギです。",
            "sourceQuote": "①「felt lonely every day」→「did not know anyone」（寂しさ＝知り合いがいない）\n②「the children could run around and shout without bothering other people」→「parents did not have to worry if their children were noisy」（子供が騒いでも他の人の迷惑にならない＝親は心配不要）\n③「movie companies got more money from indoor theaters」→「movie companies made more money from indoor theaters」（より多くの収入を得た＝より多く稼いだ）\n④「Companies offered the owners a lot of money」→「Companies offered to pay them a lot of money for their land」（多額の金を提示した＝土地に対して高額を支払うと申し出た）",
            "sourceLocation": "大問3A, 大問4B",
            "examples": [
                {"en": "He was very tired. → He was exhausted.", "ja": "彼はとても疲れていた。→ 彼は疲れ果てていた。", "note": "tired と exhausted は同義語によるパラフレーズ"},
                {"en": "She couldn't find her keys. → Her keys were missing.", "ja": "彼女は鍵が見つからなかった。→ 彼女の鍵がなくなっていた。", "note": "能動態→受動態の視点変換によるパラフレーズ"},
                {"en": "The shop is next to the station. → The shop is near the station.", "ja": "その店は駅の隣にある。→ その店は駅の近くにある。", "note": "位置表現の言い換え"}
            ],
            "practicePassage": {
                "en": "[出典: Drive-in Movie Theaters 第4段落]\nIn the 1970s, many drive-in movie theaters closed because people could rent videos to watch at home. Also, many drive-in movie theaters were just outside large towns and cities. Companies wanted the theaters so that they could build new homes on the land. They offered the owners a lot of money, and many owners decided to sell their theaters. Although there were over 4,000 drive-in movie theaters in the United States around 1960, today, there are just a few hundred left.",
                "ja": "[出典: Drive-in Movie Theaters 第4段落]\n1970年代、多くのドライブインシアターが閉館した。人々が自宅で見るためにビデオをレンタルできるようになったからだ。また、多くのドライブインシアターは大きな町や都市のすぐ外にあった。企業はその土地に新しい住宅を建てるために映画館を欲しがった。企業はオーナーに多額の金を提示し、多くのオーナーが映画館を売ることにした。1960年頃にはアメリカに4,000以上のドライブインシアターがあったが、今日ではわずか数百しか残っていない。"
            },
            "practiceQuestions": [
                {"q": "「without bothering other people」を別の表現で言い換えてください。", "a": "without disturbing others / without being a nuisance to other people"},
                {"q": "「They offered the owners a lot of money」のパラフレーズはQ37のどの選択肢にありますか？", "a": "選択肢1「Companies offered to pay them a lot of money for their land.」"},
                {"q": "「just outside large towns and cities」は何を意味しますか？", "a": "大きな町や都市のすぐ郊外に（near the outskirts of large urban areas）"},
                {"q": "「people could rent videos to watch at home」をパラフレーズしてください。", "a": "home video rentals became available / people had the option to watch movies at home by renting videos"}
            ],
            "highlightPatterns": [
                "without bothering other people",
                "They offered the owners a lot of money",
                "just outside large towns and cities",
                "people could rent videos to watch at home"
            ],
            "highlightColor": "#f59e0b",
            "highlightLabel": "パラフレーズ"
        }
    ]
}

d["lessonPlan"] = lesson_plan

with open(path, "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=4)

print("✅ lessonPlan replaced with 5 grammar-based FPs")
for fp in lesson_plan["focusPoints"]:
    pp = fp.get("practicePassage", {})
    pq = fp.get("practiceQuestions", [])
    hp = fp.get("highlightPatterns", [])
    print(f"  {fp['id']}: {fp['title']} (PP={'✓' if pp.get('en') else '✗'}, PQ={len(pq)}, HL={len(hp)})")

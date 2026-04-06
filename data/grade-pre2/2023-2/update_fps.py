"""Update data.json with full FP details for Pre-2 2023-2"""
import json, sys
sys.stdout.reconfigure(encoding='utf-8')

path = r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade-pre2\2023-2\data.json"
d = json.load(open(path, "r", encoding="utf-8"))

fps = [
    {
        "id": "fp1",
        "title": "感情と問題解決の表現",
        "subtitle": "Emotions & Problem Solving",
        "explanation": "登場人物の感情（lonely, encouraged）を読み取り、問題→解決の流れを理解する力を養います。feel + 過去分詞の受動的感情表現がポイントです。",
        "sourceQuote": "He felt lonely every day. ... The members were very kind, and Stephen quickly made friends.",
        "sourceLocation": "大問3A: Stephen's New School",
        "examples": [
            {"q": "スティーブンが寂しく感じた理由は？", "a": "新しい学校に知り合いがいなかったから。"},
            {"q": "問題はどう解決したか？", "a": "ゲームクラブに入り、親切なメンバーとすぐに友達になった。"},
            {"q": "feel + 過去分詞の例は？", "a": "felt lonely（寂しく感じた）、felt encouraged（励まされたと感じた）。"}
        ],
        "practicePassage": {
            "en": "[出典: Stephen's New School]\nStephen's family recently moved to a new city, and Stephen had to change schools. He did not know anyone at his new school, and he felt lonely every day. He talked to his parents about his problem. Stephen's mother said that he would make new friends soon, and his father suggested joining one of the clubs at his new school.",
            "ja": "[出典: Stephen's New School]\nスティーブンの家族は最近新しい都市に引っ越し、スティーブンは転校しなければならなかった。新しい学校には知り合いがおらず、毎日寂しく感じていた。彼は自分の問題について両親に話した。母はすぐに新しい友達ができると言い、父は新しい学校のクラブに入ることを勧めた。",
            "audioFile": ""
        },
        "highlightPatterns": ["felt lonely", "felt encouraged", "talked to his parents", "suggested joining"],
        "highlightColor": "#fbbf24",
        "highlightLabel": "感情・問題解決の表現",
        "practiceQuestions": [
            {"q": "スティーブンはなぜ毎日寂しく感じていたか？", "a": "新しい学校に知り合いが一人もいなかったから。"},
            {"q": "父はどのような解決策を提案したか？", "a": "新しい学校のクラブに入ることを勧めた。"},
            {"q": "「felt lonely」はどのような文法構造か？", "a": "feel + 形容詞で「～と感じる」という感情表現。"},
            {"q": "suggest の後に続く動詞の形は？", "a": "suggest + doing（動名詞）。suggested joining＝入ることを提案した。"}
        ]
    },
    {
        "id": "fp2",
        "title": "比較と対比の論理展開",
        "subtitle": "Comparison & Contrast",
        "explanation": "however, though, but を使った対比構文を読み取る力を養います。紙のカードとオンラインメッセージの比較が典型例です。",
        "sourceQuote": "Sending an electronic message ... is quicker and easier than sending a paper greeting card.",
        "sourceLocation": "大問3B: The Return of Greeting Cards",
        "examples": [
            {"q": "オンラインメッセージの利点は？", "a": "紙のカードより速くて簡単（quicker and easier）。"},
            {"q": "紙のカードの利点は？", "a": "より多くの労力がかかるので、相手を大切に思っていることを示す。"},
            {"q": "however の役割は？", "a": "前の内容と対立する内容を導入する（しかし）。"}
        ],
        "practicePassage": {
            "en": "[出典: The Return of Greeting Cards]\nFor several years, sales of greeting cards in the United States went down. Recently, though, young adults have become interested in greeting cards. Many of them think that it is too easy to send a message online. Sending a greeting card to a person takes more effort. It shows that you really care about that person.",
            "ja": "[出典: The Return of Greeting Cards]\n数年間、アメリカでのグリーティングカードの売り上げは下がった。しかし最近、若い大人がグリーティングカードに関心を持つようになった。オンラインでメッセージを送るのは簡単すぎると考える人も多い。人にカードを送ることはより多くの労力がかかる。その人のことを本当に大切に思っていることを示す。",
            "audioFile": ""
        },
        "highlightPatterns": ["though", "however", "quicker and easier than", "takes more effort"],
        "highlightColor": "#34d399",
        "highlightLabel": "対比・比較の表現",
        "practiceQuestions": [
            {"q": "カードの売り上げが下がった後、何が起きたか？", "a": "若い大人がグリーティングカードに関心を持つようになった。"},
            {"q": "「though」はここでどのような役割か？", "a": "前文との対比を示す。売り上げが下がった→しかし若者が関心を持った。"},
            {"q": "カードを送ることが特別な理由は？", "a": "より多くの労力がかかるので、相手を大切にしている証拠になるから。"},
            {"q": "「too easy to ～」の意味は？", "a": "「～するのが簡単すぎる」という否定的なニュアンス。"}
        ]
    },
    {
        "id": "fp3",
        "title": "時間経過と変化の表現",
        "subtitle": "Time & Change Expressions",
        "explanation": "at first, in the 1970s, recently, today などの時間表現で歴史的変遷を追う力を養います。",
        "sourceQuote": "Although there were over 4,000 drive-in movie theaters ... around 1960, today, there are just a few hundred left.",
        "sourceLocation": "大問4B: Drive-in Movie Theaters",
        "examples": [
            {"q": "ドライブインシアターの全盛期は？", "a": "1960年頃（4,000以上のシアター）。"},
            {"q": "衰退の原因は？", "a": "ビデオレンタルの普及と土地の売却。"},
            {"q": "although の役割は？", "a": "「～にもかかわらず」と対比を示す接続詞。"}
        ],
        "practicePassage": {
            "en": "[出典: Drive-in Movie Theaters]\nIn the 1970s, many drive-in movie theaters closed because people could rent videos to watch at home. Also, many drive-in movie theaters were just outside large towns and cities. Companies wanted the theaters so that they could build new homes on the land. They offered the owners a lot of money, and many owners decided to sell their theaters. Although there were over 4,000 drive-in movie theaters in the United States around 1960, today, there are just a few hundred left.",
            "ja": "[出典: Drive-in Movie Theaters]\n1970年代、多くのドライブインシアターが閉館した。人々が自宅でビデオをレンタルできるようになったためだ。また多くのドライブインシアターは大きな町や都市の郊外にあった。企業はその土地に新しい住宅を建てるためシアターを欲しがった。オーナーに大金を提示し、多くのオーナーがシアターを売却することにした。1960年頃には4,000以上あったが、今日では数百しか残っていない。",
            "audioFile": ""
        },
        "highlightPatterns": ["In the 1970s", "around 1960", "today", "Although"],
        "highlightColor": "#60a5fa",
        "highlightLabel": "時間・変化の表現",
        "practiceQuestions": [
            {"q": "1970年代にドライブインシアターが閉館した理由は？", "a": "人々が自宅でビデオをレンタルできるようになったから。"},
            {"q": "企業がシアターを欲しがった理由は？", "a": "土地に新しい住宅を建てるため。"},
            {"q": "Although の文の構造は？", "a": "Although ＋ 対比される事実（4000以上あった）→ 現在の状況（数百しか残っていない）。"},
            {"q": "「so that ～ could」の意味は？", "a": "「～できるように」（目的を表す接続詞）。"}
        ]
    },
    {
        "id": "fp4",
        "title": "理由と結果の因果関係",
        "subtitle": "Cause & Effect Logic",
        "explanation": "because, as a result, so, since を使って原因→結果の文脈を正確に読み取る力を養います。",
        "sourceQuote": "drive-in movie theaters soon became popular, especially with people with small children. One reason was that the children could run around and shout without bothering other people.",
        "sourceLocation": "大問4B: Drive-in Movie Theaters",
        "examples": [
            {"q": "なぜ子供連れに人気だったか？", "a": "子供が走り回ったり叫んだりしても他の人を困らせなかったから。"},
            {"q": "One reason was that... の構造は？", "a": "理由を説明する「一つの理由は～であった」という構文。"}
        ],
        "practicePassage": {
            "en": "[出典: Drive-in Movie Theaters]\nHollingshead opened a bigger drive-in movie theater in 1933, but he did not make much money from it. Other people copied his idea, though, and drive-in movie theaters soon became popular, especially with people with small children. One reason was that the children could run around and shout without bothering other people. Some drive-in movie theaters even had playgrounds, so children could enjoy themselves while they waited for the movies to start.",
            "ja": "[出典: Drive-in Movie Theaters]\nホリングスヘッドは1933年に大きなドライブインシアターを開業したが、あまり儲からなかった。しかし他の人が彼のアイデアを真似し、ドライブインシアターはすぐに人気になった。特に小さな子供がいる家庭に人気だった。理由の一つは、子供が他の人を気にせず走り回ったり叫んだりできることだった。遊び場があるシアターもあり、映画の開始を待つ間子供たちは楽しめた。",
            "audioFile": ""
        },
        "highlightPatterns": ["One reason was that", "because", "so", "without bothering"],
        "highlightColor": "#f472b6",
        "highlightLabel": "因果関係の表現",
        "practiceQuestions": [
            {"q": "ホリングスヘッドのビジネスは最初成功したか？", "a": "いいえ。あまり儲からなかった。"},
            {"q": "ドライブインシアターが特に人気だった層は？", "a": "小さな子供がいる家庭。"},
            {"q": "「without bothering」の意味は？", "a": "「～を困らせずに」。without + 動名詞で否定の付帯状況。"},
            {"q": "遊び場の役割は？", "a": "映画の開始を待つ間、子供たちが楽しめるようにするため。"}
        ]
    },
    {
        "id": "fp5",
        "title": "今回の重要なパラフレーズ",
        "subtitle": "Key Paraphrases",
        "explanation": "本文の表現と選択肢の言い換え（パラフレーズ）を見抜く力を養います。正解は本文と同じ意味を別の言葉で表現しています。",
        "sourceQuote": "you joined a baseball team → Playing for a local sports team",
        "sourceLocation": "大問4A: My visit",
        "examples": [
            {"q": "joined a baseball team = ?", "a": "Playing for a local sports team（地元のスポーツチームでプレー）。"},
            {"q": "It's been 12 months = ?", "a": "It has been a year（1年が経った）。"},
            {"q": "without bothering other people = ?", "a": "parents did not have to worry if their children were noisy."}
        ],
        "practicePassage": {
            "en": "[出典: My visit]\nI'm really excited to see you again next week. I had such a great week the last time that I visited. I can't believe it's been 12 months already. I'm glad I can stay for a whole month this time. I'm planning lots of fun things for us to do together. Please tell your little sister that I'm looking forward to playing with her again, too.",
            "ja": "[出典: My visit]\n来週また会えるのをとても楽しみにしています。前回訪ねた時はとても楽しい1週間でした。もう12ヶ月も経ったとは信じられません。今回は丸1ヶ月滞在できるのが嬉しいです。一緒にする楽しいことをたくさん計画しています。妹にも、また一緒に遊ぶのを楽しみにしていると伝えてね。",
            "audioFile": ""
        },
        "highlightPatterns": ["12 months", "a whole month", "again", "looking forward to"],
        "highlightColor": "#a78bfa",
        "highlightLabel": "パラフレーズのポイント",
        "practiceQuestions": [
            {"q": "「12 months」は選択肢でどう言い換えられているか？", "a": "「a year」（1年）。"},
            {"q": "「looking forward to playing with her again」から分かることは？", "a": "以前も妹と遊んだ→初めて会うわけではない。"},
            {"q": "「a whole month」の意味は？", "a": "「丸1ヶ月」。a wholeで「全体の」を強調。"},
            {"q": "パラフレーズを見抜くコツは？", "a": "同じ意味を違う単語で表現しているかを確認する。数値の言い換え（12ヶ月→1年）に注意。"}
        ]
    }
]

d["lessonPlan"]["focusPoints"] = fps

with open(path, "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=4)
print(f"Updated {len(fps)} FPs with full details")

"""
準2級 2023-2 data.json 修正スクリプト - Phase 2
主な修正:
1. 大問3のtype → passage-fill
2. 全パッセージにparagraphs, translations, sentencePairs追加
3. 大問4Aにformat:email, meta追加
4. 全問にquestionTranslation追加
5. vocabulary追加 (36→40+語)
"""
import json, copy, os

path = r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade-pre2\2023-2\data.json"
d = json.load(open(path, "r", encoding="utf-8"))

# ===== 1. Fix Section 2 type: reading-comprehension → passage-fill =====
d["sections"][2]["type"] = "passage-fill"
d["sections"][2]["instruction"] = "次の英文A，Bを読み，その文意にそって(26)から(30)までの(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選び，その番号を解答用紙の所定欄にマークしなさい。"
print("✅ Section 2 type → passage-fill")

# ===== 2. Add paragraphs + translations to 大問3A: Stephen's New School =====
sec3 = d["sections"][2]
p3a = sec3["passages"][0]  # A: Stephen's New School
p3a["paragraphs"] = [
    "Stephen's family recently moved to a new city, and Stephen had to change schools. He did not know anyone at his new school, and he felt lonely every day. He ( 26 ) about his problem. Stephen's mother said that he would make new friends soon, and his father suggested joining one of the clubs at his new school. However, Stephen did not like sports, music, or art, so he did not know what to do.",
    "One day, Stephen saw a poster at school for a games club. The members met three times a week to play board games and card games. Stephen really liked playing games, so he joined the club. The members were very kind, and Stephen quickly made friends. Recently, Stephen decided to ( 27 ). He has been working hard to make the rules and the other things he will need for the game. Once it is ready, he plans to try it with the other members of the club."
]
p3a["translations"] = [
    "スティーブンの家族は最近新しい街に引っ越し、スティーブンは転校しなければならなかった。新しい学校では誰も知らず、毎日寂しく感じていた。彼は（26）自分の悩みについて話した。スティーブンの母親はすぐに新しい友達ができるよと言い、父親は新しい学校のクラブに入ることを提案した。しかし、スティーブンはスポーツ、音楽、美術が好きではなかったので、どうすればいいかわからなかった。",
    "ある日、スティーブンは学校でゲームクラブのポスターを見た。メンバーは週3回集まってボードゲームやカードゲームをしていた。スティーブンはゲームがとても好きだったので、そのクラブに入った。メンバーはとても親切で、スティーブンはすぐに友達ができた。最近、スティーブンは（27）ことに決めた。彼はルールやゲームに必要なものを作るために一生懸命取り組んでいる。準備ができたら、クラブの他のメンバーと一緒に試してみるつもりだ。"
]
p3a["sentencePairs"] = [
    ["Stephen's family recently moved to a new city, and Stephen had to change schools.", "スティーブンの家族は最近新しい街に引っ越し、スティーブンは転校しなければならなかった。"],
    ["He did not know anyone at his new school, and he felt lonely every day.", "新しい学校では誰も知らず、毎日寂しく感じていた。"],
    ["Stephen's mother said that he would make new friends soon, and his father suggested joining one of the clubs at his new school.", "スティーブンの母親はすぐに新しい友達ができるよと言い、父親は新しい学校のクラブに入ることを提案した。"],
    ["However, Stephen did not like sports, music, or art, so he did not know what to do.", "しかし、スティーブンはスポーツ、音楽、美術が好きではなかったので、どうすればいいかわからなかった。"],
    ["One day, Stephen saw a poster at school for a games club.", "ある日、スティーブンは学校でゲームクラブのポスターを見た。"],
    ["The members met three times a week to play board games and card games.", "メンバーは週3回集まってボードゲームやカードゲームをしていた。"],
    ["Stephen really liked playing games, so he joined the club.", "スティーブンはゲームがとても好きだったので、そのクラブに入った。"],
    ["The members were very kind, and Stephen quickly made friends.", "メンバーはとても親切で、スティーブンはすぐに友達ができた。"],
    ["He has been working hard to make the rules and the other things he will need for the game.", "彼はルールやゲームに必要なものを作るために一生懸命取り組んでいる。"],
    ["Once it is ready, he plans to try it with the other members of the club.", "準備ができたら、クラブの他のメンバーと一緒に試してみるつもりだ。"]
]
print("✅ 大問3A paragraphs/translations/sentencePairs added")

# ===== 3. Add paragraphs + translations to 大問3B: The Return of Greeting Cards =====
p3b = sec3["passages"][1]  # B: The Return of Greeting Cards
p3b["paragraphs"] = [
    "During the 20th century, people often sent paper greeting cards to friends and family members on birthdays or at other special times. Greeting cards usually have a picture on the front and a message inside. In the 1990s, however, people began communicating online. Sending an electronic message by e-mail or through social media is quicker and easier than sending a paper greeting card. In addition, most greeting cards are thrown away. This creates a lot of trash. As a result, some people prefer online communication because they think it is ( 28 ).",
    "For several years, sales of greeting cards in the United States went down. Recently, though, young adults have become interested in greeting cards. Many of them think that it is too easy to send a message online. Sending a greeting card to a person ( 29 ). It shows that you really care about that person. Because of this, Americans still buy around 6.5 billion greeting cards every year.",
    "Although people once thought that the Internet might be bad for sales of greeting cards, it may actually be helping them. This is because people who use social media are often ( 30 ). For example, they may be sent a message to tell them that one of their friends has a birthday or wedding anniversary soon. As a result, they remember to buy a greeting card and send it to their friend."
]
p3b["translations"] = [
    "20世紀には、人々は誕生日やその他の特別な時に友人や家族に紙のグリーティングカードをよく送った。グリーティングカードの表には通常絵が描かれ、中にメッセージが書かれている。しかし1990年代に、人々はオンラインでコミュニケーションを取り始めた。Eメールやソーシャルメディアで電子メッセージを送るのは、紙のグリーティングカードを送るよりも速くて簡単だ。さらに、ほとんどのグリーティングカードは捨てられてしまう。これは大量のゴミを生む。その結果、オンラインコミュニケーションの方が（28）と考えて好む人もいる。",
    "数年間、アメリカでのグリーティングカードの売上は減少した。しかし最近、若い大人たちがグリーティングカードに関心を持つようになった。彼らの多くは、オンラインでメッセージを送るのは簡単すぎると考えている。人にグリーティングカードを送ることは（29）。それはその人のことを本当に気にかけていることを示す。このため、アメリカ人は今でも毎年約65億枚のグリーティングカードを購入している。",
    "かつてインターネットがグリーティングカードの売上に悪影響を及ぼすかもしれないと考えられていたが、実際には売上を助けているかもしれない。これは、ソーシャルメディアを使う人々がしばしば（30）からだ。例えば、友人の誕生日や結婚記念日が近いことを知らせるメッセージが送られることがある。その結果、彼らはグリーティングカードを買って友人に送ることを思い出すのだ。"
]
p3b["sentencePairs"] = [
    ["During the 20th century, people often sent paper greeting cards to friends and family members on birthdays or at other special times.", "20世紀には、人々は誕生日やその他の特別な時に友人や家族に紙のグリーティングカードをよく送った。"],
    ["Greeting cards usually have a picture on the front and a message inside.", "グリーティングカードの表には通常絵が描かれ、中にメッセージが書かれている。"],
    ["In the 1990s, however, people began communicating online.", "しかし1990年代に、人々はオンラインでコミュニケーションを取り始めた。"],
    ["Sending an electronic message by e-mail or through social media is quicker and easier than sending a paper greeting card.", "Eメールやソーシャルメディアで電子メッセージを送るのは、紙のグリーティングカードを送るよりも速くて簡単だ。"],
    ["In addition, most greeting cards are thrown away.", "さらに、ほとんどのグリーティングカードは捨てられてしまう。"],
    ["This creates a lot of trash.", "これは大量のゴミを生む。"],
    ["For several years, sales of greeting cards in the United States went down.", "数年間、アメリカでのグリーティングカードの売上は減少した。"],
    ["Recently, though, young adults have become interested in greeting cards.", "しかし最近、若い大人たちがグリーティングカードに関心を持つようになった。"],
    ["Many of them think that it is too easy to send a message online.", "彼らの多くは、オンラインでメッセージを送るのは簡単すぎると考えている。"],
    ["It shows that you really care about that person.", "それはその人のことを本当に気にかけていることを示す。"],
    ["Because of this, Americans still buy around 6.5 billion greeting cards every year.", "このため、アメリカ人は今でも毎年約65億枚のグリーティングカードを購入している。"],
    ["Although people once thought that the Internet might be bad for sales of greeting cards, it may actually be helping them.", "かつてインターネットがグリーティングカードの売上に悪影響を及ぼすかもしれないと考えられていたが、実際には売上を助けているかもしれない。"],
    ["As a result, they remember to buy a greeting card and send it to their friend.", "その結果、彼らはグリーティングカードを買って友人に送ることを思い出すのだ。"]
]
print("✅ 大問3B paragraphs/translations/sentencePairs added")

# ===== 4. Add paragraphs/translations/sentencePairs to 大問4A: Grandpa's email =====
sec4 = d["sections"][3]
p4a = sec4["passages"][0]  # A: email
p4a["format"] = "email"
p4a["meta"] = {
    "from": "Henry Robbins <h-g-robbins@oldmail.com>",
    "to": "Peter Robbins <peter1512@whichmail.com>",
    "date": "October 8",
    "subject": "My visit"
}
p4a["title"] = "My visit"
p4a["paragraphs"] = [
    "I'm really excited to see you again next week. I had such a great week the last time that I visited. I can't believe it's been 12 months already. I'm glad I can stay for a whole month this time. I'm planning lots of fun things for us to do together. Please tell your little sister that I'm looking forward to playing with her again, too.",
    "I thought we could go camping by Mirror Lake. We could try fishing in the lake, too. Have you ever been fishing before? I took your dad fishing many times when he was a boy. It's very relaxing, but you have to be ready and move quickly if you want to catch anything! I can teach you lots of tricks to help you become a good fisher.",
    "I also thought that we could go to watch a baseball game together. I haven't been to any big baseball games for a long time because there aren't any professional teams near my house. Your dad told me that you joined a baseball team in your town a few months ago. How is that going? If you want to, we can go to a park to practice throwing, catching, and hitting."
]
p4a["translations"] = [
    "来週また会えるのがとても楽しみだよ。前回訪れた時はとても楽しい一週間だった。もう12ヶ月も経ったなんて信じられない。今回は丸一ヶ月滞在できてうれしいよ。一緒にやる楽しいことをたくさん計画しているんだ。妹にも、また一緒に遊ぶのを楽しみにしていると伝えてね。",
    "ミラーレイクのそばでキャンプに行けたらと思っているんだ。湖で釣りも試してみようよ。釣りをしたことはあるかい？お父さんが少年だった頃、何度も釣りに連れていったんだよ。とてもリラックスできるけど、何かを釣りたいなら準備して素早く動かないといけないよ！上手な釣り人になるためのコツをたくさん教えてあげるよ。",
    "一緒に野球の試合を観に行くのもいいと思うんだ。家の近くにプロのチームがないから、大きな野球の試合にはずっと行けていないんだ。お父さんから、数ヶ月前に町の野球チームに入ったと聞いたよ。調子はどうかな？もしよければ、公園に行って投げたり、捕ったり、打ったりの練習をしようよ。"
]
p4a["sentencePairs"] = [
    ["I'm really excited to see you again next week.", "来週また会えるのがとても楽しみだよ。"],
    ["I had such a great week the last time that I visited.", "前回訪れた時はとても楽しい一週間だった。"],
    ["I can't believe it's been 12 months already.", "もう12ヶ月も経ったなんて信じられない。"],
    ["I'm glad I can stay for a whole month this time.", "今回は丸一ヶ月滞在できてうれしいよ。"],
    ["I'm planning lots of fun things for us to do together.", "一緒にやる楽しいことをたくさん計画しているんだ。"],
    ["Please tell your little sister that I'm looking forward to playing with her again, too.", "妹にも、また一緒に遊ぶのを楽しみにしていると伝えてね。"],
    ["I thought we could go camping by Mirror Lake.", "ミラーレイクのそばでキャンプに行けたらと思っているんだ。"],
    ["We could try fishing in the lake, too.", "湖で釣りも試してみようよ。"],
    ["Have you ever been fishing before?", "釣りをしたことはあるかい？"],
    ["I took your dad fishing many times when he was a boy.", "お父さんが少年だった頃、何度も釣りに連れていったんだよ。"],
    ["I can teach you lots of tricks to help you become a good fisher.", "上手な釣り人になるためのコツをたくさん教えてあげるよ。"],
    ["I also thought that we could go to watch a baseball game together.", "一緒に野球の試合を観に行くのもいいと思うんだ。"],
    ["I haven't been to any big baseball games for a long time because there aren't any professional teams near my house.", "家の近くにプロのチームがないから、大きな野球の試合にはずっと行けていないんだ。"],
    ["Your dad told me that you joined a baseball team in your town a few months ago.", "お父さんから、数ヶ月前に町の野球チームに入ったと聞いたよ。"],
    ["How is that going?", "調子はどうかな？"],
    ["If you want to, we can go to a park to practice throwing, catching, and hitting.", "もしよければ、公園に行って投げたり、捕ったり、打ったりの練習をしようよ。"]
]
# Add questionTranslation to 大問4A questions
for q in p4a["questions"]:
    if q["number"] == 31:
        q["questionTranslation"] = "おじいちゃんがピーターに言っていることの一つは何ですか？"
    elif q["number"] == 32:
        q["questionTranslation"] = "おじいちゃんはピーターに何を尋ねていますか？"
    elif q["number"] == 33:
        q["questionTranslation"] = "ピーターが最近始めたことは何ですか？"
print("✅ 大問4A paragraphs/translations/sentencePairs/format/meta/questionTranslation added")

# ===== 5. Add paragraphs/translations/sentencePairs to 大問4B: Drive-in Movie Theaters =====
p4b = sec4["passages"][1]  # B: Drive-in Movie Theaters
p4b["paragraphs"] = [
    "Richard Hollingshead was an American businessman. His mother loved movies, but she did not like the hard seats in movie theaters. Hollingshead thought that she might be more comfortable if she could watch movies while sitting on the soft seats of her own car. He put a screen and some speakers in his yard and invited his family and neighbors to try his new business idea: a drive-in movie theater.",
    "Hollingshead opened a bigger drive-in movie theater in 1933, but he did not make much money from it. Other people copied his idea, though, and drive-in movie theaters soon became popular, especially with people with small children. One reason was that the children could run around and shout without bothering other people. Some drive-in movie theaters even had playgrounds, so children could enjoy themselves while they waited for the movies to start.",
    "At first, these theaters had large speakers near the screen. The sound was not good, so some theaters put a speaker by every car. However, there were other problems for drive-in movie theaters. One was that drive-in movie theaters could only show movies in the evening after it became dark. Also, movie companies got more money from indoor theaters, so many of them did not let drive-in movie theaters show their best movies. Drive-in movie theaters often had to show movies that were older or less popular.",
    "In the 1970s, many drive-in movie theaters closed because people could rent videos to watch at home. Also, many drive-in movie theaters were just outside large towns and cities. Companies wanted the theaters so that they could build new homes on the land. They offered the owners a lot of money, and many owners decided to sell their theaters. Although there were over 4,000 drive-in movie theaters in the United States around 1960, today, there are just a few hundred left."
]
p4b["translations"] = [
    "リチャード・ホリングスヘッドはアメリカの実業家だった。彼の母親は映画が好きだったが、映画館の硬い座席が嫌いだった。ホリングスヘッドは、自分の車の柔らかい座席に座りながら映画を観られたら、母親はもっと快適だろうと考えた。彼は庭にスクリーンとスピーカーを置き、家族や近所の人々を新しいビジネスアイデアであるドライブインシアターに招待した。",
    "ホリングスヘッドは1933年にもっと大きなドライブインシアターをオープンしたが、あまりお金を稼ぐことはできなかった。しかし、他の人々が彼のアイデアを真似し、ドライブインシアターはすぐに人気になった。特に小さな子供がいる家庭に人気だった。一つの理由は、子供たちが他の人を気にせず走り回ったり叫んだりできたからだ。ドライブインシアターの中には遊び場があるところもあり、子供たちは映画が始まるのを待つ間楽しむことができた。",
    "最初、これらの映画館はスクリーンの近くに大きなスピーカーがあった。音質が良くなかったので、車ごとにスピーカーを設置する映画館もあった。しかし、ドライブインシアターには他の問題もあった。一つは、暗くなった夕方以降しか映画を上映できなかったことだ。また、映画会社は屋内の映画館からより多くの収入を得ていたので、ドライブインシアターに最高の映画を上映させない会社が多かった。ドライブインシアターは、古い映画や人気の低い映画を上映しなければならないことが多かった。",
    "1970年代、多くのドライブインシアターが閉館した。人々が自宅で見るためにビデオをレンタルできるようになったからだ。また、多くのドライブインシアターは大きな町や都市のすぐ外にあった。企業はその土地に新しい住宅を建てるために映画館を欲しがった。企業はオーナーに多額の金を提示し、多くのオーナーが映画館を売ることにした。1960年頃にはアメリカに4,000以上のドライブインシアターがあったが、今日ではわずか数百しか残っていない。"
]
p4b["sentencePairs"] = [
    ["Richard Hollingshead was an American businessman.", "リチャード・ホリングスヘッドはアメリカの実業家だった。"],
    ["His mother loved movies, but she did not like the hard seats in movie theaters.", "彼の母親は映画が好きだったが、映画館の硬い座席が嫌いだった。"],
    ["Hollingshead thought that she might be more comfortable if she could watch movies while sitting on the soft seats of her own car.", "ホリングスヘッドは、自分の車の柔らかい座席に座りながら映画を観られたら、母親はもっと快適だろうと考えた。"],
    ["He put a screen and some speakers in his yard and invited his family and neighbors to try his new business idea: a drive-in movie theater.", "彼は庭にスクリーンとスピーカーを置き、家族や近所の人々を新しいビジネスアイデアであるドライブインシアターに招待した。"],
    ["Hollingshead opened a bigger drive-in movie theater in 1933, but he did not make much money from it.", "ホリングスヘッドは1933年にもっと大きなドライブインシアターをオープンしたが、あまりお金を稼ぐことはできなかった。"],
    ["Other people copied his idea, though, and drive-in movie theaters soon became popular, especially with people with small children.", "しかし、他の人々が彼のアイデアを真似し、ドライブインシアターはすぐに人気になった。特に小さな子供がいる家庭に人気だった。"],
    ["One reason was that the children could run around and shout without bothering other people.", "一つの理由は、子供たちが他の人を気にせず走り回ったり叫んだりできたからだ。"],
    ["Some drive-in movie theaters even had playgrounds, so children could enjoy themselves while they waited for the movies to start.", "ドライブインシアターの中には遊び場があるところもあり、子供たちは映画が始まるのを待つ間楽しむことができた。"],
    ["At first, these theaters had large speakers near the screen.", "最初、これらの映画館はスクリーンの近くに大きなスピーカーがあった。"],
    ["The sound was not good, so some theaters put a speaker by every car.", "音質が良くなかったので、車ごとにスピーカーを設置する映画館もあった。"],
    ["However, there were other problems for drive-in movie theaters.", "しかし、ドライブインシアターには他の問題もあった。"],
    ["One was that drive-in movie theaters could only show movies in the evening after it became dark.", "一つは、暗くなった夕方以降しか映画を上映できなかったことだ。"],
    ["Also, movie companies got more money from indoor theaters, so many of them did not let drive-in movie theaters show their best movies.", "また、映画会社は屋内の映画館からより多くの収入を得ていたので、ドライブインシアターに最高の映画を上映させない会社が多かった。"],
    ["Drive-in movie theaters often had to show movies that were older or less popular.", "ドライブインシアターは、古い映画や人気の低い映画を上映しなければならないことが多かった。"],
    ["In the 1970s, many drive-in movie theaters closed because people could rent videos to watch at home.", "1970年代、多くのドライブインシアターが閉館した。人々が自宅で見るためにビデオをレンタルできるようになったからだ。"],
    ["Also, many drive-in movie theaters were just outside large towns and cities.", "また、多くのドライブインシアターは大きな町や都市のすぐ外にあった。"],
    ["Companies wanted the theaters so that they could build new homes on the land.", "企業はその土地に新しい住宅を建てるために映画館を欲しがった。"],
    ["They offered the owners a lot of money, and many owners decided to sell their theaters.", "企業はオーナーに多額の金を提示し、多くのオーナーが映画館を売ることにした。"],
    ["Although there were over 4,000 drive-in movie theaters in the United States around 1960, today, there are just a few hundred left.", "1960年頃にはアメリカに4,000以上のドライブインシアターがあったが、今日ではわずか数百しか残っていない。"]
]
# Add questionTranslation to 大問4B questions
for q in p4b["questions"]:
    if q["number"] == 34:
        q["questionTranslation"] = "リチャード・ホリングスヘッドの母親について分かることの一つは何ですか？"
    elif q["number"] == 35:
        q["questionTranslation"] = "ドライブインシアターが人気になった理由の一つは何ですか？"
    elif q["number"] == 36:
        q["questionTranslation"] = "ドライブインシアターで一部の映画が上映されなかった理由は何ですか？"
    elif q["number"] == 37:
        q["questionTranslation"] = "多くのドライブインシアターのオーナーが映画館を売ったのはなぜですか？"
print("✅ 大問4B paragraphs/translations/sentencePairs/questionTranslation added")

# ===== 6. Add vocabulary (大問3・4パッセージから追加して40語以上に) =====
new_vocab = [
    {"word": "greeting card", "meaning": "グリーティングカード", "pos": "名詞", "level": "準2級", "example": "I sent a greeting card to my friend on her birthday.", "distractors": ["招待状", "名刺", "チラシ"]},
    {"word": "electronic", "meaning": "電子の", "pos": "形容詞", "level": "準2級", "example": "Electronic devices have changed our lives.", "distractors": ["自動の", "手動の", "機械的な"]},
    {"word": "anniversary", "meaning": "記念日", "pos": "名詞", "level": "準2級", "example": "They celebrated their 10th wedding anniversary.", "distractors": ["誕生日", "祝日", "卒業式"]},
    {"word": "drive-in", "meaning": "ドライブイン式の", "pos": "形容詞", "level": "準2級", "example": "We watched a movie at the drive-in theater.", "distractors": ["屋内の", "屋外の", "移動式の"]},
    {"word": "comfortable", "meaning": "快適な", "pos": "形容詞", "level": "準2級", "example": "This sofa is very comfortable.", "distractors": ["不便な", "危険な", "退屈な"]},
    {"word": "bother", "meaning": "迷惑をかける", "pos": "動詞", "level": "準2級", "example": "Please don't bother me while I'm studying.", "distractors": ["助ける", "招待する", "励ます"]},
    {"word": "professional", "meaning": "プロの", "pos": "形容詞", "level": "準2級", "example": "She became a professional tennis player.", "distractors": ["アマチュアの", "学生の", "地元の"]},
    {"word": "rent", "meaning": "借りる・賃借する", "pos": "動詞", "level": "準2級", "example": "We rented a car for the weekend.", "distractors": ["購入する", "修理する", "売却する"]}
]
d["vocabulary"].extend(new_vocab)
print(f"✅ vocabulary: 36 → {len(d['vocabulary'])} words")

# ===== 7. Save =====
backup_path = path.replace("data.json", "data_backup.json")
import shutil
if not os.path.exists(backup_path):
    shutil.copy2(path, backup_path)
    print(f"✅ Backup saved to {backup_path}")

with open(path, "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=4)
print(f"✅ Saved to {path}")
print(f"\nFinal stats: sections={len(d['sections'])}, vocab={len(d['vocabulary'])}")

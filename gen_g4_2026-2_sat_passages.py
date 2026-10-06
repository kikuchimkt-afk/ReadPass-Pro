"""Booklet pp. 7-11: verb-aware, fully aligned bilingual reading units."""


def row(units, verb=""):
    return [" ".join(x[0] for x in units), "".join(x[1] for x in units),
            "||".join(a+"|"+b for a,b in units), verb]


def plain(en, ja):
    return row([(en,ja)])


def question(n, stem, ja, choices, meanings, answer, evidence, note, simple, reasons, easy):
    return dict(number=n, question=stem, questionTranslation=ja, choices=choices,
                choiceTranslations=meanings, answer=answer, sourceEvidence=evidence,
                grammar=f"本文の根拠は「{' / '.join(evidence)}」。{note}", grammarSimple=simple,
                choiceAnalysis=[("○ " if i==answer else "")+f"{c}＝{t}。{r}" for i,(c,t,r) in enumerate(zip(choices,meanings,reasons),1)],
                choiceAnalysisSimple=[("○ " if i==answer else "")+f"{t}。{r}" for i,(t,r) in enumerate(zip(meanings,easy),1)])


NOTICE=[
    [plain("Weekend Sale at Market Town Sports Store","マーケットタウン・スポーツ店の週末セール"),
     row([("Enjoy","楽しんでください、"),("our weekend sale!","当店の週末セールを。")],"Enjoy"),
     plain("Dates: August 28 and August 29","日程：8月28日と8月29日")],
    [row([("All baseball gloves and tennis rackets","すべての野球グローブとテニスラケットは"),("will be 70% off.","70％引きになります。")],"will"),
     row([("Soccer balls will be $10 each,","サッカーボールは1個10ドルで、"),("and swimming caps will be $5 each!","水泳帽は1個5ドルになります。")],"will")],
    [row([("Our second store on Sun Street","サン・ストリートにある当店の2号店は"),("will open on September 11.","9月11日に開店します。")],"will"),
     row([("Please visit","訪れてください、"),("that store, too.","その店にも。")],"visit")],
]

EMAIL=[
    [plain("From: Charlotte Green","差出人：シャーロット・グリーン"),plain("To: William James","宛先：ウィリアム・ジェームズ"),
     plain("Date: October 20","日付：10月20日"),plain("Subject: Halloween party","件名：ハロウィーンパーティー")],
    [plain("Hi William,","ウィリアムへ、"),
     row([("We will have","私たちは開きます、"),("a Halloween party at school this month!","今月学校でハロウィーンパーティーを。")],"will"),
     row([("What are you going to wear?","あなたは何を着る予定ですか。")],"are"),
     row([("I want","私はなりたいです、"),("to be a cat.","猫に。")],"want"),
     row([("Now I am looking for","今私は探しています、"),("the clothes.","その服を。")],"am"),
     row([("By the way,","ところで、"),("do you like pumpkin pie?","パンプキンパイは好きですか。")],"do"),
     row([("I am going to make some","私はいくつか作る予定です、"),("with my sister this weekend.","今週末に姉（妹）と。")],"am"),
     row([("How about","どうですか、"),("making some together?","一緒にいくつか作るのは。")]),
     plain("Your friend,","あなたの友人、"),plain("Charlotte","シャーロット")],
    [plain("From: William James","差出人：ウィリアム・ジェームズ"),plain("To: Charlotte Green","宛先：シャーロット・グリーン"),
     plain("Date: October 21","日付：10月21日"),plain("Subject: This weekend","件名：今週末")],
    [plain("Hi Charlotte,","シャーロットへ、"),
     row([("I want to be a baseball player","私は野球選手になりたいです、"),("for the Halloween party,","ハロウィーンパーティーで。"),("so my mother is making the clothes for me.","だから母が私のために服を作ってくれています。")],"want"),
     row([("I am going to buy","私は買う予定です、"),("a new cap on Saturday.","土曜日に新しい帽子を。")],"am"),
     row([("But I am free","でも私は空いています、"),("on Sunday.","日曜日は。")],"am"),
     row([("I want","私は作りたいです、"),("to make pumpkin pies together!","一緒にパンプキンパイを。")],"want"),
     row([("I will bring","私は持っていきます、"),("some snacks with me.","お菓子をいくつか。")],"will"),
     plain("Your friend,","あなたの友人、"),plain("William","ウィリアム")],
]
# Split this interrogative into meaningful units without changing the original.
EMAIL[1][2]=row([("What","何を"),("are you going to wear?","あなたは着る予定ですか。")],"are")

ARTICLE=[
    [row([("Aya is","アヤは"),("a high school student.","高校生です。")],"is"),
     row([("Her high school has","彼女の高校にはあります、"),("Spanish, French, Chinese, and German lessons.","スペイン語、フランス語、中国語、ドイツ語の授業が。")],"has"),
     row([("Aya takes","アヤは受けています、"),("French lessons.","フランス語の授業を。")],"takes"),
     row([("Last year,","去年、"),("Aya studied abroad in Paris.","アヤはパリに留学しました。")],"studied"),
     row([("She was excited","彼女は楽しみにしていました、"),("to eat food and stay with a host family,","食べ物を食べたりホストファミリーと過ごしたりすることを。"),("but she was nervous about taking a plane.","でも飛行機に乗ることには不安を感じていました。")],"was")],
    [row([("In Paris,","パリでは、"),("Aya studied French every day.","アヤは毎日フランス語を勉強しました。")],"studied"),
     row([("On the weekend,","週末には、"),("she rode on the train","彼女は電車に乗り、"),("and went to the library with her host family.","ホストファミリーと図書館へ行きました。")],"rode"),
     row([("They went","彼らは行きました、"),("to an art museum in a large park, too.","大きな公園の中にある美術館にも。")],"went"),
     row([("There were","ありました、"),("many beautiful and famous paintings in the museum.","美術館にはたくさんの美しく有名な絵が。")],"were"),
     row([("Aya wanted","アヤは知りたいと思いました、"),("to learn more about art.","芸術についてもっと。")],"wanted")],
    [row([("After her stay in Paris,","パリ滞在の後、"),("Aya started taking painting lessons","アヤは絵のレッスンを受け始めました、"),("with her friends from high school.","高校の友人たちと。")],"started"),
     row([("At first, Aya was not good at painting,","最初はアヤは絵を描くのが上手ではありませんでしたが、"),("but she got better.","上達しました。")],"was"),
     row([("She sent some paintings","彼女は何枚かの絵を送りました、"),("to her host family in Paris with a letter.","手紙を添えてパリのホストファミリーへ。")],"sent"),
     row([("Now, Aya studies French harder than before","今アヤは以前より熱心にフランス語を勉強し、"),("and visits museums every weekend.","毎週末、美術館を訪れています。")],"studies"),
     row([("She wants","彼女は望んでいます、"),("to be an artist and live in France in the future.","将来画家になってフランスに住むことを。")],"wants")],
]

# Full translations read naturally; bilingual slash units retain English order.
for block,translations in zip(NOTICE,[
    ["マーケットタウン・スポーツ店の週末セール","当店の週末セールをお楽しみください。","日程：8月28日と8月29日"],
    ["すべての野球グローブとテニスラケットが70％引きになります。","サッカーボールは1個10ドル、水泳帽は1個5ドルになります。"],
    ["サン・ストリートにある当店の2号店は9月11日に開店します。","その店にもぜひお越しください。"],
]):
    for r,ja in zip(block,translations): r[1]=ja
for block,translations in [(EMAIL[1],[
    "ウィリアムへ、","今月、学校でハロウィーンパーティーを開きます。","あなたは何を着る予定ですか。",
    "私は猫になりたいです。","今、その服を探しています。","ところで、パンプキンパイは好きですか。",
    "今週末、姉（妹）といくつか作る予定です。","一緒にいくつか作りませんか。","あなたの友人、","シャーロット"]),
    (EMAIL[3],["シャーロットへ、","ハロウィーンパーティーで野球選手になりたいので、母が私のために服を作ってくれています。",
               "土曜日に新しい帽子を買う予定です。","でも日曜日は空いています。","一緒にパンプキンパイを作りたいです。",
               "お菓子をいくつか持っていきます。","あなたの友人、","ウィリアム"]),
    (ARTICLE[0],["アヤは高校生です。","彼女の高校にはスペイン語、フランス語、中国語、ドイツ語の授業があります。",
                 "アヤはフランス語の授業を受けています。","去年、アヤはパリに留学しました。",
                 "食事やホストファミリーと過ごすことを楽しみにしていましたが、飛行機に乗ることには不安を感じていました。"]),
    (ARTICLE[1],["パリでは、アヤは毎日フランス語を勉強しました。","週末は電車に乗り、ホストファミリーと図書館へ行きました。",
                 "大きな公園の中にある美術館にも行きました。","美術館にはたくさんの美しく有名な絵がありました。","アヤは芸術についてもっと学びたいと思いました。"]),
    (ARTICLE[2],["パリ滞在の後、アヤは高校の友人たちと絵のレッスンを受け始めました。",
                 "最初は絵を描くのが上手ではありませんでしたが、上達しました。","何枚かの絵を、手紙を添えてパリのホストファミリーに送りました。",
                 "今は以前より熱心にフランス語を勉強し、毎週末美術館を訪れています。","将来は画家になってフランスに住みたいと思っています。"]),
]:
    for r,ja in zip(block,translations): r[1]=ja


def instruction(kind, start, end):
    nums=f"({start})と({end})" if end-start==1 else f"({start})から({end})まで"
    return f"次の{kind}の内容に関して，{nums}の質問に対する答えとして最も適切なもの，または文を完成させるのに最も適切なものを1，2，3，4の中から一つ選び，その番号のマーク欄をぬりつぶしなさい。"


def passage(label, title, blocks, questions, kind, start, end):
    paragraphs=[("\n" if label=="4A" and i==0 or label=="4B" and i%2==0 else " ").join(r[0] for r in block) for i,block in enumerate(blocks)]
    if label=="4B":
        for i in (1,3):
            b=blocks[i]
            paragraphs[i]=b[0][0]+"\n"+" ".join(r[0] for r in b[1:-2])+"\n"+b[-2][0]+"\n"+b[-1][0]
    return dict(label=label,title=title,instruction=instruction(kind,start,end),paragraphs=paragraphs,
                translations=["\n".join(r[1] for r in b) for b in blocks],
                sentencePairs=[r for b in blocks for r in b], questions=questions)


PASSAGES=[
    passage("4A","Weekend Sale at Market Town Sports Store",NOTICE,[
        question(26,"What will be $10 each during the sale?","セール中に1つ10ドルになるのは何ですか。",
                 ["Tennis rackets.","Baseball gloves.","Swimming caps.","Soccer balls."],
                 ["テニスラケット。","野球グローブ。","水泳帽。","サッカーボール。"],4,["Soccer balls will be $10 each"],
                 "価格と品物を対応させる。サッカーボールが10ドル、水泳帽は5ドル。グローブとラケットは70％引きで、10ドルとは書かれていない。",
                 "10ドルはサッカーボールだよ。すいえいぼうの5ドルと、まちがえないでね。",
                 ["ラケットは70％引きで、10ドルとはない。","グローブは70％引きで、10ドルとはない。","水泳帽は1つ5ドル。","1つ10ドルと本文に書かれている。"],
                 ["70％びきのものだよ。","70％びきのものだよ。","すいえいぼうは5ドルだよ。","ボールが10ドルだね。"]),
        question(27,"When will the second store open?","2号店はいつ開店しますか。",
                 ["On August 28.","On August 29.","On September 10.","On September 11."],
                 ["8月28日。","8月29日。","9月10日。","9月11日。"],4,["Our second store on Sun Street will open on September 11."],
                 "セールの日程と新店の開店日を区別する。8月28日・29日はセール、2号店の開店は9月11日。",
                 "セールのひではなく、あたらしいおみせがひらくひをさがすよ。9がつ11にちだね。",
                 ["セール初日で、2号店の開店日ではない。","セール2日目で、2号店の開店日ではない。","9月10日とは書かれていない。","2号店が開く日付に一致する。"],
                 ["セールがはじまるひだよ。","セールの2にちめだよ。","10にちではないよ。","11にちにひらくね。"]),
    ],"掲示",26,27),
    passage("4B","Halloween party / This weekend",EMAIL,[
        question(28,"What does Charlotte want to be for a Halloween party?","シャーロットはハロウィーンパーティーで何になりたいですか。",
                 ["A baseball player.","A singer.","A rabbit.","A cat."],
                 ["野球選手。","歌手。","ウサギ。","猫。"],4,["I want to be a cat."],
                 "1通目の差出人 Charlotte の I want を読む。猫になりたいのは Charlotte、野球選手になりたいのは2通目の William。人物を取り違えない。",
                 "シャーロットは、ねこになりたいよ。やきゅうせんしゅは、ウィリアムのほうだね。",
                 ["野球選手になりたいのは William。","歌手になりたいとは書かれていない。","ウサギになりたいとは書かれていない。","Charlotte がなりたいものに一致する。"],
                 ["ウィリアムがなりたいものだよ。","うたうひとではないよ。","ウサギではないよ。","シャーロットは、ねこだね。"]),
        question(29,"This weekend, Charlotte is going to","今週末、シャーロットは～する予定です。",
                 ["go shopping with her sister.","make pumpkin pies.","play baseball at the park.","go to a clothes shop."],
                 ["姉（妹）と買い物に行く。","パンプキンパイを作る。","公園で野球をする。","洋服店へ行く。"],2,
                 ["I am going to make some with my sister this weekend."],
                 "直前の pumpkin pie を some が受ける。服を探しているのは現在、今週末の予定は姉（妹）とパイを作ること。",
                 "some は、まえにあるパンプキンパイのこと。こんしゅうまつは、パイをつくるんだね。",
                 ["姉妹とするのは買い物ではなくパイ作り。","some が pumpkin pie を受け、週末に作る。","公園で野球をする予定はない。","服を探しているが、週末の予定として洋服店へ行くとはない。"],
                 ["きょうだいとは、パイをつくるよ。","パンプキンパイをつくるね。","やきゅうのよていではないよ。","しゅうまつは、ふくをかうのではないよ。"]),
        question(30,"What is William going to do on Saturday?","ウィリアムは土曜日に何をする予定ですか。",
                 ["Go to the library.","Play catch.","Buy a cap.","Cook dinner."],
                 ["図書館へ行く。","キャッチボールをする。","帽子を買う。","夕食を作る。"],3,
                 ["I am going to buy a new cap on Saturday."],
                 "2通目の William の土曜日の予定は帽子の購入。日曜日は空いていてパイ作りをしたいと言う。曜日ごとに予定を整理する。",
                 "どようびは、あたらしいぼうしをかうよ。にちようびのパイづくりと、わけてよもう。",
                 ["図書館に行く予定は書かれていない。","野球の仮装をするが、キャッチボールの予定はない。","Saturday の直前に buy a new cap とある。","パイ作りは希望しているが、土曜に夕食を作るとはない。"],
                 ["としょかんのよていはないよ。","キャッチボールではないよ。","どようびにぼうしをかうね。","ゆうしょくをつくるのではないよ。"]),
    ],"Eメール",28,30),
    passage("4C","A Museum in France",ARTICLE,[
        question(31,"What language does Aya study at school?","アヤは学校で何語を勉強していますか。",
                 ["Spanish.","French.","Chinese.","German."],["スペイン語。","フランス語。","中国語。","ドイツ語。"],2,["Aya takes French lessons."],
                 "学校にある4言語の授業と、Aya が選んで受けている授業を区別する。次の文で French と限定される。",
                 "がっこうには、4つのことばのじゅぎょうがあるよ。アヤがうけているのはフランスごだね。",
                 ["学校の授業にはあるが、Aya の選択ではない。","Aya が受ける授業の言語に一致する。","学校の授業にはあるが、Aya の選択ではない。","学校の授業にはあるが、Aya の選択ではない。"],
                 ["じゅぎょうはあるけど、アヤはえらんでいないよ。","アヤはフランスごをべんきょうしているね。","アヤがうけているのではないよ。","アヤがうけているのではないよ。"]),
        question(32,"What was Aya nervous about?","アヤは何に不安を感じていましたか。",
                 ["Eating new food.","Speaking a foreign language.","Taking a plane.","Staying with a host family."],
                 ["新しい食べ物を食べること。","外国語を話すこと。","飛行機に乗ること。","ホストファミリーと過ごすこと。"],3,["she was nervous about taking a plane."],
                 "but の前は楽しみなこと、後ろは不安なこと。食事とホームステイは excited、飛行機は nervous と対応させる。",
                 "ごはんとホームステイは、たのしみ。ひこうきにのるのが、しんぱいだったんだね。",
                 ["食事は excited と楽しみにしていた。","外国語を話すことが不安とは書かれていない。","nervous about の後ろにある内容。","ホームステイは excited と楽しみにしていた。"],
                 ["たべものは、たのしみだったよ。","ことばがしんぱいとは、かいていないよ。","ひこうきがしんぱいだったね。","ホームステイは、たのしみだったよ。"]),
        question(33,"Where was the art museum in Paris?","パリの美術館はどこにありましたか。",
                 ["In a large park.","Next to a library.","Near a train station.","By Aya's house."],
                 ["大きな公園の中。","図書館の隣。","駅の近く。","アヤの家のそば。"],1,["an art museum in a large park"],
                 "in a large park が art museum を説明する。電車や図書館も登場するが、美術館の所在地ではない。",
                 "びじゅつかんは、おおきなこうえんのなか。としょかんやでんしゃもでるけど、ばしょをまちがえないでね。",
                 ["美術館の場所を示す語句に一致する。","図書館に行ったが、美術館がその隣とはない。","電車に乗ったが、駅の近くとはない。","Aya の家のそばとは書かれていない。"],
                 ["こうえんのなかだね。","としょかんのとなりとは、かいていないよ。","えきのちかくとは、かいていないよ。","いえのそばとは、かいていないよ。"]),
        question(34,"After her stay in Paris, Aya","パリ滞在の後、アヤは～しました。",
                 ["visited the library.","went to a restaurant.","met new friends.","took painting lessons."],
                 ["図書館を訪れた。","レストランへ行った。","新しい友人に会った。","絵のレッスンを受けた。"],4,
                 ["After her stay in Paris, Aya started taking painting lessons with her friends from high school."],
                 "After her stay in Paris が帰国後の時期を示し、started taking painting lessons が新しい行動。図書館はパリ滞在中の行動。",
                 "パリからかえってから、えのレッスンをはじめたよ。としょかんは、パリにいたときのおはなしだね。",
                 ["図書館に行ったのはパリ滞在中。","帰国後にレストランへ行ったとはない。","高校の友人と受講したが、新しい友人に会ったとはない。","帰国後に始めたレッスンに一致する。"],
                 ["としょかんは、パリにいたときだよ。","レストランのおはなしはないよ。","あたらしいともだちにあった、ではないよ。","えのレッスンをはじめたね。"]),
        question(35,"What does Aya do every weekend now?","今アヤは毎週末何をしますか。",
                 ["She cooks French food.","She visits museums.","She studies Italian.","She writes letters."],
                 ["フランス料理を作る。","美術館を訪れる。","イタリア語を勉強する。","手紙を書く。"],2,["visits museums every weekend."],
                 "Now と every weekend が現在の習慣を示す。毎週末することは美術館訪問。手紙は以前絵を送ったとき、勉強している言語は French。",
                 "『いま』『まいしゅうまつ』にちゅうい。アヤは、まいしゅうまつびじゅつかんにいくんだね。",
                 ["料理を作る習慣は書かれていない。","毎週末の行動として visits museums とある。","勉強しているのは French で、Italian ではない。","絵に手紙を添えたが、毎週末書く習慣とはない。"],
                 ["りょうりをつくるとは、かいていないよ。","びじゅつかんにいくね。","フランスごで、イタリアごではないよ。","てがみは、えをおくったときのことだよ。"]),
    ],"英文",31,35),
]

PASSAGES[0]["format"]="notice"
PASSAGES[1]["format"]="multi-email"
PASSAGES[1]["emails"]=[]
for i in (0,2):
    meta={line.partition(":")[0].lower():line.partition(":")[2].strip() for line in PASSAGES[1]["paragraphs"][i].splitlines()}
    PASSAGES[1]["emails"].append(dict(meta=meta,body=PASSAGES[1]["paragraphs"][i+1],translation=PASSAGES[1]["translations"][i+1]))

"""Booklet pp. 6-11: verb-aware, fully aligned bilingual reading units."""


def row(units, verb=""):
    return [" ".join(x[0] for x in units), "".join(x[1] for x in units),
            "||".join(a+"|"+b for a,b in units), verb]


def plain(en, ja):
    return row([(en,ja)])


def question(n, stem, ja, choices, meanings, answer, evidence, note, simple, reasons, easy):
    return dict(number=n, question=stem, questionTranslation=ja, choices=choices,
                choiceTranslations=meanings, answer=answer, sourceEvidence=evidence,
                grammar=f"本文の根拠は「{' / '.join(evidence)}」。{note}", grammarSimple=simple,
                choiceAnalysis=[("○ " if i==answer else "")+f"{c}＝{t.rstrip('。')}。{r}" for i,(c,t,r) in enumerate(zip(choices,meanings,reasons),1)],
                choiceAnalysisSimple=[("○ " if i==answer else "")+f"{t.rstrip('。')}。{r}" for i,(t,r) in enumerate(zip(meanings,easy),1)])


# The notice keeps the booklet's four visual blocks: heading, news, Place/Time, performances.
NOTICE=[
    [plain("Town Parade","町のパレード")],
    [row([("The town basketball team","町のバスケットボールチームが"),("won the tournament!","トーナメントで優勝しました。")],"won"),
     row([("There will be a town parade","町のパレードがあります、"),("next Saturday","次の土曜日に、"),("with food and performances.","食べ物や出し物つきで。")],"will")],
    [plain("Place: Main Street","場所：メイン・ストリート"),
     plain("Time: 1:00 p.m. to 4:00 p.m.","時間：午後1時から午後4時まで")],
    [row([("The Redwood Junior High School band","レッドウッド中学校のバンドは"),("will perform three songs","3曲を演奏します、"),("for the team.","チームのために。")],"will"),
     row([("The dance club will dance","ダンスクラブは踊ります、"),("to two songs,","2曲に合わせて。"),("and the chorus will sing one song.","そして合唱団は1曲を歌います。")],"will")],
]

EMAIL=[
    [plain("From: Andy Douglas","差出人：アンディ・ダグラス"),plain("To: Dave Anderson","宛先：デイブ・アンダーソン"),
     plain("Date: July 10","日付：7月10日"),plain("Subject: Trip to the mountains","件名：山への旅行")],
    [plain("Hello Dave,","デイブへ、"),
     row([("Next weekend,","来週末、"),("my family will go","私の家族は行きます、"),("to the mountains.","山へ。")],"will"),
     row([("We'll go there","私たちはそこへ行きます、"),("on Friday night.","金曜日の夜に。")],"go"),
     row([("We'll stay","私たちは泊まります、"),("in a house by a lake.","湖のそばの家に。")],"stay"),
     row([("We'll go fishing on Saturday","私たちは土曜日に釣りに行き、"),("and hiking on Sunday.","日曜日にハイキングに行きます。")],"go"),
     row([("We'll come back","私たちは帰ってきます、"),("on Monday morning.","月曜日の朝に。")],"come"),
     row([("There are three bedrooms in the house,","その家には寝室が3つあり、"),("and my room has two beds.","私の部屋にはベッドが2台あります。")],"are"),
     row([("Do you want","あなたはしたいですか、"),("to come with us?","私たちと一緒に来ることを。")],"want"),
     plain("Your friend,","あなたの友人、"),plain("Andy","アンディ")],
    [plain("From: Dave Anderson","差出人：デイブ・アンダーソン"),plain("To: Andy Douglas","宛先：アンディ・ダグラス"),
     plain("Date: July 11","日付：7月11日"),plain("Subject: Sounds fun!","件名：楽しそう！")],
    [plain("Hi Andy,","アンディへ、"),
     row([("I talked to my mom","私は母に話しました、"),("about the trip,","その旅行について。"),("and she said, \"You can go.\"","すると母は『行っていいよ』と言いました。")],"talked"),
     row([("My father and I","父と私は"),("went camping last year.","去年キャンプに行きました。")],"went"),
     row([("We stayed in a tent","私たちはテントに泊まりました、"),("for one night.","1晩。")],"stayed"),
     row([("My sister didn't come","姉（妹）は来ませんでした、"),("because she doesn't like camping.","キャンプが好きではないので。")],"come"),
     row([("I'm looking forward","私は楽しみにしています、"),("to going to the mountains with you!","あなたと一緒に山へ行くことを。")],"looking"),
     plain("See you,","またね、"),plain("Dave","デイブ")],
]

ARTICLE=[
    [row([("Kate is a high school student,","ケイトは高校生で、"),("and she loves","彼女は大好きです、"),("eating at restaurants and cafés.","レストランやカフェで食べることが。")],"is"),
     row([("On weekdays,","平日は、"),("she usually eats lunch","彼女はたいてい昼食を食べます、"),("at the school cafeteria","学校の食堂で"),("with her friends.","友だちと。")],"eats"),
     row([("On weekends,","週末は、"),("she often eats noodles","彼女はよく麺類を食べます、"),("at restaurants with her cousin.","いとこと一緒にレストランで。")],"eats")],
    [row([("On her birthday this year,","今年の誕生日に、"),("Kate had dinner","ケイトは夕食を食べました、"),("with her grandparents.","祖父母と。")],"had"),
     row([("They are seventy years old,","祖父母は70歳ですが、"),("but they look younger.","年齢より若く見えます。")],"are"),
     row([("Kate asked them,","ケイトは祖父母に尋ねました、"),("\"Why do you look so young?\"","「どうしてそんなに若く見えるの？」と。")],"asked"),
     row([("Her grandmother said,","祖母は言いました、"),("\"We like cooking at home,","「私たちは家で料理をするのが好きで、"),("and we always make healthy meals.\"","いつも健康的な食事を作っているのよ」と。")],"said"),
     row([("Kate said,","ケイトは言いました、"),("\"Please teach me how to cook.\"","「料理の仕方を教えて」と。")],"said")],
    [row([("The next weekend,","次の週末、"),("Kate went","ケイトは行きました、"),("to her grandparents' house.","祖父母の家へ。")],"went"),
     row([("Kate's grandmother said,","ケイトの祖母は言いました、"),("\"Let's make curry","「カレーを作りましょう、"),("with chicken and lots of vegetables","鶏肉とたくさんの野菜で、"),("for lunch.\"","昼食に」と。")],"said"),
     row([("The curry was easy to make,","カレーは作るのが簡単だったので、"),("so Kate was surprised.","ケイトは驚きました。")],"was"),
     row([("It was","それは"),("delicious, too.","おいしくもありました。")],"was"),
     row([("She said,","彼女は言いました、"),("\"I'm going to make lots of healthy meals","「健康的な食事をたくさん作るつもりよ、"),("for Mom and Dad, too.\"","お母さんとお父さんにも」と。")],"said"),
     row([("Kate still enjoys eating","ケイトは今でも食べることを楽しんでいます、"),("at restaurants and cafés,","レストランやカフェで。"),("but she loves making healthy meals","でも健康的な食事を作ることも大好きです、"),("at home, too.","家で。")],"enjoys")],
]

# Full translations read naturally; bilingual slash units retain English order.
for block,translations in [(NOTICE[1],["町のバスケットボールチームがトーナメントで優勝しました。","次の土曜日に、食べ物や出し物のある町のパレードが行われます。"]),
    (NOTICE[3],["レッドウッド中学校のバンドが、チームのために3曲を演奏します。","ダンスクラブは2曲に合わせて踊り、合唱団は1曲を歌います。"]),
    (EMAIL[1],["デイブへ、","来週末、私の家族は山へ行きます。","金曜日の夜にそこへ向かいます。","湖のそばの家に泊まります。",
               "土曜日は釣りに、日曜日はハイキングに行きます。","月曜日の朝に帰ってきます。",
               "その家には寝室が3つあって、私の部屋にはベッドが2台あります。","私たちと一緒に来ませんか。","あなたの友人、","アンディ"]),
    (EMAIL[3],["アンディへ、","旅行のことを母に話したら、『行っていいよ』と言ってくれました。","父と私は去年キャンプに行きました。",
               "テントに1晩泊まりました。","姉（妹）はキャンプが好きではないので、来ませんでした。",
               "あなたと一緒に山へ行くのを楽しみにしています。","またね、","デイブ"]),
    (ARTICLE[0],["ケイトは高校生で、レストランやカフェで食事をするのが大好きです。","平日は、たいてい学校の食堂で友だちと昼食を食べます。",
                 "週末は、よくいとこと一緒にレストランで麺類を食べます。"]),
    (ARTICLE[1],["今年の誕生日に、ケイトは祖父母と夕食を食べました。","祖父母は70歳ですが、年齢より若く見えます。",
                 "ケイトは祖父母に「どうしてそんなに若く見えるの？」と尋ねました。",
                 "祖母は「私たちは家で料理をするのが好きで、いつも健康的な食事を作っているのよ」と言いました。",
                 "ケイトは「料理の仕方を教えて」と言いました。"]),
    (ARTICLE[2],["次の週末、ケイトは祖父母の家へ行きました。","ケイトの祖母は「お昼に、鶏肉とたくさんの野菜でカレーを作りましょう」と言いました。",
                 "カレーは作るのが簡単だったので、ケイトは驚きました。","それに、おいしくもありました。",
                 "ケイトは「お母さんとお父さんにも、健康的な食事をたくさん作るつもりよ」と言いました。",
                 "ケイトは今でもレストランやカフェで食べるのを楽しんでいますが、家で健康的な食事を作ることも大好きです。"]),
]:
    for r,ja in zip(block,translations): r[1]=ja


def instruction(kind, start, end):
    nums=f"({start})と({end})" if end-start==1 else f"({start})から({end})まで"
    return f"次の{kind}の内容に関して，{nums}の質問に対する答えとして最も適切なもの，または文を完成させるのに最も適切なものを1，2，3，4の中から一つ選び，その番号のマーク欄をぬりつぶしなさい。"


def email_body(block):
    return block[0][0]+"\n"+" ".join(r[0] for r in block[1:-2])+"\n"+block[-2][0]+"\n"+block[-1][0]


def passage(label, title, blocks, questions, kind, start, end):
    if label=="4A":
        # Place/Time stay on separate lines, as printed.
        paragraphs=[("\n" if i==2 else " ").join(r[0] for r in block) for i,block in enumerate(blocks)]
    elif label=="4B":
        paragraphs=["\n".join(r[0] for r in block) if i%2==0 else email_body(block) for i,block in enumerate(blocks)]
    else:
        paragraphs=[" ".join(r[0] for r in block) for block in blocks]
    return dict(label=label,title=title,instruction=instruction(kind,start,end),paragraphs=paragraphs,
                translations=["\n".join(r[1] for r in b) for b in blocks],
                sentencePairs=[r for b in blocks for r in b], questions=questions)


PASSAGES=[
    passage("4A","Town Parade",NOTICE,[
        question(26,"When will the parade start?","パレードはいつ始まりますか。",
                 ["At 1:00 p.m.","At 2:00 p.m.","At 3:00 p.m.","At 4:00 p.m."],
                 ["午後1時。","午後2時。","午後3時。","午後4時。"],1,["Time: 1:00 p.m. to 4:00 p.m."],
                 "A to B は『A から B まで』。始まる時刻は最初の 1:00 p.m.、4:00 p.m. は終わる時刻。2時・3時は掲示に書かれていない。",
                 "1:00 p.m. to 4:00 p.m. は『ごご1じから4じまで』。はじまるのは1じだね。4じは、おわるじかんだよ。",
                 ["Time の最初の時刻で、パレードが始まる時刻。","午後2時は掲示に書かれていない。","午後3時は掲示に書かれていない。","午後4時は終わる時刻で、始まる時刻ではない。"],
                 ["ごご1じにはじまるね。","2じとは、かいていないよ。","3じとは、かいていないよ。","4じは、おわるじかんだよ。"]),
        question(27,"How many songs will the school band perform?","学校のバンドは何曲演奏しますか。",
                 ["One song.","Two songs.","Three songs.","Four songs."],
                 ["1曲。","2曲。","3曲。","4曲。"],3,["The Redwood Junior High School band will perform three songs for the team."],
                 "the school band は The Redwood Junior High School band のこと。バンドは3曲、ダンスクラブは2曲、合唱団は1曲。グループと曲数を一つずつ対応させる。",
                 "バンドは3きょく。ダンスは2きょく、がっしょうは1きょく。だれが、なんきょくかをわけてよもう。",
                 ["1曲は合唱団が歌う曲数。","2曲はダンスクラブが踊る曲数。","バンドが演奏する曲数に一致する。","4曲という数は掲示にない。"],
                 ["1きょくは、がっしょうだよ。","2きょくは、ダンスだよ。","バンドは3きょくだね。","4きょくとは、かいていないよ。"]),
    ],"掲示",26,27),
    passage("4B","Trip to the mountains / Sounds fun!",EMAIL,[
        question(28,"Andy's family will go fishing on","アンディの家族は～に釣りに行きます。",
                 ["Monday.","Friday.","Saturday.","Sunday."],
                 ["月曜日。","金曜日。","土曜日。","日曜日。"],3,["We'll go fishing on Saturday and hiking on Sunday."],
                 "曜日ごとの予定を整理する。金曜日の夜に山へ向かい、土曜日に釣り、日曜日にハイキング、月曜日の朝に帰る。go fishing の直後の on Saturday が答え。",
                 "きんようびのよるにでかけて、どようびはつり、にちようびはハイキング。つりは、どようびだね。",
                 ["月曜日の朝は帰ってくる日。","金曜日の夜は山へ向かう日。","go fishing on Saturday とある。","日曜日はハイキングに行く日。"],
                 ["げつようびは、かえってくるひだよ。","きんようびは、でかけるひだよ。","どようびに、つりにいくね。","にちようびは、ハイキングだよ。"]),
        question(29,"How many bedrooms are there in the house by the lake?","湖のそばの家には寝室がいくつありますか。",
                 ["One.","Two.","Three.","Four."],
                 ["1つ。","2つ。","3つ。","4つ。"],3,["There are three bedrooms in the house"],
                 "There are three bedrooms in the house で寝室は3つ。two は Andy の部屋にあるベッドの数で、寝室の数ではない。数字が何を数えているかを確かめる。",
                 "しんしつは3つ。2は、アンディのへやのベッドのかずだよ。まちがえないでね。",
                 ["1つとは書かれていない。","2は Andy の部屋のベッドの数。","three bedrooms とある。","4つとは書かれていない。"],
                 ["1つとは、かいていないよ。","2は、ベッドのかずだよ。","しんしつは3つだね。","4つとは、かいていないよ。"]),
        question(30,"What did Dave do last year?","デイブは去年何をしましたか。",
                 ["He went to the beach.","He stayed by a lake.","He went hiking.","He went camping."],
                 ["海辺へ行った。","湖のそばに泊まった。","ハイキングに行った。","キャンプに行った。"],4,["My father and I went camping last year."],
                 "2通目の差出人 Dave の文を読む。My father and I の I が Dave。湖のそばに泊まることとハイキングは、Andy の家族の来週末の予定。",
                 "デイブは、きょねんおとうさんとキャンプにいったよ。みずうみやハイキングは、アンディたちのこんどのよていだね。",
                 ["海辺へ行ったとは書かれていない。","湖のそばに泊まるのは Andy の家族の来週末の予定。","ハイキングは Andy の家族の日曜日の予定。","去年、父とキャンプに行ったとある。"],
                 ["うみへいったとは、かいていないよ。","みずうみは、アンディたちのよていだよ。","ハイキングも、アンディたちのよていだよ。","キャンプにいったね。"]),
    ],"Eメール",28,30),
    passage("4C","Healthy Meals",ARTICLE,[
        question(31,"Where does Kate usually eat lunch on weekdays?","ケイトは平日、たいていどこで昼食を食べますか。",
                 ["At home.","At her friend's house.","At the school cafeteria.","At her grandparents' house."],
                 ["家で。","友だちの家で。","学校の食堂で。","祖父母の家で。"],3,
                 ["On weekdays, she usually eats lunch at the school cafeteria with her friends."],
                 "On weekdays（平日）と usually（たいてい）が質問と対応する。学校の食堂で友だちと食べる。friends は一緒に食べる相手で、友だちの家で食べるわけではない。祖父母の家へ行ったのは誕生日の次の週末。",
                 "へいじつは、がっこうのしょくどうでともだちとたべるよ。ともだちのいえではないから、ちゅういしよう。",
                 ["家で昼食を食べるとは書かれていない。","友だちは一緒に食べる相手で、友だちの家ではない。","平日の昼食の場所に一致する。","祖父母の家へ行ったのは、誕生日の次の週末。"],
                 ["いえでたべる、とはかいていないよ。","ともだちのいえではないよ。","がっこうのしょくどうだね。","おじいちゃんのいえは、ちがうひのことだよ。"]),
        question(32,"What does Kate often do on weekends?","ケイトは週末によく何をしますか。",
                 ["She works at a café.","She eats noodles with her cousin.","She helps at her grandparents' restaurant.","She studies at school."],
                 ["カフェで働く。","いとこと麺類を食べる。","祖父母のレストランを手伝う。","学校で勉強する。"],2,
                 ["On weekends, she often eats noodles at restaurants with her cousin."],
                 "On weekends と often が質問と対応する。いとこと一緒にレストランで麺類を食べる。カフェは食事をする場所として好きなだけで、働いているとは書かれていない。祖父母のレストランも本文に出てこない。",
                 "しゅうまつは、いとことレストランでめんをたべるよ。カフェではたらく、とはかいていないね。",
                 ["カフェで食べるのが好きなだけで、働くとはない。","週末によくすることとして書かれている。","祖父母のレストランは本文に出てこない。","週末に学校で勉強するとは書かれていない。"],
                 ["カフェではたらくとは、かいていないよ。","いとことめんをたべるね。","おじいちゃんのおみせは、でてこないよ。","がっこうでべんきょう、ではないよ。"]),
        question(33,"Who did Kate have dinner with on her birthday this year?","今年の誕生日に、ケイトは誰と夕食を食べましたか。",
                 ["Her cousin.","Her friends.","Her grandparents.","Her teacher."],
                 ["いとこ。","友だち。","祖父母。","先生。"],3,["On her birthday this year, Kate had dinner with her grandparents."],
                 "had dinner with の後ろが一緒に食べた相手。誕生日は祖父母と夕食。いとこは週末に麺類を食べる相手、友だちは平日に昼食を食べる相手で、場面ごとに相手が違う。",
                 "たんじょうびは、おじいちゃんとおばあちゃんとばんごはん。いとこやともだちは、ちがうひのあいてだよ。",
                 ["いとこは週末に麺類を一緒に食べる相手。","友だちは平日に昼食を一緒に食べる相手。","誕生日の夕食の相手に一致する。","先生は本文に出てこない。"],
                 ["いとこは、しゅうまつのあいてだよ。","ともだちは、おひるごはんのあいてだよ。","おじいちゃんとおばあちゃんだね。","せんせいは、でてこないよ。"]),
        question(34,"Why was Kate surprised?","ケイトはなぜ驚いたのですか。",
                 ["The curry was easy to make.","The curry wasn't delicious.","The curry had no vegetables.","The curry was expensive to buy."],
                 ["カレーは作るのが簡単だった。","カレーはおいしくなかった。","カレーには野菜が入っていなかった。","カレーは買うには値段が高かった。"],1,
                 ["The curry was easy to make, so Kate was surprised."],
                 "A, so B は『A なので B』。so の前の The curry was easy to make が驚いた理由。カレーはおいしく、野菜もたくさん使ったので、2と3は本文と逆。カレーは買ったのではなく家で作った。",
                 "so は『だから』。カレーをつくるのがかんたんだったから、びっくりしたんだね。",
                 ["so の前に書かれた驚きの理由。","It was delicious, too. とあり、本文と逆。","lots of vegetables を使ったので本文と逆。","家で作ったカレーで、買ったとは書かれていない。"],
                 ["かんたんだったから、びっくりしたね。","おいしかったよ。","やさいも、たくさんはいっていたよ。","かったのではなく、つくったよ。"]),
        question(35,"Now, Kate loves to","今、ケイトは～するのが大好きです。",
                 ["wash the dishes after dinner.","grow vegetables in her garden.","make healthy meals at home.","clean her grandparents' house."],
                 ["夕食の後に皿を洗う。","庭で野菜を育てる。","家で健康的な食事を作る。","祖父母の家を掃除する。"],3,
                 ["she loves making healthy meals at home, too."],
                 "最後の文の but の後ろが今の気持ち。loves making ～ と loves to make ～ はどちらも『～を作るのが大好き』。皿洗い・野菜作り・掃除は本文に出てこない。",
                 "さいごのぶんに、いえでけんこうてきなごはんをつくるのがだいすき、とあるよ。",
                 ["皿を洗う話は本文にない。","庭で野菜を育てる話は本文にない。","最後の文の loves making healthy meals at home に一致する。","祖父母の家を掃除する話は本文にない。"],
                 ["おさらあらいは、でてこないよ。","やさいをそだてる、とはかいていないよ。","いえでごはんをつくるのが、だいすきだね。","そうじは、でてこないよ。"]),
    ],"英文",31,35),
]

PASSAGES[0]["format"]="notice"
PASSAGES[1]["format"]="multi-email"
PASSAGES[1]["emails"]=[]
for i in (0,2):
    meta={line.partition(":")[0].lower():line.partition(":")[2].strip() for line in PASSAGES[1]["paragraphs"][i].splitlines()}
    PASSAGES[1]["emails"].append(dict(meta=meta,body=PASSAGES[1]["paragraphs"][i+1],translation=PASSAGES[1]["translations"][i+1]))

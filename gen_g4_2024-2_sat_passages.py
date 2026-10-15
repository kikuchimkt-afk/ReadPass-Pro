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


# The notice keeps the booklet's blocks: heading, date, opening sentence, the three bold
# schedule lines (one block each, so the app shows them on separate lines) and the body.
# The booklet prints the date "October 1" above the heading; the app always shows the
# first block as the heading, so the date follows it here.
NOTICE=[
    [plain("TO ALL STUDENTS","生徒のみなさんへ")],
    [plain("October 1","10月1日")],
    [row([("From today,","今日から、"),("the school library will open","学校の図書館は開きます、"),("at different times.","今までと違う時間に。")],"open")],
    [row([("Monday to Friday:","月曜日から金曜日："),("8:00 a.m. to 7:00 p.m.","午前8時から午後7時まで")])],
    [row([("Saturday:","土曜日："),("9:00 a.m. to 5:00 p.m.","午前9時から午後5時まで")])],
    [row([("Sunday:","日曜日："),("Closed","休み")])],
    [row([("You can use","使うことができます、"),("your student ID card","生徒証を、"),("to borrow books.","本を借りるために。")],"use"),
     row([("There are also","…もあります、"),("some new computers","新しいコンピューターが何台か、"),("in the library.","図書館には。")],"are"),
     row([("You must ask a teacher","先生に尋ねなければなりません、"),("before you use them.","それらを使う前に。")],"ask")],
]

EMAIL=[
    [plain("From: Elizabeth Young","差出人：エリザベス・ヤング"),plain("To: Ollie Young","宛先：オリー・ヤング"),
     plain("Date: April 25","日付：4月25日"),plain("Subject: New school","件名：新しい学校")],
    [plain("Hi Ollie,","オリーへ、"),
     row([("How's","どうですか、"),("your new school?","新しい学校は。")],"'s"),
     row([("You go there","あなたはそこへ通っています、"),("by train,","電車で、"),("right?","そうですよね。")],"go"),
     row([("How long","どれくらい"),("does it take?","かかりますか。")],"take"),
     row([("When I was young,","私が若かったころ、"),("I walked","私は歩いて行きました、"),("to school.","学校へ。")],"walked"),
     row([("I heard","私は聞きました、"),("about your school's baseball team","あなたの学校の野球部のことを、"),("from your mom.","あなたのお母さんから。")],"heard"),
     row([("Are you enjoying","あなたは楽しんでいますか、"),("the practices?","練習を。")],"enjoying"),
     row([("I'll come and watch","私は見に行きます、"),("your next game.","あなたの次の試合を。")],"come"),
     row([("When","いつですか、"),("is it?","それは。")],"is"),
     plain("Take care!","元気でね！"),plain("Grandma","おばあちゃんより")],
    [plain("From: Ollie Young","差出人：オリー・ヤング"),plain("To: Elizabeth Young","宛先：エリザベス・ヤング"),
     plain("Date: April 26","日付：4月26日"),plain("Subject: Baseball","件名：野球")],
    [plain("Hi Grandma,","おばあちゃんへ、"),
     row([("My new school","新しい学校は"),("is OK.","まあまあです。")],"is"),
     row([("I ride my bike","ぼくは自転車に乗ります、"),("for 10 minutes","10分間、"),("to the station","駅まで、"),("every morning.","毎朝。")],"ride"),
     row([("The train ride to school","学校までの電車の乗車は"),("takes 30 minutes.","30分かかります。")],"takes"),
     row([("Then,","それから、"),("I walk for 15 minutes","ぼくは15分歩きます、"),("to my school.","学校まで。")],"walk"),
     row([("Baseball","野球は"),("is fun.","楽しいです。")],"is"),
     row([("We practice","ぼくたちは練習します、"),("for one hour","1時間、"),("on Wednesdays and Fridays.","毎週水曜日と金曜日に。")],"practice"),
     row([("We'll have a game","試合があります、"),("next Saturday.","次の土曜日に。")],"have"),
     row([("You can come","来ることができます、"),("and watch.","そして見ることが。")],"come"),
     plain("Your grandson,","あなたの孫、"),plain("Ollie","オリーより")],
]

ARTICLE=[
    [row([("Jay is","ジェイは"),("a junior high school student.","中学生です。")],"is"),
     row([("He likes","ジェイは好きです、"),("math and science,","数学と理科が。"),("but he doesn't like","でも好きではありません、"),("history.","歴史は。")],"likes"),
     row([("His favorite subject","ジェイのいちばん好きな教科は"),("is art.","美術です。")],"is"),
     row([("Last Wednesday,","この前の水曜日、"),("Jay painted","ジェイは描きました、"),("a picture of himself,","自分自身の絵を。"),("and his teacher said to him,","すると先生はジェイに言いました、"),("\"That's very good.\"","「とてもいいですね」と。")],"painted")],
    [row([("Last Friday,","この前の金曜日、"),("Jay's class went","ジェイのクラスは行きました、"),("to an art museum.","美術館へ。")],"went"),
     row([("In the morning,","午前中、"),("the students looked at","生徒たちは見ました、"),("the paintings","絵を、"),("in the museum.","美術館の。")],"looked"),
     row([("There were paintings","絵がありました、"),("of the sea","海の、"),("and paintings","そして絵が、"),("of rivers and mountains,","川や山の。"),("but Jay liked","でもジェイは気に入りました、"),("the paintings of people","人の絵を、"),("the best.","いちばん。")],"were")],
    [row([("After looking at the paintings,","絵を見た後、"),("Jay and his classmates ate lunch","ジェイとクラスメートは昼食を食べました、"),("in the museum's restaurant.","美術館のレストランで。")],"ate"),
     row([("His friend Jane ate","友だちのジェーンは食べました、"),("pasta and soup,","パスタとスープを。"),("and his friend Tony ate","そして友だちのトニーは食べました、"),("a hamburger.","ハンバーガーを。")],"ate"),
     row([("Jay ate","ジェイは食べました、"),("a salad.","サラダを。")],"ate")],
    [row([("That evening,","その晩、"),("Jay told his mother","ジェイは母に話しました、"),("about the art museum.","美術館のことを。")],"told"),
     row([("He said,","ジェイは言いました、"),("\"I want to take art classes.\"","「美術教室に通いたい」と。")],"said"),
     row([("On Saturday,","土曜日に、"),("his mother called","母は電話しました、"),("an art school","美術学校に、"),("near their house.","家の近くの。")],"called"),
     row([("Jay will start","ジェイは始めます、"),("art classes","美術教室を、"),("next Thursday.","次の木曜日に。")],"start"),
     row([("His dream is","ジェイの夢は"),("to become an artist.","芸術家になることです。")],"is")],
]

# Full translations read naturally; bilingual slash units retain English order.
for block,translations in [(NOTICE[2],["今日から、学校の図書館の開く時間が変わります。"]),
    (NOTICE[3],["月曜日～金曜日：午前8時～午後7時"]),(NOTICE[4],["土曜日：午前9時～午後5時"]),(NOTICE[5],["日曜日：休み"]),
    (NOTICE[6],["生徒証を使って本を借りることができます。","図書館には新しいコンピューターも何台かあります。",
                "コンピューターを使う前に、先生に尋ねなければなりません。"]),
    (EMAIL[1],["オリーへ、","新しい学校はどうですか。","電車で通っているのよね。","どれくらいかかるの？",
               "私が若いころは、歩いて学校に通っていました。","あなたのお母さんから、学校の野球部のことを聞きました。",
               "練習は楽しんでいますか。","次の試合を見に行きますね。","試合はいつですか。","元気でね！","おばあちゃんより"]),
    (EMAIL[3],["おばあちゃんへ、","新しい学校はまあまあだよ。","毎朝、駅まで自転車で10分走るんだ。",
               "学校までの電車は30分かかるよ。","それから、学校まで15分歩くんだ。","野球は楽しいよ。",
               "毎週水曜日と金曜日に1時間練習しているよ。","次の土曜日に試合があるんだ。","見に来ていいよ。",
               "あなたの孫、","オリーより"]),
    (ARTICLE[0],["ジェイは中学生です。","ジェイは数学と理科が好きですが、歴史は好きではありません。",
                 "いちばん好きな教科は美術です。",
                 "この前の水曜日、ジェイは自画像（自分自身の絵）を描き、先生はジェイに「とてもいいですね」と言いました。"]),
    (ARTICLE[1],["この前の金曜日、ジェイのクラスは美術館へ行きました。","午前中、生徒たちは美術館の絵を見ました。",
                 "海の絵や、川や山の絵がありましたが、ジェイがいちばん気に入ったのは人の絵でした。"]),
    (ARTICLE[2],["絵を見た後、ジェイとクラスメートは美術館のレストランで昼食を食べました。",
                 "友だちのジェーンはパスタとスープを、友だちのトニーはハンバーガーを食べました。","ジェイはサラダを食べました。"]),
    (ARTICLE[3],["その晩、ジェイは母に美術館のことを話しました。","ジェイは「美術教室に通いたい」と言いました。",
                 "土曜日に、母は家の近くの美術学校に電話しました。","ジェイは次の木曜日から美術教室に通い始めます。",
                 "ジェイの夢は芸術家になることです。"]),
]:
    for r,ja in zip(block,translations): r[1]=ja


def instruction(kind, start, end):
    nums=f"({start})と({end})" if end-start==1 else f"({start})から({end})まで"
    return f"次の{kind}の内容に関して，{nums}の質問に対する答えとして最も適切なもの，または文を完成させるのに最も適切なものを1，2，3，4の中から一つ選び，その番号のマーク欄をぬりつぶしなさい。"


def email_body(block):
    return block[0][0]+"\n"+" ".join(r[0] for r in block[1:-2])+"\n"+block[-2][0]+"\n"+block[-1][0]


def passage(label, title, blocks, questions, kind, start, end):
    if label=="4B":
        paragraphs=["\n".join(r[0] for r in block) if i%2==0 else email_body(block) for i,block in enumerate(blocks)]
    else:
        paragraphs=[" ".join(r[0] for r in block) for block in blocks]
    return dict(label=label,title=title,instruction=instruction(kind,start,end),paragraphs=paragraphs,
                translations=["\n".join(r[1] for r in b) for b in blocks],
                sentencePairs=[r for b in blocks for r in b], questions=questions)


PASSAGES=[
    passage("4A","TO ALL STUDENTS",NOTICE,[
        question(26,"What time will the library close next Saturday?","次の土曜日、図書館は何時に閉まりますか。",
                 ["At 5:00 p.m.","At 7:00 p.m.","At 8:00 p.m.","At 9:00 p.m."],
                 ["午後5時に。","午後7時に。","午後8時に。","午後9時に。"],1,
                 ["Saturday: 9:00 a.m. to 5:00 p.m."],
                 "質問は next Saturday（次の土曜日）に図書館が閉まる時刻。掲示の Saturday: 9:00 a.m. to 5:00 p.m. から、土曜日は午後5時まで開いている。7:00 p.m. は月曜日から金曜日に閉まる時刻。8:00 と 9:00 は開く時刻で、どちらも a.m.（午前）。曜日と時刻をセットで読む。",
                 "どようびは、ごぜん9じからごご5じまで。7じは、げつようびからきんようびにしまるじかんだよ。",
                 ["土曜日は 9:00 a.m. to 5:00 p.m. で、午後5時に閉まる。","午後7時は月曜日から金曜日に閉まる時刻。","8:00 は月曜日から金曜日に開く時刻で、午前（a.m.）。","9:00 は土曜日に開く時刻で、午前（a.m.）。"],
                 ["どようびは5じにしまるね。","7じは、へいじつにしまるじかんだよ。","8じは、へいじつのあさにあくじかんだよ。","9じは、どようびのあさにあくじかんだよ。"]),
        question(27,"Before students use the new computers, they must","生徒たちは新しいコンピューターを使う前に、～しなければなりません。",
                 ["read a book about computers.","take computer lessons.","ask a teacher.","come to the library at 8:00 a.m."],
                 ["コンピューターについての本を読む。","コンピューターの授業を受ける。","先生に尋ねる。","午前8時に図書館に来る。"],3,
                 ["You must ask a teacher before you use them."],
                 "質問の they must（～しなければならない）は、掲示の最後の文 You must ask a teacher before you use them. と対応する。them は前の文の some new computers を指す。本を読むことやコンピューターの授業は書かれていない。8:00 a.m. は月曜日から金曜日に図書館が開く時刻で、来なければならない時刻ではない。",
                 "あたらしいコンピューターをつかうまえに、せんせいにきかないといけないよ。",
                 ["本を読むとは書かれていない。","コンピューターの授業は書かれていない。","You must ask a teacher before you use them. に一致する。","8:00 a.m. は平日に図書館が開く時刻で、来なければならない時刻ではない。"],
                 ["ほんをよむ、とはかいていないよ。","じゅぎょうのはなしはないよ。","せんせいにきくんだね。","8じは、へいじつにとしょかんがあくじかんだよ。"]),
    ],"掲示",26,27),
    passage("4B","New school / Baseball",EMAIL,[
        question(28,"What will Ollie's grandmother do?","オリーの祖母は何をするつもりですか。",
                 ["Watch Ollie's baseball game.","Take Ollie to school.","Buy a train ticket for Ollie.","Go for a walk with Ollie."],
                 ["オリーの野球の試合を見る。","オリーを学校へ連れて行く。","オリーに電車の切符を買う。","オリーと散歩に行く。"],1,
                 ["I'll come and watch your next game."],
                 "1通目は祖母（Grandma）からのメール。I'll come and watch your next game.（次の試合を見に行くね）とあり、your next game はオリーの学校の野球部の試合。2通目でオリーも You can come and watch.（見に来ていいよ）と答えている。学校へ連れて行く話や切符を買う話はない。walked は祖母が若いころに歩いて学校へ通った話。",
                 "おばあちゃんは『つぎのしあいをみにいくね』とかいているよ。オリーも『みにきていいよ』とこたえているね。",
                 ["I'll come and watch your next game. に一致する。","オリーは自転車・電車・徒歩で通学していて、祖母が連れて行く話はない。","電車はオリーの通学手段で、祖母が切符を買う話はない。","walked は祖母が若いころに歩いて通学した話で、散歩の予定ではない。"],
                 ["やきゅうのしあいをみにいくんだね。","がっこうへつれていく、ではないよ。","きっぷをかう、ではないよ。","さんぽのはなしはないよ。"]),
        question(29,"How long is Ollie's train ride to school?","オリーの学校までの電車の乗車時間はどれくらいですか。",
                 ["10 minutes.","15 minutes.","30 minutes.","One hour."],
                 ["10分。","15分。","30分。","1時間。"],3,
                 ["The train ride to school takes 30 minutes."],
                 "質問の train ride to school が2通目と同じ表現。The train ride to school takes 30 minutes. とあり、take は『（時間が）かかる』。10分は駅まで自転車に乗る時間、15分は駅から学校まで歩く時間、1時間は野球の練習時間。数字と、それが何の時間かをセットで読む。",
                 "でんしゃは30ぷん。10ぷんはじてんしゃ、15ふんはあるくじかん、1じかんはやきゅうのれんしゅうだよ。",
                 ["10分は駅まで自転車に乗る時間。","15分は電車を降りてから学校まで歩く時間。","The train ride to school takes 30 minutes. に一致する。","1時間は野球の練習時間。"],
                 ["10ぷんは、じてんしゃのじかんだよ。","15ふんは、あるくじかんだよ。","でんしゃは30ぷんだね。","1じかんは、れんしゅうのじかんだよ。"]),
        question(30,"Ollie will have a baseball game","オリーは～に野球の試合があります。",
                 ["next Wednesday.","next Friday.","next Saturday.","next Sunday."],
                 ["次の水曜日。","次の金曜日。","次の土曜日。","次の日曜日。"],3,
                 ["We'll have a game next Saturday."],
                 "2通目に We'll have a game next Saturday. とあり、祖母の When is it?（試合はいつ？）への答えになっている。水曜日と金曜日は練習の日（We practice for one hour on Wednesdays and Fridays.）。日曜日は本文に出てこない。",
                 "しあいはつぎのどようび。すいようびときんようびは、れんしゅうのひだよ。",
                 ["水曜日は練習の日。","金曜日は練習の日。","We'll have a game next Saturday. に一致する。","日曜日は本文に出てこない。"],
                 ["すいようびは、れんしゅうのひだよ。","きんようびは、れんしゅうのひだよ。","どようびにしあいがあるね。","にちようびは、でてこないよ。"]),
    ],"Eメール",28,30),
    passage("4C","Art Classes",ARTICLE,[
        question(31,"What subject doesn't Jay like?","ジェイが好きではない教科は何ですか。",
                 ["Math.","Science.","Art.","History."],
                 ["数学。","理科。","美術。","歴史。"],4,
                 ["He likes math and science, but he doesn't like history."],
                 "質問は doesn't like（好きではない）。He likes math and science, but he doesn't like history. で、but の前が好きな教科、後ろが好きではない教科。美術は His favorite subject is art.（いちばん好きな教科は美術）とある。",
                 "すうがくとりかはすき。れきしはすきではないよ。びじゅつは、いちばんすきなきょうかだね。",
                 ["数学は好きな教科。","理科は好きな教科。","美術はいちばん好きな教科。","but he doesn't like history に一致する。"],
                 ["すうがくは、すきだよ。","りかは、すきだよ。","びじゅつは、いちばんすきだよ。","れきしは、すきではないね。"]),
        question(32,"When did Jay's class go to an art museum?","ジェイのクラスはいつ美術館へ行きましたか。",
                 ["Last Wednesday.","Last Thursday.","Last Friday.","Last Saturday."],
                 ["この前の水曜日。","この前の木曜日。","この前の金曜日。","この前の土曜日。"],3,
                 ["Last Friday, Jay's class went to an art museum."],
                 "質問の go to an art museum が本文の went to an art museum と対応する。Last Friday（この前の金曜日）にクラスで美術館へ行った。曜日がいくつも出てくるので整理する。Last Wednesday は自画像を描いた日、On Saturday は母が美術学校に電話した日、next Thursday は美術教室が始まる日。",
                 "びじゅつかんにいったのは、このまえのきんようび。すいようびは、じぶんのえをかいたひだよ。",
                 ["水曜日は自画像を描き、先生にほめられた日。","木曜日は美術教室が始まる日（next Thursday）で、これからのこと。","Last Friday, Jay's class went to an art museum. に一致する。","土曜日は母が美術学校に電話した日。"],
                 ["すいようびは、えをかいたひだよ。","もくようびは、きょうしつがはじまるひだよ。","きんようびにいったね。","どようびは、おかあさんがでんわしたひだよ。"]),
        question(33,"Which paintings did Jay like the best?","ジェイはどの絵がいちばん気に入りましたか。",
                 ["The paintings of the sea.","The paintings of rivers.","The paintings of mountains.","The paintings of people."],
                 ["海の絵。","川の絵。","山の絵。","人の絵。"],4,
                 ["There were paintings of the sea and paintings of rivers and mountains, but Jay liked the paintings of people the best."],
                 "質問の the best（いちばん）が本文と対応する。美術館には海の絵や川や山の絵があったが、but の後ろで Jay liked the paintings of people the best.（人の絵がいちばん気に入った）と言っている。",
                 "うみやかわややまのえもあったけど、いちばんすきだったのは、ひとのえだよ。",
                 ["海の絵は美術館にあった絵の一つで、いちばん気に入った絵ではない。","川の絵は美術館にあった絵の一つで、いちばん気に入った絵ではない。","山の絵は美術館にあった絵の一つで、いちばん気に入った絵ではない。","but の後ろで the paintings of people the best と言っている。"],
                 ["うみのえは、あっただけだよ。","かわのえは、あっただけだよ。","やまのえは、あっただけだよ。","ひとのえが、いちばんすきだね。"]),
        question(34,"What did Jay's friend Tony eat for lunch?","ジェイの友だちのトニーは昼食に何を食べましたか。",
                 ["Pasta.","Soup.","A hamburger.","A salad."],
                 ["パスタ。","スープ。","ハンバーガー。","サラダ。"],3,
                 ["His friend Jane ate pasta and soup, and his friend Tony ate a hamburger."],
                 "人物と食べた物をセットで読む。パスタとスープを食べたのはジェーン、ハンバーガーを食べたのはトニー、サラダはジェイ。質問は Tony なので A hamburger.。",
                 "ジェーンはパスタとスープ、トニーはハンバーガー、ジェイはサラダをたべたよ。",
                 ["パスタを食べたのはジェーン。","スープを食べたのもジェーン。","his friend Tony ate a hamburger に一致する。","サラダを食べたのはジェイ。"],
                 ["パスタは、ジェーンだよ。","スープも、ジェーンだよ。","トニーはハンバーガーだね。","サラダは、ジェイだよ。"]),
        question(35,"What did Jay's mother do?","ジェイの母は何をしましたか。",
                 ["She taught Jay how to paint.","She went on a trip.","She called an art school.","She went to see some paintings."],
                 ["ジェイに絵の描き方を教えた。","旅行に行った。","美術学校に電話した。","絵を見に行った。"],3,
                 ["On Saturday, his mother called an art school near their house."],
                 "ジェイが I want to take art classes.（美術教室に通いたい）と言ったあと、On Saturday, his mother called an art school near their house.（土曜日に母が家の近くの美術学校に電話した）とある。絵を見に行ったのは美術館へ行ったジェイのクラスで、母ではない。絵の描き方を教えたことや旅行は書かれていない。",
                 "ジェイが『びじゅつきょうしつにかよいたい』といったので、おかあさんは、いえのちかくのびじゅつがっこうにでんわしたよ。",
                 ["絵の描き方を教えたとは書かれていない。","旅行に行ったとは書かれていない。","his mother called an art school に一致する。","絵を見に行ったのはジェイのクラスで、母ではない。"],
                 ["えのかきかたをおしえた、ではないよ。","りょこうのはなしはないよ。","でんわをしたんだね。","えをみにいったのは、ジェイのクラスだよ。"]),
    ],"英文",31,35),
]

PASSAGES[0]["format"]="notice"
PASSAGES[1]["format"]="multi-email"
PASSAGES[1]["emails"]=[]
for i in (0,2):
    meta={line.partition(":")[0].lower():line.partition(":")[2].strip() for line in PASSAGES[1]["paragraphs"][i].splitlines()}
    PASSAGES[1]["emails"].append(dict(meta=meta,body=PASSAGES[1]["paragraphs"][i+1],translation=PASSAGES[1]["translations"][i+1]))

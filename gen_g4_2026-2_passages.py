"""Booklet pp. 6-11 (2026-2 main venue): verb-aware, fully aligned bilingual reading units."""


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


NOTICE=[
    [plain("Information from the School Nurse","保健の先生からのお知らせ")],
    [row([("Our new school nurse, Ms. Brown,","新しい保健の先生のブラウン先生が"),("came to this high school","この高校に来ました、"),("last week!","先週。")],"came"),
     row([("She introduced herself","彼女は自己紹介をしました、"),("to everyone yesterday.","昨日みんなに。")],"introduced")],
    [row([("Next Monday,","次の月曜日、"),("she will talk about healthy meals for students","彼女は生徒のための健康的な食事について話します、"),("after school.","放課後に。")],"will")],
    [plain("Time: From 3:30 p.m. to 4:30 p.m.","時間：午後3時30分から午後4時30分まで"),
     plain("Place: The meeting room (next to the art room)","場所：会議室（美術室の隣）")],
    [row([("Please come and see","会いに来てください、"),("Ms. Brown!","ブラウン先生に。")],"come")],
]

EMAIL=[
    [plain("From: Tom Jackson","差出人：トム・ジャクソン"),plain("To: David Jackson","宛先：デイビッド・ジャクソン"),
     plain("Date: May 17","日付：5月17日"),plain("Subject: Are there any interesting places?","件名：おもしろい場所はある？")],
    [plain("Hi Grandpa,","おじいちゃんへ、"),
     row([("How","どんなふうに"),("are you?","過ごしているかな。")],"are"),
     row([("Next Tuesday is","次の火曜日は"),("a school holiday.","学校が休みなんだ。")],"is"),
     row([("I want to go somewhere","ぼくはどこかへ出かけたいんだ、"),("with my friends.","友だちと。")],"want"),
     row([("However,","でも、"),("I cannot find any interesting places","おもしろい場所が見つからないんだ、"),("in my town.","ぼくの町では。")],"cannot"),
     row([("We usually go to the park,","ぼくたちはふだん公園に行くよ、"),("but we want to visit a different place.","でも別の場所に行ってみたいんだ。")],"go"),
     row([("There is a good zoo","いい動物園があるよね、"),("in your town, right?","おじいちゃんの町には。")],"is"),
     plain("Write soon,","お返事待ってるね、"),plain("Tom","トム")],
    [plain("From: David Jackson","差出人：デイビッド・ジャクソン"),plain("To: Tom Jackson","宛先：トム・ジャクソン"),
     plain("Date: May 17","日付：5月17日"),plain("Subject: Yes!","件名：あるよ！")],
    [plain("Hi Tom,","トムへ、"),
     row([("I am","私は"),("fine!","元気だよ。")],"am"),
     row([("Yes,","うん、"),("my town has a zoo.","私の町には動物園があるよ。")],"has"),
     row([("There is","あるよ、"),("a baseball stadium, too.","野球場も。")],"is"),
     row([("But they are both closed","でも、どちらも休みなんだ、"),("on Tuesdays.","火曜日は。")],"are"),
     row([("How about","どうかな、"),("the new museum?","新しい博物館は。")]),
     row([("I visited there","私はそこへ行ってきたよ、"),("yesterday!","昨日。")],"visited"),
     row([("After visiting the museum,","博物館に行った後は、"),("bring your friends","友だちを連れておいで、"),("to my house!","私の家に。")],"bring"),
     row([("Your grandma sometimes makes","おばあちゃんはときどき作るよ、"),("chocolate cookies or a cheesecake,","チョコレートクッキーやチーズケーキを。"),("but she will make an apple pie","でも、アップルパイを作るんだ、"),("next Tuesday.","次の火曜日は。")],"makes"),
     row([("Let's try it","食べてみよう、"),("together!","一緒に。")],"try"),
     plain("Keep in touch,","また連絡してね、"),plain("Grandpa","おじいちゃん")],
]

ARTICLE=[
    [row([("Kelly is","ケリーは"),("a high school student.","高校生です。")],"is"),
     row([("Her mother is an art teacher,","彼女の母親は美術の先生で、"),("and her father is a painter.","父親は画家です。")],"is"),
     row([("Kelly's sister also studies art at a college,","ケリーの姉（妹）も大学で美術を勉強していますが、"),("but Kelly does not like","ケリーは好きではありません、"),("drawing pictures or making things.","絵を描くことも物を作ることも。")],"studies")],
    [row([("One day,","ある日、"),("Kelly's mother took Kelly to a museum","ケリーの母親はケリーを美術館へ連れて行きました、"),("by train.","電車で。")],"took"),
     row([("There were many paintings","たくさんの絵がありました、"),("of birds and flowers.","鳥や花の。")],"were"),
     row([("Then,","それから、"),("Kelly found a photo","ケリーは1枚の写真を見つけました、"),("in a corner.","すみのほうで。")],"found"),
     row([("She saw an interesting cloud","彼女はおもしろい雲を見ました、"),("in the photo.","その写真の中に。")],"saw"),
     row([("She was surprised","彼女は驚きました、"),("because the cloud looked like a plane in the sky.","その雲が空を飛ぶ飛行機のように見えたからです。")],"was"),
     row([("\"This is an interesting kind of art,\"","「これはおもしろい種類の芸術だな」と"),("she thought.","彼女は思いました。")],"thought"),
     row([("Kelly's mother said,","ケリーの母親は言いました、"),("\"You should try taking photos.\"","「写真を撮ってみるといいよ」と。")],"said"),
     row([("Kelly said,","ケリーは言いました、"),("\"Good idea! I'll try it.\"","「いい考えだね！やってみる」と。")],"said")],
    [row([("The next day,","次の日、"),("Kelly joined her school's photo club.","ケリーは学校の写真部に入りました。")],"joined"),
     row([("After joining the club,","部に入った後、"),("she went to a mountain","彼女は山へ行きました、"),("with the other members of her club.","部のほかのメンバーと。")],"went"),
     row([("She also visited a village and a festival","彼女は村やお祭りにも行きました、"),("alone.","一人で。")],"visited"),
     row([("Kelly took many photos,","ケリーはたくさんの写真を撮りましたが、"),("but her favorite is","彼女のお気に入りは"),("a photo of an old house.","古い家の写真です。")],"took"),
     row([("Now,","今、"),("she enjoys her new hobby.","彼女は新しい趣味を楽しんでいます。")],"enjoys")],
]

# Full translations read naturally; bilingual slash units retain English order.
for block,translations in zip(NOTICE,[
    ["保健の先生からのお知らせ"],
    ["新しい保健の先生のブラウン先生が、先週この高校に来ました。","昨日、みんなに自己紹介をしました。"],
    ["次の月曜日の放課後、生徒のための健康的な食事について話をします。"],
    ["時間：午後3時30分から午後4時30分まで","場所：会議室（美術室の隣）"],
    ["ぜひブラウン先生に会いに来てください。"],
]):
    for r,ja in zip(block,translations): r[1]=ja
for block,translations in [(EMAIL[1],[
    "おじいちゃんへ、","元気？","次の火曜日は学校が休みなんだ。","友だちとどこかへ出かけたいと思っているよ。",
    "でも、ぼくの町にはおもしろい場所が見つからないんだ。","ふだんは公園に行くけど、別の場所に行ってみたいんだ。",
    "おじいちゃんの町には、いい動物園があるよね？","お返事待ってるね、","トム"]),
    (EMAIL[3],["トムへ、","元気だよ。","うん、私の町には動物園があるよ。","野球場もあるよ。","でも、どちらも火曜日は休みなんだ。",
               "新しい博物館はどうかな？","昨日、そこへ行ってきたんだ。","博物館に行った後は、友だちを家に連れておいで。",
               "おばあちゃんはときどきチョコレートクッキーやチーズケーキを作るけれど、次の火曜日はアップルパイを作るよ。",
               "みんなで一緒に食べようね。","また連絡してね、","おじいちゃん"]),
    (ARTICLE[0],["ケリーは高校生です。","母親は美術の先生で、父親は画家です。",
                 "ケリーの姉（妹）も大学で美術を学んでいますが、ケリーは絵を描くことも物を作ることも好きではありません。"]),
    (ARTICLE[1],["ある日、ケリーの母親はケリーを電車で美術館へ連れて行きました。","鳥や花を描いた絵がたくさんありました。",
                 "それから、ケリーはすみのほうに1枚の写真を見つけました。","その写真には、おもしろい雲が写っていました。",
                 "その雲が空を飛ぶ飛行機のように見えたので、ケリーは驚きました。","「これはおもしろい種類の芸術だな」とケリーは思いました。",
                 "ケリーの母親は「写真を撮ってみるといいよ」と言いました。","ケリーは「いい考えだね！やってみる」と言いました。"]),
    (ARTICLE[2],["次の日、ケリーは学校の写真部に入りました。","入部した後、ケリーは部のほかのメンバーと山へ行きました。",
                 "また、一人で村やお祭りにも出かけました。","ケリーはたくさんの写真を撮りましたが、いちばんのお気に入りは古い家の写真です。",
                 "今、ケリーは新しい趣味を楽しんでいます。"]),
]:
    for r,ja in zip(block,translations): r[1]=ja


def instruction(kind, start, end):
    nums=f"({start})と({end})" if end-start==1 else f"({start})から({end})まで"
    return f"次の{kind}の内容に関して，{nums}の質問に対する答えとして最も適切なもの，または文を完成させるのに最も適切なものを1，2，3，4の中から一つ選び，その番号のマーク欄をぬりつぶしなさい。"


def passage(label, title, blocks, questions, kind, start, end):
    # A notice block made only of "Time:" / "Place:" label rows keeps one label per line.
    paragraphs=[("\n" if label=="4A" and (i==0 or all(r[0].startswith(("Time:","Place:")) for r in block)) or label=="4B" and i%2==0 else " ").join(r[0] for r in block) for i,block in enumerate(blocks)]
    if label=="4B":
        for i in (1,3):
            b=blocks[i]
            paragraphs[i]=b[0][0]+"\n"+" ".join(r[0] for r in b[1:-2])+"\n"+b[-2][0]+"\n"+b[-1][0]
    return dict(label=label,title=title,instruction=instruction(kind,start,end),paragraphs=paragraphs,
                translations=["\n".join(r[1] for r in b) for b in blocks],
                sentencePairs=[r for b in blocks for r in b], questions=questions)


PASSAGES=[
    passage("4A","Information from the School Nurse",NOTICE,[
        question(26,"What did Ms. Brown do yesterday?","ブラウン先生は昨日何をしましたか。",
                 ["She talked about healthy meals.","She introduced herself to everyone.","She had an important meeting.","She had lunch with students."],
                 ["健康的な食事について話した。","みんなに自己紹介をした。","大切な会議があった。","生徒たちと昼食を食べた。"],2,
                 ["She introduced herself to everyone yesterday."],
                 "yesterday と Next Monday の時を区別する。昨日したのは自己紹介。健康的な食事の話は次の月曜日の放課後の予定で、昨日のことではない。",
                 "きのうは、みんなにじこしょうかいをしたよ。たべもののおはなしは、つぎのげつようびだね。",
                 ["健康的な食事の話は次の月曜日の予定。","yesterday の文の内容に一致する。","大切な会議があったとは書かれていない。","生徒と昼食を食べたとは書かれていない。"],
                 ["つぎのげつようびのことだよ。","きのう、じこしょうかいしたね。","かいぎのおはなしはないよ。","ひるごはんのおはなしはないよ。"]),
        question(27,"Where should students go to see Ms. Brown next Monday at 3:30 p.m.?","次の月曜日の午後3時30分にブラウン先生に会うには、生徒はどこへ行けばよいですか。",
                 ["To the teachers' room.","To the meeting room.","To the school gym.","To the art room."],
                 ["職員室へ。","会議室へ。","学校の体育館へ。","美術室へ。"],2,
                 ["Time: From 3:30 p.m. to 4:30 p.m.","Place: The meeting room (next to the art room)"],
                 "Time で午後3時30分が話の始まる時間だと確かめ、Place で場所を読む。会場は会議室。美術室はかっこの中で会議室の位置を説明する目印にすぎない。",
                 "ばしょは、かいぎしつだよ。びじゅつしつは、かいぎしつのとなりにあるへや。まちがえないでね。",
                 ["職員室は本文に出てこない場所。","Place に書かれた会場に一致する。","体育館は本文に出てこない場所。","美術室は会議室の隣にある目印で、会場ではない。"],
                 ["しょくいんしつは、でてこないよ。","かいぎしつにいくんだね。","たいいくかんは、でてこないよ。","びじゅつしつは、となりのへやだよ。"]),
    ],"掲示",26,27),
    passage("4B","Are there any interesting places? / Yes!",EMAIL,[
        question(28,"Where does Tom usually go in his town?","トムはふだん自分の町でどこへ行きますか。",
                 ["To the zoo.","To the park.","To the stadium.","To the museum."],
                 ["動物園へ。","公園へ。","スタジアムへ。","博物館へ。"],2,
                 ["We usually go to the park, but we want to visit a different place."],
                 "1通目の Tom の文で usually を探す。ふだん行くのは公園。動物園は祖父の町にある場所で、野球場と博物館は2通目で祖父が挙げた場所。",
                 "トムは、いつもこうえんにいくよ。どうぶつえんは、おじいちゃんのまちにあるばしょだね。",
                 ["動物園は祖父の町にあり、トムの町の話ではない。","usually go to the park に一致する。","スタジアム（野球場）は祖父の町にある場所。","博物館は祖父が2通目ですすめた場所。"],
                 ["おじいちゃんのまちにあるよ。","いつもこうえんにいくね。","おじいちゃんのまちにあるよ。","おじいちゃんがすすめたばしょだよ。"]),
        question(29,"What did Tom's grandfather do yesterday?","トムの祖父は昨日何をしましたか。",
                 ["He walked around the zoo.","He visited his friend's house.","He watched a baseball game.","He visited the museum."],
                 ["動物園を歩いて回った。","友人の家を訪れた。","野球の試合を見た。","博物館を訪れた。"],4,
                 ["How about the new museum?","I visited there yesterday!"],
                 "2通目の I visited there yesterday! の there は直前の the new museum を指す。動物園と野球場は火曜日が休みだと書かれているだけで、昨日行ったとはない。",
                 "there（そこ）は、まえのぶんのあたらしいはくぶつかんのこと。きのう、はくぶつかんにいったんだね。",
                 ["動物園は火曜日が休みと書かれているだけ。","友人の家を訪れたとは書かれていない。","野球場の話はあるが、試合を見たとはない。","there が the new museum を指している。"],
                 ["どうぶつえんにいったとはないよ。","ともだちのいえではないよ。","やきゅうをみたとはないよ。","はくぶつかんにいったね。"]),
        question(30,"Next Tuesday, Tom's grandmother will make","次の火曜日、トムの祖母は～を作ります。",
                 ["an apple pie.","a cheesecake.","a pumpkin pie.","some chocolate cookies."],
                 ["アップルパイ。","チーズケーキ。","パンプキンパイ。","チョコレートクッキー。"],1,
                 ["Your grandma sometimes makes chocolate cookies or a cheesecake, but she will make an apple pie next Tuesday."],
                 "Your grandma はトムの祖母のこと。but の前の sometimes makes はときどき作るもの、後ろの will make ... next Tuesday が次の火曜日の予定。",
                 "おばあちゃんは、ときどきクッキーやチーズケーキをつくるよ。つぎのかようびは、アップルパイだね。",
                 ["will make の後ろにある次の火曜日の予定。","ときどき作るもので、火曜日の予定ではない。","パンプキンパイは本文に出てこない。","ときどき作るもので、火曜日の予定ではない。"],
                 ["かようびはアップルパイだね。","ときどきつくるものだよ。","パンプキンパイはでてこないよ。","ときどきつくるものだよ。"]),
    ],"Eメール",28,30),
    passage("4C","Kelly's New Hobby",ARTICLE,[
        question(31,"What does Kelly's sister do?","ケリーの姉（妹）は何をしていますか。",
                 ["She teaches art at a school.","She works at a museum.","She studies art at a college.","She works as a painter."],
                 ["学校で美術を教えている。","美術館で働いている。","大学で美術を学んでいる。","画家として働いている。"],3,
                 ["Kelly's sister also studies art at a college, but Kelly does not like drawing pictures or making things."],
                 "家族ごとの説明を整理する。美術の先生は母、画家は父、大学で美術を学んでいるのが姉（妹）。also は姉（妹）も美術に関わっていることを示す。",
                 "おかあさんはびじゅつのせんせい、おとうさんはえかき。ケリーのきょうだいは、だいがくでびじゅつをまなんでいるよ。",
                 ["美術を教えているのは母で、姉（妹）ではない。","美術館で働く家族は書かれていない。","studies art at a college に一致する。","画家として働いているのは父で、姉（妹）ではない。"],
                 ["おしえているのは、おかあさんだよ。","びじゅつかんではたらくひとはいないよ。","だいがくでまなんでいるね。","えかきは、おとうさんだよ。"]),
        question(32,"Why was Kelly surprised when she looked at the cloud in the photo?","写真の雲を見たとき、ケリーはなぜ驚いたのですか。",
                 ["The cloud looked like a plane.","The cloud looked like a bird.","The cloud looked like a flower.","The cloud looked like a train."],
                 ["雲が飛行機のように見えた。","雲が鳥のように見えた。","雲が花のように見えた。","雲が電車のように見えた。"],1,
                 ["She was surprised because the cloud looked like a plane in the sky."],
                 "because の後ろに驚いた理由がある。look like ～は「～のように見える」。鳥と花は美術館の絵の題材で、電車は美術館へ行くときの交通手段。",
                 "because のあとに、りゆうがあるよ。くもが、そらをとぶひこうきみたいにみえたんだね。",
                 ["because の後ろにある理由に一致する。","鳥は美術館の絵の題材で、雲の形ではない。","花は美術館の絵の題材で、雲の形ではない。","電車は美術館へ行くときに使ったもの。"],
                 ["ひこうきみたいなくもだね。","とりは、えのなかのものだよ。","はなは、えのなかのものだよ。","でんしゃは、のってきたものだよ。"]),
        question(33,"What did Kelly's mother say to Kelly?","ケリーの母親はケリーに何と言いましたか。",
                 ["Kelly should learn painting.","Kelly should join the art club.","Kelly should try taking photos.","Kelly should visit many museums."],
                 ["ケリーは絵を習ったほうがよい。","ケリーは美術部に入ったほうがよい。","ケリーは写真を撮ってみたほうがよい。","ケリーはたくさんの美術館を訪れたほうがよい。"],3,
                 ["Kelly's mother said, \"You should try taking photos.\""],
                 "引用符の中の You should ～ が母親の助言。try taking photos は「写真を撮ってみる」。ケリーが次の日に入ったのは美術部ではなく写真部。",
                 "おかあさんは「しゃしんをとってみたら」といったよ。ケリーがはいったのは、しゃしんぶだね。",
                 ["絵を習うようにとは言っていない。","入ったのは写真部で、美術部ではない。","母親の助言 try taking photos に一致する。","多くの美術館に行くようにとは言っていない。"],
                 ["えをならう、ではないよ。","はいったのは、しゃしんぶだよ。","しゃしんをとってみて、だね。","びじゅつかんめぐりではないよ。"]),
        question(34,"Where did Kelly go with the other members of her club?","ケリーは部のほかのメンバーとどこへ行きましたか。",
                 ["A village.","A lake.","A festival.","A mountain."],
                 ["村。","湖。","お祭り。","山。"],4,
                 ["After joining the club, she went to a mountain with the other members of her club.","She also visited a village and a festival alone."],
                 "with the other members of her club と alone を対比する。部のメンバーと行ったのは山。村とお祭りは一人で訪れた場所。湖は本文に出てこない。",
                 "ぶのなかまといったのは、やまだよ。むらとおまつりは、ひとりででかけたところだね。",
                 ["村は alone とあり、一人で訪れた場所。","湖は本文のどこにも出てこない場所。","お祭りは alone とあり、一人で訪れた場所。","部のメンバーと行った場所に一致する。"],
                 ["むらは、ひとりでいったよ。","みずうみは、でてこないよ。","おまつりは、ひとりでいったよ。","なかまと、やまにいったね。"]),
        question(35,"What is Kelly's favorite photo?","ケリーのお気に入りの写真は何ですか。",
                 ["The photo of an old house.","The photo of the sky.","The photo of the mountain.","The photo of her teacher."],
                 ["古い家の写真。","空の写真。","山の写真。","彼女の先生の写真。"],1,
                 ["Kelly took many photos, but her favorite is a photo of an old house."],
                 "her favorite is の後ろにお気に入りの写真がある。空の雲の写真は美術館で見たもの、山は部のメンバーと行った場所で、お気に入りとは書かれていない。",
                 "ケリーのいちばんすきなしゃしんは、ふるいいえのしゃしんだよ。そらは、びじゅつかんでみたしゃしんだね。",
                 ["her favorite is の後ろの内容に一致する。","空の写真は美術館で見たもので、お気に入りではない。","山には行ったが、お気に入りとは書かれていない。","先生の写真は本文に出てこない。"],
                 ["ふるいいえのしゃしんだね。","そらは、びじゅつかんでみたしゃしんだよ。","やまのしゃしんがすき、とはないよ。","せんせいのしゃしんはないよ。"]),
    ],"英文",31,35),
]

PASSAGES[0]["format"]="notice"
PASSAGES[1]["format"]="multi-email"
PASSAGES[1]["emails"]=[]
for i in (0,2):
    meta={line.partition(":")[0].lower():line.partition(":")[2].strip() for line in PASSAGES[1]["paragraphs"][i].splitlines()}
    PASSAGES[1]["emails"].append(dict(meta=meta,body=PASSAGES[1]["paragraphs"][i+1],translation=PASSAGES[1]["translations"][i+1]))

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


# The notice keeps the booklet's four visual blocks: title, headline, description, contact lines.
NOTICE=[
    [plain("Lost Pet","迷子のペット")],
    [plain("Please Help Us!","助けてください！")],
    [row([("My family is looking for","私の家族は探しています、"),("our dog Kuro.","うちの犬のクロを。")],"is"),
     row([("She","クロは"),("is about 60 cm long.","約60センチの長さです。")],"is"),
     row([("Her body","クロの体は"),("is black and white.","黒と白です。")],"is"),
     row([("Her legs","足は"),("are brown.","茶色です。")],"are"),
     row([("She has some gray circles","クロには灰色の丸い模様がいくつかあります、"),("on her back.","背中に。")],"has"),
     row([("We lost her","私たちはクロを見失いました、"),("at Sunshine Park","サンシャイン公園で、"),("on Wednesday afternoon.","水曜日の午後に。")],"lost")],
    [row([("Please call me","私に電話してください、"),("if you find her.","もしクロを見つけたら。")],"call"),
     plain("Phone number: 111-1234","電話番号：111-1234"),
     plain("Shige Ueda","シゲ・ウエダ")],
]

EMAIL=[
    [plain("From: Madeleine King","差出人：マデリン・キング"),plain("To: Ruby Garcia","宛先：ルビー・ガルシア"),
     plain("Date: July 5","日付：7月5日"),plain("Subject: Plans","件名：予定")],
    [plain("Hey Ruby,","ルビーへ、"),
     row([("Thanks for seeing a movie","映画を見てくれてありがとう、"),("with me last weekend!","先週末、私と一緒に。")]),
     row([("It","その映画は"),("was so funny!","とてもおもしろかったです。")],"was"),
     row([("My grandmother will come","私の祖母が来ます、"),("to our town","私たちの町へ。"),("and stay with my family","そして私の家族のところに泊まります、"),("next week.","来週。")],"will"),
     row([("Next Friday,","次の金曜日、"),("she will take me","祖母は私を連れて行ってくれます、"),("to an amusement park","遊園地へ、"),("near the lake.","湖の近くの。")],"will"),
     row([("We have more tickets,","私たちはチケットをもっと持っています、"),("and I want to go","そして私は行きたいです、"),("with you.","あなたと一緒に。")],"have"),
     row([("Can you","あなたは～できますか、"),("come?","来ることが。")],"come"),
     plain("Your friend,","あなたの友人、"),plain("Madeleine","マデリン")],
    [plain("From: Ruby Garcia","差出人：ルビー・ガルシア"),plain("To: Madeleine King","宛先：マデリン・キング"),
     plain("Date: July 6","日付：7月6日"),plain("Subject: Thank you","件名：ありがとう")],
    [plain("Hi Madeleine,","マデリンへ、"),
     row([("I can go with you","私はあなたと一緒に行けます、"),("on Friday,","金曜日に。"),("but I have to be home","でも家にいなければなりません、"),("before 6 p.m.","午後6時より前に。")],"go"),
     row([("My sister will come home","姉（妹）が帰ってきます、"),("from college,","大学から。"),("and my mom will cook a special dinner","そして母が特別な夕食を作ります、"),("for our family.","家族のために。")],"will"),
     row([("Should I bring anything,","私は何か持って行ったほうがいいですか、"),("like a water bottle?","水筒のような物を。")],"bring"),
     row([("I will also buy some snacks,","私はお菓子も買います、"),("and we can share them.","そして私たちはそれを分け合えます。")],"will"),
     plain("Thank you,","ありがとう、"),plain("Ruby","ルビー")],
]

ARTICLE=[
    [row([("Mindy is 25 years old,","ミンディは25歳で、"),("and she works","彼女は働いています、"),("at a company.","会社で。")],"is"),
     row([("In college,","大学時代、"),("she played basketball","彼女はバスケットボールをしていました、"),("with her friends,","友だちと。"),("but she doesn't play basketball","でも彼女はバスケットボールをしていません、"),("now.","今は。")],"played"),
     row([("At work,","職場では、"),("she sits at her desk","彼女は机に向かって座り、"),("and uses a computer.","コンピューターを使います。")],"sits")],
    [row([("One day,","ある日、"),("Mindy had lunch","ミンディは昼食を食べました、"),("with her brother.","兄（弟）と。")],"had"),
     row([("She told him,","彼女は兄（弟）に言いました、"),("\"I want to play some sports.\"","「何かスポーツがしたい」と。")],"told"),
     row([("He said,","兄（弟）は言いました、"),("\"You should try tennis.","「テニスをやってみたらいいよ。"),("Do you want to go","行きたい？"),("to a tennis lesson","テニスのレッスンに、"),("with me on Monday?\"","月曜日に僕と一緒に」と。")],"said"),
     row([("Mindy tried tennis,","ミンディはテニスをやってみましたが、"),("but she didn't like it.","好きになれませんでした。")],"tried")],
    [row([("That weekend,","その週末、"),("Mindy saw an article","ミンディは記事を見ました、"),("in the newspaper","新聞で、"),("about free soccer lessons.","無料のサッカーレッスンについての。")],"saw"),
     row([("It said,","その記事には書いてありました、"),("\"We practice","「私たちは練習しています、"),("every Sunday, Tuesday, and Thursday evening","毎週日曜日・火曜日・木曜日の夕方、"),("at six","6時に、"),("in Graystone Park.\"","グレーストーン公園で」と。")],"said"),
     row([("Mindy went to the park","ミンディはその公園へ行き、"),("on Thursday","木曜日に、"),("and met the soccer coach","サッカーのコーチに会いました、"),("for the first time.","初めて。")],"went")],
    [row([("Mindy had a good time,","ミンディは楽しい時間を過ごし、"),("and she made some new friends","新しい友だちが何人かできました、"),("there.","そこで。")],"had"),
     row([("Now,","今、"),("she goes to soccer lessons","彼女はサッカーのレッスンに通っています、"),("after work","仕事の後に、"),("every week.","毎週。")],"goes"),
     row([("She walks to Graystone Park","彼女はグレーストーン公園まで歩いて行きます、"),("because it is near her office.","公園が職場の近くにあるからです。")],"walks")],
]

# Full translations read naturally; bilingual slash units retain English order.
for block,translations in [(NOTICE[2],["私の家族は、うちの犬のクロを探しています。","クロは体長が約60センチです。","体は黒と白です。","足は茶色です。",
                                       "背中に灰色の丸い模様がいくつかあります。","水曜日の午後、サンシャイン公園でクロとはぐれてしまいました。"]),
    (NOTICE[3],["クロを見つけたら、私に電話してください。","電話番号：111-1234","シゲ・ウエダ"]),
    (EMAIL[1],["ルビーへ、","先週末は一緒に映画を見てくれてありがとう！","とてもおもしろかったね！","来週、祖母が私たちの町に来て、私の家に泊まります。",
               "次の金曜日、祖母が湖の近くの遊園地に連れて行ってくれます。","チケットがまだあるので、あなたと一緒に行きたいです。","来られますか。",
               "あなたの友人、","マデリン"]),
    (EMAIL[3],["マデリンへ、","金曜日は一緒に行けるけど、午後6時より前には家に帰っていないといけません。",
               "姉（妹）が大学から帰ってきて、母が家族のために特別な夕食を作るんです。","水筒のような物を何か持って行ったほうがいいですか。",
               "私もお菓子を買っていくので、一緒に分けて食べましょう。","ありがとう、","ルビー"]),
    (ARTICLE[0],["ミンディは25歳で、会社で働いています。","大学時代は友だちとバスケットボールをしていましたが、今はしていません。",
                 "職場では、机に向かってコンピューターを使っています。"]),
    (ARTICLE[1],["ある日、ミンディは兄（弟）と昼食を食べました。","ミンディは兄（弟）に「何かスポーツがしたいな」と言いました。",
                 "兄（弟）は「テニスをやってみたらいいよ。月曜日に僕と一緒にテニスのレッスンに行かない？」と言いました。",
                 "ミンディはテニスをやってみましたが、好きになれませんでした。"]),
    (ARTICLE[2],["その週末、ミンディは新聞で、無料のサッカーレッスンについての記事を見ました。",
                 "記事には「毎週日曜日・火曜日・木曜日の夕方6時に、グレーストーン公園で練習しています」と書いてありました。",
                 "ミンディは木曜日にその公園へ行き、初めてサッカーのコーチに会いました。"]),
    (ARTICLE[3],["ミンディは楽しく過ごし、そこで新しい友だちが何人かできました。","今では、毎週仕事の後にサッカーのレッスンに通っています。",
                 "公園が職場の近くにあるので、ミンディはグレーストーン公園まで歩いて行きます。"]),
]:
    for r,ja in zip(block,translations): r[1]=ja


def instruction(kind, start, end):
    nums=f"({start})と({end})" if end-start==1 else f"({start})から({end})まで"
    return f"次の{kind}の内容に関して，{nums}の質問に対する答えとして最も適切なもの，または文を完成させるのに最も適切なものを1，2，3，4の中から一つ選び，その番号のマーク欄をぬりつぶしなさい。"


def email_body(block):
    return block[0][0]+"\n"+" ".join(r[0] for r in block[1:-2])+"\n"+block[-2][0]+"\n"+block[-1][0]


def passage(label, title, blocks, questions, kind, start, end):
    if label=="4A":
        # The contact block keeps its three printed lines.
        paragraphs=[("\n" if i==3 else " ").join(r[0] for r in block) for i,block in enumerate(blocks)]
    elif label=="4B":
        paragraphs=["\n".join(r[0] for r in block) if i%2==0 else email_body(block) for i,block in enumerate(blocks)]
    else:
        paragraphs=[" ".join(r[0] for r in block) for block in blocks]
    return dict(label=label,title=title,instruction=instruction(kind,start,end),paragraphs=paragraphs,
                translations=["\n".join(r[1] for r in b) for b in blocks],
                sentencePairs=[r for b in blocks for r in b], questions=questions)


PASSAGES=[
    passage("4A","Lost Pet",NOTICE,[
        question(26,"Shige wants to find","シゲは～を見つけたいと思っています。",
                 ["his family's pet dog.","a park near the beach.","a long, black coat.","his old cell phone."],
                 ["家族のペットの犬。","海辺の近くの公園。","長い黒のコート。","彼の古い携帯電話。"],1,["My family is looking for our dog Kuro."],
                 "look for は『～を探す』。最初の文の our dog Kuro（うちの犬のクロ）が、選択肢では his family's pet dog（家族のペットの犬）と言いかえられている。掲示の最後に名前がある Shige Ueda が書いた人なので、My family はシゲの家族。long や black は犬の体の説明に出てくる語で、コートの話ではない。",
                 "けいじのさいしょに、かぞくでいぬのクロをさがしている、とあるよ。look for は『さがす』だね。",
                 ["our dog Kuro を家族のペットの犬と言いかえている。","公園はクロとはぐれた場所で、海辺の公園を探しているとは書かれていない。","long や black は犬の体の説明で、コートの話ではない。","携帯電話は掲示に出てこない。"],
                 ["いぬのクロをさがしているね。","こうえんは、クロがいなくなったばしょだよ。","ながい、くろい、はいぬのせつめいだよ。","けいたいでんわは、でてこないよ。"]),
        question(27,"What color are Kuro's legs?","クロの足は何色ですか。",
                 ["Black.","White.","Brown.","Gray."],
                 ["黒。","白。","茶色。","灰色。"],3,["Her legs are brown."],
                 "体（body）・足（legs）・背中（back）で色が違う。体は black and white（黒と白）、足は brown（茶色）、背中には gray circles（灰色の丸い模様）がある。体のどの部分の色かを確かめる。",
                 "からだはくろとしろ、あしはちゃいろ、せなかにははいいろのまる。あしはちゃいろだね。",
                 ["黒は体の色。","白も体の色。","Her legs are brown. に一致する。","灰色は背中の丸い模様の色。"],
                 ["くろは、からだのいろだよ。","しろも、からだのいろだよ。","あしはちゃいろだね。","はいいろは、せなかのもようだよ。"]),
    ],"掲示",26,27),
    passage("4B","Plans / Thank you",EMAIL,[
        question(28,"Where does Madeleine want to go with Ruby?","マデリンはルビーとどこへ行きたいのですか。",
                 ["To a famous college.","To an amusement park.","To a movie theater.","To the beach."],
                 ["有名な大学へ。","遊園地へ。","映画館へ。","海辺へ。"],2,
                 ["Next Friday, she will take me to an amusement park near the lake.","We have more tickets, and I want to go with you."],
                 "1通目で、祖母が次の金曜日に湖の近くの amusement park（遊園地）へ連れて行ってくれると書き、チケットがまだあるので I want to go with you（あなたと一緒に行きたい）と誘っている。映画は先週末にもう一緒に見たこと。college は2通目に出てくる、ルビーの姉（妹）が帰ってくる所。",
                 "マデリンは、きんようびにゆうえんちへいくよ。チケットがあるから、ルビーといっしょにいきたいんだね。",
                 ["college はルビーの姉（妹）が帰ってくる所で、行き先ではない。","祖母と行く遊園地に、ルビーを誘っている。","映画は先週末に一緒に見たこと。","海辺は出てこない。行き先は湖の近くの遊園地。"],
                 ["だいがくへいくのではないよ。","ゆうえんちだね。","えいがは、せんしゅうまつにみたよ。","うみは、でてこないよ。"]),
        question(29,"Why does Ruby have to come home before 6 p.m.?","ルビーはなぜ午後6時より前に帰宅しなければならないのですか。",
                 ["Her sister will come home.","Her sister will take her shopping.","Her family will leave for vacation.","Her family will watch a movie."],
                 ["姉（妹）が帰ってくるから。","姉（妹）が買い物に連れて行ってくれるから。","家族が休暇に出かけるから。","家族が映画を見るから。"],1,
                 ["My sister will come home from college"],
                 "2通目の I have to be home before 6 p.m.（午後6時より前に家にいなければならない）の理由は、次の文に書かれている。My sister will come home from college（姉（妹）が大学から帰ってくる）、そして母が家族のために特別な夕食を作る。",
                 "おねえさん（いもうと）がだいがくからかえってくるから、6じまえにかえるんだね。",
                 ["姉（妹）が大学から帰ってくることが理由。","姉（妹）が買い物に連れて行くとは書かれていない。","休暇に出かけるとは書かれていない。","映画は先週末にマデリンと見たもので、家族の予定ではない。"],
                 ["おねえさん（いもうと）がかえってくるからだね。","かいものは、でてこないよ。","りょこうは、でてこないよ。","えいがは、まえにマデリンとみたよ。"]),
        question(30,"What will Ruby buy?","ルビーは何を買うつもりですか。",
                 ["A gift for her mother.","Books for college.","A new swimsuit.","Some snacks."],
                 ["母への贈り物。","大学用の本。","新しい水着。","お菓子。"],4,["I will also buy some snacks"],
                 "2通目の最後に I will also buy some snacks（私もお菓子を買う）とある。その前の文では、水筒など何か持って行くべきかを尋ねている。母は特別な夕食を作る人で、贈り物を買うとは書かれていない。",
                 "ルビーは、おかしをかっていっしょにたべようといっているよ。snack は『おかし』だね。",
                 ["母は夕食を作る人で、贈り物を買うとは書かれていない。","college は姉（妹）が帰ってくる所で、本を買う話はない。","水着を買う話はない。","buy some snacks に一致する。"],
                 ["おかあさんへのプレゼントは、でてこないよ。","ほんをかう、とはかいていないよ。","みずぎは、でてこないよ。","おかしをかうね。"]),
    ],"Eメール",28,30),
    passage("4C","A New Activity",ARTICLE,[
        question(31,"What does Mindy do now?","ミンディは今、何をしていますか。",
                 ["She works at a company.","She sells computers.","She is a college student.","She is a basketball player."],
                 ["会社で働いている。","コンピューターを売っている。","大学生である。","バスケットボールの選手である。"],1,
                 ["she works at a company"],
                 "What does ～ do? は、仕事など普段していることを尋ねる言い方。最初の文に she works at a company（会社で働いている）とある。大学でバスケットボールをしていたのは昔のことで、今はしていない。コンピューターは職場で使っているが、売っているとは書かれていない。",
                 "ミンディはかいしゃではたらいているよ。バスケットボールは、だいがくのときのことだね。",
                 ["最初の文の she works at a company に一致する。","コンピューターは職場で使う物で、売っているとは書かれていない。","大学に通っていたのは昔のことで、今は会社で働いている。","バスケットボールは大学時代のことで、今はしていない。"],
                 ["かいしゃではたらいているね。","コンピューターをうっているのではないよ。","だいがくは、むかしのことだよ。","いまはバスケットボールをしていないよ。"]),
        question(32,"What did Mindy's brother say to Mindy?","ミンディの兄（弟）はミンディに何と言いましたか。",
                 ["She should try tennis.","She should go to college.","She should buy a newspaper.","She should cook him lunch."],
                 ["テニスをやってみるとよい。","大学に行くとよい。","新聞を買うとよい。","彼に昼食を作るとよい。"],1,
                 ["You should try tennis."],
                 "兄（弟）の言葉 You should try tennis. の You はミンディのことで、選択肢では She should try tennis. と言いかえている。should は『～したほうがよい』。新聞は、週末にミンディがサッカーレッスンの記事を見たもので、兄（弟）の言葉ではない。",
                 "おにいさん（おとうと）は『テニスをやってみたら』といったよ。should は『～したほうがいい』だね。",
                 ["兄（弟）の You should try tennis. の You を She に言いかえている。","大学に行くようにとは言っていない。","新聞はミンディが週末に記事を見たもので、兄（弟）の言葉ではない。","昼食は一緒に食べただけで、作るようにとは言っていない。"],
                 ["テニスをやってみたら、といったね。","だいがくのはなしではないよ。","しんぶんは、ミンディがじぶんでみたよ。","おひるごはんは、いっしょにたべただけだよ。"]),
        question(33,"What did Mindy see in the newspaper?","ミンディは新聞で何を見ましたか。",
                 ["An article about free soccer lessons.","A picture of her favorite park.","An article about her company.","A picture of her brother."],
                 ["無料のサッカーレッスンについての記事。","お気に入りの公園の写真。","自分の会社についての記事。","兄（弟）の写真。"],1,
                 ["Mindy saw an article in the newspaper about free soccer lessons."],
                 "第3段落の最初の文に、新聞で free soccer lessons（無料のサッカーレッスン）についての記事を見たとある。free はここでは『無料の』。公園は記事に書かれていた練習場所で、写真を見たとは書かれていない。会社や兄（弟）の記事・写真も出てこない。",
                 "しんぶんで、むりょうのサッカーレッスンのきじをみたよ。free は『むりょうの』だね。",
                 ["saw an article in the newspaper about free soccer lessons に一致する。","公園は練習場所として記事に出てくるだけで、写真の話はない。","会社についての記事は出てこない。","兄（弟）の写真は出てこない。"],
                 ["サッカーレッスンのきじだね。","こうえんのしゃしんは、でてこないよ。","かいしゃのきじは、でてこないよ。","おにいさん（おとうと）のしゃしんは、でてこないよ。"]),
        question(34,"When did Mindy meet the soccer coach for the first time?","ミンディはいつ初めてサッカーのコーチに会いましたか。",
                 ["On Sunday.","On Monday.","On Tuesday.","On Thursday."],
                 ["日曜日に。","月曜日に。","火曜日に。","木曜日に。"],4,
                 ["Mindy went to the park on Thursday and met the soccer coach for the first time."],
                 "練習日は日曜日・火曜日・木曜日の3つあるが、ミンディが公園へ行って初めてコーチに会ったのは on Thursday（木曜日）。月曜日は、兄（弟）がテニスのレッスンに誘った日。曜日がたくさん出てくるので、誰が何をした日かを分けて読む。",
                 "れんしゅうは、にちよう・かよう・もくよう。ミンディがはじめてコーチにあったのは、もくようびだよ。",
                 ["日曜日は練習日の一つだが、初めて行った日ではない。","月曜日は兄（弟）がテニスのレッスンに誘った日。","火曜日も練習日の一つだが、初めて行った日ではない。","on Thursday に公園へ行き、初めてコーチに会った。"],
                 ["にちようびは、れんしゅうのひのひとつだよ。","げつようびは、テニスのはなしだよ。","かようびも、れんしゅうのひのひとつだよ。","もくようびに、はじめてあったね。"]),
        question(35,"Why does Mindy walk to Graystone Park?","ミンディはなぜグレーストーン公園まで歩いて行くのですか。",
                 ["Her friends also walk there.","She wakes up early.","It is near her office.","It is by her house."],
                 ["友だちも歩いてそこへ行くから。","早起きするから。","公園が職場の近くにあるから。","公園が家のそばにあるから。"],3,
                 ["because it is near her office"],
                 "最後の文の because（～なので）の後ろが理由。it は Graystone Park を指し、公園が near her office（職場の近く）にある。ミンディは仕事の後にレッスンへ行く。家の近くとは書かれていない。",
                 "because は『～だから』。こうえんがしょくばのちかくにあるから、あるいていくんだね。",
                 ["友だちも歩いて行くとは書かれていない。","早起きの話は出てこない。","because it is near her office に一致する。","近いのは家ではなく職場（office）。"],
                 ["ともだちのことは、かいていないよ。","はやおきは、でてこないよ。","しょくばのちかくだからだね。","いえのちかくではないよ。"]),
    ],"英文",31,35),
]

PASSAGES[0]["format"]="notice"
PASSAGES[1]["format"]="multi-email"
PASSAGES[1]["emails"]=[]
for i in (0,2):
    meta={line.partition(":")[0].lower():line.partition(":")[2].strip() for line in PASSAGES[1]["paragraphs"][i].splitlines()}
    PASSAGES[1]["emails"].append(dict(meta=meta,body=PASSAGES[1]["paragraphs"][i+1],translation=PASSAGES[1]["translations"][i+1]))

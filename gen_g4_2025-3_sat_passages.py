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


# The notice keeps the booklet's six visual blocks: the heading and five centred sentences.
NOTICE=[
    [plain("Village Street Coffee Shop's Information","ビレッジ・ストリート・コーヒーショップからのお知らせ")],
    [row([("The shop is closed today","店は今日、閉まっています、"),("because the staff will change","スタッフが取りかえるので、"),("all the tables!","すべてのテーブルを。")],"is")],
    [row([("We are usually open","私たちはふだん営業しています、"),("from 10:00 a.m. to 4:00 p.m.","午前10時から午後4時まで。")],"are")],
    [row([("Now,","現在、"),("we are looking for","私たちは探しています、"),("new staff.","新しいスタッフを。")],"looking")],
    [row([("The new staff should work","新しいスタッフは働く必要があります、"),("from 9:30 a.m. to 4:30 p.m.","午前9時30分から午後4時30分まで、"),("on weekends.","週末に。")],"should")],
    [row([("They will make coffee","その人たちはコーヒーをいれます、"),("and clean the kitchen.","そして台所を掃除します。")],"will")],
]

EMAIL=[
    [plain("From: Tony Wilson","差出人：トニー・ウィルソン"),plain("To: Olivia West","宛先：オリビア・ウェスト"),
     plain("Date: October 2","日付：10月2日"),plain("Subject: My match","件名：ぼくの試合")],
    [plain("Hi Olivia,","オリビアへ、"),
     row([("Thanks for coming","来てくれてありがとう、"),("to my badminton match","ぼくのバドミントンの試合に、"),("last Saturday.","この前の土曜日に。")],"Thanks"),
     row([("After the match,","試合の後、"),("I wanted to talk with you,","ぼくはきみと話したかった、"),("but I had a meeting","でもミーティングがあった、"),("with my coach.","コーチとの。")],"wanted"),
     row([("I lost my match,","ぼくは試合に負けた、"),("so I was sad.","だから悲しかった。")],"lost"),
     row([("My next match is","ぼくの次の試合はあります、"),("at West Gate Sports Center","ウエスト・ゲート・スポーツセンターで、"),("on October 15","10月15日の"),("at 10:30 a.m.","午前10時30分に。")],"is"),
     row([("Can you watch","きみは見に来られる？"),("it?","その試合を。")],"watch"),
     plain("Your friend,","きみの友だち、"),plain("Tony","トニー")],
    [plain("From: Olivia West","差出人：オリビア・ウェスト"),plain("To: Tony Wilson","宛先：トニー・ウィルソン"),
     plain("Date: October 2","日付：10月2日"),plain("Subject: After your match","件名：あなたの試合の後")],
    [plain("Hi Tony,","トニーへ、"),
     row([("I'll watch","私は見ます、"),("my brother Daniel's baseball game","兄（弟）のダニエルの野球の試合を、"),("on that day.","その日に。")],"watch"),
     row([("It starts","それは始まります、"),("at 10:00 a.m.,","午前10時に、"),("so I can't see your match.","だからあなたの試合を見られません。")],"starts"),
     row([("I'm","私は"),("sorry!","申し訳なく思っています。")],"'m"),
     row([("But I'll go","でも、私は行きます、"),("to West Gate Sports Center","ウエスト・ゲート・スポーツセンターへ、"),("at 1:00 p.m.,","午後1時に、"),("after Daniel's game.","ダニエルの試合の後で。")],"go"),
     row([("After your match,","あなたの試合の後、"),("I want to go","私は行きたいです、"),("to the café","カフェへ、"),("near Eden's Supermarket","エデンズ・スーパーマーケットの近くの、"),("with you.","あなたと一緒に。")],"want"),
     row([("We can talk","私たちは話せます、"),("then!","そのときに。")],"talk"),
     plain("Your friend,","あなたの友だち、"),plain("Olivia","オリビア")],
]

ARTICLE=[
    [row([("Mika is a university student","ミカは大学生です、"),("in Japan,","日本の。"),("and her town is very cold","そして彼女の町はとても寒いです、"),("in winter.","冬は。")],"is"),
     row([("Last winter,","去年の冬、"),("a student from Australia, Kate,","オーストラリアから来た学生のケイトが"),("stayed at Mika's house","ミカの家に滞在しました、"),("for a homestay.","ホームステイで。")],"stayed"),
     row([("Kate spoke English","ケイトは英語を話しました、"),("and was learning","そして学んでいました、"),("Spanish and French.","スペイン語とフランス語を。")],"spoke"),
     row([("Mika and Kate soon became friends","ミカとケイトはすぐに友だちになりました、"),("because Kate also spoke Japanese well.","ケイトは日本語も上手に話したので。")],"became")],
    [row([("One morning,","ある朝、"),("when Mika and Kate woke up,","ミカとケイトが起きたとき、"),("they saw a lot of snow","2人はたくさんの雪を見ました、"),("in the garden.","庭に。")],"saw"),
     row([("At breakfast,","朝食のとき、"),("Kate said,","ケイトは言いました、"),("\"I saw a lot of snow","「たくさんの雪を見たよ、"),("for the first time.","初めて。"),
          ("It often rains in my town,","私の町ではよく雨が降るけれど、"),("but it doesn't snow.\"","雪は降らないの」と。")],"said"),
     row([("Then,","それから、"),("they talked about snow","2人は雪について話しました、"),("for two hours.","2時間。")],"talked")],
    [row([("The next Sunday,","次の日曜日、"),("Mika and Kate visited the snow festival","ミカとケイトは雪まつりを訪れました、"),("in Mika's town.","ミカの町の。")],"visited"),
     row([("They enjoyed seeing","2人は見るのを楽しみました、"),("beautiful snow art","美しい雪の作品を、"),("at the festival.","おまつりで。")],"enjoyed"),
     row([("Kate said,","ケイトは言いました、"),("\"This festival is exciting!\"","「このおまつりはわくわくするね！」と。")],"said"),
     row([("Mika said,","ミカは言いました、"),("\"Yes!","「うん！"),("Let's eat some hot food!\"","温かい食べ物を食べようよ！」と。")],"said"),
     row([("Then,","それから、"),("they bought four sausages.","2人はソーセージを4本買いました。")],"bought"),
     row([("They looked around the festival","2人はおまつりを見て回りました、"),("for three hours.","3時間。")],"looked"),
     row([("Mika was happy","ミカはうれしかったです、"),("to see Kate's smile.","ケイトの笑顔を見て。")],"was")],
]

# Full translations read naturally; bilingual slash units retain English order.
for block,translations in [
    (NOTICE[1],["スタッフがテーブルをすべて取りかえるため、本日は休業です。"]),
    (NOTICE[2],["ふだんの営業時間は、午前10時から午後4時までです。"]),
    (NOTICE[3],["現在、新しいスタッフを募集しています。"]),
    (NOTICE[4],["新しいスタッフには、週末の午前9時30分から午後4時30分まで働いてもらいます。"]),
    (NOTICE[5],["仕事は、コーヒーをいれることと台所の掃除です。"]),
    (EMAIL[1],["オリビアへ、","この前の土曜日は、ぼくのバドミントンの試合に来てくれてありがとう。",
               "試合の後、きみと話したかったけど、コーチとのミーティングがあったんだ。",
               "試合に負けて、悲しかったよ。","次の試合は、10月15日の午前10時30分から、ウエスト・ゲート・スポーツセンターであるんだ。",
               "見に来られるかな？","きみの友だち、","トニー"]),
    (EMAIL[3],["トニーへ、","その日は、兄（弟）のダニエルの野球の試合を見に行きます。",
               "試合が午前10時に始まるので、あなたの試合は見られません。","ごめんなさい！",
               "でも、ダニエルの試合が終わったら、午後1時にウエスト・ゲート・スポーツセンターへ行きます。",
               "あなたの試合の後、エデンズ・スーパーマーケットの近くのカフェに一緒に行きたいです。",
               "そのときに話せますね！","あなたの友だち、","オリビア"]),
    (ARTICLE[0],["ミカは日本の大学生で、彼女の町は冬になるととても寒くなります。",
                 "去年の冬、オーストラリア出身の学生ケイトが、ホームステイでミカの家に滞在しました。",
                 "ケイトは英語を話し、スペイン語とフランス語を学んでいました。",
                 "ケイトは日本語も上手に話したので、ミカとケイトはすぐに友だちになりました。"]),
    (ARTICLE[1],["ある朝、ミカとケイトが起きると、庭にたくさんの雪が積もっていました。",
                 "朝食のとき、ケイトは「こんなにたくさんの雪を見たのは初めて。私の町ではよく雨が降るけれど、雪は降らないの」と言いました。",
                 "それから2人は、雪について2時間話しました。"]),
    (ARTICLE[2],["次の日曜日、ミカとケイトはミカの町の雪まつりに行きました。",
                 "2人はおまつりで、美しい雪の作品を見て楽しみました。",
                 "ケイトは「このおまつり、わくわくするね！」と言いました。",
                 "ミカは「うん！温かいものを食べようよ！」と言いました。",
                 "それから2人は、ソーセージを4本買いました。",
                 "2人は3時間、おまつりを見て回りました。",
                 "ミカはケイトの笑顔を見て、うれしくなりました。"]),
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
        # 4A: each centred notice sentence is its own block, as printed.
        paragraphs=[" ".join(r[0] for r in block) for block in blocks]
    return dict(label=label,title=title,instruction=instruction(kind,start,end),paragraphs=paragraphs,
                translations=["\n".join(r[1] for r in b) for b in blocks],
                sentencePairs=[r for b in blocks for r in b], questions=questions)


PASSAGES=[
    passage("4A","Village Street Coffee Shop's Information",NOTICE,[
        question(26,"Today, the staff will","今日、スタッフは～します。",
                 ["help another coffee shop.","change all the tables.","welcome new staff.","clean the kitchen."],
                 ["別のコーヒーショップを手伝う。","すべてのテーブルを取りかえる。","新しいスタッフを迎える。","台所を掃除する。"],2,
                 ["The shop is closed today because the staff will change all the tables!"],
                 "掲示の最初の文で、because の後ろに今日休む理由が書かれている。the staff will change all the tables で『スタッフがすべてのテーブルを取りかえる』。台所の掃除は、これから働く新しいスタッフの仕事で、今日の予定ではない。",
                 "きょうおみせがやすみなのは、スタッフがテーブルをぜんぶとりかえるから。because のあとが、りゆうだよ。",
                 ["別のコーヒーショップの話は掲示にない。","because の後ろに、今日すべてのテーブルを取りかえるとある。","新しいスタッフは募集中で、今日迎えるとは書かれていない。","台所の掃除は、新しいスタッフがする仕事。"],
                 ["ほかのおみせのはなしは、かいていないよ。","テーブルをぜんぶとりかえるんだね。","あたらしいスタッフは、まだぼしゅうしているよ。","そうじは、あたらしいスタッフのしごとだよ。"]),
        question(27,"What time should the new staff start work on weekends?","新しいスタッフは、週末は何時に仕事を始める必要がありますか。",
                 ["At 9:30 a.m.","At 10:00 a.m.","At 4:00 p.m.","At 4:30 p.m."],
                 ["午前9時30分。","午前10時。","午後4時。","午後4時30分。"],1,
                 ["The new staff should work from 9:30 a.m. to 4:30 p.m. on weekends."],
                 "from A to B は『A から B まで』。新しいスタッフが働き始めるのは最初の 9:30 a.m. で、4:30 p.m. は終わる時刻。10:00 a.m. と 4:00 p.m. は、店のふだんの営業時間の始まりと終わり。誰の何の時間かを分けて読む。",
                 "あたらしいスタッフは、ごぜん9じ30ぷんからはたらくよ。10じは、おみせがあくじかんだね。",
                 ["新しいスタッフが週末に働き始める時刻。","午前10時は、店がふだん開く時刻。","午後4時は、店がふだん閉まる時刻。","午後4時30分は、新しいスタッフの仕事が終わる時刻。"],
                 ["9じ30ぷんにはじめるね。","10じは、おみせがあくじかんだよ。","4じは、おみせがしまるじかんだよ。","4じ30ぷんは、しごとがおわるじかんだよ。"]),
    ],"掲示",26,27),
    passage("4B","My match / After your match",EMAIL,[
        question(28,"What did Tony do after his match last Saturday?","トニーはこの前の土曜日の試合の後、何をしましたか。",
                 ["He lost his badminton racket.","He had a meeting.","He talked with Olivia.","He watched the next match."],
                 ["バドミントンのラケットをなくした。","ミーティングをした。","オリビアと話した。","次の試合を見た。"],2,
                 ["After the match, I wanted to talk with you, but I had a meeting with my coach."],
                 "After the match の文を読む。I wanted to talk with you は『きみと話したかった』で、but の後ろの I had a meeting with my coach が実際にあったこと。だから Olivia とは話せていない。lost は試合に負けたことで、ラケットをなくしたのではない。",
                 "しあいのあと、オリビアとはなしたかったけど、コーチとのミーティングがあったよ。but のあとが、ほんとうにあったことだね。",
                 ["lost は試合に負けたことで、ラケットをなくしたとは書かれていない。","but の後ろに、コーチとのミーティングがあったとある。","話したかったが、ミーティングがあって話せなかった。","次の試合は10月15日で、まだ行われていない。"],
                 ["まけたのは、しあいだよ。","コーチとミーティングをしたね。","はなしたかったけど、はなせなかったよ。","つぎのしあいは、まだだよ。"]),
        question(29,"What time will Daniel's baseball game start?","ダニエルの野球の試合は何時に始まりますか。",
                 ["At 10:00 a.m.","At 10:30 a.m.","At 1:00 p.m.","At 2:00 p.m."],
                 ["午前10時。","午前10時30分。","午後1時。","午後2時。"],1,
                 ["It starts at 10:00 a.m., so I can't see your match."],
                 "2通目の It starts at 10:00 a.m. の It は、前の文の my brother Daniel's baseball game を指す。10:30 a.m. は Tony の次の試合が始まる時刻、1:00 p.m. は Olivia がスポーツセンターへ行く時刻。2:00 p.m. はメールに出てこない。",
                 "It は、ダニエルのやきゅうのしあいのこと。ごぜん10じにはじまるよ。10じ30ぷんは、トニーのしあいだね。",
                 ["It starts at 10:00 a.m. の It がダニエルの試合を指す。","午前10時30分は、トニーの次の試合が始まる時刻。","午後1時は、オリビアがスポーツセンターへ行く時刻。","午後2時はメールに書かれていない。"],
                 ["10じにはじまるね。","10じ30ぷんは、トニーのしあいだよ。","1じは、オリビアがいくじかんだよ。","2じとは、かいていないよ。"]),
        question(30,"Where does Olivia want to go with Tony after Tony's match?","オリビアは、トニーの試合の後にトニーとどこへ行きたいのですか。",
                 ["To the baseball stadium.","To the sports shop.","To the café.","To the supermarket."],
                 ["野球場へ。","スポーツ用品店へ。","カフェへ。","スーパーマーケットへ。"],3,
                 ["After your match, I want to go to the café near Eden's Supermarket with you."],
                 "I want to go to ～ with you の『～』が行きたい場所。the café near Eden's Supermarket は『エデンズ・スーパーマーケットの近くのカフェ』で、near ～ はカフェの場所を説明している。行きたいのはスーパーマーケットではなくカフェ。",
                 "いきたいのはカフェ。スーパーマーケットは、カフェのばしょをせつめいしているだけだよ。near は『～のちかくの』だね。",
                 ["野球場へ行きたいとは書かれていない。","スポーツ用品店はメールに出てこない。","the café near Eden's Supermarket に一緒に行きたいとある。","スーパーマーケットは、カフェの場所を説明する語。"],
                 ["やきゅうじょうへいきたい、とはかいていないよ。","スポーツのおみせは、でてこないよ。","カフェにいきたいんだね。","スーパーは、カフェのちかくにあるおみせだよ。"]),
    ],"Eメール",28,30),
    passage("4C","Visiting the Snow Festival",ARTICLE,[
        question(31,"Where did Kate come from?","ケイトはどこから来ましたか。",
                 ["Australia.","France.","Spain.","America."],
                 ["オーストラリア。","フランス。","スペイン。","アメリカ。"],1,
                 ["Last winter, a student from Australia, Kate, stayed at Mika's house for a homestay."],
                 "a student from Australia, Kate は『オーストラリアから来た学生のケイト』。コンマではさまれた Kate が、a student from Australia と同じ人を表している。Spanish（スペイン語）と French（フランス語）は Kate が学んでいた言語で、出身国ではない。",
                 "ケイトは、オーストラリアからきたがくせいだよ。スペインごとフランスごは、べんきょうしていたことばだね。",
                 ["a student from Australia, Kate とある。","French は Kate が学んでいた言語で、出身国ではない。","Spanish は Kate が学んでいた言語で、出身国ではない。","アメリカは本文に出てこない。"],
                 ["オーストラリアからきたね。","フランスごは、べんきょうしていたことばだよ。","スペインごも、べんきょうしていたことばだよ。","アメリカは、でてこないよ。"]),
        question(32,"Mika and Kate soon became friends because","ミカとケイトは～ので、すぐに友だちになりました。",
                 ["Mika spoke English well.","Kate spoke Japanese well.","Mika's mother was kind to Kate.","both of them were learning Spanish."],
                 ["ミカが英語を上手に話した。","ケイトが日本語を上手に話した。","ミカの母がケイトに親切だった。","2人ともスペイン語を学んでいた。"],2,
                 ["Mika and Kate soon became friends because Kate also spoke Japanese well."],
                 "本文の because の後ろが、すぐに友だちになった理由。Kate also spoke Japanese well は『ケイトは日本語も上手に話した』で、also（～も）は英語に加えて日本語も、という意味。ミカが英語を話したとは書かれておらず、スペイン語を学んでいたと書かれているのは Kate だけ。",
                 "ケイトは、にほんごもじょうずにはなせたから、すぐにともだちになれたんだね。",
                 ["英語を話したのはケイト。ミカが英語を上手に話したとは書かれていない。","because の後ろの理由に一致する。","ミカの母は本文に出てこない。","スペイン語を学んでいたと書かれているのはケイトだけ。"],
                 ["えいごをはなしたのは、ケイトだよ。","ケイトがにほんごをじょうずにはなしたからだね。","ミカのおかあさんは、でてこないよ。","スペインごをならっていた、とかいてあるのはケイトだけだよ。"]),
        question(33,"What did Kate see for the first time when she woke up one morning?","ある朝、目が覚めたとき、ケイトは何を初めて見ましたか。",
                 ["Some Japanese flowers.","A lot of rain.","Some beautiful birds.","A lot of snow."],
                 ["日本の花。","たくさんの雨。","美しい鳥。","たくさんの雪。"],4,
                 ["they saw a lot of snow in the garden.","I saw a lot of snow for the first time."],
                 "One morning の文で、2人は庭にたくさんの雪を見た。朝食のとき Kate は I saw a lot of snow for the first time.（たくさんの雪を初めて見た）と言っている。Kate の町では It often rains（よく雨が降る）が、雪は降らない。雨は初めて見たものではない。",
                 "ケイトのまちは、あめはよくふるけど、ゆきはふらない。だから、たくさんのゆきをはじめてみたんだね。",
                 ["花は本文に出てこない。","雨は Kate の町でよく降るもので、初めて見たものではない。","鳥は本文に出てこない。","I saw a lot of snow for the first time. とある。"],
                 ["はなは、でてこないよ。","あめは、ケイトのまちでよくふるよ。","とりは、でてこないよ。","たくさんのゆきを、はじめてみたね。"]),
        question(34,"What did Mika and Kate enjoy seeing at the festival?","ミカとケイトは、おまつりで何を見て楽しみましたか。",
                 ["Some of Mika's friends.","Many famous artists.","Beautiful snow art.","An exciting contest."],
                 ["ミカの友だち何人か。","たくさんの有名な芸術家。","美しい雪の作品。","わくわくするコンテスト。"],3,
                 ["They enjoyed seeing beautiful snow art at the festival."],
                 "enjoyed seeing ～ は『～を見て楽しんだ』。質問の enjoy seeing と同じ形の文に beautiful snow art（美しい雪の作品）とある。exciting は Kate がおまつりについて言った言葉で、コンテストは本文に出てこない。art（作品）と artists（芸術家）の違いにも注意する。",
                 "おまつりで、きれいなゆきのさくひんをみてたのしんだよ。art は『さくひん』、artist は『さくひんをつくるひと』だね。",
                 ["ミカの友だちは本文に出てこない。","芸術家は本文に出てこない。","enjoyed seeing beautiful snow art とある。","exciting はおまつりの感想で、コンテストは本文にない。"],
                 ["ミカのともだちは、でてこないよ。","ゆうめいなひとは、でてこないよ。","きれいなゆきのさくひんだね。","コンテストは、でてこないよ。"]),
        question(35,"How long did Mika and Kate look around the festival?","ミカとケイトは、どのくらいの時間おまつりを見て回りましたか。",
                 ["For one hour.","For two hours.","For three hours.","For four hours."],
                 ["1時間。","2時間。","3時間。","4時間。"],3,
                 ["They looked around the festival for three hours."],
                 "How long は『どのくらいの間』と時間の長さを尋ねる。look around（見て回る）の文に for three hours とある。two hours は雪について話した時間、four は買ったソーセージの数。数字が何を表しているかを確かめる。",
                 "おまつりをみてまわったのは3じかん。2じかんは、ゆきのはなしをしたじかん。4は、ソーセージのかずだよ。",
                 ["1時間とは書かれていない。","2時間は、雪について話した時間。","looked around the festival for three hours とある。","4はソーセージの数で、時間ではない。"],
                 ["1じかんとは、かいていないよ。","2じかんは、ゆきのはなしをしたじかんだよ。","3じかんみてまわったね。","4は、ソーセージのかずだよ。"]),
    ],"英文",31,35),
]

PASSAGES[0]["format"]="notice"
PASSAGES[1]["format"]="multi-email"
PASSAGES[1]["emails"]=[]
for i in (0,2):
    meta={line.partition(":")[0].lower():line.partition(":")[2].strip() for line in PASSAGES[1]["paragraphs"][i].splitlines()}
    PASSAGES[1]["emails"].append(dict(meta=meta,body=PASSAGES[1]["paragraphs"][i+1],translation=PASSAGES[1]["translations"][i+1]))

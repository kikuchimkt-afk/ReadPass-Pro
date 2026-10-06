"""Complete, explicitly aligned reading text; never split Mr./D.C./a.m. by regex."""

def row(ja,verb,*units):
    return [" ".join(a for a,b in units),ja,"||".join(a+"|"+b for a,b in units),verb]
def plain(en,ja):return row(ja,"",(en,ja))
def question(n,stem,ja,choices,meanings,answer,evidence,note,simple,reasons,easy):
    return dict(number=n,question=stem,questionTranslation=ja,choices=choices,choiceTranslations=meanings,
                answer=answer,sourceEvidence=evidence,grammar=f"本文の根拠は「{' / '.join(evidence)}」。{note}",grammarSimple=simple,
                choiceAnalysis=[("○ " if i==answer else "")+f"{c}＝{t}。{r}" for i,(c,t,r) in enumerate(zip(choices,meanings,reasons),1)],
                choiceAnalysisSimple=[("○ " if i==answer else "")+f"{t}。{r}" for i,(t,r) in enumerate(zip(meanings,easy),1)])

NOTICE=[
    [plain("Anton Bell Cookie Shop's Opening Sale","アントン・ベル・クッキー店の開店セール"),
     row("フラワー・パークの隣に開店します。","We'll",("We'll open","当店は開店します、"),("next to Flower Park!","フラワー・パークの隣に。"))],
    [plain("Date: April 7","日付：4月7日"),plain("Time: 10:00 a.m.-5:00 p.m.","時間：午前10時から午後5時まで")],
    [row("開店セールの間、どのクッキーも1ドルで販売します。","will",("During our opening sale,","開店セールの間、"),("every cookie will be sold","どのクッキーも販売されます、"),("for only $1.","わずか1ドルで。")),
     row("3枚以上買うと、クッキーを1枚無料でもらえます。","you'll",("If you buy three or more cookies,","もしクッキーを3枚以上買えば、"),("you'll get one free cookie!","無料のクッキーを1枚もらえます。")),
     row("大きなクッキーを30種類そろえています。","have",("We have","当店にはあります、"),("thirty kinds of large cookies.","30種類の大きなクッキーが。"))],
    [plain("Special Ticket and Birthday Gift Card","特別チケットと誕生日ギフトカード"),
     row("先着40名に特別チケットをお渡しします。","will",("The first forty people","最初の40人は"),("will receive a special ticket.","特別チケットを受け取ります。")),
     row("このチケットを使うと、次回来店時に50％引きになります。","can",("With this ticket,","このチケットで、"),("you can get a 50% discount","50％の割引を受けられます、"),("on your next visit.","次の来店時に。")),
     row("すべての人に誕生日ギフトカードもお渡しします。","will",("All people","すべての人は"),("will also get a birthday gift card.","誕生日ギフトカードももらえます。")),
     row("誕生日にそのカードを当店に持参し、プレゼントと交換できます。","can",("You can bring the card","そのカードを持って来られます、"),("to our shop on your birthday","誕生日に当店へ、"),("and exchange it for a gift.","そしてプレゼントと交換できます。"))],
]

EMAIL=[
    [plain("Hi Aunt Jill,","ジルおばさんへ、"),
     row("音楽について質問があります。","have",("I have","私にはあります、"),("a question about music.","音楽についての質問が。")),
     row("先日、家でラジオを聞いていて、すてきな曲を聞きました。","was",("The other day,","先日、"),("I was listening to the radio at home,","家でラジオを聞いていました、"),("and I heard a cool song.","そしてすてきな曲を聞きました。")),
     row("歌詞のいくつかを覚えていて、インターネットで調べたら、その曲を見つけました。","remembered",("I remembered some of the words,","歌詞のいくつかを覚えていました、"),("and when I checked the Internet,","そしてインターネットで調べたとき、"),("I found the song!","その曲を見つけました。")),
     row("ホワイト・フォックスの『スノー』という曲です。","is",("It is called","それは呼ばれています、"),('"Snow" by White Fox.',"ホワイト・フォックスの『スノー』と。")),
     row("本当に古い曲です。","is",("It is","それは"),("a really old song.","本当に古い曲です。")),
     row("友達やピアノ教室の先生に聞きましたが、誰もその曲を知りませんでした。","asked",("I asked my friends and my teacher at piano school,","友達とピアノ教室の先生に尋ねました、"),("but no one knew the song.","でも誰もその曲を知りませんでした。")),
     row("おばさんは音楽が好きだと知っているので、もしかしたらその曲を知っていると思いました。","know",("I know you like music,","おばさんが音楽を好きだと知っています、"),("so I thought maybe you would know it.","だから、もしかしたらその曲を知っていると思いました。")),
     row("そのバンドの曲をもっと聞きたいです。","want",("I want to listen","私は聞きたいです、"),("to more songs by the band.","そのバンドのもっと多くの曲を。")),
     row("それらを教えてもらえますか。","Can",("Can you show","見せてもらえますか、"),("them to me?","それらを私に。")),
     plain("Love,","愛を込めて、"),plain("Marie","マリー")],
    [plain("Hi Marie,","マリーへ、"),
     row("ホワイト・フォックスと『スノー』という曲を知っています。","know",("I know White Fox", "私はホワイト・フォックスを知っています、"),('and the song "Snow."',"そして『スノー』という曲も。")),
     row("その曲を初めて聞いたのは、10歳のときでした。","heard",("I first heard that song","私はその曲を初めて聞きました、"),("when I was ten years old.","10歳のときに。")),
     row("それは20年前でした。","was",("That was","それは"),("twenty years ago!","20年前でした。")),
     row("ホワイト・フォックスは約30年前に音楽活動を始めましたが、5年前に活動をやめました。","started",("White Fox started making music around thirty years ago,","ホワイト・フォックスは約30年前に音楽活動を始めました、"),("but they stopped making music five years ago.","でも5年前に音楽活動をやめました。")),
     row("一度、彼らのコンサートに行きました。","went",("I went","私は行きました、"),("to their concert once.","彼らのコンサートに一度。")),
     row("家に彼らのCDがたくさんあるので、あなたにあげます。","have",("I have a lot of their CDs at my house,","私の家には彼らのCDがたくさんあります、"),("so I will give them to you.","だからあなたにあげます。")),
     row("土曜日の昼食後に、私の家へ来られますか。","Can",("Can you come to my house","私の家へ来られますか、"),("on Saturday after lunch?","土曜日の昼食後に。")),
     row("夕食を作ってあげるので、一緒に彼らの音楽を聞きましょう。","will",("I will make you dinner,","私はあなたに夕食を作ります、"),("and we can listen to their music together.","そして一緒に彼らの音楽を聞けます。")),
     plain("Your aunt,","あなたのおばさん、"),plain("Jill","ジル")],
    [plain("Hi Aunt Jill,","ジルおばさんへ、"),
     row("おばさんがそのバンドを知っていてうれしいです。","am",("I am happy","私はうれしいです、"),("you know the band!","おばさんがそのバンドを知っていて。")),
     row("土曜日は午前中にピアノの練習がありますが、午後は空いています。","have",("I have piano practice in the morning on Saturday,","土曜日の午前中にピアノの練習があります、"),("but I am free in the afternoon.","でも午後は空いています。")),
     row("自分の家で昼食を食べた後、バスでおばさんの家へ行きます。","will",("After eating lunch at my house,","自分の家で昼食を食べた後、"),("I will take the bus to your house.","バスでおばさんの家へ行きます。")),
     row("CDプレーヤーを持っていないので、おばさんのものを借りてもいいですか。","do",("I do not have a CD player,","私はCDプレーヤーを持っていません、"),("so can I borrow yours?","だからおばさんのものを借りてもいいですか。")),
     row("おばさんのために、ピアノで何曲か弾きたいです。","want",("I also want to play some songs","私は何曲か弾きたいです、"),("on the piano for you.","ピアノでおばさんのために。")),
     row("おばさんの家のピアノを使ってもいいですか。","Can",("Can I use the piano","ピアノを使ってもいいですか、"),("at your house?","おばさんの家で。")),
     plain("See you soon,","また近いうちに、"),plain("Marie","マリー")],
]
META=[dict(from_="Marie Brown",to="Jill Johnson",date="September 18",subject="Old song"),
      dict(from_="Jill Johnson",to="Marie Brown",date="September 18",subject="White Fox"),
      dict(from_="Marie Brown",to="Jill Johnson",date="September 19",subject="Saturday afternoon")]
for meta in META:meta["from"]=meta.pop("from_")
HEADERS=[[plain(f"From: {m['from']}",f"差出人：{['マリー・ブラウン','ジル・ジョンソン','マリー・ブラウン'][i]}"),
          plain(f"To: {m['to']}",f"宛先：{['ジル・ジョンソン','マリー・ブラウン','ジル・ジョンソン'][i]}"),
          plain(f"Date: {m['date']}",f"日付：9月{[18,18,19][i]}日"),
          plain(f"Subject: {m['subject']}",f"件名：{['古い曲','ホワイト・フォックス','土曜日の午後'][i]}")] for i,m in enumerate(META)]

ARTICLE=[
    [row("マシュー・ヘンソンは1866年に、川の近くの町で生まれました。","was",("Matthew Henson was born in 1866","マシュー・ヘンソンは1866年に生まれました、"),("in a town near a river.","川の近くの町で。")),
     row("幼いときに両親が亡くなり、おじと暮らしました。","died",("His parents died when he was young,","彼が幼いときに両親が亡くなりました、"),("and he lived with his uncle.","そして彼はおじと暮らしました。")),
     row("その後、船で働きました。","worked",("Then, he worked","その後、彼は働きました、"),("on a ship.","船で。")),
     row("その船で、地図の読み方と道具の使い方を学びました。","learned",("On that ship, he learned","その船で、彼は学びました、"),("how to read maps and use tools.","地図の読み方と道具の使い方を。")),
     row("世界を旅した後、ワシントンD.C.で暮らしました。","traveled",("He traveled around the world","彼は世界を旅しました、"),("and then lived in Washington, D.C.","そしてその後ワシントンD.C.で暮らしました。"))],
    [row("成長したヘンソンは、ロバート・ピアリーという探検家に出会いました。","met",("When Henson grew older,","ヘンソンが年を重ねたとき、"),("he met an explorer named Robert Peary.","ロバート・ピアリーという探検家に会いました。")),
     row("ピアリーは未知の場所への困難な旅を計画していて、手伝ってくれる技能のある人々を必要としていました。","was",("Peary was planning difficult trips to new places,","ピアリーは未知の場所への困難な旅を計画していました、"),("and he needed people with skills to help him.","そして彼を助ける技能のある人々を必要としていました。")),
     row("ヘンソンはこの仕事にぴったりでした。","was",("Henson was","ヘンソンは"),("perfect for this job.","この仕事にぴったりでした。")),
     row("彼はいくつかの外国語を話し、道具を修理し、方角を理解できました。","could",("He could speak several foreign languages,","彼はいくつかの外国語を話せました、"),("fix tools, and understand directions.","道具を修理し、方角を理解することもできました。")),
     row("ピアリーとヘンソンは多くの旅で仲間になりました。","became",("Peary and Henson became partners","ピアリーとヘンソンは仲間になりました、"),("on many journeys.","多くの旅で。")),
     row("2人は一緒に、世界のとても寒い地域を旅しました。","traveled",("Together, they traveled","一緒に、彼らは旅しました、"),("to very cold parts of the world.","世界のとても寒い地域へ。"))],
    [row("ピアリーとヘンソンには夢がありました。","had",("Peary and Henson had","ピアリーとヘンソンにはありました、"),("a dream.","夢が。")),
     row("世界で最も北にある北極点へ、誰よりも先に行きたかったのです。","wanted",("They wanted to go to the North Pole,","彼らは北極点へ行きたかったのです、"),("the most northern part of the world,","世界で最も北の場所へ、"),("before anyone else.","ほかの誰よりも先に。")),
     row("1891年から、何度もそこへ行こうとしました。","tried",("From 1891,","1891年から、"),("they tried many times to go.","彼らは何度も行こうとしました。")),
     row("しかし、その旅はとても危険でした。","were",("However,","しかし、"),("the journeys were very dangerous.","その旅はとても危険でした。")),
     row("大きな嵐や厚い氷に船を止められ、動けなくなることがありました。","stopped",("Sometimes, large storms and thick ice stopped their ship,","時には、大きな嵐や厚い氷が彼らの船を止めました、"),("so it could not move.","そのため船は動けませんでした。")),
     row("ついに1909年4月、ヘンソンとピアリーの夢は実現し、2人は北極点に到達しました。","came",("Finally, in April 1909,","ついに1909年4月、"),("the dream that Henson and Peary had came true,","ヘンソンとピアリーが抱いていた夢が実現しました、"),("and they reached the North Pole.","そして彼らは北極点に到達しました。")),
     row("ヘンソンは、この地点に到達した最初のアフリカ系アメリカ人でした。","was",("Henson was the first African American","ヘンソンは最初のアフリカ系アメリカ人でした、"),("to reach this point.","この地点に到達した。"))],
    [row("1900年代初め、多くの人はヘンソンが北極点へ行ったことを知りませんでした。","did",("In the early 1900s,","1900年代初め、"),("many people did not know","多くの人は知りませんでした、"),("that Henson went to the North Pole.","ヘンソンが北極点へ行ったことを。")),
     row("1930年代以降、多くの人が彼の旅を知り、1940年代に彼はメダルを授与されました。","learned",("After the 1930s,","1930年代以降、"),("many people learned about his trip,","多くの人が彼の旅について知りました、"),("and in the 1940s, he was given a medal.","そして1940年代に彼はメダルを授与されました。")),
     row("ヘンソンが1955年にニューヨークで亡くなった後、多くの人が彼を研究しました。","studied",("After Henson died in New York in 1955,","ヘンソンが1955年にニューヨークで亡くなった後、"),("many people studied him.","多くの人が彼を研究しました。")),
     row("今では、彼はとても有名です。","is",("Now he is","今、彼は"),("very famous.","とても有名です。"))],
]

NOTICE_Q=[
    question(21,"If people want a cookie for free during the sale, they should","セール中に無料のクッキーが欲しい人は、何をすべきですか。",
             ["order two different kinds of cookies.","buy three or more cookies.","go to the shop before 10:00 a.m.","give a card to the staff."],
             ["異なる2種類のクッキーを注文する。","クッキーを3枚以上買う。","午前10時より前に店へ行く。","カードを店員に渡す。"],2,
             ["If you buy three or more cookies, you'll get one free cookie!"],
             "If は無料でもらう条件。three or more は『3枚以上』。種類の数や来店時刻ではない。誕生日カードによるプレゼント交換は、別の特典として説明されている。",
             "クッキーを3まいいじょうかうと、1まいむりょうでもらえるよ。2しゅるいではなく、かうまいすうがじょうけんだね。",
             ["必要なのは2種類の注文でなく、3枚以上の購入。","本文の three or more と一致する条件。","開店時刻で、無料の条件ではない。","カードの交換は誕生日プレゼントの特典。"],
             ["2しゅるいかうだけではないよ。","3まいいじょうかうと、1まいもらえるね。","はやくいくことが、じょうけんではないよ。","カードは、たんじょうびのプレゼントだよ。"]),
    question(22,"What can people do with the special ticket?","特別チケットを使って何ができますか。",
             ["Enter Flower Park for free.","Get an invitation to another shop.","Get a discount on a future visit.","Exchange the ticket for a birthday gift."],
             ["フラワー・パークに無料で入る。","別の店への招待状をもらう。","今後の来店時に割引を受ける。","チケットを誕生日プレゼントと交換する。"],3,
             ["With this ticket, you can get a 50% discount on your next visit."],
             "this ticket は先着40人の special ticket。on your next visit が future visit に言い換えられている。誕生日プレゼントは birthday gift card の機能なので、二つの特典を区別する。",
             "とくべつチケットは、つぎにおみせへきたときのわりびきだよ。たんじょうびのプレゼントは、べつのカード。チケットとカードをわけよう。",
             ["公園は店の隣にあるだけで、入場特典ではない。","別の店への招待は書かれていない。","next visit を future visit と言い換えた選択肢。","交換できるのは誕生日カードで、特別チケットではない。"],
             ["こうえんにはいるチケットではないよ。","べつのおみせへのしょうたいではないよ。","つぎのらいてんで、わりびきになるね。","プレゼントは、べつのカードでもらうよ。"]),
]
EMAIL_Q=[
    question(23,'Where did Marie hear the song called "Snow"?','マリーは『スノー』という曲をどこで聞きましたか。',
             ["In the car.","At home.","At her friend's house.","At her piano school."],
             ["車の中で。","自宅で。","友達の家で。","ピアノ教室で。"],2,
             ["The other day, I was listening to the radio at home, and I heard a cool song."],
             "第1のメールの差出人は Marie。at home が曲を聞いた場所。piano school は後から先生に曲を尋ねた場所で、初めて聞いた場所ではない。質問の人と動作をセットで探す。",
             "マリーは、じぶんのいえでラジオをきいて、そのきょくをきいたよ。ピアノのせんせいには、あとからきょくについてきいたんだね。",
             ["ラジオを聞いたが、車ではなく at home とある。","at home が曲を聞いた場所。","友達に尋ねたが、友達の家で聞いたとは書かれていない。","先生に曲を尋ねた場所と、曲を聞いた場所を混同している。"],
             ["くるまではなく、いえだよ。","じぶんのいえで、きいたね。","ともだちのいえとはかいていないよ。","ピアノのせんせいには、あとからきいたよ。"]),
    question(24,'When did Jill first hear the song called "Snow"?','ジルは『スノー』を初めていつ聞きましたか。',
             ["Five years ago.","Ten years ago.","Twenty years ago.","Thirty years ago."],
             ["5年前。","10年前。","20年前。","30年前。"],3,
             ["I first heard that song when I was ten years old.","That was twenty years ago!"],
             "第2のメールは Jill。ten years old は当時の年齢で、何年前かの答えは次の twenty years ago。30年前はバンドの活動開始、5年前は活動終了。年齢・聞いた時期・バンドの歴史を区別する。",
             "ジルがはじめてきいたのは20ねんまえだよ。10は、そのときのねんれい。30ねんまえはバンドのはじまり、5ねんまえはおわりだね。",
             ["5年前はバンドが音楽活動をやめた時期。","10歳だったのであり、10年前とは書かれていない。","That was twenty years ago が聞いた時期を説明する。","30年前はバンドの音楽活動の開始。"],
             ["5ねんまえは、バンドがやめたときだよ。","10はねんれいで、なんねんまえかではないよ。","はじめてきいたのは20ねんまえだね。","30ねんまえは、バンドのはじまりだよ。"]),
    question(25,"What will Marie do on Saturday morning?","マリーは土曜日の午前中に何をしますか。",
             ["Buy some CDs.","Clean her house.","Practice the piano.","Eat at a restaurant."],
             ["CDを買う。","自分の家を掃除する。","ピアノを練習する。","レストランで食事をする。"],3,
             ["I have piano practice in the morning on Saturday, but I am free in the afternoon."],
             "第3のメールの in the morning on Saturday が時間を特定する。午前は piano practice、午後は空いていて、家で昼食後におばの家へ向かう。CDは買うのではなく、おばからもらう予定。",
             "どようびのごぜんは、ピアノのれんしゅうだよ。おばさんのいえへいくのは、じぶんのいえでおひるをたべたあと。ごぜんとごごをわけよう。",
             ["CDはおばが持っており、あげると伝えている。","家の掃除という予定は書かれていない。","piano practice が土曜午前の予定。","昼食は自分の家で、夕食はおばの家。"],
             ["CDをかうのではなく、もらうよ。","そうじのよていはかいていないよ。","ごぜんは、ピアノのれんしゅうだね。","レストランでたべるのではないよ。"]),
]
ARTICLE_Q=[
    question(26,"Where was Matthew Henson born?","マシュー・ヘンソンはどこで生まれましたか。",
             ["In a town close to a river.","In Washington, D.C.","On an explorer's farm.","On a ship."],
             ["川に近い町で。","ワシントンD.C.で。","探検家の農場で。","船で。"],1,
             ["Matthew Henson was born in 1866 in a town near a river."],
             "near a river が close to a river に言い換えられている。生まれた場所を聞くので was born の文に戻る。ワシントンD.C.は後から住んだ場所、船は働いた場所で、出生地ではない。",
             "うまれたのは、かわのちかくのまちだよ。near と close to は、どちらも『～のちかく』。すんだばしょや、はたらいたばしょとはわけよう。",
             ["near a river を close to a river と言い換えている。","世界を旅した後に住んだ場所で、出生地ではない。","探検家とは後から会い、農場で生まれたとは書かれていない。","船は後から働いた場所。"],
             ["かわのちかくのまちで、うまれたね。","あとからすんだばしょだよ。","のうじょうでうまれたとはかいていないよ。","ふねは、あとからはたらいたばしょだよ。"]),
    question(27,"Why did Robert Peary choose Henson to go on some journeys?","ロバート・ピアリーはなぜヘンソンを旅の仲間に選びましたか。",
             ["He could leave right away.","He could speak some languages.","He traveled to cold countries.","He had a lot of tools."],
             ["すぐに出発できたから。","いくつかの言語を話せたから。","寒い国々を旅したから。","道具をたくさん持っていたから。"],2,
             ["Peary was planning difficult trips to new places, and he needed people with skills to help him.","He could speak several foreign languages, fix tools, and understand directions."],
             "必要だったのは skills（技能）のある人。several foreign languages が some languages に対応する。寒い地域への旅は仲間になった後の行動。fix tools は修理する技能で、所有数ではない。",
             "ヘンソンは、いくつかのがいこくごをはなせたよ。たびにやくだつぎのうがあったんだね。どうぐをなおせることと、たくさんもっていることはちがうよ。",
             ["すぐ出発できたという条件は書かれていない。","外国語を話せる技能がピアリーの求める人に合う。","寒い地域への旅は仲間になった後で、選ばれた理由ではない。","道具を修理できたのであり、所有数は述べられていない。"],
             ["すぐにでかけられるから、とはかいていないよ。","いくつかのことばを、はなせたんだね。","さむいところへは、なかまになってからいったよ。","どうぐをもつかずではなく、なおせるぎのうだよ。"]),
    question(28,"What happened to Peary and Henson in 1909?","1909年、ピアリーとヘンソンに何が起こりましたか。",
             ["Their tools were stolen.","Their dream came true.","Thick ice stopped their ship.","There was a large storm."],
             ["道具を盗まれた。","夢が実現した。","厚い氷が船を止めた。","大きな嵐があった。"],2,
             ["Finally, in April 1909, the dream that Henson and Peary had came true, and they reached the North Pole."],
             "Finally と in April 1909 に続く came true が答え。夢は北極点への到達で、実際に reached the North Pole とある。嵐や氷はそれまでの旅の困難で、1909年の最終的な成功と区別する。",
             "1909ねん4がつに、ほっきょくてんへついて、ゆめがかなったよ。came true は『じつげんした』。あらしやこおりは、それまでにこまったことだね。",
             ["道具の盗難は本文に書かれていない。","北極点に到達して夢が実現した。","氷は途中の困難で、1909年の到達の出来事ではない。","嵐は途中の困難で、1909年の成功を答えていない。"],
             ["どうぐをぬすまれたとはかいていないよ。","ほっきょくてんについて、ゆめがかなったね。","こおりは、それまでのたびのこまったことだよ。","あらしも、それまでのたびのことだよ。"]),
    question(29,"In the 1940s,","1940年代、何が起こりましたか。",
             ["many other people went to the North Pole.","people thought only Peary studied foreign cultures.","Henson died in New York.","Henson received a medal."],
             ["ほかの多くの人が北極点へ行った。","ピアリーだけが外国文化を研究したと人々は考えた。","ヘンソンがニューヨークで亡くなった。","ヘンソンがメダルを受け取った。"],4,
             ["After the 1930s, many people learned about his trip, and in the 1940s, he was given a medal."],
             "in the 1940s に続く was given a medal が received a medal に言い換えられている。受動態『授与された』と能動態『受け取った』は同じ出来事。死亡は1955年なので、年代を分ける。",
             "1940ねんだいに、メダルをもらったよ。was given は『あたえられた』、received は『うけとった』で、おなじこと。なくなったのは1955ねんだね。",
             ["多くの人は旅を知ったのであり、北極点へ行ったとは書かれていない。","外国文化の研究やピアリーだけという話は書かれていない。","ニューヨークで亡くなったのは1955年。","was given a medal と同じ出来事を能動態で表す。"],
             ["ひとびとは、たびのことをしったんだよ。","ピアリーだけのけんきゅうとはかいていないよ。","なくなったのは1955ねんだよ。","1940ねんだいに、メダルをもらったね。"]),
    question(30,"What is this story about?","この話は何についてですか。",
             ["A famous ship.","A man who went to the North Pole.","A man who made a new language.","A cold country."],
             ["有名な船。","北極点へ行った男性。","新しい言語を作った男性。","寒い国。"],2,
             ["Matthew Henson was born in 1866 in a town near a river.","Finally, in April 1909, the dream that Henson and Peary had came true, and they reached the North Pole."],
             "題名 Matthew Henson と全段落の内容から、北極点へ行った人物の生涯が主題。船・寒い地域は人生の一場面で、全体の中心ではない。外国語を話せたが、新しい言語を作ったわけではない。",
             "これは、ほっきょくてんへいったヘンソンさんのおはなし。うまれたときから、ゆめがかなって、ゆうめいになるまでをよんだね。ふねだけのおはなしではないよ。",
             ["船は彼が働いた場所で、話全体の主題ではない。","出生・探検・到達・評価を通してヘンソンの生涯を描く。","外国語を話せたが、新しい言語を作ったとは書かれていない。","寒い場所は旅の行き先で、中心は人物の生涯。"],
             ["ふねだけのおはなしではないよ。","ほっきょくてんへいったひとのおはなしだね。","あたらしいことばをつくったのではないよ。","くにではなく、ヘンソンさんがちゅうしんだよ。"]),
]

def groups(blocks):
    return dict(paragraphs=[" ".join(r[0] for r in b) for b in blocks],translations=["".join(r[1] for r in b) for b in blocks],sentencePairs=[r for b in blocks for r in b])

def passages():
    a=dict(label="A",title="Anton Bell Cookie Shop's Opening Sale",format="notice",**groups(NOTICE),questions=NOTICE_Q,
           instruction="次の掲示の内容に関して，(21)と(22)の質問に対する答えとして最も適切なもの，または文を完成させるのに最も適切なものを1，2，3，4の中から一つ選び，その番号のマーク欄をぬりつぶしなさい。")
    # The title is already displayed from title. Keep the special-ticket heading
    # separate from its four body sentences (the fixed PDF gives it a panel).
    notice_rows=a["sentencePairs"]
    notice_blocks=[[notice_rows[1]],notice_rows[2:4],notice_rows[4:7],[notice_rows[7]],notice_rows[8:]]
    a["paragraphs"]=[("\n" if i==1 else " ").join(r[0] for r in rows) for i,rows in enumerate(notice_blocks)]
    a["translations"]=[("\n" if i==1 else "").join(r[1] for r in rows) for i,rows in enumerate(notice_blocks)]
    blocks=[b for pair in zip(HEADERS,EMAIL) for b in pair]
    def email_text(rows,field):
        joiner=" " if field==0 else ""
        return "\n".join([rows[0][field],joiner.join(r[field] for r in rows[1:-2]),rows[-2][field],rows[-1][field]])
    email_data=groups(blocks)
    email_data["paragraphs"]=[text for header,body in zip(HEADERS,EMAIL) for text in ["\n".join(r[0] for r in header),email_text(body,0)]]
    email_data["translations"]=[text for header,body in zip(HEADERS,EMAIL) for text in ["\n".join(r[1] for r in header),email_text(body,1)]]
    b=dict(label="B",title="Old song / White Fox / Saturday afternoon",format="multi-email",**email_data,questions=EMAIL_Q,
           instruction="次のEメールの内容に関して，(23)から(25)までの質問に対する答えとして最も適切なもの，または文を完成させるのに最も適切なものを1，2，3，4の中から一つ選び，その番号のマーク欄をぬりつぶしなさい。",
           emails=[dict(meta=meta,body=email_text(body,0),translation=email_text(body,1)) for meta,body in zip(META,EMAIL)])
    c=dict(label="C",title="Matthew Henson",format="article",**groups(ARTICLE),questions=ARTICLE_Q,
           instruction="次の英文の内容に関して，(26)から(30)までの質問に対する答えとして最も適切なもの，または文を完成させるのに最も適切なものを1，2，3，4の中から一つ選び，その番号のマーク欄をぬりつぶしなさい。")
    return [a,b,c]

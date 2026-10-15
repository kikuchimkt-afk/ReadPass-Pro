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


# The notice keeps the booklet's four visual blocks: heading, question line, body, closing request.
NOTICE=[
    [plain("Jogging in the Gym","体育館でジョギング")],
    [row([("Are you interested","あなたは興味がありますか、"),("in jogging?","ジョギングに。")],"Are")],
    [row([("Students can jog","生徒はジョギングができます、"),("in the school gym","学校の体育館で、"),("before school starts at 8:00 a.m.","午前8時に学校が始まる前に。")],"can"),
     row([("You can run around the gym","体育館の中を走り回ることができ、"),("and listen to music","そして音楽を聞くことができます、"),("for 20 minutes!","20分間。")],"can"),
     row([("Teachers will bring juice","先生たちがジュースを持ってきます、"),("to drink.","飲むための。")],"will")],
    [row([("If you want to join,","参加したい場合は、"),("please arrive","到着してください、"),("at the school gym","学校の体育館に、"),("at 7:30 a.m.","午前7時30分に。")],"arrive")],
]

EMAIL=[
    [plain("From: Mark Marshall","差出人：マーク・マーシャル"),plain("To: Agnes Marshall","宛先：アグネス・マーシャル"),
     plain("Date: October 11","日付：10月11日"),plain("Subject: Grandpa's birthday","件名：おじいちゃんの誕生日")],
    [plain("Dear Grandma,","おばあちゃんへ、"),
     row([("I want to do something","私は何かをしたいです、"),("for Grandpa's birthday","おじいちゃんの誕生日のために、"),("on Saturday.","土曜日に。")],"want"),
     row([("First, I wanted","最初、私はしたいと思っていました、"),("to take him to the zoo,","おじいちゃんを動物園に連れて行くことを。"),("but it'll rain on Saturday.","でも、土曜日は雨が降りそうです。")],"wanted"),
     row([("So, I'll take him","だから、おじいちゃんを連れて行きます、"),("to the movies!","映画に。")],"take"),
     row([("It'll be","それはなるでしょう、"),("a surprise.","サプライズに。")],"be"),
     row([("Should we take","私たちは乗ったほうがいいですか、"),("the bus or the train","バスと電車のどちらに、"),("to the Georgetown Theater?","ジョージタウン劇場へ行くのに。")],"take"),
     row([("Also,","それから、"),("does Grandpa like","おじいちゃんは好きですか、"),("horror movies?","ホラー映画が。")],"like"),
     plain("Love,","愛をこめて、"),plain("Mark","マーク")],
    [plain("From: Agnes Marshall","差出人：アグネス・マーシャル"),plain("To: Mark Marshall","宛先：マーク・マーシャル"),
     plain("Date: October 12","日付：10月12日"),plain("Subject: The movies","件名：映画")],
    [plain("Hello Mark,","マークへ、"),
     row([("Your grandfather doesn't like","あなたのおじいちゃんは好きではありません、"),("horror movies.","ホラー映画が。")],"like"),
     row([("He likes comedy movies","おじいちゃんはコメディー映画が好きです、"),("and science fiction movies,","それにSF映画も。"),("but he likes action movies","でもアクション映画が好きです、"),("the best.","いちばん。")],"likes"),
     row([("There's a new action movie","新しいアクション映画があります、"),("at the Georgetown Theater.","ジョージタウン劇場に。")],"'s"),
     row([("You should watch","あなたたちは見るといいですよ、"),("that.","それを。")],"watch"),
     row([("I'll take you","私があなたたちを連れて行きます、"),("to the Georgetown Theater","ジョージタウン劇場まで、"),("in my car.","私の車で。")],"take"),
     row([("Please take the bus","バスに乗ってください、"),("when you go home.","家に帰るときは。")],"take"),
     plain("Love,","愛をこめて、"),plain("Grandma","おばあちゃん")],
]

ARTICLE=[
    [row([("Sally is","サリーは"),("in high school.","高校生です。")],"is"),
     row([("A few months ago,","数か月前、"),("she talked","サリーは話をしました、"),("to her science teacher.","理科の先生と。")],"talked"),
     row([("He said,","先生は言いました、"),("\"What are your plans","「あなたの計画は何ですか、"),("for the future?\"","将来の」と。")],"said"),
     row([("Sally said,","サリーは言いました、"),("\"I want to be a nurse.\"","「看護師になりたいです」と。")],"said"),
     row([("Her teacher said,","先生は言いました、"),("\"You should be a volunteer","「ボランティアをするといいですよ、"),("at the hospital.","病院で。"),("You can learn many things there.\"","そこではたくさんのことが学べます」と。")],"said")],
    [row([("Sally's uncle works","サリーのおじは働いています、"),("at the hospital.","その病院で。")],"works"),
     row([("Last month,","先月、"),("Sally asked him,","サリーはおじに尋ねました、"),("\"Can I be a volunteer","「ボランティアをしてもいいですか、"),("at the hospital?\"","病院で」と。")],"asked"),
     row([("He said,","おじは言いました、"),("\"Of course.\"","「もちろん」と。")],"said"),
     row([("Sally started working","サリーは働き始めました、"),("as a volunteer","ボランティアとして"),("there","そこで、"),("last week.","先週。")],"started"),
     row([("She takes food","サリーは食べ物を運びます、"),("from the kitchen","キッチンから"),("to the people in the hospital.","病院にいる人たちのところへ。")],"takes"),
     row([("She also talks","サリーは話もします、"),("with them.","その人たちと。")],"talks"),
     row([("Some of them","その人たちの何人かは"),("are children.","子どもです。")],"are"),
     row([("They look happy","子どもたちはうれしそうです、"),("when they talk to Sally.","サリーと話すとき。")],"look")],
    [row([("Sally likes","サリーは気に入っています、"),("her volunteer job.","ボランティアの仕事を。")],"likes"),
     row([("She asks the nurses questions,","サリーは看護師たちに質問をします、"),("and they tell her","すると看護師たちはサリーに話してくれます、"),("about their jobs.","自分たちの仕事について。")],"asks"),
     row([("She likes talking","サリーは話すことが好きです、"),("with the children","子どもたちと"),("the best.","いちばん。")],"likes"),
     row([("Yesterday,","昨日、"),("one girl said,","ある女の子が言いました、"),("\"You'll be a great nurse, Sally.\"","「サリー、あなたはすばらしい看護師になるよ」と。")],"said"),
     row([("Next year,","来年、"),("Sally will go to college","サリーは大学に進みます、"),("to become a nurse.","看護師になるために。")],"will")],
]

# Full translations read naturally; bilingual slash units retain English order.
for block,translations in [(NOTICE[1],["ジョギングに興味はありますか。"]),
    (NOTICE[2],["生徒は、午前8時に学校が始まる前に、学校の体育館でジョギングができます。",
                "20分間、体育館の中を走りながら音楽を聞くことができます！","先生たちが、飲み物のジュースを持ってきてくれます。"]),
    (NOTICE[3],["参加したい人は、午前7時30分に学校の体育館に来てください。"]),
    (EMAIL[1],["おばあちゃんへ、","土曜日のおじいちゃんの誕生日に、何かしたいと思っています。",
               "最初はおじいちゃんを動物園に連れて行きたかったのですが、土曜日は雨が降りそうです。",
               "だから、おじいちゃんを映画に連れて行きます！","サプライズになります。",
               "ジョージタウン劇場へは、バスと電車のどちらで行けばいいですか。","それから、おじいちゃんはホラー映画が好きですか。",
               "愛をこめて、","マーク"]),
    (EMAIL[3],["マークへ、","おじいちゃんはホラー映画が好きではありません。",
               "コメディー映画やSF映画も好きですが、いちばん好きなのはアクション映画です。",
               "ジョージタウン劇場で新しいアクション映画をやっています。","それを見るといいですよ。",
               "私の車で、ジョージタウン劇場まで連れて行ってあげます。","家に帰るときは、バスに乗ってください。",
               "愛をこめて、","おばあちゃん"]),
    (ARTICLE[0],["サリーは高校生です。","数か月前、サリーは理科の先生と話をしました。",
                 "先生は「将来の計画は何ですか」と言いました。","サリーは「看護師になりたいです」と言いました。",
                 "先生は「病院でボランティアをするといいですよ。そこではたくさんのことが学べます」と言いました。"]),
    (ARTICLE[1],["サリーのおじは、その病院で働いています。","先月、サリーはおじに「病院でボランティアをしてもいいですか」と尋ねました。",
                 "おじは「もちろん」と言いました。","サリーは先週、そこでボランティアとして働き始めました。",
                 "サリーはキッチンから、病院にいる人たちのところへ食べ物を運びます。","その人たちと話もします。",
                 "その中には子どもたちもいます。","子どもたちは、サリーと話すときうれしそうです。"]),
    (ARTICLE[2],["サリーはボランティアの仕事が気に入っています。",
                 "サリーが看護師たちに質問をすると、看護師たちは自分の仕事について話してくれます。",
                 "サリーは子どもたちと話すのがいちばん好きです。",
                 "昨日、ある女の子が「サリー、あなたはすばらしい看護師になるよ」と言いました。",
                 "来年、サリーは看護師になるために大学に進みます。"]),
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
    passage("4A","Jogging in the Gym",NOTICE,[
        question(26,"What time should students arrive at the school gym?","生徒は何時に学校の体育館に着くべきですか。",
                 ["At 7:00 a.m.","At 7:20 a.m.","At 7:30 a.m.","At 8:00 a.m."],
                 ["午前7時に。","午前7時20分に。","午前7時30分に。","午前8時に。"],3,
                 ["If you want to join, please arrive at the school gym at 7:30 a.m."],
                 "質問の arrive at the school gym（学校の体育館に着く）は、掲示の最後の文と同じ表現。参加したい人は午前7時30分に来るように書かれている。8:00 a.m. は学校が始まる時刻で、体育館に着く時刻ではない。7時・7時20分は掲示に書かれていない。",
                 "さいごのぶんに『ごぜん7じ30ぷんにきてね』とあるよ。8じは、がっこうがはじまるじかんだね。",
                 ["午前7時は掲示に書かれていない。","午前7時20分は掲示に書かれていない。","参加する人が体育館に着く時刻に一致する。","午前8時は学校が始まる時刻で、体育館に着く時刻ではない。"],
                 ["7じとは、かいていないよ。","7じ20ぷんとは、かいていないよ。","7じ30ぷんにいくんだね。","8じは、がっこうがはじまるじかんだよ。"]),
        question(27,"What will teachers do?","先生たちは何をしますか。",
                 ["Clean the school for 20 minutes.","Jog to school.","Sing some songs.","Bring juice to the gym."],
                 ["20分間、学校を掃除する。","学校までジョギングする。","歌を何曲か歌う。","体育館にジュースを持ってくる。"],4,
                 ["Teachers will bring juice to drink."],
                 "Teachers will ～ の文を探す。先生たちは飲むためのジュースを持ってくる。20 minutes は生徒が体育館で走りながら音楽を聞ける時間で、掃除の時間ではない。学校までジョギングする話や、歌を歌う話は書かれていない。",
                 "せんせいたちは、のみもののジュースをもってきてくれるよ。20ぷんは、はしるじかんだね。",
                 ["20分は生徒が体育館で走る時間で、掃除の話はない。","ジョギングするのは体育館の中で、学校までではない。","歌を歌うとは書かれていない。音楽は走りながら聞くもの。","Teachers will bring juice to drink. に一致する。"],
                 ["そうじのはなしは、ないよ。","はしるのは、たいいくかんのなかだよ。","うたをうたう、とはかいていないよ。","ジュースをもってきてくれるね。"]),
    ],"掲示",26,27),
    passage("4B","Grandpa's birthday / The movies",EMAIL,[
        question(28,"What did Mark want to do on Saturday?","マークは土曜日に何をしたかったのですか。",
                 ["Go cycling with his grandfather.","Go to a train museum.","Take his grandfather to the zoo.","Make a birthday cake."],
                 ["祖父とサイクリングに行く。","電車の博物館に行く。","祖父を動物園に連れて行く。","誕生日ケーキを作る。"],3,
                 ["First, I wanted to take him to the zoo, but it'll rain on Saturday."],
                 "質問は did ... want と過去のことを尋ねている。1通目に First, I wanted to take him to the zoo（最初はおじいちゃんを動物園に連れて行きたかった）とあり、him は Grandpa のこと。雨が降りそうなので映画に変えたが、もともとしたかったのは動物園。サイクリング・電車の博物館・ケーキは本文に出てこない。",
                 "マークは、はじめはおじいちゃんをどうぶつえんにつれていきたかったよ。あめがふりそうなので、えいがにかえたんだね。",
                 ["サイクリングの話は本文にない。","train は劇場への行き方として出てくるだけで、博物館の話はない。","最初にしたかったこととして書かれている。","ケーキを作る話は本文にない。"],
                 ["サイクリングは、でてこないよ。","でんしゃのはくぶつかんは、でてこないよ。","どうぶつえんにつれていきたかったね。","ケーキは、でてこないよ。"]),
        question(29,"What kind of movies does Mark's grandfather like the best?","マークの祖父はどんな種類の映画がいちばん好きですか。",
                 ["Horror movies.","Comedy movies.","Science fiction movies.","Action movies."],
                 ["ホラー映画。","コメディー映画。","SF映画。","アクション映画。"],4,
                 ["He likes comedy movies and science fiction movies, but he likes action movies the best."],
                 "質問の the best（いちばん）が本文と対応する。コメディー映画とSF映画も好きだが、but の後ろで『アクション映画がいちばん好き』と言っている。ホラー映画は doesn't like（好きではない）と書かれている。",
                 "コメディーやSFもすきだけど、いちばんすきなのはアクションえいが。ホラーはすきではないよ。",
                 ["doesn't like horror movies とあり、好きではない。","好きだが、いちばん好きなものではない。","好きだが、いちばん好きなものではない。","but の後ろで the best と言っている。"],
                 ["ホラーは、すきではないよ。","すきだけど、いちばんではないよ。","すきだけど、いちばんではないよ。","いちばんすきなのはアクションだね。"]),
        question(30,"How will Mark and his grandfather go to the Georgetown Theater?","マークと祖父はどうやってジョージタウン劇場へ行きますか。",
                 ["By train.","By car.","By bus.","On foot."],
                 ["電車で。","車で。","バスで。","歩いて。"],2,
                 ["I'll take you to the Georgetown Theater in my car."],
                 "2通目で祖母が I'll take you to the Georgetown Theater in my car.（私の車で劇場まで連れて行く）と書いている。you はマークとおじいちゃん。バスは家に帰るとき（when you go home）に乗るもの。電車はマークが1通目で尋ねた行き方の一つで、祖母の答えではない。歩いて行く話はない。",
                 "おばあちゃんが、くるまでげきじょうまでつれていってくれるよ。バスは、かえるときにのるんだね。",
                 ["電車はマークが尋ねただけで、祖母の答えは車。","祖母の車で劇場まで連れて行ってもらう。","バスは家に帰るときに乗るもの。","歩いて行くとは書かれていない。"],
                 ["でんしゃではないよ。","おばあちゃんのくるまでいくね。","バスは、かえるときだよ。","あるいていく、とはかいていないよ。"]),
    ],"Eメール",28,30),
    passage("4C","Helping People",ARTICLE,[
        question(31,"What does Sally want to be in the future?","サリーは将来何になりたいのですか。",
                 ["A doctor.","A high school teacher.","A nurse.","A scientist."],
                 ["医者。","高校の先生。","看護師。","科学者。"],3,
                 ["Sally said, \"I want to be a nurse.\""],
                 "want to be ～で『～になりたい』。先生に将来の計画を聞かれ、サリーは I want to be a nurse. と答えている。最後の文の to become a nurse（看護師になるために）も同じ内容。高校に通っているのはサリー自身で、理科の先生は話をした相手。",
                 "サリーは『かんごしになりたい』といっているよ。nurse は『かんごし』だね。",
                 ["医者になりたいとは書かれていない。","サリーは高校生で、高校の先生になりたいとは書かれていない。","I want to be a nurse. に一致する。","科学者は本文に出てこない。理科の先生は話をした相手。"],
                 ["いしゃではないよ。","こうこうのせんせいではないよ。","かんごしになりたいんだね。","かがくしゃではないよ。"]),
        question(32,"When did Sally start working as a volunteer?","サリーはいつボランティアとして働き始めましたか。",
                 ["Yesterday.","Last week.","Last month.","A few months ago."],
                 ["昨日。","先週。","先月。","数か月前。"],2,
                 ["Sally started working as a volunteer there last week."],
                 "start working as a volunteer が本文と同じ表現。時を表す語句が多いので順に整理する。数か月前に先生と話し、先月おじに頼み、先週ボランティアとして働き始めた。昨日は女の子に声をかけられた日。",
                 "すうかげつまえにせんせいとはなし、せんげつおじさんにたのみ、せんしゅうはたらきはじめたよ。",
                 ["昨日は女の子に『すばらしい看護師になるよ』と言われた日。","started working as a volunteer there last week に一致する。","先月はおじにボランティアができるか尋ねた時。","数か月前は理科の先生と話をした時。"],
                 ["きのうは、おんなのこにいわれたひだよ。","せんしゅう、はじめたね。","せんげつは、おじさんにたのんだときだよ。","すうかげつまえは、せんせいとはなしたときだよ。"]),
        question(33,"What does Sally do at the hospital?","サリーは病院で何をしていますか。",
                 ["She takes food to people.","She washes the dishes.","She cleans the kitchen.","She writes reports for her uncle."],
                 ["人々に食べ物を運ぶ。","皿を洗う。","キッチンを掃除する。","おじのために報告書を書く。"],1,
                 ["She takes food from the kitchen to the people in the hospital."],
                 "本文の She takes food from the kitchen to the people in the hospital. を短くしたのが選択肢1。take A to B で『A を B へ持って行く・運ぶ』。kitchen は食べ物を運び出す場所として出てくるだけで、皿洗いや掃除をするとは書かれていない。おじは病院で働いているが、報告書の話はない。",
                 "サリーは、キッチンからびょういんのひとたちに、たべものをはこぶよ。おさらあらいやそうじではないね。",
                 ["takes food ... to the people に一致する。","皿を洗うとは書かれていない。","キッチンは食べ物を運び出す場所で、掃除するとは書かれていない。","報告書を書く話は本文にない。"],
                 ["たべものをはこぶんだね。","おさらあらいは、でてこないよ。","キッチンのそうじは、でてこないよ。","ほうこくしょのはなしは、でてこないよ。"]),
        question(34,"What does Sally like the best about her volunteer job?","サリーはボランティアの仕事について何がいちばん好きですか。",
                 ["Telling stories to the nurses.","Working with her uncle.","Cooking in the kitchen.","Talking with the children."],
                 ["看護師たちに物語を話すこと。","おじと一緒に働くこと。","キッチンで料理をすること。","子どもたちと話すこと。"],4,
                 ["She likes talking with the children the best."],
                 "質問の the best（いちばん）が本文と対応する。She likes talking with the children the best. とある。看護師にはサリーが質問をして、看護師が仕事について話してくれるので、選択肢1は話す人が逆。おじと働くことや料理をすることは書かれていない。",
                 "サリーがいちばんすきなのは、こどもたちとはなすこと。かんごしさんには、しつもんをしているね。",
                 ["看護師には質問をする側で、物語を話すとは書かれていない。","おじと一緒に働くとは書かれていない。","料理をするとは書かれていない。","She likes talking with the children the best. に一致する。"],
                 ["かんごしさんには、しつもんをしているよ。","おじさんといっしょに、ではないよ。","りょうりは、でてこないよ。","こどもたちとはなすのが、いちばんすきだね。"]),
        question(35,"What will Sally do next year?","サリーは来年何をしますか。",
                 ["Go to college.","Join a science club.","Write a book for children.","Become a teacher."],
                 ["大学に行く。","科学部に入る。","子ども向けの本を書く。","教師になる。"],1,
                 ["Next year, Sally will go to college to become a nurse."],
                 "質問の next year が本文の最後の文と対応する。Sally will go to college to become a nurse.（看護師になるために大学に進む）とあり、to become a nurse は大学へ行く目的。科学部や本の話はなく、なりたいのは教師ではなく看護師。",
                 "らいねん、サリーはかんごしになるために、だいがくにいくよ。せんせいになるのではないね。",
                 ["will go to college に一致する。","科学部に入るとは書かれていない。","本を書くとは書かれていない。","なりたいのは看護師で、教師ではない。"],
                 ["だいがくにいくんだね。","かがくぶは、でてこないよ。","ほんをかく、とはかいていないよ。","なりたいのは、かんごしだよ。"]),
    ],"英文",31,35),
]

PASSAGES[0]["format"]="notice"
PASSAGES[1]["format"]="multi-email"
PASSAGES[1]["emails"]=[]
for i in (0,2):
    meta={line.partition(":")[0].lower():line.partition(":")[2].strip() for line in PASSAGES[1]["paragraphs"][i].splitlines()}
    PASSAGES[1]["emails"].append(dict(meta=meta,body=PASSAGES[1]["paragraphs"][i+1],translation=PASSAGES[1]["translations"][i+1]))

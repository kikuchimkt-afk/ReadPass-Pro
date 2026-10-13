"""Complete, explicitly aligned reading text; never split Ms./a.m. by regex."""

def row(ja,verb,*units):
    return [" ".join(a for a,b in units),ja,"||".join(a+"|"+b for a,b in units),verb]
def plain(en,ja):return row(ja,"",(en,ja))
# Sentence meanings end in 。; the analysis adds its own, so it is not doubled.
def question(n,stem,ja,choices,meanings,answer,evidence,note,simple,reasons,easy):
    return dict(number=n,question=stem,questionTranslation=ja,choices=choices,choiceTranslations=meanings,
                answer=answer,sourceEvidence=evidence,grammar=f"本文の根拠は「{' / '.join(evidence)}」。{note}",grammarSimple=simple,
                choiceAnalysis=[("○ " if i==answer else "")+f"{c}＝{t.rstrip('。')}。{r}" for i,(c,t,r) in enumerate(zip(choices,meanings,reasons),1)],
                choiceAnalysisSimple=[("○ " if i==answer else "")+f"{t.rstrip('。')}。{r}" for i,(t,r) in enumerate(zip(meanings,easy),1)])

NOTICE=[
    [plain("Notice about Social Studies Homework","社会科の宿題についてのお知らせ"),
     row("次の水曜日の社会科の授業までに、レポートを書いてください。","write",("Please write a report","レポートを書いてください、"),("by next Wednesday's social studies class!","次の水曜日の社会科の授業までに。"))],
    [row("生徒は一人ずつ、今週の土曜日か日曜日に工場、博物館、農場、駅のいずれかを訪れ、そこで働く人にインタビューしてください。","should",("Each student should visit","生徒は一人ずつ訪れてください、"),("a factory, museum, farm, or station","工場、博物館、農場、駅のいずれかを、"),("this Saturday or Sunday","今週の土曜日か日曜日に、"),("and interview the workers.","そしてそこで働く人にインタビューしてください。")),
     row("自分の好きな場所を選びましょう。","Choose",("Choose","選びましょう、"),("your favorite place!","自分の好きな場所を。")),
     row("訪問する前に、必ず事務所に電話をして、インタビューをしたいことを職員に伝えてください。","must",("Before visiting,","訪問する前に、"),("you must call the office","事務所に電話しなければなりません、"),("and tell the staff","そして職員に伝えなければなりません、"),("that you would like to interview them.","インタビューをしたいということを。"))],
    [row("インタビューでは、次の質問をしてください。","should",("During the interviews,","インタビューの間、"),("you should ask the following questions:","次の質問をしてください。"))],
    [row("毎日の仕事では何をしていますか。","do",("What do you do","何をしていますか、"),("in your daily work?","毎日の仕事で。")),
     row("仕事で最も難しいところは何ですか。","is",("What is","何ですか、"),("the most difficult part of your work?","仕事で最も難しいところは。"))],
    [row("質問がある場合は、今週の木曜日にホワイト先生のところへ来てください。","visit",("If you have any questions,","もし質問があれば、"),("please visit Ms. White","ホワイト先生のところへ来てください、"),("this Thursday.","今週の木曜日に。")),
     row("ただし、今週は午前中は先生が不在なので、午後に来てください。","is",("However,","ただし、"),("she is absent in the morning this week,","今週、先生は午前中は不在です、"),("so visit her in the afternoon!","だから午後に先生を訪ねてください。"))],
]

EMAIL=[
    [plain("Dear Grandpa,","おじいちゃんへ、"),
     row("今日は弟のダニエルと一緒におじいちゃんの家へ行きたかったけど、ダニエルとは一緒に行けないんだ。","wanted",("I wanted to go to your house today","今日おじいちゃんの家へ行きたかったんだ、"),("with my younger brother Daniel,","弟のダニエルと一緒に、"),("but I can't go with him.","でもダニエルとは一緒に行けないんだ。")),
     row("今朝、けんかしたんだ。","fought",("We fought","ぼくたちはけんかしたんだ、"),("this morning!","今朝。")),
     row("けんかの原因は、ぼくたちの大好きなテレビゲームのことだったんだ。","was",("Our fight was","ぼくたちのけんかは、"),("about our favorite video game.","大好きなテレビゲームのことだったんだ。")),
     row("ダニエルが宿題をしなかったのでお母さんも怒って、ダニエルは1時間前に宿題を終わらせるために図書館へ行ったんだ。","got",("Mom also got angry","お母さんも怒ったんだ、"),("because Daniel didn't do his homework,","ダニエルが宿題をしなかったから、"),("so he went to the library to finish it","だから彼は宿題を終わらせるために図書館へ行ったんだ、"),("an hour ago!","1時間前に。")),
     row("ぼく一人でおじいちゃんの家へ行ってもいいかな。","Can",("Can I go to your house","おじいちゃんの家へ行ってもいいかな、"),("alone?","一人で。")),
     row("今日の午後は家にいるかな。","Are",("Are you at home","家にいるかな、"),("this afternoon?","今日の午後は。")),
     row("今日はバスでおじいちゃんの家へ行けるよ。","can",("I can go to your house","おじいちゃんの家へ行けるよ、"),("by bus today!","今日はバスで。")),
     plain("Write soon,","お返事待ってるね、"),plain("Alex","アレックス")],
    [plain("Dear Alex,","アレックスへ、"),
     row("みんな大丈夫かい。","Is",("Is everyone","みんな、"),("OK?","大丈夫かい。")),
     row("みんなが楽しく過ごしているといいね。","hope",("I hope","願っているよ、"),("you're all happy.","みんなが楽しく過ごしていることを。")),
     row("ちょうどダニエルからメールが届いたところだよ。","received",("I've just received an email","ちょうどメールを受け取ったところだよ、"),("from Daniel.","ダニエルから。")),
     row("ダニエルは、きみとお母さんに悪かったと思っているようだね。","think",("I think","思うよ、"),("he feels sorry for you and your mom.","ダニエルはきみとお母さんに悪かったと感じていると。")),
     row("ダニエルは今日中に宿題が終わると思っているそうだから、明日ダニエルと一緒にうちへ来たらどうだい。","thinks",("Daniel also thinks","ダニエルは思っているそうだ、"),("he'll finish his homework today,","今日宿題を終えるだろうと、"),("so why don't you come to my house","だから、うちへ来たらどうだい、"),("with him tomorrow?","明日ダニエルと一緒に。")),
     row("それに、きみはいつも自転車でうちへ来るよね。","come",("Also,","それに、"),("you always come to my house by bike,","きみはいつも自転車でうちへ来るね、"),("right?","そうだよね。")),
     row("今日はどうしてバスで来たいんだい。","do",("Why do you want to come here","どうしてここへ来たいんだい、"),("by bus today?","今日はバスで。")),
     row("今日は家にいるけれど、明日来るなら、おばあちゃんがフルーツケーキを作ってくれるよ。","will",("I'm at home today,","今日は家にいるよ、"),("but if you come tomorrow,","でも明日来るなら、"),("your grandma will make a fruitcake.","おばあちゃんがフルーツケーキを作ってくれるよ。")),
     row("みんなで一緒に食べられるね。","can",("We can eat it","それを食べられるね、"),("together!","みんなで一緒に。")),
     row("明日の朝、友達の一人がたくさんの果物をくれるんだ。","will",("One of my friends","友達の一人が、"),("will give me many fruits","私にたくさんの果物をくれるんだ、"),("tomorrow morning!","明日の朝に。")),
     plain("Keep in touch,","また連絡してね、"),plain("Grandpa","おじいちゃん")],
    [plain("Dear Grandpa,","おじいちゃんへ、"),
     row("ダニエルのことを教えてくれてありがとう。","Thank",("Thank you","ありがとう、"),("for telling me about Daniel.","ダニエルのことを教えてくれて。")),
     row("ダニエルが図書館から帰ってきたら、ごめんねって言うよ。","say",("When he comes home from the library,","ダニエルが図書館から帰ってきたら、"),("I'll say sorry to him!","ごめんねって言うよ。")),
     row("わかった、今日はおじいちゃんの家へ行かないよ。","go",("OK,","わかった、"),("I won't go to your house today.","今日はおじいちゃんの家へ行かないよ。")),
     row("その代わりに、明日の午後にダニエルと一緒に行くね。","visit",("I'll visit you with Daniel","ダニエルと一緒におじいちゃんのところへ行くね、"),("tomorrow afternoon instead.","その代わりに明日の午後に。")),
     row("うん、おばあちゃんのフルーツケーキが食べたいな。","want",("Yes,","うん、"),("I want to eat Grandma's fruitcake!","おばあちゃんのフルーツケーキが食べたいな。")),
     row("ダニエルも喜ぶよ。","will",("Daniel will be","ダニエルは、"),("happy, too!","同じように喜ぶよ。")),
     row("ところで今、ぼくの自転車はどこか調子が悪いんだ。","is",("Now,","ところで今、"),("something is wrong with my bike.","ぼくの自転車はどこか調子が悪いんだ。")),
     row("だから、明日の朝、お父さんと一緒に庭で自転車を直すんだ。","fix",("So,","だから、"),("I'll fix it with Dad","お父さんと一緒に自転車を直すんだ、"),("in the garden tomorrow morning!","明日の朝に庭で。")),
     row("たぶん、お昼までには直し終わると思う。","finish",("Maybe we'll finish fixing it","たぶん直し終わるよ、"),("by noon.","お昼までには。")),
     plain("See you tomorrow,","また明日ね、"),plain("Alex","アレックス")],
]
META=[dict(from_="Alex Long",to="Ben Long",date="June 15",subject="My brother Daniel"),
      dict(from_="Ben Long",to="Alex Long",date="June 15",subject="Are you OK?"),
      dict(from_="Alex Long",to="Ben Long",date="June 15",subject="OK!")]
for meta in META:meta["from"]=meta.pop("from_")
HEADERS=[[plain(f"From: {m['from']}",f"差出人：{['アレックス・ロング','ベン・ロング','アレックス・ロング'][i]}"),
          plain(f"To: {m['to']}",f"宛先：{['ベン・ロング','アレックス・ロング','ベン・ロング'][i]}"),
          plain(f"Date: {m['date']}","日付：6月15日"),
          plain(f"Subject: {m['subject']}",f"件名：{['弟のダニエル','大丈夫かい？','わかったよ！'][i]}")] for i,m in enumerate(META)]

ARTICLE=[
    [row("ハイイロオオカミは、北アメリカ、ヨーロッパ、アジアなどの地域で見られる動物です。","is",("The gray wolf is an animal","ハイイロオオカミは動物です、"),("that can be found","見られる、"),("in North America, Europe, Asia, and other areas.","北アメリカ、ヨーロッパ、アジアやその他の地域で。")),
     row("ハイイロオオカミは、森や雪の多い場所などに住んでいます。","live",("Gray wolves live","ハイイロオオカミは住んでいます、"),("in forests, snowy places, and other places.","森や雪の多い場所、その他の場所に。")),
     row("ハイイロオオカミはかつてアメリカ合衆国全体に住んでいましたが、最近では、ほとんどのハイイロオオカミが北アメリカの北部地域にしか住んでいません。","used",("Gray wolves used to live all across the United States,","ハイイロオオカミはかつてアメリカ合衆国全体に住んでいました、"),("but recently,","しかし最近では、"),("most gray wolves have only lived in the northern areas of North America.","ほとんどのハイイロオオカミが北アメリカの北部地域にしか住んでいません。")),
     row("1970年代には、アメリカ合衆国の南部地域に住むハイイロオオカミはわずか数百頭でした。","lived",("In the 1970s,","1970年代には、"),("only a few hundred gray wolves lived","わずか数百頭のハイイロオオカミしか住んでいませんでした、"),("in the southern area of the United States.","アメリカ合衆国の南部地域には。"))],
    [row("ハイイロオオカミがいなくなった主な理由は、人間に狩られたことです。","is",("The main reason the gray wolves disappeared","ハイイロオオカミがいなくなった主な理由は、"),("is that they were hunted by humans.","人間に狩られたことです。")),
     row("1800年代、人々はアメリカ合衆国の西部地域に移り住み、家を建てるために木を切り倒しました。","went",("In the 1800s,","1800年代、"),("humans went to live in the western areas of the United States","人間はアメリカ合衆国の西部地域へ移り住みました、"),("and cut down trees to build houses.","そして家を建てるために木を切り倒しました。")),
     row("そのため、ハイイロオオカミはすみかを失い、人間の家に近い新しい場所へ移らなければなりませんでした。","lost",("Therefore,","そのため、"),("the gray wolves lost their homes","ハイイロオオカミはすみかを失いました、"),("and had to go to new places close to humans' houses.","そして人間の家に近い新しい場所へ移らなければなりませんでした。")),
     row("オオカミたちは、人々のペットや農場の動物を食べました。","ate",("They ate people's pets","彼らは人々のペットを食べました、"),("or animals on people's farms.","あるいは人々の農場の動物を。")),
     row("人間はこれを嫌がり、ハイイロオオカミを狩りました。","did",("Humans did not like this,","人間はこれを好みませんでした、"),("so they hunted the gray wolves.","だからハイイロオオカミを狩りました。")),
     row("その結果、ハイイロオオカミの数は減りました。","decreased",("Then,","その結果、"),("the number of gray wolves decreased.","ハイイロオオカミの数は減りました。"))],
    [row("このことが、1900年代に新しい問題を生みました。","created",("This created a new problem","このことが新しい問題を生みました、"),("in the 1900s.","1900年代に。")),
     row("ハイイロオオカミは、もともと森の動物を食べていました。","ate",("Gray wolves originally ate","ハイイロオオカミはもともと食べていました、"),("animals in the forests.","森の動物を。")),
     row("しかし、ハイイロオオカミが少なくなったため、ほかの動物がより長く生きるようになりました。","lived",("However,","しかし、"),("because there were fewer gray wolves,","ハイイロオオカミが少なくなったので、"),("other animals lived longer.","ほかの動物がより長く生きるようになりました。")),
     row("これらの動物は、たくさんの植物を食べました。","ate",("These animals ate","これらの動物は食べました、"),("many plants.","たくさんの植物を。")),
     row("人々は、ハイイロオオカミが植物を食べる動物を食べることで、森を助けていたことに気づきました。","realized",("People realized","人々は気づきました、"),("gray wolves helped the forests","ハイイロオオカミが森を助けていたことに、"),("by eating the animals that ate the plants.","植物を食べる動物を食べることによって。"))],
    [row("1974年、アメリカ政府は新しい規則を作りました。","made",("In 1974,","1974年、"),("the American government made a new rule.","アメリカ政府は新しい規則を作りました。")),
     row("その規則は、誰もハイイロオオカミを殺したり傷つけたりしてはいけないと定めていました。","said",("The rule said","その規則は定めていました、"),("no one could kill or hurt gray wolves.","誰もハイイロオオカミを殺したり傷つけたりしてはいけないと。")),
     row("このおかげで、わずか40年で、アメリカ南部の地域ではハイイロオオカミの数が増えました。","grew",("Because of this,","このおかげで、"),("in just forty years,","わずか40年で、"),("the population of gray wolves grew","ハイイロオオカミの数が増えました、"),("in the southern areas of America.","アメリカ南部の地域で。")),
     row("ハイイロオオカミは、環境を大いに助けました。","helped",("The gray wolves helped","ハイイロオオカミは助けました、"),("the environment a lot.","環境を大いに。")),
     row("ほかの動物の数は減り、植物の数は増えました。","decreased",("The number of other animals decreased,","ほかの動物の数は減りました、"),("and the number of plants increased.","そして植物の数は増えました。"))],
]

NOTICE_Q=[
    question(21,"During the interviews, each student should ask the workers about their daily work and","インタビューの間、生徒は一人ずつ、働く人に毎日の仕事と何について尋ねるべきですか。",
             ["their favorite part of their work.","their favorite place in the city.","the food they eat after work.","the hardest part of their work."],
             ["仕事で好きなところ。","市内で好きな場所。","仕事の後に食べる食べ物。","仕事で最も大変なところ。"],4,
             ["During the interviews, you should ask the following questions:","What is the most difficult part of your work?"],
             "二つの質問のうち、daily work でない方は most difficult part。most difficult が hardest に言い換えられている。favorite は訪問先を選ぶ場面の語で、質問の内容ではない。",
             "インタビューでは、しごとでいちばんむずかしいところをきくよ。most difficult と hardest は、おなじいみだね。すきなばしょは、いくところをえらぶはなしだよ。",
             ["聞くのは好きなところでなく、最も難しいところ。","favorite place は訪問先を選ぶ話で、質問ではない。","仕事の後の食事については書かれていない。","most difficult を hardest と言い換えている。"],
             ["すきなところではなく、むずかしいところだよ。","すきなばしょは、いくところのはなしだよ。","たべもののしつもんは、かいていないよ。","いちばんむずかしいところを、きくんだね。"]),
    question(22,"When should the students visit Ms. White if they have any questions?","質問がある場合、生徒はいつホワイト先生のところへ行けばよいですか。",
             ["This Thursday afternoon.","This Saturday morning.","This Sunday morning.","Next Wednesday afternoon."],
             ["今週の木曜日の午後。","今週の土曜日の午前。","今週の日曜日の午前。","次の水曜日の午後。"],1,
             ["If you have any questions, please visit Ms. White this Thursday.","However, she is absent in the morning this week, so visit her in the afternoon!"],
             "this Thursday で曜日、visit her in the afternoon で時間帯がわかる。二つの文を組み合わせて答える。今週の午前は先生が不在。土曜日と日曜日は見学に行く日、次の水曜日はレポートを出す授業の日。",
             "しつもんがあるときは、こんしゅうのもくようびのごごにいくよ。せんせいは、ごぜんはいないんだね。すいようびは、レポートをだすひだよ。",
             ["this Thursday と afternoon を合わせた答え。","土曜日は見学に行く日で、先生は午前中不在。","日曜日も見学に行く日で、先生を訪ねる日ではない。","次の水曜日はレポートを出す授業の日。"],
             ["もくようびのごごに、いくんだね。","どようびは、けんがくにいくひだよ。","にちようびも、けんがくにいくひだよ。","すいようびは、レポートをだすひだよ。"]),
]
EMAIL_Q=[
    question(23,"This morning, Alex and Daniel","今朝、アレックスとダニエルは何をしましたか。",
             ["missed the bus to the library.","fought about their homework.","fought about a video game.","got a new video game."],
             ["図書館行きのバスに乗り遅れた。","宿題のことでけんかした。","テレビゲームのことでけんかした。","新しいテレビゲームを手に入れた。"],3,
             ["We fought this morning!","Our fight was about our favorite video game."],
             "第1のメールの差出人は Alex。fought this morning のけんかの内容は、次の文の favorite video game。宿題はダニエルが母親に怒られた理由で、けんかの原因ではない。図書館へはダニエルが宿題をしに行った。",
             "アレックスとダニエルは、けさ、すきなテレビゲームのことでけんかしたよ。しゅくだいは、おかあさんがおこったりゆうだね。",
             ["図書館へ行ったのはダニエルで、バスの話ではない。","宿題は母親が怒った理由で、けんかの原因ではない。","けんかの内容は favorite video game と一致。","新しいゲームを手に入れたとは書かれていない。"],
             ["バスにのりおくれたとは、かいていないよ。","しゅくだいは、おかあさんがおこったりゆうだよ。","すきなテレビゲームのことで、けんかしたね。","あたらしいゲームをかったのではないよ。"]),
    question(24,"Who will receive some fruits tomorrow morning?","明日の朝、果物を受け取るのは誰ですか。",
             ["Alex's grandfather.","Alex's mother.","Alex's father.","Alex's friend."],
             ["アレックスの祖父。","アレックスの母親。","アレックスの父親。","アレックスの友達。"],1,
             ["One of my friends will give me many fruits tomorrow morning!"],
             "第2のメールの差出人は祖父の Ben。give me の me は書き手の祖父なので、受け取るのは祖父。my friends の my も祖父を指し、友達は果物をくれる側。give と receive の向きを逆にしないよう注意する。",
             "おじいちゃんのメールの me は、おじいちゃんのことだよ。ともだちがくだものをくれるので、もらうのはおじいちゃんだね。",
             ["give me の me は祖父自身で、受け取る人。","母親は怒った人として出てくるだけ。","父親は明日の朝アレックスと自転車を直す人。","果物をくれるのは祖父の友達で、受け取る側ではない。"],
             ["おじいちゃんが、くだものをもらうんだね。","おかあさんは、くだものをもらわないよ。","おとうさんは、じてんしゃをなおすひとだよ。","ともだちは、くだものをあげるがわだよ。"]),
    question(25,"What will Alex do tomorrow morning?","アレックスは明日の朝、何をしますか。",
             ["He will take a bus to the library.","He will fix his bike with his father.","He will finish his homework.","He will help his mother with cooking."],
             ["バスで図書館へ行く。","父親と自転車を修理する。","宿題を終わらせる。","母親の料理を手伝う。"],2,
             ["Now, something is wrong with my bike.","So, I'll fix it with Dad in the garden tomorrow morning!"],
             "第3のメールの it は前の文の my bike を指す。with Dad が with his father に言い換えられている。図書館へ行ったのはダニエルで、宿題も彼のもの。祖父の家へ行くのは明日の午後なので、午前と区別する。",
             "アレックスは、あしたのあさ、おとうさんとにわでじてんしゃをなおすよ。Dad は father とおなじいみだね。しゅくだいをするのはダニエルだよ。",
             ["バスは今日祖父の家へ行く手段の話で、図書館ではない。","with Dad を with his father と言い換えている。","宿題を終えるのはアレックスでなくダニエル。","料理の手伝いは書かれておらず、ケーキを作るのは祖母。"],
             ["としょかんへいったのは、ダニエルだよ。","おとうさんと、じてんしゃをなおすね。","しゅくだいをするのは、ダニエルだよ。","ケーキをつくるのは、おばあちゃんだよ。"]),
]
ARTICLE_Q=[
    question(26,"The gray wolf","ハイイロオオカミについて、正しいものはどれですか。",
             ["only lives in forests.","does not like cold places.","was kept as a pet.","can be found in Europe."],
             ["森にだけ住んでいる。","寒い場所を好まない。","ペットとして飼われていた。","ヨーロッパで見られる。"],4,
             ["The gray wolf is an animal that can be found in North America, Europe, Asia, and other areas.","Gray wolves live in forests, snowy places, and other places."],
             "can be found in の後に Europe がある。forests だけでなく snowy places にも住むので only は誤りで、寒さを嫌うとも言えない。ペットは人々のもので、オオカミが食べた側。",
             "ハイイロオオカミは、ヨーロッパでもみられるよ。もりだけではなく、ゆきのおおいところにもすんでいるね。",
             ["森のほか、雪の多い場所などにも住む。","雪の多い場所にも住んでおり、合わない。","ペットは人々のもので、オオカミが食べた。","can be found in ... Europe と一致する。"],
             ["もりだけではなく、ゆきのおおいところにもいるよ。","さむいところがきらいとは、かいていないよ。","ペットではなく、ペットをたべてしまったよ。","ヨーロッパでも、みられるね。"]),
    question(27,"Why were gray wolves hunted?","ハイイロオオカミはなぜ狩られたのですか。",
             ["They were too loud.","They ate farm animals.","They went into houses.","They killed plants."],
             ["うるさすぎたから。","農場の動物を食べたから。","家の中に入ったから。","植物を枯らしたから。"],2,
             ["They ate people's pets or animals on people's farms.","Humans did not like this, so they hunted the gray wolves."],
             "this は前の文の、ペットや農場の動物を食べたことを指す。animals on people's farms が farm animals に言い換えられている。オオカミは人の家の近くへ移ったが、家の中に入ったとは書かれていない。",
             "オオカミが、ひとのペットやのうじょうのどうぶつをたべたので、ひとはオオカミをかったよ。farm animals は、のうじょうのどうぶつだね。",
             ["鳴き声の大きさについては書かれていない。","animals on people's farms の言い換え。","家の近くへ移っただけで、家に入ったとは書かれていない。","植物を食べたのはほかの動物で、オオカミではない。"],
             ["うるさいとは、かいていないよ。","のうじょうのどうぶつを、たべたからだね。","いえのちかくで、なかにははいっていないよ。","しょくぶつをたべたのは、ほかのどうぶつだよ。"]),
    question(28,"What was the problem with forests in the 1900s?","1900年代、森にはどのような問題がありましたか。",
             ["Animals ate a lot of plants.","The weather was too cold.","Gray wolves ate all the food there.","Humans used too many trees."],
             ["動物が植物をたくさん食べた。","天気が寒すぎた。","ハイイロオオカミがそこの食べ物をすべて食べた。","人間が木を使いすぎた。"],1,
             ["This created a new problem in the 1900s.","These animals ate many plants."],
             "new problem の中身は後の文にある。オオカミが減ってほかの動物が長生きし、These animals が many plants を食べた。many が a lot of に対応する。木を切ったのは1800年代。",
             "オオカミがへって、ほかのどうぶつがながいきしたよ。そのどうぶつが、しょくぶつをたくさんたべてしまったのが、もんだいだったね。",
             ["many を a lot of と言い換えている。","天候の寒さについては書かれていない。","オオカミは減っており、食べ物を食べ尽くしてはいない。","木を切り倒したのは1800年代の出来事。"],
             ["どうぶつが、しょくぶつをたくさんたべたね。","てんきのはなしは、かいていないよ。","オオカミは、へっていたよ。","きをきったのは、1800ねんだいだよ。"]),
    question(29,"Why did the number of gray wolves grow in the southern areas of America?","アメリカ南部の地域で、ハイイロオオカミの数が増えたのはなぜですか。",
             ["Animals stopped eating them.","A new rule was made.","Humans caught all of them.","They started to eat the plants."],
             ["動物がオオカミを食べなくなったから。","新しい規則が作られたから。","人間がオオカミをすべて捕まえたから。","オオカミが植物を食べ始めたから。"],2,
             ["In 1974, the American government made a new rule.","Because of this, in just forty years, the population of gray wolves grew in the southern areas of America."],
             "this は1974年に政府が作った new rule を指す。made a new rule が受動態 A new rule was made に言い換えられている。規則はオオカミを殺すことも傷つけることも禁じた。",
             "1974ねんに、オオカミをころしたりきずつけたりしてはいけない、というあたらしいきまりができたよ。だからオオカミがふえたんだね。",
             ["オオカミを食べる動物の話は書かれていない。","made a new rule を受動態で言い換えている。","規則でオオカミを殺したり傷つけたりできなくなった。","植物を食べたのはほかの動物で、オオカミではない。"],
             ["オオカミをたべるどうぶつのはなしはないよ。","あたらしいきまりが、つくられたからだね。","きまりで、オオカミをきずつけられなくなったよ。","しょくぶつをたべたのは、ほかのどうぶつだよ。"]),
    question(30,"What is this story about?","この話は何についてですか。",
             ["Animals that eat plants.","Human houses in the 1800s.","An animal that was hunted in the past.","Types of plants in northern areas."],
             ["植物を食べる動物。","1800年代の人間の家。","過去に狩られた動物。","北部地域の植物の種類。"],3,
             ["The gray wolf is an animal that can be found in North America, Europe, Asia, and other areas.","The main reason the gray wolves disappeared is that they were hunted by humans."],
             "題名 Gray Wolves のとおり、ハイイロオオカミが話の中心。人間に狩られて減り、規則で守られて再び増えた経緯を描く。植物を食べる動物や1800年代の家は話の一部で、全体の主題ではない。",
             "このおはなしは、ひとにかられてへったハイイロオオカミのおはなしだよ。きまりでまもられて、またふえたことまでよんだね。",
             ["植物を食べる動物は第3段落の一部の話題。","1800年代の家は、オオカミがすみかを失った理由の一部。","人間に狩られたハイイロオオカミの話全体と一致。","北部地域の植物の種類については書かれていない。"],
             ["しょくぶつをたべるどうぶつは、いちぶのはなしだよ。","1800ねんだいのいえも、いちぶのはなしだよ。","むかしかられたオオカミのおはなしだね。","きたのしょくぶつのしゅるいは、かいていないよ。"]),
]

def groups(blocks):
    return dict(paragraphs=[" ".join(r[0] for r in b) for b in blocks],translations=["".join(r[1] for r in b) for b in blocks],sentencePairs=[r for b in blocks for r in b])

def passages():
    a=dict(label="A",title="Notice about Social Studies Homework",format="notice",**groups(NOTICE),questions=NOTICE_Q,
           instruction="次の掲示の内容に関して，(21)と(22)の質問に対する答えとして最も適切なもの，または文を完成させるのに最も適切なものを1，2，3，4の中から一つ選び，その番号のマーク欄をぬりつぶしなさい。")
    # The title is already displayed from title. Keep the two interview
    # questions on separate lines (the fixed PDF gives them a shaded box).
    notice_rows=a["sentencePairs"]
    notice_blocks=[[notice_rows[1]],notice_rows[2:5],[notice_rows[5]],notice_rows[6:8],notice_rows[8:]]
    a["paragraphs"]=[("\n" if i==3 else " ").join(r[0] for r in rows) for i,rows in enumerate(notice_blocks)]
    a["translations"]=[("\n" if i==3 else "").join(r[1] for r in rows) for i,rows in enumerate(notice_blocks)]
    blocks=[b for pair in zip(HEADERS,EMAIL) for b in pair]
    def email_text(rows,field):
        joiner=" " if field==0 else ""
        return "\n".join([rows[0][field],joiner.join(r[field] for r in rows[1:-2]),rows[-2][field],rows[-1][field]])
    email_data=groups(blocks)
    email_data["paragraphs"]=[text for header,body in zip(HEADERS,EMAIL) for text in ["\n".join(r[0] for r in header),email_text(body,0)]]
    email_data["translations"]=[text for header,body in zip(HEADERS,EMAIL) for text in ["\n".join(r[1] for r in header),email_text(body,1)]]
    b=dict(label="B",title="My brother Daniel / Are you OK? / OK!",format="multi-email",**email_data,questions=EMAIL_Q,
           instruction="次のEメールの内容に関して，(23)から(25)までの質問に対する答えとして最も適切なもの，または文を完成させるのに最も適切なものを1，2，3，4の中から一つ選び，その番号のマーク欄をぬりつぶしなさい。",
           emails=[dict(meta=meta,body=email_text(body,0),translation=email_text(body,1)) for meta,body in zip(META,EMAIL)])
    c=dict(label="C",title="Gray Wolves",format="article",**groups(ARTICLE),questions=ARTICLE_Q,
           instruction="次の英文の内容に関して，(26)から(30)までの質問に対する答えとして最も適切なもの，または文を完成させるのに最も適切なものを1，2，3，4の中から一つ選び，その番号のマーク欄をぬりつぶしなさい。")
    return [a,b,c]

"""Grade 3's established 30-word, four-focus-point, normal/easy lesson format."""
import re

VOCAB=[
    ("explain","説明する","動詞","Can you explain this rule to me?","このルールを私に説明してくれますか。",["売る","保存する","起こる"],"大問1 Q1","explain"),
    ("elevator","エレベーター","名詞","We took the elevator to the third floor.","私たちはエレベーターで3階へ行きました。",["湖","ドア","いとこ"],"大問1 Q2","elevator"),
    ("count","数える","動詞","Please count the books on the desk.","机の上の本を数えてください。",["呼ぶ","準備する","費用がかかる"],"大問1 Q3","count"),
    ("communicate","意思を伝え合う","動詞","I communicate with my friends in English.","私は友達と英語でやり取りします。",["横切る","閉める","持つ"],"大問1 Q4","communicate"),
    ("collect","集める","動詞","My sister collects old comic books.","姉（妹）は古いマンガを集めています。",["クリックする","横切る","不平を言う"],"大問1 Q5","collect"),
    ("without","～なしで・持たずに","前置詞","I went out without my umbrella.","私は傘を持たずに外出しました。",["～まで","～のそばに","～以来"],"大問1 Q6","without"),
    ("shy","恥ずかしがりの","形容詞","Don't be shy. You can do it.","恥ずかしがらないで。あなたならできます。",["丸い","十分な","最初の"],"大問1 Q7","shy"),
    ("so ... that","とても～なので…","構文","The room was so small that we could not play there.","部屋はとても小さかったので、そこで遊べませんでした。",["～するために","～する前に","～にもかかわらず"],"大問1 Q8","so small that"),
    ("take a walk","散歩する","熟語","I take a walk every morning.","私は毎朝散歩します。",["跳ぶ","寝る","歌う"],"大問1 Q9","take a walk"),
    ("all the way","道中ずっと・全行程","熟語","We walked all the way to school.","私たちは学校までずっと歩きました。",["時々","一部分だけ","次回に"],"大問1 Q10","all the way"),
    ("in fact","実は・実際には","熟語","In fact, I have two sisters.","実は、私には姉妹が2人います。",["一方で","例えば","最後に"],"大問1 Q11","In fact"),
    ("be covered with","～で覆われている","熟語","The cake is covered with strawberries.","そのケーキはイチゴで覆われています。",["～を探す","～に参加する","～を取り替える"],"大問1 Q12","was covered with"),
    ("written","書かれた（writeの過去分詞）","過去分詞","This is a book written in English.","これは英語で書かれた本です。",["話された","売られた","盗まれた"],"大問1 Q15","written"),
    ("faster","より速く","副詞（比較級）","He can run faster than me.","彼は私より速く走れます。",["最も速く","より遅く","速すぎる"],"大問1 Q14","faster"),
    ("grow up","育つ・成長する","熟語","My father grew up in Canada.","父はカナダで育ちました。",["出発する","着替える","集める"],"大問1 Q11","grew up"),
    ("sold out","売り切れの","表現","The tickets are sold out.","チケットは売り切れです。",["無料の","割引の","予約できる"],"大問2 Q16","sold out"),
    ("smell","～の匂いがする","動詞","This soup smells good.","このスープはよい匂いがします。",["～に聞こえる","～を集める","～を数える"],"大問2 Q17","smells"),
    ("take part in","～に参加する","熟語","I want to take part in the contest.","私は大会に参加したいです。",["～を説明する","～を交換する","～を閉める"],"大問2 Q18","take part in"),
    ("taste","～の味がする","動詞","The sandwich tastes good.","そのサンドイッチはおいしいです。",["～に聞こえる","～を数える","～を用意する"],"大問2 Q19","tastes"),
    ("put on","着る・身に付ける","熟語","Please put on a clean T-shirt.","きれいなTシャツを着てください。",["脱ぐ","片付ける","返す"],"大問2 Q20","Put on"),
    ("opening sale","開店セール","名詞","Our opening sale is on Sunday.","当店の開店セールは日曜日です。",["誕生日会","スピーチ大会","音楽教室"],"大問3A","opening sale"),
    ("or more","～以上","表現","Buy three or more cookies.","クッキーを3枚以上買ってください。",["～未満","～だけ","～より少ない"],"大問3A","or more"),
    ("discount","割引","名詞","You can get a discount today.","今日は割引を受けられます。",["招待状","技能","方角"],"大問3A","discount"),
    ("exchange A for B","AをBと交換する","熟語","You can exchange the card for a gift.","カードをプレゼントと交換できます。",["AをBで説明する","AをBから借りる","AをBと数える"],"大問3A","exchange it for a gift"),
    ("borrow","借りる","動詞","Can I borrow your CD player?","あなたのCDプレーヤーを借りてもいいですか。",["貸す","買う","売る"],"大問3B 第3のメール","borrow"),
    ("concert","コンサート","名詞","We went to a concert last week.","私たちは先週コンサートへ行きました。",["競技場","公園","映画館"],"大問3B 第2のメール","concert"),
    ("explorer","探検家","名詞","The explorer traveled to a new place.","その探検家は新しい場所へ旅をしました。",["歌手","店員","客"],"大問3C","explorer"),
    ("skill","技能","名詞","He has useful skills.","彼は役に立つ技能を持っています。",["嵐","切符","道具"],"大問3C","skills"),
    ("come true","実現する","熟語","Her dream came true.","彼女の夢は実現しました。",["終わる","成長する","出発する"],"大問3C","came true"),
    ("medal","メダル","名詞","She received a medal.","彼女はメダルを受け取りました。",["地図","手紙","道具"],"大問3C","medal"),
]

def vocabulary():
    result=[]
    for i,(word,meaning,pos,example,ja,distractors,source,form) in enumerate(VOCAB,1):
        slug=re.sub(r"[^a-z0-9]+","_",word.lower()).strip("_")
        result.append(dict(word=word,meaning=meaning,pos=pos,level="3級",example=example,exampleJa=ja,distractors=distractors,
                           source=source,sourceForm=form,wordAudio=f"audio/vocab/w_{i:03}_{slug}.mp3"))
    return result

def lessonplan(sections):
    qs=[q for s in sections[:2] for q in s["questions"]];ps=sections[2]["passages"]
    def filled(n):return qs[n-1]["text"].replace("(　)",qs[n-1]["choices"][qs[n-1]["answer"]-1])
    def excerpt(label,rows):return f"[出典: {label}]\n"+" ".join(r[0] for r in rows)
    a,b,c=[p["sentencePairs"] for p in ps]
    specs=[
        dict(title="語句の「セット」と文の形で選ぶ",subtitle="Set Phrases & Sentence Forms",color="#4f8cff",label="語句と文型",
             explanation="大問1では空所の後ろまで読む。explain 内容 to 人、communicate with 人、take a walk、all the way、In fact はセット。Q8 は small の後ろの that が決め手で so ... that。Q12 は was covered with の受動態、Q13 は was talking の過去進行形。Q14 は than に合わせて faster、Q15 は letter を後ろから説明する過去分詞 written。意味を確認してから、原形・ing形・過去分詞を区別する。",
             simple="ことばをセットでおぼえよう。take a walk は『さんぽする』。so small that は『とても小さいので』。was talking は『はなしていた』、written は『かかれた』だよ。than があれば、くらべる形もたしかめよう。",
             source="大問1 Q8・Q12・Q15",quote="The movie theater was so small that there were only twenty seats. / It was covered with chocolate and strawberries. / a letter written in French",
             examples=[(filled(8),"その映画館はとても小さかったので、座席が20席しかありませんでした。","so＋形容詞＋that＋文。very small は使えても、very ... that の形にはしない。","that につなぐのは so small のセットだよ。"),
                       (filled(12),"少女は誕生日のケーキを見て驚きました。それはチョコレートとイチゴで覆われていました。","be covered with は受動態。ケーキは覆われる側。","ケーキが、チョコとイチゴでおおわれていたよ。"),
                       (filled(15),"兄（弟）は昨日、フランス語で書かれた手紙を受け取りました。パリの文通相手からでした。","written in French が letter を後ろから修飾する。主文の動詞は got。","written が、どんなてがみかをせつめいするよ。")],
             passage="\n\n".join(f"[出典: 大問1 Q{n}]\n"+filled(n) for n in [6,8,9,10,12,15]),
             passageJa="【Q6】傘を持たずに外出し、雨でぬれた。\n【Q8】映画館はとても小さく、20席しかなかった。\n【Q9】若さの秘訣は毎朝の散歩と週3回のジム。\n【Q10】学校までずっと歩いたのではなく、母が車で送った。\n【Q12】ケーキはチョコレートとイチゴで覆われていた。\n【Q15】フランス語で書かれた手紙を、パリの文通相手からもらった。",
             patterns=["so small that","take a walk","all the way","was covered with","written in French"],
             questions=[("Q8で very ではなく so を使う理由は？","small の後ろに that 節があるため。so＋形容詞＋that＋文で程度と結果をつなぐ。"),
                        ("Q12の covered とQ13の talking の違いは？","covered は過去分詞でケーキが覆われた受動態。talking はing形で、その時に話していた過去進行形。"),
                        ("Q15の written はどの語を説明する？","a letter。written in French で『フランス語で書かれた』と手紙を後ろから説明する。")],
             easyQuestions=[("take a walk はどんないみ？","さんぽする、だよ。"),("was talking はどんないみ？","そのとき、はなしていた、だよ。"),("written in French はどんなてがみ？","フランスごでかかれたてがみ、だよ。")]),
        dict(title="会話は「前後のつながり」で選ぶ",subtitle="Dialogue Context & Response",color="#34d399",label="会話の対応",
             explanation="大問2は直前の状況と次のセリフを両方読む。Q16 は今夜の券が売り切れで明日の券を提案。Q17 はシチューの匂いを smells great、Q19 は食べたサンドイッチの味を tastes really good と表す。Q18 は初参加でも頑張るので first time と but が対になる。Q20 は汚れたTシャツを清潔なものに替える Put on a clean one。one は T-shirt の代わり。",
             simple="まえとうしろのセリフがヒント。こんやのチケットはうりきれ。smell はにおい、taste はあじ。はじめてでもがんばる、という but のつながりをみよう。よごれたTシャツは、きれいなものにきがえるよ。",
             source="大問2 Q16～Q20",quote="They're sold out. / It smells great. / Put on a clean one.",
             examples=[(filled(16),"客：今夜の野球のチケットはありますか。\n店員：申し訳ありません。売り切れです。明日の券はまだあります。\n客：では、明日のものを2枚買います。","They は今夜の tickets、those は明日の tickets。","こんやのものはうりきれで、あしたのものをかうよ。"),
                       (filled(17),"夫：何を料理していますか。\n妻：ビーフシチューです。少し食べてみますか。\n夫：ええ。とてもいい匂いがします。","smell＋形容詞は匂い。taste＋形容詞は味。","ここでは、シチューのにおいをほめているよ。"),
                       (filled(20),"息子：Tシャツにケチャップを付けてしまいました。\n母：そのままでは学校へ行けません。きれいなものに着替えなさい。\n息子：分かりました、お母さん。","put on は着る。a clean one は a clean T-shirt。","one は、きれいなTシャツのことだね。")],
             passage="\n\n".join(f"[出典: 大問2 Q{n}]\n"+filled(n) for n in range(16,21)),
             passageJa="【Q16】今夜のチケットは売り切れで、明日の券を2枚買う。\n【Q17】シチューがいい匂いで、試食したい。\n【Q18】初めてのスピーチ大会でも全力を尽くす。\n【Q19】サンドイッチがおいしく、明日も母に作ってほしい。\n【Q20】汚れたTシャツをきれいなものに着替える。",
             patterns=["sold out","smells great","my first time","tastes really good","Put on a clean one"],
             questions=[("Q16の those は何を指す？","明日の試合のチケット。今夜の券は売り切れで、店員が明日の券を代案として示している。"),
                        ("Q17とQ19は何を区別する？","匂いを smell、味を taste で表す。どちらも後ろに形容詞を置く。"),
                        ("Q20でかばんを持つ選択肢が合わない理由は？","問題はTシャツの汚れ。清潔なTシャツを着るよう指示する必要がある。")],
             easyQuestions=[("sold out はどんないみ？","うりきれ、だよ。"),("smell はにおい？ あじ？","におい。あじは taste だよ。"),("a clean one の one はなに？","きれいなTシャツだよ。")]),
        dict(title="お知らせとメール——条件・人物・時刻を分ける",subtitle="Conditions, People & Times",color="#a78bfa",label="条件と時刻",
             explanation="お知らせは特典ごとに条件を整理する。無料クッキーは3枚以上の購入、特別チケットは先着40人で次回来店50％引き、誕生日ギフトカードは誕生日にプレゼントと交換。メールは差出人と日時を確認する。Marie が曲を聞いたのは自宅。Jill が初めて聞いたのは10歳のとき、つまり20年前。バンドは約30年前に活動を始め、5年前にやめた。土曜午前は Marie のピアノ練習、訪問は昼食後。数字を何の情報かと一緒に読む。",
             simple="クッキーのおまけ、わりびきチケット、たんじょうびカードは、べつのもの。メールの10はねんれい、20はなんねんまえか。マリーのどようびは、ごぜんがピアノ、ごごがおばさんのいえだよ。",
             source="大問3A・3B",quote="If you buy three or more cookies, you'll get one free cookie! / With this ticket, you can get a 50% discount on your next visit. / That was twenty years ago!",
             examples=[(a[5][0],a[5][1],"If は条件。three or more は3枚以上で、種類の数ではない。","3まいいじょうかえば、1まいもらえるよ。"),
                       (a[9][0],a[9][1],"next visit が future visit に言い換えられている。誕生日カードと区別する。","チケットは、つぎにきたときのわりびきだよ。"),
                       (b[22][0]+" "+b[23][0],b[22][1]+b[23][1],"10歳は当時の年齢、20年前はその出来事の時期。","10はねんれい、20はなんねんまえかだね。")],
             passage=excerpt("大問3A セール条件・特別チケット",[a[4],a[5],a[8],a[9],a[10],a[11]])+"\n\n"+excerpt("大問3B 第2のメール",b[22:25])+"\n\n"+excerpt("大問3B 第3のメール",b[37:39]),
             passageJa="【お知らせ】セールは1枚1ドル。3枚以上買うと1枚無料。先着40人のチケットは次回来店50％引き。全員がもらう誕生日カードは、誕生日にプレゼントと交換する。\n【第2のメール】ジルは10歳のときに曲を初めて聞いた。それは20年前。バンドは約30年前に活動を始め、5年前にやめた。\n【第3のメール】マリーは土曜午前にピアノの練習があり、午後は空いている。自分の家で昼食後、バスでおばの家へ行く。",
             patterns=["three or more","your next visit","ten years old","twenty years ago","in the morning on Saturday"],
             questions=[("Q22で誕生日プレゼントの選択肢が合わない理由は？","質問は special ticket の機能。誕生日プレゼントと交換するのは別の birthday gift card。"),
                        ("Q24の10・20・30・5はそれぞれ何？","10はジルの当時の年齢、20は初めて曲を聞いた何年前か、30はバンドの活動開始、5は活動終了。"),
                        ("Q25で昼食後の訪問を選ばない理由は？","質問は Saturday morning。昼食後は午後なので、午前の piano practice を選ぶ。")],
             easyQuestions=[("むりょうクッキーをもらうには？","3まいいじょうかうよ。"),("ジルがはじめてきいたのはなんねんまえ？","20ねんまえだよ。"),("マリーのどようびのごぜんは？","ピアノのれんしゅうだよ。")]),
        dict(title="長文読解——人物の歩みと根拠を追う",subtitle="Biography, Timeline & Paraphrases",color="#f472b6",label="時系列と根拠",
             explanation="Matthew Henson は人物の伝記。出生地 near a river は close to a river、技能 several foreign languages は some languages に言い換えられる。仲間に選ばれた理由と、後から寒い地域へ旅した結果を区別する。1891年から挑戦し、嵐や氷で苦労した後、Finally, in April 1909 に北極点へ到達。1940年代の was given a medal は received a medal と同じ出来事。死亡は1955年。題名と全段落から、北極点へ行った人物の生涯が全体の主題と分かる。",
             simple="ヘンソンさんのいっしょうのおはなしだよ。1891ねんからちょうせんし、1909ねんにほっきょくてんへついた。1940ねんだいにメダルをもらい、1955ねんになくなった。ねんと、なにをしたかをいっしょにみよう。",
             source="大問3C 第1・3・4段落",quote="in a town near a river / Finally, in April 1909 / he was given a medal",
             examples=[(c[0][0],c[0][1],"was born は出生。near a river は close to a river と同じ意味。","うまれたばしょは、かわのちかくのまちだよ。"),
                       (c[16][0],c[16][1],"主語は the dream、主節の動詞は came。that Henson and Peary had は夢の説明。had を主節の動詞と取り違えない。","1909ねんにゆめがかなって、ほっきょくてんへついたよ。"),
                       (c[19][0],c[19][1],"was given a medal と received a medal は受動態と能動態で同じ出来事。","メダルをあたえられた、つまり、もらったんだね。")],
             passage=excerpt("大問3C 第3段落",c[11:18])+"\n\n"+excerpt("大問3C 第4段落",c[18:]),
             passageJa="【第3段落】2人の夢は誰よりも先に北極点へ行くこと。1891年から何度も挑戦したが、嵐や厚い氷で船が動けなくなった。ついに1909年4月に夢が実現し、北極点へ到達。ヘンソンはそこへ到達した最初のアフリカ系アメリカ人だった。\n【第4段落】1900年代初めは多くの人が彼の到達を知らなかった。1930年代以降に旅が知られ、1940年代にメダルを授与された。1955年にニューヨークで亡くなった後、多くの人が研究し、今では有名になっている。",
             patterns=["From 1891","However","Finally, in April 1909","After the 1930s","was given a medal","After Henson died"],
             questions=[("Q27で『道具をたくさん持っていた』が不正解な理由は？","fix tools は道具を修理する技能。持っている数ではない。求められたのは skills のある人。"),
                        ("Q28で嵐・氷ではなく夢の実現を選ぶ理由は？","質問は1909年。Finally, in April 1909 の文が北極点への到達を示し、嵐や氷はそれまでの困難。"),
                        ("Q29の was given a medal はどう言い換えられる？","received a medal。メダルを授与されたことと、受け取ったことは同じ出来事。")],
             easyQuestions=[("1909ねんに、なにがあった？","ほっきょくてんへついて、ゆめがかなったよ。"),("メダルをもらったのは？","1940ねんだいだよ。"),("これは、なにのおはなし？","ほっきょくてんへいったヘンソンさんのいっしょうだよ。")]),
    ]
    points=[]
    for n,s in enumerate(specs,1):
        points.append(dict(id=f"fp{n}",title=s["title"],subtitle=s["subtitle"],explanation=s["explanation"],explanationSimple=s["simple"],
                           sourceQuote=s["quote"],sourceLocation=s["source"],sourceQuoteAudio=f"audio/fp{n}_source.mp3",
                           examples=[dict(en=en,ja=ja,note=note,noteSimple=easy,audio=f"audio/fp{n}_ex{i}.mp3") for i,(en,ja,note,easy) in enumerate(s["examples"],1)],
                           practicePassage=dict(en=s["passage"],ja=s["passageJa"],source=s["source"],audioFile=f"audio/practice_pp{n}.mp3"),
                           highlightPatterns=s["patterns"],highlightColor=s["color"],highlightLabel=s["label"],
                           practiceQuestions=[dict(q=q,a=a) for q,a in s["questions"]],practiceQuestionsSimple=[dict(q=q,a=a) for q,a in s["easyQuestions"]]))
    return dict(focusPoints=points)

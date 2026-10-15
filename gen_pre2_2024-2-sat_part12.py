"""Parts 1-2 of EIKEN Grade Pre-2 2024-2 Saturday sub-venue (October 5, 2024).

Loaded by gen_pre2_2024-2-sat.py, which passes its helper functions as ``h``.
English text and choices are transcribed from the rendered booklet pages.
"""

from __future__ import annotations


def build_part1(h) -> list[dict]:
    q = h.question
    return [
        q(
            1,
            "Henry likes to wear sweaters made of ( 1 ). They are not as warm as wool sweaters, but he thinks they are more comfortable.",
            "ヘンリーは（1）でできたセーターを着るのが好きです。ウールのセーターほど暖かくはありませんが、そのほうが着心地がよいと彼は思っています。",
            ["rumor", "nails", "politics", "cotton"],
            ["うわさ", "くぎ・つめ", "政治", "綿・木綿"],
            4,
            [
                "rumorは『うわさ』。セーターの素材にならない",
                "nailsは『くぎ・つめ』。セーターを作る素材ではない",
                "politicsは『政治』。物の素材を表す語ではない",
                "cottonは『綿・木綿』。2文目でウールのセーターと比べているので、セーターの素材が入るとわかる",
            ],
            "💡 made of ～＝～でできた（材料を表す）。not as＋形容詞＋as ～＝～ほど…ではない。wool＝羊毛・ウール。",
        ),
        q(
            2,
            "A : Aren't you coming to Lisa's softball game? You ( 2 ) her that you would.\nB : Please tell her I'm sorry. I want to, but I have to work today.",
            "A：リサのソフトボールの試合に来ないの？来るって彼女に（2）でしょう。\nB：ごめんねって伝えておいて。行きたいけど、今日は仕事をしなければならないんだ。",
            ["admitted", "returned", "promised", "searched"],
            ["認めた", "戻った・返した", "約束した", "探した"],
            3,
            [
                "admittedは『（事実や過ちを）認めた』。試合に来ると相手に伝えた約束を表さない",
                "returnedは『戻った・返した』。her that you wouldと続けても意味が通らない",
                "promisedは『約束した』。来ると約束したのに来ないのかと尋ねる流れに合い、Bも謝っている",
                "searchedは『探した』。人に何かを伝える意味がない",
            ],
            "💡 promise 人 that ...＝人に～と約束する。that you wouldはthat you would comeの省略。Aren't you ～?＝～しないの？（否定疑問文）。",
        ),
        q(
            3,
            "A : My co-worker asks me questions every five minutes. I can't get my work done.\nB : That must be ( 3 ). You should ask him to stop.",
            "A：同僚が5分ごとに私に質問してくるんだ。仕事が終わらないよ。\nB：それは（3）にちがいないね。やめてくれるよう頼んだほうがいいよ。",
            ["annoying", "social", "neat", "empty"],
            ["いらいらさせる・迷惑な", "社会の・社交的な", "きちんとした", "空の"],
            1,
            [
                "annoyingは『いらいらさせる・迷惑な』。5分ごとに質問されて仕事が進まない状況への感想に合い、やめるよう頼むべきだという助言にもつながる",
                "socialは『社会の・社交的な』。仕事のじゃまをされている状況の感想にならない",
                "neatは『きちんとした』。困っている状況を表さない",
                "emptyは『空の』。Thatが指す状況の説明にならない",
            ],
            "💡 annoying＝（人を）いらいらさせる（annoyed＝いらいらした）。must be ～＝～にちがいない。get ～ done＝～を終わらせる。ask 人 to do＝人に～するよう頼む。",
        ),
        q(
            4,
            "After Blair finished writing his letter, he put it in an envelope. Then, he carefully ( 4 ) the envelope and put a stamp on it.",
            "ブレアは手紙を書き終えると、それを封筒に入れました。それから、封筒を丁寧に（4）、切手をはりました。",
            ["sealed", "failed", "baked", "robbed"],
            ["封をした", "失敗した", "焼いた", "奪った"],
            1,
            [
                "sealedは『封をした』。手紙を封筒に入れたあと、切手をはる前にする動作として合う",
                "failedは『失敗した』。封筒を目的語にしても意味が通らない",
                "bakedは『（オーブンで）焼いた』。手紙を出す手順に合わない",
                "robbedは『（人や店などから）奪った・強盗をした』。封筒に対する動作として意味が通らない",
            ],
            "💡 seal＝（封筒などに）封をする。finish doing＝～し終える（finish to doとは言わない）。put a stamp on ～＝～に切手をはる。",
        ),
        q(
            5,
            "Naoki's dream is to become a professional athlete. He plays for his school's baseball team and practices ( 5 ) to improve his skills.",
            "ナオキの夢はプロのスポーツ選手になることです。学校の野球部でプレーしていて、技術を上達させるために（5）練習しています。",
            ["daily", "partly", "quietly", "softly"],
            ["毎日", "部分的に", "静かに", "そっと・やさしく"],
            1,
            [
                "dailyは『毎日』。プロを目指して技術を上達させるために練習を続ける様子に合う",
                "partlyは『部分的に・一部は』。練習の回数や様子を表さない",
                "quietlyは『静かに』。プロを目指して上達しようとする努力を表す語として合わない",
                "softlyは『そっと・やさしく』。音や動きの柔らかさを表し、練習への熱心さを表さない",
            ],
            "💡 daily＝毎日（副詞）／毎日の（形容詞）。to improve ～＝～を上達させるために（目的を表す不定詞）。play for ～＝～（チーム）の一員としてプレーする。",
        ),
        q(
            6,
            "Ms. Wood works at a hotel. She can speak a few languages, so she ( 6 ) people from other countries.",
            "ウッドさんはホテルで働いています。いくつかの言語を話せるので、外国から来た人々を（6）。",
            ["guesses", "assists", "examines", "conducts"],
            ["推測する", "手伝う・援助する", "調べる・診察する", "（調査などを）行う・指揮する"],
            2,
            [
                "guessesは『推測する』。言語を話せることと、人を推測することが結びつかない",
                "assistsは『手伝う・援助する』。いくつかの言語を話せるので、外国から来た人の手助けをするという因果関係に合う",
                "examinesは『調べる・診察する』。ホテルの仕事で外国の人を調べる理由にならない",
                "conductsは『（調査などを）行う・（演奏を）指揮する』。言語を話せることを理由とする仕事の内容として合わない",
            ],
            "💡 assist＝手伝う・援助する（helpより改まった語）。a few＋複数名詞＝いくつかの～。so＝だから（結果を導く）。",
        ),
        q(
            7,
            "Douglas bought some plant food to help the ( 7 ) of the vegetables in his garden. Soon after he gave it to them, they started to get bigger and bigger.",
            "ダグラスは庭の野菜の（7）を助けるために、植物用の肥料を買いました。それを与えるとすぐに、野菜はどんどん大きくなり始めました。",
            ["truth", "courage", "absence", "growth"],
            ["真実", "勇気", "不在・欠席", "成長"],
            4,
            [
                "truthは『真実』。肥料で助けるものにならない",
                "courageは『勇気』。人について使う語で、野菜には合わない",
                "absenceは『不在・欠席』。肥料を与えて助けるものではない",
                "growthは『成長』。2文目のget bigger and bigger（どんどん大きくなる）が根拠",
            ],
            "💡 growth＝成長（動詞grow＋th）。help the growth of ～＝～の成長を助ける。比較級＋and＋比較級＝ますます～。plant food＝植物用の肥料。",
        ),
        q(
            8,
            "Yuji likes his current job, but he isn't satisfied with his pay. He decided to ( 8 ) a new job.",
            "ユウジは今の仕事を気に入っていますが、給料には満足していません。彼は新しい仕事を（8）ことにしました。",
            ["explain", "seek", "represent", "retire"],
            ["説明する", "探し求める", "代表する・表す", "引退する・退職する"],
            2,
            [
                "explainは『説明する』。新しい仕事を説明するのでは、給料への不満と結びつかない",
                "seekは『探し求める』。給料に満足していないので、新しい仕事を探すことにしたという流れに合う",
                "representは『代表する・表す』。a new jobを目的語にしても文意が通らない",
                "retireは『引退する・退職する』。新しい仕事を求める流れと合わず、a new jobを続けても意味が通らない",
            ],
            "💡 seek＝探し求める（look forとほぼ同じ意味。過去形はsought）。be satisfied with ～＝～に満足している。current＝現在の。pay＝給料。",
        ),
        q(
            9,
            "Soccer player Leonard Regan was sent to ( 9 ) because he had not paid his taxes for several years.",
            "サッカー選手のレナード・リーガンは、数年間税金を払っていなかったために（9）に送られました。",
            ["liquid", "prison", "space", "mind"],
            ["液体", "刑務所", "宇宙・空間", "心・精神"],
            2,
            [
                "liquidは『液体』。人が送られる場所にならない",
                "prisonは『刑務所』。税金を払っていなかったという罪の結果として送られる場所に合う",
                "spaceは『宇宙・空間』。税金を払わなかった結果として送られる場所ではない",
                "mindは『心・精神』。人が送られる場所を表さない",
            ],
            "💡 be sent to prison＝刑務所に送られる（この意味のprisonには冠詞をつけない）。had not paid＝払っていなかった（送られた時点までのことを表す過去完了）。tax＝税金。",
        ),
        q(
            10,
            "Mr. and Mrs. Clark have been trying to find an ideal ( 10 ) to build their house. They want it in a small town, not a big city.",
            "クラーク夫妻は、家を建てるのに理想的な（10）をずっと探しています。大都市ではなく、小さな町に建てたいと思っています。",
            ["forecast", "location", "blanket", "habit"],
            ["予報", "場所・位置", "毛布", "習慣"],
            2,
            [
                "forecastは『予報』。家を建てるために探すものではない",
                "locationは『場所・位置』。2文目で大都市ではなく小さな町がいいと、場所の希望を述べているのが根拠",
                "blanketは『毛布』。家を建てる話と結びつかない",
                "habitは『習慣』。家を建てる場所の話に合わない",
            ],
            "💡 location＝場所・位置。have been trying to do＝ずっと～しようとしている（現在完了進行形）。an ideal location to build＝建てるのに理想的な場所（to不定詞が名詞を説明）。A, not B＝BではなくA。",
        ),
        q(
            11,
            "A : Vanessa, your house is so ( 11 ) the office. Why do you ride a bike instead of taking the train?\nB : Because it's good exercise.",
            "A：バネッサ、あなたの家は会社から（11）よね。どうして電車に乗らずに自転車に乗るの？\nB：いい運動になるからよ。",
            ["up to", "on board", "far from", "based on"],
            ["～まで・～次第", "（乗り物に）乗って", "～から遠い", "～に基づいて"],
            3,
            [
                "up toは『～まで・～次第』。家と会社の位置関係を表さない",
                "on boardは『（乗り物に）乗って』。家について使う表現ではない",
                "far fromは『～から遠い』。家が会社から遠いのに、なぜ電車ではなく自転車なのかと尋ねる流れに合う",
                "based onは『～に基づいて』。家と会社の距離を表さない",
            ],
            "💡 far from ～＝～から遠い。instead of doing＝～する代わりに・～しないで。Why ～?の質問にBecause ...で理由を答えている。",
        ),
        q(
            12,
            "Jake decided that, to improve his health, he would exercise regularly and eat a more balanced diet ( 12 ).",
            "ジェイクは、健康を改善するために、（12）定期的に運動し、よりバランスのとれた食事をとることに決めました。",
            ["from now on", "on the air", "by the way", "over the top"],
            ["これからは・今後は", "放送中で", "ところで", "やりすぎの・大げさな"],
            1,
            [
                "from now onは『これからは・今後は』。健康のためにこれから習慣を変えると決心した内容に合う",
                "on the airは『放送中で』。テレビやラジオについての表現で、文脈に合わない",
                "by the wayは『ところで』。話題を変えるときの表現で、決心の内容に合わない",
                "over the topは『やりすぎの・大げさな』。健康のための決心を表す文に合わない",
            ],
            "💡 from now on＝これからは・今後は。decided that ... he would ～＝～しようと決めた（decidedに合わせてwillがwouldになっている）。balanced diet＝バランスのとれた食事。",
        ),
        q(
            13,
            "John likes to keep his room clean. He ( 13 ) every morning as soon as he gets up.",
            "ジョンは部屋をきれいにしておくのが好きです。彼は毎朝、起きるとすぐに（13）。",
            ["keeps in touch", "has a fever", "makes his bed", "heads for home"],
            ["連絡を取り合う", "熱がある", "ベッドを整える", "家に向かう"],
            3,
            [
                "keeps in touchは『連絡を取り合う』。部屋をきれいにしておく話と結びつかない",
                "has a feverは『熱がある』。毎朝の習慣として述べる内容ではない",
                "makes his bedは『ベッドを整える』。部屋をきれいにしておくのが好きなので、起きてすぐにする習慣として合う",
                "heads for homeは『家に向かう』。起きたばかりで家にいるのに家へ向かうのは不自然",
            ],
            "💡 make one's bed＝ベッドを整える。keep ～ clean＝～をきれいに保つ（keep＋O＋C）。as soon as ～＝～するとすぐに。",
        ),
        q(
            14,
            "Last weekend, Oliver helped his grandmother ( 14 ) her new computer. Then, he taught her how to send emails.",
            "先週末、オリバーは祖母が新しいコンピューターを（14）のを手伝いました。それから、メールの送り方を教えました。",
            ["wish for", "work for", "set up", "fill up"],
            ["～を願う", "～のために働く・～に勤める", "～を設定する・使えるようにする", "～をいっぱいにする"],
            3,
            [
                "wish forは『～を願う・欲しがる』。すでにある新しいコンピューターについて手伝う内容にならない",
                "work forは『～のために働く・～に勤める』。コンピューターを目的語にすると意味が通らない",
                "set upは『（機器を）設定する・使えるようにする』。新しいコンピューターの準備を手伝い、そのあとメールの送り方を教えた流れに合う",
                "fill upは『～をいっぱいにする』。容器などに使い、コンピューターの準備を表さない",
            ],
            "💡 set up ～＝（機器などを）設定する・使えるように準備する。help 人 do＝人が～するのを手伝う（toのない動詞の原形）。how to do＝～の仕方。",
        ),
        q(
            15,
            "Manny is very ( 15 ) Japanese history. He often borrows books about Japan from the school library.",
            "マニーは日本の歴史にとても（15）。よく学校の図書館から日本についての本を借ります。",
            ["separate from", "broken off", "bored of", "curious about"],
            ["～から離れた・～とは別の", "折れて取れた", "～に飽きた", "～に興味がある"],
            4,
            [
                "separate fromは『～から離れた・～とは別の』。人の興味や気持ちを表さない",
                "broken offは『折れて取れた・（関係などが）断たれた』。人の気持ちを表す表現ではない",
                "bored ofは『～に飽きた』。日本の本をよく借りるという2文目と内容が逆になる",
                "curious aboutは『～に興味がある・～を知りたがる』。日本についての本をよく借りるという2文目が根拠",
            ],
            "💡 be curious about ～＝～に興味がある・～を知りたがる。borrow A from B＝BからAを借りる。often＝よく・しばしば。",
        ),
    ]


SHARED_INK_DIALOGUE = (
    "A : Excuse me. I need to buy some ink for my printer.\n"
    "B : Certainly, sir. What ( 19 )?\n"
    "A : Black. I print out lots of documents, so it runs out quickly.\n"
    "B : I see. You can find that over here. I recommend this brand, but it's ( 20 ).\n"
    "A : Hmm. That's more than I want to pay. Do you have anything cheaper?\n"
    "B : Sure. This is the cheapest we have.\n"
    "A : OK. This looks fine. I'll take some.\n"
    "B : Great. Please follow me to the checkout."
)
SHARED_INK_TRANSLATION = (
    "A：すみません。プリンターのインクを買いたいのですが。\n"
    "B：かしこまりました。（19）？\n"
    "A：黒です。書類をたくさん印刷するので、すぐになくなってしまうんです。\n"
    "B：なるほど。それならこちらにございます。このブランドがおすすめですが、（20）です。\n"
    "A：うーん。払いたい金額より高いですね。もっと安いものはありますか。\n"
    "B：はい。こちらが当店でいちばん安いものです。\n"
    "A：わかりました。これでよさそうです。いくつかいただきます。\n"
    "B：ありがとうございます。レジまでご案内します。"
)


def build_part2(h) -> list[dict]:
    q = h.question
    return [
        q(
            16,
            "A : I'm playing the violin in a concert on Saturday. Do you want to come?\nB : Wow, that's great! Where ( 16 )?\nA : I have some free ones to give to friends. Here you are.\nB : Thank you! I can't wait to watch your performance!",
            "A：土曜日のコンサートでバイオリンを弾くんだ。来たい？\nB：わあ、すごいね！どこで（16）？\nA：友達にあげる無料のものが何枚かあるんだ。はい、どうぞ。\nB：ありがとう！演奏を見るのが待ちきれないよ！",
            [
                "do you take lessons",
                "is the concert",
                "can I buy tickets",
                "shall we meet then",
            ],
            [
                "レッスンを受けているの",
                "コンサートはあるの",
                "チケットを買えるの",
                "（そのとき）待ち合わせようか",
            ],
            3,
            [
                "どこでレッスンを受けているのかと尋ねても、Aが無料のもの（free ones）を渡す返事につながらない",
                "コンサートの場所を尋ねたのなら場所を答えるはずで、何かを渡す返事と合わない",
                "どこでチケットを買えるのか。Aがfree ones（無料のもの）を友達にあげると言って渡しているので、onesがticketsを指し、チケットの入手先を尋ねたとわかる",
                "待ち合わせ場所を尋ねたのなら場所や時間を答えるはずで、何かを渡す返事にならない",
            ],
            "💡 onesは前に出た名詞の繰り返しを避ける代名詞で、ここではticketsを指す。Here you are.＝はい、どうぞ（物を渡すとき）。can't wait to do＝～するのが待ちきれない。",
        ),
        q(
            17,
            "A : Hello. I'd like to ( 17 ).\nB : I'm afraid the hotel is full this weekend, sir.\nA : That's too bad. I can't change the date of my trip.\nB : I'm very sorry. I hope you can stay with us another time.",
            "A：もしもし。（17）のですが。\nB：あいにく、今週末はホテルが満室でございます。\nA：それは残念です。旅行の日程は変えられないんです。\nB：大変申し訳ございません。またの機会にお泊まりいただければ幸いです。",
            [
                "go swimming in the pool",
                "cancel my reservation",
                "pay for my trip",
                "book a room for Saturday",
            ],
            [
                "プールに泳ぎに行きたい",
                "予約を取り消したい",
                "旅行代金を支払いたい",
                "土曜日に部屋を予約したい",
            ],
            4,
            [
                "プールで泳ぎたいという用件なら、ホテルが満室だという返事につながらない",
                "予約を取り消したいのなら、満室であることは問題にならず、日程を変えられないという話にもならない",
                "旅行代金の支払いは、ホテルが満室だという返事と結びつかない",
                "土曜日に部屋を予約したい。Bが今週末は満室だと答え、Aが旅行の日程を変えられないと残念がっているので、週末の部屋を予約しようとしたとわかる",
            ],
            "💡 book＝予約する（動詞）。I'd like to do＝～したいのですが（丁寧な言い方）。I'm afraid ...＝あいにく～です。full＝満室の・いっぱいの。",
        ),
        q(
            18,
            "A : It's Mom's birthday next Monday. Don't forget!\nB : Actually, I've been thinking about what to get for her, but I'm still not sure.\nA : Well, Dad and I are getting her some clothes, so you should probably get her something else. You know she likes to read.\nB : Thanks! I'll ( 18 ).",
            "A：来週の月曜日はお母さんの誕生日だよ。忘れないでね！\nB：実は、何をあげようかずっと考えているんだけど、まだ決まらないんだ。\nA：そうね、お父さんと私は服をあげるから、あなたは何かほかのものをあげたほうがいいと思う。お母さんが読書好きなのは知っているでしょう。\nB：ありがとう！（18）よ。",
            [
                "get her a new book",
                "give her a nice sweater",
                "find a hat that she likes",
                "buy Dad his favorite magazine",
            ],
            [
                "お母さんに新しい本を買ってあげる",
                "お母さんにすてきなセーターをあげる",
                "お母さんが気に入る帽子を探す",
                "お父さんにお気に入りの雑誌を買う",
            ],
            1,
            [
                "お母さんに新しい本を買ってあげる。Aが、お母さんは読書が好きだと教えてくれたので、本を選ぶのが自然",
                "セーターは服なので、Aと父親が服をあげるからほかのものを、という助言に合わない",
                "帽子は、Aが最後に伝えた『読書が好き』というヒントと結びつかない",
                "お母さんの誕生日プレゼントの話なので、お父さんに雑誌を買うのは目的に合わない",
            ],
            "💡 get 人 物＝人に物を買ってあげる。I've been thinking＝ずっと考えている（現在完了進行形）。something else＝何かほかのもの。",
        ),
        q(
            19,
            SHARED_INK_DIALOGUE,
            SHARED_INK_TRANSLATION,
            [
                "kind of computer do you have",
                "color of ink do you need",
                "brand of printer do you like",
                "do you play on your computer",
            ],
            [
                "どんな種類のコンピューターをお持ちですか",
                "何色のインクが必要ですか",
                "どのブランドのプリンターがお好きですか",
                "コンピューターで何をして遊びますか",
            ],
            2,
            [
                "コンピューターの種類を尋ねても、Aの答えBlack（黒）と合わない",
                "何色のインクが必要か。AがBlack.（黒です）と色で答えているのが根拠",
                "プリンターのブランドの好みを尋ねたのなら、Blackという答えにならない",
                "コンピューターで何をして遊ぶかは、インクを買いに来た客への質問として合わず、Blackとも答えない",
            ],
            "💡 What color of ～ do you need?＝何色の～が必要ですか。print out＝印刷する。run out＝なくなる・切れる。",
        ),
        q(
            20,
            SHARED_INK_DIALOGUE,
            SHARED_INK_TRANSLATION,
            [
                "not very easy to use",
                "not sold at most stores",
                "ink for printing photographs",
                "our most expensive ink",
            ],
            [
                "あまり使いやすくない",
                "ほとんどの店では売られていない",
                "写真印刷用のインク",
                "当店でいちばん高価なインク",
            ],
            4,
            [
                "使いにくいという説明なら、Aが『払いたい金額より高い』と値段の話をする流れにならない",
                "ほとんどの店で売られていないという情報は、Aが値段を理由に安いものを求める返事につながらない",
                "写真印刷用だという説明は、書類を印刷するAに勧める理由にならず、値段の話にもつながらない",
                "当店でいちばん高価なインク。AがThat's more than I want to pay.（払いたい金額より高い）と答え、もっと安いものを求めているのが根拠",
            ],
            "💡 more than I want to pay＝払いたい額より多い→高すぎる。the most expensive（いちばん高価な）⇔ the cheapest（いちばん安い）。follow me＝ついてきてください。checkout＝レジ。",
        ),
    ]

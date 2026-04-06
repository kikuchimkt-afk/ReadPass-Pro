"""Generate sections 2-3 + vocabulary + lessonPlan for 2021-3"""
import json, os
base = r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade-pre2\2021-3"
data = json.load(open(os.path.join(base, "_part1.json"), "r", encoding="utf-8"))

s3 = {"name":"大問3","nameEn":"Part 3","type":"passage-fill",
    "instruction":"次の英文A，Bを読み，その文意にそって(26)から(30)までの(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選びなさい。",
    "passages":[
        {"label":"A","title":"Lost for Words",
         "paragraphs":[
             "Keiko is 65 years old. She retired from her job a few months ago. When she was working, she was always very busy. She had no time for hobbies. However, she now has plenty of free time. She enjoys gardening, reading books, and going for walks in the countryside. She also ( 26 ). She really enjoys learning a foreign language and using it to speak with her classmates and her teacher, Mr. Lopez.",
             "One day, Mr. Lopez asked Keiko to talk about her family in class. There were many things that she wanted to say, but she could not say them. She was disappointed because she did not know all the words that she needed. Mr. Lopez tried to ( 27 ). He said that she is doing really well. If she keeps studying and practicing hard, she will soon find it easy to talk about anything."
         ],
         "translations":[
             "ケイコは65歳だ。数ヶ月前に退職した。働いていた時はいつもとても忙しかった。趣味の時間がなかった。しかし今は十分な自由時間がある。ガーデニング、読書、田舎の散歩を楽しんでいる。また( 26 )。外国語を学び、クラスメートやロペス先生と話すのを楽しんでいる。",
             "ある日、ロペス先生はケイコにクラスで家族について話すよう頼んだ。言いたいことがたくさんあったが、言えなかった。必要な単語をすべて知らなかったのでがっかりした。ロペス先生は( 27 )うとした。彼女はとてもよくやっていると言った。勉強と練習を続ければ、すぐに何でも話せるようになると。"
         ],
         "sentencePairs":[
             ["Keiko is 65 years old. She retired from her job a few months ago.","ケイコは65歳だ。数ヶ月前に退職した。"],
             ["When she was working, she was always very busy.","働いていた時はいつもとても忙しかった。"],
             ["She now has plenty of free time.","今は十分な自由時間がある。"],
             ["She really enjoys learning a foreign language.","外国語を学ぶのを楽しんでいる。"],
             ["There were many things that she wanted to say, but she could not say them.","言いたいことがたくさんあったが、言えなかった。"],
             ["She was disappointed because she did not know all the words that she needed.","必要な単語をすべて知らなかったのでがっかりした。"],
             ["If she keeps studying and practicing hard, she will soon find it easy to talk about anything.","勉強と練習を続ければ、すぐに何でも話せるようになる。"]
         ],
         "questions":[
             {"number":26,"choices":["takes Spanish lessons","is a volunteer at a hospital","likes to paint pictures","joined a yoga class"],"choiceTranslations":["スペイン語のレッスンを受けている","病院でボランティアをしている","絵を描くのが好きだ","ヨガ教室に入った"],"answer":1,"choiceAnalysis":["スペイン語レッスン→正解。💡 「learning a foreign language」＋「Mr. Lopez」（スペイン語の先生名）","病院ボランティア→外国語学習の文脈に合わない","絵を描く→外国語と無関係","ヨガ教室→クラスメートやロペス先生の文脈に合わない"],"grammar":"💡 take lessons＝レッスンを受ける。foreign language＝外国語"},
             {"number":27,"choices":["find her textbook","cheer her up","repair her bag","show her around"],"choiceTranslations":["教科書を見つける","励ます","鞄を修理する","案内する"],"answer":2,"choiceAnalysis":["教科書→がっかりした生徒への対応として不適切","励ます→正解。💡 がっかりしたケイコに「よくやっている」と励ます","鞄の修理→文脈に無関係","案内→語学の文脈に合わない"],"grammar":"💡 cheer up＝励ます、元気づける。try to ～＝～しようとする"}
         ]
        },
        {"label":"B","title":"Pest Protection",
         "paragraphs":[
             "Insects and other animals often make trouble for farmers. Such animals are known as pests and can be a big problem. They eat the fruits and vegetables that should be sold as food. They also carry diseases to the plants grown on farms. ( 28 ) costs farmers a lot of money. Many farmers use chemicals to keep pests away. These chemicals can be bad for the environment, though. They can kill other creatures. They can also get into the fruits and vegetables that people eat.",
             "The owners of the Vergenoegd Low wine farm in South Africa use a different method. They want to stop pests from eating their grapes. At the same time, they do not want any chemicals to get in their wine. Their solution is to ( 29 ) to remove pests. Every day, a team of over 1,000 ducks is taken to the fields where the grapes are grown. The ducks spend all day walking around the plants and eating the pests.",
             "Although ducks have been used to control pests in rice fields in Asia for hundreds of years, the use of ducks in other places is much less common. The ducks used on the Vergenoegd Low wine farm are a special kind. They have ( 30 ) than other kinds of ducks. As a result, they cannot fly away. Using ducks to control pests also has another advantage. Their waste helps the grape plants to grow."
         ],
         "translations":[
             "昆虫や他の動物はしばしば農家に迷惑をかける。そのような動物は害虫として知られ、大きな問題になる。食料として売られるべき果物や野菜を食べる。農場で育てられた植物に病気を運ぶ。( 28 )は農家に多額の費用をかける。多くの農家は害虫を遠ざけるために化学薬品を使う。しかし化学薬品は環境に悪い影響を与えることがある。他の生物を殺すこともある。人が食べる果物や野菜に入ることもある。",
             "南アフリカのフェルゲヌーフド・ロウワイン農場のオーナーは異なる方法を使っている。害虫がブドウを食べるのを止めたい。同時に、ワインに化学薬品を入れたくない。彼らの解決策は害虫を除去するために( 29 )ことだ。毎日1,000羽以上のアヒルのチームがブドウ畑に連れて行かれる。アヒルは一日中植物の周りを歩き回り害虫を食べる。",
             "アジアでは何百年もの間、水田で害虫を制御するためにアヒルが使われてきたが、他の場所でのアヒルの使用はあまり一般的ではない。フェルゲヌーフド農場で使われるアヒルは特別な種類だ。他の種類のアヒルより( 30 )。そのため飛んで逃げることができない。害虫を制御するためにアヒルを使うことにはもう一つの利点もある。アヒルの排泄物がブドウの木の成長を助ける。"
         ],
         "sentencePairs":[
             ["Insects and other animals often make trouble for farmers.","昆虫や他の動物はしばしば農家に迷惑をかける。"],
             ["Such animals are known as pests and can be a big problem.","そのような動物は害虫として知られ、大きな問題になる。"],
             ["Many farmers use chemicals to keep pests away.","多くの農家は害虫を遠ざけるために化学薬品を使う。"],
             ["These chemicals can be bad for the environment, though.","しかし化学薬品は環境に悪影響を与えることがある。"],
             ["They want to stop pests from eating their grapes.","害虫がブドウを食べるのを止めたい。"],
             ["Their solution is to use other animals to remove pests.","彼らの解決策は害虫を除去するために他の動物を使うことだ。"],
             ["Every day, a team of over 1,000 ducks is taken to the fields.","毎日1,000羽以上のアヒルのチームが畑に連れて行かれる。"],
             ["The ducks spend all day walking around the plants and eating the pests.","アヒルは一日中植物周りを歩き害虫を食べる。"],
             ["Although ducks have been used to control pests in rice fields in Asia for hundreds of years, the use of ducks in other places is much less common.","アジアでは数百年間アヒルが使われてきたが、他の場所ではあまり一般的でない。"],
             ["Using ducks to control pests also has another advantage.","アヒルを使うことにはもう一つの利点がある。"],
             ["Their waste helps the grape plants to grow.","排泄物がブドウの木の成長を助ける。"]
         ],
         "questions":[
             {"number":28,"choices":["The weather","The damage","Buying land","Picking fruit"],"choiceTranslations":["天候","被害","土地を買うこと","果物を収穫すること"],"answer":2,"choiceAnalysis":["天候→害虫の費用を説明する主語として不適切","被害→正解。💡 害虫が果物を食べ病気を運ぶ＝被害→費用がかかる","土地を買う→害虫の問題の文脈に合わない","果物を収穫→費用の原因として不適切"],"grammar":"💡 damage＝被害、損害。cost ～ money＝～に費用がかかる"},
             {"number":29,"choices":["get local children","move their plants","build tall fences","use other animals"],"choiceTranslations":["地元の子どもを集める","植物を移動させる","高い柵を建てる","他の動物を使う"],"answer":4,"choiceAnalysis":["子どもを集める→害虫除去方法として不適切","植物を移動→解決策として不自然","高い柵→次文のアヒルと繋がらない","他の動物を使う→正解。💡 次文で「1,000 ducks」が害虫を食べる＝動物を使う方法"],"grammar":"💡 solution＝解決策。remove＝除去する。method＝方法"},
             {"number":30,"choices":["more babies each year","more colorful bodies","much louder voices","much shorter wings"],"choiceTranslations":["毎年多くの赤ちゃん","もっと色鮮やかな体","もっと大きな声","もっと短い翅"],"answer":4,"choiceAnalysis":["赤ちゃん→飛べないことの理由にならない","色鮮やかな体→飛べないことと無関係","大きな声→飛べないことと無関係","短い翅→正解。💡 翅が短い→As a result, they cannot fly away"],"grammar":"💡 much shorter wings＝ずっと短い翅。much＝比較級を強調。As a result＝その結果"}
         ]
        }
    ]
}

s4 = {"name":"大問4","nameEn":"Part 4","type":"reading-comprehension",
    "instruction":"次の英文A，Bの内容に関して，(31)から(37)までの質問に対して最も適切なもの，または文を完成させるのに最も適切なものを1，2，3，4の中から一つ選びなさい。",
    "passages":[
        {"label":"A","title":"Ontario Trip","format":"email",
         "meta":{"from":"Joe Hess","to":"Pete Hess","date":"January 23","subject":"Ontario trip"},
         "paragraphs":[
             "Are you excited about our trip to Ontario next month? I bought my ticket to Ontario and my return ticket yesterday. My plane leaves Chicago at 11 a.m. on February 8. The flight takes only one and a half hours. Have you bought your tickets yet? What time will you leave New York City?",
             "Anyway, do you remember what we talked about on the phone last week? You said that you want to go fishing during our trip. My neighbor goes on fishing trips in Ontario every fall. She told me about a company that offers one-day fishing tours of Lake Huron. The company's name is Great Fish, and it costs $300 for two people. The tour will start at 8 a.m. and finish at 4 p.m., and the price includes lunch.",
             "I'll call the company tonight and make a reservation for February 10. My neighbor also said that we need special licenses to fish in Ontario. We can get them online, or we can buy them at a sports shop in Ontario. I think we should buy them on the Internet before we go. A one-day license costs about $20. I can't wait to go!"
         ],
         "translations":[
             "来月のオンタリオ旅行楽しみ？昨日オンタリオ行きと帰りのチケットを買ったよ。飛行機はシカゴから2月8日午前11時に出発。フライトはたった1時間半。もうチケット買った？何時にニューヨークを出発する？",
             "ところで、先週電話で話したこと覚えてる？旅行中に釣りに行きたいって言ってたよね。近所の人が毎年秋にオンタリオで釣りに行くんだ。ヒューロン湖の1日釣りツアーを提供している会社を教えてくれた。会社名はグレートフィッシュで、2人で300ドル。ツアーは朝8時から午後4時までで、昼食込み。",
             "今夜会社に電話して2月10日の予約をするよ。近所の人はオンタリオで釣りをするには特別な許可証が必要だとも言っていた。ネットで取れるし、オンタリオのスポーツショップでも買える。出発前にネットで買うべきだと思う。1日許可証は約20ドル。行くのが待ちきれない！"
         ],
         "sentencePairs":[
             ["I bought my ticket to Ontario and my return ticket yesterday.","昨日オンタリオ行きと帰りのチケットを買った。"],
             ["My plane leaves Chicago at 11 a.m. on February 8.","飛行機はシカゴから2月8日午前11時に出発する。"],
             ["The flight takes only one and a half hours.","フライトはたった1時間半だ。"],
             ["She told me about a company that offers one-day fishing tours of Lake Huron.","ヒューロン湖の1日釣りツアーを提供する会社を教えてくれた。"],
             ["It costs $300 for two people.","2人で300ドルだ。"],
             ["The price includes lunch.","料金には昼食が含まれる。"],
             ["We need special licenses to fish in Ontario.","オンタリオで釣りをするには特別な許可証が必要だ。"],
             ["I think we should buy them on the Internet before we go.","出発前にネットで買うべきだと思う。"],
             ["A one-day license costs about $20.","1日許可証は約20ドルだ。"]
         ],
         "questions":[
             {"number":31,"question":"What will Joe do in February?","questionTranslation":"ジョーは2月に何をしますか？","choices":["Buy plane tickets to Chicago.","Go on vacation with Pete.","Visit New York City.","Move to a new home in Ontario."],"choiceTranslations":["シカゴ行きの飛行機チケットを買う。","ピートと一緒に休暇に行く。","ニューヨーク市を訪問する。","オンタリオの新居に引っ越す。"],"answer":2,"choiceAnalysis":["チケット購入→すでに昨日購入済み","ピートと休暇→正解。💡 「our trip to Ontario next month」2月にピートとオンタリオ旅行","ニューヨーク訪問→ピートがNYに住んでいるだけ","引っ越し→旅行であり引っ越しではない"],"grammar":"💡 go on vacation＝休暇に行く。trip＝旅行のパラフレーズ"},
             {"number":32,"question":"Joe's neighbor","questionTranslation":"ジョーの隣人は","choices":["gave Joe a tour of Lake Huron.","said Joe could use her fishing boat.","told Joe about a fishing tour company.","recommended a restaurant to Joe."],"choiceTranslations":["ヒューロン湖のツアーをしてくれた。","釣り船を使っていいと言った。","釣りツアー会社を教えた。","レストランを勧めた。"],"answer":3,"choiceAnalysis":["ツアーをしてくれた→ツアーガイドではない","釣り船→船の記述なし","釣りツアー会社を教えた→正解。💡 「She told me about a company that offers one-day fishing tours」","レストラン→レストランの記述なし"],"grammar":"💡 tell someone about ～＝人に～について教える"},
             {"number":33,"question":"How does Joe suggest he and Pete get licenses?","questionTranslation":"ジョーはどうやって許可証を取ることを提案していますか？","choices":["By going to a sports shop to get them.","By buying them from a website.","By ordering them on the phone.","By asking a company to reserve them."],"choiceTranslations":["スポーツショップに行って取る。","ウェブサイトで買う。","電話で注文する。","会社に予約を頼む。"],"answer":2,"choiceAnalysis":["スポーツショップ→選択肢の一つだが推奨していない","ウェブサイト→正解。💡 「I think we should buy them on the Internet before we go」","電話→電話は釣りツアー予約のみ","会社に予約→許可証の方法ではない"],"grammar":"💡 on the Internet＝ネットで。from a website（パラフレーズ）"}
         ]
        },
        {"label":"B","title":"The Mystery of the Crannogs",
         "paragraphs":[
             "In some lakes in Scotland and Ireland, there are small man-made islands. These are called crannogs, and they were built long ago with large rocks that were carried into the lakes. Building the crannogs was probably a lot of hard work because some of the rocks weigh 250 kilograms. What is more, the crannogs are between 10 and 30 meters wide and connected to the land by a bridge made of rocks. Although there are over a thousand of them, no one knows the reason why they were made.",
             "Experts used to think that the crannogs were built about 3,000 years ago. However, a recent discovery shows that some of the crannogs are much older. A diver found some broken pots in the water around the crannogs in a lake on the island of Lewis. Scientists discovered that the pots were over 5,000 years old. This led to further research and the discovery of similar items in other lakes with crannogs.",
             "The pots were in good condition, and it was clear to researchers that they had not been used much before they were dropped in the lakes. The researchers believe that the pots were probably used for special ceremonies on the crannogs. It is not clear what the purpose of the ceremonies was, though, because there are no written records from the time when they were held.",
             "Two thousand years after the oldest crannogs were built, people began living on them. This is shown by old pieces of wood from their houses that have been found on the crannogs. When these people built their houses, they probably damaged the crannogs. This made it difficult to find out why the crannogs were built. Researchers are continuing to look for things to solve the mystery of the crannogs, but it may take many years for them to do so."
         ],
         "translations":[
             "スコットランドとアイルランドのいくつかの湖には小さな人工島がある。これらはクランノグと呼ばれ、大きな岩を湖に運んで昔に作られた。岩の中には250キロのものもあるため、建設はかなりの重労働だったと思われる。さらに、クランノグは幅10～30メートルで、岩でできた橋で陸地と繋がっている。1,000以上あるが、なぜ作られたのか誰も知らない。",
             "専門家たちはかつてクランノグが約3,000年前に建てられたと考えていた。しかし最近の発見により、一部のクランノグはもっと古いことが分かった。ルイス島の湖でダイバーがクランノグ周辺の水中で割れた壺を見つけた。科学者はその壺が5,000年以上前のものであることを発見した。これがさらなる調査と、他の湖でも同様の品物の発見につながった。",
             "壺は良い状態で、湖に落とされる前にあまり使われていなかったことは研究者には明らかだった。研究者たちは壺がクランノグ上での特別な儀式に使われたと考えている。しかし儀式の目的は明らかではない。儀式が行われた時代の文字による記録がないためだ。",
             "最も古いクランノグが建てられてから2,000年後、人々がクランノグに住み始めた。これはクランノグ上で見つかった家の古い木片によって示されている。これらの人々が家を建てた時、クランノグを損傷した可能性がある。これによりクランノグが建てられた理由の解明が困難になった。研究者たちはクランノグの謎を解くものを探し続けているが、何年もかかるかもしれない。"
         ],
         "sentencePairs":[
             ["In some lakes in Scotland and Ireland, there are small man-made islands.","スコットランドとアイルランドのいくつかの湖には小さな人工島がある。"],
             ["These are called crannogs, and they were built long ago with large rocks.","これらはクランノグと呼ばれ、大きな岩で昔に作られた。"],
             ["Although there are over a thousand of them, no one knows the reason why they were made.","1,000以上あるが、なぜ作られたのか誰も知らない。"],
             ["Experts used to think that the crannogs were built about 3,000 years ago.","専門家はクランノグが約3,000年前に建てられたと考えていた。"],
             ["A diver found some broken pots in the water around the crannogs.","ダイバーがクランノグ周辺の水中で割れた壺を見つけた。"],
             ["Scientists discovered that the pots were over 5,000 years old.","科学者はその壺が5,000年以上前のものであることを発見した。"],
             ["The researchers believe that the pots were probably used for special ceremonies.","研究者は壺が特別な儀式に使われたと考えている。"],
             ["Two thousand years after the oldest crannogs were built, people began living on them.","最古のクランノグ建設から2,000年後、人々が住み始めた。"],
             ["When these people built their houses, they probably damaged the crannogs.","家を建てた時にクランノグを損傷した可能性がある。"],
             ["Researchers are continuing to look for things to solve the mystery.","研究者たちは謎を解くものを探し続けている。"]
         ],
         "questions":[
             {"number":34,"question":"Crannogs are","questionTranslation":"クランノグとは","choices":["man-made lakes in Scotland and Ireland.","islands made by people a long time ago.","walls built with large rocks.","bridges that were built across lakes."],"choiceTranslations":["スコットランドとアイルランドの人工湖。","昔人々が作った島。","大きな岩で作られた壁。","湖に架けられた橋。"],"answer":2,"choiceAnalysis":["人工湖→人工島であり湖ではない","昔作られた島→正解。💡 「small man-made islands」+「built long ago」","岩の壁→島であり壁ではない","湖の橋→橋は島と陸を繋ぐもの"],"grammar":"💡 man-made＝人工の。island＝島"},
             {"number":35,"question":"The discovery of some broken pots has","questionTranslation":"割れた壺の発見によって","choices":["allowed people to find out how the crannogs were built.","proved that there are more crannogs than scientists thought.","changed experts' ideas about how old some crannogs are.","shown that it may be too dangerous to dive in these lakes."],"choiceTranslations":["クランノグの建て方が分かった。","科学者が思ったより多くのクランノグがあると証明した。","一部のクランノグの年代に関する専門家の考えが変わった。","湖でのダイビングは危険すぎるかもしれないと示した。"],"answer":3,"choiceAnalysis":["建て方→壺は建設方法を示さない","数が多い→数の記述はない","年代の考えが変わった→正解。💡 3,000年前→5,000年以上前と年代観が変化","ダイビング危険→危険の記述なし"],"grammar":"💡 used to think＝かつて考えていた。much older＝もっと古い"},
             {"number":36,"question":"What do researchers think that the pots that they found were used for?","questionTranslation":"研究者は見つかった壺が何に使われたと考えていますか？","choices":["For decorating people's homes.","For important events.","To keep written records.","To catch fish in the lakes."],"choiceTranslations":["人々の家の装飾のため。","重要な行事のため。","文字の記録を残すため。","湖で魚を捕るため。"],"answer":2,"choiceAnalysis":["装飾→装飾の記述なし","重要な行事→正解。💡 「special ceremonies」＝特別な儀式＝important events","記録を残す→written recordsがない点に言及されているだけ","魚を捕る→釣りの記述なし"],"grammar":"💡 ceremony＝儀式。important events＝重要な行事（パラフレーズ）"},
             {"number":37,"question":"Why is it difficult to know the reason that the crannogs were made?","questionTranslation":"クランノグが作られた理由を知ることが難しいのはなぜですか？","choices":["Researchers think they lost some things that they found on them.","People may have damaged them when they built their homes.","Old pieces of wood might have been removed from them.","The people who made them probably moved away long ago."],"choiceTranslations":["研究者が見つけたものを失ったと考えている。","人々が家を建てた時に損傷した可能性がある。","古い木片が取り除かれた可能性がある。","作った人々はたぶん昔に引っ越した。"],"answer":2,"choiceAnalysis":["ものを失った→失くしたとは書いていない","家の建設で損傷→正解。💡 「they probably damaged the crannogs→made it difficult to find out why」","木片の除去→除去の記述なし","引っ越した→引っ越しの記述なし"],"grammar":"💡 damage＝損傷する。make it difficult to ～＝～することを困難にする"}
         ]
        }
    ]
}

data["sections"].append(s3)
data["sections"].append(s4)

# Vocabulary 42語
data["vocabulary"] = [
    {"word":"enough","meaning":"十分に","pos":"副詞","level":"準2級","example":"She didn't study enough for the exam.","distractors":["ほとんど","前方に","さえ"]},
    {"word":"details","meaning":"詳細","pos":"名詞","level":"準2級","example":"Please give me more details about the project.","distractors":["ラウンド","季節","車輪"]},
    {"word":"consist of","meaning":"～から成る","pos":"句動詞","level":"準2級","example":"The team consists of five members.","distractors":["警告する","夢見る","祈る"]},
    {"word":"seek","meaning":"探し求める","pos":"動詞","level":"準2級","example":"Many people seek better jobs in the city.","distractors":["送る","説明する","述べる"]},
    {"word":"form","meaning":"結成する、形成する","pos":"動詞","level":"準2級","example":"They decided to form a study group.","distractors":["持ち上げる","縫う","専攻する"]},
    {"word":"secret","meaning":"秘密の","pos":"形容詞","level":"準2級","example":"She kept her plan secret from everyone.","distractors":["不可能な","液体の","疲れる"]},
    {"word":"injury","meaning":"けが","pos":"名詞","level":"準2級","example":"He was out for a month due to a knee injury.","distractors":["気候","選択肢","称賛"]},
    {"word":"arrival","meaning":"到着","pos":"名詞","level":"準2級","example":"We are looking forward to her arrival next week.","distractors":["方向","材料","接続"]},
    {"word":"traffic","meaning":"交通","pos":"名詞","level":"準2級","example":"The traffic was so bad that I was late for work.","distractors":["入口","画像","化石"]},
    {"word":"hurry","meaning":"急ぐ","pos":"動詞","level":"準2級","example":"We need to hurry or we'll miss the bus.","distractors":["繰り返す","叩く","印刷する"]},
    {"word":"play a part in","meaning":"参加する、役割を果たす","pos":"熟語","level":"準2級","example":"Every member played a part in the team's success.","distractors":["いたずらする","追跡する","ペースについていく"]},
    {"word":"according to","meaning":"～によると","pos":"熟語","level":"準2級","example":"According to the news, it will rain tomorrow.","distractors":["望んで","合計して","隠れて"]},
    {"word":"hear from","meaning":"～から連絡がある","pos":"句動詞","level":"準2級","example":"I haven't heard from her in months.","distractors":["支払う","通り過ぎる","話し合う"]},
    {"word":"look up","meaning":"調べる","pos":"句動詞","level":"準2級","example":"You can look up the word in a dictionary.","distractors":["捨てる","持ち去る","貯める"]},
    {"word":"all the time","meaning":"いつも","pos":"熟語","level":"準2級","example":"He talks about sports all the time.","distractors":["ついに","最終的に","たまには"]},
    {"word":"curious","meaning":"好奇心の強い","pos":"形容詞","level":"準2級","example":"Children are naturally curious about the world.","distractors":["怒っている","悲しい","退屈した"]},
    {"word":"help yourself","meaning":"ご自由にどうぞ","pos":"熟語","level":"準2級","example":"Please help yourself to the snacks on the table.","distractors":["設定する","取る","着る"]},
    {"word":"retire","meaning":"退職する","pos":"動詞","level":"準2級","example":"She plans to retire at the age of 65.","distractors":["就職する","転職する","昇進する"]},
    {"word":"disappointed","meaning":"がっかりした","pos":"形容詞","level":"準2級","example":"He was disappointed with his test results.","distractors":["満足した","驚いた","興奮した"]},
    {"word":"pest","meaning":"害虫","pos":"名詞","level":"準2級","example":"Farmers use different methods to control pests.","distractors":["ペット","昆虫","家畜"]},
    {"word":"chemical","meaning":"化学薬品","pos":"名詞","level":"準2級","example":"Some chemicals are harmful to the environment.","distractors":["材料","成分","栄養素"]},
    {"word":"environment","meaning":"環境","pos":"名詞","level":"準2級","example":"We must protect the environment for future generations.","distractors":["経済","社会","政治"]},
    {"word":"solution","meaning":"解決策","pos":"名詞","level":"準2級","example":"We need to find a solution to this problem.","distractors":["原因","問題","質問"]},
    {"word":"remove","meaning":"除去する","pos":"動詞","level":"準2級","example":"Please remove your shoes before entering the house.","distractors":["加える","動かす","保管する"]},
    {"word":"advantage","meaning":"利点","pos":"名詞","level":"準2級","example":"One advantage of living here is the clean air.","distractors":["欠点","特徴","機能"]},
    {"word":"mystery","meaning":"謎","pos":"名詞","level":"準2級","example":"The disappearance of the ship remains a mystery.","distractors":["歴史","発見","事実"]},
    {"word":"discovery","meaning":"発見","pos":"名詞","level":"準2級","example":"The discovery of the new planet excited scientists.","distractors":["発明","改良","観察"]},
    {"word":"ceremony","meaning":"儀式、式典","pos":"名詞","level":"準2級","example":"The graduation ceremony was held in the school gym.","distractors":["パーティ","会議","講演"]},
    {"word":"damage","meaning":"損傷する、損害","pos":"動詞/名詞","level":"準2級","example":"The storm damaged many houses in the town.","distractors":["修理する","改善する","建設する"]},
    {"word":"continue","meaning":"続ける","pos":"動詞","level":"準2級","example":"She plans to continue studying after graduation.","distractors":["始める","やめる","変える"]},
    {"word":"license","meaning":"許可証、免許","pos":"名詞","level":"準2級","example":"You need a license to drive a car.","distractors":["チケット","パスポート","証明書"]},
    {"word":"reservation","meaning":"予約","pos":"名詞","level":"準2級","example":"I made a reservation at the restaurant for Friday.","distractors":["注文","確認","キャンセル"]},
    {"word":"researcher","meaning":"研究者","pos":"名詞","level":"準2級","example":"The researchers published their findings in a journal.","distractors":["学生","教師","管理者"]},
    {"word":"condition","meaning":"状態、条件","pos":"名詞","level":"準2級","example":"The old book was still in good condition.","distractors":["位置","場所","種類"]},
    {"word":"record","meaning":"記録","pos":"名詞","level":"準2級","example":"There are no written records from that time period.","distractors":["物語","報告","説明"]},
    {"word":"weigh","meaning":"重さがある","pos":"動詞","level":"準2級","example":"This suitcase weighs 20 kilograms.","distractors":["測る","量る","計算する"]},
    {"word":"purpose","meaning":"目的","pos":"名詞","level":"準2級","example":"What is the purpose of this meeting?","distractors":["結果","理由","方法"]},
    {"word":"ancient","meaning":"古代の","pos":"形容詞","level":"準2級","example":"The museum has a collection of ancient artifacts.","distractors":["現代の","中世の","近代の"]},
    {"word":"offer","meaning":"提供する","pos":"動詞","level":"準2級","example":"The company offers free shipping on all orders.","distractors":["要求する","拒否する","制限する"]},
    {"word":"include","meaning":"含む","pos":"動詞","level":"準2級","example":"The price includes breakfast and dinner.","distractors":["除外する","追加する","変更する"]},
    {"word":"sightseeing","meaning":"観光","pos":"名詞","level":"準2級","example":"We went sightseeing in Kyoto last weekend.","distractors":["買い物","食事","散歩"]},
    {"word":"countryside","meaning":"田舎","pos":"名詞","level":"準2級","example":"They moved to the countryside for a quieter life.","distractors":["都市","郊外","海岸"]}
]

# lessonPlan with 5 FocusPoints
# 既存FPにないもの: 仮定法wish, too...to構文はすでにあるが2022-1で使用, So do I倒置, consist of等
data["lessonPlan"] = {"focusPoints": [
    {"id":"fp1","title":"仮定法 I wish + 過去形","subtitle":"Subjunctive: I wish + Past Tense",
     "explanation":"「I wish + 仮定法過去（過去形）」は「（今）～ならいいのに」と、現実と反対の願望を表します。実際には実現しないことを望む表現です。",
     "sourceQuote":"He wishes he lived in a bigger place","sourceLocation":"Part 1 Q20",
     "examples":[
         {"en":"He wishes he lived in a bigger place.","ja":"もっと広い場所に住んでいればいいのにと思っている。","note":"wishes + lived（過去形）= 仮定法過去。実際は小さなアパートに住んでいる"},
         {"en":"I wish I could speak Spanish fluently.","ja":"スペイン語を流暢に話せたらいいのに。","note":"wish + could = ～できたらいいのに"},
         {"en":"She wishes she had more free time.","ja":"もっと自由な時間があればいいのに。","note":"wishes + had = 実際は忙しい"}
     ],
     "practicePassage":{"en":"[出典: Lost for Words 第2段落]\nOne day, Mr. Lopez asked Keiko to talk about her family in class. There were many things that she wanted to say, but she could not say them. She was disappointed because she did not know all the words that she needed. Mr. Lopez tried to cheer her up. He said that she is doing really well. If she keeps studying and practicing hard, she will soon find it easy to talk about anything.",
      "ja":"ある日、ロペス先生はケイコにクラスで家族について話すよう頼んだ。言いたいことがたくさんあったが、言えなかった。必要な単語をすべて知らなかったのでがっかりした。ロペス先生は彼女を励まそうとした。よくやっていると言い、勉強と練習を続ければすぐに何でも話せるようになると。",
      "audioFile":"audio/practice_pp1.mp3"},
     "practiceQuestions":[
         {"q":"「He wishes he lived」の lived はなぜ過去形？","a":"仮定法過去。現在の事実と反対の願望を表す時、wish節の動詞を過去形にする"},
         {"q":"「I wish I were rich.」でなぜ were？","a":"仮定法過去ではbe動詞は主語に関係なく were を使う（was も口語では可）"},
         {"q":"「I wish I had studied harder.」は何形ですか？","a":"仮定法過去完了。過去の事実と反対の願望。「もっと勉強すればよかった」"},
         {"q":"wish と hope の違いは？","a":"wish＝実現困難な願望（仮定法）。hope＝実現可能な期待（直説法）"}
     ],
     "highlightPatterns":[
         "She was disappointed because she did not know all the words that she needed",
         "If she keeps studying and practicing hard, she will soon find it easy to talk about anything"
     ],
     "highlightColor":"#4f8cff","highlightLabel":"仮定法"
    },
    {"id":"fp2","title":"So do I / Neither do I 倒置表現","subtitle":"Inverted Agreement: So/Neither + Aux + S",
     "explanation":"「So + 助動詞/be + S」は「Sもそうだ」、「Neither + 助動詞/be + S」は「Sもそうでない」を表す倒置表現です。前の文の動詞・時制に合わせて助動詞を選びます。",
     "sourceQuote":"So do I","sourceLocation":"Part 1 Q19",
     "examples":[
         {"en":"A: I have so much homework. B: So do I.","ja":"A: 宿題がたくさんある。B: 私もだよ。","note":"So do I = 私もそうだ（一般動詞have → do）"},
         {"en":"A: I am tired. B: So am I.","ja":"A: 疲れた。B: 私も。","note":"So am I = 私も（be動詞 → am）"},
         {"en":"A: I can't swim. B: Neither can I.","ja":"A: 泳げない。B: 私も泳げない。","note":"Neither can I = 私もできない（否定の同意）"}
     ],
     "practicePassage":{"en":"[出典: Pest Protection 第1段落]\nInsects and other animals often make trouble for farmers. Such animals are known as pests and can be a big problem. They eat the fruits and vegetables that should be sold as food. They also carry diseases to the plants grown on farms. The damage costs farmers a lot of money. Many farmers use chemicals to keep pests away. These chemicals can be bad for the environment, though. They can kill other creatures. They can also get into the fruits and vegetables that people eat.",
      "ja":"昆虫や他の動物はしばしば農家に迷惑をかける。そのような動物は害虫として知られ、大きな問題になりうる。食料として売られるべき果物や野菜を食べる。農場で育てられた植物に病気を運ぶ。被害は農家に多額の費用をかける。多くの農家は害虫を遠ざけるために化学薬品を使う。しかし化学薬品は環境に悪影響を与えることがある。",
      "audioFile":"audio/practice_pp2.mp3"},
     "practiceQuestions":[
         {"q":"「So do I」と「So I do」の違いは？","a":"So do I＝私もそうだ（同意の倒置）。So I do＝確かにそうだ（強調の肯定）"},
         {"q":"「I went to the park yesterday. So ___ she.」の空欄は？","a":"did。過去形の一般動詞 → So did she."},
         {"q":"否定文への同意「Neither ～」の使い方は？","a":"「I don't like coffee. Neither do I.」否定文＋Neither + 助動詞 + S"},
         {"q":"「Me too」と「So do I」の違いは？","a":"Me too はカジュアル。So do I はフォーマル。意味は同じ"}
     ],
     "highlightPatterns":[
         "Such animals are known as pests and can be a big problem",
         "Many farmers use chemicals to keep pests away"
     ],
     "highlightColor":"#34d399","highlightLabel":"倒置表現"
    },
    {"id":"fp3","title":"too...to 構文と enough to 構文","subtitle":"Too...to and Enough to Constructions",
     "explanation":"too + 形容詞/副詞 + (for 人) + to V は「（人にとって）…すぎて～できない」、形容詞 + enough + to V は「～するのに十分…だ」を表します。",
     "sourceQuote":"this box is too heavy for me to carry upstairs","sourceLocation":"Part 1 Q18",
     "examples":[
         {"en":"This box is too heavy for me to carry upstairs.","ja":"この箱は重すぎて2階に運べない。","note":"too heavy for me to carry = 重すぎて運べない"},
         {"en":"She is old enough to drive a car.","ja":"彼女は車を運転できる年齢だ。","note":"old enough to drive = 運転するのに十分な年齢"},
         {"en":"The water is too cold to swim in.","ja":"水が冷たすぎて泳げない。","note":"too cold to swim in = 冷たすぎて泳げない"}
     ],
     "practicePassage":{"en":"[出典: Pest Protection 第2-3段落]\nThe owners of the Vergenoegd Low wine farm in South Africa use a different method. They want to stop pests from eating their grapes. At the same time, they do not want any chemicals to get in their wine. Their solution is to use other animals to remove pests. Every day, a team of over 1,000 ducks is taken to the fields where the grapes are grown. The ducks spend all day walking around the plants and eating the pests.",
      "ja":"南アフリカのフェルゲヌーフド農場のオーナーは異なる方法を使っている。害虫がブドウを食べるのを止めたい。同時にワインに化学薬品を入れたくない。解決策は害虫除去に他の動物を使うことだ。毎日1,000羽以上のアヒルが畑に連れて行かれ、一日中害虫を食べる。",
      "audioFile":"audio/practice_pp3.mp3"},
     "practiceQuestions":[
         {"q":"「too heavy for me to carry」を so...that で言い換えると？","a":"so heavy that I cannot carry it（thatの後にit が必要）"},
         {"q":"「enough to」の語順の注意点は？","a":"形容詞/副詞+enough+to V。名詞の場合はenough+名詞。例：enough money to buy"},
         {"q":"「too...to」は常に否定の意味ですか？","a":"基本的にyes。「…すぎて～できない」だが、too...to be trueのように慣用表現もある"},
         {"q":"「The water was not warm enough to swim in.」を too で言い換えると？","a":"The water was too cold to swim in."}
     ],
     "highlightPatterns":[
         "They want to stop pests from eating their grapes",
         "Their solution is to use other animals to remove pests",
         "Every day, a team of over 1,000 ducks is taken to the fields where the grapes are grown"
     ],
     "highlightColor":"#f472b6","highlightLabel":"too/enough構文"
    },
    {"id":"fp4","title":"過去分詞による後置修飾","subtitle":"Post-modification with Past Participles",
     "explanation":"過去分詞（-ed形/不規則形）が名詞の後ろに置かれ、「～された」「～された状態の」という受動の意味で名詞を修飾します。関係代名詞+be動詞の省略と考えられます。",
     "sourceQuote":"the plants grown on farms","sourceLocation":"Part 3B 第1段落",
     "examples":[
         {"en":"They also carry diseases to the plants grown on farms.","ja":"農場で育てられた植物にも病気を運ぶ。","note":"plants grown = plants (which are) grown（過去分詞の後置修飾）"},
         {"en":"A bridge made of rocks connects them to the land.","ja":"岩でできた橋が陸地と繋がっている。","note":"bridge made of = bridge (which is) made of"},
         {"en":"Old pieces of wood from their houses have been found on the crannogs.","ja":"家の古い木片がクランノグ上で見つかっている。","note":"pieces of wood from houses = 家からの木片"}
     ],
     "practicePassage":{"en":"[出典: The Mystery of the Crannogs 第1段落]\nIn some lakes in Scotland and Ireland, there are small man-made islands. These are called crannogs, and they were built long ago with large rocks that were carried into the lakes. Building the crannogs was probably a lot of hard work because some of the rocks weigh 250 kilograms. What is more, the crannogs are between 10 and 30 meters wide and connected to the land by a bridge made of rocks. Although there are over a thousand of them, no one knows the reason why they were made.",
      "ja":"スコットランドとアイルランドのいくつかの湖には小さな人工島がある。これらはクランノグと呼ばれ、湖に運ばれた大きな岩で昔に作られた。一部の岩は250kgもあるため建設はかなりの重労働だった。さらに幅10～30mで、岩の橋で陸地と繋がっている。1,000以上あるが、なぜ作られたかは誰も知らない。",
      "audioFile":"audio/practice_pp4.mp3"},
     "practiceQuestions":[
         {"q":"「the plants grown on farms」を関係代名詞で書き換えると？","a":"the plants which are grown on farms"},
         {"q":"「a bridge made of rocks」の made は何形？","a":"過去分詞。make の過去分詞形 made が名詞 bridge を後ろから修飾"},
         {"q":"「the fruits and vegetables that people eat」は過去分詞修飾ですか？","a":"いいえ、これは関係代名詞thatによる修飾。能動態なので現在形のeat"},
         {"q":"過去分詞と現在分詞の後置修飾の違いは？","a":"過去分詞＝受動（～された）。現在分詞＝能動（～している）。broken window vs running water"}
     ],
     "highlightPatterns":[
         "the plants grown on farms",
         "connected to the land by a bridge made of rocks",
         "large rocks that were carried into the lakes",
         "old pieces of wood from their houses that have been found on the crannogs"
     ],
     "highlightColor":"#fbbf24","highlightLabel":"後置修飾"
    },
    {"id":"fp5","title":"make it + 形容詞 + to V 構文","subtitle":"Make it + Adjective + to V",
     "explanation":"「make it + 形容詞 + to V」は「～することを（形容詞に）する」を表します。itは仮目的語で、真の目的語はto V以下です。find it + 形容詞 + to Vも同じ構造です。",
     "sourceQuote":"This made it difficult to find out why the crannogs were built","sourceLocation":"Part 4B 第4段落",
     "examples":[
         {"en":"This made it difficult to find out why the crannogs were built.","ja":"これによりクランノグが建てられた理由の解明が困難になった。","note":"made it difficult to find out = 解明することを困難にした"},
         {"en":"She will soon find it easy to talk about anything.","ja":"すぐに何でも話すのが簡単だとわかるようになる。","note":"find it easy to talk = 話すことが簡単だとわかる"},
         {"en":"Technology has made it possible to work from home.","ja":"テクノロジーが在宅勤務を可能にした。","note":"made it possible to work = 働くことを可能にした"}
     ],
     "practicePassage":{"en":"[出典: The Mystery of the Crannogs 第3-4段落]\nThe pots were in good condition, and it was clear to researchers that they had not been used much before they were dropped in the lakes. The researchers believe that the pots were probably used for special ceremonies on the crannogs. It is not clear what the purpose of the ceremonies was, though, because there are no written records from the time when they were held. Two thousand years after the oldest crannogs were built, people began living on them. When these people built their houses, they probably damaged the crannogs. This made it difficult to find out why the crannogs were built.",
      "ja":"壺は良い状態で、湖に落とされる前にあまり使われていなかったことは研究者に明らかだった。壺は特別な儀式に使われたと考えられている。しかし文字の記録がないため儀式の目的は不明だ。最古のクランノグ建設から2,000年後に人々が住み始めた。家を建てた時にクランノグを損傷した可能性があり、建設理由の解明が困難になった。",
      "audioFile":"audio/practice_pp5.mp3"},
     "practiceQuestions":[
         {"q":"「made it difficult to find out」の it は何を指す？","a":"仮目的語。真の目的語は to find out 以下。it = to find out why the crannogs were built"},
         {"q":"「find it easy to talk」を it を使わずに書き換えると？","a":"find talking about anything easy（ただし不自然なのでit構文が好まれる）"},
         {"q":"「It is clear that ～」の it も仮主語ですか？","a":"はい。仮主語のit。真の主語はthat以下。「It was clear to researchers that they had not been used much」"},
         {"q":"make it + 形容詞 + for 人 + to V の例を作ると？","a":"The rain made it impossible for us to play outside.（雨のせいで外で遊べなくなった）"}
     ],
     "highlightPatterns":[
         "This made it difficult to find out why the crannogs were built",
         "she will soon find it easy to talk about anything",
         "it was clear to researchers that they had not been used much"
     ],
     "highlightColor":"#a78bfa","highlightLabel":"仮目的語it"
    }
]}

with open(os.path.join(base, "data.json"), "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
total_q = sum(len(s.get("questions",[])) for s in data["sections"]) + sum(len(p.get("questions",[])) for s in data["sections"] for p in s.get("passages",[]))
print(f"data.json: {total_q} questions, {len(data['vocabulary'])} vocab, {len(data['lessonPlan']['focusPoints'])} FPs")

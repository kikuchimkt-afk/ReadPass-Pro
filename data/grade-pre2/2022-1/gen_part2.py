"""Generate sections 2-3 (大問3+4) + vocabulary for 2022-1"""
import json, os
base = r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade-pre2\2022-1"
data = json.load(open(os.path.join(base, "_part1.json"), "r", encoding="utf-8"))

# Section 2: 大問3 passage-fill
section3 = {
    "name":"大問3","nameEn":"Part 3","type":"passage-fill",
    "instruction":"次の英文A，Bを読み，その文意にそって(26)から(30)までの(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選びなさい。",
    "passages":[
        {"label":"A","title":"Good Friends",
         "paragraphs":[
             "Hiroko and three of her friends have been working on a project for school. They have been doing research on the history of their town, and they must give a presentation about it in class next week. Every day after school, they have been getting together in the school library. They have been discussing what information to use and how to make a great presentation. They had some good ideas, and they were looking forward to ( 26 ).",
             "However, Hiroko broke her leg during volleyball practice yesterday. Now, she must stay in the hospital for five days. She called her friends and said that she was sorry for not being able to do anything more to help them with the presentation. They told her not to worry. They said that their teacher is going to make a video of their presentation. That way, Hiroko will be able to ( 27 ). Hiroko thanked her friends and wished them good luck."
         ],
         "translations":[
             "ヒロコと3人の友達は学校のプロジェクトに取り組んでいる。町の歴史について調査を行い、来週クラスで発表しなければならない。放課後毎日、学校の図書館に集まっている。どの情報を使うか、どうすれば素晴らしい発表ができるかを話し合ってきた。良いアイデアがあり、( 26 )を楽しみにしていた。",
             "しかし、ヒロコは昨日バレーボールの練習中に足を骨折した。今、5日間入院しなければならない。友達に電話して、発表の手伝いがもうできなくて申し訳ないと言った。友達は心配しないでと言った。先生が発表のビデオを撮ってくれるから、ヒロコも( 27 )ことができると言った。ヒロコは友達に感謝し、幸運を祈った。"
         ],
         "sentencePairs":[
             ["Hiroko and three of her friends have been working on a project for school.","ヒロコと3人の友達は学校のプロジェクトに取り組んでいる。"],
             ["They have been doing research on the history of their town.","町の歴史について調査を行っている。"],
             ["Every day after school, they have been getting together in the school library.","放課後毎日、学校の図書館に集まっている。"],
             ["They had some good ideas, and they were looking forward to it.","良いアイデアがあり、それを楽しみにしていた。"],
             ["However, Hiroko broke her leg during volleyball practice yesterday.","しかし、ヒロコは昨日バレーボールの練習中に足を骨折した。"],
             ["Now, she must stay in the hospital for five days.","今、5日間入院しなければならない。"],
             ["They told her not to worry.","友達は心配しないでと言った。"],
             ["Hiroko thanked her friends and wished them good luck.","ヒロコは友達に感謝し、幸運を祈った。"]
         ],
         "questions":[
             {"number":26,"choices":["talking in front of their classmates","making food for their teachers","performing their musical in public","seeing their book in bookstores"],"choiceTranslations":["クラスメートの前で話すこと","先生のために料理すること","公の場でミュージカルを演じること","本屋で自分たちの本を見ること"],"answer":1,"choiceAnalysis":["クラスメートの前で話す→正解。💡 「give a presentation about it in class」が根拠","先生のために料理→プロジェクトの内容と無関係","ミュージカルを演じる→研究発表であり演劇ではない","本屋で本を見る→本を書いた記述はない"],"grammar":"💡 look forward to ～ing＝～を楽しみにする（toの後は動名詞）。in front of＝～の前で"},
             {"number":27,"choices":["get well soon","watch it afterwards","take part as well","play other sports"],"choiceTranslations":["すぐに良くなる","後で見る","参加する","他のスポーツをする"],"answer":2,"choiceAnalysis":["すぐ良くなる→ビデオを撮る理由にならない","後で見る→正解。💡 ビデオを撮る＝入院中のヒロコが後で見られるようにするため","参加する→入院中なので参加はできない","他のスポーツ→骨折で入院中にスポーツはできない"],"grammar":"💡 afterwards＝後で。That way＝そうすれば。be able to＝～できる"}
         ]
        },
        {"label":"B","title":"Getting to Know New Orleans",
         "paragraphs":[
             "New Orleans is a city in the southern United States. In the past, people from France, Spain, Africa, and the Caribbean came to live there. As a result, it has a unique culture. This can be seen in the design of the city's buildings and heard in the city's music. Visitors can also experience this culture by ( 28 ) that come from New Orleans and the area around it. For example, visitors can get to know the city by eating foods like jambalaya. This is made from meat, seafood, vegetables, rice, and spices.",
             "New Orleans is also famous for cakes called beignets. A beignet is like a doughnut without a hole. Beignets are normally eaten for breakfast. However, they are served all day in cafes in an area of the city called the French Quarter. Cafe du Monde is the most famous of these. It has ( 29 ). In fact, it only sells beignets and drinks.",
             "People in New Orleans usually drink a kind of coffee called cafe au lait with their beignets. They use warm milk and a special type of coffee to make this. Long ago, coffee beans were very expensive. People looked for cheaper things that tasted like coffee, and they discovered a plant called chicory. The roots of this plant ( 30 ) coffee. Over time, the people of New Orleans came to love the taste of coffee made from a mixture of coffee beans and dried chicory roots."
         ],
         "translations":[
             "ニューオーリンズはアメリカ南部の都市だ。かつて、フランス、スペイン、アフリカ、カリブ海から人々がやって来た。その結果、独自の文化がある。それは建物のデザインに見られ、音楽に聞かれる。訪問者はニューオーリンズとその周辺地域の料理を( 28 )ことでもこの文化を体験できる。例えば、ジャンバラヤのような料理を食べることで街を知ることができる。",
             "ニューオーリンズはベニエと呼ばれるケーキでも有名だ。ベニエは穴のないドーナツのようなものだ。通常朝食に食べられるが、フレンチ・クォーターと呼ばれる地域のカフェでは一日中提供される。カフェ・デュ・モンドがその中で最も有名だ。( 29 )がある。実際、ベニエと飲み物しか売っていない。",
             "ニューオーリンズの人々は通常、ベニエと一緒にカフェオレと呼ばれるコーヒーを飲む。温かい牛乳と特別な種類のコーヒーで作る。昔、コーヒー豆はとても高価だった。人々はコーヒーに似た味のもっと安いものを探し、チコリという植物を発見した。この植物の根はコーヒーと( 30 )味がする。時が経つにつれ、ニューオーリンズの人々はコーヒー豆と乾燥チコリの根を混ぜたコーヒーの味を好むようになった。"
         ],
         "sentencePairs":[
             ["New Orleans is a city in the southern United States.","ニューオーリンズはアメリカ南部の都市だ。"],
             ["In the past, people from France, Spain, Africa, and the Caribbean came to live there.","かつて、フランス、スペイン、アフリカ、カリブ海から人々がやって来た。"],
             ["As a result, it has a unique culture.","その結果、独自の文化がある。"],
             ["This can be seen in the design of the city's buildings and heard in the city's music.","それは建物のデザインに見られ、音楽に聞かれる。"],
             ["This is made from meat, seafood, vegetables, rice, and spices.","これは肉、魚介類、野菜、米、スパイスから作られる。"],
             ["A beignet is like a doughnut without a hole.","ベニエは穴のないドーナツのようなものだ。"],
             ["Beignets are normally eaten for breakfast.","通常朝食に食べられる。"],
             ["Cafe du Monde is the most famous of these.","カフェ・デュ・モンドがその中で最も有名だ。"],
             ["In fact, it only sells beignets and drinks.","実際、ベニエと飲み物しか売っていない。"],
             ["Long ago, coffee beans were very expensive.","昔、コーヒー豆はとても高価だった。"],
             ["People looked for cheaper things that tasted like coffee, and they discovered a plant called chicory.","人々はコーヒーに似た味のもっと安いものを探し、チコリという植物を発見した。"],
             ["Over time, the people of New Orleans came to love the taste of coffee made from a mixture of coffee beans and dried chicory roots.","時が経つにつれ、コーヒー豆と乾燥チコリの根を混ぜたコーヒーの味を好むようになった。"]
         ],
         "questions":[
             {"number":28,"choices":["hearing the stories","meeting the people","driving the cars","tasting the dishes"],"choiceTranslations":["物語を聞くこと","人々に会うこと","車を運転すること","料理を味わうこと"],"answer":4,"choiceAnalysis":["物語を聞く→食のeating foodsの例と繋がらない","人々に会う→料理の文脈に合わない","車を運転する→文化体験として不適切","料理を味わう→正解。💡 次文で「eating foods like jambalaya」と具体例が続く"],"grammar":"💡 taste＝味わう。dish＝料理。experience ～ by ～ing＝～することで～を体験する"},
             {"number":29,"choices":["the highest prices","special tables and chairs","a simple menu","only one waiter"],"choiceTranslations":["最も高い値段","特別なテーブルと椅子","シンプルなメニュー","ウェイターが1人だけ"],"answer":3,"choiceAnalysis":["最高価格→「ベニエと飲み物しか売らない」とは矛盾しない但し根拠なし","特別な家具→メニューの話に続く流れに合わない","シンプルなメニュー→正解。💡 「only sells beignets and drinks」＝メニューがシンプル","ウェイター1人→次文の内容と繋がらない"],"grammar":"💡 simple＝シンプルな。menu＝メニュー。In fact＝実際"},
             {"number":30,"choices":["contain more vitamins than","have a similar flavor to","grow well in bags of","can be used as cups for"],"choiceTranslations":["～より多くのビタミンを含む","～と似た風味がある","～の袋でよく育つ","～のカップとして使える"],"answer":2,"choiceAnalysis":["ビタミンが多い→味の代替品を探す文脈と無関係","似た風味がある→正解。💡 コーヒーに似た味のものを探した→チコリの根はコーヒーに似た風味","袋で育つ→コーヒーの代替品の文脈に不適切","カップとして使える→根の用途として不自然"],"grammar":"💡 have a similar flavor to ～＝～と似た風味がある。similar＝似ている。flavor＝風味"}
         ]
        }
    ]
}

# Section 3: 大問4 reading-comprehension
section4 = {
    "name":"大問4","nameEn":"Part 4","type":"reading-comprehension",
    "instruction":"次の英文A，Bの内容に関して，(31)から(37)までの質問に対して最も適切なもの，または文を完成させるのに最も適切なものを1，2，3，4の中から一つ選びなさい。",
    "passages":[
        {"label":"A","title":"Visit to Museum","format":"email",
         "meta":{"from":"Jenny Smith","to":"Ai Tanaka","date":"June 5","subject":"Visit to museum"},
         "paragraphs":[
             "How are things in Japan? I hope that you had fun by the ocean last month. I know how much you love swimming and playing in the sand with your friends. I had a great vacation, too. Last week, I stayed with my aunt and uncle in Pennsylvania. They live on a farm about 50 kilometers from a city called Pittsburgh. My brother and I enjoyed playing outside in nature.",
             "One day, it rained, so we decided to go into the city and see the natural history museum there. The museum was cool because it has many dinosaur bones. It also has an amazing collection of colorful rocks. My favorite part was the \"PaleoLab,\" though. There, scientists prepare old bones from dinosaurs and other animals for the museum. The scientists work in a special room with a large window, so museum visitors can watch them.",
             "My mom says there is a natural history museum here in Chicago, too. She said that she would take you, me, and my brother there when you come to visit the United States next month. We can spend the whole day at the museum if we go early. Let me know if you're interested. I can't wait to see you!"
         ],
         "translations":[
             "日本はどう？先月海で楽しんだ？泳いだり友達と砂遊びするのが大好きなの知ってるよ。私も素晴らしい休暇だった。先週、ペンシルベニアの叔母と叔父の家に泊まったの。ピッツバーグという街から約50キロの農場に住んでいるの。弟と自然の中で外遊びを楽しんだよ。",
             "ある日雨が降ったので、街に行って自然史博物館を見ることにした。恐竜の骨がたくさんあってすごかった。色とりどりの石のコレクションも素晴らしかった。でも一番好きだったのは「パレオラボ」。そこでは科学者が恐竜や他の動物の古い骨を博物館用に準備している。大きな窓のある特別な部屋で作業するから、来館者は見学できるの。",
             "ママがシカゴにも自然史博物館があるって言ってた。来月あなたがアメリカに来る時、私たちを連れて行ってくれるって。早く行けば一日中博物館で過ごせるよ。興味があったら教えてね。会えるのが待ちきれない！"
         ],
         "sentencePairs":[
             ["I hope that you had fun by the ocean last month.","先月海で楽しんだ？"],
             ["Last week, I stayed with my aunt and uncle in Pennsylvania.","先週、ペンシルベニアの叔母と叔父の家に泊まった。"],
             ["They live on a farm about 50 kilometers from a city called Pittsburgh.","ピッツバーグという街から約50キロの農場に住んでいる。"],
             ["My brother and I enjoyed playing outside in nature.","弟と自然の中で外遊びを楽しんだ。"],
             ["One day, it rained, so we decided to go into the city and see the natural history museum there.","ある日雨が降ったので、街に行って自然史博物館を見ることにした。"],
             ["The museum was cool because it has many dinosaur bones.","恐竜の骨がたくさんあってすごかった。"],
             ["My favorite part was the \"PaleoLab,\" though.","でも一番好きだったのは「パレオラボ」。"],
             ["The scientists work in a special room with a large window, so museum visitors can watch them.","大きな窓のある特別な部屋で作業するから、来館者は見学できる。"],
             ["She said that she would take you, me, and my brother there when you come to visit the United States next month.","来月アメリカに来る時、私たちを連れて行ってくれるって。"],
             ["I can't wait to see you!","会えるのが待ちきれない！"]
         ],
         "questions":[
             {"number":31,"question":"Last month, Ai","questionTranslation":"先月、アイは","choices":["spent some time at a beach.","started taking swimming lessons.","visited her family in Pittsburgh.","played outside with her brother."],"choiceTranslations":["海で過ごした。","水泳のレッスンを始めた。","ピッツバーグの家族を訪ねた。","弟と外で遊んだ。"],"answer":1,"choiceAnalysis":["海で過ごした→正解。💡 「you had fun by the ocean last month」が根拠","水泳レッスン→レッスンの言及なし","ピッツバーグ訪問→ジェニーがペンシルベニアに行った","弟と外遊び→ジェニーの話"],"grammar":"💡 by the ocean＝海のそばで。at a beach＝ビーチで（パラフレーズ）"},
             {"number":32,"question":"What did Jenny like best about the museum?","questionTranslation":"ジェニーが博物館で一番好きだったのは何ですか？","choices":["Watching scientists get bones ready for the museum.","Listening to a cool talk about some dinosaur bones.","Its amazing collection of colorful rocks.","Its windows were large and let in a lot of light."],"choiceTranslations":["科学者が骨を博物館用に準備するのを見ること。","恐竜の骨についてのかっこいい話を聞くこと。","色とりどりの石の素晴らしいコレクション。","大きな窓で光がたくさん入ること。"],"answer":1,"choiceAnalysis":["科学者が骨を準備するのを見る→正解。💡 「My favorite part was the PaleoLab」＋「scientists prepare old bones」が根拠","恐竜の骨の話を聞く→講演の記述なし","石のコレクション→amazingだが favorite partはPaleoLab","大きな窓→窓は見学のための設備で好きな理由ではない"],"grammar":"💡 get ～ ready＝～を準備する = prepare"},
             {"number":33,"question":"What is Ai going to do next month?","questionTranslation":"アイは来月何をする予定ですか？","choices":["Move to Chicago with her family.","Take a trip abroad to see Jenny.","Get up early to attend an event.","Start working in a history museum."],"choiceTranslations":["家族とシカゴに引っ越す。","ジェニーに会いに海外旅行する。","イベントに参加するため早起きする。","歴史博物館で働き始める。"],"answer":2,"choiceAnalysis":["シカゴに引っ越す→引っ越しの記述なし","海外旅行してジェニーに会う→正解。💡 「when you come to visit the United States next month」が根拠","早起きしてイベント参加→早く行けば一日中過ごせるが予定ではない","博物館で働く→見学であって就職ではない"],"grammar":"💡 take a trip abroad＝海外旅行する。visit the United States＝アメリカを訪問する"}
         ]
        },
        {"label":"B","title":"The Return of the Wolves",
         "paragraphs":[
             "Wolves are intelligent animals that live in groups called packs. Long ago, packs of wolves could be found in many European countries, including Germany. However, farmers hunted wolves because they sometimes killed the farmers' sheep. Other people hunted wolves for sport. By the 19th century, there were no wolves left in Germany. In the last 20 years, though, wolves have started to return to the country.",
             "In the 1980s and 1990s, European countries made laws to protect wildlife and created special areas for wild animals. At the same time, many people left their farms in eastern Europe to take jobs abroad. The result was that there were fewer people and more safe places for deer and other animals that wolves like to eat. As the number of these animals increased, the number of wolves increased, too. The wolves spread west, and in 2001, they were found living in Germany again.",
             "There are now over 120 packs of wolves in Germany, but not all of them live in the special areas for wild animals. A lot of wolves prefer places that the army uses for training. Experts think this is because these places are safe for the wolves. It seems that some people have been hunting wolves in Germany, even though they are not allowed to. However, these people are afraid of entering army training centers because they might get caught.",
             "Other animals, including rare birds, have also been protected by army training centers. There used to be many army training centers in Europe. However, some of them are no longer needed. In 2015, the German government created parks for wildlife from 62 old army training centers. This increased the total size of such parks in the country by 25 percent. Now, there are plans to bring back horses, bison, and other wild animals to these parks, too."
         ],
         "translations":[
             "オオカミはパックと呼ばれる群れで生活する知的な動物だ。昔、ドイツを含む多くのヨーロッパ諸国でオオカミの群れが見られた。しかし、農家の羊を殺すことがあったため、農家はオオカミを狩った。スポーツとして狩る人もいた。19世紀までにドイツにはオオカミがいなくなった。しかし、ここ20年でオオカミは戻り始めた。",
             "1980年代と1990年代、ヨーロッパ諸国は野生生物を守る法律を作り、野生動物のための特別区域を作った。同時に、東ヨーロッパでは多くの人が海外で仕事をするために農場を離れた。その結果、人が少なくなり、オオカミが好むシカなどの動物にとって安全な場所が増えた。これらの動物の数が増えると、オオカミの数も増えた。オオカミは西に広がり、2001年にドイツで再び見つかった。",
             "現在ドイツには120以上のオオカミの群れがいるが、すべてが野生動物のための特別区域に住んでいるわけではない。多くのオオカミは軍の訓練場を好む。専門家はこれらの場所がオオカミにとって安全だからだと考えている。禁止されているにもかかわらず、ドイツでオオカミを狩っている人がいるようだ。しかし、これらの人々は捕まる可能性があるため、軍の訓練施設に入ることを恐れている。",
             "希少な鳥を含む他の動物も軍の訓練施設によって保護されてきた。ヨーロッパには多くの軍の訓練施設があったが、もう必要のないものもある。2015年、ドイツ政府は62の古い軍の訓練施設から野生生物のための公園を作った。これにより、国内のそのような公園の総面積が25%増加した。今では、馬やバイソンなどの野生動物もこれらの公園に戻す計画がある。"
         ],
         "sentencePairs":[
             ["Wolves are intelligent animals that live in groups called packs.","オオカミはパックと呼ばれる群れで生活する知的な動物だ。"],
             ["However, farmers hunted wolves because they sometimes killed the farmers' sheep.","しかし、農家の羊を殺すことがあったため、農家はオオカミを狩った。"],
             ["By the 19th century, there were no wolves left in Germany.","19世紀までにドイツにはオオカミがいなくなった。"],
             ["European countries made laws to protect wildlife and created special areas for wild animals.","ヨーロッパ諸国は野生生物を守る法律を作り、特別区域を作った。"],
             ["Many people left their farms in eastern Europe to take jobs abroad.","東ヨーロッパでは多くの人が海外で仕事をするために農場を離れた。"],
             ["As the number of these animals increased, the number of wolves increased, too.","これらの動物の数が増えると、オオカミの数も増えた。"],
             ["The wolves spread west, and in 2001, they were found living in Germany again.","オオカミは西に広がり、2001年にドイツで再び見つかった。"],
             ["A lot of wolves prefer places that the army uses for training.","多くのオオカミは軍の訓練場を好む。"],
             ["These people are afraid of entering army training centers because they might get caught.","捕まるかもしれないので訓練施設に入ることを恐れている。"],
             ["In 2015, the German government created parks for wildlife from 62 old army training centers.","2015年にドイツ政府は62の古い訓練施設から公園を作った。"],
             ["This increased the total size of such parks in the country by 25 percent.","これにより国内の公園の総面積が25%増加した。"]
         ],
         "questions":[
             {"number":34,"question":"What is one reason that wolves disappeared from Germany?","questionTranslation":"オオカミがドイツから消えた理由の一つは何ですか？","choices":["They were hunted to stop them from killing farm animals.","The animals that wolves ate were all killed by farmers.","Farmers in Germany started keeping cows instead of sheep.","People made farms in the places where the wolves lived."],"choiceTranslations":["家畜を殺すのを止めるために狩られた。","オオカミが食べる動物がすべて農家に殺された。","ドイツの農家が羊の代わりに牛を飼い始めた。","オオカミが住んでいた場所に農場を作った。"],"answer":1,"choiceAnalysis":["家畜を殺すのを止めるため狩られた→正解。💡 「farmers hunted wolves because they sometimes killed the farmers' sheep」が根拠","食べる動物が全部殺された→そのような記述なし","牛の飼育→牛の記述なし","農場を作った→農場がオオカミの生息地を侵したとは書いていない"],"grammar":"💡 hunt＝狩る。disappear＝消える。farm animals＝家畜（sheepのパラフレーズ）"},
             {"number":35,"question":"Why did many people in eastern Europe leave their farms in the 1980s and 1990s?","questionTranslation":"1980年代と1990年代に東ヨーロッパの多くの人が農場を離れたのはなぜですか？","choices":["Their farms were bought to create areas for wild animals.","The number of wolves and other animals suddenly increased.","New laws in European countries said that they had to leave.","They had chances to go and work in other countries."],"choiceTranslations":["野生動物のための区域を作るため農場が買い取られた。","オオカミや他の動物の数が突然増えた。","ヨーロッパの新しい法律で立ち退かなければならなくなった。","他の国で働く機会があった。"],"answer":4,"choiceAnalysis":["農場が買い取られた→そのような記述なし","動物が突然増えた→人が去った結果であり原因ではない","法律で立ち退き→法律は野生生物保護であり立ち退きではない","他の国で働く機会→正解。💡 「to take jobs abroad」が根拠"],"grammar":"💡 take jobs abroad＝海外で仕事をする。chance＝機会（パラフレーズ）"},
             {"number":36,"question":"Many wolves prefer living in army training centers because","questionTranslation":"多くのオオカミが軍の訓練施設を好むのは","choices":["the soldiers at the centers give them food from the kitchens.","people who hunt them are too scared to go in the centers.","a lot of people visit the special areas for wild animals.","there are fewer roads than in other parts of Germany."],"choiceTranslations":["施設の兵士が台所から餌をくれるから。","狩りをする人が施設に入るのを恐れているから。","特別区域を訪れる人が多いから。","ドイツの他の地域より道路が少ないから。"],"answer":2,"choiceAnalysis":["兵士が餌をくれる→そのような記述なし","狩りをする人が入るのを恐れる→正解。💡 「these people are afraid of entering army training centers」が根拠","訪問者が多い→特別区域の訪問者の記述なし","道路が少ない→道路の記述なし"],"grammar":"💡 be afraid of ～ing＝～するのを恐れる。be scared to ～＝～するのが怖い（パラフレーズ）"},
             {"number":37,"question":"The German government","questionTranslation":"ドイツ政府は","choices":["plans to open 62 new army training centers.","moved some rare birds to protect them.","brought horses and bison to parks in 2015.","has provided more land for wild animals."],"choiceTranslations":["62の新しい軍の訓練施設を開く計画がある。","希少な鳥を移動させて保護した。","2015年に馬とバイソンを公園に連れてきた。","野生動物により多くの土地を提供した。"],"answer":4,"choiceAnalysis":["62の新施設を開く→古い施設を公園に転換したのであり新設ではない","鳥を移動→鳥の移動の記述なし","2015年に馬とバイソン→馬とバイソンは将来の計画","より多くの土地を提供→正解。💡 「increased the total size of such parks by 25 percent」が根拠"],"grammar":"💡 provide＝提供する。land＝土地。increase by 25%＝25%増加する"}
         ]
        }
    ]
}

data["sections"].append(section3)
data["sections"].append(section4)

# Vocabulary (42語)
data["vocabulary"] = [
    {"word":"warning","meaning":"警告","pos":"名詞","level":"準2級","example":"The sign gave a warning about the dangerous road.","distractors":["チャンネル","日陰","種類"]},
    {"word":"friendship","meaning":"友情","pos":"名詞","level":"準2級","example":"Their friendship has lasted for over 20 years.","distractors":["知識","供給","免許"]},
    {"word":"additional","meaning":"追加の","pos":"形容詞","level":"準2級","example":"We need additional information to make a decision.","distractors":["平和な","才能のある","否定的な"]},
    {"word":"push","meaning":"押す、強く促す","pos":"動詞","level":"準2級","example":"Her parents pushed her to study harder for the exam.","distractors":["祝う","満たす","逃げる"]},
    {"word":"reach","meaning":"到着する、届く","pos":"動詞","level":"準2級","example":"We finally reached the top of the mountain after hours of hiking.","distractors":["測る","数える","約束する"]},
    {"word":"achievement","meaning":"達成、業績","pos":"名詞","level":"準2級","example":"Winning the award was a great achievement for the young scientist.","distractors":["退職","治療","装備"]},
    {"word":"eventually","meaning":"最終的に","pos":"副詞","level":"準2級","example":"After many tries, she eventually passed the driving test.","distractors":["めったに","重く","明るく"]},
    {"word":"courage","meaning":"勇気","pos":"名詞","level":"準2級","example":"It took a lot of courage to speak in front of 500 people.","distractors":["ファッション","教育","平均"]},
    {"word":"scream","meaning":"叫ぶ","pos":"動詞","level":"準2級","example":"The children screamed with excitement on the roller coaster.","distractors":["飾る","収穫する","卒業する"]},
    {"word":"pretend","meaning":"ふりをする","pos":"動詞","level":"準2級","example":"The boy pretended to be asleep when his mother came in.","distractors":["期待する","爆発する","抗議する"]},
    {"word":"succeed in","meaning":"～に成功する","pos":"句動詞","level":"準2級","example":"She succeeded in passing the entrance exam.","distractors":["不満を言う","入ってくる","味方する"]},
    {"word":"in the distance","meaning":"遠くに","pos":"熟語","level":"準2級","example":"We could see the mountains in the distance.","distractors":["放送中","概して","せいぜい"]},
    {"word":"aside from","meaning":"～以外に","pos":"熟語","level":"準2級","example":"Aside from English, she also speaks French and Spanish.","distractors":["～と比べて","～に基づいて","～の近くに"]},
    {"word":"after a while","meaning":"しばらくして","pos":"熟語","level":"準2級","example":"After a while, the rain stopped and the sun came out.","distractors":["一言で言えば","最善のために","ところで"]},
    {"word":"take risks","meaning":"リスクを冒す","pos":"熟語","level":"準2級","example":"You need to take risks sometimes to achieve your goals.","distractors":["努力する","進歩する","開催される"]},
    {"word":"on fire","meaning":"火事で、燃えている","pos":"熟語","level":"準2級","example":"The building was on fire, and firefighters rushed to the scene.","distractors":["運良く","海上で","売り出し中"]},
    {"word":"on purpose","meaning":"わざと","pos":"熟語","level":"準2級","example":"I didn't break the vase on purpose. It was an accident.","distractors":["助けを借りて","無料で","所定の位置に"]},
    {"word":"reservation","meaning":"予約","pos":"名詞","level":"準2級","example":"I made a reservation at the restaurant for 7 p.m.","distractors":["予約（医者）","会議","荷物"]},
    {"word":"aquarium","meaning":"水族館","pos":"名詞","level":"準2級","example":"The children loved watching the dolphins at the aquarium.","distractors":["川","博物館","ギフトショップ"]},
    {"word":"co-worker","meaning":"同僚","pos":"名詞","level":"準2級","example":"She went out for lunch with her co-workers.","distractors":["上司","部下","顧客"]},
    {"word":"presentation","meaning":"発表、プレゼン","pos":"名詞","level":"準2級","example":"He gave a presentation about the company's new product.","distractors":["レポート","実験","討論"]},
    {"word":"research","meaning":"調査、研究","pos":"名詞","level":"準2級","example":"The scientists did research on new ways to clean water.","distractors":["講義","報告","試験"]},
    {"word":"discuss","meaning":"話し合う","pos":"動詞","level":"準2級","example":"We need to discuss the plan before we start.","distractors":["発表する","実験する","調べる"]},
    {"word":"unique","meaning":"独自の、ユニークな","pos":"形容詞","level":"準2級","example":"Each country has its own unique culture and traditions.","distractors":["一般的な","普通の","単純な"]},
    {"word":"experience","meaning":"体験する、経験","pos":"動詞/名詞","level":"準2級","example":"You should experience the local food when you travel.","distractors":["観察する","想像する","記録する"]},
    {"word":"discover","meaning":"発見する","pos":"動詞","level":"準2級","example":"Scientists discovered a new species of fish in the deep sea.","distractors":["発明する","改良する","模倣する"]},
    {"word":"mixture","meaning":"混合物","pos":"名詞","level":"準2級","example":"The cake is made from a mixture of flour, sugar, and eggs.","distractors":["材料","分量","容器"]},
    {"word":"intelligent","meaning":"知的な","pos":"形容詞","level":"準2級","example":"Dolphins are known as very intelligent animals.","distractors":["危険な","野生の","巨大な"]},
    {"word":"hunt","meaning":"狩る","pos":"動詞","level":"準2級","example":"In some countries, people still hunt deer for food.","distractors":["飼う","追い払う","捕まえる"]},
    {"word":"wildlife","meaning":"野生生物","pos":"名詞","level":"準2級","example":"The park was created to protect wildlife in the area.","distractors":["家畜","ペット","害虫"]},
    {"word":"increase","meaning":"増える、増やす","pos":"動詞","level":"準2級","example":"The number of tourists has increased over the past decade.","distractors":["減少する","維持する","変化する"]},
    {"word":"spread","meaning":"広がる","pos":"動詞","level":"準2級","example":"The fire spread quickly through the forest.","distractors":["縮小する","停止する","集中する"]},
    {"word":"prefer","meaning":"好む","pos":"動詞","level":"準2級","example":"I prefer tea to coffee in the morning.","distractors":["嫌う","避ける","無視する"]},
    {"word":"expert","meaning":"専門家","pos":"名詞","level":"準2級","example":"The expert explained the effects of climate change.","distractors":["初心者","見習い","愛好家"]},
    {"word":"allow","meaning":"許可する","pos":"動詞","level":"準2級","example":"Students are not allowed to use phones during class.","distractors":["禁止する","強制する","要求する"]},
    {"word":"government","meaning":"政府","pos":"名詞","level":"準2級","example":"The government announced a new plan to reduce pollution.","distractors":["企業","学校","病院"]},
    {"word":"total","meaning":"合計の","pos":"形容詞","level":"準2級","example":"The total cost of the project was $5 million.","distractors":["部分的な","最小の","平均的な"]},
    {"word":"dinosaur","meaning":"恐竜","pos":"名詞","level":"準2級","example":"Children are often fascinated by dinosaurs.","distractors":["昆虫","魚類","爬虫類"]},
    {"word":"collection","meaning":"コレクション、収集","pos":"名詞","level":"準2級","example":"The museum has an impressive collection of modern art.","distractors":["展示","展覧会","入場料"]},
    {"word":"scientist","meaning":"科学者","pos":"名詞","level":"準2級","example":"The scientist won a Nobel Prize for his research.","distractors":["芸術家","技術者","教授"]},
    {"word":"flavor","meaning":"風味、味","pos":"名詞","level":"準2級","example":"This tea has a mild, sweet flavor.","distractors":["色","香り","食感"]},
    {"word":"rare","meaning":"希少な、珍しい","pos":"形容詞","level":"準2級","example":"This bird is very rare and can only be found in this forest.","distractors":["一般的な","普通の","多い"]}
]

with open(os.path.join(base, "_part2.json"), "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
total_q = sum(len(s.get("questions",[])) for s in data["sections"]) + sum(len(p.get("questions",[])) for s in data["sections"] for p in s.get("passages",[]))
print(f"Part 2: {total_q} questions, {len(data['vocabulary'])} vocab")

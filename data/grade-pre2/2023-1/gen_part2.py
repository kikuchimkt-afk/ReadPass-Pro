"""準2級 2023-1 Part 2: 大問3 + 大問4"""
import json
d = json.load(open(r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade-pre2\2023-1\_part1.json","r",encoding="utf-8"))

# ===== 大問3: passage-fill (旧形式 A:2問 B:3問) =====
sec3 = {"name":"大問3","type":"passage-fill",
    "instruction":"次の英文A，Bを読み，その文意にそって(26)から(30)までの(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選び，その番号を解答用紙の所定欄にマークしなさい。",
    "passages":[
        {"label":"A","title":"Sally's Concert",
         "paragraphs":[
             "Sally has been taking piano lessons for about a year. She started because she heard her uncle Kevin playing when she visited his house. She thought that his music sounded wonderful. Sally has been practicing hard and learning quickly. Her teacher told her that there would be a concert for the students at the piano school and that Sally should take part. Sally ( 26 ), though. She thought that performing in public would be scary. However, her teacher said that it would be a good experience.",
             "At the concert, Sally's parents and Uncle Kevin were in the audience. When it was time for Sally to play, she was worrying a lot. Her teacher told her to relax and enjoy the chance to ( 27 ). Sally did her best. When she finished playing, all the people in the audience were smiling, clapping, and cheering. This made Sally feel very special, and she knew that her teacher had been right."
         ],
         "translations":[
             "サリーは約1年間ピアノのレッスンを受けている。叔父のケビンの家を訪ねた時に彼が弾いているのを聞いたのがきっかけだった。彼の音楽は素晴らしいと思った。サリーは一生懸命練習し、すぐに上達した。先生はピアノ教室の生徒のためのコンサートがあり、サリーも参加すべきだと言った。しかしサリーは（26）。人前で演奏するのは怖いと思っていた。しかし先生はそれが良い経験になると言った。",
             "コンサートでは、サリーの両親とケビンおじさんが観客席にいた。サリーの出番が来た時、彼女はとても心配していた。先生はリラックスして（27）チャンスを楽しむようにと言った。サリーは最善を尽くした。演奏が終わると、観客全員が笑顔で拍手し、歓声を上げていた。これでサリーはとても特別な気持ちになり、先生が正しかったことを知った。"
         ],
         "sentencePairs":[
             ["Sally has been taking piano lessons for about a year.","サリーは約1年間ピアノのレッスンを受けている。"],
             ["She started because she heard her uncle Kevin playing when she visited his house.","叔父のケビンの家を訪ねた時に彼が弾いているのを聞いたのがきっかけだった。"],
             ["She thought that his music sounded wonderful.","彼の音楽は素晴らしいと思った。"],
             ["Sally has been practicing hard and learning quickly.","サリーは一生懸命練習し、すぐに上達した。"],
             ["However, her teacher said that it would be a good experience.","しかし先生はそれが良い経験になると言った。"],
             ["When it was time for Sally to play, she was worrying a lot.","サリーの出番が来た時、彼女はとても心配していた。"],
             ["Sally did her best.","サリーは最善を尽くした。"],
             ["When she finished playing, all the people in the audience were smiling, clapping, and cheering.","演奏が終わると、観客全員が笑顔で拍手し、歓声を上げていた。"],
             ["This made Sally feel very special, and she knew that her teacher had been right.","これでサリーはとても特別な気持ちになり、先生が正しかったことを知った。"]
         ],
         "questions":[
             {"number":26,"choices":["could not see anything","had to ask her parents","did not have much money","was very nervous"],"answer":4,
              "choiceAnalysis":{"1":"何も見えなかったは文脈に合わない。","2":"両親に聞くは文脈に合わない。","3":"お金がないは無関係。","4":"was very nervous が正解。performing in public / scary に対応。"},
              "grammar":{"point":"nervous（緊張している）","detail":"scared / worried と同様に感情を表す形容詞。"},
              "choiceTranslations":["何も見えなかった","両親に聞かなければならなかった","あまりお金がなかった","とても緊張していた"]},
             {"number":27,"choices":["visit foreign countries","make other people happy","listen to famous pianists","help sick children"],"answer":2,
              "choiceAnalysis":{"1":"外国訪問はコンサートに無関係。","2":"make other people happy が正解。演奏で聴衆を喜ばせる文脈に対応。","3":"有名ピアニストを聴くは演奏側の文脈に合わない。","4":"病気の子供を助けるは無関係。"},
              "grammar":{"point":"make + O + 形容詞","detail":"「Oを～にする」使役構文。make people happy。"},
              "choiceTranslations":["外国を訪れる","他の人を幸せにする","有名なピアニストを聴く","病気の子供を助ける"]}
         ]},
        {"label":"B","title":"Up and Away",
         "paragraphs":[
             "Cars that can fly have appeared in many science-fiction stories. For over 100 years, people have been trying to build real flying cars. Some have succeeded, but their flying cars have never been produced in large numbers. These cars were usually too expensive for people to buy. However, a company in the European country of Slovakia thinks that its flying cars can be made ( 28 ). As a result, it might soon be common to see flying cars in the sky.",
             "Stefan Klein, the owner of the company, has spent about 30 years trying to develop a flying car. In June 2021, Klein's car ( 29 ). It took 35 minutes to travel about 90 kilometers from the airport in Nitra to the one in Bratislava. After it landed, the flying car's wings were folded up in less than three minutes, and Klein drove the car to the city center. The car has now been flown over 200 times, and the government of Slovakia has decided to allow people to use it for air travel.",
             "Klein thinks that his company will be able to sell many flying cars. He still faces several challenges, though. First, his flying car can only take off and land at airports. Also, it uses gasoline, so some people say that it is not good for the environment. ( 30 ), people need a pilot's license if they want to use the flying car. However, Klein thinks he will be able to solve these problems sometime soon."
         ],
         "translations":[
             "空を飛べる車は多くのSF物語に登場してきた。100年以上にわたり、人々は本物の空飛ぶ車を作ろうとしてきた。成功した人もいるが、その空飛ぶ車が大量生産されたことはなかった。これらの車は通常、人々が買うには高すぎた。しかし、ヨーロッパのスロバキアの会社は、自社の空飛ぶ車を（28）作れると考えている。その結果、空に空飛ぶ車を見ることがすぐに一般的になるかもしれない。",
             "その会社のオーナーであるステファン・クラインは、約30年間空飛ぶ車の開発に取り組んできた。2021年6月、クラインの車は（29）。ニトラの空港からブラチスラバの空港まで約90キロメートルを移動するのに35分かかった。着陸後、空飛ぶ車の翼は3分もかからず折りたたまれ、クラインは車で市の中心部まで運転した。この車はすでに200回以上飛行しており、スロバキア政府は人々がそれを航空旅行に使用することを許可することを決定した。",
             "クラインは自社が多くの空飛ぶ車を販売できると考えている。しかし、まだいくつかの課題に直面している。まず、彼の空飛ぶ車は空港でしか離着陸できない。また、ガソリンを使用するため、環境に良くないと言う人もいる。（30）、空飛ぶ車を使いたい人はパイロットの免許が必要だ。しかし、クラインはこれらの問題をいずれ解決できると考えている。"
         ],
         "sentencePairs":[
             ["Cars that can fly have appeared in many science-fiction stories.","空を飛べる車は多くのSF物語に登場してきた。"],
             ["For over 100 years, people have been trying to build real flying cars.","100年以上にわたり、人々は本物の空飛ぶ車を作ろうとしてきた。"],
             ["These cars were usually too expensive for people to buy.","これらの車は通常、人々が買うには高すぎた。"],
             ["Stefan Klein, the owner of the company, has spent about 30 years trying to develop a flying car.","その会社のオーナーであるステファン・クラインは、約30年間空飛ぶ車の開発に取り組んできた。"],
             ["It took 35 minutes to travel about 90 kilometers from the airport in Nitra to the one in Bratislava.","ニトラの空港からブラチスラバの空港まで約90キロメートルを移動するのに35分かかった。"],
             ["The car has now been flown over 200 times.","この車はすでに200回以上飛行している。"],
             ["He still faces several challenges, though.","しかし、まだいくつかの課題に直面している。"],
             ["Also, it uses gasoline, so some people say that it is not good for the environment.","また、ガソリンを使用するため、環境に良くないと言う人もいる。"],
             ["However, Klein thinks he will be able to solve these problems sometime soon.","しかし、クラインはこれらの問題をいずれ解決できると考えている。"]
         ],
         "questions":[
             {"number":28,"choices":["at lower prices","in a shorter time","from recycled paper","by a new kind of robot"],"answer":1,
              "choiceAnalysis":{"1":"at lower prices（より安い価格で）が正解。too expensive の課題に対する解決策。","2":"shorter time は expense の問題に対応しない。","3":"recycled paper は車に不適切。","4":"robot は文脈にない。"},
              "grammar":{"point":"at lower prices","detail":"「より安い価格で」。比較級を使った価格表現。"},
              "choiceTranslations":["より安い価格で","より短い時間で","リサイクル紙から","新しい種類のロボットで"]},
             {"number":29,"choices":["went on sale","was hit by a truck","made its first trip","won a famous race"],"answer":3,
              "choiceAnalysis":{"1":"発売されたは次の文の移動の記述と合わない。","2":"トラックに衝突は文脈に合わない。","3":"made its first trip（初飛行した）が正解。35 minutes / travel 90km に対応。","4":"レースに勝ったは文脈にない。"},
              "grammar":{"point":"make a trip（旅をする）","detail":"make one's first trip で「初めての旅をする」。"},
              "choiceTranslations":["発売された","トラックにぶつけられた","初飛行をした","有名なレースで優勝した"]},
             {"number":30,"choices":["Even so","Therefore","Moreover","For example"],"answer":3,
              "choiceAnalysis":{"1":"Even so（それでも）は追加の課題を述べる文脈に合わない。","2":"Therefore（したがって）は因果関係に使うが追加ではない。","3":"Moreover（さらに）が正解。課題の追加列挙。First → Also → Moreover。","4":"For example は例示で課題追加に合わない。"},
              "grammar":{"point":"Moreover（さらに）","detail":"追加情報を加える接続副詞。First, Also, Moreover の列挙パターン。"},
              "choiceTranslations":["それでも","したがって","さらに","例えば"]}
         ]}
    ]}

# ===== 大問4: reading-comprehension =====
sec4 = {"name":"大問4","type":"reading-comprehension",
    "instruction":"次の英文A，Bの内容に関して，(31)から(37)までの質問に対して最も適切なもの，または文を完成させるのに最も適切なものを1，2，3，4の中から一つ選び，その番号を解答用紙の所定欄にマークしなさい。",
    "passages":[
        {"label":"A","title":"My cousins","format":"email",
         "meta":{"from":"Ralph Parker <ralph_parker@epostal.com>","to":"Gary Jones <gazjones_101@mymessage.com>","date":"June 4","subject":"My cousins"},
         "paragraphs":[
             "We haven't had a chance to meet since you and your family moved to your new house. Are you enjoying your new school? I know there's a great park near your new place. My mom and dad took me there once after we went to the mall on that side of the city. I really wanted to try the basketball court there, but I didn't have my ball. Have you played on it yet?",
             "By the way, do you remember my cousins from Seattle? We had fun with them when they visited last summer. They're coming to stay with us again at the end of this month. Would you like to come over while they're here? We could have a game of basketball with them. I've also got a new board game, and I think we would have a great time playing it.",
             "My cousins will be staying with us from June 21 to June 29. They will also visit their other relatives in the city, so they'll be quite busy. Can you tell me a couple of dates when you can come? My dad says that if your mom or dad can bring you here, he will take you home in the evening. Please speak to your parents and let me know."
         ],
         "translations":[
             "君と君の家族が新しい家に引っ越して以来、会う機会がなかったね。新しい学校は楽しい？君の新しい家の近くに素敵な公園があるのは知ってるよ。お母さんとお父さんがあの辺のモールに行った後、一度連れて行ってくれたんだ。そこのバスケットコートを使ってみたかったけど、ボールを持っていなかったんだ。もう使ったことある？",
             "ところで、シアトルから来たいとこたちのこと覚えてる？去年の夏に訪ねてきた時、一緒に楽しかったよね。今月末にまたうちに泊まりに来るんだ。いとこたちがいる間、遊びに来ない？一緒にバスケの試合もできるし。新しいボードゲームも手に入れたから、きっと楽しいと思うよ。",
             "いとこたちは6月21日から29日までうちに泊まるよ。街の他の親戚も訪ねるから結構忙しいみたい。来られる日を2つほど教えてくれる？お父さんが言うには、君のお母さんかお父さんがここまで送ってくれたら、夕方にお父さんが家まで送ってくれるって。ご両親に聞いて教えてね。"
         ],
         "sentencePairs":[
             ["We haven't had a chance to meet since you and your family moved to your new house.","君と君の家族が新しい家に引っ越して以来、会う機会がなかったね。"],
             ["I really wanted to try the basketball court there, but I didn't have my ball.","そこのバスケットコートを使ってみたかったけど、ボールを持っていなかったんだ。"],
             ["Have you played on it yet?","もう使ったことある？"],
             ["They're coming to stay with us again at the end of this month.","今月末にまたうちに泊まりに来るんだ。"],
             ["Would you like to come over while they're here?","いとこたちがいる間、遊びに来ない？"],
             ["My cousins will be staying with us from June 21 to June 29.","いとこたちは6月21日から29日までうちに泊まるよ。"],
             ["Can you tell me a couple of dates when you can come?","来られる日を2つほど教えてくれる？"],
             ["My dad says that if your mom or dad can bring you here, he will take you home in the evening.","お父さんが言うには、君のお母さんかお父さんがここまで送ってくれたら、夕方にお父さんが家まで送ってくれるって。"]
         ],
         "questions":[
             {"number":31,"question":"What is one thing that Ralph asks Gary?","choices":["If Gary has tried the basketball court in his local park.","If Gary bought a new basketball when he went to the mall.","Whether Gary's new school is near his new house.","Whether Gary's parents are planning to move to a new house."],"answer":1,"questionTranslation":"ラルフがゲイリーに尋ねていることの一つは何ですか？",
              "choiceAnalysis":{"1":"正解。Have you played on it yet? に対応。","2":"バスケットボールの購入は本文にない。","3":"学校と家の距離は聞いていない。","4":"引っ越しの計画は聞いていない。"},
              "grammar":{"point":"現在完了の疑問文","detail":"Have you played...yet? 経験を尋ねる現在完了形。"},
              "choiceTranslations":["ゲイリーが地元の公園のバスケットコートを使ったかどうか。","ゲイリーがモールで新しいバスケットボールを買ったかどうか。","ゲイリーの新しい学校が新しい家の近くかどうか。","ゲイリーの両親が新しい家に引っ越す予定かどうか。"]},
             {"number":32,"question":"Ralph says that his cousins from Seattle","choices":["will play in a basketball tournament in June.","have told him about a great new board game.","want to know if Gary can remember them.","came to stay with his family last year."],"answer":4,"questionTranslation":"ラルフはシアトルのいとこたちについて何と言っていますか？",
              "choiceAnalysis":{"1":"バスケのトーナメントは本文にない。","2":"ボードゲームはラルフが買ったもの。","3":"いとこがゲイリーを覚えているか聞いているのはラルフ。","4":"正解。visited last summer に対応。"},
              "grammar":{"point":"過去形による事実の記述","detail":"came to stay = 泊まりに来た。last year の過去の事実。"},
              "choiceTranslations":["6月にバスケのトーナメントに参加する。","素晴らしい新しいボードゲームについて教えてくれた。","ゲイリーが彼らを覚えているか知りたがっている。","去年彼の家族のところに泊まりに来た。"]},
             {"number":33,"question":"What does Ralph's father say that he will do?","choices":["Speak to Gary's parents.","Tell Ralph the best dates to come.","Take Gary back to his house.","Visit Ralph's relatives in the city."],"answer":3,"questionTranslation":"ラルフのお父さんは何をすると言っていますか？",
              "choiceAnalysis":{"1":"ゲイリーの両親と話すとは言っていない。","2":"日程を教えるのはゲイリーに頼んでいること。","3":"正解。he will take you home in the evening に対応。","4":"親戚を訪ねるのはいとこたち。"},
              "grammar":{"point":"条件文 if...will","detail":"if your parents can bring you, he will take you home. 条件と結果。"},
              "choiceTranslations":["ゲイリーの両親と話す。","ラルフに来るのに最適な日を教える。","ゲイリーを家まで送る。","街のラルフの親戚を訪ねる。"]}
         ]},
        {"label":"B","title":"Video Game Arcades",
         "paragraphs":[
             "The first computer games were quite different from the ones that people play today. When computer games appeared in the 1950s, computers were big and expensive. They were only found in universities and large companies. Although computers were invented to solve serious problems, creating games is a good way to learn computer programming. In addition, the process of inventing new games has led to many important discoveries for computer technology.",
             "In the early 1970s, computers were still too expensive for most people to own. However, a number of fun games had been developed by students at universities in the United States. Some of these students wanted to make money from their games. They built computers inside large wooden boxes. Then, they put the boxes in places like bars and cafés. Customers could play the games by putting money into a special hole in the boxes.",
             "These computer games were a big success. More and more of them were created. One of the most popular games was Space Invaders. In this game, players tried to shoot space monsters that were attacking them. In the 1970s, \"video game arcades\" began to appear. These were places with many computer game machines. During the 1970s and 1980s, video game arcades became important places for young people to meet friends and make new ones.",
             "At the same time, companies were developing cheap home computers. People with these machines did not have to go to video game arcades. They did not have to pay each time they wanted to play a game. They did not have to wait for other people to finish playing, either. Video game arcade owners tried to introduce games that used technology that home computers did not have. However, home computer makers were able to find ways to make their games more attractive. Now, many video game arcades have closed."
         ],
         "translations":[
             "最初のコンピュータゲームは、今日人々がプレイするものとはかなり異なっていた。コンピュータゲームが1950年代に登場した時、コンピュータは大きくて高価だった。大学や大企業にしかなかった。コンピュータは深刻な問題を解決するために発明されたが、ゲームを作ることはコンピュータプログラミングを学ぶ良い方法だ。さらに、新しいゲームを発明する過程がコンピュータ技術の多くの重要な発見につながった。",
             "1970年代初頭、コンピュータはまだほとんどの人が所有するには高すぎた。しかし、アメリカの大学の学生たちによって多くの楽しいゲームが開発されていた。これらの学生の中には、ゲームでお金を稼ぎたいと思う者もいた。彼らは大きな木製の箱の中にコンピュータを作り込んだ。そして、バーやカフェなどの場所にその箱を置いた。客は箱の特別な穴にお金を入れることでゲームをプレイできた。",
             "これらのコンピュータゲームは大成功だった。どんどん多くのゲームが作られた。最も人気のあるゲームの一つはスペースインベーダーだった。このゲームでは、プレイヤーは攻撃してくる宇宙モンスターを撃とうとした。1970年代に「ビデオゲームアーケード」が現れ始めた。これらはたくさんのコンピュータゲーム機がある場所だった。1970年代と1980年代に、ビデオゲームアーケードは若者が友達に会い、新しい友達を作る重要な場所になった。",
             "同時に、企業は安価な家庭用コンピュータを開発していた。これらの機械を持つ人々はビデオゲームアーケードに行く必要がなくなった。ゲームをプレイしたい度にお金を払う必要もなくなった。他の人がプレイし終わるのを待つ必要もなくなった。ビデオゲームアーケードのオーナーは、家庭用コンピュータにはない技術を使ったゲームを導入しようとした。しかし、家庭用コンピュータメーカーはゲームをより魅力的にする方法を見つけることができた。現在、多くのビデオゲームアーケードが閉店している。"
         ],
         "sentencePairs":[
             ["The first computer games were quite different from the ones that people play today.","最初のコンピュータゲームは、今日人々がプレイするものとはかなり異なっていた。"],
             ["When computer games appeared in the 1950s, computers were big and expensive.","コンピュータゲームが1950年代に登場した時、コンピュータは大きくて高価だった。"],
             ["Although computers were invented to solve serious problems, creating games is a good way to learn computer programming.","コンピュータは深刻な問題を解決するために発明されたが、ゲームを作ることはコンピュータプログラミングを学ぶ良い方法だ。"],
             ["In the early 1970s, computers were still too expensive for most people to own.","1970年代初頭、コンピュータはまだほとんどの人が所有するには高すぎた。"],
             ["Some of these students wanted to make money from their games.","これらの学生の中には、ゲームでお金を稼ぎたいと思う者もいた。"],
             ["Customers could play the games by putting money into a special hole in the boxes.","客は箱の特別な穴にお金を入れることでゲームをプレイできた。"],
             ["These computer games were a big success.","これらのコンピュータゲームは大成功だった。"],
             ["One of the most popular games was Space Invaders.","最も人気のあるゲームの一つはスペースインベーダーだった。"],
             ["Video game arcade owners tried to introduce games that used technology that home computers did not have.","ビデオゲームアーケードのオーナーは、家庭用コンピュータにはない技術を使ったゲームを導入しようとした。"],
             ["However, home computer makers were able to find ways to make their games more attractive.","しかし、家庭用コンピュータメーカーはゲームをより魅力的にする方法を見つけることができた。"],
             ["Now, many video game arcades have closed.","現在、多くのビデオゲームアーケードが閉店している。"]
         ],
         "questions":[
             {"number":34,"question":"Computer games can be used to","choices":["train new staff members when they join large companies.","help people understand how to make computer software.","solve serious problems all over the world.","find ways for universities to save money."],"answer":2,"questionTranslation":"コンピュータゲームは何に使えますか？",
              "choiceAnalysis":{"1":"新入社員の研修は本文にない。","2":"正解。creating games is a good way to learn computer programming のパラフレーズ。","3":"深刻な問題を解決するのはコンピュータの目的であり、ゲームの目的ではない。","4":"大学の節約は本文にない。"},
              "grammar":{"point":"パラフレーズの読み取り","detail":"learn computer programming → understand how to make computer software。"},
              "choiceTranslations":["大企業に入社した新入社員を研修する。","コンピュータソフトウェアの作り方を理解する助けになる。","世界中の深刻な問題を解決する。","大学がお金を節約する方法を見つける。"]},
             {"number":35,"question":"Why did some students put computers in places like bars and cafés?","choices":["To discover how much money people would pay for a computer.","To do research on why computer games had become so popular.","So that they could find out what food and drinks customers bought.","So that they could get some money from the games they had made."],"answer":4,"questionTranslation":"なぜ学生たちはバーやカフェにコンピュータを置いたのですか？",
              "choiceAnalysis":{"1":"コンピュータの価格調査ではない。","2":"人気の研究ではない。","3":"飲食物の調査ではない。","4":"正解。wanted to make money from their games のパラフレーズ。"},
              "grammar":{"point":"so that S could ～","detail":"「Sが～できるように」目的を表す構文。"},
              "choiceTranslations":["人々がコンピュータにいくら払うか調べるため。","なぜコンピュータゲームがそれほど人気になったか研究するため。","客がどんな飲食物を買うか調べるため。","自分たちが作ったゲームからお金を得るため。"]},
             {"number":36,"question":"One reason many young people went to \"video game arcades\" was","choices":["that they could get to know new people.","that they thought space monsters might attack.","to show people the games they had created.","to get jobs making computer game machines."],"answer":1,"questionTranslation":"多くの若者がビデオゲームアーケードに行った理由の一つは？",
              "choiceAnalysis":{"1":"正解。meet friends and make new ones のパラフレーズ。","2":"宇宙モンスターの攻撃は冗談のような選択肢。","3":"ゲームを見せるためではない。","4":"仕事を得るためではない。"},
              "grammar":{"point":"get to know（知り合いになる）","detail":"make new friends → get to know new people のパラフレーズ。"},
              "choiceTranslations":["新しい人と知り合いになれたから。","宇宙モンスターが攻撃してくると思ったから。","自分たちが作ったゲームを人に見せるため。","コンピュータゲーム機を作る仕事を得るため。"]},
             {"number":37,"question":"How did owners try to get more people to come to their video game arcades?","choices":["By introducing games that people could play without paying.","By giving discounts on home computers to their best customers.","By adding things for people to do while waiting to play games.","By bringing in computer technology that people did not have at home."],"answer":4,"questionTranslation":"オーナーたちはどのようにしてより多くの人をビデオゲームアーケードに来させようとしましたか？",
              "choiceAnalysis":{"1":"無料ゲームの導入は本文にない。","2":"家庭用コンピュータの割引は本文にない。","3":"待ち時間のアクティビティは本文にない。","4":"正解。introduce games that used technology that home computers did not have のパラフレーズ。"},
              "grammar":{"point":"by ～ing（～することによって）","detail":"手段を表す前置詞 by + 動名詞。"},
              "choiceTranslations":["お金を払わずにプレイできるゲームを導入して。","最高の顧客に家庭用コンピュータの割引を提供して。","ゲームを待つ間にできることを追加して。","家庭にはないコンピュータ技術を導入して。"]}
         ]}
    ]}

d["sections"].append(sec3)
d["sections"].append(sec4)

with open(r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade-pre2\2023-1\_part2.json","w",encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=4)

total = sum(len(s.get("questions",[])) + sum(len(p.get("questions",[])) for p in s.get("passages",[])) for s in d["sections"])
print(f"✅ Part2 saved: total {total} questions")

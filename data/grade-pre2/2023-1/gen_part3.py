"""準2級 2023-1 Part 3: vocabulary + lessonPlan + assemble final data.json"""
import json, os

d = json.load(open(r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade-pre2\2023-1\_part2.json","r",encoding="utf-8"))

# ===== Vocabulary (40+語) =====
d["vocabulary"] = [
    {"word":"erased","meaning":"消した","pos":"動詞","level":"準2級","example":"He erased the mistake from his paper.","distractors":["書いた","延ばした","許した"]},
    {"word":"control","meaning":"支配・制御","pos":"名詞","level":"準2級","example":"We have no control over the weather.","distractors":["問題","成績","熱"]},
    {"word":"blankets","meaning":"毛布","pos":"名詞","level":"準2級","example":"She put extra blankets on her bed.","distractors":["枕","カーテン","シーツ"]},
    {"word":"educational","meaning":"教育的な","pos":"形容詞","level":"準2級","example":"This is a very educational program.","distractors":["現代的な","暴力的な","孤独な"]},
    {"word":"reality","meaning":"現実","pos":"名詞","level":"準2級","example":"He had to face the reality of his situation.","distractors":["起源","提案","海岸"]},
    {"word":"refused","meaning":"断った","pos":"動詞","level":"準2級","example":"She refused to sell her guitar.","distractors":["雇った","引退した","存在した"]},
    {"word":"discussions","meaning":"議論・話し合い","pos":"名詞","level":"準2級","example":"We had interesting discussions about history.","distractors":["消費者","筋肉","アプローチ"]},
    {"word":"respects","meaning":"尊敬する","pos":"動詞","level":"準2級","example":"He respects his teacher very much.","distractors":["助ける","場所を見つける","結合する"]},
    {"word":"greeted","meaning":"迎えた","pos":"動詞","level":"準2級","example":"She greeted him with a warm smile.","distractors":["約束した","要求した","面接した"]},
    {"word":"terribly","meaning":"ひどく・非常に","pos":"副詞","level":"準2級","example":"I'm terribly sorry for the mistake.","distractors":["等しく","穏やかに","安全に"]},
    {"word":"take turns","meaning":"交代でする","pos":"熟語","level":"準2級","example":"They take turns washing the dishes.","distractors":["拍手する","回す","信頼する"]},
    {"word":"on business","meaning":"出張で","pos":"熟語","level":"準2級","example":"He went to New York on business.","distractors":["少なくとも","暗記して","永久に"]},
    {"word":"felt like","meaning":"〜したい気分だった","pos":"熟語","level":"準2級","example":"I felt like eating pizza for dinner.","distractors":["〜のように見えた","通り過ぎた","走り過ぎた"]},
    {"word":"take place","meaning":"行われる","pos":"熟語","level":"準2級","example":"The meeting takes place every Monday.","distractors":["成長する","実現する","延期する"]},
    {"word":"rely on","meaning":"〜に頼る","pos":"熟語","level":"準2級","example":"You can rely on me for help.","distractors":["並べる","提出する","乗り越える"]},
    {"word":"dress up","meaning":"仮装する","pos":"熟語","level":"準2級","example":"She dressed up as a princess for Halloween.","distractors":["消す","抑える","勃発する"]},
    {"word":"backed up","meaning":"裏付けた","pos":"熟語","level":"準2級","example":"He backed up his argument with data.","distractors":["引き離した","叫んだ","望んだ"]},
    {"word":"had given","meaning":"あげていた（過去完了）","pos":"動詞","level":"準2級","example":"She had already given him the book.","distractors":["あげている","あげられた","あげていた"]},
    {"word":"nobody","meaning":"誰も〜ない","pos":"代名詞","level":"準2級","example":"Nobody came to the party.","distractors":["みんな","誰か","誰でも"]},
    {"word":"nervous","meaning":"緊張した","pos":"形容詞","level":"準2級","example":"Sally was very nervous before the concert.","distractors":["退屈な","勇敢な","眠い"]},
    {"word":"audience","meaning":"観客・聴衆","pos":"名詞","level":"準2級","example":"The audience cheered loudly.","distractors":["舞台","楽器","指揮者"]},
    {"word":"clapping","meaning":"拍手する","pos":"動詞","level":"準2級","example":"Everyone was clapping after the performance.","distractors":["叫ぶ","泣く","笑う"]},
    {"word":"science-fiction","meaning":"SF・空想科学","pos":"名詞","level":"準2級","example":"He enjoys reading science-fiction novels.","distractors":["歴史小説","恋愛小説","伝記"]},
    {"word":"succeed","meaning":"成功する","pos":"動詞","level":"準2級","example":"She worked hard and finally succeeded.","distractors":["失敗する","諦める","迷う"]},
    {"word":"environment","meaning":"環境","pos":"名詞","level":"準2級","example":"We should protect the environment.","distractors":["経済","政治","教育"]},
    {"word":"pilot's license","meaning":"パイロット免許","pos":"名詞","level":"準2級","example":"You need a pilot's license to fly a plane.","distractors":["運転免許","釣り免許","営業許可"]},
    {"word":"challenge","meaning":"課題・挑戦","pos":"名詞","level":"準2級","example":"Learning a new language is a big challenge.","distractors":["結果","理由","利点"]},
    {"word":"arcade","meaning":"アーケード・ゲームセンター","pos":"名詞","level":"準2級","example":"We played games at the video game arcade.","distractors":["映画館","図書館","博物館"]},
    {"word":"programming","meaning":"プログラミング","pos":"名詞","level":"準2級","example":"She is learning computer programming.","distractors":["会計","料理","裁縫"]},
    {"word":"customers","meaning":"客・顧客","pos":"名詞","level":"準2級","example":"The store has many regular customers.","distractors":["従業員","経営者","株主"]},
    {"word":"attractive","meaning":"魅力的な","pos":"形容詞","level":"準2級","example":"The new design is very attractive.","distractors":["退屈な","普通の","古い"]},
    {"word":"relatives","meaning":"親戚","pos":"名詞","level":"準2級","example":"We visited our relatives during the holidays.","distractors":["友人","同僚","隣人"]},
    {"word":"tournament","meaning":"トーナメント・大会","pos":"名詞","level":"準2級","example":"He played in a basketball tournament.","distractors":["練習","レッスン","試験"]},
    {"word":"gasoline","meaning":"ガソリン","pos":"名詞","level":"準2級","example":"The car runs on gasoline.","distractors":["電気","水素","天然ガス"]},
    {"word":"technology","meaning":"技術","pos":"名詞","level":"準2級","example":"Technology is changing the world.","distractors":["自然","芸術","宗教"]},
    {"word":"wooden","meaning":"木製の","pos":"形容詞","level":"準2級","example":"They built a wooden box.","distractors":["金属の","プラスチックの","ガラスの"]},
    {"word":"discover","meaning":"発見する","pos":"動詞","level":"準2級","example":"Scientists discovered a new species.","distractors":["隠す","壊す","忘れる"]},
    {"word":"introduce","meaning":"導入する・紹介する","pos":"動詞","level":"準2級","example":"The company introduced a new product.","distractors":["撤退する","中止する","拒否する"]},
    {"word":"solve","meaning":"解決する","pos":"動詞","level":"準2級","example":"We need to solve this problem quickly.","distractors":["作る","増やす","無視する"]},
    {"word":"develop","meaning":"開発する","pos":"動詞","level":"準2級","example":"They are developing a new app.","distractors":["破壊する","中止する","延期する"]},
    {"word":"popular","meaning":"人気のある","pos":"形容詞","level":"準2級","example":"This game is very popular with children.","distractors":["珍しい","嫌いな","退屈な"]}
]

# ===== lessonPlan: 文法・構文ベース FP =====
d["lessonPlan"] = {"focusPoints": [
    {"id":"fp1","title":"過去完了形（大過去）","subtitle":"Past Perfect Tense",
     "explanation":"過去完了形（had + 過去分詞）は、過去のある時点より前に完了していた動作を表します。「〜していた」という大過去の表現で、時間の前後関係を明確にします。",
     "sourceQuote":"Mike cried when he broke the toy truck that his mother had given him for his birthday.","sourceLocation":"大問1 Q18",
     "examples":[
         {"en":"She had already left when I arrived.","ja":"私が着いた時、彼女はすでに出発していた。","note":"arrived（過去）より前にleft（過去完了）"},
         {"en":"He realized that he had forgotten his wallet.","ja":"彼は財布を忘れたことに気づいた。","note":"realized（過去）より前にforgotten（過去完了）"},
         {"en":"A number of fun games had been developed by students.","ja":"多くの楽しいゲームが学生たちによって開発されていた。","note":"過去完了の受動態 had been + 過去分詞"}
     ],
     "practicePassage":{"en":"[出典: Video Game Arcades 第2段落]\nIn the early 1970s, computers were still too expensive for most people to own. However, a number of fun games had been developed by students at universities in the United States. Some of these students wanted to make money from their games. They built computers inside large wooden boxes. Then, they put the boxes in places like bars and cafés. Customers could play the games by putting money into a special hole in the boxes.",
      "ja":"[出典: Video Game Arcades 第2段落]\n1970年代初頭、コンピュータはまだほとんどの人が所有するには高すぎた。しかし、アメリカの大学の学生たちによって多くの楽しいゲームが開発されていた。これらの学生の中には、ゲームでお金を稼ぎたいと思う者もいた。彼らは大きな木製の箱の中にコンピュータを作り込んだ。そして、バーやカフェなどの場所にその箱を置いた。客は箱の特別な穴にお金を入れることでゲームをプレイできた。"},
     "practiceQuestions":[
         {"q":"「had been developed」はなぜ過去完了形ですか？","a":"1970年代初頭（過去）の時点で、それ以前にすでに開発されていたことを表すため。"},
         {"q":"「had given」（Q18）で過去完了が使われる理由は？","a":"「壊した」（過去）よりも前に「もらった」ことを表す大過去。"},
         {"q":"過去完了の受動態の形は？","a":"had been + 過去分詞（例：had been developed）"}
     ],
     "highlightPatterns":["a number of fun games had been developed by students","the toy truck that his mother had given him","We had fun with them when they visited last summer"],
     "highlightColor":"#4f8cff","highlightLabel":"過去完了形"},
    {"id":"fp2","title":"too...to 構文と enough to 構文","subtitle":"Too...to / Enough to Constructions",
     "explanation":"too + 形容詞 + to 不定詞 は「〜すぎて…できない」、形容詞 + enough + to 不定詞 は「…するのに十分〜だ」を表します。長文の論理展開で物事の程度を述べる際に頻出します。",
     "sourceQuote":"These cars were usually too expensive for people to buy.","sourceLocation":"大問3B 第1段落",
     "examples":[
         {"en":"The box was too heavy for me to carry.","ja":"その箱は重すぎて私には運べなかった。","note":"too + 形容詞 + for 人 + to 不定詞"},
         {"en":"She is old enough to drive a car.","ja":"彼女は車を運転できる年齢だ。","note":"形容詞 + enough + to 不定詞"},
         {"en":"Computers were still too expensive for most people to own.","ja":"コンピュータはまだほとんどの人が所有するには高すぎた。","note":"本試験の実例"}
     ],
     "practicePassage":{"en":"[出典: Up and Away 第1段落]\nCars that can fly have appeared in many science-fiction stories. For over 100 years, people have been trying to build real flying cars. Some have succeeded, but their flying cars have never been produced in large numbers. These cars were usually too expensive for people to buy. However, a company in the European country of Slovakia thinks that its flying cars can be made at lower prices. As a result, it might soon be common to see flying cars in the sky.",
      "ja":"[出典: Up and Away 第1段落]\n空を飛べる車は多くのSF物語に登場してきた。100年以上にわたり、人々は本物の空飛ぶ車を作ろうとしてきた。成功した人もいるが、その空飛ぶ車が大量生産されたことはなかった。これらの車は通常、人々が買うには高すぎた。しかし、ヨーロッパのスロバキアの会社は、自社の空飛ぶ車をより安い価格で作れると考えている。その結果、空に空飛ぶ車を見ることがすぐに一般的になるかもしれない。"},
     "practiceQuestions":[
         {"q":"「too expensive for people to buy」を別の表現に書き換えてください。","a":"so expensive that people could not buy them"},
         {"q":"「too expensive for most people to own」の意味は？","a":"ほとんどの人が所有するには高すぎた（＝所有できなかった）"},
         {"q":"enough to を使って「彼は十分速く走れた」を英語にしてください。","a":"He was fast enough to win the race."}
     ],
     "highlightPatterns":["too expensive for people to buy","too expensive for most people to own","a good way to learn computer programming"],
     "highlightColor":"#34d399","highlightLabel":"too...to構文"},
    {"id":"fp3","title":"接続副詞による論理展開","subtitle":"Conjunctive Adverbs for Logical Flow",
     "explanation":"However（しかし）、As a result（その結果）、In addition（さらに）、Moreover（さらに）などの接続副詞は、文と文の論理関係を示します。長文読解では、これらの表現を手がかりに筆者の論理展開を追います。",
     "sourceQuote":"However, a company in the European country of Slovakia thinks that its flying cars can be made at lower prices.","sourceLocation":"大問3B 第1段落",
     "examples":[
         {"en":"It was raining. However, they decided to go hiking.","ja":"雨が降っていた。しかし、彼らはハイキングに行くことにした。","note":"However は逆接を示す接続副詞"},
         {"en":"She studied hard. As a result, she passed the exam.","ja":"彼女は一生懸命勉強した。その結果、試験に合格した。","note":"As a result は因果関係の結果を示す"},
         {"en":"The food was great. Moreover, the service was excellent.","ja":"料理は素晴らしかった。さらに、サービスも優れていた。","note":"Moreover は追加情報を示す"}
     ],
     "practicePassage":{"en":"[出典: Up and Away 第3段落]\nKlein thinks that his company will be able to sell many flying cars. He still faces several challenges, though. First, his flying car can only take off and land at airports. Also, it uses gasoline, so some people say that it is not good for the environment. Moreover, people need a pilot's license if they want to use the flying car. However, Klein thinks he will be able to solve these problems sometime soon.",
      "ja":"[出典: Up and Away 第3段落]\nクラインは自社が多くの空飛ぶ車を販売できると考えている。しかし、まだいくつかの課題に直面している。まず、彼の空飛ぶ車は空港でしか離着陸できない。また、ガソリンを使用するため、環境に良くないと言う人もいる。さらに、空飛ぶ車を使いたい人はパイロットの免許が必要だ。しかし、クラインはこれらの問題をいずれ解決できると考えている。"},
     "practiceQuestions":[
         {"q":"この段落で使われている接続副詞を全て挙げてください。","a":"though, First, Also, Moreover, However の5つ"},
         {"q":"Moreover と Also の違いは？","a":"どちらも追加を示すが、Moreover はよりフォーマルで強調的。"},
         {"q":"However の前後の論理関係は？","a":"逆接。課題がある（前）→ しかし解決できると考えている（後）"}
     ],
     "highlightPatterns":["However, a company in the European country of Slovakia","As a result, it might soon be common","Moreover, people need a pilot's license","However, Klein thinks he will be able to solve","In addition, the process of inventing new games has led to"],
     "highlightColor":"#f472b6","highlightLabel":"接続副詞"},
    {"id":"fp4","title":"受動態の多様な形","subtitle":"Various Forms of Passive Voice",
     "explanation":"受動態（be + 過去分詞）は基本形だけでなく、助動詞付き（can be made）、完了形（have been flown）、進行形（were being developed）など多様な形があります。",
     "sourceQuote":"its flying cars can be made at lower prices","sourceLocation":"大問3B 第1段落",
     "examples":[
         {"en":"The car can be driven by anyone.","ja":"その車は誰でも運転できる。","note":"助動詞 + be + 過去分詞"},
         {"en":"The car has now been flown over 200 times.","ja":"その車はすでに200回以上飛行している。","note":"現在完了の受動態 has been + 過去分詞"},
         {"en":"Many games were created.","ja":"多くのゲームが作られた。","note":"基本的な過去の受動態"}
     ],
     "practicePassage":{"en":"[出典: Video Game Arcades 第3-4段落]\nThese computer games were a big success. More and more of them were created. One of the most popular games was Space Invaders. In this game, players tried to shoot space monsters that were attacking them. In the 1970s, \"video game arcades\" began to appear. These were places with many computer game machines. During the 1970s and 1980s, video game arcades became important places for young people to meet friends and make new ones.",
      "ja":"[出典: Video Game Arcades 第3-4段落]\nこれらのコンピュータゲームは大成功だった。どんどん多くのゲームが作られた。最も人気のあるゲームの一つはスペースインベーダーだった。このゲームでは、プレイヤーは攻撃してくる宇宙モンスターを撃とうとした。1970年代に「ビデオゲームアーケード」が現れ始めた。これらはたくさんのコンピュータゲーム機がある場所だった。1970年代と1980年代に、ビデオゲームアーケードは若者が友達に会い、新しい友達を作る重要な場所になった。"},
     "practiceQuestions":[
         {"q":"「can be made」の態と構造は？","a":"助動詞付き受動態。can + be + 過去分詞。"},
         {"q":"「has been flown」の態と時制は？","a":"現在完了の受動態。has + been + 過去分詞。"},
         {"q":"「were created」を能動態にしてください。","a":"People created more and more of them."}
     ],
     "highlightPatterns":["its flying cars can be made at lower prices","their flying cars have never been produced in large numbers","The car has now been flown over 200 times","More and more of them were created","the government of Slovakia has decided to allow people to use it"],
     "highlightColor":"#fbbf24","highlightLabel":"受動態"},
    {"id":"fp5","title":"今回の重要なパラフレーズ","subtitle":"Key Paraphrases in This Exam",
     "explanation":"英検の読解問題では、本文の内容が選択肢で別の言い方（パラフレーズ）に書き換えられます。同じ意味を異なる語句で表現する力が正解を見つけるカギです。",
     "sourceQuote":"①「creating games is a good way to learn computer programming」→「help people understand how to make computer software」\n②「make money from their games」→「get some money from the games they had made」\n③「meet friends and make new ones」→「get to know new people」\n④「introduce games that used technology that home computers did not have」→「bringing in computer technology that people did not have at home」",
     "sourceLocation":"大問4B",
     "examples":[
         {"en":"meet friends and make new ones → get to know new people","ja":"友達に会い新しい友達を作る → 新しい人と知り合いになる","note":"make new friends → get to know new people"},
         {"en":"too expensive to buy → people could not afford them","ja":"買うには高すぎた → 人々にはそれを買う余裕がなかった","note":"too...to → could not afford"},
         {"en":"make money from → get some money from","ja":"〜からお金を稼ぐ → 〜からいくらかのお金を得る","note":"make money → get money の言い換え"}
     ],
     "practicePassage":{"en":"[出典: Video Game Arcades 第4段落]\nAt the same time, companies were developing cheap home computers. People with these machines did not have to go to video game arcades. They did not have to pay each time they wanted to play a game. They did not have to wait for other people to finish playing, either. Video game arcade owners tried to introduce games that used technology that home computers did not have. However, home computer makers were able to find ways to make their games more attractive. Now, many video game arcades have closed.",
      "ja":"[出典: Video Game Arcades 第4段落]\n同時に、企業は安価な家庭用コンピュータを開発していた。これらの機械を持つ人々はビデオゲームアーケードに行く必要がなくなった。ゲームをプレイしたい度にお金を払う必要もなくなった。他の人がプレイし終わるのを待つ必要もなくなった。ビデオゲームアーケードのオーナーは、家庭用コンピュータにはない技術を使ったゲームを導入しようとした。しかし、家庭用コンピュータメーカーはゲームをより魅力的にする方法を見つけることができた。現在、多くのビデオゲームアーケードが閉店している。"},
     "practiceQuestions":[
         {"q":"「introduce games that used technology that home computers did not have」のパラフレーズは？","a":"bring in computer technology that people did not have at home"},
         {"q":"「meet friends and make new ones」を別の言い方で？","a":"get to know new people / socialize with others"},
         {"q":"「did not have to pay each time」の意味を別の言い方で？","a":"could play without paying every time / playing was free"},
         {"q":"「make their games more attractive」の意味は？","a":"ゲームをより魅力的にする＝ゲームの質を向上させる"}
     ],
     "highlightPatterns":["introduce games that used technology that home computers did not have","meet friends and make new ones","make money from their games","creating games is a good way to learn computer programming"],
     "highlightColor":"#f59e0b","highlightLabel":"パラフレーズ"}
]}

# Save final data.json
outpath = r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade-pre2\2023-1\data.json"
with open(outpath, "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=4)

total = sum(len(s.get("questions",[])) + sum(len(p.get("questions",[])) for p in s.get("passages",[])) for s in d["sections"])
print(f"✅ data.json saved: {total} questions, {len(d['vocabulary'])} vocab, {len(d['lessonPlan']['focusPoints'])} FPs")

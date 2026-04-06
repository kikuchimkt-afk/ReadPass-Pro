"""Generate sections 3-4 + vocabulary + lessonPlan for 2021-1"""
import json, os
base = r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade-pre2\2021-1"
data = json.load(open(os.path.join(base, "_part1.json"), "r", encoding="utf-8"))

s3 = {"name":"大問3","nameEn":"Part 3","type":"passage-fill",
    "instruction":"次の英文A，Bを読み，その文意にそって(26)から(30)までの(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選びなさい。",
    "passages":[
        {"label":"A","title":"Pumpkin Soup",
         "paragraphs":[
             "Lisa loves soup. She always has a cup of soup for breakfast. Sometimes, she has two cups. There are many kinds of soup at the supermarket that Lisa goes to. Some of them ( 26 ). However, Lisa likes to try them all. She does not mind spending a lot of money on soup every month.",
             "One day, Lisa's best friend, Rachel, said that she would teach Lisa how to make soup from pumpkins. At first, Lisa was worried that it might be too difficult for her. However, Rachel showed Lisa all the things she needed to do. It was not hard at all. In fact, making pumpkin soup ( 27 ). The soup also tasted much better than the pumpkin soup from the supermarket. Lisa decided that she would like to try making other types of soup in the future, too."
         ],
         "translations":[
             "リサはスープが大好きだ。朝食にはいつもスープを1杯飲む。2杯飲むこともある。リサが行くスーパーには多くの種類のスープがある。中には( 26 )ものもある。しかしリサは全部試すのが好きだ。毎月スープに多くのお金を使うことを気にしない。",
             "ある日、リサの親友レイチェルがカボチャからスープの作り方を教えてくれると言った。最初リサは難しすぎるかもと心配した。しかしレイチェルが必要なことをすべて教えてくれた。全く難しくなかった。実際、カボチャスープを作るのは( 27 )。スーパーのカボチャスープよりずっと美味しかった。リサは将来、他のスープも作ってみたいと思った。"
         ],
         "sentencePairs":[
             ["She always has a cup of soup for breakfast.","朝食にはいつもスープを1杯飲む。"],
             ["She does not mind spending a lot of money on soup every month.","毎月スープに多くのお金を使うことを気にしない。"],
             ["At first, Lisa was worried that it might be too difficult for her.","最初リサは難しすぎるかもと心配した。"],
             ["It was not hard at all.","全く難しくなかった。"],
             ["The soup also tasted much better than the pumpkin soup from the supermarket.","スーパーのカボチャスープよりずっと美味しかった。"],
             ["Lisa decided that she would like to try making other types of soup in the future.","リサは将来他のスープも作ってみたいと思った。"]
         ],
         "questions":[
             {"number":26,"choices":["have vegetables in them","taste very delicious","come from other countries","are quite expensive"],"choiceTranslations":["野菜が入っている","とても美味しい","他の国から来ている","かなり高い"],"answer":4,"choiceAnalysis":["野菜入り→「お金を使うことを気にしない」に繋がらない","美味しい→Howeverとの対比にならない","外国から→お金の文脈に繋がらない","かなり高い→正解。💡 高いが全部試す→お金を使うことを気にしない"],"grammar":"💡 quite＝かなり。do not mind ～ing＝～するのを気にしない"},
             {"number":27,"choices":["gave her new problems","made her mother happy","was a lot of fun","took a long time"],"choiceTranslations":["新しい問題を引き起こした","母を喜ばせた","とても楽しかった","長い時間がかかった"],"answer":3,"choiceAnalysis":["新しい問題→難しくなかったので矛盾","母を喜ばせた→母の話は出ていない","とても楽しかった→正解。💡 難しくなかった＋スーパーより美味しい→楽しかった→他のスープも作りたい","長い時間→「難しくなかった」に続く文脈として不適切"],"grammar":"💡 a lot of fun＝とても楽しい。In fact＝実際"}
         ]
        },
        {"label":"B","title":"Sharing the Love of Dogs",
         "paragraphs":[
             "Some websites on the Internet let people borrow things from each other. For example, people can borrow other people's tools. Tools such as drills can be expensive, and most people do not ( 28 ). After a tool is used once, it is often kept in a cabinet or garage for months. Borrowing tools can save both money and space. Now, there is even a website for borrowing pets. It is called BorrowMyDoggy. Dog owners can put photos and other information about their pets on the website. Dog lovers can search the website for dogs to borrow.",
             "Dog owners might use BorrowMyDoggy if they become busy with work or they have to look after someone in their family. They need ( 29 ) their dogs. People who want to borrow dogs use the website to contact dog owners. Dog owners can ask these people questions. In this way, owners can find out if people will be nice to their dogs. If an owner is happy, the person can then meet the dog and take it for a walk or play with it.",
             "Many dog lovers cannot have a dog as a pet. Maybe they do not have enough time or money. Maybe their house is too small. Maybe someone in their family does not like dogs. BorrowMyDoggy is ( 30 ). They get a chance to spend time with their favorite animals. Moreover, playing with dogs reduces these people's stress and helps them to be healthy and happy."
         ],
         "translations":[
             "インターネットの一部のウェブサイトでは物を貸し借りできる。たとえばドリルなどの工具を借りられる。工具は高価で、ほとんどの人は( 28 )。一度使った工具はキャビネットやガレージに何ヶ月も保管されることが多い。工具を借りればお金とスペースの両方を節約できる。今ではペットを借りるウェブサイトまである。BorrowMyDoggyだ。飼い主はペットの写真や情報をサイトに掲載でき、犬好きは借りたい犬を検索できる。",
             "飼い主は仕事が忙しくなったり家族の世話が必要になった時にBorrowMyDoggyを使うかもしれない。犬を( 29 )が必要だ。犬を借りたい人はサイトを通じて飼い主に連絡する。飼い主は質問をして犬に優しくしてくれるか確認できる。飼い主が満足すれば、その人は犬と会い散歩に連れて行ったり遊んだりできる。",
             "多くの犬好きはペットとして犬を飼えない。時間やお金が足りないかもしれない。家が小さすぎるかもしれない。家族が犬嫌いかもしれない。BorrowMyDoggyはそのような人に( 30 )。大好きな動物と過ごす機会が得られる。さらに犬と遊ぶことでストレスが減り、健康で幸せでいられる。"
         ],
         "sentencePairs":[
             ["Some websites on the Internet let people borrow things from each other.","インターネットの一部のサイトでは物の貸し借りができる。"],
             ["Tools such as drills can be expensive.","ドリルなどの工具は高価になり得る。"],
             ["Borrowing tools can save both money and space.","工具を借りればお金とスペースの両方を節約できる。"],
             ["Dog owners can put photos and other information about their pets on the website.","飼い主はペットの写真や情報をサイトに掲載できる。"],
             ["They need kind people to care for their dogs.","犬の世話をしてくれる優しい人が必要だ。"],
             ["Moreover, playing with dogs reduces these people's stress.","さらに犬と遊ぶことでストレスが減る。"]
         ],
         "questions":[
             {"number":28,"choices":["have enough time","need them every day","know how to use them","want to break them"],"choiceTranslations":["十分な時間がある","毎日必要とする","使い方を知っている","壊したい"],"answer":2,"choiceAnalysis":["時間→工具と時間の関係が不明","毎日必要→正解。💡 毎日使わない→一度使ったら何ヶ月も保管→借りる方が良い","使い方→工具の保管の文脈に合わない","壊したい→文脈に合わない"],"grammar":"💡 every day＝毎日。cabinet＝キャビネット。garage＝ガレージ"},
             {"number":29,"choices":["more space to keep","kind people to care for","to give special food to","to learn more about"],"choiceTranslations":["もっとスペースが必要","世話してくれる優しい人","特別な食べ物を与える","もっと知る"],"answer":2,"choiceAnalysis":["スペース→犬を借りてもらう理由にならない","優しい人→正解。💡 忙しくなった→犬の世話をしてくれる優しい人が必要→サイトで探す","特別な食べ物→犬を貸す文脈に合わない","もっと知る→犬を貸す文脈に合わない"],"grammar":"💡 care for ～＝～の世話をする。look after＝世話をする"},
             {"number":30,"choices":["opening new websites","working with animal doctors","also good for the dogs","perfect for such people"],"choiceTranslations":["新しいサイトを開設","動物医と協力","犬にも良い","そのような人に最適"],"answer":4,"choiceAnalysis":["サイト開設→犬を飼えない人の文脈に合わない","動物医→文脈に合わない","犬にも良い→前文は人が犬を飼えない理由","そのような人に最適→正解。💡 犬を飼えない人→BorrowMyDoggyはそういう人に最適→動物と過ごせる"],"grammar":"💡 perfect for ～＝～に最適。such people＝そのような人々"}
         ]
        }
    ]
}

s4 = {"name":"大問4","nameEn":"Part 4","type":"reading-comprehension",
    "instruction":"次の英文A，Bの内容に関して，(31)から(37)までの質問に対して最も適切なもの，または文を完成させるのに最も適切なものを1，2，3，4の中から一つ選びなさい。",
    "passages":[
        {"label":"A","title":"Thanks!","format":"email",
         "meta":{"from":"John Evans","to":"Benjamin Crane","date":"May 30","subject":"Thanks!"},
         "paragraphs":[
             "Thank you for coming to my 16th birthday party last week. It was great to see you and all the rest of my friends there. Also, thank you for the jazz CD you gave me. I've been listening to it every day while I study. It's really relaxing! My sister really likes it, too, and she wants to borrow it.",
             "Anyway, I wanted to tell you about another gift that I got. It was from my aunt who lives in Oregon. It's a book about all the different hiking and backpacking trails in Oregon. It has trail maps, descriptions, and advice on the best camping sites along each trail. Now, I really want to go backpacking in Oregon!",
             "My aunt said she will take me backpacking this summer. She said I can choose any trail that I like. She also said I can bring a friend. Would you like to come with me? I've never been backpacking before. My aunt said it's better to only do a one-night trip the first time. That way, if it's too hard, we can go home the next day. Please speak to your parents and let me know if you can come. See you in school!"
         ],
         "translations":[
             "先週の僕の16歳の誕生日パーティーに来てくれてありがとう。君や他の友達全員に会えて嬉しかった。ジャズCDもありがとう。毎日勉強中に聴いてるよ。すごくリラックスできる！姉もすごく気に入って借りたがっているよ。",
             "ところで、もう一つもらったプレゼントのことを伝えたかったんだ。オレゴンに住んでいる叔母からのもので、オレゴンのハイキングやバックパッキングのトレイルについての本なんだ。トレイルの地図、説明、各トレイル沿いの最高のキャンプ場のアドバイスが載っている。オレゴンにバックパッキングに行きたくなった！",
             "叔母が今年の夏バックパッキングに連れて行ってくれるって。好きなトレイルを選んでいいって。友達を連れてきてもいいって。一緒に来ない？バックパッキングは初めてだから、叔母は初回は1泊だけにした方がいいって。大変すぎたら翌日帰れるからね。両親に聞いて来られるか教えて。学校で会おう！"
         ],
         "sentencePairs":[
             ["Thank you for coming to my 16th birthday party last week.","先週の16歳の誕生日パーティーに来てくれてありがとう。"],
             ["Also, thank you for the jazz CD you gave me.","ジャズCDもありがとう。"],
             ["I've been listening to it every day while I study.","毎日勉強中に聴いている。"],
             ["It's a book about all the different hiking and backpacking trails in Oregon.","オレゴンのハイキングとバックパッキングトレイルについての本だ。"],
             ["She also said I can bring a friend.","友達を連れてきてもいいって言ってた。"],
             ["My aunt said it's better to only do a one-night trip the first time.","初回は1泊だけの方がいいと叔母が言った。"],
             ["Please speak to your parents and let me know if you can come.","両親に聞いて来られるか教えて。"]
         ],
         "questions":[
             {"number":31,"question":"Last week,","questionTranslation":"先週、","choices":["John let his sister borrow a CD.","John had to study for a test.","Ben gave John a present.","Ben had his 16th birthday."],"choiceTranslations":["ジョンは姉にCDを貸した。","ジョンはテスト勉強をしなければならなかった。","ベンはジョンにプレゼントをあげた。","ベンは16歳の誕生日だった。"],"answer":3,"choiceAnalysis":["姉にCDを貸した→姉は借りたがっている（まだ貸していない）","テスト勉強→テストの話はない","プレゼントをあげた→正解。💡 「Thank you for the jazz CD you gave me」＝ベンがジョンにCDをあげた","ベンの誕生日→ジョンの誕生日"],"grammar":"💡 gave＝あげた（giveの過去形）。present＝プレゼント"},
             {"number":32,"question":"What did John's aunt give him?","questionTranslation":"ジョンの叔母は何をあげましたか？","choices":["Hiking equipment and a tent.","Directions for hiking to Oregon.","A book about places to walk.","A backpack made in Oregon."],"choiceTranslations":["ハイキング用品とテント。","オレゴンへのハイキングの道順。","歩ける場所についての本。","オレゴン製のバックパック。"],"answer":3,"choiceAnalysis":["ハイキング用品→本をもらった","道順→本の内容はトレイルガイド","歩ける場所の本→正解。💡 ハイキング＋バックパッキングのトレイル＝歩ける場所の本","バックパック→本をもらった"],"grammar":"💡 trail＝トレイル、歩行コース。places to walk＝歩ける場所（パラフレーズ）"},
             {"number":33,"question":"What does John invite Ben to do?","questionTranslation":"ジョンはベンを何に誘っていますか？","choices":["Help him choose his first hiking trail.","Stay at his aunt's house this summer.","Speak to his parents about school.","Go on a trip with him and his aunt."],"choiceTranslations":["最初のハイキングコースを選ぶのを手伝う。","今夏叔母の家に泊まる。","両親に学校について話す。","叔母と一緒に旅行に行く。"],"answer":4,"choiceAnalysis":["トレイル選び→叔母とのバックパッキングに来ないかと誘っている","叔母の家→バックパッキングの旅","学校について→「学校で会おう」は挨拶","旅行に行く→正解。💡 「Would you like to come with me?」→叔母と一緒にバックパッキング旅行"],"grammar":"💡 go on a trip＝旅行に行く。invite＝誘う"}
         ]
        },
        {"label":"B","title":"While You Wait",
         "paragraphs":[
             "Many airports are busy places. Travelers hurry through them to reach their airplanes or pick up their suitcases. The staff are busy and must handle many problems every day. Most art museums, on the other hand, are calm, quiet places. Visitors walk around slowly, looking at the artwork. The staff do not move much at all. Airports and art museums are very different types of places. So, it might be surprising to discover that more art museums are opening in airports.",
             "One example is Schiphol Airport in the Netherlands. Many travelers change airplanes at Schiphol Airport. As a result, they spend time there. The Netherlands is famous for art and art museums, and in 2002, the most famous art museum in the country opened a \"mini-museum\" in Schiphol Airport. Travelers can enjoy art by some of the most famous artists in the world while they wait for their next airplane.",
             "Other airports are starting to display more art, too. At Heathrow Airport in London, the T5 Gallery shows artwork by young, local artists. Travelers can even buy the artwork if they really like it. Terminal 2 at Mumbai Airport was built to be both an airport and an art museum. The building contains over 5,000 pieces of art from all over India, including both traditional and modern pieces.",
             "Some people do not think that art in airports is a good idea. They say that travelers are too busy to enjoy art. However, more people go to airports than art museums every year. As a result, more people have the chance to see art at airports. Travelers can learn not only about art, but also about the cultures of the countries they visit. Also, art can help people to relax even if they do not look at it closely — and this helps to make airports more enjoyable places."
         ],
         "translations":[
             "空港は忙しい場所だ。旅行者は飛行機に乗ったりスーツケースを受け取るために急ぐ。スタッフは忙しく毎日多くの問題に対処する。一方、美術館は穏やかで静かな場所だ。来場者はゆっくり歩きながら作品を鑑賞する。スタッフもほとんど動かない。空港と美術館はとても異なる場所だ。だから空港に美術館がオープンしていると知ると驚くかもしれない。",
             "一例はオランダのスキポール空港だ。多くの旅行者がスキポールで乗り換える。そのため時間を過ごす。オランダは芸術と美術館で有名で、2002年に国内で最も有名な美術館がスキポール空港に「ミニ美術館」を開設した。旅行者は次の飛行機を待つ間、世界で最も有名な芸術家の作品を楽しめる。",
             "他の空港でもアート展示が始まっている。ロンドンのヒースロー空港のT5ギャラリーでは若い地元アーティストの作品を展示。気に入れば購入もできる。ムンバイ空港のターミナル2は空港と美術館の両方として建設された。インド各地の5,000点以上の伝統的・現代的作品がある。",
             "空港にアートがあるのは良くないという人もいる。旅行者は忙しすぎてアートを楽しめないと言う。しかし美術館より空港に行く人の方が多い。だからより多くの人がアートを見る機会を得る。旅行者はアートだけでなく訪問先の文化も学べる。またアートはじっくり見なくてもリラックスに役立ち、空港をより楽しい場所にする。"
         ],
         "sentencePairs":[
             ["Airports and art museums are very different types of places.","空港と美術館はとても異なる場所だ。"],
             ["It might be surprising to discover that more art museums are opening in airports.","空港に美術館がオープンしていると知ると驚くかもしれない。"],
             ["Many travelers change airplanes at Schiphol Airport.","多くの旅行者がスキポール空港で乗り換える。"],
             ["The most famous art museum in the country opened a mini-museum in Schiphol Airport.","国内で最も有名な美術館がスキポール空港にミニ美術館を開設した。"],
             ["Terminal 2 at Mumbai Airport was built to be both an airport and an art museum.","ムンバイ空港ターミナル2は空港と美術館の両方として建設された。"],
             ["More people go to airports than art museums every year.","美術館より空港に行く人の方が多い。"],
             ["Art can help people to relax even if they do not look at it closely.","アートはじっくり見なくてもリラックスに役立つ。"]
         ],
         "questions":[
             {"number":34,"question":"What has been happening at airports recently?","questionTranslation":"最近空港で何が起きていますか？","choices":["They have been showing posters of famous museums.","More and more travelers have been arriving late.","The staff have been helping to carry people's bags.","Places showing art have been opening inside them."],"choiceTranslations":["有名な美術館のポスターを展示している。","遅れて到着する旅行者が増えている。","スタッフが荷物運びを手伝っている。","アートを展示する場所がオープンしている。"],"answer":4,"choiceAnalysis":["ポスター→美術館そのものが開設","遅刻→そのような話はない","荷物運び→そのような話はない","アート展示場所→正解。💡 「more art museums are opening in airports」"],"grammar":"💡 have been ～ing＝現在完了進行形。recently＝最近"},
             {"number":35,"question":"Travelers at Schiphol Airport","questionTranslation":"スキポール空港の旅行者は","choices":["have been able to get free tickets to museums since 2002.","take a long time to change from one airplane to another.","often meet famous artists while they wait for their airplanes.","can see art from the most famous collection in the Netherlands."],"choiceTranslations":["2002年から美術館の無料チケットを入手できる。","乗り換えに長い時間がかかる。","飛行機を待つ間に有名な芸術家に会う。","オランダで最も有名なコレクションのアートを見られる。"],"answer":4,"choiceAnalysis":["無料チケット→ミニ美術館が空港内にある","乗り換えに長時間→時間を過ごすとあるが長時間とは言っていない","芸術家に会う→芸術家の作品を見る","最も有名なコレクション→正解。💡 「the most famous art museum...opened a mini-museum」→最も有名なコレクション"],"grammar":"💡 collection＝コレクション。the most famous＝最も有名な"},
             {"number":36,"question":"What is special about Terminal 2 at Mumbai Airport?","questionTranslation":"ムンバイ空港ターミナル2の特別な点は？","choices":["It displays work by artists from all over the world.","It allows travelers to buy artwork by young artists.","It was designed for both travelers and art lovers.","It lends over 5,000 pieces of art to other airports."],"choiceTranslations":["世界中のアーティストの作品を展示。","若いアーティストの作品を購入できる。","旅行者とアート愛好家の両方のために設計された。","5,000点以上の作品を他の空港に貸し出す。"],"answer":3,"choiceAnalysis":["世界中→インド各地から","購入できる→ヒースロー空港の話","両方のために設計→正解。💡 「was built to be both an airport and an art museum」","貸し出す→空港内に所蔵"],"grammar":"💡 be designed for＝～のために設計される。be built to be＝～として建設される"},
             {"number":37,"question":"Why do some people think that art in airports is not a good idea?","questionTranslation":"空港のアートが良くないと考える人がいるのはなぜ？","choices":["Because fewer people are visiting art museums every year.","Because travelers want to relax when they are at airports.","Because airport users do not have time to look at it.","Because it does not help people learn about other cultures."],"choiceTranslations":["美術館を訪れる人が減っているから。","旅行者は空港でリラックスしたいから。","空港利用者はアートを見る時間がないから。","異文化を学ぶのに役立たないから。"],"answer":3,"choiceAnalysis":["訪問者減少→美術館より空港の方が多い（減少とは言っていない）","リラックスしたい→アートがリラックスに役立つと述べている","時間がない→正解。💡 「travelers are too busy to enjoy art」＝忙しすぎてアートを楽しめない＝時間がない","文化学習→アートは文化を学べると述べている（反論側）"],"grammar":"💡 too busy to ～＝忙しすぎて～できない"}
         ]
        }
    ]
}

data["sections"].append(s3)
data["sections"].append(s4)

# Vocabulary
data["vocabulary"] = [
    {"word":"ancient","meaning":"古代の","pos":"形容詞","level":"準2級","example":"They visited ancient buildings in Rome.","distractors":["正確な","責任のある","できない"]},
    {"word":"translate","meaning":"翻訳する","pos":"動詞","level":"準2級","example":"She translated the article into English.","distractors":["案内する","投げる","制御する"]},
    {"word":"countryside","meaning":"田舎","pos":"名詞","level":"準2級","example":"He goes for a drive in the countryside.","distractors":["決定","実験","画像"]},
    {"word":"tax","meaning":"税金","pos":"名詞","level":"準2級","example":"You need to pay tax on everything you buy.","distractors":["データ","合計","無駄"]},
    {"word":"angrily","meaning":"怒って","pos":"副詞","level":"準2級","example":"He shouted angrily at the driver.","distractors":["部分的に","密かに","きつく"]},
    {"word":"rescue","meaning":"救助する","pos":"動詞","level":"準2級","example":"Firefighters rescue people from buildings.","distractors":["量る","生産する","押印する"]},
    {"word":"release","meaning":"発売する","pos":"動詞","level":"準2級","example":"Her new CD will be released next week.","distractors":["閉じ込める","分ける","発明する"]},
    {"word":"spread","meaning":"広まる","pos":"動詞","level":"準2級","example":"The news spread through the school quickly.","distractors":["提供する","伸びる","立つ"]},
    {"word":"stage","meaning":"舞台","pos":"名詞","level":"準2級","example":"She felt nervous before getting on the stage.","distractors":["場","コート","画面"]},
    {"word":"lecture","meaning":"講義","pos":"名詞","level":"準2級","example":"She attended the professor's lecture.","distractors":["コメント","出荷","家具"]},
    {"word":"frankly speaking","meaning":"率直に言って","pos":"熟語","level":"準2級","example":"Frankly speaking, I disagree with this plan.","distractors":["泣いて","おしゃべりして","叫んで"]},
    {"word":"take out","meaning":"出す","pos":"句動詞","level":"準2級","example":"Could you take out the garbage?","distractors":["取る","脱ぐ","持っていく"]},
    {"word":"make up one's mind","meaning":"決心する","pos":"熟語","level":"準2級","example":"Please make up your mind quickly!","distractors":["自分のことに集中する","約束を守る","お釣りを取っておく"]},
    {"word":"come across","meaning":"偶然出会う","pos":"句動詞","level":"準2級","example":"He came across an old friend downtown.","distractors":["来る","横切る","一緒に来る"]},
    {"word":"confident","meaning":"自信がある","pos":"形容詞","level":"準2級","example":"The coach was confident of winning.","distractors":["疲れた","心配した","緊張した"]},
    {"word":"bring up","meaning":"育てる","pos":"句動詞","level":"準2級","example":"She was brought up in the United Kingdom.","distractors":["見せびらかす","入る","下に置く"]},
    {"word":"turn down","meaning":"（音量を）下げる","pos":"句動詞","level":"準2級","example":"Could you turn down the TV volume?","distractors":["調べる","記入する","立ち寄る"]},
    {"word":"give up","meaning":"諦める","pos":"句動詞","level":"準2級","example":"He gave up learning the piano.","distractors":["始める","続ける","楽しむ"]},
    {"word":"survey","meaning":"調査","pos":"名詞","level":"準2級","example":"A survey was taken by a major bank.","distractors":["結果","報告","記事"]},
    {"word":"stomachache","meaning":"腹痛","pos":"名詞","level":"準2級","example":"I have a terrible stomachache.","distractors":["頭痛","のどの痛み","腰痛"]},
    {"word":"trail","meaning":"トレイル、小道","pos":"名詞","level":"準2級","example":"The book shows different hiking trails in Oregon.","distractors":["道路","高速道路","駐車場"]},
    {"word":"backpacking","meaning":"バックパッキング旅行","pos":"名詞","level":"準2級","example":"I've never been backpacking before.","distractors":["キャンプ","ハイキング","サイクリング"]},
    {"word":"display","meaning":"展示する","pos":"動詞","level":"準2級","example":"The airport displays artwork by local artists.","distractors":["隠す","売る","作る"]},
    {"word":"artwork","meaning":"芸術作品","pos":"名詞","level":"準2級","example":"Visitors walk around slowly, looking at the artwork.","distractors":["建物","道具","家具"]},
    {"word":"calm","meaning":"穏やかな","pos":"形容詞","level":"準2級","example":"Art museums are calm, quiet places.","distractors":["忙しい","うるさい","混雑した"]},
    {"word":"handle","meaning":"対処する","pos":"動詞","level":"準2級","example":"The staff must handle many problems every day.","distractors":["無視する","避ける","作る"]},
    {"word":"contain","meaning":"含む","pos":"動詞","level":"準2級","example":"The building contains over 5,000 pieces of art.","distractors":["失う","壊す","隠す"]},
    {"word":"reduce","meaning":"減らす","pos":"動詞","level":"準2級","example":"Playing with dogs reduces stress.","distractors":["増やす","維持する","変える"]},
    {"word":"tool","meaning":"道具","pos":"名詞","level":"準2級","example":"People can borrow other people's tools.","distractors":["食べ物","服","本"]},
    {"word":"cabinet","meaning":"キャビネット","pos":"名詞","level":"準2級","example":"The drill is kept in a cabinet.","distractors":["机","棚","箱"]},
    {"word":"pumpkin","meaning":"カボチャ","pos":"名詞","level":"準2級","example":"Rachel taught Lisa how to make pumpkin soup.","distractors":["トマト","ジャガイモ","ニンジン"]},
    {"word":"including","meaning":"～を含めて","pos":"前置詞","level":"準2級","example":"It has art from all over India, including traditional pieces.","distractors":["～を除いて","～の代わりに","～に加えて"]},
    {"word":"culture","meaning":"文化","pos":"名詞","level":"準2級","example":"Travelers can learn about the cultures of other countries.","distractors":["歴史","政治","経済"]},
    {"word":"enjoyable","meaning":"楽しい","pos":"形容詞","level":"準2級","example":"Art helps to make airports more enjoyable places.","distractors":["退屈な","困難な","危険な"]},
    {"word":"stress","meaning":"ストレス","pos":"名詞","level":"準2級","example":"Playing with dogs reduces stress.","distractors":["喜び","興奮","疲労"]},
    {"word":"garage","meaning":"ガレージ","pos":"名詞","level":"準2級","example":"Tools are often kept in a garage.","distractors":["台所","寝室","浴室"]},
    {"word":"description","meaning":"説明、記述","pos":"名詞","level":"準2級","example":"The book has descriptions of each trail.","distractors":["写真","地図","動画"]},
    {"word":"contact","meaning":"連絡する","pos":"動詞","level":"準2級","example":"People use the website to contact dog owners.","distractors":["無視する","避ける","忘れる"]},
    {"word":"discover","meaning":"発見する","pos":"動詞","level":"準2級","example":"It might be surprising to discover art museums in airports.","distractors":["隠す","忘れる","無視する"]},
    {"word":"collection","meaning":"コレクション、収蔵品","pos":"名詞","level":"準2級","example":"The museum has the most famous collection.","distractors":["展覧会","建物","歴史"]},
    {"word":"accent","meaning":"アクセント、なまり","pos":"名詞","level":"準2級","example":"She has a British accent.","distractors":["声","言葉","文法"]},
    {"word":"volume","meaning":"音量","pos":"名詞","level":"準2級","example":"Could you turn down the volume of the TV?","distractors":["画面","チャンネル","電源"]}
]

# lessonPlan with 5 FocusPoints
data["lessonPlan"] = {"focusPoints": [
    {"id":"fp1","title":"much + 比較級（比較の強調）","subtitle":"Much + Comparative: Emphasizing Comparison",
     "explanation":"「much + 比較級」は「はるかに～」を表し、比較を強調します。much以外にも far, even, a lot, still が比較級を強調できます。very は比較級の強調には使えません。",
     "sourceQuote":"it was much more exciting than she expected","sourceLocation":"Part 1 Q18",
     "examples":[
         {"en":"It was much more exciting than she expected.","ja":"予想よりはるかに面白かった。","note":"much more exciting＝比較級の強調"},
         {"en":"This soup tasted much better than the supermarket's.","ja":"このスープはスーパーのよりずっと美味しかった。","note":"much better＝betterの強調"},
         {"en":"The city is far larger than I thought.","ja":"その都市は思ったよりはるかに大きかった。","note":"far＝muchの代わりに使える"}
     ],
     "practicePassage":{"en":"[出典: Pumpkin Soup 全文]\nLisa loves soup. She always has a cup of soup for breakfast. Sometimes, she has two cups. There are many kinds of soup at the supermarket that Lisa goes to. Some of them are quite expensive. However, Lisa likes to try them all. She does not mind spending a lot of money on soup every month. One day, Lisa's best friend, Rachel, said that she would teach Lisa how to make soup from pumpkins. At first, Lisa was worried that it might be too difficult for her. However, Rachel showed Lisa all the things she needed to do. It was not hard at all. In fact, making pumpkin soup was a lot of fun. The soup also tasted much better than the pumpkin soup from the supermarket.",
      "ja":"リサはスープが大好きだ。朝食にいつもスープを1杯飲む。2杯の時もある。スーパーには多くの種類があり、中にはかなり高いものもある。でもリサは全部試すのが好きでお金を気にしない。ある日親友レイチェルがカボチャスープの作り方を教えてくれた。最初は難しいかもと心配したが全く難しくなかった。実際とても楽しかった。スーパーのよりずっと美味しかった。",
      "audioFile":"audio/practice_pp1.mp3"},
     "practiceQuestions":[
         {"q":"much + 比較級の例を3つ挙げると？","a":"much better, much larger, much more interesting"},
         {"q":"veryは比較級を修飾できますか？","a":"いいえ。very more excitingやvery betterは不正。veryは原級のみ修飾"},
         {"q":"「far more expensive」の意味は？","a":"はるかに高い。farもmuchと同じく比較級を強調"},
         {"q":"「even better than before」の意味は？","a":"前よりさらに良い。evenも比較級を強調する"}
     ],
     "highlightPatterns":[
         "She does not mind spending a lot of money on soup every month",
         "At first, Lisa was worried that it might be too difficult for her"
     ],
     "highlightColor":"#4f8cff","highlightLabel":"比較級の強調"
    },
    {"id":"fp2","title":"give up ～ing（動名詞を取る動詞）","subtitle":"Give up + Gerund: Verbs Followed by Gerund",
     "explanation":"「give up ～ing」は「～するのを諦める」。give upは動名詞（～ing）のみを目的語にとり、不定詞（to～）は使えません。同様に enjoy, finish, mind, avoid, suggest なども動名詞を取る動詞です。",
     "sourceQuote":"I gave up learning the piano last year","sourceLocation":"Part 1 Q19",
     "examples":[
         {"en":"I gave up learning the piano last year.","ja":"去年ピアノを学ぶのを諦めた。","note":"give up ～ing。不定詞は使えない"},
         {"en":"She doesn't mind spending money on soup.","ja":"スープにお金を使うことを気にしない。","note":"mind ～ing＝動名詞を取る動詞"},
         {"en":"He enjoys playing with his dogs every day.","ja":"毎日犬と遊ぶことを楽しんでいる。","note":"enjoy ～ing＝動名詞のみ"}
     ],
     "practicePassage":{"en":"[出典: Sharing the Love of Dogs 第1段落]\nSome websites on the Internet let people borrow things from each other. For example, people can borrow other people's tools. Tools such as drills can be expensive, and most people do not need them every day. After a tool is used once, it is often kept in a cabinet or garage for months. Borrowing tools can save both money and space. Now, there is even a website for borrowing pets. It is called BorrowMyDoggy.",
      "ja":"インターネットの一部のサイトでは物の貸し借りができる。工具は高価で毎日は使わない。一度使った工具は何ヶ月も保管される。借りればお金とスペースを節約できる。ペットを借りるサイトまであり、BorrowMyDoggyという。",
      "audioFile":"audio/practice_pp2.mp3"},
     "practiceQuestions":[
         {"q":"動名詞のみを目的語にとる動詞を5つ挙げると？","a":"give up, enjoy, finish, mind, avoid"},
         {"q":"「I gave up to learn」は正しいですか？","a":"いいえ。give upは動名詞のみ。I gave up learningが正しい"},
         {"q":"stopは動名詞と不定詞で意味が変わる。違いは？","a":"stop ～ing＝～するのをやめる。stop to ～＝～するために立ち止まる"},
         {"q":"「She finished writing the report.」の意味は？","a":"彼女はレポートを書き終えた。finishも動名詞を取る"}
     ],
     "highlightPatterns":[
         "Tools such as drills can be expensive, and most people do not need them every day",
         "Borrowing tools can save both money and space"
     ],
     "highlightColor":"#34d399","highlightLabel":"動名詞を取る動詞"
    },
    {"id":"fp3","title":"過去分詞の後置修飾","subtitle":"Past Participle as Post-modifier",
     "explanation":"「名詞 + 過去分詞（+ by ～）」で「～された名詞」を表します。関係代名詞 which/that is を省略した形です。例: a survey taken by a bank ＝ a survey which was taken by a bank。",
     "sourceQuote":"According to a survey taken by a major bank","sourceLocation":"Part 1 Q20",
     "examples":[
         {"en":"According to a survey taken by a major bank, ...","ja":"大手銀行が実施した調査によると…","note":"taken＝過去分詞の後置修飾"},
         {"en":"The building contains art from all over India.","ja":"その建物にはインド各地の芸術作品がある。","note":"from＝前置詞句による後置修飾"},
         {"en":"The language spoken in this country is French.","ja":"この国で話されている言語はフランス語だ。","note":"spoken＝過去分詞の後置修飾"}
     ],
     "practicePassage":{"en":"[出典: While You Wait 第2段落]\nOne example is Schiphol Airport in the Netherlands. Many travelers change airplanes at Schiphol Airport. As a result, they spend time there. The Netherlands is famous for art and art museums, and in 2002, the most famous art museum in the country opened a \"mini-museum\" in Schiphol Airport. Travelers can enjoy art by some of the most famous artists in the world while they wait for their next airplane.",
      "ja":"一例はオランダのスキポール空港だ。多くの旅行者がスキポールで乗り換えるため時間を過ごす。オランダは芸術で有名で、2002年に最も有名な美術館が空港にミニ美術館を開設した。旅行者は次の飛行機を待つ間、世界的に有名な芸術家の作品を楽しめる。",
      "audioFile":"audio/practice_pp3.mp3"},
     "practiceQuestions":[
         {"q":"「a survey taken by a bank」を関係代名詞で書き換えると？","a":"a survey which was taken by a bank"},
         {"q":"「the language spoken in this country」の意味は？","a":"この国で話されている言語"},
         {"q":"現在分詞と過去分詞の後置修飾の違いは？","a":"現在分詞（～ing）＝能動。過去分詞（～ed）＝受動。例: a boy running（走っている少年）vs a book written（書かれた本）"},
         {"q":"「The pictures displayed in the airport are modern.」の意味は？","a":"空港に展示されている絵は現代的だ。displayed＝展示された"}
     ],
     "highlightPatterns":[
         "Many travelers change airplanes at Schiphol Airport",
         "Travelers can enjoy art by some of the most famous artists in the world"
     ],
     "highlightColor":"#f472b6","highlightLabel":"過去分詞の後置修飾"
    },
    {"id":"fp4","title":"too...to 構文（結果の不定詞）","subtitle":"Too...to Construction: Result Infinitive",
     "explanation":"「too + 形容詞/副詞 + to + 動詞」は「～すぎて…できない」を表します。so...that...can'tで言い換え可能。enough to ～（十分に～できる）と合わせて覚えましょう。",
     "sourceQuote":"travelers are too busy to enjoy art","sourceLocation":"Part 4B 第4段落",
     "examples":[
         {"en":"Travelers are too busy to enjoy art.","ja":"旅行者は忙しすぎてアートを楽しめない。","note":"too busy to enjoy＝忙しすぎて楽しめない"},
         {"en":"The movie was too exciting for her to believe.","ja":"その映画は彼女が信じられないほど面白かった。","note":"too...for+人+to～の形"},
         {"en":"He is old enough to drive a car.","ja":"彼は車を運転できる年齢だ。","note":"enough to＝十分に～できる（対比）"}
     ],
     "practicePassage":{"en":"[出典: While You Wait 第3-4段落]\nOther airports are starting to display more art, too. At Heathrow Airport in London, the T5 Gallery shows artwork by young, local artists. Travelers can even buy the artwork if they really like it. Terminal 2 at Mumbai Airport was built to be both an airport and an art museum. The building contains over 5,000 pieces of art from all over India, including both traditional and modern pieces. Some people do not think that art in airports is a good idea. They say that travelers are too busy to enjoy art.",
      "ja":"他の空港でもアート展示が増えている。ヒースロー空港のT5ギャラリーでは若い地元アーティストの作品を展示し購入もできる。ムンバイ空港ターミナル2は空港と美術館の両方として建設された。インド各地の5,000点以上の作品がある。空港にアートは良くないという人もいる。旅行者は忙しすぎてアートを楽しめないと言う。",
      "audioFile":"audio/practice_pp4.mp3"},
     "practiceQuestions":[
         {"q":"「too busy to enjoy」をso...thatで言い換えると？","a":"so busy that they cannot enjoy art"},
         {"q":"too...toとenough to の違いは？","a":"too...to＝～すぎてできない（否定的）。enough to＝十分に～できる（肯定的）"},
         {"q":"「The box is too heavy for me to carry.」の意味は？","a":"その箱は私が運ぶには重すぎる"},
         {"q":"「She is too young to understand.」をso...thatで書き換えると？","a":"She is so young that she cannot understand."}
     ],
     "highlightPatterns":[
         "Terminal 2 at Mumbai Airport was built to be both an airport and an art museum",
         "The building contains over 5,000 pieces of art from all over India"
     ],
     "highlightColor":"#fbbf24","highlightLabel":"too...to構文"
    },
    {"id":"fp5","title":"be brought up（受動態の句動詞）","subtitle":"Passive Phrasal Verbs: Be Brought Up",
     "explanation":"「be brought up」は「育てられる」の意味。bring up（育てる）の受動態です。句動詞の受動態は「be + 過去分詞 + 前置詞/副詞」の形になります。他にも be looked after（世話される）、be taken out（出される）など。",
     "sourceQuote":"she was brought up in the United Kingdom","sourceLocation":"Part 1 Q16",
     "examples":[
         {"en":"She was brought up in the United Kingdom.","ja":"彼女はイギリスで育てられた。","note":"bring up（育てる）の受動態"},
         {"en":"The garbage was taken out this morning.","ja":"ゴミは今朝出された。","note":"take out（出す）の受動態"},
         {"en":"The children are looked after by their grandmother.","ja":"子供たちは祖母に面倒を見られている。","note":"look after（世話する）の受動態"}
     ],
     "practicePassage":{"en":"[出典: Sharing the Love of Dogs 第2-3段落]\nDog owners might use BorrowMyDoggy if they become busy with work or they have to look after someone in their family. They need kind people to care for their dogs. People who want to borrow dogs use the website to contact dog owners. Dog owners can ask these people questions. In this way, owners can find out if people will be nice to their dogs. Many dog lovers cannot have a dog as a pet. BorrowMyDoggy is perfect for such people. They get a chance to spend time with their favorite animals. Moreover, playing with dogs reduces these people's stress and helps them to be healthy and happy.",
      "ja":"飼い主は仕事が忙しくなったり家族の世話が必要な時にBorrowMyDoggyを使う。犬の世話をしてくれる優しい人が必要だ。犬を借りたい人はサイトで飼い主に連絡する。多くの犬好きはペットとして犬を飼えない。BorrowMyDoggyはそのような人に最適で、大好きな動物と過ごす機会が得られ、ストレスも減る。",
      "audioFile":"audio/practice_pp5.mp3"},
     "practiceQuestions":[
         {"q":"「She was brought up in London.」の能動態は？","a":"Her parents brought her up in London.（主語は文脈による）"},
         {"q":"「look after」の受動態は？","a":"be looked after。例: The dogs are looked after by kind people."},
         {"q":"「turn down」の受動態は？","a":"be turned down。例: The volume was turned down."},
         {"q":"句動詞の受動態で注意すべき点は？","a":"前置詞/副詞を動詞から離さないこと。be brought upはOK、be brought upのupを省略しない"}
     ],
     "highlightPatterns":[
         "They need kind people to care for their dogs",
         "Moreover, playing with dogs reduces these people's stress and helps them to be healthy and happy"
     ],
     "highlightColor":"#a78bfa","highlightLabel":"受動態の句動詞"
    }
]}

with open(os.path.join(base, "data.json"), "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
total_q = sum(len(s.get("questions",[])) for s in data["sections"]) + sum(len(p.get("questions",[])) for s in data["sections"] for p in s.get("passages",[]))
print(f"data.json: {total_q} questions, {len(data['vocabulary'])} vocab, {len(data['lessonPlan']['focusPoints'])} FPs")

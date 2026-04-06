"""Generate sections 3-4 + vocabulary + lessonPlan for 2021-2"""
import json, os
base = r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade-pre2\2021-2"
data = json.load(open(os.path.join(base, "_part1.json"), "r", encoding="utf-8"))

s3 = {"name":"大問3","nameEn":"Part 3","type":"passage-fill",
    "instruction":"次の英文A，Bを読み，その文意にそって(26)から(30)までの(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選びなさい。",
    "passages":[
        {"label":"A","title":"Finding Their Way",
         "paragraphs":[
             "Yesterday, Jenny and her sister, Sophie, went by car to visit their cousin Ben in the countryside. They were looking forward to meeting him because they had not seen him for a long time. While Jenny drove, Sophie used the map application on her smartphone to find the way to his house. She had never done this before, so she was a little nervous at first. However, the map application ( 26 ). It told her the easiest route and where Jenny needed to turn.",
             "However, just before they reached Ben's town, Sophie's smartphone's battery died. She did not have a charger so she could not use her smartphone. Jenny stopped the car at a convenience store. Luckily, she had written ( 27 ) on a piece of paper. She called Ben from a public telephone outside the convenience store and told him what happened. He soon came to the convenience store to meet them. They were very glad to see him."
         ],
         "translations":[
             "昨日、ジェニーと姉のソフィーは田舎のいとこベンを訪ねるために車で出かけた。長い間会っていなかったので会うのを楽しみにしていた。ジェニーが運転する間、ソフィーはスマートフォンの地図アプリを使ってベンの家への道を探した。初めてだったので最初は少し緊張していた。しかし地図アプリは( 26 )。一番簡単なルートとジェニーが曲がるべき場所を教えてくれた。",
             "しかしベンの町に着く直前、ソフィーのスマートフォンのバッテリーが切れた。充電器がなかったのでスマートフォンが使えなかった。ジェニーはコンビニに車を停めた。幸い彼女は( 27 )を紙に書いていた。コンビニの外の公衆電話からベンに電話し、事情を説明した。ベンはすぐにコンビニまで迎えに来てくれた。とても嬉しかった。"
         ],
         "sentencePairs":[
             ["They were looking forward to meeting him because they had not seen him for a long time.","長い間会っていなかったので彼に会うのを楽しみにしていた。"],
             ["Sophie used the map application on her smartphone to find the way to his house.","ソフィーはスマホの地図アプリで彼の家への道を探した。"],
             ["She had never done this before, so she was a little nervous at first.","初めてだったので最初は少し緊張していた。"],
             ["It told her the easiest route and where Jenny needed to turn.","一番簡単なルートと曲がるべき場所を教えてくれた。"],
             ["Sophie's smartphone's battery died.","ソフィーのスマホのバッテリーが切れた。"],
             ["She called Ben from a public telephone outside the convenience store.","コンビニの外の公衆電話からベンに電話した。"]
         ],
         "questions":[
             {"number":26,"choices":["was easy to make","was very helpful","cost a lot of money","stopped working"],"choiceTranslations":["作るのが簡単だった","とても役に立った","お金がかかった","動かなくなった"],"answer":2,"choiceAnalysis":["作りやすい→アプリの使用者の視点として不適切","とても役立った→正解。💡 ルートと曲がる場所を教えてくれた＝役立った","お金がかかった→次文との流れに合わない","動かなくなった→次文でルートを教えてくれたので矛盾"],"grammar":"💡 helpful＝役に立つ。route＝ルート、道順"},
             {"number":27,"choices":["Ben's phone number","the name of Ben's town","her home address","what she needed to buy"],"choiceTranslations":["ベンの電話番号","ベンの町の名前","自宅の住所","買うべきもの"],"answer":1,"choiceAnalysis":["ベンの電話番号→正解。💡 公衆電話からベンに電話した＝電話番号を書いていた","町の名前→電話をかけた理由にならない","自宅の住所→ベンに電話する文脈に合わない","買うべきもの→ベンに電話する文脈に合わない"],"grammar":"💡 luckily＝幸い。public telephone＝公衆電話"}
         ]
        },
        {"label":"B","title":"Horse Sense",
         "paragraphs":[
             "When we are happy, angry, or sad, we show our feelings on our faces. By changing the shape of our eyes, mouth, and other parts of our face, we can show other people our feelings. Some animals do the same thing, too. Dogs, monkeys, and horses can show their feelings by using their faces.",
             "Understanding others' feelings ( 28 ). If we see an angry face, we can try to be careful. If we see a kind face, we can start to make friends.",
             "Recent research has found that horses can understand people's feelings by looking at their faces. Scientists showed large photographs of a person with either a happy face or an angry face to 28 horses. When the horses saw the angry face, they became afraid. The scientists knew the horses were afraid because they looked at the photograph ( 29 ). When a horse is scared of something, it will turn its head to the right and use its left eye to watch the thing.",
             "Perhaps over thousands of years of working with humans, horses have become able to understand humans' faces. Dogs have the same ability, perhaps because they have also worked with humans for thousands of years. Another explanation is that the 28 horses in the study came from local riding schools, where many different students ride the horses every day. It is possible that these animals learned to guess people's feelings because they had ( 30 ) in their lives."
         ],
         "translations":[
             "私たちは嬉しい時、怒っている時、悲しい時、顔に感情を表す。目、口、顔の他の部分の形を変えて、他の人に感情を伝えることができる。一部の動物も同じことをする。犬、サル、馬は顔を使って感情を表現できる。",
             "他者の感情を理解することは( 28 )。怒った顔を見れば気をつけようとする。優しい顔を見れば友達になろうとする。",
             "最近の研究で、馬が人の顔を見て感情を理解できることが分かった。科学者は28頭の馬に、嬉しい顔か怒った顔の人の大きな写真を見せた。馬が怒った顔を見ると怖がった。馬が怖がっていると分かったのは、写真を( 29 )見たからだ。馬が何かを怖がると頭を右に向け、左目でそれを見る。",
             "おそらく何千年もの間人間と一緒に働いてきたことで、馬は人の顔を理解できるようになった。犬にも同じ能力がある。おそらく犬も何千年も人間と一緒に働いてきたからだ。別の説明として、研究の28頭の馬は地元の乗馬学校から来ており、毎日多くの異なる生徒が馬に乗っている。これらの動物は人生で多くの人を( 30 )ために、人の感情を推測することを学んだ可能性がある。"
         ],
         "sentencePairs":[
             ["When we are happy, angry, or sad, we show our feelings on our faces.","嬉しい時、怒っている時、悲しい時、顔に感情を表す。"],
             ["Some animals do the same thing, too.","一部の動物も同じことをする。"],
             ["Recent research has found that horses can understand people's feelings by looking at their faces.","最近の研究で馬が人の顔を見て感情を理解できることが分かった。"],
             ["Scientists showed large photographs of a person with either a happy face or an angry face to 28 horses.","科学者は28頭の馬に嬉しい顔か怒った顔の写真を見せた。"],
             ["When a horse is scared of something, it will turn its head to the right and use its left eye to watch the thing.","馬が何かを怖がると頭を右に向け左目でそれを見る。"],
             ["Perhaps over thousands of years of working with humans, horses have become able to understand humans' faces.","何千年も人間と働いてきたことで馬は人の顔を理解できるようになった。"],
             ["It is possible that these animals learned to guess people's feelings.","これらの動物は人の感情を推測することを学んだ可能性がある。"]
         ],
         "questions":[
             {"number":28,"choices":["is not always useful","is often not easy","takes a long time","helps us stay safe"],"choiceTranslations":["いつも役立つわけではない","しばしば簡単ではない","長い時間がかかる","安全でいる助けになる"],"answer":4,"choiceAnalysis":["役立たない→次文の例と矛盾","簡単でない→次文で具体例を挙げており不適切","時間がかかる→次文と繋がらない","安全に役立つ→正解。💡 怒った顔→気をつける＝安全を守る"],"grammar":"💡 stay safe＝安全でいる。understanding feelings helps us stay safe"},
             {"number":29,"choices":["very carefully","several times","for less than one second","with their left eyes"],"choiceTranslations":["とても注意深く","何度も","1秒未満","左目で"],"answer":4,"choiceAnalysis":["注意深く→左目の説明と繋がらない","何度も→左目の説明と繋がらない","1秒未満→左目の説明と繋がらない","左目で→正解。💡 次文「頭を右に向け左目で見る」＝怖い時の反応"],"grammar":"💡 with their left eyes＝左目で。scared of＝～を怖がる"},
             {"number":30,"choices":["many good friends","plenty of food","been to many places","seen a lot of people"],"choiceTranslations":["多くの良い友達","たくさんの食べ物","多くの場所に行った","たくさんの人を見た"],"answer":4,"choiceAnalysis":["良い友達→感情の推測を学ぶ理由にならない","食べ物→感情と無関係","多くの場所→感情の推測と繋がらない","多くの人を見た→正解。💡 毎日多くの生徒が乗る→多くの人を見た→感情を学んだ"],"grammar":"💡 It is possible that ～＝～の可能性がある。guess＝推測する"}
         ]
        }
    ]
}

s4 = {"name":"大問4","nameEn":"Part 4","type":"reading-comprehension",
    "instruction":"次の英文A，Bの内容に関して，(31)から(37)までの質問に対して最も適切なもの，または文を完成させるのに最も適切なものを1，2，3，4の中から一つ選びなさい。",
    "passages":[
        {"label":"A","title":"Asian Tours","format":"email",
         "meta":{"from":"Charles Baker","to":"Allison Carter","date":"October 10","subject":"Asian tours"},
         "paragraphs":[
             "This is Charles, the travel agent at Wander World Tours. Thank you for contacting me yesterday about trips in Asia. You told me on the phone that you had a great time on our five-day Rhine River Tour in Germany last year. I thought about the things that you said you liked and didn't like about it.",
             "I remember you said your favorite part about the Rhine River trip was visiting a new place every day. You also liked that you didn't have to spend time on buses, and it was nice because you didn't have to move your things to new hotels. However, you also said the price of $3,500 for the trip was too much, and the food was great but expensive.",
             "Because of those things, I would like to recommend our Mekong River Tour in Vietnam. It lasts eight days and costs only $2,800. Also, we have one-city tours for some cities in Asia. With these, you can stay at the same hotel for the whole trip. The price is different for each city, so I'm sending you some information about these tours. They are attached to this e-mail. Please take a look at them and call me."
         ],
         "translations":[
             "こちらはワンダーワールドツアーの旅行代理店のチャールズです。昨日アジア旅行についてご連絡いただきありがとうございます。電話で、昨年のドイツのライン川5日間ツアーがとても楽しかったとおっしゃっていましたね。気に入った点と気に入らなかった点について考えました。",
             "ライン川ツアーで一番気に入ったのは毎日新しい場所を訪れることだとおっしゃっていましたね。バスに乗る時間がないのも良かったし、荷物を新しいホテルに移さなくてよいのも良かったと。ただ、3,500ドルは高すぎるとも、食事は素晴らしかったが高かったともおっしゃっていました。",
             "そのため、ベトナムのメコン川ツアーをお勧めしたいと思います。8日間で2,800ドルです。また、アジアのいくつかの都市の1都市ツアーもあります。これなら旅行中ずっと同じホテルに滞在できます。料金は都市ごとに異なりますので、ツアー情報をお送りします。このメールに添付しています。ご覧の上お電話ください。"
         ],
         "sentencePairs":[
             ["Thank you for contacting me yesterday about trips in Asia.","昨日アジア旅行についてご連絡いただきありがとうございます。"],
             ["You told me on the phone that you had a great time on our five-day Rhine River Tour.","電話でライン川5日間ツアーが楽しかったとおっしゃいましたね。"],
             ["Your favorite part was visiting a new place every day.","一番気に入ったのは毎日新しい場所を訪れることでした。"],
             ["You also liked that you didn't have to spend time on buses.","バスに時間を使わなくて良いのも気に入っていましたね。"],
             ["You also said the price of $3,500 for the trip was too much.","3,500ドルは高すぎるとおっしゃっていました。"],
             ["I would like to recommend our Mekong River Tour in Vietnam.","ベトナムのメコン川ツアーをお勧めします。"],
             ["It lasts eight days and costs only $2,800.","8日間で2,800ドルです。"],
             ["Please take a look at them and call me.","ご覧の上お電話ください。"]
         ],
         "questions":[
             {"number":31,"question":"Yesterday, Ms. Carter","questionTranslation":"昨日、カーターさんは","choices":["talked to a travel agent.","returned from a trip to Germany.","visited Wander World Tours.","sent an e-mail to Charles Baker."],"choiceTranslations":["旅行代理店の人と話した。","ドイツ旅行から帰った。","ワンダーワールドツアーを訪問した。","チャールズ・ベイカーにメールを送った。"],"answer":1,"choiceAnalysis":["旅行代理店と話した→正解。💡 「You told me on the phone」＝電話で話した＝旅行代理店と話した","ドイツから帰った→ドイツ旅行は昨年","訪問した→電話で連絡","メールを送った→電話で連絡した"],"grammar":"💡 contact＝連絡する。travel agent＝旅行代理店の担当者"},
             {"number":32,"question":"What did Ms. Carter like most about the Rhine River trip?","questionTranslation":"カーターさんがライン川ツアーで一番気に入ったことは？","choices":["Staying at a new hotel.","Spending time on the bus.","Going to new places every day.","Tasting great food."],"choiceTranslations":["新しいホテルに泊まること。","バスに乗って時間を過ごすこと。","毎日新しい場所に行くこと。","素晴らしい食事を味わうこと。"],"answer":3,"choiceAnalysis":["新しいホテル→荷物を移さなくて良いのが良かった（ホテルが変わらない）","バス→バスに乗らなくて良いのが良かった","毎日新しい場所→正解。💡 「your favorite part was visiting a new place every day」","食事→食事は良かったが高かった"],"grammar":"💡 favorite part＝一番気に入った部分"},
             {"number":33,"question":"What does Charles Baker ask Ms. Carter to do?","questionTranslation":"チャールズ・ベイカーはカーターさんに何を頼んでいますか？","choices":["E-mail him some information.","Call him about some trips to Asia.","Tell him her favorite city in Vietnam.","Pay $2,800 for a one-city tour."],"choiceTranslations":["情報をメールする。","アジア旅行について電話する。","ベトナムのお気に入りの都市を伝える。","一都市ツアーに2,800ドル払う。"],"answer":2,"choiceAnalysis":["メール→チャールズが情報を送る側","電話する→正解。💡 「Please take a look at them and call me」","お気に入りの都市→そのような依頼なし","2,800ドル→メコン川ツアーの価格で一都市ツアーではない"],"grammar":"💡 take a look at＝見る。call＝電話する"}
         ]
        },
        {"label":"B","title":"An Unusual Spice",
         "paragraphs":[
             "Hing is a spice which is widely used in Indian cooking. Many traditional Indian dishes are made from vegetables like potatoes and beans, and hing is added to the dishes to give them a stronger flavor. However, hing has a very bad smell until it is added to food and heated. The smell is so bad that hing must be kept inside a closed box, or everything nearby will start to smell like it.",
             "Hing is made from the juice of a plant called asafetida. This plant grows in dry, sunny places such as Iran, Afghanistan, and parts of China. Asafetida has a root like a carrot. When the plant is four years old, a hole is cut in the root, and a thick, sticky juice comes out — this is hing. This sticky juice soon dries and becomes hard. After that, it is often made into a powder before being sold.",
             "Cooking hing in hot butter or oil changes it. The bad smell goes away, and hing gives a wonderful flavor to food. Many people say it tastes like cooked onions. It is not often used in Western food, probably because not many cooks know about it. However, hing has been used for many years to make Worcestershire sauce — a British sauce that adds flavor to foods. This sauce was first created by British people living in India.",
             "There are other reasons for using hing, too. In the past, people wore small bags of hing around their necks to stop illnesses. Also, it has been taken as a medicine for hundreds of years to help with some stomach problems. In 1918, hing was used to fight a serious disease called Spanish flu. Recently, researchers have found that hing can actually protect people from diseases, so it seems that this unusual spice might become even more popular in the future."
         ],
         "translations":[
             "ヒングはインド料理で広く使われるスパイスだ。多くの伝統的なインド料理はジャガイモや豆などの野菜で作られ、ヒングは風味を強くするために加えられる。しかしヒングは食べ物に加えて加熱するまでとても臭い。臭いがひどいので密閉された箱に入れておかないと、近くのものすべてに臭いが移る。",
             "ヒングはアサフェティダという植物の汁から作られる。この植物はイラン、アフガニスタン、中国の一部など乾燥した日当たりの良い場所で育つ。アサフェティダはニンジンのような根がある。植物が4歳になると根に穴を開け、粘り気のある汁が出る——これがヒングだ。粘着性の汁はすぐに乾いて固くなる。その後、売られる前に粉にされることが多い。",
             "ヒングを熱いバターや油で調理すると変わる。臭いが消え、食べ物に素晴らしい風味を与える。多くの人は炒めた玉ねぎのような味だと言う。西洋料理ではあまり使われない。おそらく多くの調理人が知らないからだ。ただしヒングは長年、ウスターソース——食べ物に風味を加えるイギリスのソース——の原料として使われてきた。このソースはインドに住むイギリス人によって初めて作られた。",
             "ヒングを使う他の理由もある。昔は病気を防ぐためにヒングの小さな袋を首にかけていた。また何百年もの間、胃の問題を助ける薬として服用されてきた。1918年にはスペイン風邪と呼ばれる深刻な病気と戦うために使われた。最近、研究者はヒングが実際に病気から人を守ることを発見しており、この珍しいスパイスは将来さらに人気が出るかもしれない。"
         ],
         "sentencePairs":[
             ["Hing is a spice which is widely used in Indian cooking.","ヒングはインド料理で広く使われるスパイスだ。"],
             ["Hing has a very bad smell until it is added to food and heated.","ヒングは食べ物に加えて加熱するまでとても臭い。"],
             ["The smell is so bad that hing must be kept inside a closed box.","臭いがひどいので密閉箱に入れておかなければならない。"],
             ["Hing is made from the juice of a plant called asafetida.","ヒングはアサフェティダという植物の汁から作られる。"],
             ["This plant grows in dry, sunny places such as Iran, Afghanistan, and parts of China.","イラン、アフガニスタン、中国の一部など乾燥した日当たりの良い場所で育つ。"],
             ["Cooking hing in hot butter or oil changes it.","熱いバターや油で調理すると変わる。"],
             ["The bad smell goes away, and hing gives a wonderful flavor to food.","臭いが消え、素晴らしい風味を食べ物に与える。"],
             ["It is not often used in Western food, probably because not many cooks know about it.","西洋料理ではあまり使われない。多くの調理人が知らないからだ。"],
             ["Recently, researchers have found that hing can actually protect people from diseases.","最近研究者はヒングが実際に病気から人を守ることを発見した。"]
         ],
         "questions":[
             {"number":34,"question":"Hing is a spice which is","questionTranslation":"ヒングとは","choices":["made from potatoes and beans.","kept close to an open window.","used in Indian food to make the flavor stronger.","popular in India because of its wonderful smell."],"choiceTranslations":["ジャガイモと豆で作られる。","開いた窓の近くに置かれる。","インド料理の風味を強くするために使われる。","素晴らしい香りのためインドで人気。"],"answer":3,"choiceAnalysis":["ジャガイモと豆→料理の材料であってヒングの材料ではない","窓の近く→密閉箱に保管（窓は開けない）","風味を強くする→正解。💡 「added to give them a stronger flavor」","素晴らしい香り→加熱前は臭い"],"grammar":"💡 widely＝広く。flavor＝風味。be added to＝～に加えられる"},
             {"number":35,"question":"What is true about the plant called asafetida?","questionTranslation":"アサフェティダという植物について正しいのはどれですか？","choices":["It releases a thick, sticky juice from its flowers.","It grows in places where there is not much rain.","Its leaves can be made into a powder and then sold.","Its roots must be cut every four years to make it grow."],"choiceTranslations":["花から粘り気のある汁を出す。","雨の少ない場所で育つ。","葉を粉にして売れる。","4年ごとに根を切って成長させる必要がある。"],"answer":2,"choiceAnalysis":["花から→根から汁が出る","雨の少ない場所→正解。💡 「dry, sunny places」＝乾燥した場所＝雨が少ない","葉を粉に→汁を粉にする","4年ごとに根を切る→4歳で根に穴を開ける（成長目的ではない）"],"grammar":"💡 dry＝乾燥した。not much rain＝雨が少ない（パラフレーズ）"},
             {"number":36,"question":"Why is hing probably not often used in Western food?","questionTranslation":"ヒングが西洋料理であまり使われないのはなぜですか？","choices":["Because only a few chefs have ever heard about it.","Because many people do not like the taste of onions.","Because chefs prefer to use Worcestershire sauce.","Because cooking it with oil makes the smell worse."],"choiceTranslations":["知っている調理人がほとんどいないから。","多くの人が玉ねぎの味を好まないから。","調理人がウスターソースを好むから。","油で調理すると臭いが悪化するから。"],"answer":1,"choiceAnalysis":["知っている人が少ない→正解。💡 「not many cooks know about it」のパラフレーズ","玉ねぎの味→使わない理由ではない","ウスターソース→ヒングが原料","臭いが悪化→油で調理すると臭いが消える"],"grammar":"💡 a few＝少数の。not many＝多くない（パラフレーズ）"},
             {"number":37,"question":"What have researchers discovered about hing?","questionTranslation":"研究者はヒングについて何を発見しましたか？","choices":["Wearing a small bag of it keeps insects away.","Eating too much of it can cause stomach problems.","It is actually useful to help fight diseases.","It was first brought to Europe in 1918."],"choiceTranslations":["小さな袋を身につけると虫除けになる。","食べ過ぎると胃の問題を引き起こす。","実際に病気と戦うのに役立つ。","1918年に初めてヨーロッパに持ち込まれた。"],"answer":3,"choiceAnalysis":["虫除け→病気予防であって虫除けではない","胃の問題→胃の問題を助ける（引き起こさない）","病気と戦う→正解。💡 「hing can actually protect people from diseases」","1918年→スペイン風邪に使われた年で持ち込みではない"],"grammar":"💡 actually＝実際に。protect from＝～から守る"}
         ]
        }
    ]
}

data["sections"].append(s3)
data["sections"].append(s4)

# Vocabulary
data["vocabulary"] = [
    {"word":"trouble","meaning":"困難、問題","pos":"名詞","level":"準2級","example":"She had trouble with her homework.","distractors":["興味","沈黙","記憶"]},
    {"word":"formal","meaning":"正式な、フォーマルな","pos":"形容詞","level":"準2級","example":"You need to wear formal clothes to the party.","distractors":["厳しい","否定的な","鋭い"]},
    {"word":"perform","meaning":"演じる、実行する","pos":"動詞","level":"準2級","example":"She will perform in the school play.","distractors":["帆走する","押印する","生産する"]},
    {"word":"treat","meaning":"扱う","pos":"動詞","level":"準2級","example":"He always treats his friends kindly.","distractors":["無視する","溶かす","届ける"]},
    {"word":"surface","meaning":"表面","pos":"名詞","level":"準2級","example":"The surface of the lake was frozen.","distractors":["物体","位置","高さ"]},
    {"word":"recover","meaning":"回復する","pos":"動詞","level":"準2級","example":"It took her three months to recover from her injury.","distractors":["閉める","抗議する","行進する"]},
    {"word":"happily","meaning":"楽しそうに","pos":"副詞","level":"準2級","example":"The children were playing happily in the park.","distractors":["突然","ほとんど～ない","すぐに"]},
    {"word":"recognize","meaning":"認識する、見分ける","pos":"動詞","level":"準2級","example":"I didn't recognize him because he changed so much.","distractors":["言及する","設立する","組み合わせる"]},
    {"word":"experiment","meaning":"実験","pos":"名詞","level":"準2級","example":"We did an experiment to test the theory.","distractors":["オーケストラ","態度","画像"]},
    {"word":"rhythm","meaning":"リズム","pos":"名詞","level":"準2級","example":"I like music with a fast rhythm.","distractors":["距離","チャンネル","信念"]},
    {"word":"catch up with","meaning":"追いつく","pos":"句動詞","level":"準2級","example":"He studied hard to catch up with his classmates.","distractors":["思いつく","考え直す","気づく"]},
    {"word":"look down on","meaning":"見下す","pos":"句動詞","level":"準2級","example":"You should never look down on others.","distractors":["振り返る","見透かす","検討する"]},
    {"word":"ashamed","meaning":"恥じている","pos":"形容詞","level":"準2級","example":"He was ashamed of his behavior.","distractors":["誇りに思う","満足した","怒った"]},
    {"word":"get rid of","meaning":"処分する、取り除く","pos":"句動詞","level":"準2級","example":"We need to get rid of this old furniture.","distractors":["修理する","保管する","購入する"]},
    {"word":"instead of","meaning":"～の代わりに","pos":"熟語","level":"準2級","example":"She drank tea instead of coffee.","distractors":["～の準備ができて","～によると","～と同じ"]},
    {"word":"suffer from","meaning":"～に苦しむ","pos":"句動詞","level":"準2級","example":"Many people suffer from headaches.","distractors":["～を楽しむ","～を望む","～を恐れる"]},
    {"word":"try on","meaning":"試着する","pos":"句動詞","level":"準2級","example":"Can I try on this jacket?","distractors":["現れる","引き受ける","あきらめる"]},
    {"word":"whoever","meaning":"～する人は誰でも","pos":"代名詞","level":"準2級","example":"Whoever finishes first can leave early.","distractors":["何でも","いつでも","どこでも"]},
    {"word":"spice","meaning":"スパイス、香辛料","pos":"名詞","level":"準2級","example":"Indian cooking uses many different spices.","distractors":["ソース","材料","野菜"]},
    {"word":"flavor","meaning":"風味、味","pos":"名詞","level":"準2級","example":"This spice gives a wonderful flavor to food.","distractors":["香り","色","食感"]},
    {"word":"root","meaning":"根","pos":"名詞","level":"準2級","example":"The roots of the tree grew deep into the ground.","distractors":["葉","花","枝"]},
    {"word":"powder","meaning":"粉","pos":"名詞","level":"準2級","example":"The spice is sold as a powder.","distractors":["液体","固体","結晶"]},
    {"word":"protect","meaning":"守る、保護する","pos":"動詞","level":"準2級","example":"Hing can protect people from diseases.","distractors":["攻撃する","危険にさらす","無視する"]},
    {"word":"researcher","meaning":"研究者","pos":"名詞","level":"準2級","example":"Researchers discovered new uses for the spice.","distractors":["学生","教師","管理者"]},
    {"word":"disease","meaning":"病気","pos":"名詞","level":"準2級","example":"The medicine can fight many diseases.","distractors":["けが","症状","治療"]},
    {"word":"recommend","meaning":"勧める","pos":"動詞","level":"準2級","example":"I would like to recommend this tour.","distractors":["拒否する","延期する","取り消す"]},
    {"word":"attach","meaning":"添付する","pos":"動詞","level":"準2級","example":"The files are attached to this e-mail.","distractors":["削除する","印刷する","保存する"]},
    {"word":"contact","meaning":"連絡する","pos":"動詞","level":"準2級","example":"Please contact me if you have any questions.","distractors":["無視する","避ける","忘れる"]},
    {"word":"charger","meaning":"充電器","pos":"名詞","level":"準2級","example":"She forgot to bring her phone charger.","distractors":["バッテリー","ケーブル","画面"]},
    {"word":"route","meaning":"ルート、道順","pos":"名詞","level":"準2級","example":"The map showed the easiest route.","distractors":["地図","目的地","距離"]},
    {"word":"nervous","meaning":"緊張した","pos":"形容詞","level":"準2級","example":"She was nervous before her first presentation.","distractors":["リラックスした","退屈した","興奮した"]},
    {"word":"countryside","meaning":"田舎","pos":"名詞","level":"準2級","example":"They drove to the countryside to visit their cousin.","distractors":["都市","郊外","海岸"]},
    {"word":"ability","meaning":"能力","pos":"名詞","level":"準2級","example":"Dogs have the ability to understand human emotions.","distractors":["習慣","経験","知識"]},
    {"word":"traditional","meaning":"伝統的な","pos":"形容詞","level":"準2級","example":"Many traditional dishes use local ingredients.","distractors":["現代的な","外国の","簡単な"]},
    {"word":"explanation","meaning":"説明","pos":"名詞","level":"準2級","example":"There is another explanation for this result.","distractors":["質問","回答","議論"]},
    {"word":"widely","meaning":"広く","pos":"副詞","level":"準2級","example":"This method is widely used around the world.","distractors":["狭く","少し","まれに"]},
    {"word":"sticky","meaning":"粘り気のある","pos":"形容詞","level":"準2級","example":"A thick, sticky juice comes out from the root.","distractors":["乾いた","硬い","柔らかい"]},
    {"word":"actually","meaning":"実際に","pos":"副詞","level":"準2級","example":"Researchers found that hing can actually protect people.","distractors":["おそらく","ほぼ","めったに"]},
    {"word":"medicine","meaning":"薬","pos":"名詞","level":"準2級","example":"Hing has been taken as medicine for hundreds of years.","distractors":["食品","サプリ","ビタミン"]},
    {"word":"cancel","meaning":"中止する","pos":"動詞","level":"準2級","example":"The match was canceled due to the bus breakdown.","distractors":["延期する","開始する","続ける"]},
    {"word":"author","meaning":"著者","pos":"名詞","level":"準2級","example":"Do you know who the author is?","distractors":["読者","編集者","出版社"]},
    {"word":"injury","meaning":"けが","pos":"名詞","level":"準2級","example":"It took months to recover from her injury.","distractors":["病気","痛み","手術"]}
]

# lessonPlan with 5 FocusPoints
data["lessonPlan"] = {"focusPoints": [
    {"id":"fp1","title":"whoever / whatever 複合関係代名詞","subtitle":"Compound Relative Pronouns",
     "explanation":"whoever（～する人は誰でも）、whatever（何でも）、whichever（どちらでも）は「先行詞＋関係代名詞」を一語にまとめた複合関係代名詞です。whoever = anyone who、whatever = anything that と言い換えられます。",
     "sourceQuote":"The school gives a prize to whoever makes the best speech","sourceLocation":"Part 1 Q19",
     "examples":[
         {"en":"The school gives a prize to whoever makes the best speech.","ja":"学校は最高のスピーチをした人に賞を与える。","note":"whoever = anyone who。先行詞を含む"},
         {"en":"You can eat whatever you want.","ja":"何でも好きなものを食べていいよ。","note":"whatever = anything that"},
         {"en":"Whoever comes first will get the best seat.","ja":"最初に来た人が一番良い席をもらえる。","note":"whoever＝主語になる場合もある"}
     ],
     "practicePassage":{"en":"[出典: Finding Their Way 第1段落]\nYesterday, Jenny and her sister, Sophie, went by car to visit their cousin Ben in the countryside. They were looking forward to meeting him because they had not seen him for a long time. While Jenny drove, Sophie used the map application on her smartphone to find the way to his house. She had never done this before, so she was a little nervous at first. However, the map application was very helpful. It told her the easiest route and where Jenny needed to turn.",
      "ja":"昨日、ジェニーと姉のソフィーはいとこのベンを訪ねるために車で田舎に出かけた。長い間会っていなかったので楽しみにしていた。ジェニーが運転する間、ソフィーはスマホの地図アプリでベンの家への道を探した。初めてだったので少し緊張したが、地図アプリはとても役立った。一番簡単なルートと曲がる場所を教えてくれた。",
      "audioFile":"audio/practice_pp1.mp3"},
     "practiceQuestions":[
         {"q":"whoever を anyone who を使って言い換えると？","a":"The school gives a prize to anyone who makes the best speech."},
         {"q":"whatever と whenever の違いは？","a":"whatever＝何でも（もの）。whenever＝いつでも（時）"},
         {"q":"「Whoever wants to join can come.」の意味は？","a":"参加したい人は誰でも来ていい。whoever＝主語として使用"},
         {"q":"「Whatever happens, don't give up.」の意味は？","a":"何が起こっても諦めるな。whatever＝譲歩の用法"}
     ],
     "highlightPatterns":[
         "They were looking forward to meeting him because they had not seen him for a long time",
         "She had never done this before, so she was a little nervous at first"
     ],
     "highlightColor":"#4f8cff","highlightLabel":"複合関係代名詞"
    },
    {"id":"fp2","title":"need to be + 過去分詞（受動態の不定詞）","subtitle":"Passive Infinitive: need to be + Past Participle",
     "explanation":"「need to be + 過去分詞」は「～される必要がある」を表します。主語が動作を受ける側の場合に使います。また「need ～ing」も同じ意味で使えます（例: The floor needs cleaning.）。",
     "sourceQuote":"It needs to be cleaned","sourceLocation":"Part 1 Q20",
     "examples":[
         {"en":"This kitchen floor needs to be cleaned.","ja":"この台所の床は掃除される必要がある。","note":"needs to be cleaned = needs cleaning。受動態の不定詞"},
         {"en":"The report needs to be finished by Friday.","ja":"レポートは金曜日までに仕上げる必要がある。","note":"受動態の不定詞。主語が動作を受ける側"},
         {"en":"This car needs to be repaired.","ja":"この車は修理される必要がある。","note":"needs to be repaired = needs repairing"}
     ],
     "practicePassage":{"en":"[出典: Horse Sense 第2-3段落]\nUnderstanding others' feelings helps us stay safe. If we see an angry face, we can try to be careful. If we see a kind face, we can start to make friends. Recent research has found that horses can understand people's feelings by looking at their faces. Scientists showed large photographs of a person with either a happy face or an angry face to 28 horses. When the horses saw the angry face, they became afraid.",
      "ja":"他者の感情を理解することは安全でいる助けになる。怒った顔を見れば気をつけようとする。優しい顔を見れば友達になろうとする。最近の研究で馬が人の顔を見て感情を理解できることが分かった。科学者は28頭の馬に嬉しい顔か怒った顔の大きな写真を見せた。馬が怒った顔を見ると怖がった。",
      "audioFile":"audio/practice_pp2.mp3"},
     "practiceQuestions":[
         {"q":"「needs to be cleaned」を「needs ～ing」で言い換えると？","a":"needs cleaning。意味は同じ「掃除される必要がある」"},
         {"q":"「The wall needs to be painted.」の意味は？","a":"壁は塗られる必要がある（ペンキを塗る必要がある）"},
         {"q":"能動態と受動態の不定詞の違いは？","a":"能動態: need to clean（自分が掃除する）。受動態: need to be cleaned（掃除される）"},
         {"q":"「This problem needs to be solved immediately.」を和訳すると？","a":"この問題はすぐに解決される必要がある"}
     ],
     "highlightPatterns":[
         "Understanding others' feelings helps us stay safe",
         "Scientists showed large photographs of a person with either a happy face or an angry face to 28 horses"
     ],
     "highlightColor":"#34d399","highlightLabel":"受動態不定詞"
    },
    {"id":"fp3","title":"one...the other（2つのうちの片方・もう片方）","subtitle":"One...the Other: Referring to Two Things",
     "explanation":"「one...the other」は「（2つのうち）一方…もう一方」を表します。3つ以上の場合は「one...another...the other」や「some...others」を使います。",
     "sourceQuote":"One is in France and the other is in Germany","sourceLocation":"Part 1 Q18",
     "examples":[
         {"en":"One is in France and the other is in Germany.","ja":"一方はフランスで、もう一方はドイツだ。","note":"one...the other＝2つのうち一方ともう一方"},
         {"en":"I have two cats. One is black and the other is white.","ja":"猫を2匹飼っている。1匹は黒で、もう1匹は白だ。","note":"2匹のうちの1匹ともう1匹"},
         {"en":"Some students like math, and others prefer science.","ja":"数学が好きな生徒もいれば、理科を好む生徒もいる。","note":"some...others＝3つ以上の場合"}
     ],
     "practicePassage":{"en":"[出典: An Unusual Spice 第1段落]\nHing is a spice which is widely used in Indian cooking. Many traditional Indian dishes are made from vegetables like potatoes and beans, and hing is added to the dishes to give them a stronger flavor. However, hing has a very bad smell until it is added to food and heated. The smell is so bad that hing must be kept inside a closed box, or everything nearby will start to smell like it.",
      "ja":"ヒングはインド料理で広く使われるスパイスだ。多くの伝統的なインド料理はジャガイモや豆などの野菜で作られ、ヒングは風味を強くするために加えられる。しかしヒングは食べ物に加えて加熱するまでとても臭い。臭いがひどいので密閉箱に入れておかないと近くのものに臭いが移る。",
      "audioFile":"audio/practice_pp3.mp3"},
     "practiceQuestions":[
         {"q":"「one...the other」と「one...another」の違いは？","a":"the other＝残り1つ（2つの場合）。another＝もう1つ（3つ以上の場合）"},
         {"q":"「some...others」はどんな時に使う？","a":"不特定の複数のうち「一部は…他は…」と対比する時。3つ以上"},
         {"q":"「I want the other one.」の意味は？","a":"（2つのうち）もう一方が欲しい"},
         {"q":"「Some like coffee, others prefer tea.」の意味は？","a":"コーヒーが好きな人もいれば、紅茶を好む人もいる"}
     ],
     "highlightPatterns":[
         "Hing is a spice which is widely used in Indian cooking",
         "hing is added to the dishes to give them a stronger flavor"
     ],
     "highlightColor":"#f472b6","highlightLabel":"one/the other"
    },
    {"id":"fp4","title":"so...that 構文（結果を表す副詞節）","subtitle":"So...that Construction for Result Clauses",
     "explanation":"「so + 形容詞/副詞 + that + S + V」は「とても…なので～する」という結果を表します。that以下が結果を述べます。such...that構文（such + 名詞 + that）も同様の意味です。",
     "sourceQuote":"The smell is so bad that hing must be kept inside a closed box","sourceLocation":"Part 4B 第1段落",
     "examples":[
         {"en":"The smell is so bad that hing must be kept inside a closed box.","ja":"臭いがとてもひどいので密閉箱に入れておかなければならない。","note":"so bad that...＝とても臭いので…という結果"},
         {"en":"He was so tired that he fell asleep immediately.","ja":"彼はとても疲れていたのですぐに眠ってしまった。","note":"so tired that＝とても疲れたので"},
         {"en":"It was such a good book that I read it twice.","ja":"とても良い本だったので2回読んだ。","note":"such a good book that＝名詞を修飾する場合はsuch"}
     ],
     "practicePassage":{"en":"[出典: An Unusual Spice 第2-3段落]\nHing is made from the juice of a plant called asafetida. This plant grows in dry, sunny places such as Iran, Afghanistan, and parts of China. Asafetida has a root like a carrot. When the plant is four years old, a hole is cut in the root, and a thick, sticky juice comes out — this is hing. This sticky juice soon dries and becomes hard. After that, it is often made into a powder before being sold. Cooking hing in hot butter or oil changes it. The bad smell goes away, and hing gives a wonderful flavor to food.",
      "ja":"ヒングはアサフェティダという植物の汁から作られる。この植物はイラン、アフガニスタン、中国の一部など乾燥した日当たりの良い場所で育つ。アサフェティダはニンジンのような根がある。4歳になると根に穴を開け粘り気のある汁が出る。粘着性の汁はすぐ乾いて固くなる。その後粉にされて売られる。熱いバターや油で調理すると臭いが消え素晴らしい風味になる。",
      "audioFile":"audio/practice_pp4.mp3"},
     "practiceQuestions":[
         {"q":"「so...that」構文を「too...to」で言い換えると？","a":"The smell is too bad to keep outside a closed box.（ただし意味が少し変わる）"},
         {"q":"so...thatとsuch...thatの違いは？","a":"so＋形容詞/副詞＋that。such＋名詞＋that。例: so good that / such a good book that"},
         {"q":"「He ran so fast that nobody could catch him.」の意味は？","a":"彼はとても速く走ったので誰も追いつけなかった"},
         {"q":"that は省略できますか？","a":"口語ではthatを省略することが多い。The smell is so bad (that) it must be kept inside a box."}
     ],
     "highlightPatterns":[
         "Hing is made from the juice of a plant called asafetida",
         "This sticky juice soon dries and becomes hard",
         "Cooking hing in hot butter or oil changes it"
     ],
     "highlightColor":"#fbbf24","highlightLabel":"so...that構文"
    },
    {"id":"fp5","title":"used to ～（過去の習慣・状態）","subtitle":"Used to: Past Habits and States",
     "explanation":"「used to + 動詞の原形」は「以前は～していた（が今はしていない）」を表します。過去の習慣や状態で、現在とは異なることを示します。「be used to ～ing」（～に慣れている）と混同しないよう注意。",
     "sourceQuote":"Adam used to look down on people who could not swim","sourceLocation":"Part 1 Q12",
     "examples":[
         {"en":"Adam used to look down on people who could not swim.","ja":"アダムは以前、泳げない人を見下していた。","note":"used to＝以前は～していた。今は見下していない"},
         {"en":"I used to live in Tokyo, but now I live in Osaka.","ja":"以前は東京に住んでいたが、今は大阪に住んでいる。","note":"used to live＝以前住んでいた"},
         {"en":"She is used to getting up early.","ja":"彼女は早起きに慣れている。","note":"be used to ～ing＝～に慣れている（別の表現）"}
     ],
     "practicePassage":{"en":"[出典: An Unusual Spice 第4段落]\nThere are other reasons for using hing, too. In the past, people wore small bags of hing around their necks to stop illnesses. Also, it has been taken as a medicine for hundreds of years to help with some stomach problems. In 1918, hing was used to fight a serious disease called Spanish flu. Recently, researchers have found that hing can actually protect people from diseases, so it seems that this unusual spice might become even more popular in the future.",
      "ja":"ヒングを使う他の理由もある。昔は病気を防ぐためにヒングの小さな袋を首にかけていた。また何百年もの間、胃の問題の薬として服用されてきた。1918年にはスペイン風邪に使われた。最近研究者はヒングが実際に病気から守ることを発見しており、将来さらに人気が出るかもしれない。",
      "audioFile":"audio/practice_pp5.mp3"},
     "practiceQuestions":[
         {"q":"「used to」と「would」の違いは？","a":"used to＝過去の習慣＋状態。would＝過去の習慣のみ（状態には使えない）"},
         {"q":"「used to」と「be used to」の違いは？","a":"used to V＝以前～していた。be used to Ving＝～に慣れている"},
         {"q":"「I used to play soccer.」の否定形は？","a":"I didn't use to play soccer. / I never used to play soccer."},
         {"q":"「Did you use to live here?」の意味は？","a":"以前ここに住んでいましたか？（疑問文ではused→use）"}
     ],
     "highlightPatterns":[
         "In the past, people wore small bags of hing around their necks to stop illnesses",
         "it has been taken as a medicine for hundreds of years to help with some stomach problems",
         "researchers have found that hing can actually protect people from diseases"
     ],
     "highlightColor":"#a78bfa","highlightLabel":"used to"
    }
]}

with open(os.path.join(base, "data.json"), "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
total_q = sum(len(s.get("questions",[])) for s in data["sections"]) + sum(len(p.get("questions",[])) for s in data["sections"] for p in s.get("passages",[]))
print(f"data.json: {total_q} questions, {len(data['vocabulary'])} vocab, {len(data['lessonPlan']['focusPoints'])} FPs")

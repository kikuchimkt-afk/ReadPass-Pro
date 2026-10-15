"""Parts 1-2 of EIKEN Grade Pre-2 2024-3 Saturday sub-venue (January 25, 2025).

Loaded by gen_pre2_2024-3-sat.py, which passes its helper functions as ``h``.
English text and choices are transcribed from the rendered booklet pages.
"""

from __future__ import annotations


def build_part1(h) -> list[dict]:
    q = h.question
    return [
        q(
            1,
            "Tanya likes to ( 1 ) something for her family every weekend. This Saturday, she plans to make some delicious chocolate chip cookies.",
            "ターニャは毎週末、家族のために何かを（1）のが好きです。今週の土曜日は、おいしいチョコチップクッキーを作る予定です。",
            ["burn", "bend", "bake", "burst"],
            ["燃やす・焦がす", "曲げる", "焼く", "破裂する"],
            3,
            [
                "burnは『燃やす・焦がす』。家族のために何かを燃やすのでは、クッキーを作る話につながらない",
                "bendは『曲げる』。2文目のクッキー作りの予定と結びつかない",
                "bakeは『（オーブンで）焼く』。2文目でchocolate chip cookiesを作る予定だと述べているのが根拠",
                "burstは『破裂する・破裂させる』。お菓子作りの場面に合わない",
            ],
            "💡 bake＝（パンや菓子をオーブンで）焼く。like to do＝～するのが好き。plan to do＝～する予定だ。",
        ),
        q(
            2,
            "A : Mr. Smith, is my answer to this math problem ( 2 )?\nB : No, Johnny, it's wrong. Please try solving the problem again.",
            "A：スミス先生、この数学の問題の私の答えは（2）ですか。\nB：いいえ、ジョニー、間違っています。もう一度問題を解いてみてください。",
            ["awful", "correct", "gentle", "tight"],
            ["ひどい", "正しい", "優しい・穏やかな", "きつい"],
            2,
            [
                "awfulは『ひどい』。答えの正誤を尋ねる言い方にならず、wrongとの対比が成り立たない",
                "correctは『正しい』。Noと答えてit's wrong（間違っている）と続くので、正しいかどうかを尋ねている",
                "gentleは『優しい・穏やかな』。人の性格や態度を表す語で、答えの正誤を表さない",
                "tightは『きつい』。服や予定がきついことを表し、答えには使わない",
            ],
            "💡 correct⇔wrong（正しい⇔間違った）。try doing＝試しに～してみる。",
        ),
        q(
            3,
            "Carla asked Professor Anderson to speak more loudly because she could not hear his lecture ( 3 ).",
            "カーラはアンダーソン教授に、もっと大きな声で話してくれるよう頼みました。教授の講義が（3）聞こえなかったからです。",
            ["rapidly", "easily", "nervously", "calmly"],
            ["急速に", "簡単に・楽に", "神経質に・不安そうに", "落ち着いて"],
            2,
            [
                "rapidlyは『急速に』。講義を急速に聞くとは言わず、大きな声を頼む理由にならない",
                "easilyは『簡単に・楽に』。could not hear ... easily（楽に聞き取れなかった）が、大きな声で話すよう頼んだ理由になる",
                "nervouslyは『神経質に・不安そうに』。聞き取りにくさの説明にならない",
                "calmlyは『落ち着いて』。声を大きくしてほしい理由と結びつかない",
            ],
            "💡 ask 人 to do＝人に～するよう頼む。more loudly＝もっと大きな声で（loudlyの比較級）。not ... easily＝楽には～できない。",
        ),
        q(
            4,
            "When Tom's mother asked him if he had eaten the cake, he ( 4 ) it. He said that his brother Greg had eaten it.",
            "トムのお母さんがケーキを食べたのかと尋ねると、トムはそれを（4）。兄（弟）のグレッグが食べたと言いました。",
            ["respected", "denied", "compared", "encouraged"],
            ["尊敬した", "否定した", "比較した", "励ました"],
            2,
            [
                "respectedは『尊敬した』。ケーキを食べたかという質問への反応にならない",
                "deniedは『否定した』。自分ではなくグレッグが食べたと言っているので、食べたことを否定したとわかる",
                "comparedは『比較した』。何と比べたのかがわからず、文意が通らない",
                "encouragedは『励ました』。ケーキを励ますことはできない",
            ],
            "💡 deny＝（事実であることを）否定する。ask 人 if ...＝人に～かどうか尋ねる。had eatenは尋ねた時点より前のことを表す過去完了。",
        ),
        q(
            5,
            "The temperature was so low in the mountains that the water in the river started to ( 5 ).",
            "山の中は気温がとても低かったので、川の水が（5）始めました。",
            ["freeze", "sink", "praise", "cure"],
            ["凍る", "沈む", "ほめる", "（病気を）治す"],
            1,
            [
                "freezeは『凍る』。気温がとても低いという原因に合う結果",
                "sinkは『沈む』。川の水そのものが沈むとは言わず、気温の低さとも結びつかない",
                "praiseは『ほめる』。人や行いをほめる語で、水の状態の変化を表さない",
                "cureは『（病気を）治す』。水の変化を表す語ではない",
            ],
            "💡 so＋形容詞＋that ...＝とても～なので…。freeze（凍る）の過去形・過去分詞はfroze／frozen。",
        ),
        q(
            6,
            "A : Do you think the Jaguars will win today's baseball game against the Warriors, Dad?\nB : I'm not sure. The Warriors are a very strong team, so it will be a close game. It could go either way. But I hope the Jaguars ( 6 ) them.",
            "A：お父さん、ジャガーズは今日の野球の試合でウォリアーズに勝つと思う？\nB：わからないな。ウォリアーズはとても強いチームだから、接戦になるだろう。どちらが勝ってもおかしくない。でも、ジャガーズが彼らを（6）といいな。",
            ["sail", "beat", "cut", "measure"],
            ["航海する", "打ち負かす", "切る", "測る"],
            2,
            [
                "sailは『航海する』。野球の試合の勝敗を表さない",
                "beatは『（相手を）打ち負かす』。ジャガーズがウォリアーズ（them）に勝つことを願う文になり、Aの質問winにも対応する",
                "cutは『切る』。相手チームを目的語にしても、試合の勝敗の意味にならない",
                "measureは『測る』。試合の勝ち負けとは関係がない",
            ],
            "💡 beat＋相手＝相手を負かす。win the game（試合に勝つ）と目的語の違いに注意。It could go either way.＝どちらに転ぶかわからない。close game＝接戦。",
        ),
        q(
            7,
            "Many people moved to Greenwood after the ( 7 ) company built a station there. The train made it easy to travel to nearby cities.",
            "（7）会社がグリーンウッドに駅を作ってから、多くの人がそこへ引っ越してきました。電車のおかげで、近くの都市へ行きやすくなりました。",
            ["airport", "weight", "railroad", "salary"],
            ["空港", "重さ", "鉄道", "給料"],
            3,
            [
                "airportは『空港』。駅を作り、The trainと続く文脈に合わない",
                "weightは『重さ』。駅を建てる会社の種類にならない",
                "railroadは『鉄道』。駅を作り、2文目でThe trainと続くので鉄道会社とわかる",
                "salaryは『給料』。会社の種類を表さない",
            ],
            "💡 railroad company＝鉄道会社。make it easy to do＝～するのを簡単にする（itはto以下を指す形式目的語）。",
        ),
        q(
            8,
            "After the death of her cat, Nancy was very sad. Her parents tried to ( 8 ) her by giving her a new cat as a present.",
            "飼っていた猫が死んでしまい、ナンシーはとても悲しんでいました。両親は新しい猫をプレゼントして、彼女を（8）しようとしました。",
            ["comfort", "announce", "develop", "explore"],
            ["慰める", "発表する", "開発する・発達させる", "探検する"],
            1,
            [
                "comfortは『慰める』。悲しんでいるナンシーに新しい猫を贈る目的に合う",
                "announceは『発表する』。人を目的語にして、悲しみを和らげる意味にはならない",
                "developは『開発する・発達させる』。悲しんでいる人への行動として合わない",
                "exploreは『探検する』。herを目的語にすると文意が通らない",
            ],
            "💡 comfort＝慰める。by doing＝～することによって（手段）。as a present＝プレゼントとして。",
        ),
        q(
            9,
            "The new software for the company's computers is very easy to use. It does not ( 9 ) things like the old software did.",
            "会社のコンピューターの新しいソフトウェアは、とても使いやすいです。古いソフトウェアのように物事を（9）しません。",
            ["repair", "imagine", "complicate", "inspire"],
            ["修理する", "想像する", "複雑にする", "刺激を与える・やる気にさせる"],
            3,
            [
                "repairは『修理する』。使いやすさについての説明にならない",
                "imagineは『想像する』。ソフトウェアが主語では文意が通らない",
                "complicateは『複雑にする』。easy to useと対比して、古いソフトのように物事を複雑にしないと説明している",
                "inspireは『刺激を与える・やる気にさせる』。使いやすさとの関係がない",
            ],
            "💡 complicate＝複雑にする（形容詞はcomplicated）。like the old software did＝古いソフトウェアがそうしたように（didはcomplicated thingsの代わり）。",
        ),
        q(
            10,
            "The ( 10 ) has decided to build a new hospital in the city. This will make it easier for people to get medical treatment.",
            "（10）は市内に新しい病院を建てることを決めました。これで人々は治療を受けやすくなるでしょう。",
            ["technology", "health", "career", "government"],
            ["科学技術", "健康", "職業・経歴", "政府・行政機関"],
            4,
            [
                "technologyは『科学技術』。病院の建設を決める主体にならない",
                "healthは『健康』。決定を下す主語として不自然",
                "careerは『職業・経歴』。病院の建設を決める主体ではない",
                "governmentは『政府・行政機関』。has decided to build a new hospitalの主語として、病院の建設を決める組織に合う",
            ],
            "💡 decide to do＝～することに決める。make it easier for 人 to do＝人が～するのをより簡単にする。medical treatment＝治療。",
        ),
        q(
            11,
            "Travis always buys good quality clothes because he can wear them for several years. Even though such clothes are expensive, Travis believes that he saves money ( 11 ).",
            "トラビスは何年も着られるので、いつも質のよい服を買います。そのような服は値段が高いですが、（11）お金の節約になるとトラビスは考えています。",
            ["with an open mind", "at the last minute", "for a good laugh", "in the long run"],
            ["偏見を持たずに", "土壇場で・直前に", "大笑いするために", "長い目で見れば"],
            4,
            [
                "with an open mindは『偏見を持たずに』。お金を節約できる理由にならない",
                "at the last minuteは『土壇場で・直前に』。何年も着られるという長い期間の話と合わない",
                "for a good laughは『大笑いするために』。節約の話とは関係がない",
                "in the long runは『長い目で見れば』。高くても何年も着られるので、結局はお金の節約になるという流れに合う",
            ],
            "💡 in the long run＝長い目で見れば・結局は。even though＝～だけれども（譲歩）。such clothes＝そのような服（good quality clothesを指す）。",
        ),
        q(
            12,
            "A : Honey, I think you should ( 12 ) this old T-shirt. It has a hole in it.\nB : OK. I'll throw it away.",
            "A：ねえ、この古いTシャツは（12）方がいいと思うよ。穴が開いているもの。\nB：わかった。捨てるよ。",
            ["run out of", "get rid of", "play tricks on", "cut down on"],
            ["～を使い果たす", "～を処分する", "～にいたずらをする", "～（の量）を減らす"],
            2,
            [
                "run out ofは『～を使い果たす・切らす』。Tシャツを使い果たすとは言わない",
                "get rid ofは『～を処分する・取り除く』。BのI'll throw it away（捨てる）と内容が一致する",
                "play tricks onは『～にいたずらをする』。人に対して使う表現で、Tシャツには合わない",
                "cut down onは『～（の量）を減らす』。1枚のTシャツについて使う表現ではない",
            ],
            "💡 get rid of ～＝～を処分する・取り除く。throw ～ away＝～を捨てる（Bの返答がget rid ofの言い換えになっている）。",
        ),
        q(
            13,
            "Tammy is going to ( 13 ) today. It is a beautiful day, so she can put the clothes outside to dry.",
            "タミーは今日、（13）つもりです。よく晴れた日なので、服を外に干して乾かせます。",
            ["take a seat", "hold her breath", "lose her balance", "do the laundry"],
            ["席に着く", "息を止める", "バランスを崩す", "洗濯をする"],
            4,
            [
                "take a seatは『席に着く』。服を外に干す話につながらない",
                "hold her breathは『息を止める』。天気がよいことや服を乾かすことと関係がない",
                "lose her balanceは『バランスを崩す』。前もって予定として述べる内容ではない",
                "do the laundryは『洗濯をする』。晴れているので服を外に干して乾かせるという2文目に合う",
            ],
            "💡 do the laundry＝洗濯をする。put ～ outside to dry＝～を外に出して乾かす（to dryは目的を表す不定詞）。",
        ),
        q(
            14,
            "A : Is it going to rain tomorrow?\nB : The weather report said it would. However, it should ( 14 ) by the afternoon.",
            "A：明日は雨が降るのかな。\nB：天気予報では降ると言っていたよ。でも、午後までには（14）はずだよ。",
            ["clear up", "give up", "fill up", "show up"],
            ["（天気が）晴れる", "あきらめる", "いっぱいになる", "現れる"],
            1,
            [
                "clear upは『（天気が）晴れる』。雨の予報のあと、Howeverで午後には晴れると続く流れに合う",
                "give upは『あきらめる』。天気を表すitの動きとして不自然",
                "fill upは『いっぱいになる』。天気の変化を表さない",
                "show upは『現れる』。人が来ることなどに使い、天気が回復する意味にはならない",
            ],
            "💡 clear up＝（天気が）晴れる・回復する。said it would＝said it would rainの省略。should＝～するはずだ（見込み）。by＝～までに。",
        ),
        q(
            15,
            "The weather in the city is getting warmer ( 15 ). People there are looking forward to the start of spring.",
            "その市の天気は（15）暖かくなってきています。そこに住む人々は、春の始まりを楽しみにしています。",
            ["in common", "in secret", "at most", "day by day"],
            ["共通して", "ひそかに", "せいぜい・多くても", "日ごとに"],
            4,
            [
                "in commonは『共通して』。have ～ in commonの形で使い、天気の変化を表さない",
                "in secretは『ひそかに』。天気が暖かくなる様子には使わない",
                "at mostは『せいぜい・多くても』。数量の上限を表し、getting warmerの変化を説明できない",
                "day by dayは『日ごとに』。is getting warmer（だんだん暖かくなっている）という変化に合う",
            ],
            "💡 day by day＝日ごとに・日に日に。be getting＋比較級＝だんだん～になってきている。look forward to＋名詞＝～を楽しみに待つ。",
        ),
    ]


SHARED_TOUR_DIALOGUE = (
    "A : Hi. I'd like to take a guided tour of this city tomorrow. Do you have any suggestions?\n"
    "B : Sure. If you ( 19 ), I recommend the one in the morning. It will take you to the old temples and shrines in the city.\n"
    "A : Sounds interesting. What time does it start?\n"
    "B : It starts at 9:30 and ends at 12:30.\n"
    "A : That's too bad. I've ( 20 ).\n"
    "B : In that case, we have another tour that starts at 2:00 p.m. On this tour, you can visit a famous temple and try the tea ceremony.\n"
    "A : That would be wonderful. How much does it cost?\n"
    "B : It's fifty dollars per person, including a Japanese-style dinner."
)
SHARED_TOUR_TRANSLATION = (
    "A：こんにちは。明日、この市のガイド付きツアーに参加したいのですが、何かおすすめはありますか。\n"
    "B：はい。（19）なら、午前中のツアーをおすすめします。市内の古いお寺や神社に連れて行ってくれます。\n"
    "A：おもしろそうですね。何時に始まりますか。\n"
    "B：9時30分に始まり、12時30分に終わります。\n"
    "A：それは残念です。（20）。\n"
    "B：それでしたら、午後2時に始まる別のツアーがあります。このツアーでは有名なお寺を訪れ、茶道を体験できます。\n"
    "A：それはすばらしいですね。料金はいくらですか。\n"
    "B：和食の夕食付きで、お一人様50ドルです。"
)


def build_part2(h) -> list[dict]:
    q = h.question
    return [
        q(
            16,
            "A : Did you come to our party last night?\nB : Yes, I did. But I had to leave early to go to a dance practice.\nA : I see. That's ( 16 ). Are you in a club activity?\nB : Yes. We are going to perform at the school festival next week.",
            "A：昨夜は私たちのパーティーに来た？\nB：うん、行ったよ。でも、ダンスの練習に行くために早く帰らなければならなかったんだ。\nA：なるほど。（16）。部活をしているの？\nB：うん。来週、学園祭で発表するんだ。",
            [
                "why I'm not good at dancing",
                "why I didn't see you there",
                "not what I want to know",
                "because you came early",
            ],
            [
                "（それが）私がダンスが得意ではない理由",
                "（それで）会場であなたを見かけなかった",
                "私が知りたいことではない",
                "あなたが早く来たから",
            ],
            2,
            [
                "Bが早く帰ったことは、Aがダンスを得意でない理由にはならない",
                "会場であなたを見かけなかった理由。Bがパーティーを早く帰ったと聞き、会場で会わなかったわけがわかったという流れ",
                "AはI seeと事情を受け入れており、知りたいことではないと突き放す理由がない",
                "Bは早く来たのではなく、早く帰った（leave early）ので内容が逆",
            ],
            "💡 That's why ～＝それが～の理由だ・だから～なのだ。leave early＝早く帰る。perform＝演じる・発表する。",
        ),
        q(
            17,
            "A : This is the front desk. What can I do for you?\nB : Hi. This is Ashley Smith in Room 101. Can I ( 17 ), please? I want to dry my hair but only have wet ones in my room.\nA : Certainly, ma'am. We'll bring you a fresh one in about five minutes.\nB : Thank you very much.",
            "A：フロントでございます。ご用件をお伺いします。\nB：こんにちは。101号室のアシュリー・スミスです。（17）ことはできますか。髪を乾かしたいのですが、部屋には濡れたものしかないのです。\nA：かしこまりました。5分ほどで新しいものをお持ちします。\nB：どうもありがとうございます。",
            [
                "get an extra towel",
                "order room service",
                "clean the bathroom",
                "fix a hair dryer",
            ],
            [
                "タオルをもう1枚もらう",
                "ルームサービスを注文する",
                "浴室を掃除する",
                "ヘアドライヤーを修理する",
            ],
            1,
            [
                "タオルをもう1枚もらう。wet ones（濡れたもの）とa fresh one（新しいもの）のones／oneがtowelを指しているとわかる",
                "ルームサービスでは、髪を乾かしたいのに濡れたものしかないという説明につながらない",
                "浴室の掃除は、髪を乾かしたいという用件と結びつかない",
                "ドライヤーの修理なら、濡れたものしかない（only have wet ones）という説明と合わず、新しいものを届けるという返答にもつながらない",
            ],
            "💡 ones／oneは前に出た名詞の繰り返しを避ける代名詞。wet ones＝濡れたタオル、a fresh one＝新しいタオル。extra＝追加の。",
        ),
        q(
            18,
            "A : Good morning, honey. What's for breakfast today?\nB : I wanted to make some omelets, but ( 18 ).\nA : That's strange. We bought some at the supermarket yesterday.\nB : I know. Wait, I might have left them in the car. I'll go to the garage and see if I can find them.",
            "A：おはよう。今日の朝ごはんは何？\nB：オムレツを作りたかったんだけど、（18）。\nA：それは変だね。昨日スーパーで買ったよ。\nB：そうだよね。待って、車の中に置いたままかもしれない。ガレージに行って、見つかるか見てくるね。",
            [
                "I dropped the eggs and broke them all",
                "I ate all of the eggs last week",
                "I can't find any eggs in the fridge",
                "I'm not good at cooking eggs",
            ],
            [
                "卵を落として全部割ってしまった",
                "先週、卵を全部食べてしまった",
                "冷蔵庫に卵が見つからない",
                "卵料理が得意ではない",
            ],
            3,
            [
                "全部割ってしまったのなら、車の中を探しに行く流れにならない",
                "先週食べてしまっても、昨日買った卵は残っているはずで、車の中を探しに行く理由にならない",
                "冷蔵庫に卵が見つからない。Aが昨日買ったと言い、Bが車に置いたままかもしれないと探しに行くので、卵が見当たらない状況とわかる",
                "料理が苦手だという話なら、卵を探しに行く必要はない",
            ],
            "💡 might have＋過去分詞＝～したかもしれない（過去についての推量）。see if ...＝～かどうか確かめる。some／themはeggsを指す。",
        ),
        q(
            19,
            SHARED_TOUR_DIALOGUE,
            SHARED_TOUR_TRANSLATION,
            [
                "want to learn about the history",
                "want to try some traditional food",
                "don't want to walk around outside",
                "don't want to get up early",
            ],
            [
                "歴史について学びたい",
                "伝統的な料理を食べてみたい",
                "外を歩き回りたくない",
                "早起きしたくない",
            ],
            1,
            [
                "歴史について学びたい。午前のツアーは古いお寺や神社を回るので、歴史に関心がある人に勧める理由になる",
                "伝統料理を食べたいなら、和食の夕食が付く午後のツアーの方が合う",
                "お寺や神社を回るツアーなので、外を歩きたくない人に勧める理由にならない",
                "早起きしたくない人に、9時30分に始まる午前のツアーを勧めるのは不自然",
            ],
            "💡 If you＋現在形, I recommend ～＝もし～なら、～をおすすめします。the one＝the tour。temples and shrines＝寺と神社。",
        ),
        q(
            20,
            SHARED_TOUR_DIALOGUE,
            SHARED_TOUR_TRANSLATION,
            [
                "never seen such a beautiful building",
                "already decided which tour to take",
                "been looking for a good place to stay",
                "made a reservation for lunch at noon",
            ],
            [
                "こんなに美しい建物を見たことがない",
                "どのツアーに参加するかもう決めた",
                "泊まるのによい場所を探している",
                "正午に昼食の予約をした",
            ],
            4,
            [
                "That's too bad.（それは残念）の理由にならず、別の時間のツアーを勧められる流れにもならない",
                "参加するツアーをもう決めているなら、Bが別のツアーを紹介する流れにならない",
                "泊まる場所を探していることは、午前のツアーに参加できない理由にならない",
                "正午に昼食の予約をした。ツアーが12時30分まで続くので参加できず、Bが午後のツアーを勧める流れに合う",
            ],
            "💡 I've made a reservation＝予約をしてある（現在完了）。In that case＝それなら。including ～＝～を含めて。",
        ),
    ]

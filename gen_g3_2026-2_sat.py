# -*- coding: utf-8 -*-
"""Grade 3 Saturday 2026-2; visually verified booklet pp. 2-11, official key."""
import importlib.util
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parent
OUT=ROOT/"data/grade3/2026-2-sat/data.json"

def module(suffix):
    spec=importlib.util.spec_from_file_location(suffix,ROOT/f"gen_g3_2026-2_sat_{suffix}.py")
    result=importlib.util.module_from_spec(spec);spec.loader.exec_module(result)
    return result

# Original question/options, translations, normal/easy grammar and
# option-specific explanations. The existing Grade 3 format has no question TTS.
ROWS=[
    ("A: I don't know much about baseball. Can you (　) the rules to me?\nB: Sure. It's easy.",
     "A：野球についてあまり知りません。ルールを私に (　) くれますか。\nB：もちろん。簡単ですよ。",
     ["sell","save","happen","explain"],["売る","救う・保存する","起こる","説明する"],4,
     "explain 内容 to 人で『人に内容を説明する』。野球をあまり知らないので、ルールの説明を頼んでいる。Can you＋原形は依頼。happen は出来事が起きる動詞で、the rules を目的語には取れない。",
     "やきゅうのルールがわからないから、おしえてほしいんだね。explain the rules to me は『わたしにルールをせつめいして』。to me は『わたしに』だよ。",
     ["ルールを売ってほしい場面ではない。","ルールを救う・保存する話ではない。","出来事が起こるという動詞で、ルールを説明できない。","知らないルールを説明するよう依頼している。"],
     ["ルールをうるのではないよ。","ルールをたすけることではないよ。","できごとがおこる、ではないよ。","ルールをせつめいしてもらうんだね。"]),
    ("Ms. Tanaka took the (　) and went to the third floor of the building.",
     "田中さんは (　) に乗り、建物の3階へ行きました。",
     ["lake","door","cousin","elevator"],["湖","ドア","いとこ","エレベーター"],4,
     "建物の3階へ移動するため、take the elevator（エレベーターに乗る）を使う。took は take の過去形で、went と同じく過去の行動。the third floor は『3階』で、移動手段が手がかり。",
     "たてものの3かいへいくために、エレベーターにのったよ。took the elevator は『エレベーターにのった』。took は take のむかしの形だね。",
     ["湖には乗って建物の3階へ移動できない。","ドアは入口で、階を移動する乗り物ではない。","いとこは人で、階を移動する手段ではない。","3階へ上がる移動手段に合う。"],
     ["みずうみにのって3かいにはいけないよ。","ドアは、かいをいどうするのりものではないよ。","いとこは、のりものではないね。","エレベーターで3かいへいくんだね。"]),
    ("A: How many birds are in that tree?\nB: I don't know. It's difficult to (　) them.",
     "A：あの木には何羽の鳥がいますか。\nB：分かりません。それらを (　) のは難しいです。",
     ["cost","prepare","call","count"],["費用がかかる","準備する","呼ぶ","数える"],4,
     "How many は数を尋ねる。鳥の数が分からないので count them（それらを数える）。It's difficult to＋原形で『～するのは難しい』。them は複数の birds を指す。",
     "とりがなんわいるか、かぞえるのはむずかしいんだね。count は『かぞえる』。them は、きにいるとりたちのことだよ。",
     ["費用の話ではなく、鳥の数を聞いている。","鳥を準備することでは、何羽か分からない。","呼ぶことではなく、数を知るための行動が必要。","How many の答えを得るため、鳥を数える。"],
     ["おかねがかかることではないよ。","とりをじゅんびするのではないよ。","とりをよぶことではないよ。","とりのかずを、かぞえるんだね。"]),
    ("Yuki studies English hard to (　) with his friends in Canada.",
     "ユウキはカナダの友達と (　) ために、英語を熱心に勉強しています。",
     ["cross","hold","communicate","shut"],["横切る","持つ・開催する","意思を伝え合う","閉める"],3,
     "communicate with 人は『人と意思を伝え合う』。英語を勉強する目的を to＋原形で表す。with his friends に合う動詞を選び、友達と英語でやり取りするという意味にする。",
     "カナダのともだちと、おはなしするためにえいごをべんきょうしているよ。communicate with は『～とやりとりする』。to のあとは、もとの形だね。",
     ["横切ることは、英語を学んで友達とやり取りする目的ではない。","持つ・開催するでは with his friends に合わない。","友達と英語で意思を伝え合う目的に合う。","閉めることは、友達とのやり取りではない。"],
     ["みちなどをよこぎることではないよ。","もつことでは、はなしがつながらないよ。","ともだちとやりとりするためだね。","ドアなどをしめることではないよ。"]),
    ("My brother loves old comic books, so he started to (　) them last year.",
     "兄（弟）は古いマンガが大好きなので、去年それらを (　) 始めました。",
     ["collect","click","cross","complain"],["集める","クリックする","横切る","不平を言う"],1,
     "古いマンガが好きなので collect them（それらを集める）が自然。started to＋原形は『～し始めた』。them は old comic books、so は前の好みから行動へのつながりを表す。",
     "ふるいマンガがすきだから、あつめはじめたんだね。collect は『あつめる』。started to collect で『あつめはじめた』になるよ。",
     ["好きな古いマンガを集め始めたという流れ。","紙のマンガを集める場面で、クリックではない。","マンガを横切るという意味にはならない。","complain them では不平を言う形にならず、好みの文脈にも合わない。"],
     ["すきなマンガをあつめるんだね。","クリックするおはなしではないよ。","マンガをよこぎるのではないよ。","もんくをいうおはなしではないよ。"]),
    ("Greg left the house (　) his umbrella, so he got wet in the evening when it started to rain.",
     "グレッグは傘を (　) 家を出たので、夕方、雨が降り始めたときにぬれました。",
     ["since","until","beside","without"],["～以来・～なので","～まで","～のそばに","～なしで・持たずに"],4,
     "雨でぬれた理由は、傘を持たずに家を出たこと。without＋名詞は『～なしで』。so が原因と結果をつなぎ、when it started to rain がぬれた時期を示す。beside は横の位置で、傘がないことではない。",
     "かさをもたずにでかけたので、あめでぬれたよ。without his umbrella は『かさをもたないで』。so のあとに、そのけっかがつづくね。",
     ["since は時期・理由の表現で、傘を持たないことを示さない。","until は期限で、傘がない状態を表せない。","傘のそばという場所では、ぬれた理由にならない。","傘なしで出かけたことが、ぬれた理由。"],
     ["いつから、というおはなしではないよ。","いつまで、ということではないよ。","かさのよこ、というばしょではないよ。","かさをもたなかったから、ぬれたんだね。"]),
    ("A: Mr. Taylor, I don't want to sing the song in front of everyone.\nB: Come on, Jack. Don't be so (　). You can do it.",
     "A：テイラー先生、みんなの前でその歌を歌いたくありません。\nB：さあ、ジャック。そんなに (　) ならないで。君ならできます。",
     ["shy","first","round","enough"],["恥ずかしがりの","最初の","丸い","十分な"],1,
     "人前で歌いたくないジャックを励ますので shy（恥ずかしがりの）。Don't be so shy は『そんなに恥ずかしがらないで』。so はここでは程度『そんなに』。You can do it が励ましの文脈を示す。",
     "みんなのまえでうたうのが、はずかしいんだね。shy は『はずかしがり』。『そんなにはずかしがらないで、できるよ』とはげましているよ。",
     ["人前で歌うのをためらう気持ちに合う。","最初かどうかを注意している場面ではない。","丸いという形は、人前で歌う気持ちに合わない。","十分という意味では、励ます文にならない。"],
     ["はずかしがっているきもちだね。","いちばんさいしょ、ということではないよ。","まるいかたちのことではないよ。","じゅうぶん、というおはなしではないよ。"]),
    ("The movie theater was (　) small that there were only twenty seats.",
     "その映画館は (　) 小さかったので、座席が20席しかありませんでした。",
     ["very","so","too","almost"],["とても","とても～なので（so ... that）","～すぎる","ほとんど"],2,
     "so＋形容詞＋that＋文は『とても～なので…』。small の後ろに that there were ... が続くので so。very small 自体は正しいが、very ... that という構文は作れない。too は通常 too ... to と組み合わせる。",
     "『とても小さいので、20せきしかない』という文。so small that をセットでつなぐよ。that のあとに、小さいためにおきたことがつづくね。",
     ["very small は言えるが、that 節につなぐこの構文には使わない。","so small that で、小ささと座席の少なさをつなぐ。","too small to ... の形とは違い、ここは that 節。","almost はほとんどで、結果を表す that 節をつなげない。"],
     ["very のあとに、この that はつなげないよ。","so small that のセットだね。","too のセットは、ここではあわないよ。","ほとんど、といういみではつながらないよ。"]),
    ("A: How do you stay so young, Mike?\nB: Well, I like to (　) a walk every morning. I also go to the gym three times a week.",
     "A：マイク、どうやってそんなに若さを保っているのですか。\nB：ええ、毎朝 (　) のが好きです。週に3回ジムにも行きます。",
     ["miss","pass","jump","take"],["逃す・恋しく思う","通る・渡す","跳ぶ","散歩する（take a walk）"],4,
     "take a walk は『散歩する』。若さを保つ方法として、散歩とジムでの運動を挙げている。like to＋原形なので take。a walk の前に置く動詞は、まとまりで覚える。",
     "まいあささんぽをするのが、わかさのひけつだね。take a walk は『さんぽする』のセット。ジムでも、しゅうに3かいうんどうしているよ。",
     ["散歩を逃すことでは、健康のための習慣にならない。","pass a walk は散歩する定型表現ではない。","jump a walk は散歩を表す組合せではない。","take a walk が毎朝の散歩を表す。"],
     ["さんぽをのがすおはなしではないよ。","pass a walk とはいわないよ。","とびはねることではないよ。","take a walk で『さんぽする』だね。"]),
    ("A: Did you walk all the (　) to school today?\nB: No, my mom drove me.",
     "A：今日は学校まで (　) 歩いて行ったのですか。\nB：いいえ、母が車で送ってくれました。",
     ["way","side","course","part"],["道のり（all the wayでずっと）","側・横","コース・課程","部分"],1,
     "all the way to＋場所は『～までずっと』。学校までの全行程を歩いたかを尋ね、母が車で送ったと答えている。way を含む定型表現を使う。drove は drive の過去形。",
     "がっこうまで、ずっとあるいたかきいているよ。all the way to school は『がっこうまでずっと』。おかあさんのくるまでいった、とこたえているね。",
     ["all the way to school が学校までの全行程を表す。","all the side は、ずっと学校までという表現にならない。","all the course to はこの移動の定型表現ではない。","part は部分で、学校までずっととは言えない。"],
     ["がっこうまでずっと、というセットだね。","よこ、ということではないよ。","コースということではないよ。","いちぶではなく、ずっとのことだよ。"]),
    ("A: How did you and Chris meet?\nB: We grew up together in Canada. (　) fact, we met over 30 years ago.",
     "A：あなたとクリスはどのように知り合ったのですか。\nB：カナダで一緒に育ちました。(　)、30年以上前に知り合ったのです。",
     ["To","After","In","Near"],["～へ","～の後に","実は（In fact）","～の近くに"],3,
     "In fact は『実は・実際には』。一緒に育ったことを述べ、知り合ったのが30年以上前だと詳しく補足する。文頭なので In と大文字にする。fact と組む前置詞をセットで覚える。",
     "『じつは、30ねんよりもっとまえにあった』とくわしくいっているよ。In fact は『じつは』のセット。さいしょにくるので In の I はおおもじだね。",
     ["To fact は実はという決まり文句にならない。","After fact では、説明を補足する意味にならない。","In fact で実際の事情を詳しく補足する。","Near fact は、実はという表現ではない。"],
     ["To fact というセットではないよ。","あとで、ということではないよ。","In fact で『じつは』だね。","ちかく、というばしょではないよ。"]),
    ("The girl was surprised when she saw her birthday cake. It was (　) with chocolate and strawberries.",
     "少女は誕生日のケーキを見て驚きました。それはチョコレートとイチゴで (　) いました。",
     ["covered","jumped","got","sounded"],["覆われた（coverの過去分詞）","跳んだ","得た","～に聞こえた"],1,
     "be covered with＋物は『～で覆われている』。ケーキがチョコレートとイチゴで飾られた状態なので was covered with。was＋過去分詞は受動態。単に動詞の過去形を was の後ろに置くのではない。",
     "ケーキが、チョコレートとイチゴでおおわれていたんだね。was covered with は『～でおおわれていた』。ケーキがじぶんでとぶのではないよ。",
     ["was covered with でケーキが覆われた状態を表す。","ケーキが跳ぶ内容ではなく、was jumped もこの意味に合わない。","was got with では、材料で覆われた意味にならない。","sounded は音・印象で、ケーキの表面を説明できない。"],
     ["チョコとイチゴでおおわれているね。","ケーキがとぶのではないよ。","なにかをもらうおはなしではないよ。","おとがきこえることではないよ。"]),
    ("A: Why weren't you in the gym when volleyball practice started?\nB: I'm sorry. I was (　) to my teacher.",
     "A：バレーボールの練習が始まったとき、なぜ体育館にいなかったのですか。\nB：すみません。先生と (　)。",
     ["talk","talks","talked","talking"],["話す（原形）","話す（三人称単数形）","話した（過去形）","話している（ing形）"],4,
     "was＋動詞のing形は過去進行形『～していた』。練習が始まったときに先生と話していたので was talking to my teacher。was の後ろに原形 talk や過去形 talked は置かない。",
     "れんしゅうがはじまったとき、せんせいとはなしていたんだね。was talking は『はなしていた』。was のあとに、ing の形をつけよう。",
     ["was の後ろに原形 talk だけでは過去進行形を作れない。","talks は三人称単数現在形で、was の後ろに合わない。","was talked では先生と話していたという過去進行形にならない。","was talking でその時に続いていた会話を表す。"],
     ["was のあとは、ing の形がひつようだよ。","talks では、はなしていたにならないよ。","talked では、このセットにならないよ。","was talking で『はなしていた』だね。"]),
    ("Ken can run (　) than his sister. She's very slow.","ケンは姉（妹）より (　) 走れます。彼女はとても遅いです。",
     ["fast","faster","fastest","too fast"],["速く","より速く","最も速く","速すぎる"],2,
     "than his sister が比較の相手を示すので、fast の比較級 faster。faster than は『～より速く』。fastest は最上級で、2人の走る速さを than で比べる形とは違う。can の後ろは原形 run。",
     "おねえさん・いもうとより、はやくはしれるんだね。『～よりはやく』は faster than。than がみえたら、くらべる形をたしかめよう。",
     ["than を伴う比較には原級 fast ではなく比較級を使う。","faster than で姉（妹）より速いと表す。","fastest は最も速くで、ここで than とつながらない。","too fast は速すぎるで、比較級ではない。"],
     ["くらべるので、fast のままではないよ。","faster than で『～よりはやく』だね。","いちばんはやい、という形ではないよ。","はやすぎる、ではくらべる形にならないよ。"]),
    ("My brother got a letter (　) in French yesterday. It was from his pen pal in Paris.",
     "兄（弟）は昨日、フランス語で (　) 手紙を受け取りました。パリの文通相手からでした。",
     ["write","wrote","written","writing"],["書く（原形）","書いた（過去形）","書かれた（過去分詞）","書いている（ing形）"],3,
     "a letter written in French は『フランス語で書かれた手紙』。written は write の過去分詞で、後ろから letter を説明する。手紙は書く側でなく書かれた物。主文の動詞 got はすでにあり、wrote を追加しない。",
     "てがみは、フランスごで『かかれた』ものだね。written in French が、どんなてがみかをあとからせつめいするよ。てがみがじぶんでかくのではないね。",
     ["原形 write では、書かれた手紙と後ろから説明できない。","過去形 wrote を追加しても letter を修飾する形にならない。","過去分詞 written が、書かれた手紙を表す。","writing は書いている側の意味になり、手紙に合わない。"],
     ["かかれた、の形がひつようだよ。","wrote は、このあとからのせつめいにはつかわないよ。","written で『かかれたてがみ』だね。","てがみが、じぶんでかいているのではないよ。"]),
    ("Customer: Hello. Are there still tickets for tonight's baseball game?\nClerk: I'm sorry. (　) We still have some for tomorrow's game.\nCustomer: OK. I'll buy two of those.",
     "客：こんにちは。今夜の野球の試合のチケットはまだありますか。\n店員：申し訳ありません。(　) 明日の試合のものならまだあります。\n客：分かりました。それを2枚買います。",
     ["It's a big stadium.","I'm a stranger here.","They're sold out.","I'm glad to hear that."],
     ["大きな競技場です。","私はこの辺りに不案内です。","売り切れです。","それを聞いてうれしいです。"],3,
     "I'm sorry. の後、明日の券ならあると代案を示すので、今夜の券は They're sold out（売り切れ）。They は今夜の tickets、those は明日の券を指す。some は tickets を省いた表現。",
     "こんやのチケットはうりきれで、あしたのチケットならあるよ。They're sold out. は『うりきれです』。おきゃくさんは、あしたのものを2まいかうんだね。",
     ["競技場の大きさは、チケットが残っているかに答えない。","道に不案内という話は、券の有無と無関係。","今夜は売り切れなので、明日の券を案内している。","喜ぶ理由がなく、謝罪と明日の券の案内につながらない。"],
     ["たてもののおおきさではないよ。","みちがわからないことではないよ。","こんやのものは、うりきれなんだね。","うれしい、というこたえではつながらないよ。"]),
    ("Husband: What are you cooking?\nWife: Beef stew. Do you want to try some?\nHusband: Sure. (　)",
     "夫：何を料理しているのですか。\n妻：ビーフシチューです。少し食べてみますか。\n夫：ええ。(　)",
     ["You'll be all right.","Not at all.","It smells great.","I'll be ready to go."],
     ["あなたは大丈夫でしょう。","どういたしまして・全くそんなことはありません。","とてもよい匂いがします。","出かける準備ができます。"],3,
     "シチューを試食したいと Sure と答え、料理のよい匂いを It smells great と述べる。smell＋形容詞は『～な匂いがする』。匂いの段階なので tastes とは区別する。出発や体調を話している場面ではない。",
     "シチューをたべてみたい、とこたえているよ。It smells great. は『とてもいいにおい』。おりょうりのにおいをほめているんだね。",
     ["大丈夫という励ましは、試食を勧める場面に合わない。","お礼への返答などで、Sure の後の料理の感想に合わない。","よい匂いだと料理への関心を示している。","出かける準備は、料理の試食とつながらない。"],
     ["だいじょうぶ、とげんきづけることではないよ。","おれいをいわれたのではないよ。","いいにおいのシチューだね。","でかけるじゅんびではないよ。"]),
    ("Teacher: Mark, would you like to take part in the speech contest?\nStudent: Yes. (　) but I'll try my best.",
     "先生：マーク、スピーチ大会に参加しませんか。\n生徒：はい。(　) でも、全力を尽くします。",
     ["It'll be my first time,","It's your turn to go,","I'd like a piece,","I have another idea,"],
     ["初めてになります、","あなたが行く番です、","一切れ欲しいです、","別の考えがあります、"],1,
     "but I'll try my best が『不慣れでも頑張る』という対比を作るので It'll be my first time。take part in は『参加する』。選択肢末尾のコンマの後に but が続き、一つの文としてつながる。",
     "スピーチたいかいは、はじめて。でもがんばるよ、というつながりだね。my first time は『じぶんにとってはじめて』。but は『でも』だよ。",
     ["初参加という不安と、頑張る決意を but でつなぐ。","先生が行く番という話では、生徒の決意につながらない。","一切れは食べ物の量で、大会への参加に合わない。","別の考えの内容がなく、初参加でも努力する流れに合わない。"],
     ["はじめてだけど、がんばるんだね。","せんせいのばん、ということではないよ。","たべものをひときれ、ではないよ。","べつのかんがえをいうばめんではないよ。"]),
    ("Mother: How is the egg sandwich, Ethan?\nSon: (　) Can you make me one tomorrow, too?\nMother: Of course.",
     "母：イーサン、卵サンドイッチはどうですか。\n息子：(　) 明日も一つ作ってくれますか。\n母：もちろん。",
     ["It was my first time.","It tastes really good.","I will go there.","I often buy it there."],
     ["初めてでした。","本当においしいです。","そこへ行きます。","よくそこで買います。"],2,
     "How is the egg sandwich? は味の感想を求める。明日も母に作ってほしいので It tastes really good（本当においしい）。taste＋形容詞は『～の味がする』。one は同じ種類のサンドイッチ一つを指す。",
     "サンドイッチがおいしいから、あしたもつくってほしいんだね。It tastes really good. は『とてもおいしい』。one は、サンドイッチをもうひとつということだよ。",
     ["初めてという話だけでは、味の質問や再度のお願いに答えない。","味をほめ、明日も作ってほしいと頼む流れ。","行く場所を尋ねている会話ではない。","店で買う話ではなく、母に作ってもらっている。"],
     ["はじめてかどうかではなく、あじをきいているよ。","おいしいから、あしたもほしいんだね。","どこかへいくことではないよ。","おみせでかうおはなしではないよ。"]),
    ("Son: Oh no! I got some ketchup on my T-shirt.\nMother: You can't go to school like that. (　)\nSon: All right, Mom.",
     "息子：ああ、Tシャツにケチャップを付けてしまいました。\n母：そのままでは学校へ行けません。(　)\n息子：分かりました、お母さん。",
     ["Put on a clean one.","Take your bag.","The school bus is coming.","Wash the dishes."],
     ["きれいなものに着替えなさい。","かばんを持ちなさい。","スクールバスが来ています。","皿を洗いなさい。"],1,
     "ケチャップで汚れたTシャツでは登校できないので、Put on a clean one と清潔なTシャツを着るよう指示する。put on は『着る』、one は T-shirt の代わり。All right が指示を引き受ける返答。",
     "Tシャツがよごれたので、きれいなものにきがえるよ。Put on は『きる』。a clean one の one は、きれいなTシャツのことだね。",
     ["汚れた服をきれいな服に替えるよう指示している。","かばんを持っても、服の汚れは解決しない。","バスの到着では、汚れた服の問題は解決しない。","汚れたのは服で、皿を洗う理由はない。"],
     ["きれいなTシャツにきがえるんだね。","かばんをもっても、ふくはきれいにならないよ。","バスがきても、ふくのよごれはのこるね。","おさらがよごれたのではないよ。"]),
]

WRITING={
    "section4":dict(type="email-reply",title="ライティング（Eメール）",prompt={},
                    sampleAnswer="My class starts at six in the evening. I am learning to play the guitar there. I enjoy playing music with other students."),
    "section5":dict(type="composition",title="ライティング（英作文）",question="What do you usually do before going to bed?",
                    sampleAnswer="I usually drink hot milk before going to bed. First, I can sleep better after I drink it. Second, it is fun for me to talk with my family while drinking it every night.")
}
WRITING["section4"]["prompt"]={"from":"James","body":"Hi,\nThank you for your e-mail.\nI hear that you are learning to play an instrument at a music school. I have some questions for you. What time does your class start? What instrument do you learn to play there?\nYour friend,\nJames"}

def build():
    p,m=module("passages"),module("materials")
    qs=[]
    for n,(text,ja,choices,meanings,answer,grammar,simple,reasons,easy) in enumerate(ROWS,1):
        qs.append(dict(number=n,text=text,translation=ja,choices=choices,choiceTranslations=meanings,
                       answer=answer,grammar=grammar,grammarSimple=simple,
                       choiceAnalysis=[("○ " if i==answer else "")+f"{c}＝{t}。{why}" for i,(c,t,why) in enumerate(zip(choices,meanings,reasons),1)],
                       choiceAnalysisSimple=[("○ " if i==answer else "")+f"{t}。{why}" for i,(t,why) in enumerate(zip(meanings,easy),1)]))
    sections=[
        dict(name="大問1",nameEn="Part 1",type="vocabulary",instruction="次の(1)から(15)までの(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選び，その番号のマーク欄をぬりつぶしなさい。",questions=qs[:15]),
        dict(name="大問2",nameEn="Part 2",type="vocabulary",instruction="次の(16)から(20)までの会話について，(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選び，その番号のマーク欄をぬりつぶしなさい。",questions=qs[15:]),
        dict(name="大問3",nameEn="Part 3",type="reading-comprehension",instruction="次の掲示・Eメール・英文を読み、それぞれの問いに答えなさい。",passages=p.passages()),
    ]
    listening=[1,1,1,2,1,2,2,2,3,2,1,1,1,4,1,2,4,1,2,2,3,1,2,3,1,4,1,1,4,2]
    return dict(grade="grade3",year="2026",session="2026-2-sat",exam="2026-2-sat",title="英検3級 2026年度 第2回（土曜準会場）",
                sections=sections,writing=WRITING,listening={f"part{i+1}":dict(zip(map(str,range(i*10+1,i*10+11)),listening[i*10:i*10+10])) for i in range(3)},
                vocabulary=m.vocabulary(),lessonPlan=m.lessonplan(sections))

if __name__=="__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(build(),ensure_ascii=False,indent=4)+"\n",encoding="utf-8")
    print(OUT)

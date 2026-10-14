# -*- coding: utf-8 -*-
"""Reproduce Grade 4 2025-2 Saturday; booklet pp. 2-11, text layer + page images."""
import importlib.util
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "data/grade4/2025-2-sat/data.json"


def module(suffix):
    spec=importlib.util.spec_from_file_location(suffix,ROOT/f"gen_g4_2025-2_sat_{suffix}.py")
    result=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


# stem, translation, choices, meanings, answer, normal/simple grammar,
# choice-specific reasons. All four normal/simple analyses retain meanings.
ROWS = [
    ("Yesterday, Hiroko got a (　) from her uncle. It was a new bike.",
     "昨日、ヒロコはおじから (　) をもらいました。それは新しい自転車でした。",
     ["guest","gift","road","rule"],["客","贈り物・プレゼント","道路","規則"],2,
     "got a ... from her uncle（おじから～をもらった）と、次の It was a new bike.（それは新しい自転車だった）がヒント。おじからもらった物が自転車なので gift（贈り物）。guest は人で、road や rule は人からもらう物ではない。",
     "おじさんから、あたらしいじてんしゃをもらったよ。gift は『おくりもの・プレゼント』。じてんしゃのプレゼントだね。",
     ["招かれた客で、おじからもらう物ではない。","新しい自転車という贈り物を受け取った。","道路は人からもらう物ではない。","規則はもらう物ではなく、自転車ともつながらない。"],
     ["おきゃくさんをもらうのではないよ。","じてんしゃのプレゼントをもらったね。","みちをもらうことはできないよ。","きまりのことではないよ。"]),
    ("Lisa works on a (　). She likes to grow vegetables and plants.",
     "リサは (　) で働いています。彼女は野菜や植物を育てるのが好きです。",
     ["coin","farm","scarf","cousin"],["硬貨","農場","スカーフ・マフラー","いとこ"],2,
     "works on a ...（～で働いている）の後ろには働く場所が入る。2文目の『野菜や植物を育てるのが好き』から farm（農場）。work on a farm で『農場で働く』。硬貨・スカーフ・いとこは働く場所ではない。",
     "やさいやしょくぶつをそだてるのがすきなリサ。はたらくばしょは farm『のうじょう』だね。",
     ["硬貨は働く場所ではない。","野菜や植物を育てる場所として農場が合う。","身に着ける物で、働く場所ではない。","人を表す語で、働く場所ではない。"],
     ["おかねのコインでは、はたらけないよ。","のうじょうで、やさいをそだてるんだね。","まくものでは、はたらくばしょにならないよ。","いとこは、ひとのことだよ。"]),
    ("Scott loves to travel. He often stays at a (　) when he visits another city.",
     "スコットは旅行が大好きです。彼は別の都市を訪れるとき、よく (　) に泊まります。",
     ["hobby","hotel","season","ticket"],["趣味","ホテル","季節","切符・チケット"],2,
     "stays at（～に泊まる）の後ろには泊まる場所が必要。旅行で別の都市を訪れたときに泊まるのは hotel。hobby（趣味）や season（季節）は場所ではなく、ticket（切符）には泊まれない。",
     "りょこうがすきなスコット。ほかのまちでとまるのは hotel『ホテル』だね。stay at は『～にとまる』だよ。",
     ["趣味は泊まる場所ではない。","旅先で泊まる場所として自然。","季節は時期で、泊まる場所ではない。","切符には泊まれない。"],
     ["しゅみには、とまれないよ。","ホテルにとまるんだね。","きせつは、ばしょではないよ。","チケットには、とまれないよ。"]),
    ("A: Why do you always get up (　) on weekends, Dad?\nB: I go fishing at the lake with my friends.",
     "A：お父さん、どうして週末はいつも (　) 起きるのですか。\nB：友だちと湖へ釣りに行くからです。",
     ["again","same","soon","early"],["もう一度","同じ","すぐに","早く"],4,
     "get up early で『早く起きる』。週末ごとに友だちと湖へ釣りに行くことが、早起きの理由になる。again（もう一度）や soon（すぐに）では釣りに行く理由とつながらず、same（同じ）は起きる様子を表さない。",
     "しゅうまつに、みずうみへつりにいくから、はやくおきるんだね。get up early は『はやくおきる』だよ。",
     ["もう一度起きる、では釣りに行く理由と合わない。","『同じ』では起きる様子を表せない。","すぐに起きる、では週末の習慣の理由にならない。","釣りに行くために、週末は早く起きている。"],
     ["もういちど、ではないよ。","おなじ、ではいみがつながらないよ。","すぐに、ではないよ。","はやくおきるんだね。"]),
    ("Mariko is going to make cookies, so she needs to buy some (　) this afternoon.",
     "マリコはクッキーを作る予定なので、今日の午後に (　) を買う必要があります。",
     ["history","butter","weather","money"],["歴史","バター","天気","お金"],2,
     "so は『だから』で、前半のクッキー作りが買い物の理由。クッキーの材料になる butter（バター）を買う。money（お金）は支払いに使う物で、ここで買う材料ではない。歴史や天気は買えない。",
     "クッキーをつくるから、ざいりょうの butter『バター』をかうんだね。おかねは、かうためにつかうものだよ。",
     ["歴史は買う物ではない。","クッキーの材料として買う。","天気は買えない。","支払いに使う物で、クッキーの材料ではない。"],
     ["れきしは、かえないよ。","クッキーのざいりょうだね。","てんきは、かえないよ。","おかねで、ざいりょうをかうんだよ。"]),
    ("A: Do you (　) the name of Jenny's pet dog?\nB: Yes, its name is Bounce.",
     "A：ジェニーのペットの犬の名前を (　) か。\nB：はい、名前はバウンスです。",
     ["remember","play","wait","show"],["覚えている","遊ぶ","待つ","見せる"],1,
     "B が Yes の後に犬の名前を答えているので、A は名前を覚えているかを尋ねている。remember the name で『名前を覚えている』。play（遊ぶ）・wait（待つ）・show（見せる）では、名前を答える返事につながらない。",
     "『なまえをおぼえている？』『うん、バウンスだよ』。remember は『おぼえている』だよ。",
     ["名前を覚えているか尋ね、B が名前を答えている。","名前で遊ぶかを尋ねる話ではない。","何かを待つ話で、名前を答える流れにならない。","名前を見せる話ではなく、B は名前を言っている。"],
     ["なまえをおぼえているか、きいているね。","あそぶことではないよ。","まつことではないよ。","みせることではないよ。"]),
    ("Studying English is (　) for Miki. She will visit Canada next year.",
     "英語を勉強することはミキにとって (　) です。彼女は来年カナダを訪れます。",
     ["quiet","long","careful","important"],["静かな","長い","注意深い","大切な"],4,
     "主語は Studying English（英語を勉強すること）。来年カナダを訪れるので、英語の勉強はミキにとって important（大切）。important for 人で『人にとって大切だ』。quiet・long・careful では、カナダへ行くことと理由がつながらない。",
     "らいねんカナダにいくから、えいごのべんきょうがたいせつなんだね。important は『たいせつな』だよ。",
     ["静かかどうかは、カナダ訪問とつながらない。","長さを言っても、カナダ訪問とつながらない。","人の態度を表す語で、勉強の大切さを表さない。","カナダへ行くので、英語の勉強が大切。"],
     ["しずか、ではないよ。","ながい、ではないよ。","ちゅういぶかい、ではないよ。","えいごのべんきょうが、たいせつなんだね。"]),
    ("Ken is very (　) at soccer. He's on the school soccer team.",
     "ケンはサッカーがとても (　) です。彼は学校のサッカー部に入っています。",
     ["short","warm","good","long"],["短い・背が低い","暖かい","上手な・よい","長い"],3,
     "be good at ～で『～が上手だ・得意だ』。学校のサッカー部に入っていることも、サッカーが上手だという内容に合う。short・warm・long では『サッカーが～』という能力の意味にならない。",
     "good at は『～がじょうず・とくい』。サッカーぶにいるケンは、サッカーがじょうずなんだね。",
     ["背の低さや短さで、サッカーの上手さを表さない。","温度を表す語で、サッカーの能力ではない。","good at soccer でサッカーが上手。","長さを表す語で、サッカーの能力ではない。"],
     ["みじかい、ではないよ。","あたたかい、ではないよ。","サッカーがじょうずなんだね。","ながい、ではないよ。"]),
    ("A: Matt, why were you late today?\nB: Sorry, Ms. Parker. I (　) up late.",
     "A：マット、今日はどうして遅刻したのですか。\nB：すみません、パーカー先生。遅く (　)。",
     ["woke","rode","put","cut"],["目が覚めた","乗った","置いた","切った"],1,
     "wake up で『目が覚める』。遅刻した理由を過去のこととして話すので、wake の過去形 woke。woke up late で『起きるのが遅かった』。rode・put・cut も過去形だが、up late と合わせて寝坊の意味にはならない。",
     "ちこくしたのは、おきるのがおそかったから。wake up『めがさめる』のむかしの形は woke だよ。",
     ["woke up late で寝坊したことになり、遅刻の理由になる。","乗り物に乗った話で、寝坊の理由にならない。","物を置いた話で、up late とつながらない。","物を切った話で、遅刻の理由にならない。"],
     ["おきるのがおそかったんだね。","のったことではないよ。","おいたことではないよ。","きったことではないよ。"]),
    ("That bookstore is very big. It has books from all (　) the world.",
     "あの書店はとても大きいです。世界 (　) の本があります。",
     ["under","over","with","up"],["～の下に","～じゅうに","～と一緒に","上へ"],2,
     "all over the world で『世界中』。books from all over the world は『世界中から集まった本』。大きな書店なので、いろいろな国の本がある。under・with・up では、この決まった表現にならない。",
     "all over the world は『せかいじゅう』。おおきなほんやさんには、せかいじゅうのほんがあるんだね。",
     ["『～の下に』では世界中という意味にならない。","all over the world で世界中。","『～と一緒に』では世界中という意味にならない。","『上へ』では世界中という意味にならない。"],
     ["『～のした』ではないよ。","せかいじゅう、のセットだね。","『～といっしょに』ではないよ。","『うえへ』ではないよ。"]),
    ("A: Are you ready to go?\nB: Wait a (　). I can't find my coat.",
     "A：出かける準備はできましたか。\nB：(　) 待ってください。コートが見つからないのです。",
     ["time","point","minute","place"],["時間・回","点","分・少しの間","場所"],3,
     "Wait a minute. は『ちょっと待って』という決まった言い方。コートが見つからず、出発まで少し時間がほしい場面。time・point・place では『ちょっと待って』の意味にならない。",
     "コートがみつからないから『ちょっとまって』。Wait a minute. でおぼえよう。minute は『ふん』だよ。",
     ["time では『ちょっと待って』の決まった言い方にならない。","点という意味で、待つ時間を表さない。","Wait a minute で『ちょっと待って』となる。","場所という意味で、待つ時間を表さない。"],
     ["time では、このいいかたにならないよ。","『てん』では、まつじかんにならないよ。","Wait a minute. で『ちょっとまって』だね。","『ばしょ』では、まつじかんにならないよ。"]),
    ("Jenny got very tired in the race, but she did not give (　). She ran and finished the race.",
     "ジェニーはレースでとても疲れましたが、(　) ませんでした。彼女は走って、レースを最後まで終えました。",
     ["off","on","up","at"],["離れて","上に・続けて","上へ・すっかり","～で・～に"],3,
     "give up で『あきらめる』。とても疲れたが、but の後ろで『あきらめなかった』と続き、最後まで走ったことにつながる。off・on・at を give の後ろに置いても『あきらめる』の意味にはならない。",
     "give up は『あきらめる』。つかれたけど、あきらめないで、さいごまではしったんだね。",
     ["give off では『あきらめる』の意味にならない。","give on という形では『あきらめる』の意味にならない。","did not give up で、あきらめずに完走した。","give at という形では『あきらめる』の意味にならない。"],
     ["off では、このセットにならないよ。","on では、このセットにならないよ。","give up で『あきらめる』だね。","at では、このセットにならないよ。"]),
    ("Yesterday, I (　) my smartphone when I went shopping. I'm really sad now.",
     "昨日、私は買い物に行ったときにスマートフォンを (　)。今、とても悲しいです。",
     ["lose","lost","will lose","losing"],["なくす（原形）","なくした（過去形）","なくすだろう","なくしている（-ing形）"],2,
     "Yesterday と went が過去を示すので、lose（なくす）の過去形 lost。今悲しいのは、昨日スマートフォンをなくしたから。will lose は未来のこと、losing は be 動詞がないと主語 I の動詞にならない。",
     "きのうのできごとだから、むかしの形の lost『なくした』。lose→lost とおぼえよう。",
     ["原形では昨日の出来事を表せない。","Yesterday の出来事なので過去形 lost。","未来の形で、昨日のことには使えない。","-ing 形だけでは主語 I の動詞にならない。"],
     ["いまの形では、きのうのことにならないよ。","きのうのことだから lost だね。","これからのことではないよ。","ing の形だけでは、つかえないよ。"]),
    ("A: Do you know Mt. Fuji?\nB: Of course! It's the (　) famous mountain in Japan.",
     "A：富士山を知っていますか。\nB：もちろんです。日本で (　) 有名な山です。",
     ["too","much","many","most"],["～すぎる","ずっと・たくさんの","たくさんの","最も"],4,
     "the most famous で『最も有名な』。famous は前に most を置いて最上級にする。in Japan が比べる範囲で、富士山は日本でいちばん有名な山。too・much・many では the ～ famous で『最も有名な』の形を作れない。",
     "the most famous は『いちばんゆうめいな』。ふじさんは、にほんでいちばんゆうめいなやまだね。",
     ["too famous は『有名すぎる』で、最上級にならない。","much では『最も有名な』の形にならない。","数の多さを表す語で、famous を最上級にしない。","the most famous で『最も有名な』。"],
     ["『～すぎる』ではないよ。","much では、いちばんにならないよ。","many は、かずがおおいことだよ。","the most で『いちばん』だね。"]),
    ("A: Why are you so late, Jim?\nB: I'm sorry, Mom. I was (　) to my teacher after school.",
     "A：ジム、どうしてこんなに遅くなったのですか。\nB：ごめんなさい、お母さん。放課後、先生と (　) いました。",
     ["talk","talks","talking","talked"],["話す（原形）","話す（三人称単数現在）","話している（-ing形）","話した（過去形）"],3,
     "was＋動詞の -ing 形で『～していた』という過去進行形。I was talking to my teacher で『先生と話していた』。遅くなった理由として、その時していたことを説明している。talk・talks・talked では was と組み合わせて『話していた』の形にならない。",
     "was talking は『はなしていた』。おそくなったのは、せんせいとはなしていたからだね。",
     ["was の後ろに原形 talk は置かない。","was の後ろに三人称単数現在形は置かない。","was talking で『話していた』という過去進行形。","was の後ろに talked を置いても『話していた』にならない。"],
     ["was のあとに talk はおかないよ。","s のついた形ではないよ。","was talking で『はなしていた』だね。","was のあとに talked では、このいみにならないよ。"]),
    ("Mother: Ted, I can't take you to your piano lesson today.\nSon: (　)\nMother: I have to meet Grandma at the airport.",
     "母：テッド、今日はピアノのレッスンに連れて行けません。\n息子：(　)\n母：空港でおばあちゃんを迎えなければならないのです。",
     ["Why not?","What time?","Good job!","Great idea!"],["どうして（だめなの）ですか。","何時ですか。","よくやったね。","いい考えですね。"],1,
     "連れて行けないと言われた息子が理由を尋ねる場面。Why not? は否定の文を受けて『どうして（だめなの）？』と聞く言い方。母が空港でおばあちゃんを迎えるという理由を答えている。What time? なら次に時刻を答える流れになる。",
     "『つれていけないの』『どうして？』『くうこうにいくから』とつながるよ。Why not? は『どうしてだめなの？』だね。",
     ["行けない理由を尋ね、母が理由を答えている。","時刻を尋ねると、次は時刻を答える流れになる。","相手をほめる言葉で、行けない話への返事にならない。","提案への返事で、行けないと言われた場面に合わない。"],
     ["どうしてだめなのか、きいているね。","なんじかは、きいていないよ。","ほめることばではないよ。","いいかんがえ、ではないよ。"]),
    ("Girl: Hi, Mike. (　)\nBoy: A card for my dad. It's Father's Day this Sunday.",
     "女の子：こんにちは、マイク。(　)\n男の子：お父さんへのカードです。今度の日曜日は父の日なんです。",
     ["What are you making?","How was your holiday?","Where is the post office?","Where are you going?"],
     ["何を作っているのですか。","休日はどうでしたか。","郵便局はどこですか。","どこへ行くのですか。"],1,
     "返事の A card for my dad.（父へのカード）は物を答えている。何を作っているかを尋ねる What are you making? が合う。父の日のためにカードを作っている。休日の感想や場所を聞く質問では、カードと答える流れにならない。",
     "『なにをつくっているの？』『おとうさんへのカードだよ』。ちちのひのじゅんびだね。",
     ["作っている物を尋ね、カードと答えている。","休日の感想を聞かれたら、楽しかったなどと答える。","郵便局の場所を聞く質問に、カードは答えにならない。","行き先を聞く質問に、カードは答えにならない。"],
     ["つくっているものをきいているね。","やすみのかんそうではないよ。","ゆうびんきょくのばしょではないよ。","いくばしょではないよ。"]),
    ("Woman 1: Does your son go to school?\nWoman 2: Yes, (　) He likes his teacher.",
     "女性1：息子さんは学校に通っていますか。\n女性2：はい、(　) 彼は先生のことが好きです。",
     ["he started last month.","he's in his bedroom.","I'll make lunch for him.","I'll ask his classmates."],
     ["先月から通い始めました。","彼は寝室にいます。","私が彼に昼食を作ります。","私が彼のクラスメートに聞きます。"],1,
     "Does your son go to school? は息子が学校に通っているかを尋ねている。Yes の後ろで先月から通い始めたと説明し、先生が好きだと続く。started は start（始める）の過去形。寝室にいることや昼食を作ることは、通学の質問への説明にならない。",
     "『がっこうにいっている？』『うん、せんげつからいきはじめたよ』。start は『はじめる』、started は『はじめた』だね。",
     ["通学の質問に答え、先生が好きだと続く。","今いる場所の説明で、通学しているかの答えにならない。","昼食を作ることは通学の説明にならない。","クラスメートに聞くことは、通学の質問への答えにならない。"],
     ["せんげつから、がっこうにいっているんだね。","いまいるばしょのことではないよ。","おひるごはんのことではないよ。","ともだちにきくことではないよ。"]),
    ("Woman: I went to the new restaurant today.\nMan: Really? (　)\nWoman: The chicken sandwich.",
     "女性：今日、新しいレストランに行きました。\n男性：本当ですか。(　)\n女性：チキンサンドイッチです。",
     ["How much was it?","Where is my table?","Who did you go with?","What did you have?"],
     ["いくらでしたか。","私のテーブルはどこですか。","誰と行きましたか。","何を食べましたか。"],4,
     "返事の The chicken sandwich. は料理の名前。レストランで何を食べたかを尋ねる What did you have? が合う。have はここでは『食べる』。値段や一緒に行った人を聞かれたら、料理名ではなく金額や人を答える。",
     "『なにをたべたの？』『チキンサンドイッチ』。have は『たべる』といういみでもつかうよ。",
     ["値段を聞かれたら金額を答える。","自分の席を尋ねる質問で、料理名の答えにならない。","一緒に行った人を聞かれたら、人を答える。","食べた物を尋ね、料理名で答えている。"],
     ["ねだんではないよ。","テーブルのばしょではないよ。","いっしょにいったひとではないよ。","たべたものをきいているね。"]),
    ("Boy: Let's go to the zoo.\nGirl: I can't go today, but (　)\nBoy: OK. Let's go then.",
     "男の子：動物園に行こうよ。\n女の子：今日は行けないけれど、(　)\n男の子：分かった。そのときに行こう。",
     ["I'll be free this weekend.","I'm a student.","do you have a small one?","do you understand me?"],
     ["今週末は空いています。","私は学生です。","小さいものを持っていますか。","私の言うことが分かりますか。"],1,
     "今日は行けないが、but の後ろで空いている時を伝える。I'll be free this weekend.（今週末は空いている）を受けて、男の子が Let's go then.（その時に行こう）と答える。then は this weekend を指す。学生であることなどでは、then が指す時がない。",
     "きょうはいけないけど、こんしゅうまつはあいているよ。then『そのとき』は、こんしゅうまつのことだね。",
     ["空いている時を示し、then がその時を指す。","学生であることは、行く日の話につながらない。","小さい物を持っているかは、動物園へ行く話とつながらない。","分かるかどうかを聞いても、then が指す時がない。"],
     ["こんしゅうまつなら、いけるんだね。","がくせいかどうかではないよ。","ちいさいもののおはなしではないよ。","わかるかどうかではないよ。"]),
]


def build():
    p,o,m=module("passages"),module("order"),module("materials")
    qs=[]
    for n,r in enumerate(ROWS,1):
        text,ja,choices,meanings,answer,grammar,simple,reasons,easy=r
        qs.append(dict(number=n,text=text,translation=ja,choices=choices,
                       choiceTranslations=meanings,answer=answer,grammar=grammar,grammarSimple=simple,
                       choiceAnalysis=[("○ " if i==answer else "")+f"{c}＝{t.rstrip('。')}。{why}" for i,(c,t,why) in enumerate(zip(choices,meanings,reasons),1)],
                       choiceAnalysisSimple=[("○ " if i==answer else "")+f"{t.rstrip('。')}。{why}" for i,(t,why) in enumerate(zip(meanings,easy),1)],
                       questionAudio=f"audio/q{n}.mp3"))
    sections=[
        dict(name="大問1",nameEn="Part 1",type="vocabulary",instruction="次の(1)から(15)までの(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選び，その番号のマーク欄をぬりつぶしなさい。",questions=qs[:15]),
        dict(name="大問2",nameEn="Part 2",type="vocabulary",instruction="次の(16)から(20)までの会話について，(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選び，その番号のマーク欄をぬりつぶしなさい。",questions=qs[15:]),
        dict(name="大問3",nameEn="Part 3",type="sentence-order",instruction="次の(21)から(25)までの日本文の意味を表すように①から⑤までを並べかえて□の中に入れなさい。そして，2番目と4番目にくるものの最も適切な組合せを1，2，3，4の中から一つ選び，その番号のマーク欄をぬりつぶしなさい。※ただし，(　)の中では，文のはじめにくる語も小文字になっています。",questions=o.questions()),
        dict(name="大問4",nameEn="Part 4",type="reading-comprehension",instruction="次の掲示・Eメール・英文を読み、それぞれの問いに答えなさい。",passages=p.PASSAGES),
    ]
    listening=[1,1,1,3,1,1,2,1,3,1,1,4,3,3,4,3,4,4,2,3,3,1,2,4,1,3,3,1,3,1]
    return dict(grade="grade4",year="2025",session="2025-2-sat",exam="2025-2-sat",
                title="英検4級 2025年度 第2回（土曜準会場）",sections=sections,
                listening={f"part{i+1}":dict(zip(map(str,range(10*i+1,10*i+11)),listening[10*i:10*i+10])) for i in range(3)},
                vocabulary=m.vocabulary(),lessonPlan=m.lessonplan(sections))


if __name__=="__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(build(),ensure_ascii=False,indent=4)+"\n",encoding="utf-8")
    print(OUT)

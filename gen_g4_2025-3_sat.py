# -*- coding: utf-8 -*-
"""Reproduce Grade 4 2025-3 Saturday; booklet pp. 2-11, page images + text layer."""
import importlib.util
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "data/grade4/2025-3-sat/data.json"


def module(suffix):
    spec=importlib.util.spec_from_file_location(suffix,ROOT/f"gen_g4_2025-3_sat_{suffix}.py")
    result=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


# stem, translation, choices, meanings, answer, normal/simple grammar,
# choice-specific reasons. All four normal/simple analyses retain meanings.
ROWS = [
    ("A: Do you want some more chicken, Mr. Norton?\nB: No, thanks. I'm (　).",
     "A：ノートンさん、チキンをもう少しいかがですか。\nB：いいえ、けっこうです。おなかが (　) です。",
     ["dry","long","slow","full"],["乾いた","長い","遅い","いっぱいの・満腹の"],4,
     "No, thanks.（いいえ、けっこうです）で、おかわりを断っている。断る理由として I'm full.（おなかがいっぱいです）が合う。full は『いっぱいの』で、食事の場面では『満腹の』。dry・long・slow では、おかわりを断る理由にならない。",
     "『チキンをもっとどう？』『いいえ、もうおなかがいっぱい』。full は『いっぱいの』だよ。",
     ["乾いている、ではおかわりを断る理由にならない。","長さを表す語で、おかわりを断る理由にならない。","遅い、ではおかわりを断る理由にならない。","おなかがいっぱいなので、おかわりを断っている。"],
     ["かわいている、ではないよ。","ながい、ではないよ。","おそい、ではないよ。","おなかがいっぱいなんだね。"]),
    ("A: Does your family have a (　) garden?\nB: No, it's small, but my father loves to grow vegetables in it.",
     "A：あなたの家には (　) 庭がありますか。\nB：いいえ、小さいです。でも、父はそこで野菜を育てるのが大好きです。",
     ["sure","rainy","large","ready"],["確かな","雨の降る","大きい・広い","準備ができた"],3,
     "B は No, it's small（いいえ、小さいです）と答えている。small（小さい）と反対の意味の large（大きい・広い）を入れると、質問と答えがかみ合う。sure・rainy・ready は庭の大きさを表さない。",
     "『おおきいにわはある？』『ううん、ちいさいよ』。large は『おおきい』、small は『ちいさい』だよ。",
     ["確かな、では庭の様子を表さない。","雨の降る、は天気の言葉で、小さいという答えにつながらない。","small（小さい）と反対の意味で、No の答えと合う。","準備ができた、では庭の様子を表さない。"],
     ["たしかな、ではないよ。","あめのふる、ではないよ。","おおきいにわか、きいているね。","じゅんびができた、ではないよ。"]),
    ("In art class, Anna is (　) a picture of her pet rabbit.",
     "美術の授業で、アンナはペットのウサギの絵を (　) います。",
     ["listening","cooking","drawing","teaching"],["聞いている","料理している","描いている","教えている"],3,
     "is＋動詞の -ing 形で『～している』。a picture（絵）を目的語にとり、美術の授業に合うのは draw（描く）。draw a picture で『絵を描く』。listening は後ろに to が必要で、cooking・teaching は絵とつながらない。",
     "びじゅつのじゅぎょうで、ウサギのえをかいているね。draw a picture は『えをかく』だよ。",
     ["listen は後ろに to が必要で、絵を聞くことはできない。","絵を料理することはできない。","draw a picture で『絵を描く』。美術の授業に合う。","絵を教える、では意味が通らない。"],
     ["えをきく、ではないよ。","えをりょうりする、ではないよ。","えをかいているんだね。","えをおしえる、ではないよ。"]),
    ("A: Did you enjoy riding your bike today, Kelly?\nB: No, it was hard because the (　) was so strong.",
     "A：ケリー、今日は自転車に乗って楽しかったですか。\nB：いいえ、(　) がとても強かったので大変でした。",
     ["summer","wind","story","family"],["夏","風","物語","家族"],2,
     "because の後ろが、自転車に乗るのが大変だった理由。strong（強い）と結びついて、自転車をこぎにくくするのは wind（風）。The wind is strong. で『風が強い』。summer・story・family では、自転車が大変だった理由にならない。",
     "かぜがつよいと、じてんしゃはたいへんだね。wind は『かぜ』だよ。",
     ["夏は季節で、自転車が大変だった理由にならない。","風が強いと、自転車に乗るのが大変になる。","物語は自転車に乗ることと関係がない。","家族が強い、では大変だった理由にならない。"],
     ["なつは、きせつのなまえだよ。","かぜがつよかったんだね。","おはなしは、かんけいないよ。","かぞくのことではないよ。"]),
    ("A: Is it going to rain tomorrow?\nB: No, but it'll be (　) here.",
     "A：明日は雨が降りますか。\nB：いいえ。でも、ここは (　) でしょう。",
     ["cheap","lazy","simple","cloudy"],["安い","怠けた","簡単な","くもりの"],4,
     "it は天気を表す主語。A は雨が降るかを尋ね、B は No, but（いいえ、でも）と続けている。雨は降らないが晴れでもない天気として cloudy（くもりの）が合う。cheap・lazy・simple は天気を表さない。",
     "あめはふらないけど、くもりになるよ。cloudy は『くもりの』。てんきの it だね。",
     ["値段を表す語で、天気を表さない。","人の様子を表す語で、天気を表さない。","簡単さを表す語で、天気を表さない。","雨ではないが、くもりになるという天気の答え。"],
     ["ねだんのことではないよ。","なまけている、ではないよ。","かんたん、ではないよ。","くもりになるんだね。"]),
    ("Bill loves tennis. He has a tennis (　) every Saturday morning in the park near his house.",
     "ビルはテニスが大好きです。彼は毎週土曜日の朝、家の近くの公園でテニスの (　) があります。",
     ["captain","school","lesson","story"],["主将・キャプテン","学校","レッスン・授業","物語"],3,
     "has a tennis lesson で『テニスのレッスンがある』。every Saturday morning（毎週土曜日の朝）に公園であるものとして lesson が合う。captain は人、school は学校、story は物語で、毎週土曜日の朝に公園であることを表さない。",
     "テニスがだいすきなビルは、まいしゅうどようびのあさにテニスのレッスンがあるんだね。lesson は『レッスン』だよ。",
     ["キャプテンは人で、毎週土曜日の朝にあるものではない。","学校は、公園で毎週あるものではない。","毎週土曜日の朝にテニスのレッスンがある。","物語では、公園で毎週あることにならない。"],
     ["キャプテンは、ひとのことだよ。","がっこう、ではないよ。","テニスのレッスンがあるんだね。","おはなし、ではないよ。"]),
    ("A: I love cats and dogs. What is your favorite (　)?\nB: I like frogs. They are cute.",
     "A：私はネコとイヌが大好きです。あなたのいちばん好きな (　) は何ですか。\nB：私はカエルが好きです。かわいいですよ。",
     ["article","astronaut","office","animal"],["記事","宇宙飛行士","事務所・会社","動物"],4,
     "A は cats and dogs（ネコとイヌ）が好きだと話し、B は frogs（カエル）と答えている。どれも動物なので、What is your favorite animal?（いちばん好きな動物は何ですか）が合う。article・astronaut・office では、カエルという答えにつながらない。",
     "ネコ、イヌ、カエルは、みんな animal『どうぶつ』だね。すきなどうぶつをきいているよ。",
     ["記事を尋ねると、カエルという答えにならない。","宇宙飛行士を尋ねると、カエルという答えにならない。","事務所を尋ねると、カエルという答えにならない。","ネコ・イヌ・カエルはどれも動物。"],
     ["きじ、ではないよ。","うちゅうひこうし、ではないよ。","じむしょ、ではないよ。","すきなどうぶつをきいているね。"]),
    ("A: Is this your camera?\nB: Yes. I like (　) pictures.",
     "A：これはあなたのカメラですか。\nB：はい。私は写真を (　) のが好きです。",
     ["answering","taking","hearing","riding"],["答えること","撮ること","聞くこと","乗ること"],2,
     "take a picture で『写真を撮る』。like＋動詞の -ing 形で『～するのが好きだ』なので、like taking pictures で『写真を撮るのが好きだ』。カメラの持ち主なので話がつながる。answering・hearing・riding は pictures とつながらない。",
     "カメラで、しゃしんをとるのがすきなんだね。take pictures は『しゃしんをとる』だよ。",
     ["写真に答えることはできない。","take pictures で『写真を撮る』。カメラの話に合う。","写真を聞くことはできない。","写真に乗ることはできない。"],
     ["しゃしんにこたえる、ではないよ。","しゃしんをとるのがすきなんだね。","しゃしんをきく、ではないよ。","しゃしんにのる、ではないよ。"]),
    ("A: Did you like the Christmas concert?\nB: I really liked it, but I didn't know the songs in the second (　) of the concert.",
     "A：クリスマスコンサートは気に入りましたか。\nB：とても気に入りました。でも、コンサートの2つ目の (　) の歌は知りませんでした。",
     ["game","shop","world","part"],["試合・ゲーム","店","世界","部分・部"],4,
     "the second part of the concert で『コンサートの2つ目の部分（第2部）』。コンサートがいくつかの部分に分かれていて、その2つ目の部分の歌を知らなかった。game・shop・world は、コンサートの一部分を表さない。",
     "part は『ぶぶん』。コンサートの2つめのぶぶんのうたを、しらなかったんだね。",
     ["試合は、コンサートの一部分を表さない。","店は、コンサートの一部分を表さない。","世界は、コンサートの一部分を表さない。","the second part で『2つ目の部分（第2部）』。"],
     ["しあい、ではないよ。","おみせ、ではないよ。","せかい、ではないよ。","コンサートの2つめのぶぶんだね。"]),
    ("A: What subject are you (　) in at school?\nB: I love P.E. because I enjoy learning about different sports.",
     "A：学校では、どの教科に (　) がありますか。\nB：体育が大好きです。いろいろなスポーツについて学ぶのが楽しいからです。",
     ["ready","interested","angry","international"],["準備ができた","興味がある","怒った","国際的な"],2,
     "be interested in ～で『～に興味がある』。疑問文では What subject are you interested in? と、in が文の後ろに残る。B は好きな教科として体育を答えている。ready・angry・international では、in と合わせて『～に興味がある』の意味にならない。",
     "interested in は『～にきょうみがある』。たいいくがすき、とこたえているね。",
     ["準備ができた、では好きな教科を答える流れにならない。","be interested in で『～に興味がある』。好きな教科の答えに合う。","怒った、では好きな教科を答える流れにならない。","国際的な、は人の気持ちを表さない。"],
     ["じゅんびができた、ではないよ。","きょうみがあるきょうかを、きいているね。","おこっている、ではないよ。","こくさいてきな、ではないよ。"]),
    ("A: Is there a good movie (　) TV tonight?\nB: Yes. It's about a young dancer.",
     "A：今夜、テレビ (　) いい映画をやっていますか。\nB：はい。若いダンサーの映画です。",
     ["on","for","by","after"],["～で（放送されて）","～のために","～によって・～のそばに","～の後に"],1,
     "on TV で『テレビで（放送されて）』。テレビで番組や映画が放送されることを表すときは on を使う。for・by・after では『テレビで放送される』の意味にならない。",
     "on TV は『テレビで』。こんやテレビでやるえいがのことだね。",
     ["on TV で『テレビで（放送されて）』。","『テレビのために』では、放送される意味にならない。","『テレビによって・テレビのそばに』では、放送される意味にならない。","『テレビの後に』では、意味が通らない。"],
     ["テレビでやるえいがだね。","『テレビのために』ではないよ。","by では、このいみにならないよ。","『テレビのあとに』ではないよ。"]),
    ("On the plane, I (　) a new friend. She is a high school student, too.",
     "飛行機の中で、私は新しい友だちを (　)。彼女も高校生です。",
     ["came","wrote","made","told"],["来た","書いた","作った","伝えた"],3,
     "make a friend で『友だちを作る・友だちになる』。飛行機の中で知り合った過去のことなので、make の過去形 made。came（来た）は後ろに a new friend を置けず、wrote（書いた）・told（伝えた）では友だちができた意味にならない。",
     "make a friend は『ともだちをつくる』。make のむかしの形は made だよ。",
     ["come の過去形で、後ろに a new friend を置けない。","友だちを書く、では意味が通らない。","made a new friend で『新しい友だちができた』。","told は『（人に）伝えた』で、友だちができた意味にならない。"],
     ["きた、ではないよ。","かいた、ではないよ。","あたらしいともだちができたんだね。","つたえた、ではないよ。"]),
    ("A: Hello, it's Dave. Is Kelly there?\nB: Yes, but she's (　) dinner right now.",
     "A：もしもし、デイブです。ケリーはいますか。\nB：はい。でも、ケリーはちょうど今、夕食を (　) ところです。",
     ["eating","eats","eat","ate"],["食べている（-ing形）","食べる（三人称単数現在）","食べる（原形）","食べた（過去形）"],1,
     "she's は she is の短縮形。is＋動詞の -ing 形で『～している』という現在進行形になる。right now（ちょうど今）も、今していることを表す。eats・eat・ate は is の後ろに置けない。",
     "she's は she is。is eating で『たべているところ』。right now は『ちょうどいま』だよ。",
     ["she's eating で『食べているところ』。","is の後ろに三人称単数現在形は置かない。","is の後ろに原形は置かない。","is の後ろに過去形は置かない。right now とも合わない。"],
     ["いまたべているところだね。","s のついた形は、is のあとにおかないよ。","is のあとに eat はおかないよ。","むかしの形ではないよ。"]),
    ("A: Do you and your mom have the same sweater?\nB: Yes, but (　) is green.",
     "A：あなたとお母さんは同じセーターを持っていますか。\nB：はい。でも、(　) は緑色です。",
     ["its","hers","his","yours"],["それの","彼女のもの","彼の・彼のもの","あなたのもの"],2,
     "hers は『彼女のもの』で、ここでは母のセーター（her sweater）を指す。同じセーターだが、母のものは緑色だということ。its は物や動物について使い、後ろに名詞を置く。his は男性のもの、yours は相手 A のものを指すので、B の母の話にならない。",
     "hers は『かのじょのもの』。おかあさんのセーターは、みどりいろなんだね。",
     ["its は物や動物について使い、後ろに名詞を置く。母のものを表さない。","hers は母のセーターを指す。","his は男性のものを指し、母のものではない。","yours は相手 A のものを指し、B の母の話にならない。"],
     ["its は、ひとのものをあらわさないよ。","おかあさんのセーターのことだね。","his は、おとこのひとのものだよ。","yours は『あなたのもの』だよ。"]),
    ("Yesterday, Anna (　) me a lot of pictures of her family.",
     "昨日、アンナは私に家族の写真をたくさん (　)。",
     ["show","shows","showed","showing"],["見せる（原形）","見せる（三人称単数現在）","見せた（過去形）","見せている（-ing形）"],3,
     "Yesterday（昨日）があるので過去形 showed。show＋人＋物で『人に物を見せる』なので、showed me a lot of pictures で『私にたくさんの写真を見せた』。show・shows は現在の形、showing は be 動詞がないと主語 Anna の動詞にならない。",
     "Yesterday は『きのう』。きのうのことだから、むかしの形 showed だよ。",
     ["原形では昨日の出来事を表せない。","現在の形で、昨日のことには使えない。","Yesterday の出来事なので過去形 showed。","-ing 形だけでは主語 Anna の動詞にならない。"],
     ["いまの形では、きのうのことにならないよ。","s のついたいまの形ではないよ。","きのうのことだから showed だね。","ing の形だけでは、つかえないよ。"]),
    ("Son: Mom, I don't like carrots. (　)\nMother: Yes. They're good for you.",
     "息子：お母さん、ぼくはニンジンが好きじゃないんだ。(　)\n母：そうよ。体にいいのよ。",
     ["Can we eat in the park?","Do I have to eat them?","Let's go to a restaurant.","I'll wash the dishes."],
     ["公園で食べてもいい？","それを食べなければいけないの？","レストランに行こうよ。","ぼくがお皿を洗うよ。"],2,
     "ニンジンが好きではない息子が、Do I have to eat them?（食べなければいけないの？）と尋ねる。have to は『～しなければならない』、them は carrots を指す。母は Yes（そうよ）と答え、体によいという理由を続けている。公園やレストランの話では、They're good for you. につながらない。",
     "『ニンジンをたべなきゃだめ？』『そうよ、からだにいいのよ』。have to は『～しなければならない』だよ。",
     ["公園で食べる話では、母の『体にいい』とつながらない。","them は carrots。食べなければならないかを尋ね、母が Yes と答える。","レストランへ行く提案では、母の答えとつながらない。","皿洗いを申し出ても、『体にいい』という返事にならない。"],
     ["こうえんでたべる、ではないよ。","たべなきゃだめ？ときいているね。","レストランのはなしではないよ。","おさらあらいのはなしではないよ。"]),
    ("Boy: I need a dictionary. Do you have one?\nGirl: No, I don't. (　)\nBoy: Thanks.",
     "男の子：辞書が必要なんだ。持ってる？\n女の子：ううん、持っていないよ。(　)\n男の子：ありがとう。",
     ["I'll go to sleep early.","It's next week.","You should ask Mr. Carter.","I like Japanese class."],
     ["私は早く寝るよ。","それは来週だよ。","カーターさんに聞いてみるといいよ。","私は日本語の授業が好きだよ。"],3,
     "女の子は辞書を持っていないが、聞いてみるとよい人を教えている。should は『～したほうがよい』。助言を受けた男の子が Thanks.（ありがとう）と答える。早く寝る話や来週の予定では、お礼の返事につながらない。",
     "じしょはもっていないけど、『カーターさんにきいてみたら』とおしえてあげたね。should は『～したほうがいい』だよ。",
     ["早く寝る話は、辞書を探す相談とつながらない。","何が来週なのかが分からず、お礼の返事にもつながらない。","聞いてみるとよい人を教えたので、男の子がお礼を言う。","授業の好みは、辞書を探す相談とつながらない。"],
     ["はやくねる、ではないよ。","らいしゅう、ではないよ。","きいてみるといいひとを、おしえているね。","すきなじゅぎょうのはなしではないよ。"]),
    ("Girl 1: You look nice today.\nGirl 2: Thanks. This is a new dress.\nGirl 1: (　)",
     "女の子1：今日はすてきだね。\n女の子2：ありがとう。これは新しいワンピースなの。\n女の子1：(　)",
     ["I went to a party.","It's in my bedroom.","You can do it.","It's very pretty."],
     ["私はパーティーに行ったよ。","それは私の寝室にあるよ。","あなたならできるよ。","とてもかわいいね。"],4,
     "女の子2は、着ている新しいワンピースの話をしている。女の子1は It's very pretty.（とてもかわいいね）とほめる。It は a new dress を指す。今着ているワンピースが寝室にあるとは言わず、You can do it. は相手を励ます言葉。",
     "あたらしいワンピースを『とてもかわいいね』とほめているよ。It はワンピースのことだね。",
     ["自分がパーティーに行った話で、ワンピースの話につながらない。","今着ているワンピースが寝室にあることにはならない。","相手を励ます言葉で、服をほめる場面に合わない。","It は新しいワンピースを指し、ほめている。"],
     ["パーティーのはなしではないよ。","いまきているから、へやにはないよ。","がんばって、のことばだよ。","ワンピースをほめているね。"]),
    ("Girl: Your new cell phone is nice. (　)\nBoy: Sure. Here you are.",
     "女の子：あなたの新しい携帯電話、すてきだね。(　)\n男の子：いいよ。はい、どうぞ。",
     ["Where did you get it?","How much was it?","Can I see it, please?","Can I help you?"],
     ["どこで手に入れたの？","いくらだったの？","見せてもらってもいい？","何かお手伝いしましょうか。"],3,
     "男の子の Sure.（いいよ）と Here you are.（はい、どうぞ）は、頼まれて物を渡すときの返事。携帯電話を見たいと頼む Can I see it, please? が合う。Can I ～? は『～してもいいですか』。場所や値段を聞かれたら、店の名前や金額を答える。",
     "『みせてもいい？』『いいよ、はいどうぞ』。Here you are. は、ものをわたすときのことばだよ。",
     ["場所を聞かれたら、店などの場所を答える。","値段を聞かれたら、金額を答える。","見せてほしいと頼み、男の子が電話を渡している。","店員などが手伝いを申し出る言葉で、ここでは合わない。"],
     ["どこでかったか、ではないよ。","ねだん、ではないよ。","みせてね、とたのんでいるね。","おてつだい、ではないよ。"]),
    ("Wife: I like this TV show. (　)\nHusband: Me, too. It's really funny.",
     "妻：私はこのテレビ番組が好きよ。(　)\n夫：ぼくもだよ。本当におもしろいね。",
     ["Why are you watching it?","Who is that actor?","How about you?","When did it start?"],
     ["どうしてそれを見ているの？","あの俳優は誰？","あなたはどう？","それはいつ始まったの？"],3,
     "How about you? は『あなたはどう？』と相手の考えを尋ねる言い方。夫は Me, too.（ぼくも好きだよ）と答えている。見ている理由、俳優の名前、始まった時を聞かれたら、Me, too. では答えにならない。",
     "『わたしはこのばんぐみがすき。あなたは？』『ぼくもだよ』。How about you? は『あなたはどう？』だね。",
     ["見ている理由を聞かれたら、理由を答える。","俳優を聞かれたら、人の名前を答える。","相手の気持ちを尋ね、夫が Me, too. と答える。","始まった時を聞かれたら、時を答える。"],
     ["りゆうをきかれたら、りゆうをこたえるよ。","はいゆうのなまえではないよ。","『あなたはどう？』ときいているね。","いつはじまったか、ではないよ。"]),
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
    listening=[3,1,3,1,2,3,2,3,2,2,1,2,3,4,2,3,4,1,2,1,2,2,1,3,1,2,2,1,1,4]
    return dict(grade="grade4",year="2025",session="2025-3-sat",exam="2025-3-sat",
                title="英検4級 2025年度 第3回（土曜準会場）",sections=sections,
                listening={f"part{i+1}":dict(zip(map(str,range(10*i+1,10*i+11)),listening[10*i:10*i+10])) for i in range(3)},
                vocabulary=m.vocabulary(),lessonPlan=m.lessonplan(sections))


if __name__=="__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(build(),ensure_ascii=False,indent=4)+"\n",encoding="utf-8")
    print(OUT)

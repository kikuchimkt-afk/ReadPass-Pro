# -*- coding: utf-8 -*-
"""Reproduce Grade 4 2024-2 Saturday; booklet pp. 2-11, transcribed from page images (noisy OCR text layer used only as a cross-check)."""
import importlib.util
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "data/grade4/2024-2-sat/data.json"


def module(suffix):
    spec=importlib.util.spec_from_file_location(suffix,ROOT/f"gen_g4_2024-2_sat_{suffix}.py")
    result=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


# stem, translation, choices, meanings, answer, normal/simple grammar,
# choice-specific reasons. All four normal/simple analyses retain meanings.
ROWS = [
    ("Karen wants to listen to the newest pop songs, so she listens to the (　) every morning.",
     "カレンは最新のポップソングを聞きたいので、毎朝 (　) を聞いています。",
     ["radio","shelf","pool","theater"],["ラジオ","棚","プール","劇場"],1,
     "listen to ～で『～を聞く』。so（だから）の前が理由で、最新のポップソングを聞きたいから毎朝聞くものなので radio（ラジオ）。listen to the radio で『ラジオを聞く』。shelf・pool・theater は耳で聞くものではない。",
     "あたらしいうたをききたいから、まいあさラジオをきくんだね。radio は『ラジオ』だよ。",
     ["最新の曲を聞くために毎朝聞くものとして合う。","棚は物を置く家具で、聞くものではない。","プールは泳ぐ場所で、聞くものではない。","劇場は劇などを見に行く場所で、毎朝聞くものではない。"],
     ["まいあさラジオでうたをきくんだね。","たなは、ものをおくところだよ。","プールは、およぐところだよ。","げきじょうは、げきをみるところだよ。"]),
    ("A: This video game looks fun. Can I (　) it?\nB: Of course, Mike. Let's play it together.",
     "A：このテレビゲーム、おもしろそうだね。(　) もいい？\nB：もちろんだよ、マイク。一緒に遊ぼう。",
     ["try","make","break","cut"],["試す・やってみる","作る","壊す","切る"],1,
     "Can I ～? は『～してもいいですか』と許可を求める言い方。おもしろそうなゲームを見て、Can I try it?（やってみてもいい？）と頼んでいる。B が Of course（もちろん）と答え、Let's play it together.（一緒に遊ぼう）と続けているので、ゲームをやってみる話。make・break・cut ではゲームで遊ぶ話につながらない。",
     "『このゲーム、おもしろそう。やってみてもいい？』『もちろん。いっしょにあそぼう』。try は『やってみる』だよ。",
     ["ゲームをやってみたいと頼み、Let's play it together. につながる。","ゲームを作るのではなく、遊ぶ話をしている。","壊してもいいかと聞く場面ではない。","ゲームを切る、では意味が通らない。"],
     ["やってみたいんだね。","つくる、ではないよ。","こわす、ではないよ。","きる、ではないよ。"]),
    ("A: Could you (　) some drinks to the party tomorrow, Kate?\nB: Sure. I'll buy some at the shop before I come to your house.",
     "A：ケイト、明日のパーティーに飲み物を (　) くれる？\nB：いいよ。あなたの家に行く前に、お店で買っていくね。",
     ["shoot","bring","clean","throw"],["シュートする・撃つ","持って来る","掃除する","投げる"],2,
     "Could you ～? は『～してくれませんか』と頼む言い方。bring A to B で『A を B へ持って来る』。B は『家に行く前にお店で買う』と答えているので、飲み物をパーティーに持って来てほしいという頼みだとわかる。shoot・clean・throw では、飲み物を買って行くという返事とつながらない。",
     "『あしたのパーティーに、のみものをもってきてくれる？』『いいよ。かってからいくね』。bring は『もってくる』だよ。",
     ["シュートする・撃つという意味で、飲み物について頼む内容にならない。","飲み物をパーティーに持って来てほしいと頼み、B が買って行くと答えている。","飲み物を掃除する、では意味が通らない。","飲み物を投げる、では頼みの内容として合わない。"],
     ["シュートする、ではないよ。","のみものをもってきてね、とたのんでいるね。","そうじする、ではないよ。","なげる、ではないよ。"]),
    ("Dave (　) some eggs to make a cake, so he went to the shop to buy some.",
     "デイブはケーキを作るために卵が (　) ので、お店へ買いに行きました。",
     ["told","needed","played","ate"],["話した（tell の過去形）","必要だった（need の過去形）","遊んだ・（競技を）した（play の過去形）","食べた（eat の過去形）"],2,
     "need は『～を必要とする』で、needed はその過去形。ケーキを作るのに卵が必要だった → だから（so）お店へ買いに行った、という流れになる。buy some の some は some eggs のこと。told・played・ate では、卵を買いに行く理由にならない。",
     "ケーキをつくるのにたまごがひつようだったから、かいにいったんだね。needed は『ひつようだった』だよ。",
     ["卵に何かを話した、では意味が通らない。","ケーキ作りに卵が必要で、だから買いに行ったとつながる。","卵で遊んだ、では買いに行く理由にならない。","ケーキを作るために卵を食べた、では意味が通らない。"],
     ["はなした、ではないよ。","たまごがひつようだったんだね。","あそんだ、ではないよ。","たべた、ではないよ。"]),
    ("The students were very excited when a (　) singer came to their school and sang some of his most popular songs.",
     "(　) 歌手が学校に来て、いちばん人気のある歌を何曲か歌ったとき、生徒たちはとてもわくわくしました。",
     ["cloudy","long","famous","bored"],["くもった","長い","有名な","退屈した"],3,
     "a (　) singer の空所には、歌手を説明する語が入る。歌手が自分のいちばん人気のある歌（his most popular songs）を歌い、生徒たちがとてもわくわくした（were very excited）ことから、famous（有名な）が合う。cloudy は天気、long は長さを表す語。bored は『退屈した』で、わくわくした場面に合わない。",
     "ゆうめいなかしゅががっこうにきたから、みんなわくわくしたんだね。famous は『ゆうめいな』だよ。",
     ["天気を表す語で、歌手の説明にならない。","長さを表す語で、歌手の説明にならない。","人気の歌を持つ有名な歌手が来て、生徒がわくわくした。","退屈した歌手では、生徒がわくわくした場面に合わない。"],
     ["てんきのことばだよ。","ながさのことばだよ。","ゆうめいなかしゅだね。","たいくつした、ではあわないよ。"]),
    ("It was raining outside, so the students practiced soccer in the (　).",
     "外は雨が降っていたので、生徒たちは (　) でサッカーを練習しました。",
     ["kitchen","gym","store","bag"],["台所","体育館","店","かばん"],2,
     "so（だから）の前が理由。外は雨だったので、建物の中で運動できる gym（体育館）でサッカーを練習した。kitchen（台所）や store（店）はサッカーを練習する場所ではなく、bag（かばん）の中では練習できない。",
     "そとはあめだったから、たいいくかんでサッカーをしたんだね。gym は『たいいくかん』だよ。",
     ["台所は料理をする場所で、サッカーの練習には使わない。","雨の日に建物の中でサッカーを練習できる場所。","店はサッカーを練習する場所ではない。","かばんの中では練習できない。"],
     ["だいどころでは、サッカーはしないよ。","たいいくかんでれんしゅうしたんだね。","おみせでは、サッカーはしないよ。","かばんのなかではできないよ。"]),
    ("George had a toothache, so he went to see the (　).",
     "ジョージは歯が痛かったので、(　) に診てもらいに行きました。",
     ["arm","wall","dentist","singer"],["腕","壁","歯医者","歌手"],3,
     "toothache は『歯痛』で、had a toothache は『歯が痛かった』。so の後ろは歯が痛いときにすることなので、go to see the dentist（歯医者に診てもらう）が合う。arm（腕）や wall（壁）は会いに行く相手ではなく、singer（歌手）では歯の痛みとつながらない。",
     "はがいたかったから、はいしゃさんにいったんだね。dentist は『はいしゃ』だよ。",
     ["腕は体の部分で、会いに行く相手ではない。","壁は会いに行く相手ではない。","歯が痛いときに診てもらう人。","歌手に会っても、歯の痛みとつながらない。"],
     ["うでは、からだのぶぶんだよ。","かべに、あいにはいかないよ。","はいしゃさんにいったんだね。","かしゅでは、はのいたみとつながらないよ。"]),
    ("Dan didn't go to school yesterday because he had a (　). He stayed in bed all day.",
     "ダンは (　) をひいていたので、昨日は学校へ行きませんでした。一日中ベッドで寝ていました。",
     ["key","cup","cold","belt"],["鍵","カップ","かぜ","ベルト"],3,
     "have a cold で『かぜをひいている』。because（～なので）の後ろは学校を休んだ理由で、2文目の He stayed in bed all day.（一日中ベッドで寝ていた）とも合う。cold は『寒い・冷たい』の意味でよく使うが、a cold と名詞で使うと『かぜ』。key・cup・belt を持っていても、学校を休む理由にならない。",
     "かぜをひいたから、がっこうをやすんでねていたんだね。a cold は『かぜ』だよ。",
     ["鍵を持っていても、学校を休む理由にならない。","カップを持っていても、学校を休む理由にならない。","かぜをひいて、一日中寝ていたことと合う。","ベルトを持っていても、学校を休む理由にならない。"],
     ["かぎでは、やすむりゆうにならないよ。","カップでは、やすむりゆうにならないよ。","かぜでやすんだんだね。","ベルトでは、やすむりゆうにならないよ。"]),
    ("Last week, Robert went to Chicago. His sister lives there, so he stayed (　) her.",
     "先週、ロバートはシカゴへ行きました。姉（妹）がそこに住んでいるので、彼女 (　) 泊まりました。",
     ["with","into","from","through"],["～と一緒に・～の家に","～の中へ","～から","～を通り抜けて"],1,
     "stay with ～で『～の家に泊まる』。there は Chicago を指し、姉（妹）がシカゴに住んでいるので、その家に泊まったという流れになる。into・from・through は stay と組み合わせても、人の家に泊まる意味にならない。",
     "シカゴにすんでいるおねえさん（いもうと）のいえにとまったんだね。stay with は『～のいえにとまる』だよ。",
     ["stay with ～で『～の家に泊まる』。","『～の中へ』では、人の家に泊まる意味にならない。","『～から』では、泊まった場所を表せない。","『～を通り抜けて』では、人の家に泊まる意味にならない。"],
     ["おねえさんのいえにとまったね。","『～のなかへ』ではないよ。","『～から』ではないよ。","『～をとおって』ではないよ。"]),
    ("Richard usually (　) home at 5:00 p.m. His train was late today, so he arrived at his house at 6:30 p.m.",
     "リチャードはふだん午後5時に家に (　)。今日は電車が遅れたので、午後6時30分に家に着きました。",
     ["jumps","has","gets","learns"],["跳ぶ","持っている","（get home で）家に着く","学ぶ"],3,
     "get home で『家に着く・帰宅する』。usually（ふだん）とあるので現在形で、主語 Richard に合わせて gets。2文目の arrived at his house（家に着いた）が同じ内容を表している。この home は『家へ』という意味なので、前に to は置かない。jumps・has・learns では帰宅を表せない。",
     "いつもは5じにいえにかえるけど、きょうはでんしゃがおくれたんだね。get home は『いえにつく』だよ。",
     ["跳ぶ、では帰宅の時刻を表せない。","has home では意味が通らない。","gets home で『帰宅する』。arrived at his house と同じ内容。","学ぶ、では帰宅の時刻を表せない。"],
     ["とぶ、ではないよ。","has では、いみがつながらないよ。","いえにかえるんだね。","まなぶ、ではないよ。"]),
    ("Fiona got a camera for her birthday. She likes (　) pictures of her friends.",
     "フィオナは誕生日にカメラをもらいました。彼女は友だちの写真を (　) のが好きです。",
     ["taking","speaking","hearing","pushing"],["撮ること（take の -ing 形）","話すこと","聞くこと","押すこと"],1,
     "take pictures で『写真を撮る』。like ～ing で『～するのが好きだ』なので、likes taking pictures（写真を撮るのが好きだ）となる。誕生日にカメラをもらったという1文目ともつながる。speaking・hearing・pushing は pictures と組み合わせても『写真を撮る』の意味にならない。",
     "カメラでともだちのしゃしんをとるのがすきなんだね。take pictures は『しゃしんをとる』だよ。",
     ["taking pictures で『写真を撮ること』。カメラの話とつながる。","写真を話す、では意味が通らない。","写真を聞く、では意味が通らない。","写真を押す、では意味が通らない。"],
     ["しゃしんをとるのがすきなんだね。","はなす、ではないよ。","きく、ではないよ。","おす、ではないよ。"]),
    ("A: How many (　) do you go to the library every month?\nB: Usually once or twice.",
     "A：毎月、何 (　) 図書館へ行きますか。\nB：たいてい1回か2回です。",
     ["tools","leaves","times","shakes"],["道具","葉（leaf の複数形）","回・度（time の複数形）","振ること・シェイク"],3,
     "How many times ～? で『何回～』と回数を尋ねる。B の once or twice（1回か2回）は回数の答え。time は『回・度』の意味では数えられる名詞なので、How many の後ろで times と複数形になる。tools・leaves・shakes では、図書館へ行く回数を尋ねられない。",
     "『まいつき、なんかいとしょかんにいく？』『1かいか2かい』。How many times は『なんかい』だよ。",
     ["道具の数を尋ねても、once or twice とつながらない。","葉の数を尋ねても、図書館へ行く話にならない。","How many times で回数を尋ね、once or twice と答えている。","shakes では、図書館へ行く回数を尋ねられない。"],
     ["どうぐのかずではないよ。","はっぱのかずではないよ。","なんかいいくか、きいているね。","shakes では、かいすうをきけないよ。"]),
    ("A: What time is the next train, Sandy?\nB: I don't know. I'm going to (　) at the ticket office now.",
     "A：サンディ、次の電車は何時？\nB：わからない。今から切符売り場で (　) つもりだよ。",
     ["checked","checks","check","checking"],["確かめた（過去形）","確かめる（三人称単数現在）","確かめる（原形）","確かめている（-ing形）"],3,
     "be going to＋動詞の原形で『～するつもりだ』。I'm going to の to の後ろは原形なので check。次の電車の時刻がわからないので、今から切符売り場で確かめると言っている。checked（過去形）・checks（三人称単数現在）・checking（-ing形）は be going to の後ろには置かない。",
     "be going to のあとは、もとのかたちの check だよ。『いまからしらべてくるね』といっているね。",
     ["be going to の後ろに過去形は置かない。","be going to の後ろに s のついた形は置かない。","be going to＋原形で『確かめるつもりだ』。","be going to の後ろに -ing 形は置かない。"],
     ["むかしのかたちは、つかわないよ。","s のついたかたちは、つかわないよ。","もとのかたちの check だね。","ing のかたちは、つかわないよ。"]),
    ("Jane is a (　) tennis player than Kevin. Kevin never wins when they play together.",
     "ジェーンはケビンより (　) テニス選手です。2人が一緒にプレーすると、ケビンは一度も勝てません。",
     ["well","best","good","better"],["上手に","最もよい（good の最上級）","よい・上手な","よりよい（good の比較級）"],4,
     "than（～より）があるので比較級が入る。good の比較級は better で、-er をつけずに形が変わる。a better tennis player than Kevin で『ケビンより上手なテニス選手』。2文目の『ケビンは一度も勝てない』とも合う。best は最上級で、than とは組み合わせない。good はそのままの形で、than と使えない。well は『上手に』と動作を説明する語で、a ～ tennis player の形に入らない。",
     "than『～より』があるから、better『よりじょうずな』をえらぶよ。good → better → best とかわるね。",
     ["『上手に』と動作を説明する語で、a ～ tennis player の形にならない。","best は最上級で、than とは組み合わせない。","good のままでは、than とつながらない。","than Kevin と比べ、good の比較級 better を使う。"],
     ["well は『じょうずに』で、ここにはいらないよ。","best は『いちばん』だよ。","than があるから、good のままではだめだよ。","『よりじょうずな』で better だね。"]),
    ("A: Can you help (　)? I want to carry this box into the house. It's very heavy!\nB: Sure.",
     "A：(　) を手伝ってくれる？ この箱を家の中に運びたいんだ。とても重いんだよ！\nB：いいよ。",
     ["I","my","mine","me"],["私は","私の","私のもの","私を・私に"],4,
     "help＋人で『人を手伝う』。help の後ろに手伝う相手を置くときは『～を』の形（目的格）にするので me。Can you help me? で『手伝ってくれる？』。I は主語に使う形、my は後ろに名詞が必要な形、mine は『私のもの』という意味で、手伝う相手を表せない。",
     "help のあとは『わたしを』の me だよ。『てつだってくれる？』とたのんでいるね。",
     ["I は主語に使う形で、help の後ろには置かない。","my は後ろに名詞が必要で、ここでは使えない。","『私のもの』という意味で、手伝う相手を表せない。","help me で『私を手伝う』。"],
     ["I は『わたしは』だよ。","my は『わたしの』だよ。","mine は『わたしのもの』だよ。","『わたしを』の me だね。"]),
    ("Boy: You have a pet, right?\nGirl: (　) He's white and gray.",
     "男の子：ペットを飼っているよね？\n女の子：(　) 白と灰色なの。",
     ["Yes, I'll think about it.","Yes, I have a cat.","No, you can't have any.","No, you won't."],
     ["うん、考えておくね。","うん、ネコを飼っているよ。","ううん、あなたは1つも持てないよ。","ううん、あなたはそうしないよ。"],2,
     "～, right? は『～だよね？』と確かめる言い方。空所の後ろの He's white and gray.（白と灰色だよ）の He は飼っているペットを指すので、Yes, I have a cat.（ネコを飼っている）が合う。I'll think about it. は誘いや提案への返事。No, you can't have any. は Can I have ～? のような頼みへの返事、No, you won't. は Will I ～? のような質問への返事で、どちらもペットを飼っているかの答えにならない。",
     "『ペットをかってるよね？』『うん、ネコをかってるよ。しろとはいいろなの』。He はネコのことだよ。",
     ["考えておく、は提案などへの返事で、ペットの色の説明につながらない。","ネコを飼っていると答え、He's white and gray. でその色を説明している。","Can I have ～? のような頼みへの返事で、ペットを飼っているかの答えにならない。","Will I ～? のような質問への返事で、ペットを飼っているかの答えにならない。"],
     ["かんがえておく、ではないよ。","ネコをかっているんだね。","ううん、だといろのはなしにつながらないよ。","このしつもんのこたえではないよ。"]),
    ("Student: Excuse me, Mr. Brown. (　)\nTeacher: Sure. What is it?\nStudent: I want to ask you about our homework.",
     "生徒：すみません、ブラウン先生。(　)\n先生：いいですよ。何ですか。\n生徒：宿題についてお聞きしたいのです。",
     ["Do you know that?","Where do you live?","May I talk to you?","Whose book is it?"],
     ["それを知っていますか。","どこに住んでいますか。","お話ししてもいいですか。","それはだれの本ですか。"],3,
     "May I ～? は『～してもいいですか』と丁寧に許可を求める言い方。先生が Sure.（いいですよ）と答えて What is it?（何ですか）と用件を尋ね、生徒が宿題について聞きたいと続けている。Where do you live? や Whose book is it? には Sure. では答えられない。Do you know that? の that が指すものもない。",
     "『おはなししてもいいですか？』『いいですよ。なんですか？』とつづくね。May I ～? は『～してもいいですか』だよ。",
     ["that が指すものがなく、What is it? ともつながらない。","住んでいる場所を聞かれたら、場所を答える。","話してもいいかと尋ね、先生が Sure. What is it? と答えている。","だれの本かを聞かれたら、持ち主を答える。"],
     ["that がなにか、わからないよ。","すんでいるところをきいているのではないよ。","はなしてもいいか、きいているね。","だれのほんか、ではないよ。"]),
    ("Girl 1: I like your socks. They're so cute.\nGirl 2: Thanks. (　)",
     "女の子1：あなたの靴下、いいね。とてもかわいい。\n女の子2：ありがとう。(　)",
     ["You have one, too.","I forgot them.","My mother said it.","They were a present."],
     ["あなたも1つ持っているよ。","それを忘れたの。","母がそれを言ったの。","それはプレゼントだったの。"],4,
     "靴下をほめられて Thanks. とお礼を言い、その靴下について話を続けている。They は your socks（あなたの靴下）を指し、They were a present.（プレゼントだった）が自然。I forgot them. だと、今はいている靴下の話と合わない。You have one, too. や My mother said it. では、ほめられたことへの返事にならない。",
     "くつしたをほめられて『ありがとう。プレゼントだったの』とこたえているよ。They はくつしたのことだね。",
     ["ほめられた返事として、相手も持っていると言うのは合わない。","今はいている靴下を忘れた、では話が合わない。","it が指すものがはっきりせず、ほめられた返事にならない。","They＝靴下がプレゼントだったと説明している。"],
     ["あなたももっている、ではないよ。","わすれた、ではあわないよ。","おかあさんがいった、ではないよ。","プレゼントだったんだね。"]),
    ("Son: Can I put these teacups here, Mom?\nMother: Sure, Tom, but (　)",
     "息子：お母さん、このティーカップをここに置いてもいい？\n母：いいわよ、トム。でも (　)",
     ["they are.","I'm reading.","be careful.","in the car."],
     ["それらはそうです。","私は読書中です。","気をつけてね。","車の中で。"],3,
     "Can I ～? と許可を求められ、母は Sure（いいわよ）と認めたうえで、but（でも）と注意を加えている。ティーカップは割れやすいので be careful（気をつけて）が合う。Be careful. は be で始まる命令文。they are. や in the car. では意味が通らず、I'm reading. では注意にならない。",
     "『ここにおいてもいい？』『いいわよ。でもきをつけてね』。カップはわれやすいからね。be careful は『きをつけて』だよ。",
     ["they are. では何がそうなのかわからず、意味が通らない。","読書中だと言っても、but の後ろの注意にならない。","Sure の後ろに but で注意を加えている。","車の中で、ではティーカップを置く話とつながらない。"],
     ["いみがつながらないよ。","よんでいる、ではないよ。","きをつけてね、だね。","くるまのなか、ではないよ。"]),
    ("Father: Good morning, Paul. (　)\nSon: I'm not hungry. I just want a glass of juice.",
     "父：おはよう、ポール。(　)\n息子：おなかはすいていないんだ。ジュースを1杯だけほしいな。",
     ["What would you like for breakfast?","What did you buy at the store?","How much was that cup?","How will you go to school today?"],
     ["朝食に何が食べたい？","お店で何を買ったの？","そのカップはいくらだった？","今日はどうやって学校へ行くの？"],1,
     "What would you like for ～? は『～に何がほしいですか』と希望を尋ねる言い方。息子が I'm not hungry.（おなかはすいていない）と言い、ジュースだけほしいと答えているので、朝食に何を食べたいかを尋ねる質問が合う。Good morning から朝の場面とわかる。買った物・値段・通学方法の質問では、おなかがすいていないという答えとつながらない。",
     "『あさごはん、なにがいい？』『おなかはすいてないよ。ジュースだけ』。What would you like は『なにがほしい？』だよ。",
     ["朝食の希望を尋ね、ジュースだけほしいと答えている。","買った物を聞かれたら、買った物を答える。","値段を聞かれたら、金額を答える。","通学方法を聞かれたら、行き方を答える。"],
     ["あさごはんのはなしだね。","かったもの、ではないよ。","ねだん、ではないよ。","がっこうへのいきかた、ではないよ。"]),
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
    listening=[3,1,2,3,1,2,3,1,3,1,1,2,2,4,1,1,2,4,1,4,4,1,3,4,1,4,2,2,3,3]
    return dict(grade="grade4",year="2024",session="2024-2-sat",exam="2024-2-sat",
                title="英検4級 2024年度 第2回（土曜準会場）",sections=sections,
                listening={f"part{i+1}":dict(zip(map(str,range(10*i+1,10*i+11)),listening[10*i:10*i+10])) for i in range(3)},
                vocabulary=m.vocabulary(),lessonPlan=m.lessonplan(sections))


if __name__=="__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(build(),ensure_ascii=False,indent=4)+"\n",encoding="utf-8")
    print(OUT)

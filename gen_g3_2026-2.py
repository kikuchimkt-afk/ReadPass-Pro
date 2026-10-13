# -*- coding: utf-8 -*-
"""Grade 3 2026-2 (main venue, October 4); booklet text layer pp. 2-11, official key."""
import importlib.util
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parent
OUT=ROOT/"data/grade3/2026-2/data.json"

def module(suffix):
    spec=importlib.util.spec_from_file_location(suffix,ROOT/f"gen_g3_2026-2_{suffix}.py")
    result=importlib.util.module_from_spec(spec);spec.loader.exec_module(result)
    return result

# Original question/options, translations, normal/easy grammar and
# option-specific explanations. The existing Grade 3 format has no question TTS.
ROWS=[
    ("Many people in Japan enjoy seeing (　) in spring. They often have parties under the trees with their friends.",
     "日本の多くの人々は、春に (　) を見るのを楽しみます。彼らはよく友達と木の下でパーティーをします。",
     ["blossoms","memories","stones","pages"],["（木の）花","思い出","石","ページ"],1,
     "blossom は果樹などの木に咲く花。2文目の『木の下で友達とパーティーをする』から、春の花見の場面だと分かる。enjoy は後ろに動名詞を取り、enjoy seeing で『見るのを楽しむ』。under the trees が木の花を選ぶ手がかり。",
     "はるに、きのしたでパーティーをするのは、おはなみだね。blossoms は『きにさくはな』。enjoy seeing は『みるのをたのしむ』だよ。",
     ["春に木の下で楽しむ花見の場面に合う。","思い出を見に行くという場面ではない。","石を見ても、木の下のパーティーにつながらない。","ページは本の一部で、春の木の下の場面に合わない。"],
     ["はるにさく、きのはなだね。","おもいでをみにいくのではないよ。","いしをみるおはなしではないよ。","ほんのページではないよ。"]),
    ("These days, there are some people who use a delivery (　) because they do not have time to go shopping.",
     "最近では、買い物に行く時間がないため、配達 (　) を利用する人がいます。",
     ["type","hope","service","chance"],["型・種類","希望","サービス","機会"],3,
     "delivery service は『配達サービス』。買い物に行く時間がない人が、品物を届けてもらうために利用するもの。use a delivery service で『配達サービスを利用する』。who 以下が some people を説明している。",
     "かいものにいくじかんがないから、とどけてもらうんだね。delivery service は『はいたつサービス』。use は『つかう・りようする』だよ。",
     ["配達の型を利用するでは、意味が通らない。","配達の希望を利用するとは言わない。","配達サービスを使えば、買い物に行かずに済む。","配達の機会を利用するでは、文脈に合わない。"],
     ["しゅるい、ではつながらないよ。","きぼうをつかうのではないよ。","はいたつサービスをつかうんだね。","チャンスをつかうのではないよ。"]),
    ("A: Why are you going to Canada?\nB: I'm going to (　) my English skills.",
     "A：なぜカナダへ行くのですか。\nB：英語力を (　) つもりです。",
     ["hurry","break","improve","cover"],["急ぐ","壊す","向上させる","覆う"],3,
     "improve は『向上させる』で、improve my English skills は『英語力を伸ばす』。カナダへ行く理由を聞かれ、英語力を伸ばすつもりだと答えている。be going to＋原形は『～するつもりだ』。break（壊す）は目的に合わない。",
     "カナダへいくのは、えいごをもっとじょうずにするためだね。improve は『よくする・のばす』。I'm going to は『～するつもり』だよ。",
     ["急ぐという意味では、英語力の話につながらない。","英語力を壊すことは、カナダへ行く目的にならない。","英語力を伸ばすことがカナダへ行く理由になる。","英語力を覆うという意味にはならない。"],
     ["いそぐ、ではつながらないよ。","えいごのちからをこわすのではないよ。","えいごをじょうずにするんだね。","なにかをおおうことではないよ。"]),
    ("In English class, the students had to write a short essay with five (　).",
     "英語の授業で、生徒たちは5つの (　) で短い作文を書かなければなりませんでした。",
     ["fireworks","sentences","memories","tournaments"],["花火","文","思い出","トーナメント・大会"],2,
     "sentence は『文』。英語の授業で短い作文（essay）を書く場面なので、作文の長さを表す five sentences（5つの文）が合う。had to＋原形は『～しなければならなかった』で、have to の過去形。",
     "えいごのじゅぎょうで、みじかいさくぶんをかいたんだね。sentence は『ぶん』。five sentences で『5つのぶん』だよ。",
     ["花火は作文を組み立てるものではない。","作文は文で書くので、5つの文が合う。","5つの思い出では、作文の長さを表せない。","大会の数は、作文の内容と関係がない。"],
     ["はなびではさくぶんはかけないよ。","5つのぶんでかくんだね。","おもいでのかずではないよ。","しあいのかずではないよ。"]),
    ("Jack likes to buy (　) food at the market because it is fresh and not expensive.",
     "ジャックは、新鮮で高くないので、市場で (　) 食べ物を買うのが好きです。",
     ["silent","local","weak","large"],["静かな","地元の","弱い","大きい"],2,
     "local は『地元の・その土地の』で、local food は『地元産の食べ物』。because 以下の『新鮮で高くない』が、地元産の食べ物を選ぶ理由として自然につながる。like to＋原形は『～するのが好きだ』。it は前の food を指す。",
     "しんせんで、たかくないから、じもとのたべものをかうんだね。local は『じもとの』。it は、そのたべもののことだよ。",
     ["静かな食べ物では、新鮮で安い理由にならない。","新鮮で安い地元の食べ物を買う理由に合う。","弱い食べ物という表現は意味が通らない。","大きさは、新鮮で高くない理由と関係がない。"],
     ["しずかなたべもの、とはいわないよ。","じもとのたべものをかうんだね。","よわいたべもの、ではないよ。","おおきさのおはなしではないよ。"]),
    ("Wearing helmets helps people to (　) their heads when they are skiing.",
     "ヘルメットをかぶることは、スキーをしているときに頭を (　) のに役立ちます。",
     ["invite","spend","protect","follow"],["招待する","費やす","守る","ついて行く・従う"],3,
     "protect their heads は『頭を守る』で、ヘルメットをかぶる目的に合う。help 人 to＋原形は『人が～するのに役立つ』。主語は動名詞の Wearing helmets で、単数扱いなので helps となる。",
     "ヘルメットは、スキーのときにあたまをまもるものだね。protect は『まもる』。Wearing helmets は『ヘルメットをかぶること』だよ。",
     ["頭を招待するという意味にはならない。","頭を費やすという表現は成り立たない。","ヘルメットは頭を守るためにかぶる。","頭について行くという意味では通じない。"],
     ["あたまをしょうたいするのではないよ。","じかんやおかねをつかうことではないよ。","ヘルメットであたまをまもるんだね。","あたまについていくのではないよ。"]),
    ("A: Why did you move away from the city?\nB: My husband and I love nature, so we live (　) a small river in the mountains.",
     "A：なぜ都会から引っ越したのですか。\nB：夫も私も自然が大好きなので、山の中の小さな川 (　) 住んでいます。",
     ["until","about","from","by"],["～まで","～について","～から","～のそばに"],4,
     "by＋場所は『～のそばに』で、live by a small river は『小さな川のそばに住む』。自然が好きだから都会を離れ、山の中の川のそばで暮らしているという流れ。until は時の期限、about は話題を表すので、住む場所を示せない。",
     "しぜんがすきだから、やまのなかのかわのそばにすんでいるんだね。by は『～のそばに』。by a river で『かわのそば』だよ。",
     ["until は時の期限で、住む場所を表さない。","about は話題を表し、住む場所には使わない。","from は出発点で、川から住むとは言わない。","川のそばに住むという場所を表す。"],
     ["いつまで、ということではないよ。","～について、ではないよ。","～から、ではつながらないよ。","かわのそばにすんでいるんだね。"]),
    ("Misa won a silver medal in a big piano competition. Her parents were very (　) of her.",
     "ミサは大きなピアノコンクールで銀メダルを取りました。両親は彼女をとても (　) 思いました。",
     ["warm","funny","safe","proud"],["暖かい","おかしい","安全な","誇りに思って"],4,
     "be proud of 人は『人を誇りに思う』。娘が大きなコンクールで銀メダルを取ったので、両親が誇らしく思うのは自然。of her の of と結びつく形容詞を選ぶ。warm や safe は of と組んでも『～を誇りに思う』の意味にならない。",
     "ミサがぎんメダルをとって、りょうしんはほこらしいきもちだね。be proud of は『～をほこりにおもう』。of とセットでおぼえよう。",
     ["暖かいでは、メダルを取った娘への気持ちを表せない。","おかしいでは、喜びや誇りの気持ちに合わない。","安全なは、娘の受賞への気持ちではない。","be proud of で娘を誇りに思う気持ちを表す。"],
     ["あたたかい、ではないよ。","おもしろい、ではつながらないよ。","あんぜん、ではないよ。","ミサをほこりにおもっているね。"]),
    ("A: Is that your new friend, Kate?\nB: Yes. Let's show him (　) our town.",
     "A：ケイト、あれはあなたの新しい友達ですか。\nB：ええ。彼に私たちの町を (　) しましょう。",
     ["around","up","off","of"],["～のあちこちを","上へ","離れて","～の"],1,
     "show 人 around 場所は『人に場所を案内して回る』。Kate の新しい友達に自分たちの町を案内しようと提案している。Let's＋原形は『～しよう』という誘い。him は Kate の新しい友達を指す。up や off では町を案内する意味にならない。",
     "ケイトのあたらしいともだちに、まちをあんないしようといっているよ。show him around は『かれをあんないする』。him はそのともだちだね。",
     ["show 人 around 場所で町を案内して回る意味になる。","show him up our town では案内の意味にならない。","off は離れる意味で、町の案内にならない。","show him of our town という言い方はしない。"],
     ["まちをあんないしてまわるんだね。","うえへ、ではつながらないよ。","はなれて、ではないよ。","～の、ではあんないにならないよ。"]),
    ("A: Are you enjoying this book, Kevin?\nB: No, Mom. I'm (　) of reading it.",
     "A：ケビン、この本を楽しんでいますか。\nB：いいえ、お母さん。それを読むのには (　) います。",
     ["happy","tired","sleepy","sorry"],["うれしい","飽きて・うんざりして","眠い","残念に思って・すまなく思って"],2,
     "be tired of ～ing は『～するのに飽きている・うんざりしている』。本を楽しんでいるかと聞かれ No と答えているので、読むのに飽きたという内容が合う。of の後ろは動名詞 reading。happy は No という返答と矛盾する。",
     "ほんをたのしんでいないから、よむのにあきているんだね。be tired of は『～にあきている』。of のあとは reading の形だよ。",
     ["No と答えているので、うれしいでは矛盾する。","No に続き、読むのに飽きたと伝えている。","眠いは of と組んで飽きたの意味にならない。","sorry は for と組むことが多く、文脈にも合わない。"],
     ["たのしくないので、うれしいではないよ。","よむのにあきているんだね。","ねむい、ではつながらないよ。","あやまるばめんではないよ。"]),
    ("A: Are you (　) for your piano concert, Paula?\nB: Yes. I practiced for three hours every day this week.",
     "A：ポーラ、ピアノの演奏会の (　) はできていますか。\nB：はい。今週は毎日3時間練習しました。",
     ["late","ready","near","dark"],["遅れた","準備ができた","近い","暗い"],2,
     "be ready for＋名詞は『～の準備ができている』。演奏会について尋ね、今週は毎日3時間練習したと答えているので、準備ができているかを確認する文になる。late for は『～に遅れる』で、練習の話とつながらない。",
     "えんそうかいのじゅんびができているか、きいているよ。be ready for は『～のじゅんびができている』。まいにち3じかんもれんしゅうしたんだね。",
     ["遅れるかを聞くと、練習した答えにつながらない。","準備ができたかを聞き、練習したと答えている。","近いでは、演奏会への準備を尋ねられない。","暗いは、演奏会への準備と関係がない。"],
     ["おくれる、ではつながらないよ。","じゅんびができているかきいているね。","ちかい、ではないよ。","くらい、ではないよ。"]),
    ("The bike race was long and difficult, but most people didn't (　) up. They were very happy when they finished the race.",
     "その自転車レースは長くて大変でしたが、ほとんどの人は (　) ませんでした。レースを走り終えたとき、彼らはとても喜びました。",
     ["take","find","give","begin"],["取る","見つける","与える（give upであきらめる）","始める"],3,
     "give up は『あきらめる』。レースは長くて大変だったが（but）、ほとんどの人はあきらめず、走り終えて喜んだという流れ。didn't の後ろは原形 give。take up は『取り上げる・始める』で、この流れに合わない。",
     "レースはたいへんだったけど、ほとんどのひとがあきらめなかったんだね。give up は『あきらめる』。but は『でも』だよ。",
     ["take up は取り上げる・始める意味で、流れに合わない。","find up という決まった言い方はない。","give up で、大変でもあきらめなかったと表す。","begin up という言い方はなく、意味も通らない。"],
     ["take up ではつながらないよ。","find up とはいわないよ。","give up で『あきらめる』だね。","begin up とはいわないよ。"]),
    ("A: Keiko, I think it's important for us (　) volunteer work.\nB: Yes, I think so, too. I'd like to work at the hospital.",
     "A：ケイコ、私たちがボランティア活動を (　) ことは大切だと思います。\nB：ええ、私もそう思います。病院で働きたいです。",
     ["did","to do","do","does"],["した（過去形）","すること（to不定詞）","する（原形）","する（三人称単数形）"],2,
     "It is ～ for 人 to＋原形は『人が…することは～だ』。it は形式主語で、to do volunteer work が本当の主語。for us は to do の意味上の主語を示す。動詞の過去形や原形だけでは、この構文の主語になれない。",
     "『わたしたちがボランティアをすることはたいせつ』という文だね。It's important for us to do で『～することはたいせつ』。to のあとはもとの形だよ。",
     ["過去形 did では、it の内容を示す形にならない。","for us to do で私たちがすることを表す。","原形 do だけでは、it の内容を示せない。","does は三人称単数現在形で、この形に合わない。"],
     ["did では、このセットにならないよ。","to do で『すること』だね。","do だけでは、つながらないよ。","does では、このセットにならないよ。"]),
    ("At the top of the mountain, it was much (　) than at the bottom.",
     "山の頂上では、ふもとよりもずっと (　)。",
     ["cooler","cool","coolest","too cool"],["より涼しい","涼しい","最も涼しい","涼しすぎる"],1,
     "than at the bottom があるので、cool の比較級 cooler を選ぶ。much は比較級の前に置いて『ずっと・はるかに』と差を強める。山の頂上とふもとの気温を比べている。coolest は最上級で、than と組まない。",
     "やまのうえは、ふもとより、ずっとすずしいんだね。than があるので cooler をえらぶよ。much は『ずっと』と、ちがいをつよめるね。",
     ["than を伴う比較で、比較級 cooler が合う。","原級 cool は much ～ than の形に合わない。","最上級 coolest は than とつながらない。","too cool は比較級ではなく、than に合わない。"],
     ["cooler than で『～よりすずしい』だね。","くらべるので、cool のままではないよ。","いちばん、の形ではないよ。","すずしすぎる、ではくらべられないよ。"]),
    ("A: Look over there! That man is a famous Korean actor, (　) he?\nB: You're right.",
     "A：あそこを見て！あの男の人は有名な韓国の俳優です (　)。\nB：その通りです。",
     ["doesn't","won't","isn't","aren't"],["does not の短縮形","will not の短縮形","is not の短縮形","are not の短縮形"],3,
     "文末の『, 否定の短縮形＋代名詞?』は付加疑問文で『～ですよね』と確認する。前の文は be動詞 is を使った肯定文なので、否定の形 isn't he? とする。主語 he は That man を受け、3人称単数なので aren't は使わない。",
     "『あのひとは、ゆうめいなはいゆうですよね』とたしかめているよ。まえの文に is があるから、isn't he? になるね。",
     ["一般動詞の文ではないので doesn't は使わない。","未来の will の文ではないので won't は合わない。","is の肯定文なので isn't he? で確かめる。","主語 he は単数なので aren't は使わない。"],
     ["is の文なので、doesn't ではないよ。","will の文ではないよ。","is の文だから isn't だね。","he には aren't をつかわないよ。"]),
    ("Woman 1: Wow! This is a really nice apartment. (　)\nWoman 2: I moved here last summer.",
     "女性1：わあ！本当にすてきなアパートですね。(　)\n女性2：去年の夏にここへ引っ越してきました。",
     ["Where did you live before?","How long have you lived here?","Why is it so hot?","How often do you clean it?"],
     ["以前はどこに住んでいたのですか","ここにどのくらい住んでいるのですか","なぜこんなに暑いのですか","どのくらいの頻度で掃除するのですか"],2,
     "How long have you lived here? は現在完了（継続）で、住んでいる期間を尋ねる。女性2は I moved here last summer と越してきた時期を示し、住んでいる期間を伝えている。Where は以前の住所を聞く表現。",
     "『ここにどれくらいすんでいるの？』ときいているよ。こたえは『きょねんのなつにひっこしてきた』。How long は『どのくらいのあいだ』だね。",
     ["以前の住所を聞いており、引っ越した時期の答えと合わない。","住んでいる期間を聞き、越してきた時期で答えている。","暑さの理由を聞いても、引っ越しの答えにならない。","掃除の頻度には、引っ越した時期で答えない。"],
     ["まえにすんでいたばしょではないよ。","どのくらいすんでいるかきいているね。","あつさのりゆうではないよ。","そうじのかいすうではないよ。"]),
    ("Mother: How do you like your Chinese history class, Bobby?\nSon: It's really interesting. (　)",
     "母：ボビー、中国史の授業はどうですか。\n息子：本当におもしろいです。(　)",
     ["I hope you do.","I want to take a class.","I'm learning a lot.","I'm glad you like it."],
     ["あなたがそうするといいですね","授業を受けたいです","たくさんのことを学んでいます","気に入ってくれてうれしいです"],3,
     "How do you like ～? は『～はどうですか』と感想を尋ねる表現。息子は授業が本当におもしろいと答え、続けて I'm learning a lot（たくさん学んでいる）と前向きな感想を加えている。現在進行形で、今学んでいる最中であることを表す。",
     "ちゅうごくのれきしのじゅぎょうは、おもしろいんだね。I'm learning a lot. は『たくさんまなんでいる』。たのしいかんそうをつけたしているよ。",
     ["相手の行動を願う表現で、授業の感想に合わない。","すでに授業を受けているので、受けたいは合わない。","おもしろい授業で多くを学んでいると感想を加えている。","相手が気に入ったことを喜ぶ言葉で、息子の感想ではない。"],
     ["あいてにねがうことばではないよ。","もうじゅぎょうをうけているね。","たくさんまなんでいるんだね。","じぶんのかんそうではないよ。"]),
    ("Father: Henry, why is there a plate on the sofa?\nSon: I don't know. (　) but I'll take it to the kitchen.\nFather: Thanks.",
     "父：ヘンリー、どうしてソファの上にお皿があるのですか。\n息子：分かりません。(　) でも、台所に持って行きます。\n父：ありがとう。",
     ["I forgot to go,","I'll look in my bedroom,","I'm good at cooking,","It's not mine,"],
     ["行くのを忘れました","寝室を探します","料理が得意です","私のものではありません"],4,
     "皿がソファにある理由を聞かれ、息子は I don't know と答える。続けて It's not mine（自分のものではない）と言い、but で『それでも台所へ持って行く』とつなぐ。自分の皿ではないが片付けるという逆接の流れ。",
     "おさらはじぶんのものではないけど、だいどころへもっていくんだね。It's not mine は『ぼくのじゃない』。but は『でも』だよ。",
     ["行くのを忘れた話は、皿がある理由と関係がない。","寝室を探すことは、皿を台所へ運ぶ話に合わない。","料理が得意なことは、皿がある理由に答えない。","自分の皿ではないが片付けると but でつなぐ。"],
     ["いくのをわすれたはなしではないよ。","しんしつをさがすのではないよ。","りょうりのとくいさではないよ。","じぶんのではないけど、はこぶんだね。"]),
    ("Boy 1: Did you hear that Kazu broke his leg in the soccer game?\nBoy 2: No, I didn't. How is he?\nBoy 1: (　) She'll know.",
     "男の子1：カズがサッカーの試合で脚を骨折したと聞きましたか。\n男の子2：いいえ、聞いていません。彼の具合はどうですか。\n男の子1：(　) 彼女なら知っているでしょう。",
     ["Let's call and ask his sister.","He's the best player.","Let's go and visit him.","He's at the hospital now."],
     ["彼の姉（妹）に電話して聞いてみましょう","彼は一番の選手です","彼のお見舞いに行きましょう","彼は今、病院にいます"],1,
     "How is he? と様子を聞かれ、男の子1は『彼の姉（妹）に電話して聞こう』と提案する。直後の She'll know の She は his sister を指し、彼女なら知っているはずだという流れ。他の選択肢には She が指す女性が出てこない。",
     "カズのようすは、カズのおねえさんかいもうとにきこうといっているよ。つぎの She は、その sister のことだね。",
     ["She が指す姉（妹）が登場し、次の文とつながる。","一番の選手という話では、She が誰か分からない。","見舞いの提案では、She'll know とつながらない。","病院にいると答えると、She が誰か分からない。"],
     ["おねえさんかいもうとにきくんだね。","いちばんのせんしゅ、ではないよ。","She がだれかわからなくなるよ。","びょういんにいる、ではつながらないよ。"]),
    ("Girl: I have a lot of DVDs.\nBoy: Really? (　)\nGirl: Of course. Come to my house after school.",
     "女の子：私はDVDをたくさん持っています。\n男の子：本当ですか。(　)\n女の子：もちろん。放課後に私の家に来てください。",
     ["Is the DVD store open?","Will you lend me some?","Did you go to the concert?","Do you work here?"],
     ["DVD店は開いていますか","いくつか貸してくれますか","コンサートに行きましたか","ここで働いているのですか"],2,
     "lend 人 物は『人に物を貸す』。Will you ～? は依頼の表現で、some は some DVDs を表す。女の子が Of course と承諾し、放課後に家に来るよう言っているので、DVDを貸してほしいという依頼が合う。",
     "DVDをたくさんもっている女の子に、かしてとたのんでいるよ。lend me some は『いくつかかして』。some は DVD のことだね。",
     ["店が開いているかは、女の子の家に来る話と合わない。","DVDを貸してと頼み、家に来てと承諾されている。","コンサートの話は、DVDを持っていることと関係がない。","ここで働いているかを聞く場面ではない。"],
     ["おみせのことではないよ。","DVDをかしてとたのんでいるね。","コンサートのおはなしではないよ。","しごとのことではないよ。"]),
]

WRITING={
    "section4":dict(type="email-reply",title="ライティング（Eメール）",prompt={},
                    sampleAnswer="I get on the bus at seven in the morning. It takes thirty minutes to go to school. I usually study on the bus."),
    "section5":dict(type="composition",title="ライティング（英作文）",question="What is your dream for the future?",
                    sampleAnswer="My dream for the future is to travel around the world. I have two reasons. First, I want to visit famous places in many countries. Second, I like meeting people from different cultures.")
}
WRITING["section4"]["prompt"]={"from":"James","body":"Hi,\nThank you for your e-mail.\nMy brother tells me that you go to school by bus. I have some questions for you. What time do you get on the bus? And how long does it take you to go to school?\nYour friend,\nJames"}

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
    listening=[2,1,3,3,1,3,2,1,3,2,1,2,4,4,3,1,3,1,1,2,2,1,2,2,1,3,2,2,3,3]
    return dict(grade="grade3",year="2026",session="2026-2",exam="2026-2",title="英検3級 2026年度 第2回",
                sections=sections,writing=WRITING,listening={f"part{i+1}":dict(zip(map(str,range(i*10+1,i*10+11)),listening[i*10:i*10+10])) for i in range(3)},
                vocabulary=m.vocabulary(),lessonPlan=m.lessonplan(sections))

if __name__=="__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(build(),ensure_ascii=False,indent=4)+"\n",encoding="utf-8")
    print(OUT)

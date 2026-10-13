# -*- coding: utf-8 -*-
"""Grade 4 2026-2 (main venue, October 4); booklet text layer pp. 2-11, official key."""
import importlib.util
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "data/grade4/2026-2/data.json"


def module(suffix):
    spec=importlib.util.spec_from_file_location(suffix,ROOT/f"gen_g4_2026-2_{suffix}.py")
    result=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


# stem, translation, choices, meanings, answer, normal/simple grammar,
# choice-specific reasons. All four normal/simple analyses retain meanings.
ROWS = [
    ("A: Are you in a rock (　)?\nB: Yes, I play the guitar.",
     "A：あなたはロック (　) に入っていますか。\nB：はい、ギターを弾いています。",
     ["band","top","time","part"],["バンド","頂上・一番上","時間・時刻","部分・役"],1,
     "rock band は『ロックバンド』。be in a band で『バンドに入っている』。B の I play the guitar.（ギターを弾いている）もヒントになる。top・time・part では、入っている音楽グループを表せない。",
     "『ギターをひいているよ』とこたえているね。rock band は『ロックバンド』。バンドにはいっているか、きいているんだよ。",
     ["rock band で、所属している音楽グループを表す。","頂上や一番上は、入るグループではない。","時間に入っているという意味にはならない。","部分や役では、ギターを弾く集団を表せない。"],
     ["ロックバンドにはいっているんだね。","いちばんうえのことではないよ。","じかんのことではないよ。","ぶぶんのことではないよ。"]),
    ("A: How old is your (　) brother?\nB: He's six. He loves to read books.",
     "A：あなたの (　) 兄弟は何歳ですか。\nB：6歳です。本を読むのが大好きです。",
     ["little","long","less","left"],["年下の・小さい","長い","より少ない","左の"],1,
     "little brother は『弟』。B の He's six.（6歳です）からも、年下の兄弟について尋ねていると分かる。long は長さ、less は量の少なさ、left は左を表し、brother の前に置いても意味が通らない。",
     "little brother は『おとうと』のこと。6さいで、ほんをよむのがすきな、としたのきょうだいのことをきいているんだね。",
     ["little brother で『弟』を表す。","長いでは、兄弟がどんな人か表せない。","より少ないは、量を比べるときの語。","左のでは、どの兄弟か表せない。"],
     ["little brother は『おとうと』だね。","ながい、ではないよ。","すくない、ではないよ。","ひだり、ではないよ。"]),
    ("When Tim plays video games, he often (　) to do his homework. His mother is not happy.",
     "ティムはテレビゲームをすると、よく宿題をするのを (　)。お母さんはそれを喜んでいません。",
     ["finds","hears","crosses","forgets"],["見つける","聞く","渡る・横切る","忘れる"],4,
     "forget to＋動詞の原形で『～するのを忘れる』。ゲームをすると宿題をし忘れるので、母親は喜んでいない。主語 he に合わせて forgets となる。find・hear・cross は to do と結び付いてこの意味にならない。",
     "ゲームをすると、しゅくだいをわすれてしまうんだね。forget to は『～するのをわすれる』。だからおかあさんはうれしくないんだよ。",
     ["見つけるでは、宿題をしない話にならない。","聞くでは、宿題をしない理由にならない。","渡る・横切るは宿題とつながらない。","forget to do で、宿題をし忘れることを表す。"],
     ["みつけることではないよ。","きくことではないよ。","わたることではないよ。","しゅくだいをわすれるんだね。"]),
    ("Steve bought a popular (　) about animals. Now, he studies a lot of interesting animal facts.",
     "スティーブは動物についての人気の (　) を買いました。今、彼は動物についての面白い事実をたくさん学んでいます。",
     ["sandwich","mountain","magazine","stadium"],["サンドイッチ","山","雑誌","スタジアム・競技場"],3,
     "about animals（動物について）が内容を表すので、読み物の magazine（雑誌）が合う。その雑誌で動物の面白い事実を学んでいる、という流れになる。サンドイッチ・山・競技場は、動物についての情報が書かれたものではない。",
     "どうぶつのことがかいてある、にんきの『ざっし』をかったんだね。magazine は『ざっし』。よんで、いろいろなことをしったよ。",
     ["サンドイッチから動物の事実は学べない。","山は買うものではなく、内容も書かれていない。","動物についての雑誌で、事実を学んでいる。","競技場は買って読むものではない。"],
     ["たべもののことではないよ。","やまはかうものではないよ。","どうぶつのざっしをかったんだね。","スタジアムはかえないよ。"]),
    ("A: (　) your teeth before you go to bed.\nB: I know, Mom.",
     "A：寝る前に歯を (　) なさい。\nB：分かっているよ、お母さん。",
     ["Follow","Grow","Move","Brush"],["従う・ついて行く","育つ・育てる","動かす・動く","磨く"],4,
     "brush your teeth で『歯を磨く』。動詞の原形で始まる命令文で、寝る前に歯を磨くよう母親が言っている。B の I know, Mom. はその返事。follow・grow・move は teeth と組み合わせても歯磨きの意味にならない。",
     "ねるまえに『はをみがきなさい』といわれているね。brush は『みがく』。brush your teeth で『はをみがく』だよ。",
     ["歯に従うという使い方はしない。","歯を育てるという内容ではない。","歯を動かすでは、寝る前にすることにならない。","brush your teeth で、歯を磨くことを表す。"],
     ["ついていくことではないよ。","そだてることではないよ。","うごかすことではないよ。","ねるまえにはをみがくんだね。"]),
    ("A: Where are you going, Mike?\nB: To the post office. I want to (　) this letter to my uncle. It's his birthday next week.",
     "A：マイク、どこへ行くのですか。\nB：郵便局です。この手紙をおじに (　) たいのです。来週がおじの誕生日なんです。",
     ["send","buy","clean","stop"],["送る","買う","掃除する","止める"],1,
     "post office（郵便局）へ行く目的がヒント。send 物 to 人で『物を人に送る』。おじの誕生日に合わせて手紙を送りたいという流れになる。want to の後ろは動詞の原形。手紙を買う・掃除する・止めるでは意味が通らない。",
     "ゆうびんきょくにいくのは、てがみをおくるためだね。send は『おくる』。send A to B で『AをBにおくる』だよ。",
     ["send ～ to 人 で、手紙をおじに送る。","手紙を買うのでは、郵便局へ行く目的に合わない。","手紙を掃除するという話ではない。","手紙を止めるでは、意味が通らない。"],
     ["てがみをおくるんだね。","てがみをかうのではないよ。","そうじのことではないよ。","とめることではないよ。"]),
    ("Mr. and Mrs. Williams both have jobs, so they do the (　) together on the weekend.",
     "ウィリアムズ夫妻は2人とも仕事をしているので、週末に一緒に (　) をします。",
     ["weather","story","hometown","housework"],["天気","物語","故郷","家事"],4,
     "do the housework で『家事をする』。2人とも仕事をしているので（so）、週末に一緒に家事をするという流れになる。so の後ろはその結果。天気・物語・故郷は、do と組み合わせて行う作業にならない。",
     "ふたりともしごとがあるから、しゅうまつにいっしょに『かじ』をするんだね。do the housework は『かじをする』だよ。",
     ["天気をするという言い方はしない。","物語をするでは意味が通らない。","故郷をするという言い方はしない。","do the housework で、家事をすることを表す。"],
     ["てんきのことではないよ。","おはなしのことではないよ。","ふるさとのことではないよ。","いっしょにかじをするんだね。"]),
    ("A: It's a nice day today.\nB: Yes, it is. Let's (　) a short walk before dinner.",
     "A：今日はいい天気ですね。\nB：ええ、そうですね。夕食の前に少し散歩を (　) ましょう。",
     ["close","take","like","ride"],["閉める","取る・する","好む","乗る"],2,
     "take a walk で『散歩をする』。Let's＋動詞の原形で『～しましょう』と誘う形。天気がよいので、夕食の前に短い散歩をしようという流れになる。close・like・ride は a walk と組み合わせても、散歩をする意味にならない。",
     "いいてんきだから、さんぽにさそっているね。take a walk は『さんぽをする』というセット。take をつかうよ。",
     ["散歩を閉めるという言い方はしない。","take a walk で散歩をすることを表す。","散歩を好もう、という誘い方はしない。","ride は乗り物に乗る語で、散歩には使わない。"],
     ["しめることではないよ。","さんぽをしよう、とさそっているね。","『すき』ではないよ。","のりものにのることではないよ。"]),
    ("A: I'm going to go on a (　) to France this summer.\nB: That's great. You'll have a wonderful time.",
     "A：この夏、フランスへ (　) に行く予定です。\nB：それはいいですね。すばらしい時間を過ごせるでしょう。",
     ["music","trip","present","flower"],["音楽","旅行","贈り物・現在","花"],2,
     "go on a trip to＋場所で『～へ旅行に行く』。to France が行き先を示す。B の You'll have a wonderful time. も旅行への返答として合う。音楽・贈り物・花では go on a ～ の形で出かける内容にならない。",
     "このなつ、フランスへりょこうにいくんだね。trip は『りょこう』。go on a trip で『りょこうにいく』というセットだよ。",
     ["音楽に出かけてフランスへ行くとは言わない。","go on a trip to France で旅行に行く。","贈り物に出かけるという形にはならない。","花に出かけるでは、意味が通らない。"],
     ["おんがくではないよ。","フランスへりょこうにいくんだね。","プレゼントではないよ。","おはなのことではないよ。"]),
    ("A: Do you want to play tennis today?\nB: Yes. I can play (　) the afternoon.",
     "A：今日テニスをしたいですか。\nB：はい。午後 (　) できます。",
     ["in","on","at","to"],["～に・～の中で","～の上に・～に","～に（時刻）","～へ"],1,
     "in the afternoon で『午後に』。朝・午後・夕方などの時間帯には in を使う。on は曜日や日付、at は時刻、to は行き先などを示す前置詞なので、ここでは合わない。",
     "『ごごに』は in the afternoon というよ。あさやゆうがたも、in the morning、in the evening のように in をつかうね。",
     ["in the afternoon で『午後に』を表す。","on は曜日や日付の前に使う。","at は時刻の前に使い、afternoon には使わない。","to は行き先などを示し、ここでは合わない。"],
     ["『ごごに』は in をつかうね。","ようびやひにちにつかうよ。","なんじ、というときにつかうよ。","いくさきにつかうよ。"]),
    ("A: Can I talk to you, Steve?\nB: Yes, Dad. (　) a minute, please.",
     "A：スティーブ、ちょっと話してもいいかな。\nB：はい、お父さん。(　) 待ってください。",
     ["That","Less","More","Just"],["あれ・それ","より少ない","もっと多い","ちょうど・ほんの"],4,
     "Just a minute, please. は『少し待ってください』という決まった言い方。話しかけられた B が、Yes, Dad. と応じたうえで少し待ってほしいと頼んでいる。That・Less・More ではこの意味にならない。",
     "Just a minute は『ちょっとまって』というきまったいいかた。おとうさんに、すこしまってね、とおねがいしているよ。",
     ["That a minute という言い方はしない。","Less a minute では意味が通らない。","More a minute では、待ってと頼む意味にならない。","Just a minute で、少し待ってと頼む。"],
     ["このいいかたはしないよ。","『すくない』ではないよ。","『もっと』ではないよ。","ちょっとまって、だね。"]),
    ("A: How was your trip to Canada?\nB: It was great. I became good friends (　) some students.",
     "A：カナダへの旅行はどうでしたか。\nB：とてもよかったです。何人かの学生 (　) 仲良くなりました。",
     ["with","under","for","after"],["～と（一緒に）","～の下に","～のために","～の後に"],1,
     "become friends with＋人で『人と友達になる』。became は become の過去形。旅行中に何人かの学生と仲良くなったという内容になる。under・for・after では、友達になった相手を示せない。",
     "カナダで、がくせいとなかよくなったんだね。friends with は『～とともだち』。with は『～と』だよ。",
     ["friends with で、友達になった相手を示す。","under は位置を表し、相手を示さない。","for は目的などを示し、友達の相手にならない。","after は順序を表し、この意味にならない。"],
     ["with は『～と』だね。","『～のした』ではないよ。","『～のために』ではないよ。","『～のあと』ではないよ。"]),
    ("A: I need to call my mom. (　) I use your smartphone?\nB: Sure.",
     "A：母に電話をしなければなりません。あなたのスマートフォンを使っても (　) か。\nB：いいですよ。",
     ["Does","Have","Could","Did"],["する（do の三人称単数現在）","持っている（現在完了にも使う）","～してもよいか（ていねいな許可）","した（do の過去形）"],3,
     "Could I＋動詞の原形 ～? は『～してもいいですか』とていねいに許可を求める言い方。母に電話するため、相手のスマートフォンを使ってよいか尋ねている。Sure. はその承諾。Does は主語 I に使わず、Did では過去のことを尋ねる文になる。",
     "スマートフォンをつかってもいい？ときいているね。Could I ～? は『～してもいいですか』とていねいにたずねるいいかただよ。",
     ["主語 I の疑問文に Does は使わない。","Have I の後ろは過去分詞で、原形 use は続かない。","Could I use ～? で、使ってよいか尋ねる。","過去のことを尋ねる文になり、今の頼みにならない。"],
     ["I には Does をつかわないよ。","このかたちにはならないよ。","つかってもいい？ときいているね。","むかしのことをきいていないよ。"]),
    ("A: How was your weekend?\nB: Well, it rained all weekend, so we (　) go camping.",
     "A：週末はどうでしたか。\nB：ええと、週末はずっと雨が降っていたので、私たちはキャンプに (　)。",
     ["wasn't","isn't","didn't","weren't"],["～ではなかった（was not）","～ではない（is not）","～しなかった（did not）","～ではなかった（were not）"],3,
     "it rained（雨が降った）から過去の話だと分かる。go は動詞の原形なので、一般動詞の過去の否定文 didn't＋原形を使う。wasn't・weren't は be 動詞の過去形で後ろに原形 go を置けず、isn't は現在形。",
     "rained で、むかしのおはなしだとわかるね。go のまえには didn't をおいて『いかなかった』というよ。",
     ["be 動詞の過去形で、後ろに原形 go は置けない。","be 動詞の現在形で、過去の話にも合わない。","didn't go で、行かなかったことを表す。","be 動詞の過去形で、原形 go とつながらない。"],
     ["go のまえには、つかわないよ。","いまの形で、go ともあわないよ。","didn't go で『いかなかった』だね。","be どうしなので、go とあわないよ。"]),
    ("A: Which cake did you like (　), the chocolate cake or the lemon cake?\nB: The lemon one.",
     "A：チョコレートケーキとレモンケーキでは、どちらのケーキが (　) 気に入りましたか。\nB：レモンのほうです。",
     ["well","better","much","good"],["上手に・よく","よりよく・もっと","たくさん・とても","よい"],2,
     "Which ～ did you like better, A or B? は『AとBのどちらが気に入ったか』と比べる形。better は well の比較級で、like ～ better は『～のほうが好き』。well・much・good は比較級ではない。",
     "2つのケーキをくらべて、どちらがすきかきいているね。like ～ better は『～のほうがすき』。better をつかおう。",
     ["well のままでは、2つを比べる形にならない。","like ～ better で、どちらが好きか比べる。","much のままでは、2つを比べる形にならない。","good は形容詞で、like の後ろで比べられない。"],
     ["『じょうずに』では、くらべられないよ。","どちらがすきか、くらべているね。","『たくさん』では、くらべられないよ。","『よい』では、くらべられないよ。"]),
    ("Boy: Thank you for coming to my baseball game, Uncle Jim.\nUncle: (　) I enjoyed it very much.",
     "男の子：ジムおじさん、ぼくの野球の試合に来てくれてありがとう。\nおじ：(　) とても楽しかったよ。",
     ["I'm sorry about that.","That's all, thanks.","Yes, please.","You're welcome."],
     ["それはごめんなさい。","以上です、ありがとう。","はい、お願いします。","どういたしまして。"],4,
     "Thank you for ～ing（～してくれてありがとう）への返事は You're welcome.（どういたしまして）。続く I enjoyed it very much. も試合を楽しんだと伝えている。謝る表現や Yes, please. は合わない。",
     "『きてくれてありがとう』といわれたね。You're welcome. は『どういたしまして』。ありがとうへのへんじだよ。",
     ["お礼を言われて謝るのは不自然。","注文などを終えるときの言い方で、お礼への返事ではない。","何かを勧められたときの返事で、お礼には合わない。","お礼に『どういたしまして』と応じている。"],
     ["あやまることではないよ。","『それでおわり』ではないよ。","すすめられたときのへんじだよ。","『どういたしまして』だね。"]),
    ("Daughter: Let's play tennis, Dad.\nFather: Not today. (　)",
     "娘：お父さん、テニスをしようよ。\n父：今日はやめておこう。(　)",
     ["It's going to rain.","I like sports.","I'll do it.","Your mother will buy some."],
     ["雨が降りそうだよ。","私はスポーツが好きだよ。","私がそれをするよ。","お母さんがいくつか買ってくれるよ。"],1,
     "Not today.（今日はだめ）と断ったあとには、その理由が続く。It's going to rain. は『雨が降りそうだ』で、今日テニスをしない理由として自然。スポーツが好き、自分がする、母親が買うという内容は、断る理由として合わない。",
     "『きょうはだめ』のあとに、そのりゆうをいっているね。『あめがふりそう』だから、テニスをしないんだよ。",
     ["雨が降りそうなことが、今日やめる理由になる。","スポーツが好きなことは、断る理由にならない。","自分がすると言うと、断った内容と合わない。","母親が買う話は、テニスの誘いとつながらない。"],
     ["あめがふりそうだから、やめるんだね。","すきなら、ことわらないよね。","『わたしがする』ではないよ。","かいもののおはなしではないよ。"]),
    ("Woman 1: I love this coat. I'm going to buy it.\nWoman 2: (　)\nWoman 1: No, it's only $60.",
     "女性1：このコートがとても気に入りました。買うつもりです。\n女性2：(　)\n女性1：いいえ、たったの60ドルです。",
     ["Will it close soon?","Are you cold?","Did you see it?","Is it expensive?"],
     ["それはもうすぐ閉まりますか。","あなたは寒いですか。","あなたはそれを見ましたか。","それは高いですか。"],4,
     "No, it's only $60.（いいえ、たったの60ドル）が決め手。only は値段の安さを示すので、Is it expensive?（高いですか）が合う。閉まる時間・寒さ・見たかどうかの質問では、値段を答える返事につながらない。",
     "『いいえ、たったの60ドルだよ』とこたえているね。だから『それはたかい？』ときいたんだよ。expensive は『たかい』。",
     ["閉まる時間を聞かれて、値段では答えない。","寒いかどうかに、値段で答えるのは不自然。","見たかどうかに、値段で答えるのは合わない。","高いかを尋ね、only $60 で安いと答えている。"],
     ["おみせのじかんではないよ。","さむいかどうかではないよ。","みたかどうかではないよ。","ねだんがたかいか、きいているね。"]),
    ("Son: Dad, I'm home. Where's Mom?\nFather: She's at the library now. (　)",
     "息子：お父さん、ただいま。お母さんはどこですか。\n父：今、図書館にいます。(　)",
     ["She'll get up early.","It's not your book.","She'll be back soon.","Thanks for telling me."],
     ["彼女は早く起きるでしょう。","それはあなたの本ではありません。","彼女はすぐに戻ってきます。","教えてくれてありがとう。"],3,
     "She's at the library now.（今は図書館にいる）に続けて、She'll be back soon.（すぐ戻る）と伝えている。母親の居場所を尋ねた息子への自然な説明になる。起きる時刻や本の持ち主の話はつながらない。",
     "おかあさんはいま、としょかんにいるよ。そのあとに『すぐにもどってくるよ』とつたえているね。be back は『もどる』。",
     ["起きる時刻は、今の居場所の話とつながらない。","本の持ち主の話は、母親の居場所と無関係。","図書館にいる母親が、すぐ戻ると伝えている。","教えているのは父親なので、礼を言う流れではない。"],
     ["おきるじかんのことではないよ。","ほんのおはなしではないよ。","すぐにかえってくるんだね。","おしえているのはおとうさんだよ。"]),
    ("Boy: It's raining today. Do we have soccer practice?\nGirl: (　) Let's ask Mr. Smith.",
     "男の子：今日は雨が降っています。サッカーの練習はありますか。\n女の子：(　) スミスさんに聞いてみましょう。",
     ["I'm not sure.","You're doing great.","That's my ball.","This isn't my uniform."],
     ["よく分かりません。","よくできていますね。","それは私のボールです。","これは私のユニフォームではありません。"],1,
     "Do we have soccer practice? に、Let's ask Mr. Smith.（スミスさんに聞こう）と続く。分からないので聞こうと言っており、I'm not sure.（よく分からない）が合う。ボールやユニフォームの話は答えにならない。",
     "れんしゅうがあるか、わからないんだね。だから『スミスさんにきこう』といっているよ。I'm not sure は『よくわからない』。",
     ["分からないので、スミスさんに聞こうと続く。","相手をほめる言葉で、練習の有無に答えていない。","ボールの持ち主は、質問と関係がない。","ユニフォームの話は、練習の有無と無関係。"],
     ["わからないから、きいてみるんだね。","ほめることばではないよ。","ボールのおはなしではないよ。","ユニフォームのおはなしではないよ。"]),
]


def build():
    p,o,m=module("passages"),module("order"),module("materials")
    qs=[]
    for n,r in enumerate(ROWS,1):
        text,ja,choices,meanings,answer,grammar,simple,reasons,easy=r
        qs.append(dict(number=n,text=text,translation=ja,choices=choices,
                       choiceTranslations=meanings,answer=answer,grammar=grammar,grammarSimple=simple,
                       choiceAnalysis=[("○ " if i==answer else "")+f"{c}＝{t.rstrip('。')}。{why}" for i,(c,t,why) in enumerate(zip(choices,meanings,reasons),1)],
                       choiceAnalysisSimple=[("○ " if i==answer else "")+f"{t.rstrip('。')}。{why}" for i,(t,why) in enumerate(zip(meanings,easy),1)]))
    sections=[
        dict(name="大問1",nameEn="Part 1",type="vocabulary",instruction="次の(1)から(15)までの(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選び，その番号のマーク欄をぬりつぶしなさい。",questions=qs[:15]),
        dict(name="大問2",nameEn="Part 2",type="vocabulary",instruction="次の(16)から(20)までの会話について，(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選び，その番号のマーク欄をぬりつぶしなさい。",questions=qs[15:]),
        dict(name="大問3",nameEn="Part 3",type="sentence-order",instruction="次の(21)から(25)までの日本文の意味を表すように①から⑤までを並べかえて□の中に入れなさい。そして，2番目と4番目にくるものの最も適切な組合せを1，2，3，4の中から一つ選び，その番号のマーク欄をぬりつぶしなさい。※ただし，(　)の中では，文のはじめにくる語も小文字になっています。",questions=o.questions()),
        dict(name="大問4",nameEn="Part 4",type="reading-comprehension",instruction="次の掲示・Eメール・英文を読み、それぞれの問いに答えなさい。",passages=p.PASSAGES),
    ]
    listening=[3,3,1,2,3,3,3,2,3,3,3,4,2,1,4,3,2,1,1,1,4,3,2,3,3,1,4,3,1,4]
    return dict(grade="grade4",year="2026",session="2026-2",exam="2026-2",
                title="英検4級 2026年度 第2回",sections=sections,
                listening={f"part{i+1}":dict(zip(map(str,range(10*i+1,10*i+11)),listening[10*i:10*i+10])) for i in range(3)},
                vocabulary=m.vocabulary(),lessonPlan=m.lessonplan(sections))


if __name__=="__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(build(),ensure_ascii=False,indent=4)+"\n",encoding="utf-8")
    print(OUT)

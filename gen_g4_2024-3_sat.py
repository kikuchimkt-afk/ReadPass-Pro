# -*- coding: utf-8 -*-
"""Reproduce Grade 4 2024-3 Saturday; booklet pp. 2-11, transcribed from page images (no text layer)."""
import importlib.util
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "data/grade4/2024-3-sat/data.json"


def module(suffix):
    spec=importlib.util.spec_from_file_location(suffix,ROOT/f"gen_g4_2024-3_sat_{suffix}.py")
    result=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


# stem, translation, choices, meanings, answer, normal/simple grammar,
# choice-specific reasons. All four normal/simple analyses retain meanings.
ROWS = [
    ("A: Will it be sunny tomorrow?\nB: No. It'll be (　) all day.",
     "A：明日は晴れるでしょうか。\nB：いいえ。一日中 (　) でしょう。",
     ["cloudy","soft","hungry","long"],["くもった","やわらかい","おなかがすいた","長い"],1,
     "A は明日晴れるかを尋ね、B は No と答えているので、晴れ以外の天気が入る。It'll be cloudy で『くもりになるだろう』。all day は『一日中』。soft・hungry・long は天気を表す語ではない。",
     "『あしたははれる？』『ううん、いちにちじゅう くもりだよ』。cloudy は『くもった』だね。",
     ["晴れるかという質問に No と答え、くもりの天気を伝えている。","やわらかさを表す語で、天気を表さない。","人の空腹を表す語で、天気には使わない。","長さを表す語で、天気を表さない。"],
     ["くもりのてんきだね。","やわらかい、はてんきではないよ。","おなかがすいた、はひとのことだよ。","ながい、はてんきではないよ。"]),
    ("Jenny's father works for a big computer (　). He loves computers, so he enjoys his job.",
     "ジェニーのお父さんは大きなコンピューター (　) で働いています。彼はコンピューターが大好きなので、仕事を楽しんでいます。",
     ["company","size","color","side"],["会社","大きさ","色","側・横"],1,
     "works for ～で『～に勤めている』。for の後ろには勤め先が入るので company（会社）。a big computer company で『大きなコンピューター会社』。2文目の his job（彼の仕事）も勤め先の話とつながる。size・color・side は勤め先にならない。",
     "works for は『～ではたらく』。おとうさんは、おおきなコンピューターのかいしゃではたらいているんだね。company は『かいしゃ』だよ。",
     ["勤め先として会社が合い、his job ともつながる。","大きさは勤め先にならない。","色は勤め先にならない。","側・横という意味で、勤め先にならない。"],
     ["かいしゃではたらいているね。","おおきさでは、はたらけないよ。","いろでは、はたらけないよ。","よこ、ではいみがつながらないよ。"]),
    ("A: How long did you study today, Alex?\nB: I studied for three (　).",
     "A：アレックス、今日はどれくらい勉強しましたか。\nB：3 (　) 勉強しました。",
     ["cousins","rooms","clothes","hours"],["いとこ","部屋","服","時間"],4,
     "How long ～? は『どれくらいの間～』と時間の長さを尋ねる言い方。for three hours で『3時間』。hours は hour（時間）の複数形。cousins・rooms・clothes では時間の長さを答えられない。",
     "How long は『どれくらいのあいだ』。こたえは『3じかん』で、hours は『じかん』だよ。",
     ["人を表す語で、勉強した時間の長さにならない。","部屋の数では、時間の長さを答えられない。","服は時間の長さを表さない。","How long の質問に、3時間と長さを答えている。"],
     ["いとこは、ひとのことだよ。","へやのかずではないよ。","ふくのことではないよ。","3じかん、べんきょうしたんだね。"]),
    ("Tony is going to give his grandmother a birthday (　) tomorrow. She will be 80 years old.",
     "トニーは明日、祖母に誕生日の (　) をあげるつもりです。祖母は80歳になります。",
     ["health","age","present","weather"],["健康","年齢","プレゼント・贈り物","天気"],3,
     "give＋人＋物で『人に物をあげる』。a birthday present で『誕生日プレゼント』。祖母が明日80歳になるので、誕生日の贈り物をあげる。age（年齢）は2文目の80歳と関係がありそうに見えるが、人にあげる物ではない。health や weather もあげる物ではない。",
     "おばあちゃんに、たんじょうびの present『プレゼント』をあげるんだね。80さいのおいわいだよ。",
     ["健康は人にあげる物ではない。","年齢は人にあげる物ではない。","誕生日に祖母へ贈る物として合う。","天気は人にあげる物ではない。"],
     ["けんこうは、あげるものではないよ。","ねんれいは、あげるものではないよ。","たんじょうびのプレゼントだね。","てんきは、あげるものではないよ。"]),
    ("A: Are you studying Chinese?\nB: Yes. It's a difficult (　), but I enjoy learning it.",
     "A：あなたは中国語を勉強しているのですか。\nB：はい。難しい (　) ですが、学ぶのを楽しんでいます。",
     ["season","language","aunt","breakfast"],["季節","言語・言葉","おば","朝食"],2,
     "It は Chinese（中国語）を指す。中国語は language（言語）の一つなので、It's a difficult language で『難しい言語だ』。後半の learning it も中国語を学ぶこと。season・aunt・breakfast では中国語を言いかえられない。",
     "It は『ちゅうごくご』のこと。ちゅうごくごは language『ことば』だね。むずかしいけど、たのしくべんきょうしているよ。",
     ["季節では、中国語を言いかえられない。","It＝Chinese を言いかえ、難しい言語だと説明している。","おばは人で、中国語を指さない。","朝食は中国語を指さない。"],
     ["きせつのことではないよ。","ちゅうごくごは、ことばだね。","おばさんのことではないよ。","あさごはんのことではないよ。"]),
    ("A: Thanks for taking me to the baseball game, Grandma.\nB: You're welcome. I enjoyed watching the game (　).",
     "A：おばあちゃん、野球の試合に連れて行ってくれてありがとう。\nB：どういたしまして。(　) 試合を見て、私も楽しかったですよ。",
     ["ago","forward","together","almost"],["～前に","前へ","一緒に","ほとんど"],3,
     "孫を野球の試合に連れて行った祖母が、『一緒に試合を見て楽しかった』と答えている。together は『一緒に』。ago は two days ago のように期間を表す語の後ろで使う。forward（前へ）や almost（ほとんど）を文の終わりに置いても、試合を見た様子を表せない。",
     "おばあちゃんとまごが、いっしょにやきゅうをみたんだね。together は『いっしょに』だよ。",
     ["ago は two days ago のように期間の後ろで使い、ここには合わない。","『前へ』では、試合を見た様子を表せない。","祖母と孫が一緒に試合を見たことを表す。","『ほとんど』を文の終わりに置いても、意味が通らない。"],
     ["『～まえ』ではないよ。","『まえへ』ではないよ。","いっしょにみたんだね。","『ほとんど』ではないよ。"]),
    ("Hiroko had a great time at her school festival, so she will always (　) it.",
     "ヒロコは学校の文化祭でとても楽しく過ごしたので、いつまでもそれを (　) でしょう。",
     ["remember","find","learn","hear"],["覚えている","見つける","学ぶ","聞く"],1,
     "had a great time は『とても楽しい時を過ごした』。so（だから）の後ろで、楽しかった文化祭をいつまでも覚えているという流れになる。will always remember it で『いつまでも覚えているだろう』。it は文化祭のこと。find・learn・hear では、楽しかったこととのつながりができない。",
     "ぶんかさいがとてもたのしかったから、ずっとおぼえているね。remember は『おぼえている』だよ。",
     ["楽しかった文化祭をいつまでも覚えている、と so の後ろにつながる。","文化祭を見つける、では楽しかったこととつながらない。","文化祭を学ぶ、では意味が通らない。","文化祭を聞く、では意味が通らない。"],
     ["ずっとおぼえているんだね。","みつける、ではないよ。","まなぶ、ではないよ。","きく、ではないよ。"]),
    ("A: Where is the station?\nB: It's over (　).",
     "A：駅はどこですか。\nB：(　) にあります。",
     ["away","back","straight","there"],["離れて","戻って・後ろへ","まっすぐに","そこに・あそこに"],4,
     "over there で『あそこに・向こうに』。駅の場所を尋ねられ、離れた場所を指して答えている。away・back・straight を over の後ろに置いても、場所を答える決まった言い方にならない。",
     "『えきはどこ？』『あそこだよ』。over there は『あそこに』でセットだよ。",
     ["『離れて』という意味で、over と組み合わせても駅の場所を示せない。","『戻って』という意味で、場所を答える言い方にならない。","道順を説明する語で、over とはセットにならない。","over there で『あそこに』と駅の場所を答えている。"],
     ["away では、このセットにならないよ。","back では、このセットにならないよ。","straight では、このセットにならないよ。","over there で『あそこに』だね。"]),
    ("A: Are you ready to go to school, Emily?\nB: Yes, Mom. I'll go now. (　) goodbye to Dad for me.",
     "A：エミリー、学校へ行く準備はできましたか。\nB：うん、お母さん。もう行くね。お父さんに、私からさよならと (　)。",
     ["Say","Look","Get","Take"],["言う","見る","手に入れる","取る・持って行く"],1,
     "say goodbye to ～で『～にさよならを言う』。命令文なので動詞の原形 Say で始める。for me は『私の代わりに』で、出かける前に父へのあいさつを母に頼んでいる。Look・Get・Take は goodbye と組み合わせても『さよならを言う』の意味にならない。",
     "say goodbye は『さよならをいう』。『おとうさんに、さよならっていっておいてね』とたのんでいるよ。",
     ["say goodbye to で『～にさよならを言う』。","look は『見る』で、goodbye と組み合わせても意味が通らない。","get goodbye では『さよならを言う』の意味にならない。","take goodbye では『さよならを言う』の意味にならない。"],
     ["さよならをいうんだね。","みる、ではないよ。","get では、このいみにならないよ。","take では、このいみにならないよ。"]),
    ("Nick and his wife will have lunch at a restaurant today. Then, they will go to a zoo (　) the afternoon.",
     "ニックと妻は今日、レストランで昼食を食べます。それから、午後 (　) 動物園へ行きます。",
     ["on","at","in","out"],["～の上に・（曜日）に","（時刻）に・（地点）で","（時間帯）に・～の中に","外へ"],3,
     "in the afternoon で『午後に』。in the morning（午前中に）と同じ形で覚える。at は at three（3時に）のように時刻に、on は on Sunday（日曜日に）のように曜日に使う。ここは the afternoon だけなので in を選ぶ。out は『外へ』で時を表さない。",
     "in the afternoon は『ごごに』。ひるごはんのあと、ごごにどうぶつえんへいくんだね。",
     ["on は on Sunday のように曜日に使い、ここでは『午後に』の形にならない。","at は at three のように時刻に使う。","in the afternoon で『午後に』。","out は『外へ』で、時を表さない。"],
     ["on は、ようびにつかうよ。","at は、なんじ、につかうよ。","in the afternoon で『ごごに』だね。","out は『そとへ』だよ。"]),
    ("A: Let's watch a movie tonight.\nB: I can't. I (　) to study for my math test tomorrow.",
     "A：今夜、映画を見ようよ。\nB：見られないんだ。明日の数学のテストのために勉強 (　)。",
     ["give","cut","do","have"],["与える","切る","する","（have to で）～しなければならない"],4,
     "have to＋動詞の原形で『～しなければならない』。映画に誘われて I can't. と断り、その理由として明日のテスト勉強をしなければならないと説明している。give・cut・do は to study と組み合わせても『～しなければならない』の意味にならない。",
     "have to は『～しなければならない』。あしたのテストのべんきょうをしなきゃいけないから、えいがはみられないんだね。",
     ["give to study では意味が通らない。","cut to study では意味が通らない。","do to study では『しなければならない』の意味にならない。","have to study で『勉強しなければならない』と断る理由を言っている。"],
     ["give では、いみがつながらないよ。","cut では、いみがつながらないよ。","do では、このいみにならないよ。","have to で『～しなきゃいけない』だね。"]),
    ("Yukiko's father comes (　) Canada, but he can speak Japanese very well.",
     "ユキコのお父さんはカナダ (　) ですが、日本語をとても上手に話せます。",
     ["under","for","from","with"],["～の下に","～のために","～から・～出身の","～と一緒に"],3,
     "come from ～で『～の出身だ』。主語が Yukiko's father なので comes。カナダ出身だが日本語がとても上手だ、と but で対比している。under・for・with は come と組み合わせても出身を表さない。",
     "comes from Canada は『カナダしゅっしん』。カナダのひとだけど、にほんごがじょうずなんだね。",
     ["『～の下に』では出身を表さない。","『～のために』では出身を表さない。","come from で『～の出身だ』。","『～と一緒に』では出身を表さない。"],
     ["『～のした』ではないよ。","『～のために』ではないよ。","comes from で『～しゅっしん』だね。","『～といっしょに』ではないよ。"]),
    ("A: Mark, please (　) touch my computer.\nB: I'm sorry, Mom.",
     "A：マーク、私のコンピューターにさわら (　) ください。\nB：ごめんなさい、お母さん。",
     ["doesn't","don't","didn't","aren't"],["does not の短縮形","do not の短縮形","did not の短縮形","are not の短縮形"],2,
     "Don't＋動詞の原形で『～しないで』という否定の命令文。please をつけると丁寧になり、please don't touch で『さわらないでください』。B が I'm sorry と謝っているのも、注意された場面に合う。doesn't・didn't・aren't は否定の命令文には使わない。",
     "please don't touch は『さわらないでね』。マークは、おかあさんにちゅういされたんだね。",
     ["否定の命令文には doesn't を使わない。","please don't touch で『さわらないでください』。","否定の命令文には didn't を使わない。","否定の命令文には aren't を使わない。"],
     ["doesn't は、ここではつかわないよ。","『さわらないで』だね。","didn't は、むかしのことにつかうよ。","aren't は、ここではつかわないよ。"]),
    ("A: (　) did you come to the zoo today?\nB: To take a picture of the pandas.",
     "A：今日は (　) 動物園に来たのですか。\nB：パンダの写真を撮るためです。",
     ["Why","When","Where","Which"],["なぜ","いつ","どこで・どこへ","どちら・どの"],1,
     "B の To take a picture of the pandas. は『パンダの写真を撮るために』という目的を答えている。目的や理由を尋ねるのは Why。When なら時、Which なら選ぶものを答える流れになる。場所は to the zoo とすでに言っているので Where も合わない。",
     "『どうしてどうぶつえんにきたの？』『パンダのしゃしんをとるためだよ』。Why は『なぜ』だね。",
     ["目的を尋ね、写真を撮るためと答えている。","時を尋ねると、次は時を答える流れになる。","場所は to the zoo とすでに言っている。","Which なら選ぶものを答える流れになる。"],
     ["りゆうをきいているね。","いつ、はきいていないよ。","ばしょは、もうどうぶつえんだよ。","どれ、はきいていないよ。"]),
    ("A: What did you do yesterday, John?\nB: I (　) table tennis with my father and sister.",
     "A：ジョン、昨日は何をしましたか。\nB：父と姉（妹）と卓球を (　)。",
     ["play","played","playing","plays"],["する（原形）","した（過去形）","している（-ing形）","する（三人称単数現在）"],2,
     "A が What did you do yesterday? と昨日のことを尋ねているので、B も過去形 played で答える。play table tennis で『卓球をする』。play・plays は現在の形、playing は be 動詞がないと主語 I の動詞にならない。",
     "きのうのことだから、むかしのかたちの played『した』だね。",
     ["原形では昨日の出来事を表せない。","yesterday のことなので過去形 played。","-ing 形だけでは主語 I の動詞にならない。","三人称単数現在の形で、主語 I にも昨日のことにも合わない。"],
     ["いまのかたちではないよ。","きのうのことだから played だね。","ing のかたちだけでは、つかえないよ。","s のついたかたちではないよ。"]),
    ("Daughter: Mom, it's seven o'clock and I'm hungry!\nMother: (　) Let's eat.",
     "娘：お母さん、7時だよ。おなかがすいた！\n母：(　) 食べましょう。",
     ["Dinner is ready.","I can talk to you.","There is no food.","Yes, I will."],
     ["夕食の準備ができました。","あなたと話せます。","食べ物がありません。","はい、そうします。"],1,
     "娘が7時でおなかがすいたと言い、母は空所の後ろで Let's eat.（食べましょう）と誘っている。食べる前の一言として Dinner is ready.（夕食ができた）が合う。There is no food. では Let's eat. とつながらない。Yes, I will. は質問や依頼に答える言い方で、娘は質問も依頼もしていない。",
     "『おなかすいた！』『ごはんができたよ。たべよう』。ready は『じゅんびができた』だよ。",
     ["夕食ができたと伝え、Let's eat. につながる。","話せると言っても、食事の話につながらない。","食べ物がないと、Let's eat. と誘えない。","質問や依頼に答える言い方で、この場面に合わない。"],
     ["ごはんができたんだね。","はなすことではないよ。","たべものがないと、たべられないよ。","しつもんのへんじではないよ。"]),
    ("Boy: Jane, I forgot my eraser. (　)\nGirl: Here you are.",
     "男の子：ジェーン、消しゴムを忘れちゃった。(　)\n女の子：はい、どうぞ。",
     ["Is it today?","How much is yours?","When does it start?","Can I use yours?"],
     ["それは今日ですか。","あなたのはいくらですか。","それはいつ始まりますか。","あなたのを使ってもいいですか。"],4,
     "消しゴムを忘れたので、相手の消しゴムを借りたいと頼む場面。Can I ～? は『～してもいいですか』と許可を求める言い方で、yours は your eraser のこと。女の子の Here you are.（はい、どうぞ）は物を手渡すときの言葉なので、借りたいという頼みへの返事になる。",
     "『けしゴムをわすれた。あなたのをつかってもいい？』『はい、どうぞ』。Here you are. は、ものをわたすときのことばだよ。",
     ["今日かどうかを聞いても、Here you are. とつながらない。","値段を聞かれたら、金額を答える。","始まる時刻を聞かれたら、時刻を答える。","消しゴムを借りたいと頼み、相手が手渡している。"],
     ["きょうかどうか、ではないよ。","ねだんをきいているのではないよ。","はじまるじかんではないよ。","けしゴムをかりたいんだね。"]),
    ("Boy: Can you play the guitar?\nGirl: (　) I started learning a month ago.",
     "男の子：ギターを弾けますか。\n女の子：(　) 1か月前に習い始めました。",
     ["A little.","I like them.","I have a ticket.","Have a good time."],
     ["少しだけ。","私はそれらが好きです。","チケットを持っています。","楽しんできてね。"],1,
     "Can you ～? はできるかどうかを尋ねる質問。1か月前に習い始めたばかりなので、A little.（少しだけ）と答えるのが自然。I like them. の them が指すものがなく、ギターを弾けるかの答えにもならない。Have a good time. は出かける人にかける言葉。",
     "『ギターをひける？』『すこしだけ。1かげつまえにならいはじめたの』。A little. は『すこしだけ』だよ。",
     ["弾けるかどうかに『少しだけ』と答え、始めたばかりの説明につながる。","them が指すものがなく、弾けるかの答えにならない。","チケットの話は、ギターを弾けるかの答えにならない。","出かける人にかける言葉で、この質問の答えにならない。"],
     ["すこしだけ、ひけるんだね。","すき、はこたえにならないよ。","チケットのはなしではないよ。","でかけるひとへのことばだよ。"]),
    ("Teacher: Where is your science homework, Amy?\nStudent: I'm sorry. (　)",
     "先生：エイミー、理科の宿題はどこですか。\n生徒：すみません。(　)",
     ["It was a test.","Science is interesting.","I forgot it.","School starts at eight."],
     ["それはテストでした。","理科はおもしろいです。","それを忘れました。","学校は8時に始まります。"],3,
     "宿題がどこにあるかを聞かれ、I'm sorry. と謝っているので、宿題を出せない理由が続く。I forgot it. の it は science homework を指し、『宿題を忘れた』となる。理科がおもしろいことや始業時刻では、謝る理由にならない。",
     "『しゅくだいはどこ？』『ごめんなさい。わすれました』。forgot は forget『わすれる』のむかしのかたちだよ。",
     ["宿題をテストだったと言っても、謝る理由にならない。","理科がおもしろいことは、宿題がない理由にならない。","it＝宿題を忘れたと謝っている。","始業時刻は、宿題の場所の質問と関係がない。"],
     ["テストのはなしではないよ。","りかがおもしろい、ではないよ。","しゅくだいをわすれたんだね。","がっこうのはじまるじかんではないよ。"]),
    ("Father: School starts next week, Tom. Do you need anything?\nSon: Yes, (　)",
     "父：トム、来週から学校が始まるね。何か必要なものはあるかい？\n息子：うん、(　)",
     ["a pencil case.","I'm full.","I'm fifteen.","that's mine."],
     ["筆箱。","おなかがいっぱいです。","ぼくは15歳です。","それはぼくのものです。"],1,
     "Do you need anything? は『何か必要なものはある？』と尋ねている。Yes の後ろには必要なものを答えるので、a pencil case（筆箱）が合う。I'm full.（おなかがいっぱい）や I'm fifteen.（15歳です）は必要なものを答えていない。that's mine. は持ち主を言う言い方。",
     "『なにかいるものはある？』『うん、ふでばこ』。いるものをこたえているね。",
     ["必要なものとして筆箱を答えている。","おなかの具合で、必要なものの答えにならない。","年齢で、必要なものの答えにならない。","持ち主を言う言い方で、必要なものの答えにならない。"],
     ["ふでばこがいるんだね。","おなかいっぱい、ではないよ。","ねんれいではないよ。","だれのものか、ではないよ。"]),
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
    listening=[2,3,2,2,3,2,3,1,1,2,4,2,3,1,2,3,2,1,4,1,4,1,3,2,4,2,1,3,1,4]
    return dict(grade="grade4",year="2024",session="2024-3-sat",exam="2024-3-sat",
                title="英検4級 2024年度 第3回（土曜準会場）",sections=sections,
                listening={f"part{i+1}":dict(zip(map(str,range(10*i+1,10*i+11)),listening[10*i:10*i+10])) for i in range(3)},
                vocabulary=m.vocabulary(),lessonPlan=m.lessonplan(sections))


if __name__=="__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(build(),ensure_ascii=False,indent=4)+"\n",encoding="utf-8")
    print(OUT)

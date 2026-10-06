"""Grade 4's existing 30-word / four-focus-point / normal-and-easy format."""
import re

VOCAB=[
    ("temperature","温度","名詞","The temperature is high today.","今日は気温が高いです。",["住所","故郷","村"],"大問1 Q1","temperature"),
    ("aquarium","水槽・水族館","名詞","There are five fish in the aquarium.","水槽には5匹の魚がいます。",["図書館","台所","庭"],"大問1 Q1","aquarium"),
    ("end","終わる","動詞","Our class will end at three.","私たちの授業は3時に終わります。",["描く","建てる","聞く"],"大問1 Q2","end"),
    ("close","閉まる・休みになる","動詞","The shop will close at six.","その店は6時に閉まります。",["踊る","立つ","話す"],"大問1 Q3","close"),
    ("tell","話す・伝える","動詞","Please tell me your name.","名前を教えてください。",["乗る","止める","走る"],"大問1 Q4","tells"),
    ("apartment","アパート","名詞","My aunt lives in a small apartment.","おばは小さなアパートに住んでいます。",["休暇","試合","公演"],"大問1 Q5","apartment"),
    ("warm","暖かい","形容詞","It is warm in this room.","この部屋は暖かいです。",["怒っている","汚れた","暗い"],"大問1 Q6","warm"),
    ("repeat","繰り返す","動詞","Please repeat your name.","名前をもう一度言ってください。",["受け取る","掃除する","会う"],"大問1 Q7","repeat"),
    ("for a long time","長い間","熟語","We played in the park for a long time.","私たちは公園で長い間遊びました。",["時間どおりに","初めて","すぐに"],"大問1 Q8","for a long time"),
    ("look like","～に似ている","熟語","You look like your father.","あなたはお父さんに似ています。",["～を探す","～を世話する","～を待つ"],"大問1 Q9","looks like"),
    ("talk with","～と話す","熟語","I talked with my teacher after school.","私は放課後に先生と話しました。",["～を見る","～を待つ","～を探す"],"大問1 Q10","talked with"),
    ("fine with me","私はそれでよい・都合がよい","熟語","Friday is fine with me.","私は金曜日で大丈夫です。",["私は疲れている","私は遅れている","私は迷っている"],"大問1 Q11","fine with me"),
    ("again and again","何度も何度も","熟語","She read the letter again and again.","彼女は手紙を何度も読みました。",["時々","一度だけ","やがて"],"大問1 Q12","again and again"),
    ("drink","飲む","動詞","I drank some milk this morning.","私は今朝、牛乳を飲みました。",["歌う","描く","食べる"],"大問1 Q13","drank"),
    ("hers","彼女のもの","代名詞","This bag is hers.","このかばんは彼女のものです。",["私のもの","彼のもの","彼らのもの"],"大問1 Q14","Hers"),
    ("have to","～しなければならない","熟語","I have to do my homework.","私は宿題をしなければなりません。",["～する必要はない","～したい","～してもよい"],"大問1 Q15","have to"),
    ("delicious","おいしい","形容詞","This cake is delicious.","このケーキはおいしいです。",["難しい","悲しい","寒い"],"大問2 Q16","delicious"),
    ("some more","もう少し・追加の分","熟語","Would you like some more tea?","お茶をもう少しいかがですか。",["長い間","何度も","少し前に"],"大問2 Q16","some more"),
    ("umbrella","傘","名詞","I have a blue umbrella.","私は青い傘を持っています。",["スプーン","帽子","コート"],"大問2 Q18","umbrella"),
    ("hurry up","急ぐ・急いで","熟語","Hurry up! The bus is coming.","急いで。バスが来ています。",["座って","待って","静かにして"],"大問2 Q20","hurry up"),
    ("tallest","最も背が高い","形容詞（最上級）","He is the tallest boy in our class.","彼はクラスで一番背が高い男の子です。",["最も速い","最も新しい","最も小さい"],"大問3 Q21","tallest"),
    ("begin to","～し始める","熟語","We began to study English last year.","私たちは去年、英語を勉強し始めました。",["～するのをやめる","～しなければならない","～するのが得意だ"],"大問3 Q24","began to"),
    ("a glass of","コップ一杯の～","熟語","Can I have a glass of juice?","ジュースをコップ一杯もらえますか。",["1枚の～","1足の～","1週間の～"],"大問3 Q25","a glass of"),
    ("sale","セール・特売","名詞","The shoe sale starts on Friday.","靴のセールは金曜日に始まります。",["会議","試験","旅行"],"大問4A","sale"),
    ("70% off","70％引き","表現","This cap is 70% off today.","この帽子は今日70％引きです。",["70ドル","70％の値上げ","70個"],"大問4A","70% off"),
    ("each","それぞれ・1つにつき","副詞・代名詞","These pens are two dollars each.","これらのペンは1本2ドルです。",["一緒に","合計で","一度だけ"],"大問4A","each"),
    ("pumpkin pie","パンプキンパイ","名詞","My sister made a pumpkin pie.","姉（妹）がパンプキンパイを作りました。",["野球帽","水泳帽","校歌"],"大問4B","pumpkin pie"),
    ("study abroad","留学する","熟語","My brother wants to study abroad.","兄（弟）は留学したいと思っています。",["家に帰る","電車に乗る","図書館へ行く"],"大問4C","studied abroad"),
    ("nervous about","～に不安を感じる","熟語","I am nervous about the test.","私は試験に不安を感じています。",["～が得意だ","～を楽しみにする","～に興味がある"],"大問4C","nervous about"),
    ("museum","博物館・美術館","名詞","We visited a museum on Sunday.","私たちは日曜日に博物館を訪れました。",["駅","公園","学校"],"大問4C","museum"),
]


def vocabulary():
    result=[]
    for i,(word,meaning,pos,example,ja,distractors,source,form) in enumerate(VOCAB,1):
        slug=re.sub(r"[^a-z0-9]+","_",word.lower()).strip("_")
        result.append(dict(word=word,meaning=meaning,pos=pos,level="4級",example=example,
                           exampleJa=ja,distractors=distractors,source=source,sourceForm=form,
                           wordAudio=f"audio/vocab/w_{i:03}_{slug}.mp3",exampleAudio=f"audio/vocab/ex_{i:03}_{slug}.mp3"))
    return result


def lessonplan(sections):
    import importlib.util
    from pathlib import Path
    spec=importlib.util.spec_from_file_location("order",Path(__file__).with_name("gen_g4_2026-2_sat_order.py"))
    o=importlib.util.module_from_spec(spec);spec.loader.exec_module(o)
    qs=[q for s in sections for q in s.get("questions",[])]
    def filled(n):
        q=next(q for q in qs if q["number"]==n)
        return o.completed(q) if "words" in q else q["text"].replace("(　)",q["choices"][q["answer"]-1])
    specs=[
        dict(title="単語は「セット」で覚える",subtitle="Vocabulary & Useful Phrases",color="#4f8cff",label="語句のセット",
             explanation="単語の意味だけでなく、隣の語とセットで覚える。Q4 は tell＋人＋stories、Q8 は for a long time、Q9 は look like、Q10 は talk with、Q11 は fine with me、Q12 は again and again。Q13 は went に合わせて drank という過去形、Q14 は her boots を Hers に置き換える。Q15 の have to の後ろは原形 go。意味のつながりを先に読み、形を最後に確かめよう。",
             simple="たんごは、おとなりのことばといっしょにおぼえよう。for a long time は『ながいあいだ』。again and again は『なんどもなんども』。have to のあとは、もとの形だよ。",
             source="大問1 Q4・Q8・Q12",quote="He often tells us funny stories in his lessons. / I watched her for a long time. / I want to listen to it again and again.",
             examples=[("He often tells us funny stories in his lessons.","先生は授業でよく私たちに面白い話をします。","tell＋人＋stories の順に並べる。","だれに、どんなおはなしをするかをつなごう。"),
                       ("I watched her for a long time.","私は長い間、祖母を見ていました。","for＋時間で期間を示す。at は時刻、by は期限。","for a long time をひとつのセットにしよう。"),
                       ("I want to listen to it again and again.","私はそれを何度も繰り返し聴きたいです。","again and again の and は固定。","まんなかの and をわすれないでね。")],
             passage="[出典: 大問1 Q8]\n"+filled(8)+"\n\n[出典: 大問1 Q12]\n"+filled(12),
             passageJa="日曜に祖母がクッキーを作り、私は長い間見ていた。祖母のクッキーが大好き。誕生日にもらったCDが気に入り、何度も聴きたい。",
             patterns=["funny stories","a long time","again","have to","with me"],
             questions=[("Q8で at ではなく for を選ぶのはなぜ？","a long time は時刻ではなく、見ていた時間の長さだから。for＋期間にする。"),
                        ("Q13で drank を使う根拠は？","後ろの went back が過去の出来事。水を飲むことも同じ過去なので drink の過去形 drank。"),
                        ("Q14で Her ではなく Hers を選ぶのはなぜ？","Hers だけで her boots を表せる。Her は『彼女の』なので後ろに名詞が必要。")],
             easyQuestions=[("ながいあいだ、はどのセット？","for a long time だよ。"),("なんどもなんども、は？","again and again だよ。"),("have to のあとは、どの形？","go など、もとの形だよ。")]),
        dict(title="会話は「次のセリフ」で選ぶ",subtitle="Conversation Clues",color="#34d399",label="会話の手がかり",
             explanation="空所の後ろから読むと、答えの役割が分かる。Q16 の Yes, please. は勧めを受ける返答なので、おかわりの質問。Q18 の it's in my bag は持ち物の場所なので umbrella。Q19 の It's too difficult. は本が読めない理由。Q17 は会議の時刻だから must go now、Q20 は遅刻しているから hurry up。前後の発言が一つの話題としてつながるか確認する。",
             simple="つぎのセリフがヒント。『はい、おねがいします』は、おかわり。『かばんにあるよ』は、かさ。『むずかしすぎる』は、ほんがよめないりゆうだね。",
             source="大問2 Q16・Q18・Q19",quote="Do you want some more? / Yes, please. / Did you bring your umbrella? / Yes, it's in my bag. / I can't read this book. / It's too difficult.",
             examples=[("Do you want some more?","もう少し欲しいですか。","次の Yes, please. が食べ物の勧めへの返答。","おかわりをすすめているよ。"),
                       ("Did you bring your umbrella?","傘を持ってきましたか。","it は umbrella。in my bag と置き場所を答える。","かばんのなかにあるのは、かさだね。"),
                       ("I can't read this book. It's too difficult.","この本が読めません。難しすぎます。","難しい本→読めない、という理由のつながり。","むずかしいから、よめないんだね。")],
             passage="[出典: 大問2 Q16]\n"+filled(16)+"\n\n[出典: 大問2 Q18]\n"+filled(18)+"\n\n[出典: 大問2 Q19]\n"+filled(19),
             passageJa="娘はスープを褒め、おかわりの勧めに『はい、お願いします』。雨なので傘を持参したか聞くと、かばんにあるという返答。本が難しくて読めないので悲しそう。",
             patterns=["Yes, please.","in my bag","It's too difficult.","It's time for the meeting.","You're late for school."],
             questions=[("Q16でスプーンの持ち主を聞く選択肢が合わないのは？","Yes, please. は申し出を受ける返答。持ち主の確認ではない。"),
                        ("Q18の it は何を指す？","持ってきた umbrella。雨の好みや寒さが、かばんに入っているわけではない。"),
                        ("Q20で hurry up を選ぶ根拠は？","You're late for school. と遅刻を知らせ、娘が I'm coming. と応じている。")],
             easyQuestions=[("Yes, please. はどんないみ？","はい、おねがいします、だよ。"),("かばんのなかにあるのは？","かさだよ。"),("hurry up はどんないみ？","いそいで、だよ。")]),
        dict(title="並べ替え——5つの「型」を知る",subtitle="Five Sentence Patterns",color="#a78bfa",label="整序の型",
             explanation="Q21 は Who is the tallest in ...? という最上級の疑問文。Q22 は rode his bike to school＋when 節。Q23 は Stop watching TV and go to bed. という2つの命令。Q24 は began to sing、Q25 は was drinking＋a glass of water。『his bike』『go to』『school song』『a glass』はそれぞれ1つの語句で、語数ではなく5つの語句の位置を数える。固定の Ian / The students / Ryan や文末は数えない。完成文を作ってから、空所内の2番目と4番目を選択肢と照合する。",
             simple="5つのことばのかたまりをならべよう。his bike や a glass は、2つにわけないよ。さいしょからかいてある Ian などは、ばんごうにかぞえない。あきの2ばんめと4ばんめをたしかめよう。",
             source="大問3 Q21～Q25（並べ替え後の完成文）",quote="Who is the tallest in your class? / The students began to sing their school song. / Ryan was drinking a glass of water in the kitchen.",
             examples=[(filled(21),"あなたのクラスで一番背が高いのはだれですか。","who→is→the tallest→in。2番目⑤is、4番目④tallest。","2ばんめ is、4ばんめ tallest だね。"),
                       (filled(24),"生徒たちは校歌を歌い始めました。","began to sing をセットにする。2番目①to、4番目④their。","うたいはじめた、は began to sing だよ。"),
                       (filled(25),"ライアンは台所で水を一杯飲んでいました。","was drinking と a glass of water。2番目②drinking、4番目③of。","a glass はひとつのかたまりだよ。")],
             passage="\n\n".join(f"[出典: 大問3 Q{n} 完成文]\n"+filled(n) for n in range(21,26)),
             passageJa="クラスで一番背が高いのはだれか。イアンは中学生の時、自転車で学校へ行った。マイクにテレビをやめて寝るよう命令する。生徒たちは校歌を歌い始めた。ライアンは台所で水を一杯飲んでいた。",
             patterns=["go to","his bike","school song","a glass","was"],
             questions=[("Q22の2番目が his bike になるのはなぜ？","空所の並びは rode→his bike→to→school→when。固定の Ian は数えず、his bike 全体が2番目。"),
                        ("Q23は stop の後ろに何を置く？","watching。stop watching TV で『テレビを見るのをやめる』。and で go to bed につなぐ。"),
                        ("Q25の2番目・4番目は？","was→drinking→a glass→of→water なので、②drinking と③of。選択肢3。")],
             easyQuestions=[("a glass は2つにわける？","わけないよ。1つのかたまりだね。"),("さいしょの Ryan もかぞえる？","かぞえないよ。あいている5つのところだけだね。"),("どこをこたえる？","あいているところの2ばんめと4ばんめだよ。")]),
        dict(title="読解——お知らせ・メール・物語の読み分け",subtitle="Notice, E-mail & Story Reading",color="#f472b6",label="読解キーワード",
             explanation="【お知らせ】値段と品物、セールの日と開店日を分ける。10ドルはボール、5ドルは水泳帽、2号店は9月11日。【メール】差出人を確認。Charlotte は猫の仮装とパイ作り、William は野球選手の仮装。William の土曜は帽子購入、日曜は空いている。【物語】Aya はフランス語を学び、飛行機を不安に感じた。パリの美術館は公園の中。帰国後に絵を習い、今は毎週末美術館へ行く。人物・時期・行動をセットにして根拠の文へ戻る。",
             simple="お知らせは、ねだんとひづけ。メールは、だれのよていか。ものがたりは、パリにいたとき・かえってから・いまをわけよう。アヤは、いままいしゅうまつびじゅつかんにいくよ。",
             source="大問4A・4B・4C",quote="Soccer balls will be $10 each / will open on September 11 / I am going to buy a new cap on Saturday / Aya started taking painting lessons / visits museums every weekend",
             examples=[("Soccer balls will be $10 each, and swimming caps will be $5 each!","サッカーボールは1個10ドルで、水泳帽は1個5ドルです。","品物と価格を一対一で対応させる。","ボール10ドル、ぼうし5ドルだね。"),
                       ("I am going to buy a new cap on Saturday.","私は土曜日に新しい帽子を買う予定です。","2通目の差出人 William の土曜日の予定。","ウィリアムのどようびは、ぼうしをかうひ。"),
                       ("Now, Aya studies French harder than before and visits museums every weekend.","今アヤは以前より熱心にフランス語を学び、毎週末美術館を訪れます。","Now と every weekend で現在の習慣を探す。","いままいしゅうまつに、することだよ。")],
             passage="[出典: 大問4A]\n"+" ".join(sections[3]["passages"][0]["paragraphs"][1:])+"\n\n[出典: 大問4B 第2のメール]\n"+" ".join(sections[3]["passages"][1]["sentencePairs"][19+i][0] for i in range(5))+"\n\n[出典: 大問4C 最終段落]\n"+sections[3]["passages"][2]["paragraphs"][2],
             passageJa="【お知らせ】グローブとラケットは70％引き。ボール10ドル、水泳帽5ドル。2号店は9月11日開店。\n【メール】ウィリアムは野球選手の仮装をし、土曜に帽子を買う。日曜は空いていて、一緒にパイを作りたい。お菓子を持参する。\n【物語】パリ滞在後、アヤは高校の友人と絵を習い、上達した。絵と手紙をホストファミリーに送った。今はフランス語を熱心に学び、毎週末美術館へ。将来は画家になりフランスに住みたい。",
             patterns=["$10 each","September 11","on Saturday","on Sunday","nervous about taking a plane","in a large park","After her stay in Paris","visits museums every weekend"],
             questions=[("Q27で8月28日・29日を選ばない理由は？","セールの日付だから。2号店の開店は September 11。"),
                        ("Q28で野球選手ではなく猫を選ぶ理由は？","Charlotte の希望を聞く問題。野球選手は William の希望で、差出人が違う。"),
                        ("Q34とQ35で時期をどう区別する？","Q34 はパリ滞在後に始めた絵のレッスン。Q35 は今の毎週末の美術館訪問。")],
             easyQuestions=[("10ドルになるのは？","サッカーボールだよ。"),("シャーロットは、なにになりたい？","ねこだよ。"),("アヤは、いままいしゅうまつどこへいく？","びじゅつかんだよ。")]),
    ]
    points=[]
    for n,s in enumerate(specs,1):
        points.append(dict(id=f"fp{n}",title=s["title"],subtitle=s["subtitle"],explanation=s["explanation"],
                           explanationSimple=s["simple"],sourceQuote=s["quote"],sourceLocation=s["source"],
                           sourceQuoteAudio=f"audio/fp{n}_source.mp3",
                           examples=[dict(en=en,ja=ja,note=note,noteSimple=easy,audio=f"audio/fp{n}_ex{i}.mp3") for i,(en,ja,note,easy) in enumerate(s["examples"],1)],
                           practicePassage=dict(en=s["passage"],ja=s["passageJa"],source=s["source"],audioFile=f"audio/practice_pp{n}.mp3"),
                           highlightPatterns=s["patterns"],highlightColor=s["color"],highlightLabel=s["label"],
                           practiceQuestions=[dict(q=q,a=a) for q,a in s["questions"]],
                           practiceQuestionsSimple=[dict(q=q,a=a) for q,a in s["easyQuestions"]]))
    return dict(title="今回の4つの学習ポイント",focusPoints=points)

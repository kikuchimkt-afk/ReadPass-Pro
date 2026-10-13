"""Grade 4's existing 30-word / four-focus-point / normal-and-easy format (2026-2, main venue).

Audio references are added later by data/grade4/2026-2/_gen_tts.py.
"""

VOCAB=[
    ("band","バンド・楽団","名詞","My brother plays the drums in a band.","兄（弟）はバンドでドラムを演奏しています。",["頂上","時間","部分"],"大問1 Q1","band"),
    ("little","年下の・小さい","形容詞","My little sister is five years old.","私の妹は5歳です。",["長い","背の高い","左の"],"大問1 Q2","little"),
    ("forget","忘れる","動詞","Don't forget to bring your lunch.","お弁当を持ってくるのを忘れないで。",["見つける","聞こえる","横切る"],"大問1 Q3","forgets"),
    ("magazine","雑誌","名詞","I read a music magazine every month.","私は毎月、音楽雑誌を読みます。",["サンドイッチ","山","競技場"],"大問1 Q4","magazine"),
    ("brush","（ブラシで）磨く","動詞","I brush my teeth after breakfast.","私は朝食の後に歯を磨きます。",["従う","育てる","動かす"],"大問1 Q5","Brush"),
    ("send","送る","動詞","I will send you a photo.","あなたに写真を送ります。",["買う","掃除する","止める"],"大問1 Q6","send"),
    ("housework","家事","名詞","I help my mother with the housework.","私は母の家事を手伝います。",["天気","物語","故郷"],"大問1 Q7","housework"),
    ("take a walk","散歩する","熟語","We take a walk in the park every Sunday.","私たちは毎週日曜日に公園を散歩します。",["昼寝する","買い物をする","泳ぐ"],"大問1 Q8","take a short walk"),
    ("trip","旅行","名詞","We went on a trip to Kyoto.","私たちは京都へ旅行に行きました。",["音楽","プレゼント","花"],"大問1 Q9","trip"),
    ("in the afternoon","午後に","熟語","I play soccer in the afternoon.","私は午後にサッカーをします。",["朝に","夜に","正午に"],"大問1 Q10","in the afternoon"),
    ("Just a minute.","ちょっと待って。","表現","Just a minute. I'm coming.","ちょっと待って。今行きます。",["どうぞ。","いいですね。","ありがとう。"],"大問1 Q11","Just a minute"),
    ("become friends with","～と友達になる","熟語","I became friends with a girl from Australia.","私はオーストラリア出身の女の子と友達になりました。",["～とけんかする","～を待つ","～を助ける"],"大問1 Q12","friends with"),
    ("could","（Could I ～? で）～してもよいですか","助動詞","Could I open the window?","窓を開けてもいいですか。",["～しなければならない","～するつもりだ","～したことがある"],"大問1 Q13","Could I use"),
    ("better","（like ～ better で）～のほうが好き","副詞","I like summer better than winter.","私は冬より夏のほうが好きです。",["最もよく","とても","少し"],"大問1 Q15","better"),
    ("enjoy","楽しむ","動詞","I enjoyed the movie very much.","私はその映画をとても楽しみました。",["忘れる","送る","磨く"],"大問2 Q16","enjoyed"),
    ("expensive","値段が高い","形容詞","This watch is too expensive for me.","この腕時計は私には高すぎます。",["安い","寒い","新しい"],"大問2 Q18","expensive"),
    ("be back","戻る","熟語","I'll be back in ten minutes.","10分で戻ります。",["出発する","起きる","寝る"],"大問2 Q19","be back"),
    ("practice","練習","名詞","We have basketball practice after school.","放課後にバスケットボールの練習があります。",["試合","制服","休日"],"大問2 Q20","practice"),
    ("sure","確かな（I'm not sure. で「よく分からない」）","形容詞","I'm not sure about the answer.","答えに自信がありません。",["うれしい","忙しい","眠い"],"大問2 Q20","not sure"),
    ("quiet","静かな","形容詞","Please be quiet in the classroom.","教室では静かにしてください。",["うるさい","忙しい","明るい"],"大問3 Q22","quiet"),
    ("leave","出る・出発する","動詞","My father leaves home at seven.","父は7時に家を出ます。",["着く","泊まる","戻る"],"大問3 Q23","left home"),
    ("kind","種類","名詞","This shop sells many kinds of bread.","この店はたくさんの種類のパンを売っています。",["色","値段","大きさ"],"大問3 Q24","kinds of"),
    ("too ... for ～","～には…すぎる","熟語","This bag is too heavy for me.","このかばんは私には重すぎます。",["～のために…する","～と同じくらい…","～より…"],"大問3 Q25","too big for"),
    ("nurse","看護師（school nurse で保健室の先生）","名詞","The nurse helped me when I was sick.","具合が悪いとき、看護師さんが助けてくれました。",["料理人","画家","運転手"],"大問4A","school nurse"),
    ("introduce","紹介する","動詞","She introduced herself to the class.","彼女はクラスで自己紹介をしました。",["招待する","説明する","訪ねる"],"大問4A","introduced herself"),
    ("healthy","健康によい・健康な","形容詞","Fruit is healthy food.","果物は健康によい食べ物です。",["危険な","高価な","古い"],"大問4A","healthy meals"),
    ("holiday","休日","名詞","Next Monday is a holiday.","次の月曜日は休日です。",["誕生日","試験","練習"],"大問4B","school holiday"),
    ("closed","閉まっている","形容詞","The shop is closed on Sundays.","その店は日曜日は閉まっています。",["開いている","混んでいる","新しい"],"大問4B","closed on Tuesdays"),
    ("surprised","驚いた","形容詞","I was surprised at the news.","私はその知らせに驚きました。",["怒った","疲れた","退屈した"],"大問4C","surprised"),
    ("hobby","趣味","名詞","My hobby is taking photos.","私の趣味は写真を撮ることです。",["宿題","夢","仕事"],"大問4C","hobby"),
]


def vocabulary():
    return [dict(word=word,meaning=meaning,pos=pos,level="4級",example=example,exampleJa=ja,distractors=distractors,
                 source=source,sourceForm=form) for word,meaning,pos,example,ja,distractors,source,form in VOCAB]


def lessonplan(sections):
    import importlib.util
    from pathlib import Path
    spec=importlib.util.spec_from_file_location("order",Path(__file__).with_name("gen_g4_2026-2_order.py"))
    o=importlib.util.module_from_spec(spec);spec.loader.exec_module(o)
    qs=[q for s in sections for q in s.get("questions",[])]
    def filled(n):
        q=next(q for q in qs if q["number"]==n)
        return o.completed(q) if "words" in q else q["text"].replace("(　)",q["choices"][q["answer"]-1])
    def excerpt(label,rows):return f"[出典: {label}]\n"+" ".join(r[0] for r in rows)
    pa,pb,pc=[p["sentencePairs"] for p in sections[3]["passages"]]
    specs=[
        dict(title="語句のセットと動詞の形を確かめる",subtitle="Word Partners & Verb Forms",color="#4f8cff",label="語句のセット",
             explanation="大問1は空所の前後の語とセットで考える。Q1 は rock band、Q5 は brush your teeth、Q7 は do the housework、Q8 は take a walk、Q9 は go on a trip、Q12 は become friends with。前置詞は Q10 の in the afternoon。動詞の形では、Q14 は rained に合わせた過去の否定 didn't＋原形 go、Q15 は Which ～ better, A or B? で2つを比べる。",
             simple="ことばは、となりのことばといっしょにおぼえよう。brush your teeth は『はをみがく』、take a walk は『さんぽする』。in the afternoon は『ごごに』だよ。didn't のあとは go のような、もとの形だね。",
             source="大問1 Q5・Q14・Q15",quote="Brush your teeth before you go to bed. / Well, it rained all weekend, so we didn't go camping. / Which cake did you like better, the chocolate cake or the lemon cake?",
             examples=[(filled(5),"A：寝る前に歯を磨きなさい。\nB：分かっているよ、お母さん。","brush your teeth で『歯を磨く』。命令文なので動詞の原形 Brush で始める。","はをみがく、は brush your teeth だよ。"),
                       (filled(14),"A：週末はどうでしたか。\nB：ええと、週末ずっと雨が降ったので、キャンプに行きませんでした。","rained と同じ過去の話なので didn't。didn't の後ろは動詞の原形 go。wasn't や weren't の後ろに go は置けない。","むかしのことだから didn't。そのあとは go のままだよ。"),
                       (filled(15),"A：チョコレートケーキとレモンケーキ、どちらのケーキのほうが好きでしたか。\nB：レモンのほうです。","Which ～ did you like better, A or B? で2つを比べる。better は well の比較級。","2つをくらべて『どっちがすき？』は better をつかうよ。")],
             passage="\n\n".join(f"[出典: 大問1 Q{n}]\n"+filled(n) for n in [1,5,7,8,9,12]),
             passageJa="【Q1】ロックバンドに入っていて、ギターを弾く。\n【Q5】寝る前に歯を磨きなさい。\n【Q7】ウィリアムズ夫妻は共働きなので、週末に一緒に家事をする。\n【Q8】夕食の前に少し散歩しよう。\n【Q9】この夏、フランスへ旅行に行く。\n【Q12】カナダで何人かの生徒と仲良くなった。",
             patterns=["rock band","Brush your teeth","do the housework","take a short walk","go on a trip","friends with"],
             questions=[("Q8で take を選ぶ理由は？","take a walk で『散歩する』というセットだから。a short walk の short は walk を説明している。"),
                        ("Q14で didn't を選ぶ理由は？","rained から過去の話と分かる。後ろの go は原形なので、一般動詞の過去の否定 didn't を使う。"),
                        ("Q15の better は何と何を比べている？","the chocolate cake と the lemon cake。Which ～ better, A or B? で『AとBのどちらのほうが～』。")],
             easyQuestions=[("take a walk はどんないみ？","さんぽする、だよ。"),("go on a trip はどんないみ？","りょこうにいく、だよ。"),("in the afternoon はどんないみ？","ごごに、だよ。")]),
        dict(title="会話は空所の前後のセリフをつなげて考える",subtitle="Linking Lines in Conversations",color="#34d399",label="会話のつながり",
             explanation="大問2は空所の前後をつなげて読む。Q16 は Thank you for coming というお礼への返事なので You're welcome。Q17 は Not today. の理由として It's going to rain。Q18 は No, it's only $60. という答えから、値段を尋ねる Is it expensive?。Q19 は at the library now に続く She'll be back soon。Q20 は Let's ask Mr. Smith. から、練習があるか分からない I'm not sure。",
             simple="あなのまえとあとのセリフをつなげよう。『ありがとう』には『どういたしまして』。『きょうはだめ』のりゆうは『あめがふりそう』。『ううん、60ドルだけ』なら『たかいの？』ときいたんだね。",
             source="大問2 Q16・Q18・Q20",quote="You're welcome. I enjoyed it very much. / Is it expensive? / I'm not sure. Let's ask Mr. Smith.",
             examples=[(filled(16),"男の子：ぼくの野球の試合に来てくれてありがとう、ジムおじさん。\nおじ：どういたしまして。とても楽しかったよ。","Thank you for ～ing というお礼への返事は You're welcome.。Yes, please. は勧められたものを受けるときの返事。","ありがとう、には『どういたしまして』だね。"),
                       (filled(18),"女性1：このコートが大好き。買うつもりよ。\n女性2：それは高いの？\n女性1：ううん、たった60ドルよ。","No, it's only $60. は『高くない』という答え。値段について Yes/No で尋ねる Is it expensive? が合う。","『たった60ドル』だから、たかいかきいたんだね。"),
                       (filled(20),"男の子：今日は雨が降っているね。サッカーの練習はあるのかな。\n女の子：よく分からないわ。スミスさんに聞いてみよう。","Let's ask Mr. Smith. は、自分では分からないのでスミスさんに聞こうという提案。I'm not sure. とつながる。","わからないから、スミスさんにきくんだね。")],
             passage="\n\n".join(f"[出典: 大問2 Q{n}]\n"+filled(n) for n in range(16,21)),
             passageJa="【Q16】試合に来てくれたお礼を言われ、どういたしましてと答える。\n【Q17】今日は雨が降りそうなので、テニスはしない。\n【Q18】コートは高いか尋ね、たった60ドルだと答える。\n【Q19】母は今図書館にいて、すぐに戻る。\n【Q20】練習があるか分からないので、スミスさんに聞く。",
             patterns=["You're welcome.","It's going to rain.","Is it expensive?","She'll be back soon.","I'm not sure."],
             questions=[("Q16で Yes, please. が合わない理由は？","Yes, please. は何かを勧められたときの返事。ここは Thank you というお礼への返事なので You're welcome.。"),
                        ("Q17で It's going to rain. を選ぶ理由は？","Not today.（今日はだめ）の理由になるから。雨が降りそうなので、テニスをしない。"),
                        ("Q19で She'll be back soon. が合う理由は？","母は今図書館にいると答えた後なので、『すぐに戻る』と続けると自然。")],
             easyQuestions=[("You're welcome. はどんないみ？","どういたしまして、だよ。"),("It's going to rain. はどんないみ？","あめがふりそう、だよ。"),("I'm not sure. はどんないみ？","よくわからない、だよ。")]),
        dict(title="並べ替え——動詞を見つけて意味のまとまりを作る",subtitle="Verbs & Word Groups",color="#a78bfa",label="整序のまとまり",
             explanation="まず主語と動詞を決め、意味のまとまりを作ってから並べる。Q21 は practiced kicking the ball（practice＋～ing）に before the soccer game。Q22 は You must be quiet（助動詞＋be＋形容詞）。Q23 は left home for school（家を出て学校へ向かう）。Q24 は That shop has many kinds of ice cream、Q25 は This desk is too big for Jack（too＋形容詞＋for＋人）。",
             simple="さいしょに『だれが』『どうする』をきめよう。practiced kicking は『けるれんしゅうをした』、must be quiet は『しずかにしなければならない』。too big for Jack は『ジャックにはおおきすぎる』だよ。",
             source="大問3 Q21～Q25（並べ替え後の完成文）",quote="Peter practiced kicking the ball before the soccer game. / You must be quiet in the library. / This desk is too big for Jack.",
             examples=[(filled(21),"ピーターはサッカーの試合の前にボールを蹴る練習をしました。","practice＋～ing で『～する練習をする』。2番目②kicking、4番目⑤before。","2ばんめ kicking、4ばんめ before だね。"),
                       (filled(23),"私は昨日の朝、5時に家を出て学校へ向かいました。","leave home for school で『家を出て学校へ向かう』。2番目⑤home、4番目②school。","left home for school がひとつのながれだよ。"),
                       (filled(25),"この机はジャックには大きすぎます。","too＋形容詞＋for＋人 で『人には～すぎる』。2番目①is、4番目③big。","too big for Jack は『ジャックにはおおきすぎる』だよ。")],
             passage="\n\n".join(f"[出典: 大問3 Q{n} 完成文]\n"+filled(n) for n in range(21,26)),
             passageJa="ピーターはサッカーの試合の前にボールを蹴る練習をした。図書館では静かにしなければならない。私は昨日の朝5時に家を出て学校へ向かった。あの店にはたくさんの種類のアイスクリームがある。この机はジャックには大きすぎる。",
             patterns=["practiced kicking","must be quiet","left home for school","many kinds of","too big for"],
             questions=[("Q22の2番目と4番目は？","You→must→be→quiet→in なので、②must と④quiet。選択肢1。"),
                        ("Q23で home の後ろに for school を置く理由は？","leave home は『家を出る』、for school は『学校へ向かって』。家を出て学校へ向かう流れになる。"),
                        ("Q24で many kinds of の順になるのはなぜ？","many は kinds を前から説明し、of の後ろに ice cream が続く。many kinds of ～で『たくさんの種類の～』。")],
             easyQuestions=[("must be quiet はどんないみ？","しずかにしなければならない、だよ。"),("many kinds of はどんないみ？","たくさんのしゅるいの、だよ。"),("どこをこたえる？","あいているところの2ばんめと4ばんめだよ。")]),
        dict(title="読解——人物・時・場所を正しく結びつける",subtitle="Who, When & Where",color="#f472b6",label="読解キーワード",
             explanation="【掲示】Ms. Brown が昨日したのは自己紹介。健康的な食事の話は来週の月曜日で、場所は meeting room（art room の隣）。【メール】Tom がふだん行くのは公園。祖父が昨日行ったのは新しい博物館で、動物園と野球場は火曜日が休み。祖母は火曜日にアップルパイを作る。【物語】姉は大学で美術を学ぶ。雲は飛行機のように見えた。母は写真を勧め、Kelly は部員と山へ、村と祭りには一人で行った。お気に入りは古い家の写真。",
             simple="だれが、いつ、どこで、をたしかめよう。ブラウンせんせいは、きのうじこしょうかいをしたよ。トムのおじいさんは、きのうはくぶつかんへいった。ケリーがぶいんといったのは、やまだね。",
             source="大問4A・4B・4C",quote="She introduced herself to everyone yesterday. / I visited there yesterday! / After joining the club, she went to a mountain with the other members of her club.",
             examples=[(pa[2][0],pa[2][1],"yesterday がQ26の手がかり。健康的な食事の話は Next Monday の予定で、時期が違う。","きのうしたのは、じこしょうかいだよ。"),
                       (pb[22][0]+" "+pb[23][0],pb[22][1]+pb[23][1],"there は前の文の the new museum を指す。祖父が昨日訪れたのは博物館。","there は、あたらしいはくぶつかんのことだね。"),
                       (pc[12][0]+" "+pc[13][0],pc[12][1]+pc[13][1],"部員と行ったのは a mountain。村と祭りは alone（一人で）訪れた場所。","ぶいんといったのはやま。むらとまつりは、ひとりでいったよ。")],
             passage=excerpt("大問4A",pa[1:6])+"\n\n"+excerpt("大問4B 第2のメール",pb[19:26])+"\n\n"+excerpt("大問4C 第3段落",pc[11:15]),
             passageJa="【掲示】新しい保健室の先生のブラウン先生は先週この高校に来て、昨日みんなに自己紹介をした。来週の月曜日の放課後、生徒のための健康的な食事について話す。時間は午後3時30分から4時30分、場所は美術室の隣の会議室。\n【第2のメール】祖父の町には動物園も野球場もあるが、どちらも火曜日は休み。祖父は新しい博物館を勧め、昨日そこを訪れた。博物館の後は友達を家に連れておいで。祖母は火曜日にアップルパイを作る。\n【物語の第3段落】ケリーは写真部に入り、部員と山へ行った。村と祭りには一人で行った。たくさん写真を撮ったが、お気に入りは古い家の写真。",
             patterns=["introduced herself","next to the art room","closed on Tuesdays","visited there yesterday","an apple pie","looked like a plane","with the other members","an old house"],
             questions=[("Q27で art room を選ばない理由は？","art room は会議室の場所を説明する語。行くのは The meeting room（美術室の隣）。"),
                        ("Q29で動物園や野球場を選ばない理由は？","どちらも火曜日は休みとあるだけ。祖父が昨日訪れたのは the new museum。"),
                        ("Q34で village や festival を選ばない理由は？","村と祭りには alone（一人で）行った。部員と行ったのは a mountain。")],
             easyQuestions=[("ブラウンせんせいがきのうしたことは？","みんなにじこしょうかいをしたよ。"),("トムのおばあさんがかようびにつくるものは？","アップルパイだよ。"),("ケリーのおきにいりのしゃしんは？","ふるいいえのしゃしんだよ。")]),
    ]
    points=[]
    for n,s in enumerate(specs,1):
        points.append(dict(id=f"fp{n}",title=s["title"],subtitle=s["subtitle"],explanation=s["explanation"],
                           explanationSimple=s["simple"],sourceQuote=s["quote"],sourceLocation=s["source"],
                           examples=[dict(en=en,ja=ja,note=note,noteSimple=easy) for en,ja,note,easy in s["examples"]],
                           practicePassage=dict(en=s["passage"],ja=s["passageJa"],source=s["source"]),
                           highlightPatterns=s["patterns"],highlightColor=s["color"],highlightLabel=s["label"],
                           practiceQuestions=[dict(q=q,a=a) for q,a in s["questions"]],
                           practiceQuestionsSimple=[dict(q=q,a=a) for q,a in s["easyQuestions"]]))
    return dict(title="今回の4つの学習ポイント",focusPoints=points)

"""Grade 4's existing 30-word / four-focus-point / normal-and-easy format."""
import re

VOCAB=[
    ("full","いっぱいの・満腹の","形容詞","The bus was full this morning.","今朝、バスは満員でした。",["空の","安い","遅い"],"大問1 Q1","full"),
    ("large","大きい・広い","形容詞","We live in a large house.","私たちは大きな家に住んでいます。",["小さい","古い","新しい"],"大問1 Q2","large"),
    ("grow","育てる","動詞","My grandmother grows tomatoes.","祖母はトマトを育てています。",["売る","洗う","切る"],"大問1 Q2","grow"),
    ("draw","（絵を）描く","動詞","Please draw a picture of your family.","あなたの家族の絵を描いてください。",["料理する","教える","聞く"],"大問1 Q3","drawing"),
    ("wind","風","名詞","The wind is cold today.","今日は風が冷たいです。",["雨","雪","雲"],"大問1 Q4","wind"),
    ("cloudy","くもりの","形容詞","It was cloudy yesterday.","昨日はくもりでした。",["晴れた","雨の","雪の"],"大問1 Q5","cloudy"),
    ("lesson","レッスン・授業","名詞","I have a piano lesson on Fridays.","私は毎週金曜日にピアノのレッスンがあります。",["試合","宿題","休み"],"大問1 Q6","lesson"),
    ("favorite","いちばん好きな","形容詞","My favorite color is blue.","私のいちばん好きな色は青です。",["嫌いな","新しい","有名な"],"大問1 Q7","favorite"),
    ("take pictures","写真を撮る","熟語","We took pictures at the zoo.","私たちは動物園で写真を撮りました。",["絵を描く","手紙を書く","本を読む"],"大問1 Q8","taking pictures"),
    ("part","部分・部","名詞","I liked the last part of the movie.","私はその映画の最後の部分が気に入りました。",["店","世界","試合"],"大問1 Q9","part"),
    ("be interested in","～に興味がある","熟語","I'm interested in Japanese history.","私は日本の歴史に興味があります。",["～に怒っている","～の準備ができている","～が苦手だ"],"大問1 Q10","interested in"),
    ("on TV","テレビで","熟語","I watched a soccer game on TV.","私はテレビでサッカーの試合を見ました。",["ラジオで","映画館で","学校で"],"大問1 Q11","on TV"),
    ("make a friend","友だちを作る・友だちになる","熟語","I made a lot of friends at camp.","私はキャンプでたくさんの友だちができました。",["友だちとけんかする","友だちを待つ","友だちに手紙を書く"],"大問1 Q12","made a new friend"),
    ("right now","ちょうど今","熟語","I'm busy right now.","私はちょうど今、忙しいです。",["昨日","来週","いつも"],"大問1 Q13","right now"),
    ("hers","彼女のもの","代名詞","This pen is mine, and that one is hers.","このペンは私ので、あのペンは彼女のです。",["彼のもの","あなたのもの","私たちのもの"],"大問1 Q14","hers"),
    ("show","見せる","動詞","Please show me your notebook.","あなたのノートを見せてください。",["借りる","なくす","洗う"],"大問1 Q15","showed"),
    ("have to","～しなければならない","熟語","I have to clean my room today.","私は今日、部屋を掃除しなければなりません。",["～してもよい","～したい","～するのが好きだ"],"大問2 Q16","have to"),
    ("be good for","～によい・～のためになる","熟語","Milk is good for your bones.","牛乳は骨によいです。",["～に悪い","～が得意だ","～に遅れる"],"大問2 Q16","good for"),
    ("should","～したほうがよい","助動詞","You should go to bed early tonight.","今夜は早く寝たほうがいいですよ。",["～してはいけない","～できる","～したことがある"],"大問2 Q17","should"),
    ("pretty","かわいい・きれいな","形容詞","Your garden is very pretty.","あなたの庭はとてもきれいです。",["古い","重い","高い"],"大問2 Q18","pretty"),
    ("Here you are.","はい、どうぞ。","表現","Here you are. This is your ticket.","はい、どうぞ。これがあなたのチケットです。",["ありがとう。","ごめんなさい。","さようなら。"],"大問2 Q19","Here you are."),
    ("funny","おもしろい・おかしい","形容詞","That story was very funny.","その話はとてもおもしろかったです。",["悲しい","怖い","難しい"],"大問2 Q20","funny"),
    ("next to","～の隣に・～の隣の","熟語","The bank is next to the station.","銀行は駅の隣にあります。",["～の後ろに","～の向かいに","～の上に"],"大問3 Q22","next to"),
    ("be going to","～するつもりだ","熟語","I'm going to visit my aunt next week.","私は来週、おばを訪ねるつもりです。",["～したことがある","～しなければならない","～してもよい"],"大問3 Q23","going to"),
    ("closed","閉まっている・休業の","形容詞","The museum is closed on Mondays.","その博物館は毎週月曜日が休館日です。",["開いている","混んでいる","新しい"],"大問4A","closed"),
    ("look for","～を探す","熟語","I'm looking for my key.","私は鍵を探しています。",["～を見る","～の世話をする","～を楽しみにする"],"大問4A","looking for"),
    ("match","試合","名詞","Our team won the match.","私たちのチームはその試合に勝ちました。",["練習","会議","旅行"],"大問4B","match"),
    ("meeting","会議・ミーティング","名詞","We have a meeting after school.","放課後にミーティングがあります。",["試合","授業","休み"],"大問4B","meeting"),
    ("for the first time","初めて","熟語","I ate sushi for the first time.","私は初めてすしを食べました。",["もう一度","最後に","いつも"],"大問4C","for the first time"),
    ("look around","見て回る","熟語","Let's look around the museum.","博物館を見て回りましょう。",["～を探す","～の世話をする","～をあきらめる"],"大問4C","looked around"),
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
    spec=importlib.util.spec_from_file_location("order",Path(__file__).with_name("gen_g4_2025-3_sat_order.py"))
    o=importlib.util.module_from_spec(spec);spec.loader.exec_module(o)
    qs=[q for s in sections for q in s.get("questions",[])]
    def filled(n):
        q=next(q for q in qs if q["number"]==n)
        return o.completed(q) if "words" in q else q["text"].replace("(　)",q["choices"][q["answer"]-1])
    notice,email,story=sections[3]["passages"]
    specs=[
        dict(title="空所の前後と「セット」で考える",subtitle="Word Sets & Grammar Clues",color="#4f8cff",label="語句のセット",
             explanation="単語の意味だけでなく、空所の前後の語とのセットで答えを決める。Q8 は like taking pictures（写真を撮るのが好き）、Q10 は be interested in（～に興味がある）、Q11 は on TV（テレビで）、Q12 は make a friend の過去形を使った made a new friend。文法の問題も前後が手がかりになる。Q13 は she's（she is）と right now から現在進行形 eating、Q14 は母のセーターを指す hers、Q15 は Yesterday から過去形 showed。空所だけを見ず、前後の語や時を表す語と一緒に読もう。",
             simple="あなのまえとうしろを、いっしょによもう。interested in は『～にきょうみがある』。on TV は『テレビで』。Yesterday があれば、むかしの形だよ。",
             source="大問1 Q10・Q11・Q15",quote="What subject are you interested in at school? / Is there a good movie on TV tonight? / Yesterday, Anna showed me a lot of pictures of her family.",
             examples=[("What subject are you interested in at school?","学校では、どの教科に興味がありますか。","be interested in の in が文の後ろに残る。What subject（どの教科）が in の後ろに来る語にあたる。","interested in で『～にきょうみがある』だね。"),
                       ("Is there a good movie on TV tonight?","今夜、テレビでいい映画をやっていますか。","on TV で『テレビで（放送されて）』。for や by では、この意味にならない。","on TV は『テレビで』だよ。"),
                       ("Yesterday, Anna showed me a lot of pictures of her family.","昨日、アンナは私に家族の写真をたくさん見せてくれました。","Yesterday があるので過去形 showed。show＋人＋物で『人に物を見せる』。","きのうのことだから showed だね。")],
             passage="[出典: 大問1 Q12]\n"+filled(12)+"\n\n[出典: 大問1 Q15]\n"+filled(15),
             passageJa="飛行機の中で新しい友だちができた。彼女も高校生だ。昨日、アンナは私に家族の写真をたくさん見せてくれた。",
             patterns=["interested in","on TV","taking pictures","made a new friend","right now"],
             questions=[("Q10で interested を選ぶのはなぜ？","be interested in で『～に興味がある』。空所の後ろの in と合い、B も好きな教科（体育）を答えている。"),
                        ("Q13で eating を選ぶ根拠は？","she's は she is の短縮形。is の後ろに動詞の -ing 形を置くと『～しているところ』になり、right now（ちょうど今）とも合う。"),
                        ("Q14の hers は何を指す？","her sweater（母のセーター）。同じセーターだが、母のものは緑色だと言っている。")],
             easyQuestions=[("『～にきょうみがある』は、どのセット？","interested in だよ。"),("『テレビで』は、えいごで？","on TV だよ。"),("Yesterday があるとき、show はどうなる？","むかしの形の showed になるよ。")]),
        dict(title="会話は「返事」から逆に考える",subtitle="Conversation Clues",color="#34d399",label="会話の手がかり",
             explanation="空所の後ろの返事から、空所に入る文を考える。Q16 は母が Yes. They're good for you.（そうよ、体にいいのよ）と答えているので、食べなければいけないかを尋ねる Do I have to eat them?。Q17 は男の子が Thanks. とお礼を言うので、聞いてみるとよい人を教える You should ask Mr. Carter.。Q19 は Sure. Here you are.（いいよ、はいどうぞ）と物を渡しているので Can I see it, please?。Q20 は夫が Me, too. と答えているので、相手の気持ちを尋ねる How about you?。Q18 は新しいワンピースをほめる It's very pretty.。返事が空所の文にきちんと答えているかを確かめよう。",
             simple="あとのへんじがヒント。『いいよ、はいどうぞ』なら『みせて』。『ぼくも』なら『あなたはどう？』だね。",
             source="大問2 Q16・Q19・Q20",quote="Do I have to eat them? / Yes. They're good for you. / Can I see it, please? / Sure. Here you are. / How about you? / Me, too. It's really funny.",
             examples=[("Do I have to eat them?","それを食べなければいけないの？","have to で『～しなければならない』。them は carrots を指す。","たべなきゃだめ？ときいているよ。"),
                       ("Can I see it, please?","見せてもらってもいい？","Can I ～? で『～してもいいですか』。返事の Here you are. は物を渡すときの言葉。","みせて、とたのんでいるね。"),
                       ("How about you?","あなたはどう？","相手の考えや気持ちを尋ねる言い方。返事は Me, too.（ぼくもだよ）。","『あなたはどう？』だよ。")],
             passage="[出典: 大問2 Q16]\n"+filled(16)+"\n\n[出典: 大問2 Q19]\n"+filled(19)+"\n\n[出典: 大問2 Q20]\n"+filled(20),
             passageJa="息子はニンジンが好きではなく、食べなければいけないのかと尋ねる。母は『そうよ、体にいいのよ』と答える。女の子が男の子の新しい携帯電話を見せてほしいと頼むと、男の子は電話を渡す。妻がこのテレビ番組が好きだと言って夫の考えを尋ねると、夫も好きで、本当におもしろいと答える。",
             patterns=["have to eat","good for you","Here you are","How about you","Me, too"],
             questions=[("Q16で Let's go to a restaurant. が合わないのはなぜ？","母が Yes. They're good for you.（そうよ、体にいいのよ）と答えている。レストランへ行く提案への返事にはならない。"),
                        ("Q17で、男の子が Thanks. と言ったのはなぜ？","女の子が You should ask Mr. Carter.（カーターさんに聞いてみるといいよ）と、聞いてみるとよい人を教えてくれたから。"),
                        ("Q19で How much was it? を選ばないのは？","値段を聞かれたら金額を答える。返事は Sure. Here you are. で、物を渡している。")],
             easyQuestions=[("Here you are. は、どんなときにいう？","ものをわたすときだよ。"),("How about you? のいみは？","『あなたはどう？』だよ。"),("Q16 の them は、なに？","ニンジン（carrots）だよ。")]),
        dict(title="並べ替え——文の「骨組み」から組み立てる",subtitle="Five Sentence Patterns",color="#a78bfa",label="整序の型",
             explanation="Q21 は Please＋動詞の原形 tell＋人 us＋about ～（私たちに～について話してください）。Q22 は eats dinner の後ろに場所 at the restaurant を置き、next to her house（彼女の家の隣の）で説明を加える。Q23 は be going to＋動詞の原形（～するつもりだ）で、主語 My father に合わせて is。Q24 は have to＋動詞の原形（～しなければならない）の後ろに go to the post office。Q25 は Please don't＋動詞の原形（～しないでください）。『your trip』『the restaurant』『the post office』『go to』『Ms. Sato's』は1つの語句なので分けずに数える。最初から書かれている Please / Ai often eats / My / I や文末の語句は数えない。完成文を作ってから、2番目と4番目を選択肢と照らし合わせる。",
             simple="まず、ぶんのほねぐみをきめよう。have to や is going to のあとは、うごきのことばのもとの形だよ。go to や the post office は、ひとつのかたまりとしてかぞえるよ。",
             source="大問3 Q21～Q25（並べ替え後の完成文）",quote="Please tell us about your trip to Hokkaido. / My father is going to wash his car this weekend. / I have to go to the post office this afternoon.",
             examples=[(filled(21),"私たちにあなたの北海道旅行について話してください。","tell→us→about→your trip→to。2番目③us、4番目⑤your trip。","2ばんめ us、4ばんめ your trip だね。"),
                       (filled(23),"私の父は今週末，車を洗うつもりです。","father→is→going→to→wash。2番目⑤is、4番目③to。","is going to のじゅんばんだね。"),
                       (filled(24),"私は今日の午後，郵便局へ行かなくてはなりません。","have→to→go to→the post office→this。2番目②to、4番目①the post office。","have to のあとに go to をおくよ。")],
             passage="\n\n".join(f"[出典: 大問3 Q{n} 完成文]\n"+filled(n) for n in range(21,26)),
             passageJa="私たちにあなたの北海道旅行について話してほしい。愛はよく、彼女の家の隣のレストランで夕食を食べる。父は今週末、車を洗うつもりだ。私は今日の午後、郵便局へ行かなければならない。佐藤先生の日本語の授業では、英語を話さないでほしい。",
             patterns=["tell us about","next to her house","is going to","have to go","don't speak"],
             questions=[("Q21で tell の直後に us を置くのはなぜ？","tell＋人＋about ～で『人に～について話す』。話す相手 us を tell の直後に置く。"),
                        ("Q23の2番目・4番目は？","father→is→going→to→wash なので、⑤is と③to。選択肢3。"),
                        ("Q25は日本文が『話さないでください』なのに、Please で始まるのはなぜ？","Please don't＋動詞の原形で『～しないでください』と、ていねいに頼むことができるから。")],
             easyQuestions=[("go to は、2つにわけてかぞえる？","わけないよ。1つのかたまりとしてかぞえるよ。"),("さいしょの Please も、ばんごうにいれる？","いれないよ。あいている5つのところだけだね。"),("is going to のあとは、どんな形？","wash のような、うごきのことばのもとの形だよ。")]),
        dict(title="読解——時刻・人物・数字を本文で確かめる",subtitle="Notice, E-mail & Story Reading",color="#f472b6",label="読解キーワード",
             explanation="【掲示】今日休むのは、because の後ろの the staff will change all the tables が理由。10:00 a.m. to 4:00 p.m. は店のふだんの営業時間、9:30 a.m. to 4:30 p.m. は新しいスタッフが週末に働く時間。【メール】Tony は試合の後 Olivia と話したかったが、but の後ろにあるとおりコーチとのミーティングがあった。Daniel の野球の試合は 10:00 a.m.、Tony の次の試合は 10:30 a.m.、Olivia がスポーツセンターへ行くのは 1:00 p.m.。行きたいのはスーパーマーケットの近くのカフェ。【物語】Kate はオーストラリア出身で、日本語も上手に話したのですぐに友だちになった。雪を初めて見て、雪について2時間話した。雪まつりでは雪の作品を見て楽しみ、3時間見て回った。時刻・人物・数字が何を指すかを確かめ、根拠の文へ戻る。",
             simple="けいじは、おみせのじかんとスタッフのじかんをわけよう。メールは、だれの、なんじのよていか。ものがたりは、2じかんと3じかんのちがいにちゅういしよう。",
             source="大問4A・4B・4C",quote="The new staff should work from 9:30 a.m. to 4:30 p.m. on weekends. / It starts at 10:00 a.m., so I can't see your match. / Mika and Kate soon became friends because Kate also spoke Japanese well. / They looked around the festival for three hours.",
             examples=[("The shop is closed today because the staff will change all the tables!","スタッフがテーブルをすべて取りかえるため、本日は休業です。","because の後ろが、今日休む理由。","テーブルをとりかえるから、やすみだね。"),
                       ("After the match, I wanted to talk with you, but I had a meeting with my coach.","試合の後、きみと話したかったけど、コーチとのミーティングがあったんだ。","but の後ろが実際にあったこと。wanted to talk は『話したかった』で、話したわけではない。","はなしたかったけど、ミーティングがあったよ。"),
                       ("Then, they talked about snow for two hours.","それから2人は、雪について2時間話しました。","two hours は雪について話した時間。おまつりを見て回ったのは three hours。","2じかんは、ゆきのはなしをしたじかんだよ。")],
             passage="[出典: 大問4A]\n"+"\n".join(notice["paragraphs"][1:])+"\n\n[出典: 大問4B 第2のメール]\n"+" ".join(r[0] for r in email["sentencePairs"][17:23])+"\n\n[出典: 大問4C 最終段落]\n"+story["paragraphs"][2],
             passageJa="【掲示】スタッフがテーブルをすべて取りかえるため、本日は休業。ふだんの営業時間は午前10時から午後4時まで。新しいスタッフを募集していて、週末の午前9時30分から午後4時30分まで働き、コーヒーをいれたり台所を掃除したりする。\n【メール】オリビアはその日、兄（弟）ダニエルの野球の試合を見る。試合は午前10時に始まるので、トニーの試合は見られない。でもダニエルの試合の後、午後1時にスポーツセンターへ行く。トニーの試合の後は、エデンズ・スーパーマーケットの近くのカフェへ一緒に行きたい。そのときに話せる。\n【物語】次の日曜日、ミカとケイトはミカの町の雪まつりへ行き、美しい雪の作品を見て楽しんだ。ケイトは『わくわくする』と言い、ミカは温かいものを食べようと言った。2人はソーセージを4本買い、3時間おまつりを見て回った。ミカはケイトの笑顔を見てうれしかった。",
             patterns=["closed today","9:30 a.m.","10:00 a.m.","had a meeting","the café","for the first time","three hours"],
             questions=[("Q27で At 10:00 a.m. を選ばない理由は？","10:00 a.m. は店がふだん開く時刻。新しいスタッフは週末 9:30 a.m. から働く。"),
                        ("Q29の It starts at 10:00 a.m. の It は何を指す？","前の文の my brother Daniel's baseball game（兄（弟）ダニエルの野球の試合）。"),
                        ("Q35で For two hours. を選ばない理由は？","two hours は雪について話した時間。おまつりを見て回ったのは for three hours。")],
             easyQuestions=[("あたらしいスタッフは、なんじからはたらく？","ごぜん9じ30ぷんからだよ。"),("オリビアがトニーといきたいのは、どこ？","カフェだよ。"),("ケイトがはじめてみたものは？","たくさんのゆきだよ。")]),
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

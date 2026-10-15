"""Grade 4's existing 30-word / four-focus-point / normal-and-easy format."""
import re

VOCAB=[
    ("radio","ラジオ","名詞","My grandfather listens to the radio after dinner.","祖父は夕食の後にラジオを聞きます。",["テレビ","新聞","雑誌"],"大問1 Q1","radio"),
    ("try","やってみる・試す","動詞","I want to try skiing this winter.","私はこの冬、スキーをやってみたいです。",["あきらめる","選ぶ","見せる"],"大問1 Q2","try"),
    ("bring","持って来る","動詞","Please bring your lunch tomorrow.","明日はお弁当を持って来てください。",["送る","借りる","忘れる"],"大問1 Q3","bring"),
    ("need","必要とする","動詞","I need a new pair of shoes.","私は新しい靴が1足必要です。",["探す","捨てる","貸す"],"大問1 Q4","needed"),
    ("famous","有名な","形容詞","Kyoto is famous for its old temples.","京都は古いお寺で有名です。",["退屈な","新しい","静かな"],"大問1 Q5","famous"),
    ("gym","体育館","名詞","We play basketball in the gym after school.","私たちは放課後、体育館でバスケットボールをします。",["図書館","台所","教室"],"大問1 Q6","gym"),
    ("dentist","歯医者","名詞","I go to the dentist once a year.","私は年に1回、歯医者に行きます。",["看護師","歌手","教師"],"大問1 Q7","dentist"),
    ("have a cold","かぜをひいている","熟語","My brother has a cold, so he is in bed.","兄（弟）はかぜをひいているので、寝ています。",["熱がある","おなかが痛い","疲れている"],"大問1 Q8","had a cold"),
    ("stay with","～の家に泊まる","熟語","I stayed with my aunt in Osaka last summer.","私は去年の夏、大阪のおばの家に泊まりました。",["～を訪ねる","～と話す","～を待つ"],"大問1 Q9","stayed with"),
    ("get home","家に着く・帰宅する","熟語","My father gets home at seven every evening.","父は毎晩7時に帰宅します。",["家を出る","家にいる","家を掃除する"],"大問1 Q10","gets home"),
    ("take pictures","写真を撮る","熟語","We took a lot of pictures at the zoo.","私たちは動物園でたくさん写真を撮りました。",["絵を描く","絵を見る","カメラを買う"],"大問1 Q11","taking pictures"),
    ("how many times","何回","熟語","How many times did you see that movie?","あなたはその映画を何回見ましたか。",["何時に","何人","いくら"],"大問1 Q12","How many times"),
    ("check","確かめる・調べる","動詞","Please check your answers again.","もう一度、答えを確かめてください。",["書く","消す","選ぶ"],"大問1 Q13","check"),
    ("better","よりよい・より上手な","形容詞","This bag is better than that one.","このかばんはあのかばんよりよいです。",["いちばんよい","もっと悪い","同じくらいよい"],"大問1 Q14","better"),
    ("heavy","重い","形容詞","My bag is very heavy today.","今日は私のかばんがとても重いです。",["軽い","大きい","新しい"],"大問1 Q15","heavy"),
    ("pet","ペット","名詞","My friend has a pet rabbit.","友だちはペットのウサギを飼っています。",["家族","おもちゃ","先生"],"大問2 Q16","pet"),
    ("May I","～してもいいですか","表現","May I open the window?","窓を開けてもいいですか。",["～してくれませんか","～しましょうか","～しませんか"],"大問2 Q17","May I"),
    ("present","プレゼント・贈り物","名詞","This watch was a present from my father.","この腕時計は父からのプレゼントでした。",["手紙","忘れ物","買い物"],"大問2 Q18","present"),
    ("be careful","気をつける","熟語","Be careful on the stairs.","階段では気をつけてね。",["急ぐ","静かにする","待つ"],"大問2 Q19","be careful"),
    ("hungry","おなかがすいた","形容詞","I'm always hungry after soccer practice.","サッカーの練習の後は、いつもおなかがすきます。",["のどがかわいた","眠い","疲れた"],"大問2 Q20","hungry"),
    ("should","～したほうがよい","助動詞","You should drink more water.","もっと水を飲んだほうがいいですよ。",["～してもよい","～できる","～するつもりだ"],"大問3 Q21","should"),
    ("have to","～しなければならない","熟語","We have to leave home at seven.","私たちは7時に家を出なければなりません。",["～したい","～してもよい","～するのが好きだ"],"大問3 Q22","have to"),
    ("corner","角","名詞","Turn left at the next corner.","次の角を左に曲がってください。",["橋","信号","駅"],"大問3 Q25","the corner"),
    ("borrow","借りる","動詞","I borrowed a pen from Ken.","私はケンからペンを借りました。",["貸す","返す","買う"],"大問4A","borrow"),
    ("closed","閉まっている・休みの","形容詞","The museum is closed on Mondays.","その博物館は月曜日が休みです。",["開いている","混んでいる","新しい"],"大問4A","Closed"),
    ("take","（時間が）かかる","動詞","It takes ten minutes to walk to the park.","公園まで歩いて10分かかります。",["始まる","終わる","待つ"],"大問4B","takes 30 minutes"),
    ("practice","練習する","動詞","I practice the piano every day.","私は毎日ピアノを練習します。",["教える","休む","見る"],"大問4B","practice"),
    ("favorite","いちばん好きな","形容詞","My favorite color is blue.","私のいちばん好きな色は青です。",["きらいな","新しい","ふつうの"],"大問4C","favorite"),
    ("painting","絵・絵画","名詞","There is a big painting on the wall.","壁に大きな絵がかかっています。",["写真","地図","鏡"],"大問4C","paintings"),
    ("artist","芸術家・画家","名詞","That artist lives in Paris.","その画家はパリに住んでいます。",["作家","医者","歌手"],"大問4C","artist"),
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
    spec=importlib.util.spec_from_file_location("order",Path(__file__).with_name("gen_g4_2024-2_sat_order.py"))
    o=importlib.util.module_from_spec(spec);spec.loader.exec_module(o)
    qs=[q for s in sections for q in s.get("questions",[])]
    def filled(n):
        q=next(q for q in qs if q["number"]==n)
        return o.completed(q) if "words" in q else q["text"].replace("(　)",q["choices"][q["answer"]-1])
    notice,email,story=sections[3]["passages"]
    specs=[
        dict(title="語句の「セット」と文の形",subtitle="Vocabulary & Useful Phrases",color="#4f8cff",label="語句のセット",
             explanation="空所の前後の語と組み合わせて考える。Q8 は have a cold（かぜをひいている）、Q9 は stay with ～（～の家に泊まる）、Q10 は get home（帰宅する）、Q11 は like ～ing（～するのが好きだ）と take pictures（写真を撮る）、Q12 は How many times ～?（何回～）。形を決める問題もある。Q13 は I'm going to の後ろなので動詞の原形 check、Q14 は than（～より）があるので good の比較級 better、Q15 は help の後ろに手伝う相手を置くので『私を』の me。空所の前後を一緒に読み、どのセット・どの形になるかを確かめよう。",
             simple="ことばは、まえやうしろのことばといっしょにおぼえよう。have a cold は『かぜをひいている』。get home は『いえにつく』。than があったら better のような『より～』のかたちだよ。",
             source="大問1 Q8・Q10・Q14",quote="Dan didn't go to school yesterday because he had a cold. / Richard usually gets home at 5:00 p.m. / Jane is a better tennis player than Kevin.",
             examples=[("Dan didn't go to school yesterday because he had a cold.","ダンはかぜをひいていたので、昨日は学校へ行きませんでした。","have a cold で『かぜをひいている』。cold は a をつけて名詞として使うと『かぜ』という意味になる。","a cold は『かぜ』だよ。"),
                       ("Richard usually gets home at 5:00 p.m.","リチャードはふだん午後5時に帰宅します。","get home で『家に着く・帰宅する』。この home は『家へ』という意味なので to をつけない。主語が Richard で、ふだんのことなので gets。","get home は『いえにつく』だよ。"),
                       ("Jane is a better tennis player than Kevin.","ジェーンはケビンより上手なテニス選手です。","than（～より）があるので比較級を使う。good の比較級は better。","than があるから better だね。")],
             passage="[出典: 大問1 Q9]\n"+filled(9)+"\n\n[出典: 大問1 Q10]\n"+filled(10),
             passageJa="ロバートは先週シカゴへ行き、そこに住む姉（妹）の家に泊まった。リチャードはふだん午後5時に帰宅するが、今日は電車が遅れたので、午後6時30分に家に着いた。",
             patterns=["had a cold","stayed with","gets home","taking pictures","How many times","going to check","better tennis player"],
             questions=[("Q9で with を選ぶのはなぜ？","stay with ～で『～の家に泊まる』という言い方になるから。姉（妹）がシカゴに住んでいるので、その家に泊まった。"),
                        ("Q13で check を選ぶ根拠は？","I'm going to の後ろだから。be going to＋動詞の原形で『～するつもりだ』となり、原形の check を使う。"),
                        ("Q15の help me はどんな意味？","『私を手伝う』。help の後ろに手伝う相手を置くときは、I ではなく me（私を）の形にする。")],
             easyQuestions=[("『かぜをひいている』は、えいごで？","have a cold だよ。"),("『いえにつく』は？","get home だよ。"),("than があるときにえらぶかたちは？","better のような『より～』のかたちだよ。")]),
        dict(title="会話は「返事」と「続き」から選ぶ",subtitle="Conversation Clues",color="#34d399",label="会話の手がかり",
             explanation="空所の後ろにある返事や続きの文から、空所に入る言葉を考える。Q2 は B が Of course と答えて Let's play it together. と誘っているので、やってみたいと頼む try。Q16 は He's white and gray. の He が飼っているペットを指すので Yes, I have a cat.。Q17 は先生が Sure. What is it? と答えているので、話してもいいかを尋ねる May I talk to you?。Q19 は Sure の後ろに but があるので、注意を加える be careful.。Q20 は息子が I'm not hungry. と答えているので、朝食の希望を尋ねる What would you like for breakfast?。答えを入れた後、会話が自然につながるかを確かめよう。",
             simple="あとのことばがヒント。『いいですよ。なんですか？』なら『はなしてもいいですか？』。『おなかはすいていない』なら『あさごはん、なにがいい？』だね。",
             source="大問2 Q16・Q17・Q20",quote="Yes, I have a cat. He's white and gray. / May I talk to you? / Sure. What is it? / What would you like for breakfast?",
             examples=[("May I talk to you?","お話ししてもいいですか。","May I ～? は『～してもいいですか』と丁寧に許可を求める言い方。先生の Sure. What is it? につながる。","『はなしてもいいですか』だよ。"),
                       ("Sure, Tom, but be careful.","いいわよ、トム。でも気をつけてね。","Sure（いいよ）と認めた後、but で注意を加えている。Be careful. は be で始まる命令文。","『でも、きをつけてね』だね。"),
                       ("What would you like for breakfast?","朝食に何が食べたい？","What would you like for ～? は『～に何がほしいですか』と希望を尋ねる言い方。","『あさごはん、なにがいい？』だよ。")],
             passage="[出典: 大問2 Q16]\n"+filled(16)+"\n\n[出典: 大問2 Q17]\n"+filled(17)+"\n\n[出典: 大問2 Q20]\n"+filled(20),
             passageJa="ペットを飼っているかと聞かれた女の子は、白と灰色のネコを飼っていると答える。生徒はブラウン先生に話してもいいかと尋ね、宿題について質問したいと伝える。父は朝食に何が食べたいかを尋ね、息子はおなかがすいていないのでジュースだけほしいと答える。",
             patterns=["Of course","I have a cat","May I talk to you","be careful","I'm not hungry"],
             questions=[("Q16で Yes, I'll think about it. が合わないのはなぜ？","I'll think about it.（考えておくね）は誘いや提案への返事だから。後ろの He's white and gray. は飼っているペットの説明なので、Yes, I have a cat. が合う。"),
                        ("Q17で先生が What is it? と聞いているのはなぜ？","生徒が May I talk to you?（お話ししてもいいですか）と尋ねたので、Sure（いいですよ）と答えてから用件を聞いている。"),
                        ("Q20の I'm not hungry. から何がわかる？","食べ物について聞かれたこと。Good morning から朝の場面なので、朝食に何が食べたいかを尋ねる質問が合う。")],
             easyQuestions=[("May I ～? は、どんないみ？","『～してもいいですか』だよ。"),("be careful は？","『きをつけて』だよ。"),("I'm not hungry. は？","『おなかはすいていない』だよ。")]),
        dict(title="並べ替え——動詞の形と語句のかたまり",subtitle="Five Sentence Patterns",color="#a78bfa",label="整序の型",
             explanation="Q21 は should＋動詞の原形（～したほうがよい）と take a bath（お風呂に入る）。Q22 は have to＋動詞の原形（～しなければならない）と after school（放課後）。Q23 は couldn't＋動詞の原形の後ろに、because（～なので）で理由を加える形。Q24 は Which train（どの電車）が主語の疑問文で、その後ろに goes を続ける。Q25 は met＋人（～に会った）と at the corner of ～（～の角で）。my room・his friends・the corner はそれぞれ1つの語句なので2つに分けず、5つの語句の位置を数える。最初から書かれている I・Dale couldn't・Excuse me. や文末の語は数えない。Q21 の you と Q24 の which は、文のはじめの語でも（　）の中では小文字になっている。完成文を作ってから、2番目と4番目を選択肢と照らし合わせる。",
             simple="5つのことばのかたまりをならべよう。my room や the corner は2つにわけないよ。さいしょからかいてある I や Excuse me. は、ばんごうにかぞえない。あいているところの2ばんめと4ばんめをたしかめよう。",
             source="大問3 Q21～Q25（並べ替え後の完成文）",quote="You should take a bath early tonight. / I have to clean my room after school. / Excuse me. Which train goes to Kyoto?",
             examples=[(filled(21),"今夜は早くお風呂に入ったほうがいいですよ。","you→should→take→a→bath。2番目④should、4番目③a。","2ばんめ should、4ばんめ a だね。"),
                       (filled(23),"雪が降っていたので，デールは友達とテニスをすることができませんでした。","play→tennis→with→his friends→because。2番目①tennis、4番目②his friends。","his friends は1つのかたまりだよ。"),
                       (filled(24),"すみません。京都へ行く電車はどれですか。","which→train→goes→to→Kyoto。2番目②train、4番目④to。","which train『どのでんしゃ』からはじめよう。")],
             passage="\n\n".join(f"[出典: 大問3 Q{n} 完成文]\n"+filled(n) for n in range(21,26)),
             passageJa="今夜は早くお風呂に入ったほうがいい。私は放課後、自分の部屋をそうじしなければならない。雪が降っていたので、デールは友達とテニスができなかった。すみません、京都へ行く電車はどれですか。私はこの通りの角でジャックに会った。",
             patterns=["should take a bath","have to clean","because it was snowing","Which train goes","at the corner of"],
             questions=[("Q21で you を最初に置くのはなぜ？","日本文は『（あなたは）お風呂に入ったほうがいい』で、主語 you の後ろに should＋動詞の原形 take を続けるから。（　）の中では文のはじめの語も小文字で書かれている。"),
                        ("Q24で which train の後ろに goes を置くのはなぜ？","Which train（どの電車）がこの文の主語だから。主語の後ろに動詞 goes を続けると『どの電車が京都へ行きますか』になる。"),
                        ("Q25の2番目・4番目は？","met→Jack→at→the corner→of なので、②Jack と③the corner。選択肢1。")],
             easyQuestions=[("my room は、2つにわけてかぞえる？","わけないよ。1つのかたまりとしてかぞえるよ。"),("Excuse me. も、ばんごうにいれる？","いれないよ。あいている5つのところだけだね。"),("こたえるのは、どこ？","あいているところの2ばんめと4ばんめだよ。")]),
        dict(title="読解——数字・曜日・人物を整理する",subtitle="Notice, E-mail & Story Reading",color="#f472b6",label="読解キーワード",
             explanation="【掲示】曜日ごとに、開く時刻と閉まる時刻を区別する。月曜日から金曜日は午前8時から午後7時まで、土曜日は午前9時から午後5時まで、日曜日は休み。新しいコンピューターを使う前には先生に尋ねる。【メール】1通目は祖母の質問、2通目はオリーの答え。駅まで自転車で10分、電車で30分、駅から学校まで歩いて15分、野球の練習は1時間。数字が何の時間かをセットで読む。試合は次の土曜日で、水曜日と金曜日は練習の日。【物語】この前の水曜日に自画像を描き、金曜日にクラスで美術館へ行き、土曜日に母が美術学校に電話した。美術教室は次の木曜日に始まる。昼食は、ジェーンがパスタとスープ、トニーがハンバーガー、ジェイがサラダ。曜日と出来事、人物と食べた物をセットにして、根拠の文へ戻る。",
             simple="けいじは、ようびとじかんをわける。メールは、すうじがなんのじかんか。ものがたりは、いつなにをしたか、だれがなにをたべたかをならべよう。",
             source="大問4A・4B・4C",quote="Saturday: 9:00 a.m. to 5:00 p.m. / The train ride to school takes 30 minutes. / Last Friday, Jay's class went to an art museum.",
             examples=[("Saturday: 9:00 a.m. to 5:00 p.m.","土曜日：午前9時～午後5時","土曜日は午後5時に閉まる。午後7時は月曜日から金曜日に閉まる時刻。","どようびは5じにしまるよ。"),
                       ("The train ride to school takes 30 minutes.","学校までの電車は30分かかります。","take は『（時間が）かかる』。10分は自転車、15分は歩く時間。","でんしゃは30ぷんだね。"),
                       ("His friend Jane ate pasta and soup, and his friend Tony ate a hamburger.","友だちのジェーンはパスタとスープを、友だちのトニーはハンバーガーを食べました。","人物と食べた物をセットで読む。トニーが食べたのはハンバーガー。","トニーはハンバーガーだよ。")],
             passage="[出典: 大問4A]\n"+"\n".join(notice["paragraphs"][1:])+"\n\n[出典: 大問4B 第2のメール]\n"+" ".join(r[0] for r in email["sentencePairs"][20:28])+"\n\n[出典: 大問4C 第4段落]\n"+story["paragraphs"][3],
             passageJa="【掲示】10月1日。今日から、学校の図書館の開く時間が変わる。月曜日から金曜日は午前8時から午後7時まで、土曜日は午前9時から午後5時まで、日曜日は休み。生徒証で本を借りられる。図書館には新しいコンピューターもあり、使う前に先生に尋ねなければならない。\n【メール】新しい学校はまあまあ。毎朝、駅まで自転車で10分走る。学校までの電車は30分かかる。それから学校まで15分歩く。野球は楽しい。毎週水曜日と金曜日に1時間練習している。次の土曜日に試合があるので、見に来ていい。\n【物語】その晩、ジェイは母に美術館のことを話し、美術教室に通いたいと言った。土曜日に、母は家の近くの美術学校に電話した。ジェイは次の木曜日から美術教室に通い始める。ジェイの夢は芸術家になること。",
             patterns=["Monday to Friday","Saturday: 9:00 a.m. to 5:00 p.m.","takes 30 minutes","next Saturday","Last Friday","Last Wednesday","ate a hamburger"],
             questions=[("Q26で At 7:00 p.m. を選ばない理由は？","7:00 p.m. は月曜日から金曜日に閉まる時刻だから。質問は next Saturday なので、Saturday: 9:00 a.m. to 5:00 p.m. の 5:00 p.m. を選ぶ。"),
                        ("Q29で 15 minutes. を選ばない理由は？","15分は、電車を降りてから学校まで歩く時間だから。電車の乗車時間は The train ride to school takes 30 minutes. の30分。"),
                        ("Q32の答えの根拠はどこ？","Last Friday, Jay's class went to an art museum. の Last Friday。Last Wednesday は自画像を描いた日、On Saturday は母が美術学校に電話した日。")],
             easyQuestions=[("どようびに、としょかんがしまるのはなんじ？","ごご5じだよ。"),("オリーのでんしゃは、なんぷん？","30ぷんだよ。"),("びじゅつかんにいったのは、なんようび？","このまえのきんようびだよ。")]),
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

"""Grade 4's existing 30-word / four-focus-point / normal-and-easy format."""
import re

VOCAB=[
    ("gift","贈り物・プレゼント","名詞","I bought a gift for my mother.","私は母への贈り物を買いました。",["客","道路","規則"],"大問1 Q1","gift"),
    ("farm","農場","名詞","My uncle has a big farm.","おじは大きな農場を持っています。",["硬貨","いとこ","スカーフ"],"大問1 Q2","farm"),
    ("vegetable","野菜","名詞","Please eat your vegetables, Tom.","トム、野菜を食べてね。",["果物","肉","魚"],"大問1 Q2","vegetables"),
    ("hotel","ホテル","名詞","We stayed at a hotel near the station.","私たちは駅の近くのホテルに泊まりました。",["趣味","季節","切符"],"大問1 Q3","hotel"),
    ("early","早く","副詞","I got up early this morning.","私は今朝、早く起きました。",["遅く","もう一度","すぐに"],"大問1 Q4","early"),
    ("butter","バター","名詞","I put some butter on my bread.","私はパンにバターをぬりました。",["砂糖","牛乳","卵"],"大問1 Q5","butter"),
    ("remember","覚えている","動詞","I remember his phone number.","私は彼の電話番号を覚えています。",["忘れる","見せる","待つ"],"大問1 Q6","remember"),
    ("important","大切な","形容詞","Sleep is important for children.","睡眠は子どもにとって大切です。",["静かな","注意深い","長い"],"大問1 Q7","important"),
    ("be good at","～が得意だ・上手だ","熟語","My sister is good at drawing.","姉（妹）は絵を描くのが得意です。",["～が苦手だ","～に遅れる","～を怖がる"],"大問1 Q8","good at"),
    ("wake up","目が覚める・起きる","熟語","I woke up at six today.","私は今日、6時に目が覚めました。",["寝る","あきらめる","急ぐ"],"大問1 Q9","woke up"),
    ("all over the world","世界中","熟語","People all over the world love soccer.","世界中の人々がサッカーを愛しています。",["町の中だけ","家の近く","学校の前"],"大問1 Q10","all over the world"),
    ("Wait a minute.","ちょっと待って。","表現","Wait a minute. I'll get my bag.","ちょっと待って。かばんを取ってきます。",["もう一度言って。","急いで。","よくやったね。"],"大問1 Q11","Wait a minute."),
    ("give up","あきらめる","熟語","Don't give up. You can do it.","あきらめないで。あなたならできます。",["始める","起きる","手伝う"],"大問1 Q12","give up"),
    ("lose","なくす","動詞","Don't lose your key.","鍵をなくさないでね。",["見つける","買う","借りる"],"大問1 Q13","lost"),
    ("the most famous","最も有名な","形容詞（最上級）","This is the most famous park in our city.","ここは私たちの市で最も有名な公園です。",["有名すぎる","より有名な","少し有名な"],"大問1 Q14","the most famous"),
    ("talk to","～と話す","熟語","I talked to my friend on the phone.","私は電話で友だちと話しました。",["～を待つ","～を探す","～の世話をする"],"大問1 Q15","talking to"),
    ("take","連れて行く","動詞","My father took me to the zoo.","父は私を動物園へ連れて行ってくれました。",["迎えに行く","待っている","送り返す"],"大問2 Q16","take you to"),
    ("airport","空港","名詞","We met my aunt at the airport.","私たちは空港でおばに会いました。",["駅","郵便局","図書館"],"大問2 Q16","airport"),
    ("Father's Day","父の日","名詞","I gave my father a tie on Father's Day.","父の日に、父にネクタイを贈りました。",["母の日","誕生日","祝日"],"大問2 Q17","Father's Day"),
    ("start","始める・始まる","動詞","The movie starts at seven.","映画は7時に始まります。",["終わる","止まる","休む"],"大問2 Q18","started"),
    ("free","ひまな・空いている","形容詞","Are you free tomorrow?","明日はひまですか。",["忙しい","疲れた","うれしい"],"大問2 Q20","free"),
    ("have time to","～する時間がある","熟語","I don't have time to watch TV today.","今日はテレビを見る時間がありません。",["～するのをやめる","～する必要がある","～するのが得意だ"],"大問3 Q21","have time to"),
    ("many kinds of","たくさんの種類の～","熟語","That shop sells many kinds of bread.","その店はたくさんの種類のパンを売っています。",["少しの～","1つの～","同じ～"],"大問3 Q22","many kinds of"),
    ("learn to","～するようになる・～を身につける","熟語","My brother learned to swim last summer.","兄（弟）は去年の夏に泳げるようになりました。",["～するのを忘れる","～するのをやめる","～するのを手伝う"],"大問3 Q25","learned to"),
    ("parade","パレード","名詞","Many people watched the parade.","たくさんの人がパレードを見ました。",["試合","会議","授業"],"大問4A","parade"),
    ("tournament","トーナメント・勝ち抜き戦","名詞","Our team won the tennis tournament.","私たちのチームはテニスのトーナメントで優勝しました。",["練習","休み","旅行"],"大問4A","tournament"),
    ("perform","演奏する・演じる","動詞","The students will perform a play.","生徒たちは劇を演じます。",["休む","買う","掃除する"],"大問4A","perform"),
    ("look forward to","～を楽しみにする","熟語","I'm looking forward to summer vacation.","私は夏休みを楽しみにしています。",["～を探す","～の世話をする","～をあきらめる"],"大問4B","looking forward to"),
    ("healthy","健康的な・健康によい","形容詞","Fruit is a healthy snack.","果物は健康的なおやつです。",["高価な","簡単な","有名な"],"大問4C","healthy"),
    ("surprised","驚いた","形容詞","I was surprised at the big cake.","私はその大きなケーキに驚きました。",["疲れた","眠い","怒った"],"大問4C","surprised"),
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
    spec=importlib.util.spec_from_file_location("order",Path(__file__).with_name("gen_g4_2025-2_sat_order.py"))
    o=importlib.util.module_from_spec(spec);spec.loader.exec_module(o)
    qs=[q for s in sections for q in s.get("questions",[])]
    def filled(n):
        q=next(q for q in qs if q["number"]==n)
        return o.completed(q) if "words" in q else q["text"].replace("(　)",q["choices"][q["answer"]-1])
    notice,email,story=sections[3]["passages"]
    specs=[
        dict(title="語句は「セット」で覚える",subtitle="Vocabulary & Useful Phrases",color="#4f8cff",label="語句のセット",
             explanation="単語の意味だけでなく、前後の語とセットで覚える。Q4 は get up early、Q8 は be good at、Q9 は wake の過去形を使った woke up、Q10 は all over the world、Q11 は Wait a minute.、Q12 は give up。Q13 は Yesterday に合わせて過去形 lost、Q14 は the most famous という最上級、Q15 は was talking という過去進行形。空所の前後を一緒に読み、どのセットになるかを確かめよう。",
             simple="たんごは、まえやうしろのことばといっしょにおぼえよう。give up は『あきらめる』。all over the world は『せかいじゅう』。Wait a minute. は『ちょっとまって』だよ。",
             source="大問1 Q10・Q11・Q12",quote="It has books from all over the world. / Wait a minute. I can't find my coat. / Jenny got very tired in the race, but she did not give up.",
             examples=[("It has books from all over the world.","そこには世界中の本があります。","all over the world で『世界中』。over をほかの前置詞に変えると、この意味にならない。","all over the world をひとつのセットにしよう。"),
                       ("Wait a minute. I can't find my coat.","ちょっと待って。コートが見つからないのです。","Wait a minute. は『ちょっと待って』という決まった言い方。","Wait a minute. で『ちょっとまって』だね。"),
                       ("Jenny got very tired in the race, but she did not give up.","ジェニーはレースでとても疲れましたが、あきらめませんでした。","give up で『あきらめる』。did not の後ろは原形 give。","give up は『あきらめる』だよ。")],
             passage="[出典: 大問1 Q10]\n"+filled(10)+"\n\n[出典: 大問1 Q12]\n"+filled(12),
             passageJa="その本屋はとても大きく、世界中の本がある。ジェニーはレースでとても疲れたが、あきらめずに走り、最後まで走り切った。",
             patterns=["all over the world","give up","get up","good at","Wait a minute"],
             questions=[("Q10で over を選ぶのはなぜ？","all over the world で『世界中』という決まった表現になるから。books from all over the world で『世界中から集まった本』。"),
                        ("Q13で lost を使う根拠は？","Yesterday と went が過去を示す。lose（なくす）の過去形 lost にする。"),
                        ("Q14の the most famous はどんな意味？","『最も有名な』。in Japan が比べる範囲で、富士山が日本でいちばん有名な山だと言っている。")],
             easyQuestions=[("『あきらめる』は、どのセット？","give up だよ。"),("『せかいじゅう』は、えいごで？","all over the world だよ。"),("『ちょっとまって』は？","Wait a minute. だよ。")]),
        dict(title="会話は「答えの文」から選ぶ",subtitle="Conversation Clues",color="#34d399",label="会話の手がかり",
             explanation="空所の後ろの返事から、空所の役割を考える。Q16 は母が空港へ行くという理由を答えているので、理由を尋ねる Why not?。Q17 は A card for my dad. と作っている物を答えているので What are you making?。Q19 は The chicken sandwich. と料理名を答えているので What did you have?。Q20 は Let's go then. の then が指す時を示す I'll be free this weekend.。Q18 は Yes の後ろで通学の様子を説明している。返事が質問の答えになっているかを確かめよう。",
             simple="あとのへんじがヒント。『カードだよ』なら『なにをつくっているの？』。『チキンサンドイッチ』なら『なにをたべたの？』だね。",
             source="大問2 Q16・Q17・Q19",quote="Why not? / I have to meet Grandma at the airport. / What are you making? / A card for my dad. / What did you have? / The chicken sandwich.",
             examples=[("Why not?","どうして（だめなの）ですか。","直後に母が空港へ行く理由を答えている。","りゆうをきいているよ。"),
                       ("What are you making?","何を作っているのですか。","返事の A card for my dad. が作っている物。","つくっているものは、カードだね。"),
                       ("What did you have?","何を食べましたか。","have はここでは『食べる』。返事は料理名。","たべたものは、チキンサンドイッチだよ。")],
             passage="[出典: 大問2 Q16]\n"+filled(16)+"\n\n[出典: 大問2 Q17]\n"+filled(17)+"\n\n[出典: 大問2 Q19]\n"+filled(19),
             passageJa="母は今日、テッドをピアノのレッスンに連れて行けない。理由を聞かれ、空港でおばあちゃんを迎えると答える。マイクは父の日のためにお父さんへのカードを作っている。女性は新しいレストランでチキンサンドイッチを食べた。",
             patterns=["Why not?","A card for my dad","The chicken sandwich","Let's go then","He likes his teacher"],
             questions=[("Q16で Good job! が合わないのはなぜ？","Good job! は相手をほめる言葉。連れて行けないと言われた場面で、母も次に理由を答えている。"),
                        ("Q19で How much was it? を選ばないのは？","値段を聞かれたら金額を答える。返事の The chicken sandwich. は料理名なので、食べた物を尋ねる質問が合う。"),
                        ("Q20の then は何を指す？","this weekend。空所に I'll be free this weekend. を入れると、男の子が『その時に行こう』と答える流れになる。")],
             easyQuestions=[("Why not? は、どんないみ？","どうしてだめなの？、だよ。"),("What did you have? のこたえは？","チキンサンドイッチだよ。"),("Let's go then. の then は、いつ？","こんしゅうまつだよ。")]),
        dict(title="並べ替え——5つの「型」を知る",subtitle="Five Sentence Patterns",color="#a78bfa",label="整序の型",
             explanation="Q21 は did not have time to＋動詞の原形（～する時間がなかった）。Q22 は many kinds of＋名詞（たくさんの種類の～）。Q23 は Thank you very much for＋名詞（～をどうもありがとう）。Q24 は Do you need some help? という一般動詞の疑問文。Q25 は learned to cook（料理を学んだ）＋from my mother。『the nice』は1つの語句なので2つに分けず、5つの語句の位置を数える。最初から書かれている Eri / I have / Thank / Kathy, / I や文末の語は数えない。完成文を作ってから、2番目と4番目を選択肢と照らし合わせる。",
             simple="5つのことばのかたまりをならべよう。the nice は2つにわけないよ。さいしょからかいてある Eri や Thank は、ばんごうにかぞえない。あいているところの2ばんめと4ばんめをたしかめよう。",
             source="大問3 Q21～Q25（並べ替え後の完成文）",quote="Eri did not have time to see her aunt yesterday. / Thank you very much for the nice postcard. / Kathy, do you need some help?",
             examples=[(filled(21),"恵理は昨日，彼女の叔母に会う時間がありませんでした。","did→not→have→time→to。2番目④not、4番目③time。","2ばんめ not、4ばんめ time だね。"),
                       (filled(23),"すてきなお葉書をどうもありがとうございました。","you→very→much→for→the nice。2番目②very、4番目①for。","Thank you very much のあとに for をおくよ。"),
                       (filled(24),"キャシー，何か手伝いましょうか。","do→you→need→some→help。2番目④you、4番目③some。","do you need のじゅんばんだね。")],
             passage="\n\n".join(f"[出典: 大問3 Q{n} 完成文]\n"+filled(n) for n in range(21,26)),
             passageJa="恵理は昨日、叔母に会う時間がなかった。私の庭にはたくさんの種類の花がある。すてきな葉書のお礼を言う。キャシーに手伝いが必要か尋ねる。私は母から料理を学んだ。",
             patterns=["have time to","many kinds of","very much","need some help","learned to cook"],
             questions=[("Q21で not の後ろに have を置くのはなぜ？","did not の後ろは動詞の原形。did not have time to see で『会う時間がなかった』。"),
                        ("Q23の2番目・4番目は？","you→very→much→for→the nice なので、②very と①for。選択肢3。"),
                        ("Q24は日本文が『手伝いましょうか』なのに need を使うのはなぜ？","英語では Do you need some help?（手助けが必要ですか）と相手に尋ねて、手伝いを申し出ることができるから。")],
             easyQuestions=[("the nice は、2つにわけてかぞえる？","わけないよ。1つのかたまりとしてかぞえるよ。"),("さいしょの Thank も、ばんごうにいれる？","いれないよ。あいている5つのところだけだね。"),("こたえるのは、どこ？","あいているところの2ばんめと4ばんめだよ。")]),
        dict(title="読解——掲示・メール・物語の読み分け",subtitle="Notice, E-mail & Story Reading",color="#f472b6",label="読解キーワード",
             explanation="【掲示】Time の 1:00 p.m. to 4:00 p.m. は始まりと終わり。曲数はバンド3曲・ダンスクラブ2曲・合唱団1曲と、グループごとに対応させる。【メール】Andy の家族は金曜日の夜に山へ向かい、土曜日に釣り、日曜日にハイキング、月曜日の朝に帰る。寝室は3つ、ベッド2台は Andy の部屋。去年キャンプに行ったのは2通目の差出人 Dave。【物語】平日の昼食は学校の食堂、週末はいとこと麺類、誕生日は祖父母と夕食。カレーが簡単に作れて驚き、今は家で健康的な食事を作るのも大好き。人物・時・数をセットにして、根拠の文へ戻る。",
             simple="けいじは、じかんときょくのかず。メールは、だれの、なんようびのよていか。ものがたりは、だれと、いつたべたかをわけよう。",
             source="大問4A・4B・4C",quote="Time: 1:00 p.m. to 4:00 p.m. / We'll go fishing on Saturday and hiking on Sunday. / My father and I went camping last year. / The curry was easy to make, so Kate was surprised.",
             examples=[("The Redwood Junior High School band will perform three songs for the team.","レッドウッド中学校のバンドは、チームのために3曲を演奏します。","the school band とこのバンドを結びつけ、曲数を読む。","バンドは3きょくだね。"),
                       ("There are three bedrooms in the house, and my room has two beds.","その家には寝室が3つあり、私の部屋にはベッドが2台あります。","three は寝室、two はベッドの数。何を数えているかを確かめる。","しんしつは3つ、ベッドは2だいだよ。"),
                       ("Kate still enjoys eating at restaurants and cafés, but she loves making healthy meals at home, too.","ケイトは今でもレストランやカフェで食べるのを楽しんでいますが、家で健康的な食事を作ることも大好きです。","but の後ろが今の新しい楽しみ。","いまは、いえでごはんをつくるのもだいすきだよ。")],
             passage="[出典: 大問4A]\n"+"\n".join(notice["paragraphs"][1:])+"\n\n[出典: 大問4B 第2のメール]\n"+" ".join(r[0] for r in email["sentencePairs"][19:24])+"\n\n[出典: 大問4C 最終段落]\n"+story["paragraphs"][2],
             passageJa="【掲示】町のバスケットボールチームが優勝し、次の土曜日に町のパレードがある。場所はメイン・ストリート、時間は午後1時から4時まで。バンドは3曲、ダンスクラブは2曲、合唱団は1曲。\n【メール】デイブは旅行のことを母に話し、行ってよいと言われた。去年は父とキャンプに行き、テントに1晩泊まった。姉（妹）はキャンプが好きではないので来なかった。山へ行くのを楽しみにしている。\n【物語】次の週末、ケイトは祖父母の家で鶏肉と野菜のカレーを作った。作るのが簡単で驚き、おいしくもあった。両親にも健康的な食事を作るつもり。今もレストランやカフェが好きだが、家で健康的な食事を作るのも大好き。",
             patterns=["1:00 p.m.","three songs","on Saturday","three bedrooms","went camping","school cafeteria","easy to make","healthy meals at home"],
             questions=[("Q26で 4:00 p.m. を選ばない理由は？","1:00 p.m. to 4:00 p.m. の 4:00 p.m. は終わる時刻。パレードが始まるのは 1:00 p.m.（午後1時）。"),
                        ("Q30で He went hiking. を選ばない理由は？","ハイキングは Andy の家族の日曜日の予定。Dave が去年したのはキャンプ。"),
                        ("Q34の驚いた理由はどこに書いてある？","The curry was easy to make, so Kate was surprised. の so の前。作るのが簡単だったから。")],
             easyQuestions=[("パレードがはじまるのは、なんじ？","ごご1じだよ。"),("デイブがきょねんしたことは？","キャンプだよ。"),("ケイトがびっくりしたのは、なぜ？","カレーをつくるのが、かんたんだったからだよ。")]),
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

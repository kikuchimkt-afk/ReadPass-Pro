"""Grade 4's existing 30-word / four-focus-point / normal-and-easy format."""
import re

VOCAB=[
    ("teach","教える","動詞","My mother teaches music at a junior high school.","母は中学校で音楽を教えています。",["学ぶ","払う","飛ぶ"],"大問1 Q1","teaches"),
    ("borrow","借りる","動詞","Can I borrow your eraser?","あなたの消しゴムを借りてもいいですか。",["貸す","返す","買う"],"大問1 Q2","borrow"),
    ("shy","恥ずかしがりの・内気な","形容詞","The shy boy didn't say hello to me.","その恥ずかしがりの男の子は、私にあいさつをしませんでした。",["元気な","親切な","背の高い"],"大問1 Q3","shy"),
    ("island","島","名詞","There are many birds on that island.","あの島にはたくさんの鳥がいます。",["山","川","湖"],"大問1 Q4","islands"),
    ("question","質問","名詞","May I ask you a question?","あなたに質問してもいいですか。",["答え","宿題","贈り物"],"大問1 Q5","questions"),
    ("actor","俳優","名詞","That actor is popular in Japan.","あの俳優は日本で人気があります。",["歌手","医者","料理人"],"大問1 Q6","actor"),
    ("member","一員・メンバー","名詞","I'm a member of the art club.","私は美術部の部員です。",["コーチ","客","建物"],"大問1 Q7","member"),
    ("hurry up","急ぐ","熟語","Hurry up, or you'll miss the bus.","急がないと、バスに乗り遅れますよ。",["ゆっくりする","待つ","休む"],"大問1 Q8","Hurry up"),
    ("look like","～に似ている・～のように見える","熟語","Tom looks like his father.","トムはお父さんに似ています。",["～を探す","～の世話をする","～を楽しみにする"],"大問1 Q9","looks like"),
    ("take a trip","旅行する","熟語","We took a trip to Kyoto last spring.","私たちは去年の春に京都へ旅行しました。",["散歩する","写真を撮る","買い物をする"],"大問1 Q10","took a trip"),
    ("fine","元気な・大丈夫な・よい","形容詞","I had a cold last week, but I'm fine now.","先週は風邪をひいていましたが、今は元気です。",["忙しい","病気の","眠い"],"大問1 Q11","fine"),
    ("for example","例えば","熟語","I like fruit. For example, I often eat apples.","私は果物が好きです。例えば、よくリンゴを食べます。",["ところで","最後に","しかし"],"大問1 Q12","For example"),
    ("best of all","すべての中でいちばん","熟語","Which season do you like best of all?","あなたはどの季節がいちばん好きですか。",["少しだけ","ほとんど～ない","2番目に"],"大問1 Q13","best of all"),
    ("hers","彼女のもの","代名詞","This umbrella isn't mine. It's hers.","この傘は私のものではありません。彼女のものです。",["彼のもの","私たちのもの","彼らのもの"],"大問1 Q14","hers"),
    ("stop","（～するのを）やめる・止める","動詞","Please stop talking in the library.","図書館でおしゃべりするのはやめてください。",["始める","続ける","急ぐ"],"大問1 Q15","Stop sending"),
    ("full","満腹の・いっぱいの","形容詞","The bus was full of people.","バスは人でいっぱいでした。",["空腹の","眠い","寒い"],"大問2 Q16","full"),
    ("tired","疲れた","形容詞","She was tired after the long walk.","彼女は長い散歩の後で疲れていました。",["うれしい","元気な","ひまな"],"大問2 Q17","tired"),
    ("be born","生まれる","熟語","My sister was born in May.","姉（妹）は5月に生まれました。",["育つ","引っ越す","住む"],"大問2 Q19","born"),
    ("someday","いつか","副詞","I want to visit Canada someday.","私はいつかカナダを訪れたいです。",["昨日","毎日","もう"],"大問2 Q19","someday"),
    ("feel","感じる・～の気分である","動詞","I feel happy when I sing.","私は歌うと楽しい気分になります。",["聞く","見る","忘れる"],"大問2 Q20","feel"),
    ("both A and B","AとBの両方","熟語","Both Ken and Mike like baseball.","ケンもマイクも野球が好きです。",["AかBのどちらか","AでもBでもない","AよりB"],"大問3 Q21","both English and Russian"),
    ("by car","車で","熟語","My father goes to work by car.","父は車で仕事に行きます。",["歩いて","電車で","自転車で"],"大問3 Q22","by car"),
    ("be good at","～が得意だ・上手だ","熟語","Ken is good at math.","ケンは数学が得意です。",["～が苦手だ","～に興味がある","～を怖がる"],"大問3 Q23","good at"),
    ("better than","～よりじょうずに・～よりよく","熟語","Yumi sings better than her sister.","ユミはお姉さんより歌がじょうずです。",["～と同じくらい","～ほど上手ではない","いちばん"],"大問3 Q24","better than"),
    ("again and again","何度も","熟語","He watched the movie again and again.","彼はその映画を何度も見ました。",["一度だけ","まだ","ときどき"],"大問3 Q25","again and again"),
    ("look for","～を探す","熟語","I'm looking for my glasses.","私はめがねを探しています。",["～を見つける","～を待つ","～の世話をする"],"大問4A","looking for"),
    ("amusement park","遊園地","名詞","We rode a roller coaster at the amusement park.","私たちは遊園地でジェットコースターに乗りました。",["動物園","水族館","映画館"],"大問4B","amusement park"),
    ("company","会社","名詞","My aunt works for a big company.","おばは大きな会社に勤めています。",["学校","病院","お店"],"大問4C","company"),
    ("article","記事","名詞","I read an article about space.","私は宇宙についての記事を読みました。",["写真","手紙","地図"],"大問4C","article"),
    ("for the first time","初めて","熟語","I ate sushi for the first time yesterday.","昨日、私は初めてすしを食べました。",["最後に","何度も","もう一度"],"大問4C","for the first time"),
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
    spec=importlib.util.spec_from_file_location("order",Path(__file__).with_name("gen_g4_2025-1_sat_order.py"))
    o=importlib.util.module_from_spec(spec);spec.loader.exec_module(o)
    qs=[q for s in sections for q in s.get("questions",[])]
    def filled(n):
        q=next(q for q in qs if q["number"]==n)
        return o.completed(q) if "words" in q else q["text"].replace("(　)",q["choices"][q["answer"]-1])
    notice,email,story=sections[3]["passages"]
    specs=[
        dict(title="語句は「セット」で覚える",subtitle="Vocabulary & Useful Phrases",color="#4f8cff",label="語句のセット",
             explanation="単語の意味だけでなく、前後の語とセットで覚える。Q8 は Hurry up!（急いで）、Q9 は look like（～に似ている）、Q10 は take a trip（旅行する）の過去形 took a trip、Q11 は ～ is fine with me（私は～で大丈夫）、Q12 は For example（例えば）。Q13 は of all があるので最上級の best、Q14 は her bag を1語で表す hers（彼女のもの）、Q15 は stop の後ろに -ing 形を置く stop sending（送るのをやめる）。空所の前後を一緒に読み、どのセットになるかを確かめよう。",
             simple="たんごは、まえやうしろのことばといっしょにおぼえよう。look like は『～ににている』。For example は『たとえば』。Hurry up! は『いそいで！』だよ。",
             source="大問1 Q9・Q10・Q12",quote="She really looks like you. / Last summer, Ted took a trip to America. / For example, I like soccer, baseball, and basketball.",
             examples=[("She really looks like you.","彼女は本当にあなたに似ています。","look like ～ で『～に似ている』。主語 She に合わせて looks になる。","looks like で『ににている』だよ。"),
                       ("Last summer, Ted took a trip to America.","去年の夏、テッドはアメリカへ旅行しました。","take a trip to ～ で『～へ旅行する』。took は take の過去形。","took a trip で『りょこうした』だね。"),
                       ("For example, I like soccer, baseball, and basketball.","例えば、私はサッカー、野球、バスケットボールが好きです。","For example で『例えば』。前の many kinds of sports の具体例を挙げている。","For example は『たとえば』だよ。")],
             passage="[出典: 大問1 Q9]\n"+filled(9)+"\n\n[出典: 大問1 Q12]\n"+filled(12),
             passageJa="古い写真の女の子はカレンにとても似ている。それは15歳のときのカレンの母だった。B はたくさんの種類のスポーツが好きで、例えばサッカー、野球、バスケットボールが好きだ。",
             patterns=["looks like","took a trip","For example","best of all","Hurry up"],
             questions=[("Q9で looks を選ぶのはなぜ？","look like ～ で『～に似ている』という意味になるから。主語 She に合わせて looks になっている。"),
                        ("Q13で best を使う根拠は？","of all（すべての中で）があるから。『いちばん好き』は like ～ best で表す。better は2つを比べるときの形。"),
                        ("Q15で sending を選ぶのはなぜ？","stop の後ろに動詞の -ing 形を置くと『～するのをやめる』という意味になるから。Stop sending messages で『メッセージを送るのをやめなさい』。")],
             easyQuestions=[("『～ににている』は、どのセット？","look like だよ。"),("『たとえば』は、えいごで？","For example だよ。"),("『いそいで！』は？","Hurry up! だよ。")]),
        dict(title="会話は「前後の文」から選ぶ",subtitle="Conversation Clues",color="#34d399",label="会話の手がかり",
             explanation="空所の前後の文から、空所の役割を考える。Q16 はスパゲッティのおかわりを No と断っているので、断る理由になる I'm full.。Q17 は Are you OK? への返事で、後ろの I didn't sleep well last night. が理由になる I'm tired.。Q18 は one brother を His で受けて名前を伝える His name is Ben.。Q19 は Where（どこ）への答えなので場所を表す In a small town near here. で、続く there はその町を指す。Q20 は I'm fine, thanks. という返事から、気分を尋ねる How do you feel?。前後の文とつながるかを確かめよう。",
             simple="まえとあとのぶんがヒント。『おかわりは？』『いらない、おなかいっぱい』。『どこでうまれたの？』『このちかくのまち』だね。",
             source="大問2 Q16・Q19・Q20",quote="No, Dad, I'm full. / Where were you born, Julie? / In a small town near here. / How do you feel? / I'm fine, thanks.",
             examples=[("No, Dad, I'm full.","いいえ、お父さん、おなかがいっぱいです。","No と断る理由として、満腹だと伝えている。","おなかいっぱいだから、いらないんだね。"),
                       ("In a small town near here.","この近くの小さな町で。","Where were you born? への答えで、生まれた場所を伝えている。","うまれたばしょを、こたえているよ。"),
                       ("How do you feel?","気分はどうですか。","返事の I'm fine, thanks. が気分を伝えている。","『きぶんはどう？』だね。")],
             passage="[出典: 大問2 Q16]\n"+filled(16)+"\n\n[出典: 大問2 Q19]\n"+filled(19)+"\n\n[出典: 大問2 Q20]\n"+filled(20),
             passageJa="父がスパゲッティのおかわりをすすめるが、ローラはおなかがいっぱいだと断る。ジュリーはこの近くの小さな町で生まれ、いつかそこへ連れて行くと言う。母が今日はずっと元気そうだと言って気分を尋ね、ティムは元気だと答える。",
             patterns=["I'm full","I'm tired","His name is Ben","near here","How do you feel"],
             questions=[("Q16で I don't know it. が合わないのはなぜ？","おかわりをすすめられて No と断る場面なので、断る理由が必要。知らないと言っても、スパゲッティを食べるかどうかの返事にならない。"),
                        ("Q18で They're very kind. を選ばないのは？","They're は複数の人を指す。男の子の兄弟は one brother（1人）なので、1人を指す His で始まる His name is Ben. が合う。"),
                        ("Q19の there は何を指す？","a small town near here（この近くの小さな町）。女性2は、自分が生まれたその町に、いつか連れて行くと言っている。")],
             easyQuestions=[("I'm full. は、どんないみ？","おなかがいっぱい、だよ。"),("Where were you born? のこたえは？","うまれたばしょ、をこたえるよ。"),("How do you feel? のこたえは？","I'm fine, thanks. だよ。")]),
        dict(title="並べ替え——5つの「型」を知る",subtitle="Five Sentence Patterns",color="#a78bfa",label="整序の型",
             explanation="Q21 は can＋動詞の原形と both A and B（A と B の両方）。Q22 は went to＋場所と by＋乗り物（～で）。Q23 は be good at（～が得意だ）の否定文 is not good at。Q24 は plays the guitar に better than（～よりじょうずに）を続け、文末の do は play the guitar のくり返しを避けた語。Q25 は read this interesting story と again and again（何度も）。『my family』『the guitar』『interesting story』はそれぞれ1つの語句なので分けずに、5つの語句の位置を数える。最初から書かれている Akiko / My sister / I や文末の語は数えない。Q22 は空所が文の最初から始まる。完成文を作ってから、2番目と4番目を選択肢と照らし合わせる。",
             simple="5つのことばのかたまりをならべよう。my family や the guitar は2つにわけないよ。さいしょからかいてある Akiko や My sister は、ばんごうにかぞえない。あいているところの2ばんめと4ばんめをたしかめよう。",
             source="大問3 Q21～Q25（並べ替え後の完成文）",quote="Akiko can speak both English and Russian. / My sister is not good at cooking. / I read this interesting story again and again.",
             examples=[(filled(21),"明子は英語とロシア語の両方を話すことができます。","can→speak→both→English→and。2番目②speak、4番目③English。","2ばんめ speak、4ばんめ English だね。"),
                       (filled(23),"私の姉は料理が得意ではありません。","is→not→good→at→cooking。2番目①not、4番目②at。","is not good at のじゅんばんだよ。"),
                       (filled(25),"私はこの面白い物語を何回も読みました。","read→this→interesting story→again→and。2番目③this、4番目④again。","again and again で『なんども』だね。")],
             passage="\n\n".join(f"[出典: 大問3 Q{n} 完成文]\n"+filled(n) for n in range(21,26)),
             passageJa="明子は英語とロシア語の両方を話せる。私の家族は8月に車で北海道へ行った。私の姉は料理が得意ではない。妹は私よりじょうずにギターを弾く。私はこの面白い物語を何回も読んだ。",
             patterns=["both English and","went to Hokkaido","not good at","better than","again and again"],
             questions=[("Q22で by を car の前に置くのはなぜ？","by＋乗り物で『～で（交通手段）』を表すから。by car で『車で』。文末の car in August に by をつなげる。"),
                        ("Q24の2番目・4番目は？","plays→the guitar→better→than→I なので、③the guitar と⑤than。選択肢3。"),
                        ("Q24の文末の do は何を表す？","play the guitar（ギターを弾く）のくり返しを避けた語。than I do で『私が弾くより』。")],
             easyQuestions=[("the guitar は、2つにわけてかぞえる？","わけないよ。1つのかたまりとしてかぞえるよ。"),("Q22で、さいしょにくることばは？","my family だよ。ぶんのはじめだけど、こもじになっているよ。"),("こたえるのは、どこ？","あいているところの2ばんめと4ばんめだよ。")]),
        dict(title="読解——掲示・メール・物語の読み分け",subtitle="Notice, E-mail & Story Reading",color="#f472b6",label="読解キーワード",
             explanation="【掲示】look for は『～を探す』。our dog Kuro が選択肢では his family's pet dog と言いかえられている。体は黒と白、足は茶色、背中に灰色の丸い模様と、体の部分ごとに色を対応させる。【メール】1通目でマデリンは、祖母と行く遊園地にルビーを誘っている。2通目でルビーは、姉（妹）が大学から帰ってくるので午後6時より前に帰らなければならないこと、お菓子を買うことを書いている。【物語】ミンディは今は会社で働いている。兄（弟）にテニスをすすめられたが好きになれず、新聞で無料のサッカーレッスンの記事を見た。木曜日に初めてコーチに会い、公園が職場の近くなので歩いて通う。人物・時・場所をセットにして、根拠の文へ戻る。",
             simple="けいじは、からだのどこが、なにいろか。メールは、だれが、なにをするか。ものがたりは、いつ、なにをしたかをわけよう。",
             source="大問4A・4B・4C",quote="Her legs are brown. / Next Friday, she will take me to an amusement park near the lake. / My sister will come home from college, and my mom will cook a special dinner for our family. / Mindy went to the park on Thursday and met the soccer coach for the first time.",
             examples=[("Her legs are brown.","足は茶色です。","体（body）・足（legs）・背中（back）で色が違う。legs の色を読む。","あしはちゃいろだね。"),
                       ("I can go with you on Friday, but I have to be home before 6 p.m.","金曜日は一緒に行けるけど、午後6時より前には家に帰っていないといけません。","have to は『～しなければならない』。その理由は次の文に書かれている。","have to は『～しなければならない』だよ。"),
                       ("She walks to Graystone Park because it is near her office.","公園が職場の近くにあるので、ミンディはグレーストーン公園まで歩いて行きます。","because の後ろが理由。it は Graystone Park を指す。","because は『～だから』だよ。")],
             passage="[出典: 大問4A]\n"+notice["paragraphs"][2]+"\n\n[出典: 大問4B 2通目のメール]\n"+" ".join(r[0] for r in email["sentencePairs"][18:22])+"\n\n[出典: 大問4C 最終段落]\n"+story["paragraphs"][3],
             passageJa="【掲示】シゲの家族は、犬のクロを探している。クロは体長約60センチで、体は黒と白、足は茶色、背中に灰色の丸い模様がいくつかある。水曜日の午後にサンシャイン公園ではぐれた。\n【メール】ルビーは金曜日に一緒に行けるが、午後6時より前に家に帰らなければならない。姉（妹）が大学から帰ってきて、母が家族のために特別な夕食を作るからだ。水筒などを持って行くべきか尋ね、お菓子を買うので一緒に分けようと言う。\n【物語】ミンディは楽しく過ごし、新しい友だちができた。今は毎週仕事の後にサッカーのレッスンに通っている。公園が職場の近くにあるので、歩いて行く。",
             patterns=["looking for","legs are brown","amusement park","come home from college","some snacks","works at a company","free soccer lessons","on Thursday","near her office"],
             questions=[("Q27で Gray. を選ばない理由は？","灰色は背中の丸い模様（gray circles on her back）の色。足（legs）の色は Her legs are brown. で茶色。"),
                        ("Q29の理由はどこに書いてある？","I can go with you on Friday, but I have to be home before 6 p.m. の次の文。My sister will come home from college（姉（妹）が大学から帰ってくる）とある。"),
                        ("Q34で On Tuesday. を選ばない理由は？","火曜日は練習日の一つとして書かれているだけ。ミンディが公園へ行き、初めてコーチに会ったのは on Thursday（木曜日）。")],
             easyQuestions=[("クロのあしは、なにいろ？","ちゃいろだよ。"),("ルビーがかうものは？","おかしだよ。"),("ミンディがあるいてこうえんへいくのは、なぜ？","こうえんが、しょくばのちかくにあるからだよ。")]),
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

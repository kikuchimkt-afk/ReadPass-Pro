"""Grade 4's existing 30-word / four-focus-point / normal-and-easy format."""
import re

VOCAB=[
    ("cloudy","くもった","形容詞","It was cloudy this morning.","今朝はくもっていました。",["晴れた","雨の","雪の"],"大問1 Q1","cloudy"),
    ("company","会社","名詞","My mother works for a car company.","母は自動車会社に勤めています。",["工場","銀行","学校"],"大問1 Q2","company"),
    ("hour","時間","名詞","I watch TV for an hour every day.","私は毎日1時間テレビを見ます。",["分","秒","日"],"大問1 Q3","hours"),
    ("present","プレゼント・贈り物","名詞","I got a nice present from my aunt.","私はおばからすてきなプレゼントをもらいました。",["手紙","写真","お金"],"大問1 Q4","present"),
    ("language","言語・言葉","名詞","Spanish is a beautiful language.","スペイン語は美しい言語です。",["季節","科目","国"],"大問1 Q5","language"),
    ("together","一緒に","副詞","Let's walk to school together.","一緒に歩いて学校へ行こう。",["別々に","ひとりで","すぐに"],"大問1 Q6","together"),
    ("remember","覚えている","動詞","I remember my first day at this school.","私はこの学校での最初の日を覚えています。",["忘れる","見つける","学ぶ"],"大問1 Q7","remember"),
    ("over there","あそこに・向こうに","熟語","My bike is over there.","私の自転車はあそこにあります。",["ここに","後ろに","下に"],"大問1 Q8","over there"),
    ("say goodbye to","～にさよならを言う","熟語","I said goodbye to my friends at the station.","私は駅で友だちにさよならを言いました。",["～にお礼を言う","～を待つ","～に会う"],"大問1 Q9","Say goodbye to"),
    ("in the afternoon","午後に","熟語","I play tennis in the afternoon.","私は午後にテニスをします。",["午前中に","夜に","正午に"],"大問1 Q10","in the afternoon"),
    ("have to","～しなければならない","熟語","I have to clean my room today.","私は今日、部屋を掃除しなければなりません。",["～したい","～してもよい","～するのが好きだ"],"大問1 Q11","have to"),
    ("come from","～の出身だ","熟語","Our new teacher comes from Australia.","私たちの新しい先生はオーストラリア出身です。",["～へ行く","～に住む","～を訪ねる"],"大問1 Q12","comes from"),
    ("touch","さわる","動詞","Don't touch the cake, Ken.","ケン、そのケーキにさわらないで。",["見る","使う","運ぶ"],"大問1 Q13","touch"),
    ("take a picture","写真を撮る","熟語","Can I take a picture here?","ここで写真を撮ってもいいですか。",["絵を描く","手紙を書く","映画を見る"],"大問1 Q14","take a picture"),
    ("table tennis","卓球","名詞","We played table tennis after school.","私たちは放課後に卓球をしました。",["テニス","野球","バドミントン"],"大問1 Q15","table tennis"),
    ("ready","準備ができた","形容詞","Are you ready for the test?","テストの準備はできていますか。",["疲れた","忙しい","遅れた"],"大問2 Q16","ready"),
    ("forget","忘れる","動詞","Don't forget your umbrella.","傘を忘れないでね。",["覚えている","見つける","買う"],"大問2 Q17","forgot"),
    ("Here you are.","はい、どうぞ。","表現","Here you are. This is your ticket.","はい、どうぞ。これがあなたのチケットです。",["どういたしまして。","おかえりなさい。","いただきます。"],"大問2 Q17","Here you are."),
    ("homework","宿題","名詞","I did my homework after dinner.","私は夕食後に宿題をしました。",["授業","試験","休み時間"],"大問2 Q19","homework"),
    ("need","必要とする","動詞","I need a new notebook.","私は新しいノートが必要です。",["売る","捨てる","貸す"],"大問2 Q20","need"),
    ("finish","終える","動詞","I finished my homework before dinner.","私は夕食の前に宿題を終えました。",["始める","忘れる","手伝う"],"大問3 Q22","finished drawing"),
    ("take","（人を）連れて行く","動詞","My father took us to the beach.","父は私たちを海辺へ連れて行ってくれました。",["迎えに行く","探す","世話をする"],"大問3 Q24","took me to"),
    ("tell","（人に）話す・伝える","動詞","My friend told me about his trip.","友だちは私に旅行のことを話してくれました。",["尋ねる","書く","考える"],"大問3 Q25","tell me about"),
    ("be interested in","～に興味がある","熟語","My brother is interested in old cars.","兄（弟）は古い車に興味があります。",["～が苦手だ","～に疲れている","～を怖がる"],"大問4A","interested in"),
    ("arrive","到着する","動詞","The train will arrive at ten.","電車は10時に到着します。",["出発する","待つ","止まる"],"大問4A","arrive"),
    ("surprise","驚き・サプライズ","名詞","The party was a big surprise for her.","そのパーティーは彼女にとって大きな驚きでした。",["約束","心配","失敗"],"大問4B","surprise"),
    ("best","（the best で）いちばん","副詞","I like summer the best.","私は夏がいちばん好きです。",["少しだけ","ときどき","まったく～ない"],"大問4B","the best"),
    ("future","将来・未来","名詞","I want to live in Canada in the future.","私は将来カナダに住みたいです。",["過去","今日","週末"],"大問4C","future"),
    ("nurse","看護師","名詞","My aunt is a nurse at a big hospital.","おばは大きな病院の看護師です。",["医者","教師","科学者"],"大問4C","nurse"),
    ("volunteer","ボランティア","名詞","She works as a volunteer at the library.","彼女は図書館でボランティアとして働いています。",["店員","先生","生徒"],"大問4C","volunteer"),
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
    spec=importlib.util.spec_from_file_location("order",Path(__file__).with_name("gen_g4_2024-3_sat_order.py"))
    o=importlib.util.module_from_spec(spec);spec.loader.exec_module(o)
    qs=[q for s in sections for q in s.get("questions",[])]
    def filled(n):
        q=next(q for q in qs if q["number"]==n)
        return o.completed(q) if "words" in q else q["text"].replace("(　)",q["choices"][q["answer"]-1])
    notice,email,story=sections[3]["passages"]
    specs=[
        dict(title="語句は「セット」で覚える",subtitle="Vocabulary & Useful Phrases",color="#4f8cff",label="語句のセット",
             explanation="単語の意味だけでなく、前後の語とセットで覚える。Q8 は over there（あそこに）、Q9 は say goodbye to（～にさよならを言う）、Q10 は in the afternoon（午後に）、Q11 は have to（～しなければならない）、Q12 は come from（～の出身だ）。Q13 は please don't＋動詞の原形で『～しないでください』、Q15 は昨日のことを尋ねる質問に合わせて過去形 played。空所の前後を一緒に読み、どのセットになるかを確かめよう。",
             simple="たんごは、まえやうしろのことばといっしょにおぼえよう。over there は『あそこに』。have to は『～しなきゃいけない』。come from は『～しゅっしん』だよ。",
             source="大問1 Q8・Q11・Q12",quote="It's over there. / I have to study for my math test tomorrow. / Yukiko's father comes from Canada, but he can speak Japanese very well.",
             examples=[("It's over there.","あそこにあります。","over there で『あそこに・向こうに』。over と there をセットで使う。","over there は『あそこに』だよ。"),
                       ("I have to study for my math test tomorrow.","明日の数学のテストのために勉強しなければなりません。","have to＋動詞の原形で『～しなければならない』。to の後ろは原形 study。","have to は『～しなきゃいけない』だね。"),
                       ("Yukiko's father comes from Canada, but he can speak Japanese very well.","ユキコのお父さんはカナダ出身ですが、日本語をとても上手に話せます。","come from ～で『～の出身だ』。主語が Yukiko's father なので comes。","comes from で『～しゅっしん』だよ。")],
             passage="[出典: 大問1 Q9]\n"+filled(9)+"\n\n[出典: 大問1 Q11]\n"+filled(11),
             passageJa="エミリーは学校へ行く準備ができ、母にお父さんへのさよならを頼む。映画に誘われた人は、明日の数学のテストのために勉強しなければならないので断る。",
             patterns=["over there","goodbye to","in the afternoon","have to","comes from"],
             questions=[("Q8で there を選ぶのはなぜ？","over there で『あそこに・向こうに』という決まった言い方になるから。駅の場所を尋ねられて、向こうを指して答えている。"),
                        ("Q10で in を選ぶ根拠は？","in the afternoon で『午後に』。at は at three のような時刻に、on は on Sunday のような曜日に使う。"),
                        ("Q13の please don't touch はどんな意味？","『さわらないでください』。Don't＋動詞の原形で『～しないで』という否定の命令文になる。")],
             easyQuestions=[("『あそこに』は、えいごで？","over there だよ。"),("『～しなきゃいけない』は？","have to だよ。"),("『カナダしゅっしん』は？","comes from Canada だよ。")]),
        dict(title="会話は「前後の文」から選ぶ",subtitle="Conversation Clues",color="#34d399",label="会話の手がかり",
             explanation="空所の前後の文から、空所の役割を考える。Q14 は B が To take a picture of the pandas.（パンダの写真を撮るため）と目的を答えているので Why。Q16 は母が空所の後ろで Let's eat. と誘っているので Dinner is ready.。Q17 は女の子が Here you are.（はい、どうぞ）と物を渡しているので、借りたいと頼む Can I use yours?。Q18 は1か月前に習い始めたばかりなので A little.。Q19 は I'm sorry. と謝っているので I forgot it.。答えを入れた後、会話が自然につながるかを確かめよう。",
             simple="まえやあとのことばがヒント。『はい、どうぞ』なら『かしてくれる？』。『たべよう』なら『ごはんができたよ』だね。",
             source="大問1 Q14・大問2 Q16・Q17",quote="Why did you come to the zoo today? / To take a picture of the pandas. / Dinner is ready. Let's eat. / Can I use yours? / Here you are.",
             examples=[("Why did you come to the zoo today?","今日はなぜ動物園に来たのですか。","返事の To take a picture of the pandas. が目的を表すので Why。","りゆうをきいているよ。"),
                       ("Can I use yours?","あなたのを使ってもいいですか。","Can I ～? は許可を求める言い方。yours は your eraser のこと。","『かしてくれる？』とたのんでいるね。"),
                       ("I started learning a month ago.","1か月前に習い始めました。","始めたばかりなので、弾けるかどうかの質問に A little. と答える。","はじめたばかりだから、すこしだけだね。")],
             passage="[出典: 大問2 Q16]\n"+filled(16)+"\n\n[出典: 大問2 Q17]\n"+filled(17)+"\n\n[出典: 大問2 Q19]\n"+filled(19),
             passageJa="7時になっておなかがすいた娘に、母は夕食ができたと伝える。消しゴムを忘れた男の子は、ジェーンに消しゴムを使わせてほしいと頼む。理科の宿題がどこにあるかを先生に聞かれたエイミーは、忘れたと謝る。",
             patterns=["To take a picture","Dinner is ready","Can I use yours","A little","I forgot it"],
             questions=[("Q16で Yes, I will. が合わないのはなぜ？","Yes, I will. は質問や依頼に答える言い方。娘はおなかがすいたと言っているだけで、母は次に Let's eat. と誘っている。"),
                        ("Q17の yours は何を指す？","your eraser（あなたの消しゴム）。消しゴムを忘れたので、ジェーンのものを使わせてほしいと頼んでいる。"),
                        ("Q19で I forgot it. を選ぶ根拠は？","宿題の場所を聞かれて I'm sorry. と謝っているから。it は science homework を指す。")],
             easyQuestions=[("Here you are. は、どんないみ？","はい、どうぞ、だよ。"),("Q14のこたえ To take a picture は、どんないみ？","『しゃしんをとるため』だよ。"),("『ごはんができたよ』は、えいごで？","Dinner is ready. だよ。")]),
        dict(title="並べ替え——5つの「型」を知る",subtitle="Five Sentence Patterns",color="#a78bfa",label="整序の型",
             explanation="Q21 は What time did you＋動詞の原形 ～?（何時に～しましたか）。Q22 は finish＋-ing 形（～し終える）と a picture of ～（～の絵）。Q23 は I use this cup の後ろに when I drink tea（紅茶を飲む時）を加える形。Q24 は take＋人＋to＋場所（人を～へ連れて行く）の過去形 took。Q25 は please tell me about ～（私に～について話してください）。this cup・a museum・spring vacation はそれぞれ1つの語句なので2つに分けず、5つの語句の位置を数える。最初から書かれている What / I / My / Sally, please や文末の語は数えない。完成文を作ってから、2番目と4番目を選択肢と照らし合わせる。",
             simple="5つのことばのかたまりをならべよう。this cup や a museum は2つにわけないよ。さいしょからかいてある What や My は、ばんごうにかぞえない。あいているところの2ばんめと4ばんめをたしかめよう。",
             source="大問3 Q21～Q25（並べ替え後の完成文）",quote="What time did you get home yesterday? / I use this cup when I drink tea. / My uncle took me to a museum today.",
             examples=[(filled(21),"あなたはきのう何時に帰宅しましたか。","time→did→you→get→home。2番目③did、4番目①get。","2ばんめ did、4ばんめ get だね。"),
                       (filled(23),"私は紅茶を飲む時はこのカップを使います。","use→this cup→when→I→drink。2番目④this cup、4番目⑤I。","this cup は1つのかたまりだよ。"),
                       (filled(24),"叔父は今日私を博物館に連れて行ってくれました。","uncle→took→me→to→a museum。2番目①took、4番目⑤to。","took me to のじゅんばんだね。")],
             passage="\n\n".join(f"[出典: 大問3 Q{n} 完成文]\n"+filled(n) for n in range(21,26)),
             passageJa="あなたが昨日何時に帰宅したかを尋ねる。私は祖母の絵を描き終えた。私は紅茶を飲む時にこのカップを使う。叔父は今日、私を博物館に連れて行ってくれた。サリーに春休みについて話してほしいと頼む。",
             patterns=["What time","finished drawing","when I drink","took me to","tell me about"],
             questions=[("Q22で finished の後ろを drawing にするのはなぜ？","finish の後ろに『～すること』を続けるときは -ing 形にするから。finished drawing で『描き終えた』。"),
                        ("Q23の2番目・4番目は？","use→this cup→when→I→drink なので、④this cup と⑤I。選択肢1。"),
                        ("Q25は日本文に『私に』がないのに me を使うのはなぜ？","tell＋人＋about ～で『人に～について話す』という形になるから。話を聞くのは私なので me を入れる。")],
             easyQuestions=[("this cup は、2つにわけてかぞえる？","わけないよ。1つのかたまりとしてかぞえるよ。"),("さいしょの My も、ばんごうにいれる？","いれないよ。あいている5つのところだけだね。"),("こたえるのは、どこ？","あいているところの2ばんめと4ばんめだよ。")]),
        dict(title="読解——掲示・メール・物語の読み分け",subtitle="Notice, E-mail & Story Reading",color="#f472b6",label="読解キーワード",
             explanation="【掲示】時刻が2つ出てくる。8:00 a.m. は学校が始まる時刻、7:30 a.m. は参加する人が体育館に着く時刻。20 minutes は走りながら音楽を聞ける時間。【メール】1通目はマークの質問、2通目は祖母の答え。マークは最初おじいちゃんを動物園に連れて行きたかったが、雨が降りそうなので映画に変えた。祖父がいちばん好きなのはアクション映画。劇場へは祖母の車で行き、帰りはバスに乗る。【物語】数か月前に先生と話し、先月おじに頼み、先週ボランティアを始めた。昨日は女の子に声をかけられ、来年は大学に進む。時を表す語句と出来事をセットにして、根拠の文へ戻る。",
             simple="けいじは、2つのじかんをわける。メールは、だれがきいて、だれがこたえたか。ものがたりは、いつ、なにをしたかをじゅんばんにならべよう。",
             source="大問4A・4B・4C",quote="If you want to join, please arrive at the school gym at 7:30 a.m. / I'll take you to the Georgetown Theater in my car. / Sally started working as a volunteer there last week.",
             examples=[("Students can jog in the school gym before school starts at 8:00 a.m.","生徒は、午前8時に学校が始まる前に、学校の体育館でジョギングができます。","8:00 a.m. は学校が始まる時刻。体育館に着く時刻（7:30 a.m.）と区別する。","8じは、がっこうがはじまるじかんだよ。"),
                       ("He likes comedy movies and science fiction movies, but he likes action movies the best.","コメディー映画やSF映画も好きですが、いちばん好きなのはアクション映画です。","but の後ろの the best（いちばん）が答えの根拠。","いちばんすきなのは、アクションえいがだね。"),
                       ("Please take the bus when you go home.","家に帰るときは、バスに乗ってください。","バスは家に帰るときに乗るもの。劇場へ行くときは祖母の車。","バスは、かえるときだよ。")],
             passage="[出典: 大問4A]\n"+"\n".join(notice["paragraphs"][1:])+"\n\n[出典: 大問4B 第2のメール]\n"+" ".join(r[0] for r in email["sentencePairs"][18:24])+"\n\n[出典: 大問4C 第2段落]\n"+story["paragraphs"][1],
             passageJa="【掲示】ジョギングに興味はありますか。生徒は、午前8時に学校が始まる前に学校の体育館でジョギングができる。20分間、体育館の中を走りながら音楽を聞ける。先生たちが飲み物のジュースを持ってくる。参加したい人は、午前7時30分に体育館に来ること。\n【メール】おじいちゃんはホラー映画が好きではない。コメディー映画やSF映画も好きだが、いちばん好きなのはアクション映画。ジョージタウン劇場で新しいアクション映画をやっているので、それを見るとよい。劇場までは祖母が車で連れて行く。家に帰るときはバスに乗る。\n【物語】サリーのおじは、その病院で働いている。先月、サリーはボランティアをしてもよいかをおじに尋ね、おじは「もちろん」と答えた。サリーは先週ボランティアを始めた。キッチンから病院の人たちのところへ食べ物を運び、その人たちと話もする。その中には子どもたちもいて、サリーと話すとうれしそうにしている。",
             patterns=["8:00 a.m.","7:30 a.m.","the best","in my car","A few months ago","Last month","last week"],
             questions=[("Q26で 8:00 a.m. を選ばない理由は？","8:00 a.m. は学校が始まる時刻。参加する人が体育館に着くのは 7:30 a.m.（午前7時30分）。"),
                        ("Q30で By bus. を選ばない理由は？","バスは家に帰るときに乗るもの。劇場へは祖母が車で連れて行く（I'll take you to the Georgetown Theater in my car.）。"),
                        ("Q32の答えの根拠はどこ？","Sally started working as a volunteer there last week. の last week。Last month はおじに頼んだ時、A few months ago は先生と話をした時。")],
             easyQuestions=[("たいいくかんにつくのは、なんじ？","ごぜん7じ30ぷんだよ。"),("おじいちゃんがいちばんすきなえいがは？","アクションえいがだよ。"),("サリーがボランティアをはじめたのは、いつ？","せんしゅうだよ。")]),
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

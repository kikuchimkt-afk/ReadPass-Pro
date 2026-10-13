"""Grade 3's established 30-word, four-focus-point, normal/easy lesson format (2026-2, main venue).

Audio references are added later by data/grade3/2026-2/_gen_tts.py.
"""

VOCAB=[
    ("blossom","（木の）花","名詞","The cherry blossoms in the park are beautiful.","公園の桜の花は美しいです。",["思い出","石","ページ"],"大問1 Q1","blossoms"),
    ("delivery service","配達サービス","名詞","This shop has a delivery service.","この店には配達サービスがあります。",["予約","割引","会員"],"大問1 Q2","delivery service"),
    ("improve","向上させる・上達させる","動詞","I read English books to improve my reading.","読む力を伸ばすために、英語の本を読みます。",["急ぐ","壊す","覆う"],"大問1 Q3","improve"),
    ("sentence","文","名詞","Please write three sentences about your family.","家族について3つの文を書いてください。",["花火","大会","思い出"],"大問1 Q4","sentences"),
    ("local","地元の","形容詞","We often eat at a local restaurant.","私たちはよく地元のレストランで食事をします。",["静かな","弱い","大きい"],"大問1 Q5","local"),
    ("protect","守る","動詞","Sunglasses protect your eyes.","サングラスは目を守ります。",["招待する","過ごす","ついて行く"],"大問1 Q6","protect"),
    ("by","～のそばに","前置詞","There is a big tree by the station.","駅のそばに大きな木があります。",["～の下に","～について","～から"],"大問1 Q7","by a small river"),
    ("be proud of","～を誇りに思う","熟語","I am proud of my team.","私は自分のチームを誇りに思います。",["～を怖がる","～に遅れる","～が苦手である"],"大問1 Q8","proud of"),
    ("show ... around","～を案内する","熟語","I will show you around my school.","私の学校を案内します。",["～を迎えに行く","～を待つ","～を手伝う"],"大問1 Q9","show him around"),
    ("be tired of","～に飽きている","熟語","I'm tired of watching TV.","テレビを見るのに飽きました。",["～が得意である","～を誇りに思う","～の準備ができている"],"大問1 Q10","tired of"),
    ("be ready for","～の準備ができている","熟語","Are you ready for the test?","テストの準備はできていますか。",["～に遅れる","～に近い","～に飽きている"],"大問1 Q11","ready for"),
    ("give up","あきらめる","熟語","Don't give up. You can do it.","あきらめないで。あなたならできます。",["始める","見つける","取る"],"大問1 Q12","give up"),
    ("volunteer work","ボランティア活動","名詞","My sister does volunteer work at a library.","姉（妹）は図書館でボランティア活動をしています。",["宿題","部活動","アルバイト"],"大問1 Q13","volunteer work"),
    ("cool","涼しい","形容詞","It is cool in the morning.","朝は涼しいです。",["暑い","晴れた","うるさい"],"大問1 Q14","cooler"),
    ("apartment","アパート・マンション","名詞","We live in an apartment near the station.","私たちは駅の近くのアパートに住んでいます。",["事務所","図書館","病院"],"大問2 Q16","apartment"),
    ("interesting","おもしろい・興味深い","形容詞","This science book is interesting.","この理科の本はおもしろいです。",["退屈な","眠い","難しい"],"大問2 Q17","interesting"),
    ("plate","皿","名詞","Please put the cake on this plate.","ケーキをこの皿にのせてください。",["コップ","いす","かばん"],"大問2 Q18","plate"),
    ("break","折る・壊す","動詞","He broke his arm last week.","彼は先週、腕を骨折しました。",["治す","洗う","運ぶ"],"大問2 Q19","broke"),
    ("lend","貸す","動詞","Can you lend me your pen?","ペンを貸してくれますか。",["借りる","売る","買う"],"大問2 Q20","lend"),
    ("report","レポート・報告書","名詞","I wrote a report about my town.","私は自分の町についてのレポートを書きました。",["地図","切符","招待状"],"大問3A","report"),
    ("interview","インタビューする","動詞","We will interview a famous chef.","私たちは有名なシェフにインタビューします。",["招待する","手伝う","説明する"],"大問3A","interview"),
    ("factory","工場","名詞","My father works at a car factory.","父は自動車工場で働いています。",["農場","駅","博物館"],"大問3A","factory"),
    ("absent","不在の・欠席の","形容詞","Ken was absent from school yesterday.","ケンは昨日、学校を休みました。",["忙しい","早い","元気な"],"大問3A","absent"),
    ("fight","けんかする","動詞","My brother and I sometimes fight.","兄（弟）と私は時々けんかします。",["約束する","笑う","練習する"],"大問3B 第1のメール","fought"),
    ("instead","その代わりに","副詞","I didn't drink coffee. I drank tea instead.","私はコーヒーを飲みませんでした。代わりに紅茶を飲みました。",["一緒に","もう一度","すぐに"],"大問3B 第3のメール","instead"),
    ("fix","修理する","動詞","My father can fix old radios.","父は古いラジオを修理できます。",["売る","塗る","借りる"],"大問3B 第3のメール","fix"),
    ("hunt","狩る","動詞","Lions hunt other animals for food.","ライオンは食べ物を得るために、ほかの動物を狩ります。",["育てる","守る","数える"],"大問3C","hunted"),
    ("decrease","減る","動詞","The number of students in this town decreased.","この町の生徒の数は減りました。",["増える","変わる","止まる"],"大問3C","decreased"),
    ("population","（人や動物の）数・人口","名詞","The population of this city is growing.","この市の人口は増えています。",["環境","政府","地域"],"大問3C","population"),
    ("environment","環境","名詞","We should protect the environment.","私たちは環境を守るべきです。",["政府","規則","森"],"大問3C","environment"),
]

def vocabulary():
    return [dict(word=word,meaning=meaning,pos=pos,level="3級",example=example,exampleJa=ja,distractors=distractors,source=source,sourceForm=form)
            for word,meaning,pos,example,ja,distractors,source,form in VOCAB]

def lessonplan(sections):
    qs=[q for s in sections[:2] for q in s["questions"]];ps=sections[2]["passages"]
    def filled(n):return qs[n-1]["text"].replace("(　)",qs[n-1]["choices"][qs[n-1]["answer"]-1])
    def excerpt(label,rows):return f"[出典: {label}]\n"+" ".join(r[0] for r in rows)
    a,b,c=[p["sentencePairs"] for p in ps]
    specs=[
        dict(title="熟語のセットと文の形で選ぶ",subtitle="Set Phrases & Sentence Patterns",color="#4f8cff",label="熟語と文の形",
             explanation="大問1は空所の前後をセットで読む。Q8 は be proud of ～『～を誇りに思う』、Q9 は show 人 around 場所『人に場所を案内する』、Q10 は be tired of ～ing『～するのに飽きている』、Q11 は be ready for ～『～の準備ができている』、Q12 は give up『あきらめる』。文の形では、Q13 の It's important for 人 to＋原形、Q14 の much＋比較級＋than、Q15 の付加疑問 isn't he? を確かめる。",
             simple="ことばはセットでおぼえよう。proud of は『～がじまん』、tired of は『～にあきた』、give up は『あきらめる』。much cooler than は『～よりずっとすずしい』、isn't he? は『～だよね』とたしかめる言い方だよ。",
             source="大問1 Q8・Q13・Q15",quote="Her parents were very proud of her. / I think it's important for us to do volunteer work. / That man is a famous Korean actor, isn't he?",
             examples=[(filled(8),"ミサは大きなピアノコンクールで銀メダルを取りました。両親は彼女をとても誇りに思いました。","be proud of 人で『人を誇りに思う』。of の後の her はミサ。proud は of とセットで使う。","proud of her は『ミサがじまん』ということだよ。"),
                       (filled(13),"A：ケイコ、私たちがボランティア活動をすることは大切だと思います。\nB：ええ、私もそう思います。病院で働きたいです。","It's important for 人 to＋動詞の原形で『人が～することは大切だ』。for us が to do の動作をする人を表す。","for us to do は『わたしたちがすること』だよ。"),
                       (filled(15),"A：あそこを見て！あの男性は有名な韓国の俳優ですよね。\nB：そのとおりです。","付加疑問は前の文に合わせる。be動詞 is の肯定文なので isn't he? で『～ですよね』と確かめる。","is の文だから、さいごは isn't he? だね。")],
             passage="\n\n".join(f"[出典: 大問1 Q{n}]\n"+filled(n) for n in [8,9,10,12,13,14]),
             passageJa="【Q8】ミサは銀メダルを取り、両親は彼女をとても誇りに思った。\n【Q9】新しい友達に町を案内しよう。\n【Q10】その本を読むのに飽きている。\n【Q12】長く大変な自転車レースでも、ほとんどの人はあきらめなかった。\n【Q13】私たちがボランティア活動をすることは大切だ。\n【Q14】山の頂上は、ふもとよりずっと涼しかった。",
             patterns=["proud of her","show him around","tired of reading","give up","for us to do","much cooler than"],
             questions=[("Q10で tired の後ろが of reading になるのはなぜ？","be tired of ～ing で『～するのに飽きている』。前置詞 of の後ろなので、動詞は ing形になる。"),
                        ("Q13で to do を選ぶ理由は？","It's important for 人 to＋動詞の原形の形だから。for us が『私たちが』を表し、to do が『すること』になる。"),
                        ("Q15で doesn't he? ではなく isn't he? になる理由は？","前の文が be動詞 is の肯定文だから。付加疑問では is を否定形の isn't にし、主語 that man を he で受ける。")],
             easyQuestions=[("give up はどんないみ？","あきらめる、だよ。"),("show him around our town はどんないみ？","かれにまちをあんないする、だよ。"),("much cooler than はどんないみ？","～よりずっとすずしい、だよ。")]),
        dict(title="会話は「答え」と「次のひと言」から考える",subtitle="Dialogue Clues Before & After",color="#34d399",label="会話の手がかり",
             explanation="大問2は空所の後ろのセリフが最大のヒント。Q16 は I moved here last summer に合う How long have you lived here?（現在完了で期間を尋ねる）。Q17 は It's really interesting に続けて I'm learning a lot と具体的に付け加える。Q18 は but I'll take it to the kitchen と逆接でつながる It's not mine。Q19 は She'll know の She が his sister を指す。Q20 は Of course. Come to my house に合う依頼 Will you lend me some?。",
             simple="あなのあとのセリフをよくよもう。『きょねんのなつにひっこした』なら『どのくらいすんでいるの？』。She'll know の she は、カズのおねえさんかいもうとだよ。Of course. なら、なにかをたのんだとわかるね。",
             source="大問2 Q16～Q20",quote="How long have you lived here? / Let's call and ask his sister. She'll know. / Will you lend me some?",
             examples=[(filled(16),"女性1：わあ！本当にすてきなアパートですね。ここにどのくらい住んでいるのですか。\n女性2：去年の夏にここへ引っ越してきました。","How long have you lived here? は現在完了で、住んでいる期間を尋ねる。引っ越した時期を答える返事と合う。","いつひっこしたかで、すんでいるながさがわかるね。"),
                       (filled(19),"男の子1：カズがサッカーの試合で足を骨折したって聞いた？\n男の子2：ううん、聞いていない。具合はどう？\n男の子1：電話して、カズのお姉さん（妹）に聞いてみよう。彼女なら知っているよ。","She'll know の She は his sister。聞く相手を示した選択肢だけが She とつながる。","She は、カズのおねえさんかいもうとのことだよ。"),
                       (filled(20),"女の子：私はDVDをたくさん持っているの。\n男の子：本当？何枚か貸してくれる？\n女の子：もちろん。放課後、私の家に来て。","Will you ～? は依頼。lend 人 物で『人に物を貸す』。some は some DVDs のこと。","Of course. は『いいよ』。かしてほしいとたのんだんだね。")],
             passage="\n\n".join(f"[出典: 大問2 Q{n}]\n"+filled(n) for n in range(16,21)),
             passageJa="【Q16】アパートにどのくらい住んでいるか尋ね、去年の夏に引っ越したと答える。\n【Q17】中国史の授業はとてもおもしろく、多くのことを学んでいる。\n【Q18】ソファの皿は自分のものではないが、台所へ持って行く。\n【Q19】カズのけがの様子は、電話でカズの姉（妹）に聞く。\n【Q20】DVDを貸してと頼み、放課後に家へ来るよう言われる。",
             patterns=["How long have you lived here?","I'm learning a lot.","It's not mine,","ask his sister","lend me some"],
             questions=[("Q16で Where did you live before? が合わない理由は？","返事の I moved here last summer は、ここへ来た時期を答えている。前に住んでいた場所ではなく、住んでいる期間の質問に合う。"),
                        ("Q18の but の前後はどうつながる？","『自分の皿ではない、でも台所へ持って行く』という逆接。It's not mine が but I'll take it と対になる。"),
                        ("Q19の She は誰を指す？","his sister（カズの姉か妹）。電話して聞く相手を示し、その人なら知っているとつなげている。")],
             easyQuestions=[("How long have you lived here? はどんないみ？","ここにどのくらいすんでいるの？、だよ。"),("It's not mine. はどんないみ？","それはわたしのものではない、だよ。"),("lend me some はどんないみ？","わたしにいくつかかして、だよ。")]),
        dict(title="掲示とメール——人物・時間・行動を結びつける",subtitle="People, Times & Actions",color="#a78bfa",label="人物と時間",
             explanation="掲示は指示を順に整理する。インタビューでは日々の仕事と the most difficult part を尋ね、選択肢では the hardest part に言い換えられる。質問がある人は今週の木曜日に White 先生を訪ねるが、午前は不在なので午後に行く。メールは書き手と me が誰かを確認する。第2のメールの me は祖父なので、果物を受け取るのは祖父。第3のメールでは、明日の午前に父と自転車を直し、午後に祖父を訪ねる。",
             simple="ホワイトせんせいは、もくようびのごご。ごぜんはいないよ。おじいさんのメールの me は、おじいさんのこと。アレックスは、あしたのごぜんにおとうさんとじてんしゃをなおして、ごごにおじいさんのいえへいくよ。",
             source="大問3A・3B",quote="What is the most difficult part of your work? / However, she is absent in the morning this week, so visit her in the afternoon! / One of my friends will give me many fruits tomorrow morning!",
             examples=[(a[7][0],a[7][1],"most difficult は difficult の最上級。設問の選択肢では the hardest part に言い換えられている。","いちばんたいへんなところ、をきくんだね。"),
                       (a[8][0]+" "+a[9][0],a[8][1]+a[9][1],"this Thursday に訪ねるが、However で条件が加わる。午前は absent なので、木曜日の午後になる。","もくようびのごごに、せんせいのところへいくよ。"),
                       (b[28][0],b[28][1],"第2のメールの書き手は祖父。me は祖父自身なので、果物を受け取るのは祖父。","me はおじいさん。くだものをもらうのはおじいさんだね。")],
             passage=excerpt("大問3A 面接の質問・質問の受付",a[5:10])+"\n\n"+excerpt("大問3B 第1のメール",b[6:8])+"\n\n"+excerpt("大問3B 第2のメール",b[26:29])+"\n\n"+excerpt("大問3B 第3のメール",[b[39],b[43],b[44]]),
             passageJa="【掲示】インタビューでは、日々の仕事と、仕事で最も難しい部分を尋ねる。質問がある人は今週の木曜日にホワイト先生を訪ねるが、今週の午前は不在なので午後に行く。\n【第1のメール】アレックスとダニエルは今朝けんかをした。好きなテレビゲームのことでだった。\n【第2のメール】祖父は今日家にいる。明日来れば祖母がフルーツケーキを作り、一緒に食べられる。明日の朝、友人が祖父にたくさんの果物をくれる。\n【第3のメール】アレックスは明日の午後、ダニエルと祖父を訪ねる。明日の午前に父と庭で自転車を直し、正午までに終わるかもしれない。",
             patterns=["the most difficult part","visit her in the afternoon","about our favorite video game","give me many fruits","with Dad in the garden"],
             questions=[("Q21で the hardest part が正解になる理由は？","掲示の the most difficult part を言い換えた表現だから。favorite part は掲示の質問にない。"),
                        ("Q22で木曜日の午前を選ばない理由は？","However の後に、今週の午前は absent（不在）とあるから。訪ねるのは木曜日の午後。"),
                        ("Q24で果物を受け取るのは誰？","祖父。第2のメールの書き手は Grandpa なので、give me の me は祖父を指す。")],
             easyQuestions=[("ホワイトせんせいにあえるのはいつ？","もくようびのごごだよ。"),("アレックスとダニエルは、なにでけんかした？","すきなテレビゲームのことだよ。"),("アレックスのあしたのごぜんのよていは？","おとうさんとじてんしゃをなおすよ。")]),
        dict(title="説明文——原因と結果のつながりを追う",subtitle="Cause & Effect in an Article",color="#f472b6",label="原因と結果",
             explanation="Gray Wolves は原因と結果の連続で書かれている。人が家を建てるために木を切る→オオカミがすみかを失う→人家の近くでペットや農場の動物を食べる→人が狩る→数が減る。1900年代には、オオカミが減って他の動物が長生きし、植物を多く食べた。1974年の新しい規則で南部のオオカミは増え、環境を大いに助けた。Therefore／so／because／Because of this などのつなぎ言葉が目印になる。",
             simple="オオカミのかずがへったり、ふえたりしたりゆうをおうよ。ひとがかったから、へった。へると、ほかのどうぶつがしょくぶつをたくさんたべた。あたらしいルールができて、また、ふえたんだね。so や because がヒントだよ。",
             source="大問3C 第2～4段落",quote="The main reason the gray wolves disappeared is that they were hunted by humans. / Therefore, the gray wolves lost their homes / Because of this, in just forty years",
             examples=[(c[4][0],c[4][1],"主語は The main reason the gray wolves disappeared（オオカミがいなくなった主な理由）と長い。動詞は is で、that 以下が理由の中身。","おもなりゆうは、ひとにかられたことだよ。"),
                       (c[6][0],c[6][1],"Therefore は『そのため』。前の文の『木を切って家を建てた』が原因で、すみかを失ったことが結果。","ひとが木をきったので、すむところがなくなったんだね。"),
                       (c[17][0],c[17][1],"Because of this の this は前の文の新しい規則。規則が原因で、南部のオオカミが増えたという結果をつなぐ。","ルールができたから、オオカミがふえたよ。")],
             passage=excerpt("大問3C 第2段落",c[4:10])+"\n\n"+excerpt("大問3C 第3・4段落",c[10:18]),
             passageJa="【第2段落】オオカミがいなくなった主な理由は、人に狩られたこと。1800年代、人は西部に移り住み、家を建てるために木を切った。そのためオオカミはすみかを失い、人家の近くへ行くしかなかった。ペットや農場の動物を食べたので人は嫌がって狩り、オオカミの数は減った。\n【第3・4段落】これが1900年代に新しい問題を生んだ。オオカミが減って他の動物が長生きし、植物を多く食べた。人々は、オオカミが森を助けていたと気づいた。1974年、政府はオオカミを殺したり傷つけたりしてはいけないという規則を作り、40年で南部のオオカミは増えた。",
             patterns=["The main reason","Therefore,","so they hunted","However, because","Because of this,"],
             questions=[("Q27で They ate farm animals が正解になる理由は？","本文の animals on people's farms（人々の農場の動物）を farm animals と言い換えている。人はそれを嫌って狩った。"),
                        ("Q28の1900年代の問題は何？","オオカミが減って他の動物が長生きし、植物を多く食べたこと。Animals ate a lot of plants が言い換え。"),
                        ("Q29で数が増えた原因を示す語句は？","Because of this。this は1974年の新しい規則（オオカミを殺したり傷つけたりしてはいけない）を指す。")],
             easyQuestions=[("オオカミがかられたのはなぜ？","ペットやのうじょうのどうぶつをたべたからだよ。"),("1900ねんだいのもんだいは？","どうぶつがしょくぶつをたくさんたべたことだよ。"),("オオカミがふえたのはなぜ？","あたらしいルールができたからだよ。")]),
    ]
    points=[]
    for n,s in enumerate(specs,1):
        points.append(dict(id=f"fp{n}",title=s["title"],subtitle=s["subtitle"],explanation=s["explanation"],explanationSimple=s["simple"],
                           sourceQuote=s["quote"],sourceLocation=s["source"],
                           examples=[dict(en=en,ja=ja,note=note,noteSimple=easy) for en,ja,note,easy in s["examples"]],
                           practicePassage=dict(en=s["passage"],ja=s["passageJa"],source=s["source"]),
                           highlightPatterns=s["patterns"],highlightColor=s["color"],highlightLabel=s["label"],
                           practiceQuestions=[dict(q=q,a=a) for q,a in s["questions"]],practiceQuestionsSimple=[dict(q=q,a=a) for q,a in s["easyQuestions"]]))
    return dict(focusPoints=points)

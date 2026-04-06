"""Generate data.json for Pre-Grade 2 2022-2 (Part 1: sections 0-1)"""
import json, os

data = {
    "grade": "準2級",
    "year": "2022",
    "session": "2",
    "title": "2022年度 第2回 英検準2級 リーディング",
    "vocabulary": [],
    "sections": [],
    "lessonPlan": {}
}

# =====================================================
# Section 0: 大問1（vocabulary型・20問）
# =====================================================
section1 = {
    "name": "大問1",
    "nameEn": "Part 1",
    "type": "vocabulary",
    "instruction": "次の(1)から(20)までの(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選びなさい。",
    "questions": [
        {
            "number": 1,
            "text": "The two leaders decided to stop the war between their countries. They promised their people that there would be ( 1 ).",
            "translation": "二人の指導者は両国間の戦争をやめることを決めた。彼らは国民に( 1 )があるだろうと約束した。",
            "choices": ["peace", "faith", "honor", "matter"],
            "choiceTranslations": ["平和", "信仰", "名誉", "問題"],
            "answer": 1,
            "choiceAnalysis": ["✅ peace＝平和。戦争をやめた後に平和が来る→正解", "❌ faith＝信仰。戦争終結の文脈に合わない", "❌ honor＝名誉。戦争をやめる約束の内容として不適切", "❌ matter＝問題。平和の反対の意味になり矛盾"],
            "grammar": "💡 peace＝平和。promise (that) ～＝～と約束する。There would be ～＝～があるだろう（仮定法の一種）"
        },
        {
            "number": 2,
            "text": "Troy's feet have grown so much this year that none of his shoes ( 2 ) him. His mother is taking him shopping today to buy new ones.",
            "translation": "トロイの足は今年とても大きくなったので、どの靴も彼に( 2 )なくなった。母親は新しい靴を買いに今日彼を買い物に連れて行く。",
            "choices": ["sew", "fit", "cure", "gain"],
            "choiceTranslations": ["縫う", "合う", "治す", "得る"],
            "answer": 2,
            "choiceAnalysis": ["❌ sew＝縫う。靴のサイズの問題とは無関係", "✅ fit＝合う、フィットする。足が大きくなったので靴が合わない→正解", "❌ cure＝治す。靴の文脈に合わない", "❌ gain＝得る。靴が人を得るのは不自然"],
            "grammar": "💡 fit＝合う、フィットする。so...that～＝とても…なので～。none of ～＝～のどれも…ない"
        },
        {
            "number": 3,
            "text": "The little girl wanted to play with the cat. But whenever she ( 3 ) it, the cat ran away.",
            "translation": "その小さな女の子は猫と遊びたかった。しかし彼女が猫に( 3 )するたびに、猫は逃げてしまった。",
            "choices": ["celebrated", "approached", "separated", "researched"],
            "choiceTranslations": ["祝った", "近づいた", "分離した", "研究した"],
            "answer": 2,
            "choiceAnalysis": ["❌ celebrated＝祝った。猫と遊ぶ文脈に合わない", "✅ approached＝近づいた。近づくと猫が逃げる→正解", "❌ separated＝分離した。離れる動作では逃げる必要がない", "❌ researched＝研究した。猫に対して使う表現ではない"],
            "grammar": "💡 approach＝近づく（他動詞で前置詞不要）。whenever＝～するたびに。run away＝逃げる"
        },
        {
            "number": 4,
            "text": "Momoko lives in Tokyo, which is in the ( 4 ) part of Japan. Every summer, she takes a train and visits her grandfather in Osaka, which is in the west.",
            "translation": "モモコは日本の( 4 )に位置する東京に住んでいる。毎年夏、彼女は電車に乗って西にある大阪の祖父を訪ねる。",
            "choices": ["relative", "eastern", "smooth", "brave"],
            "choiceTranslations": ["相対的な", "東部の", "滑らかな", "勇敢な"],
            "answer": 2,
            "choiceAnalysis": ["❌ relative＝相対的な。地理的な位置の説明に不適切", "✅ eastern＝東部の。東京は日本の東部にある→正解", "❌ smooth＝滑らかな。地理の文脈に合わない", "❌ brave＝勇敢な。地域の説明に合わない"],
            "grammar": "💡 eastern＝東部の。east（名詞：東）の形容詞形。western＝西部の。which is ～＝関係代名詞の非制限用法"
        },
        {
            "number": 5,
            "text": "Xiang could not go to work for two weeks because of a serious ( 5 ). She had to take a lot of medicine and went to see the doctor many times.",
            "translation": "シャンは重い( 5 )のために2週間仕事に行けなかった。たくさんの薬を飲み、何度も医者に通わなければならなかった。",
            "choices": ["illness", "facility", "decade", "immigration"],
            "choiceTranslations": ["病気", "施設", "10年間", "移民"],
            "answer": 1,
            "choiceAnalysis": ["✅ illness＝病気。薬を飲み医者に通う→正解", "❌ facility＝施設。仕事を休む理由にならない", "❌ decade＝10年間。2週間の欠勤理由としては不適切", "❌ immigration＝移民。医者に通う文脈と無関係"],
            "grammar": "💡 illness＝病気。sick（形容詞）の名詞形。because of ～＝～のために（前置詞句）"
        },
        {
            "number": 6,
            "text": "Before Yasuko moved to her new apartment in Tokyo, she bought some ( 6 ). However, when she moved in, there was not enough space for the table and the bed.",
            "translation": "ヤスコが東京の新しいアパートに引っ越す前に、いくつかの( 6 )を買った。しかし、引っ越してみると、テーブルとベッドのための十分なスペースがなかった。",
            "choices": ["atmosphere", "religion", "furniture", "poverty"],
            "choiceTranslations": ["雰囲気", "宗教", "家具", "貧困"],
            "answer": 3,
            "choiceAnalysis": ["❌ atmosphere＝雰囲気。テーブルやベッドの文脈に合わない", "❌ religion＝宗教。引っ越しの買い物と無関係", "✅ furniture＝家具。テーブルとベッドは家具→正解", "❌ poverty＝貧困。買い物の対象ではない"],
            "grammar": "💡 furniture＝家具（不可算名詞）。a piece of furniture＝家具1点。some furniture＝いくつかの家具"
        },
        {
            "number": 7,
            "text": "In recent years, the city has had to build many new roads and schools because its population has grown so ( 7 ).",
            "translation": "近年、人口が非常に( 7 )増加したため、市は多くの新しい道路や学校を建設しなければならなくなった。",
            "choices": ["exactly", "pleasantly", "fairly", "rapidly"],
            "choiceTranslations": ["正確に", "心地よく", "公平に", "急速に"],
            "answer": 4,
            "choiceAnalysis": ["❌ exactly＝正確に。人口増加の速度の説明に不適切", "❌ pleasantly＝心地よく。人口増加の修飾語としては不自然", "❌ fairly＝公平に、かなり。道路・学校建設の必要性を説明するには弱い", "✅ rapidly＝急速に。急速な人口増加でインフラ整備が必要→正解"],
            "grammar": "💡 rapidly＝急速に。rapid（形容詞：急速な）の副詞形。population＝人口。in recent years＝近年"
        },
        {
            "number": 8,
            "text": "Cars are safer than motorcycles, but the ( 8 ) of motorcycles is that they use less gasoline.",
            "translation": "車はバイクより安全だが、バイクの( 8 )はガソリンの使用量が少ないことだ。",
            "choices": ["advantage", "destruction", "laboratory", "concentration"],
            "choiceTranslations": ["利点", "破壊", "実験室", "集中"],
            "answer": 1,
            "choiceAnalysis": ["✅ advantage＝利点。バイクの良い点としてガソリン消費の少なさ→正解", "❌ destruction＝破壊。バイクの利点の説明に合わない", "❌ laboratory＝実験室。バイクとの関係がない", "❌ concentration＝集中。ガソリンの使用量の文脈に合わない"],
            "grammar": "💡 advantage＝利点。反意語は disadvantage（欠点）。the advantage of ～ is that ...＝～の利点は…ということだ"
        },
        {
            "number": 9,
            "text": "The colors on a map sometimes show different features of the earth. Blue is used to ( 9 ) water, and green is often used to show forests.",
            "translation": "地図上の色は時に地球のさまざまな特徴を示す。青は水を( 9 )ために使われ、緑はしばしば森林を示すために使われる。",
            "choices": ["develop", "exchange", "represent", "guide"],
            "choiceTranslations": ["開発する", "交換する", "表す", "案内する"],
            "answer": 3,
            "choiceAnalysis": ["❌ develop＝開発する。色で水を開発する意味にならない", "❌ exchange＝交換する。色と水の交換は不自然", "✅ represent＝表す。青色が水を表す→正解", "❌ guide＝案内する。色が水を案内する表現は不自然"],
            "grammar": "💡 represent＝表す、代表する。be used to ～＝～するために使われる（受動態＋不定詞）。feature＝特徴"
        },
        {
            "number": 10,
            "text": "When my parents were young, a milkman brought milk to their homes every day, just like postmen and postwomen ( 10 ) letters to us now.",
            "translation": "親が若い頃、牛乳配達人が毎日家に牛乳を届けていた。ちょうど今、郵便配達員が私たちに手紙を( 10 )ようにだ。",
            "choices": ["balance", "deliver", "operate", "replace"],
            "choiceTranslations": ["バランスを取る", "届ける", "操作する", "取り替える"],
            "answer": 2,
            "choiceAnalysis": ["❌ balance＝バランスを取る。手紙の配達と無関係", "✅ deliver＝届ける。郵便配達員が手紙を届ける→正解", "❌ operate＝操作する。手紙には使わない表現", "❌ replace＝取り替える。手紙の文脈に合わない"],
            "grammar": "💡 deliver＝届ける、配達する。delivery（名詞）＝配達。just like ～＝ちょうど～のように"
        },
        {
            "number": 11,
            "text": "A : Brian, I think the new boy at school is really cute, but I don't know his name.\nB : He's in my gym class. I'll find ( 11 ) his name for you.",
            "translation": "A：ブライアン、学校の新しい男の子がすごくかっこいいと思うんだけど、名前がわからないの。\nB：彼は僕の体育のクラスにいるよ。彼の名前を( 11 )してあげるよ。",
            "choices": ["out", "up", "above", "away"],
            "choiceTranslations": ["外に", "上に", "上方に", "離れて"],
            "answer": 1,
            "choiceAnalysis": ["✅ out＝find out＝調べる、見つけ出す→正解", "❌ up＝find up は句動詞として存在しない", "❌ above＝find above は不自然な組み合わせ", "❌ away＝find away は不自然な組み合わせ"],
            "grammar": "💡 find out＝調べる、見つけ出す。I'll ～ for you.＝あなたのために～してあげる"
        },
        {
            "number": 12,
            "text": "A : I'm taking a drawing class, but my pictures are always terrible!\nB : Just ( 12 ) trying. It takes a long time to learn a skill like that.",
            "translation": "A：デッサン教室に通っているんだけど、いつもひどい絵ばかり！\nB：( 12 )続けなよ。そういうスキルを身につけるには長い時間がかかるよ。",
            "choices": ["turn on", "keep on", "bring up", "sit up"],
            "choiceTranslations": ["つける", "続ける", "育てる", "起き上がる"],
            "answer": 2,
            "choiceAnalysis": ["❌ turn on＝（電源を）つける。努力の継続には不適切", "✅ keep on＝～し続ける。練習を続けるよう励ます→正解", "❌ bring up＝育てる、持ち出す。文脈に合わない", "❌ sit up＝起き上がる。デッサンの練習と無関係"],
            "grammar": "💡 keep on ～ing＝～し続ける。It takes a long time to ～＝～するのに長い時間がかかる"
        },
        {
            "number": 13,
            "text": "Andrew applied ( 13 ) three jobs, and he is now waiting to hear if any of the companies want to interview him.",
            "translation": "アンドリューは3つの仕事に( 13 )し、今はどの会社が面接したいか連絡を待っている。",
            "choices": ["about", "for", "by", "across"],
            "choiceTranslations": ["～について", "～に", "～によって", "～を横切って"],
            "answer": 2,
            "choiceAnalysis": ["❌ about＝applied about は不自然な前置詞の組み合わせ", "✅ for＝apply for＝～に応募する→正解", "❌ by＝applied by は受動態の前置詞で文脈に合わない", "❌ across＝applied across は不自然な組み合わせ"],
            "grammar": "💡 apply for ～＝～に応募する。application（名詞）＝応募、申請。interview＝面接する"
        },
        {
            "number": 14,
            "text": "Lisa speaks to her parents on the phone every week because she lives far away and she misses them. After she ( 14 ), she soon starts to miss them again.",
            "translation": "リサは遠くに住んでいて両親が恋しいので、毎週電話で話をする。彼女が( 14 )した後、またすぐに恋しくなる。",
            "choices": ["hangs up", "carries out", "puts away", "goes ahead"],
            "choiceTranslations": ["電話を切る", "実行する", "片付ける", "先に進む"],
            "answer": 1,
            "choiceAnalysis": ["✅ hangs up＝電話を切る。電話を切った後にまた恋しくなる→正解", "❌ carries out＝実行する。電話の文脈に合わない", "❌ puts away＝片付ける。電話の会話の流れに合わない", "❌ goes ahead＝先に進む。電話の終了を意味しない"],
            "grammar": "💡 hang up＝電話を切る。miss＝恋しく思う。speak to ～ on the phone＝～と電話で話す"
        },
        {
            "number": 15,
            "text": "Sharon is really scared of spiders. There was one in her bedroom the other day. She jumped ( 15 ) of it, screamed, and hid in the bathroom.",
            "translation": "シャロンはクモが本当に怖い。先日、寝室に1匹いた。彼女はそれを( 15 )して飛び上がり、叫んでバスルームに隠れた。",
            "choices": ["for the life", "in the light", "at the sight", "on the point"],
            "choiceTranslations": ["命をかけて", "～の光の中で", "～を見て", "～の寸前に"],
            "answer": 3,
            "choiceAnalysis": ["❌ for the life＝命をかけて。文脈に合わない", "❌ in the light＝光の中で。クモを見る文脈に合わない", "✅ at the sight＝～を見て。クモを見て飛び上がった→正解", "❌ on the point＝寸前に。飛び上がる動作の理由にならない"],
            "grammar": "💡 at the sight of ～＝～を見て。be scared of ～＝～を怖がる。scream＝叫ぶ"
        },
        {
            "number": 16,
            "text": "Mr. Simmons not only teaches his students to play the piano but also tells them in ( 16 ) about the lives of the most famous pianists in history.",
            "translation": "シモンズ先生は生徒にピアノの弾き方を教えるだけでなく、歴史上最も有名なピアニストの生涯について( 16 )に話す。",
            "choices": ["case", "detail", "hand", "touch"],
            "choiceTranslations": ["場合", "詳細", "手", "接触"],
            "answer": 2,
            "choiceAnalysis": ["❌ case＝in case＝～の場合に。ここでは情報の詳しさを表す", "✅ detail＝in detail＝詳しく→正解", "❌ hand＝in hand＝手に持って。文脈に合わない", "❌ touch＝in touch＝連絡を取って。教える文脈に合わない"],
            "grammar": "💡 in detail＝詳しく、詳細に。not only A but also B＝AだけでなくBも"
        },
        {
            "number": 17,
            "text": "Daisy tried to ( 17 ) in several ways when she was at college. She had jobs in the college library and cafeteria, and she even worked as a model for art classes.",
            "translation": "デイジーは大学時代、いくつかの方法で( 17 )しようとした。大学の図書館やカフェテリアで働き、美術の授業のモデルまでした。",
            "choices": ["take pride", "make money", "give birth", "lose speed"],
            "choiceTranslations": ["誇りを持つ", "お金を稼ぐ", "出産する", "速度を落とす"],
            "answer": 2,
            "choiceAnalysis": ["❌ take pride＝誇りを持つ。複数の仕事の理由としては不適切", "✅ make money＝お金を稼ぐ。複数のアルバイトで稼ぐ→正解", "❌ give birth＝出産する。仕事の文脈に合わない", "❌ lose speed＝速度を落とす。アルバイトの文脈に合わない"],
            "grammar": "💡 make money＝お金を稼ぐ。earn money とも言う。in several ways＝いくつかの方法で"
        },
        {
            "number": 18,
            "text": "Jane's sister has four sons. One is a high school student, and ( 18 ) are elementary school students.",
            "translation": "ジェーンの姉には息子が4人いる。1人は高校生で、( 18 )は小学生だ。",
            "choices": ["all another", "another ones", "the other", "the others"],
            "choiceTranslations": ["すべての別の", "別のもの", "残りの1つ", "残りの全員"],
            "answer": 4,
            "choiceAnalysis": ["❌ all another＝文法的に不正確な表現", "❌ another ones＝another は単数で ones とは使えない", "❌ the other＝残りの1つ。4人中3人なので複数形が必要", "✅ the others＝残りの全員。4人中1人を除いた残り3人→正解"],
            "grammar": "💡 the others＝残りのすべて（複数）。one...the others＝1つは…残りは全部。another＝もう1つ（不特定の1つ）"
        },
        {
            "number": 19,
            "text": "Sandra thought her pet dog Charlie looked so cute ( 19 ) his new jacket. She took some photos of him and shared them online with her friends.",
            "translation": "サンドラはペットの犬チャーリーが新しいジャケットを( 19 )とてもかわいいと思った。写真を撮ってオンラインで友達と共有した。",
            "choices": ["at", "in", "of", "behind"],
            "choiceTranslations": ["～で", "～を着て", "～の", "～の後ろに"],
            "answer": 2,
            "choiceAnalysis": ["❌ at＝場所・時間を表す前置詞。衣服の着用には使わない", "✅ in＝～を着て。in his jacket＝ジャケットを着て→正解", "❌ of＝～の。衣服の着用には使わない", "❌ behind＝～の後ろに。衣服の着用とは異なる"],
            "grammar": "💡 in＝（衣服を）着て。in a red dress＝赤いドレスを着て。look cute in ～＝～を着てかわいく見える"
        },
        {
            "number": 20,
            "text": "Barcelona is the ( 20 ) city in Spain. Only Madrid is bigger.",
            "translation": "バルセロナはスペインで( 20 )都市だ。マドリードだけがそれより大きい。",
            "choices": ["second-largest", "second-larger", "two-larger", "two-largest"],
            "choiceTranslations": ["2番目に大きい", "2番目により大きい", "2つのより大きい", "2つの最も大きい"],
            "answer": 1,
            "choiceAnalysis": ["✅ second-largest＝2番目に大きい。マドリードだけが大きい＝2番目→正解", "❌ second-larger＝最上級にはlargestを使う", "❌ two-larger＝文法的に不正確", "❌ two-largest＝文法的に不正確"],
            "grammar": "💡 the second-largest＝2番目に大きい。序数＋最上級で「N番目に～な」を表す。the third-oldest＝3番目に古い"
        }
    ]
}

# =====================================================
# Section 1: 大問2（vocabulary型・5問・会話文空所補充）
# =====================================================
section2 = {
    "name": "大問2",
    "nameEn": "Part 2",
    "type": "vocabulary",
    "instruction": "次の(21)から(25)までの会話文の(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選びなさい。",
    "questions": [
        {
            "number": 21,
            "text": "A : Soccer practice normally finishes at 5 p.m., but Coach Stevens said that today's practice will finish at six.\nB : Really? Did he say that? I didn't hear him. I'd better call my mom and ask her to ( 21 ).\nA : Do you want to use my phone?\nB : Thanks! My mom will be angry if she has to wait for an hour.",
            "translation": "A：サッカーの練習は普通5時に終わるけど、スティーブンスコーチが今日は6時に終わると言ったよ。\nB：本当？そう言ったの？聞こえなかった。ママに電話して( 21 )って頼まなきゃ。\nA：僕の電話使う？\nB：ありがとう！1時間待たされたらママ怒るよ。",
            "choices": ["bring my soccer shoes", "pick me up later than usual", "speak to Coach Stevens", "keep my dinner warm"],
            "choiceTranslations": ["サッカーシューズを持ってきてもらう", "いつもより遅く迎えに来てもらう", "スティーブンスコーチに話してもらう", "夕食を温かく保っておいてもらう"],
            "answer": 2,
            "choiceAnalysis": ["サッカーシューズを持ってくる→練習時間の変更と無関係", "いつもより遅く迎えに来る→正解。💡 1時間遅く終わるので迎えも遅くなる必要がある", "コーチに話す→母親に頼む内容としては不自然", "夕食を温かくしておく→1時間待つ文脈に直接関係ない"],
            "grammar": "💡 pick me up＝迎えに来る。I'd better＝～した方がいい。later than usual＝いつもより遅く"
        },
        {
            "number": 22,
            "text": "A : Excuse me. Could you help me to find a book about making a garden?\nB : Certainly. We have several books that can help you. Do you plan to ( 22 )?\nA : Hmm. I think it would be fun to start with things I can eat, like potatoes and carrots.\nB : Then, this book will be perfect for you.",
            "translation": "A：すみません。ガーデニングについての本を見つけるのを手伝っていただけますか？\nB：もちろんです。お役に立てる本がいくつかあります。( 22 )する予定ですか？\nA：うーん。ジャガイモやニンジンのような食べられるものから始めたら楽しそうです。\nB：それなら、この本がぴったりですよ。",
            "choices": ["do it with someone else", "buy more than one book", "come to the library often", "grow flowers or vegetables"],
            "choiceTranslations": ["誰か他の人と一緒にする", "1冊以上の本を買う", "図書館によく来る", "花や野菜を育てる"],
            "answer": 4,
            "choiceAnalysis": ["誰か他の人とする→回答のジャガイモやニンジンの内容と繋がらない", "1冊以上買う→回答が食べ物の話なので文脈に合わない", "図書館によく来る→ガーデニングの計画を聞く質問ではない", "花や野菜を育てる→正解。💡 回答でジャガイモやニンジン（＝野菜）と言っているので花か野菜かを聞いている"],
            "grammar": "💡 plan to ～＝～する予定だ。grow＝育てる（植物を栽培する）。start with ～＝～から始める"
        },
        {
            "number": 23,
            "text": "A : Let's order some sausage pizzas for lunch after the meeting tomorrow. Four should be enough.\nB : Wait. Pete and Sarah don't eat meat.\nA : You're right. We'd better get something for them, too.\nB : Let's get ( 23 ).",
            "translation": "A：明日の会議の後、昼食にソーセージピザを注文しよう。4枚で足りるかな。\nB：待って。ピートとサラは肉を食べないよ。\nA：そうだったね。彼らの分も何か用意した方がいいね。\nB：( 23 )注文しよう。",
            "choices": ["two sausage pizzas and two chicken pizzas", "four extra-large chicken pizzas", "one sausage pizza and one vegetarian pizza", "three sausage pizzas and one vegetarian pizza"],
            "choiceTranslations": ["ソーセージピザ2枚とチキンピザ2枚", "特大チキンピザ4枚", "ソーセージピザ1枚とベジタリアンピザ1枚", "ソーセージピザ3枚とベジタリアンピザ1枚"],
            "answer": 4,
            "choiceAnalysis": ["ソーセージ2枚とチキン2枚→チキンも肉なのでピートとサラには不適切", "特大チキン4枚→全部チキン（肉）なので不適切", "ソーセージ1枚とベジタリアン1枚→元々4枚必要だったので少なすぎる", "ソーセージ3枚とベジタリアン1枚→正解。💡 肉を食べない2人にベジタリアン、残りにソーセージ。合計4枚"],
            "grammar": "💡 vegetarian＝菜食主義の。We'd better＝We had better＝～した方がいい。enough＝十分な"
        },
        {
            "number": 24,
            "text": "A : Mr. Taylor, I don't know what topic to choose for the class presentation. Can you help me?\nB : OK. Think about the things we've studied in class this year. Was there anything you liked?\nA : Well, I really enjoyed learning about ( 24 ).\nB : That would be a good topic. For example, you could talk about the strange fish that live deep in the sea.",
            "translation": "A：テイラー先生、クラス発表のトピックを何にしたらいいかわかりません。助けてもらえますか？\nB：いいよ。今年の授業で勉強したことを考えてみて。好きなものはあった？\nA：はい、( 24 )について学ぶのがとても楽しかったです。\nB：それはいいトピックだね。例えば、深海に住む変わった魚について話せるよ。",
            "choices": ["life in the ocean", "famous travelers", "recycling metal", "stars and planets"],
            "choiceTranslations": ["海の生き物", "有名な旅行者", "金属のリサイクル", "星と惑星"],
            "answer": 1,
            "choiceAnalysis": ["海の生き物→正解。💡 先生の「深海に住む変わった魚」の例示が直接の根拠", "有名な旅行者→深海の魚の話題と繋がらない", "金属のリサイクル→海の生き物と無関係", "星と惑星→海ではなく宇宙の話題"],
            "grammar": "💡 life in the ocean＝海の生き物。what topic to choose＝どのトピックを選ぶか（疑問詞＋不定詞）"
        },
        {
            "number": 25,
            "text": "A : I'll see what I can find at the library. Also, I can take a look on the Internet.\nB : If you need more help, come and talk to me anytime.",
            "translation": "A：図書館で何が見つかるか調べてみます。あと、インターネットでも見てみます。\nB：もっと助けが必要なら、いつでも来て話してね。",
            "choices": ["work with a partner", "look for other information", "practice your presentation", "talk to your parents"],
            "choiceTranslations": ["パートナーと組む", "他の情報を探す", "プレゼンの練習をする", "両親に相談する"],
            "answer": 2,
            "choiceAnalysis": ["パートナーと組む→回答の「図書館で調べる」と繋がらない", "他の情報を探す→正解。💡 回答で図書館やインターネットで調べると言っているので、他の情報源を探すようアドバイスした", "プレゼンの練習をする→情報収集の段階でのアドバイスとしては早すぎる", "両親に相談する→学校の発表の文脈で不自然"],
            "grammar": "💡 look for ～＝～を探す。take a look＝見てみる。anytime＝いつでも"
        }
    ]
}

data["sections"] = [section1, section2]

output_dir = r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade-pre2\2022-2"
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "_part1.json"), "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
print(f"Part 1 saved: {len(section1['questions'])} + {len(section2['questions'])} = {len(section1['questions']) + len(section2['questions'])} questions")

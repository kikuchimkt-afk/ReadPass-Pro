# -*- coding: utf-8 -*-
"""Image-verified original passages; complete bilingual reading units.

Each row: natural translation, main finite verb, English|Japanese chunks.
The rows generate paragraphs, translations and four-field sentencePairs.
"""


def passage(label, title, blocks, **extra):
    paragraphs, translations, pairs = [], [], []
    for block in blocks:
        english, japanese = [], []
        for ja, verb, slash in block:
            en = " ".join(unit.split("|",1)[0] for unit in slash.split("||"))
            pairs.append([en, ja, slash, verb])
            english.append(en)
            japanese.append(ja)
        paragraphs.append(" ".join(english))
        translations.append("".join(japanese))
    return dict(label=label, title=title, paragraphs=paragraphs,
                translations=translations, sentencePairs=pairs, questions=[], **extra)


COOKING = passage("", "Cooking Together", [
    [
        ("ディーンは中学生だったとき、母親と台所で過ごす時間を楽しんでいた。", "enjoyed", "Dean enjoyed spending time|ディーンは時間を過ごすことを楽しんでいた||in the kitchen with his mother|母親と台所で||when he was a junior high school student.|中学生だったとき"),
        ("ほとんど毎晩、母親のそばに立って、一緒に夕食を作った。", "stood", "He stood beside his mother|彼は母親のそばに立った||almost every evening|ほとんど毎晩||as they cooked dinner together.|一緒に夕食を作りながら"),
        ("料理は ( 21 ) だった。", "was", "Cooking was|料理は～だった||( 21 ).|（21）"),
        ("それはまた、ディーンが母親にその日の出来事を話す特別な時間でもあった。", "was", "It was also a special time|それは特別な時間でもあった||for Dean to talk about his day|ディーンがその日の出来事を話す||with his mother.|母親と"),
        ("2人はよく笑い、ただ一緒にいることを楽しんだ。", "laughed", "They laughed a lot|2人はよく笑った||and simply enjoyed being together.|そしてただ一緒にいることを楽しんだ"),
        ("こうした穏やかなひとときは、ディーンの子ども時代の最も幸せな思い出のいくつかになった。", "became", "These quiet moments became|こうした穏やかなひとときはなった||some of Dean's happiest memories|ディーンの最も幸せな思い出のいくつかに||from his childhood.|子ども時代の"),
    ], [
        ("25年後、ディーンは10歳の娘を持つ父親になっていた。", "was", "Twenty-five years later,|25年後||Dean was a father|ディーンは父親になっていた||with a ten-year-old daughter.|10歳の娘を持つ"),
        ("仕事で忙しかったので、望むほど多くの時間を家で過ごすことができなかった。", "could not spend", "Because he was busy with work,|仕事で忙しかったので||he could not spend as much time at home|彼は家でそれほど多くの時間を過ごせなかった||as he wanted.|彼が望むほどには"),
        ("ある日、彼は母親と台所で過ごした子どもの頃の日々をふと思い出した。", "remembered", "One day, he suddenly remembered|ある日、彼はふと思い出した||his childhood days in the kitchen|台所で過ごした子どもの頃の日々を||with his mother.|母親と"),
        ("それは ( 22 )。", "", "That|それは||( 22 ).|（22）"),
        ("それ以来、仕事で忙しくても、できるときはいつでも娘と夕食を作ろうと努めている。", "has been trying", "Since then, he has been trying|それ以来、彼は努めている||to cook dinner with his daughter|娘と夕食を作るように||whenever possible,|できるときはいつでも||even if he is busy with work.|仕事で忙しくても"),
        ("今では、台所にいることが2人の特別な時間になっている。", "has become", "Now, being in the kitchen|今では、台所にいることが||has become their special time together.|2人の特別な時間になっている"),
    ],
])

EMAIL = passage("A", "English play event", [
    [
        ("スティーブンへ。", "", "Dear Steven,|スティーブンへ"),
        ("大学のイベントクラブの伊藤愛子です。", "is", "This is Aiko Ito|伊藤愛子です||from the university's Event Club.|大学のイベントクラブの"),
        ("お約束したとおり、私たちの大学でのイベントについて詳細をお伝えします。", "'m sharing", "As I promised,|お約束したとおり||I'm sharing details|詳細をお伝えします||about the event at our university.|私たちの大学でのイベントについて"),
        ("来月、カナダの提携大学から学生の演劇チームが、日本にある私たちのキャンパスを訪れます。", "will visit", "Next month, a student theater team|来月、学生の演劇チームが||from our partner university in Canada|カナダの提携大学から||will visit our campus in Japan.|日本にある私たちのキャンパスを訪れます"),
        ("私たちに英語で劇を上演してくれますが、それは英語の学習に関心のある多くの学生にとって貴重な経験となるでしょう。", "will perform", "They will perform a play in English for us,|私たちに英語で劇を上演してくれます||which will be a valuable experience|それは貴重な経験となるでしょう||for many students|多くの学生にとって||who are interested in learning English.|英語の学習に関心のある"),
    ], [
        ("劇は7月25日土曜日、キャンパス内の大ホールで1回上演されます。", "will be performed", "The play will be performed once|劇は1回上演されます||on Saturday, July 25,|7月25日土曜日に||in the main hall on campus.|キャンパス内の大ホールで"),
        ("午後6時に始まり、約2時間続きます。", "will start", "It will start at 6 p.m.|午後6時に始まります||and last about two hours.|そして約2時間続きます"),
        ("私たちの大学の全ての学生と教員には無料のイベントですが、学外からの来場者は少額の料金を払う必要があります。", "is", "This is a free event|これは無料のイベントです||for all students and teachers of our university,|私たちの大学の全ての学生と教員にとって||while visitors from outside the university|一方、学外からの来場者は||will need to pay a small fee.|少額の料金を払う必要があります"),
        ("劇の後には、俳優とイベントクラブのメンバーが会って話せる、和やかな夕食会があります。", "will be", "After the play,|劇の後には||there will be a friendly dinner party|和やかな夕食会があります||where the actors and Event Club members|俳優とイベントクラブのメンバーが||can meet and talk.|会って話せる"),
    ], [
        ("また、あなたにお手伝いをお願いしたいと思っています。", "would also like", "I would also like|また、私は～したいと思っています||to ask for your help.|あなたにお手伝いをお願いすることを"),
        ("私たちのイベントクラブは、イベントを支え、円滑に進行させるボランティアを探しています。", "is looking", "Our Event Club is looking for volunteers|私たちのイベントクラブはボランティアを探しています||to support the event|イベントを支える||and make it run smoothly.|そしてそれを円滑に進行させる"),
        ("アメリカからの交換留学生として、言語面での支援を手伝っていただけます。", "can help", "As an exchange student from the United States,|アメリカからの交換留学生として||you can help us|あなたは私たちを手伝えます||with language support.|言語面での支援で"),
        ("言い換えると、訪問するチームと私たちのスタッフの間のコミュニケーションを手伝うことが、あなたの仕事に含まれます。", "will include", "In other words,|言い換えると||your tasks will include helping|あなたの仕事には手伝うことが含まれます||with communication|コミュニケーションの||between the visiting team and our staff.|訪問するチームと私たちのスタッフの間の"),
        ("ボランティアも夕食会に招待されます。", "are also invited", "Volunteers are also invited|ボランティアも招待されます||to the dinner party.|夕食会に"),
        ("関心があれば、6月30日までに知らせてください。", "let", "If you are interested,|関心があれば||please let me know|私に知らせてください||by June 30.|6月30日までに"),
    ], [
        ("よろしくお願いします。", "", "Thank you,|よろしくお願いします"),
        ("伊藤愛子", "", "Aiko Ito|伊藤愛子"),
    ],
], format="email", meta={"from":"Aiko Ito <aiko.ito-1206@letter-wings.com>",
                        "to":"Steven Clark <s.c-0528@bluelines-mail.com>",
                        "date":"June 15", "subject":"English play event"})
# Preserve the greeting/signature line breaks, without changing sentence coverage.
EMAIL["paragraphs"][0] = EMAIL["paragraphs"][0].replace("Dear Steven, ", "Dear Steven,\n", 1)
EMAIL["paragraphs"][-1] = "Thank you,\nAiko Ito"
EMAIL["translations"][0] = EMAIL["translations"][0].replace("スティーブンへ。", "スティーブンへ。\n", 1)
EMAIL["translations"][-1] = "よろしくお願いします。\n伊藤愛子"

HANDWASHING = passage("B", "Handwashing", [
    [
        ("今日の人々は、手洗いが健康にとって重要であると知っている。", "know", "People today know|今日の人々は知っている||that handwashing is important|手洗いが重要であると||for their health.|健康にとって"),
        ("しかし、約150年前には一般的な習慣ではなかった。", "was", "However, it was not a common habit|しかし、それは一般的な習慣ではなかった||about 150 years ago.|約150年前には"),
        ("当時、多くの医師は手洗いの重要性を理解していなかった。", "did not understand", "Back then, many doctors|当時、多くの医師は||did not understand the importance of handwashing.|手洗いの重要性を理解していなかった"),
        ("ハンガリー出身のイグナーツ・ゼンメルワイスという医師が、医療従事者にとっての手洗いの重要性を最初に認識した人だった。", "was", "A doctor from Hungary named Ignaz Semmelweis|イグナーツ・ゼンメルワイスというハンガリー出身の医師は||was the first person|最初の人だった||to recognize its importance for medical workers.|医療従事者にとってのその重要性を認識した"),
        ("多くの医師が細菌についてよく知らなかった一方で、ゼンメルワイスは19世紀半ばに、手を洗うことで人々が病気を広めるのを防げると発見した。", "discovered", "While many doctors did not know much about bacteria,|多くの医師が細菌についてよく知らなかった一方で||Semmelweis discovered|ゼンメルワイスは発見した||in the middle of the nineteenth century|19世紀半ばに||that washing hands could prevent people|手を洗うことが人々を防げると||from spreading disease.|病気を広めることから"),
    ], [
        ("彼はある重要なことに気づいた後、その考えに至った。", "got", "He got the idea|彼はその考えに至った||after noticing something important.|ある重要なことに気づいた後"),
        ("当時、多くの女性が出産後にある病気で亡くなった。", "died", "At that time, many women died|当時、多くの女性が亡くなった||from a disease|ある病気で||after giving birth.|出産後に"),
        ("これは、出産を助ける専門家である助産師が運営する診療所よりも、医師が運営する病院ではるかに頻繁に起きた。", "happened", "This happened much more often|これははるかに頻繁に起きた||in hospitals run by doctors|医師が運営する病院で||than in clinics run by midwives,|助産師が運営する診療所よりも||professionals who helped with giving birth.|出産を助ける専門家である"),
        ("ゼンメルワイスはまた、一部の病院の医師が、遺体の検査からそのまま女性の出産の手助けに移っていることにも気づいた。", "noticed", "Semmelweis also noticed|ゼンメルワイスはまた気づいた||that some hospital doctors were going straight|一部の病院の医師がそのまま移っていると||from examining dead bodies|遺体を検査することから||to helping women give birth.|女性の出産を手助けすることへ"),
        ("このことから、医師は気づかないまま母親たちに有害なものを運んでいるのではないかと彼は考えた。", "made", "This made him think|このことは彼に考えさせた||that doctors might be carrying something harmful|医師が有害なものを運んでいるかもしれないと||to the mothers|母親たちのところへ||without realizing it.|それに気づかずに"),
    ], [
        ("病気を防ぐための彼の方法は、石けんによる普通の手洗いとは異なっていた。", "was", "His method to prevent the disease|病気を防ぐための彼の方法は||was different from regular handwashing|普通の手洗いとは異なっていた||with soap.|石けんによる"),
        ("医師は特別な液体を使って、注意深く手を洗う必要があった。", "needed", "Doctors needed to clean their hands carefully|医師は注意深く手を洗う必要があった||using a special liquid.|特別な液体を使って"),
        ("他の医師がこれに従うようになると、母親たちの死亡率は約18パーセントから約2パーセントに下がった。", "dropped", "After other doctors began to follow this,|他の医師がこれに従うようになると||the death rate of the mothers dropped|母親たちの死亡率は下がった||from about 18 percent to about 2 percent.|約18パーセントから約2パーセントに"),
        ("さらに、医療器具も洗浄すると、死亡率は約1パーセントに下がった。", "went down", "In addition,|さらに||when medical tools were cleaned,|医療器具も洗浄すると||the rate went down to about 1 percent.|死亡率は約1パーセントに下がった"),
        ("このように、彼は病院での医師の働き方を変える発見をした。", "made", "In this way, he made a discovery|このように、彼は発見をした||that changed how doctors worked in hospitals.|病院での医師の働き方を変える"),
    ], [
        ("ゼンメルワイスは重要な発見をしたにもかかわらず、当時の多くの医師は彼を信じなかった。", "did not believe", "Even though Semmelweis made an important discovery,|ゼンメルワイスは重要な発見をしたにもかかわらず||many doctors at that time did not believe him.|当時の多くの医師は彼を信じなかった"),
        ("自分たちの行動が母親たちを死なせているという考えを、医師たちは受け入れたがらなかった。", "did not want", "They did not want to accept the idea|彼らはその考えを受け入れたがらなかった||that their actions were causing mothers to die.|自分たちの行動が母親たちを死なせているという"),
        ("残念ながら、人々がその発見の価値を真に理解する前に、ゼンメルワイスは亡くなった。", "passed away", "Sadly, Semmelweis passed away|残念ながら、ゼンメルワイスは亡くなった||before people truly understood|人々が真に理解する前に||the value of his discovery.|彼の発見の価値を"),
        ("後に、彼の研究は、他の科学者が細菌についてさらに学ぶ助けとなった。", "helped", "Later, his work helped other scientists|後に、彼の研究は他の科学者を助けた||learn more about bacteria.|細菌についてさらに学ぶように"),
        ("時がたつにつれて、人々は手洗いの重要性を理解した。", "understood", "Over time, people understood|時がたつにつれて、人々は理解した||the importance of handwashing.|手洗いの重要性を"),
        ("最終的には、20世紀初めまでに、医師にも一般の人々にも手洗いが普通のことになった。", "became", "Eventually, by the early twentieth century,|最終的には、20世紀初めまでに||it became common|それは普通のことになった||for both doctors and ordinary people.|医師にも一般の人々にも"),
    ],
])


def question(n, stem, ja, choices, translations, answer, reasons, grammar, evidence):
    return dict(number=n, question=stem, questionTranslation=ja, choices=choices,
                choiceTranslations=translations, answer=answer,
                choiceAnalysis=[f"{t}→{r}" for t,r in zip(translations,reasons)],
                grammar=grammar, sourceEvidence=evidence)


COOKING["questions"] = [
    question(21, "( 21 )", "空所 ( 21 ) に入る内容を選びなさい。",
             ["something done without talking", "only about enjoying delicious food", "more than just preparing meals", "a task given by his mother"],
             ["話をせずにすること", "おいしい食べ物を楽しむことだけ", "単に食事を用意する以上のこと", "母親から与えられた仕事"], 3,
             ["母親とその日の出来事を話した、とあるので、会話をしないという内容に反する。", "食事だけでなく、話して笑い、一緒にいることを楽しんでいた。", "正解。💡a special time ... to talk about his day と enjoyed being together が、料理以外の価値を示す。", "母親に命じられたとは書かれておらず、楽しい共有の時間を述べている。"],
             "💡more than just ... は「単に～だけではない」。空所の直後の also に注目し、夕食作りに加えて会話や一緒に過ごす時間にも意味があった、とまとめる。",
             [COOKING["sentencePairs"][3][0], COOKING["sentencePairs"][4][0]]),
    question(22, "( 22 )", "空所 ( 22 ) に入る内容を選びなさい。",
             ["reminded him of something important", "made him feel nervous about cooking", "kept him away from the kitchen", "encouraged him to quit his job"],
             ["彼に大切なことを思い出させた", "彼を料理について不安にさせた", "彼を台所から遠ざけた", "彼に仕事を辞めるよう勧めた"], 1,
             ["正解。💡remembered his childhood days と cook dinner with his daughter が、親子の時間の大切さを思い出したことを示す。", "料理への不安はなく、その後は娘と料理をしようと努めている。", "台所から離れるのではなく、娘と台所で過ごすようになっている。", "even if he is busy with work とあり、仕事を続けながら時間を作っている。"],
             "💡remind A of B は「AにBを思い出させる」。That は直前の子ども時代の記憶を受ける。Since then の後にある行動の変化から、何を思い出したのか判断する。",
             [COOKING["sentencePairs"][8][0], COOKING["sentencePairs"][10][0]]),
]

EMAIL["questions"] = [
    question(23, "What will happen next month?", "来月、何が起こりますか。",
             ["University students from Canada will perform a play in Japan.", "An English movie event will be held by the Event Club.", "Aiko Ito and her theater team will give a performance.", "The theater team from Aiko's university will visit Canada."],
             ["カナダの大学生が日本で劇を上演する。", "イベントクラブが英語の映画イベントを開催する。", "伊藤愛子とその演劇チームが公演する。", "愛子の大学の演劇チームがカナダを訪れる。"], 1,
             ["正解。💡a student theater team ... in Canada will visit our campus in Japan と perform a play が一致する。", "上演するのは play（劇）で、movie（映画）ではない。", "演じるのはカナダの提携大学のチームで、愛子のチームではない。", "カナダから日本へ来るので、訪問の方向が逆。"],
             "💡What will happen? は予定される出来事を問う。Next month を目印に第1段落を確認し、from Canada と in Japan で、誰がどこで上演するのか整理する。",
             [EMAIL["sentencePairs"][3][0], EMAIL["sentencePairs"][4][0]]),
    question(24, "What is true about the event?", "イベントについて正しいことは何ですか。",
             ["It will have two performances on July 25.", "There will be a ceremony before the play.", "It will be held in a hall at the university.", "There will not be any fee for people attending the show."],
             ["7月25日に2回公演する。", "劇の前に式典がある。", "大学のホールで開催される。", "公演に来る人には誰にも料金がかからない。"], 3,
             ["performed once とあるので、公演は2回ではなく1回。", "劇の後の dinner party はあるが、劇の前の式典は述べていない。", "正解。💡in the main hall on campus が、大学内のホールでの開催を示す。", "学内の学生・教員は無料だが、学外の来場者は small fee を払う。"],
             "💡内容一致では回数・前後・場所・料金の対象を一つずつ照合する。once は1回、After は後、on campus は学内。無料なのは全来場者ではなく学内の学生と教員に限られる。",
             [EMAIL["sentencePairs"][5][0]]),
    question(25, "Aiko asks Steven Clark to", "愛子はスティーブン・クラークに、何をするよう頼んでいますか。",
             ["serve as a leader of the volunteer members.", "help connect the staff and the theater team.", "support her team in planning a dinner event.", "start helping her event team on June 30."],
             ["ボランティアのリーダーを務める。", "スタッフと演劇チームの橋渡しを手伝う。", "夕食会の計画で彼女のチームを支える。", "6月30日にイベントチームの手伝いを始める。"], 2,
             ["役割は言語面の支援で、リーダーを任せるとは書かれていない。", "正解。💡helping with communication between the visiting team and our staff が橋渡しの仕事を示す。", "夕食会に招かれるが、その計画をする役割ではない。", "by June 30 は関心があるか連絡する締切で、活動の開始日ではない。"],
             "💡help connect は「つながりを助ける」で、helping with communication の言い換え。In other words の後に依頼内容の具体化がある。by＋日付は「その日までに」で開始日とは区別する。",
             [EMAIL["sentencePairs"][12][0]]),
]

HANDWASHING["questions"] = [
    question(26, "What was true about the situation around 150 years ago?", "約150年前の状況について正しいことは何ですか。",
             ["Handwashing was a common custom followed by doctors.", "Bacteria were not well understood by most doctors.", "Ignaz Semmelweis spread the risk of bacteria to humans.", "Doctors did not shake hands to prevent serious diseases."],
             ["手洗いは医師たちが行う一般的な習慣だった。", "ほとんどの医師は細菌をよく理解していなかった。", "イグナーツ・ゼンメルワイスは細菌の危険を人間に広めた。", "医師たちは深刻な病気を防ぐため握手をしなかった。"], 2,
             ["not a common habit とあり、当時は一般的ではなかった。", "正解。💡many doctors did not know much about bacteria が、細菌の理解が乏しかったことを示す。", "彼は病気の拡散を防ぐ方法を発見した人で、危険を広めたとはない。", "手洗いの話であり、握手を控えたという記述はない。"],
             "💡around 150 years ago は第1段落の about 150 years ago を探す目印。not well understood は did not know much の言い換え。今日の常識と当時の状況を混同しない。",
             [HANDWASHING["sentencePairs"][4][0]]),
    question(27, "One of the things Semmelweis noticed was that", "ゼンメルワイスが気づいたことの一つは、何ですか。",
             ["women were less safe when giving birth in hospitals run by doctors.", "a disease was spread from mothers to others after giving birth.", "it was rare for mothers to give birth in hospitals at that time.", "many babies delivered by midwives often got sick after birth."],
             ["医師が運営する病院では、女性が出産する際の安全性が低かった。", "出産後、母親から他の人へ病気が広がった。", "当時、母親が病院で出産するのはまれだった。", "助産師が取り上げた多くの赤ちゃんが、出生後によく病気になった。"], 1,
             ["正解。💡This happened much more often in hospitals run by doctors が、母親の死亡が病院で多かったことを示す。", "病気を運んだと疑われたのは医師で、母親から他の人への拡散ではない。", "病院と診療所の死亡の頻度を比べており、病院出産がまれとは書かれていない。", "比較しているのは母親の死亡で、助産師が扱った赤ちゃんの病気ではない。"],
             "💡less safe は死亡が多いという事実の言い換え。This は直前の女性が出産後に亡くなることを受ける。run by doctors は hospitals を後ろから説明する過去分詞句。",
             [HANDWASHING["sentencePairs"][6][0], HANDWASHING["sentencePairs"][7][0]]),
    question(28, "What happened after other doctors started to use Semmelweis's method?", "他の医師がゼンメルワイスの方法を使い始めた後、何が起こりましたか。",
             ["Doctors stopped helping mothers give birth at hospitals.", "Hospitals began to use only new medical tools regularly.", "The number of babies born in the hospital dropped greatly.", "The death rate of mothers became much lower than before."],
             ["医師たちは病院で母親の出産を手助けするのをやめた。", "病院は定期的に、新しい医療器具だけを使うようになった。", "病院で生まれる赤ちゃんの数が大きく減った。", "母親の死亡率が以前よりずっと低くなった。"], 4,
             ["出産の手助けをやめたのではなく、手を洗う方法を変えた。", "器具を洗浄したとあり、新しい器具だけに交換したとはない。", "減ったのは母親の死亡率で、出生数ではない。", "正解。💡the death rate ... dropped from about 18 percent to about 2 percent が大幅な低下を示す。"],
             "💡After で始まる第3段落の文が手がかり。from A to B は変化の前後を示す。数値が下がった対象は the death rate of the mothers であり、赤ちゃんの人数ではない。",
             [HANDWASHING["sentencePairs"][12][0]]),
    question(29, "What happened after Semmelweis's discovery?", "ゼンメルワイスの発見の後、何が起こりましたか。",
             ["His idea was proved to be completely wrong shortly after he died.", "The public began to wash their hands before doctors did regularly.", "Many doctors denied his great discovery while he was still alive.", "Many scientists started learning about bacteria soon after the discovery."],
             ["彼の死後まもなく、その考えは完全に間違いだと証明された。", "一般の人々が、医師より先に習慣的な手洗いを始めた。", "彼が生きている間、多くの医師がその偉大な発見を否定した。", "発見の直後、多くの科学者が細菌について学び始めた。"], 3,
             ["後に価値が理解され、細菌研究の助けとなったので、間違いと証明されたわけではない。", "医師と一般の人々の両方に普及したとあるが、一般の人々が先とはない。", "正解。💡many doctors ... did not believe him が否定を示す。価値の理解は彼の死後だった。", "Later とはあるが soon after the discovery という直後の時期は述べていない。"],
             "💡while he was still alive は「彼がまだ生きている間」。did not believe が denied の根拠。before people truly understood と Later を手がかりに、生前の反応と後年の評価を分ける。",
             [HANDWASHING["sentencePairs"][15][0], HANDWASHING["sentencePairs"][17][0]]),
]

PASSAGES = [COOKING, EMAIL, HANDWASHING]

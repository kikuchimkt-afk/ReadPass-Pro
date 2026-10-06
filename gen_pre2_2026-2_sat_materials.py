# -*- coding: utf-8 -*-
"""40 source-balanced vocabulary items and five original-based lesson cards."""
import re

# word, meaning, pos, new example, three distractors, literal source form.
# Part 1:17, Part 2:6, Part 3:6, Part 4:11.
WORDS = [
    ("besides", "そのうえ", "副詞", "The room is bright. Besides, it is close to the station.", "しかし／その代わりに／かなり", "Besides"),
    ("outdoor", "屋外の", "形容詞", "We enjoyed an outdoor concert in the park.", "屋内の／毎日の／頻繁な", "outdoor"),
    ("anniversary", "記念日", "名詞", "They celebrated their tenth wedding anniversary.", "交響曲／謎／流行", "anniversary"),
    ("injury", "けが", "名詞", "He missed the race because of a knee injury.", "画像／品目／勇気", "injury"),
    ("steam", "蒸気", "名詞", "Steam rose from the hot soup.", "棚／勇気／恐慌", "steam"),
    ("manage", "経営する", "動詞", "Her uncle manages a small bakery.", "保存する／発見する／気分を害する", "manages"),
    ("remain", "～のままである", "動詞", "Please remain quiet during the announcement.", "通過する／費やす／意味する", "remain"),
    ("imagine", "想像する", "動詞", "Can you imagine living on an island?", "受け取る／発表する／聞く", "imagine"),
    ("deal", "お買い得品・有利な取引", "名詞", "We found a good deal on a used bicycle.", "脳／英雄／記録", "deal"),
    ("introduction", "導入・序論", "名詞", "The introduction explains the purpose of the report.", "翻訳／収集／観察", "introduction"),
    ("hold on", "待つ", "熟語", "Hold on a moment while I check the address.", "参加する／立ち寄る／設置する", "Hold on"),
    ("poor at", "～が苦手な", "熟語", "I am poor at drawing, but I enjoy it.", "～に気づいている／～をうらやむ／～に腹を立てている", "poor at"),
    ("short of", "～が不足している", "熟語", "We were short of time before the meeting.", "～によくない／～に腹を立てている／～に気づいている", "short of"),
    ("in case of", "～の場合に", "熟語", "In case of snow, the buses may be delayed.", "～を経由して／現在は／確かに", "in case"),
    ("write down", "書き留める", "熟語", "Write down the new words in your notebook.", "捨てる／跳び上がる／落ち着く", "write down"),
    ("throughout", "～の間ずっと", "前置詞", "The wind was strong throughout the night.", "～の前に／～にもかかわらず／～の外で", "throughout"),
    ("flour", "小麦粉", "名詞", "Mix the flour with water in a bowl.", "砂糖／蒸気／塩", "flour"),
    ("wrap", "包む", "動詞", "Please wrap the book in blue paper.", "捨てる／外す／借りる", "wrap"),
    ("discount", "割引", "名詞", "Students can get a discount on train tickets.", "追加料金／贈り物／注文", "discount"),
    ("feel free to", "遠慮なく～する", "熟語", "Feel free to ask questions after the lesson.", "～するのを避ける／～しなければならない／～するのを忘れる", "feel free to"),
    ("instead of", "～の代わりに", "熟語", "We walked instead of taking a bus.", "～のために／～と一緒に／～に加えて", "instead of"),
    ("get along with", "～とうまく付き合う", "熟語", "She gets along with her new classmates.", "～を非難する／～を追い越す／～から逃げる", "get along with"),
    ("employee", "従業員", "名詞", "Every employee received a name badge.", "著者／客／雇用主", "employees"),
    ("childhood", "子ども時代", "名詞", "He spent his childhood in a small town.", "職業／老年期／思いつき", "childhood"),
    ("memory", "思い出", "名詞", "The photo brings back a happy memory.", "予定／作業／忠告", "memories"),
    ("remind A of", "Aに～を思い出させる", "熟語", "This song reminds me of my first school.", "Aを～から遠ざける／Aに～を勧める／Aに～を任せる", "reminded him of"),
    ("since then", "それ以来", "熟語", "I moved here in May and have lived here since then.", "それ以前に／その間だけ／その代わりに", "Since then"),
    ("whenever", "～するときはいつでも", "接続詞", "Call me whenever you need help.", "～した後でだけ／～しない限り／～する一方で", "whenever"),
    ("even if", "たとえ～でも", "接続詞", "I will go for a walk even if it is cold.", "～なので／～するために／～するとすぐに", "even if"),
    ("perform", "上演する", "動詞", "Our drama club will perform a short play.", "延期する／招待する／翻訳する", "perform"),
    ("valuable", "貴重な", "形容詞", "The workshop gave us valuable experience.", "ありふれた／有害な／無料の", "valuable"),
    ("volunteer", "ボランティア", "名詞", "A volunteer showed us around the museum.", "来場者／俳優／教員", "volunteers"),
    ("communication", "意思疎通・コミュニケーション", "名詞", "Clear communication helps a team work well.", "競争／料金／発見", "communication"),
    ("recognize", "認識する", "動詞", "We should recognize the value of daily practice.", "否定する／広める／防ぐ", "recognize"),
    ("bacteria", "細菌", "名詞", "Some bacteria live in the soil.", "石けん／液体／器具", "bacteria"),
    ("prevent A from", "Aが～するのを防ぐ", "熟語", "The fence prevents children from entering the road.", "Aに～を勧める／Aが～するのを助ける／Aに～を思い出させる", "prevent people from"),
    ("give birth", "出産する", "熟語", "The animal gave birth to two babies.", "病気になる／亡くなる／手を洗う", "giving birth"),
    ("harmful", "有害な", "形容詞", "Some chemicals are harmful to plants.", "有益な／普通の／貴重な", "harmful"),
    ("death rate", "死亡率", "名詞", "The report compares the death rate in two regions.", "出生数／人口／体温", "death rate"),
    ("pass away", "亡くなる", "熟語", "The writer passed away at the age of ninety.", "出産する／気づく／受け入れる", "passed away"),
]


def vocabulary():
    result = []
    for n, (word, meaning, pos, example, distractors, form) in enumerate(WORDS, 1):
        slug = re.sub(r"[^a-z0-9]+", "_", word.lower()).strip("_")
        result.append(dict(word=word, meaning=meaning, pos=pos, level="準2級",
                           source="大問1" if n<=17 else "大問2" if n<=23 else "大問3" if n<=29 else "大問4",
                           sourceForm=form, example=example, distractors=distractors.split("／"),
                           wordAudio=f"audio/vocab/w_{n:03d}_{slug}.mp3",
                           exampleAudio=f"audio/vocab/ex_{n:03d}_{slug}.mp3"))
    return result


def example(en, ja, note):
    return dict(en=en, ja=ja, note=note)


def lessonplan(passages):
    cooking, email, hand = passages
    def quote(p, n, note):
        en, ja = p["sentencePairs"][n][:2]
        return example(en, ja, note)
    def practice(p, index, n):
        en, ja = p["paragraphs"][index], p["translations"][index]
        for q in p["questions"]:
            en = en.replace(f"( {q['number']} )", q["choices"][q["answer"]-1])
        if p is cooking and index == 1:
            ja = ja.replace("それは ( 22 )。", "それは彼に大切なことを思い出させた。")
        return dict(en=f"[出典: {p['title']} 第{index+1}段落]\n{en}", ja=ja,
                    audioFile=f"audio/practice_pp{n}.mp3")
    fps = [
        dict(id="fp1", title="量の比較と条件の省略（as much time as / whenever possible）",
             subtitle="Quantity Comparisons and Reduced Conditions",
             explanation="Cooking Together 第2段落の as much time ... as he wanted は、『彼が望むのと同じくらい多くの時間』です。could not があるため、全体では『望むほど時間を過ごせなかった』となります。time はここでは不可算名詞なので many ではなく much。whenever possible は whenever it is possible の主語・be動詞が省略された形で、『できるときはいつでも』を表します。even if he is busy with work は『仕事で忙しくても』という譲歩の条件。望む時間を確保できなかった父親が、それでもできる限り娘と料理をする、という変化を読み取ります。",
             sourceQuote="as much time at home as he wanted / whenever possible / even if he is busy with work",
             sourceLocation="大問3「Cooking Together」第2段落", highlightLabel="量・条件", highlightColor="#4f8cff",
             examples=[quote(cooking,7,"as much＋不可算名詞＋as。否定の could not により、希望する量に届かないと読む。"),
                       example("I could not read as many books as I wanted.", "私は読みたかったほど多くの本を読めませんでした。", "books は可算名詞なので many。否定文で希望する冊数に届かなかったことを表す。"),
                       example("Please check the answers whenever possible.", "できるときはいつでも答えを確認してください。", "whenever it is possible の it is が省略されている。")],
             practicePassage=practice(cooking,1,1),
             practiceQuestions=[
                 {"q":"as much time ... as he wanted を、could not も含めて訳してください。", "a":"『彼が望むほど多くの時間を家で過ごすことができなかった』。as ... as が量を比べ、could not がその量に届かなかったことを示します。"},
                 {"q":"なぜ as many time ではなく as much time ですか。", "a":"ここで time は回数ではなく時間の長さを表す不可算名詞なので much を使います。回数なら可算の times です。"},
                 {"q":"whenever possible で省略されている部分と、意味を答えてください。", "a":"whenever it is possible の it is が省略されています。意味は『できるときはいつでも』です。"},
                 {"q":"even if he is busy with work は、忙しさを料理の中止理由にしていますか。", "a":"いいえ。『仕事で忙しくても』という譲歩の条件で、忙しさがあっても娘と料理するよう努めることを示します。"}],
             highlightPatterns=["as much time at home as he wanted", "whenever possible", "even if he is busy with work"]),
        dict(id="fp2", title="立場を示すasと、相手・支援内容を分けるhelp A with B",
             subtitle="Roles with as and help A with B",
             explanation="メール第3段落の As an exchange student ... は『交換留学生として』という立場を示し、理由の接続詞 as＋文とは形が異なります。you can help us with language support は、help の目的語 us が支援を受ける相手、with の後の language support が支援内容です。続く In other words は具体的な言い換えを導き、訪問チームとスタッフの意思疎通を助ける仕事だと分かります。make it run smoothly の it は event。最後の by June 30 は返事の締切を表すので、手伝いを始める日と混同しないようにします。",
             sourceQuote="As an exchange student from the United States, you can help us with language support. / by June 30",
             sourceLocation="大問4A「English play event」第3段落", highlightLabel="立場・支援・締切", highlightColor="#34d399",
             examples=[quote(email,11,"As＋名詞は立場。help us with ... で、誰を、何で助けるのかを分ける。"),
                       example("As a team leader, I help new members with their tasks.", "チームリーダーとして、私は新しいメンバーの仕事を手伝います。", "立場は team leader、支援相手は new members、支援内容は their tasks。"),
                       example("Please let me know by Friday.", "金曜日までに知らせてください。", "by は期限。Friday に開始するという意味ではない。")],
             practicePassage=practice(email,2,2),
             practiceQuestions=[
                 {"q":"As an exchange student の as は、どのような意味ですか。", "a":"『交換留学生として』という立場です。後ろが名詞句なので、as＋主語＋動詞の『～なので』とは形が異なります。"},
                 {"q":"help us with language support の支援相手と支援内容を分けてください。", "a":"支援相手は us（イベントクラブ側）、支援内容は language support（言語面での支援）です。"},
                 {"q":"In other words の後は、language support をどう具体化していますか。", "a":"訪問する演劇チームと大学側スタッフの間のコミュニケーションを手伝う仕事だと説明しています。"},
                 {"q":"by June 30 は、活動開始日と連絡の締切のどちらですか。", "a":"関心があることを伝える連絡の締切です。『6月30日までに知らせてください』で、開始日ではありません。"}],
             highlightPatterns=["As an exchange student from the United States", "help us with language support", "In other words", "by June 30"]),
        dict(id="fp3", title="something＋形容詞と、行動の前後をつなぐfrom -ing to -ing",
             subtitle="Postmodifying something and Sequences of Actions",
             explanation="Handwashing 第2段落の something important、something harmful は、something のような不定代名詞を形容詞が後ろから説明する形です。『重要なこと』『有害なもの』と、名詞に相当する部分から読みます。また、from examining dead bodies to helping women give birth は、from と to の後ろに動名詞を置いて、医師の行動がどこからどこへ移ったかを示します。ここでの to は前置詞なので helping です。without realizing it も前置詞＋動名詞で『気づかずに』。医師が無自覚に有害なものを運んだのでは、という疑いにつながります。",
             sourceQuote="something important / from examining dead bodies to helping women give birth / something harmful / without realizing it",
             sourceLocation="大問4B「Handwashing」第2段落", highlightLabel="不定代名詞・行動の順序", highlightColor="#f472b6",
             examples=[quote(hand,8,"from と to が二つの行動をつなぐ。to の後ろは helping で、不定詞ではない。"),
                       example("I learned something useful from the class.", "授業で役に立つことを学びました。", "useful が something を後ろから修飾する。useful something とはしない。"),
                       example("She went from reading the instructions to trying the game.", "彼女は説明を読むことから、ゲームを試すことへ移りました。", "from V-ing to V-ing で行動の移行を示す。")],
             practicePassage=practice(hand,1,3),
             practiceQuestions=[
                 {"q":"something important と something harmful では、形容詞はどこに置かれていますか。", "a":"どちらも something の後ろです。『重要なこと』『有害なもの』と、不定代名詞を後ろから説明しています。"},
                 {"q":"医師は何をすることから、何をすることへ移っていましたか。", "a":"遺体を検査することから、そのまま女性の出産を手助けすることへ移っていました。from と to の後ろを対応させて読みます。"},
                 {"q":"to helping の helping は、なぜ動名詞ですか。", "a":"この to は from ... to ... の前置詞だからです。行動を名詞の形で表すため V-ing を置き、不定詞の to help とは区別します。"},
                 {"q":"without realizing it は、医師のどのような状態を表しますか。", "a":"母親に有害なものを運んでいることに気づいていない状態です。without＋動名詞で『～することなしに』を表します。"}],
             highlightPatterns=["something important", "from examining dead bodies to helping women give birth", "something harmful", "without realizing it"]),
        dict(id="fp4", title="考えの内容を説明するthat節とcause A to V",
             subtitle="Content Clauses after idea and cause A to V",
             explanation="Handwashing 第4段落の the idea that ... では、that 節が idea の内容を説明します。『自分たちの行動が母親たちを死なせているという考え』と読み、idea に何かを行う関係代名詞の節とは区別します。cause A to V は『Aが～する原因となる』で、causing mothers to die の mothers は die する人です。many doctors did not believe him と did not want to accept the idea を結ぶと、発見の内容を認めたがらなかったことが分かります。before と Later を目印に、生前の否定と後年の理解を読み分けます。",
             sourceQuote="the idea that their actions were causing mothers to die / before people truly understood / Later, his work helped other scientists",
             sourceLocation="大問4B「Handwashing」第4段落", highlightLabel="考えの内容・原因", highlightColor="#fbbf24",
             examples=[quote(hand,16,"that 節は idea の内容。cause＋mothers＋to die で、何が誰に何を起こすのかを読む。"),
                       example("We discussed the idea that everyone should have a role.", "全員が役割を持つべきだという考えについて話し合いました。", "that 以下は完全な文で、idea の具体的な内容を説明する。"),
                       example("The heavy rain caused the river to rise.", "大雨で川の水位が上がりました。", "cause A to V。原因は rain、上昇するものは river。")],
             practicePassage=practice(hand,3,4),
             practiceQuestions=[
                 {"q":"the idea の具体的な内容を述べているのは、どの部分ですか。", "a":"that their actions were causing mothers to die の部分です。『自分たちの行動が母親たちを死なせている』という考えを説明しています。"},
                 {"q":"causing mothers to die の原因・対象・結果を分けてください。", "a":"原因は医師たちの行動、対象は母親たち、結果は亡くなることです。cause A to V の A が to V の動作をする人になります。"},
                 {"q":"before people truly understood は、どの出来事より理解が遅れたことを示しますか。", "a":"ゼンメルワイスが亡くなることより、発見の価値の理解が遅れたことです。彼は真に理解される前に亡くなりました。"},
                 {"q":"Later 以降は、生前の評価とどう異なりますか。", "a":"生前は多くの医師が信じなかった一方、後には研究が細菌の理解を助け、手洗いの重要性が広く理解されるようになりました。"}],
             highlightPatterns=["the idea that their actions were causing mothers to die", "before people truly understood", "Later, his work helped other scientists"]),
        dict(id="fp5", title="今回の重要なパラフレーズ", subtitle="Key Paraphrases in This Exam",
             explanation="内容一致問題では、本文の単語をそのまま探すだけでなく、同じ事実を別の形で表した選択肢を見分けます。Q28の became much lower than before は、第3段落の dropped from about 18 percent to about 2 percent の言い換えです。低下したのは母親の死亡率で、赤ちゃんの出生数ではありません。Q27の less safe は母親の死亡が多かったこと、Q25の help connect は意思疎通を手伝うことをまとめています。数値・対象・時期を保った言い換えかを確かめると、似た語を使った不正解を除けます。",
             sourceQuote="the death rate of the mothers dropped from about 18 percent to about 2 percent / the rate went down to about 1 percent",
             sourceLocation="大問4B「Handwashing」第3段落（Q28）／大問4A Q25・大問4B Q27",
             highlightLabel="パラフレーズの根拠", highlightColor="#f59e0b",
             examples=[quote(hand,12,"dropped from 18 percent to 2 percent → became much lower than before。対象は母親の死亡率。"),
                       example("Helping with communication can connect two teams.", "意思疎通を手伝うことは、2つのチームの橋渡しになります。", "Q25の helping with communication → help connect。役割が同じかを確認する。"),
                       example("A place where more mothers die is less safe for them.", "亡くなる母親が多い場所は、母親たちにとって安全性が低い場所です。", "Q27の死亡が多い → less safe。母親から赤ちゃんへ対象を変えない。")],
             practicePassage=practice(hand,2,5),
             practiceQuestions=[
                 {"q":"dropped from about 18 percent to about 2 percent を、数値を使わず言い換えてください。", "a":"『以前よりずっと低くなった』。Q28の became much lower than before と同じ変化を表します。"},
                 {"q":"低下した数値は、赤ちゃんの数ですか、母親の死亡率ですか。", "a":"母親の死亡率です。the death rate of the mothers が主語で、出生数についての記述ではありません。"},
                 {"q":"medical tools were cleaned を『新しい器具に交換した』と言い換えてよいですか。", "a":"いいえ。cleaned は洗浄したという行為で、器具を新品に交換したとは述べていません。行為の内容が変わっています。"},
                 {"q":"約2パーセントから約1パーセントへ下がったのは、何をしたときですか。", "a":"医療器具も洗浄したときです。when medical tools were cleaned と the rate went down を対応させて読みます。"}],
             highlightPatterns=["the death rate of the mothers dropped from about 18 percent to about 2 percent", "when medical tools were cleaned", "the rate went down to about 1 percent"]),
    ]
    return dict(title="2026年度 第2回（土曜準会場）準2級 授業のポイント", focusPoints=fps)

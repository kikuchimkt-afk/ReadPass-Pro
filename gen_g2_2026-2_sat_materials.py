# -*- coding: utf-8 -*-
"""Balanced vocabulary and the established five-focus-point lesson format."""
import re

# 25 items from Part 1, 15 from Part 2, 15 from Part 3.
# Each example is new, rather than an extracted test-booklet sentence.
WORDS = [
    ("irony", "皮肉・意外な巡り合わせ", "名詞", "The irony is that the swimming coach cannot swim.", "印象／冒険／選択肢"),
    ("architecture", "建築学", "名詞", "She studied architecture before designing a school.", "家具／地理学／工芸"),
    ("consult", "相談する", "動詞", "You should consult a specialist before starting the project.", "禁止する／まねる／困らせる"),
    ("clay", "粘土", "名詞", "The children made small animals out of clay.", "砂／金属／絵の具"),
    ("strengthen", "強化する", "動詞", "Daily exercise can strengthen your muscles.", "回復する／中断する／集める"),
    ("thoroughly", "十分に・徹底的に", "副詞", "Please wash your hands thoroughly before cooking.", "さわやかに／以前は／単に"),
    ("calculate", "計算する", "動詞", "We calculated the cost of buying new computers.", "遭遇する／代表する／影響する"),
    ("naked", "裸の", "形容詞", "The baby was naked before her bath.", "明らかな／適切な／集中的な"),
    ("exception", "例外", "名詞", "There is one exception to this rule.", "要件／罰／集中"),
    ("pretend", "ふりをする", "動詞", "The child pretended to be a famous singer.", "発見する／見積もる／疑問に思う"),
    ("stick to", "続ける・守る", "熟語", "I will stick to my study plan this month.", "偶然出会う／見上げる／立ち去る"),
    ("cross out", "線を引いて消す", "熟語", "Cross out the incorrect word with a single line.", "電源を切る／倒す／引き離す"),
    ("in progress", "進行中で", "熟語", "The road repairs are still in progress.", "無作為に／平穏で／万一に備えて"),
    ("give in", "折れる・譲歩する", "熟語", "She refused to give in to pressure.", "離陸する／育てる／近づく"),
    ("break off", "打ち切る", "熟語", "They decided to break off the negotiations.", "取り上げる／失望させる／だまされる"),
    ("no matter", "～にかかわらず", "熟語", "No matter how busy he is, he reads every day.", "～に基づいて／～次第で／～の代わりに"),
    ("in general", "一般に", "熟語", "In general, these plants need plenty of sunlight.", "対照的に／詳しく／要するに"),
    ("impression", "印象", "名詞", "The polite receptionist made a good impression.", "冒険／皮肉／選択肢"),
    ("prohibit", "禁止する", "動詞", "The museum prohibits taking photographs in this room.", "許可する／勧める／相談する"),
    ("imitate", "まねる", "動詞", "The bird can imitate the sound of a phone.", "禁止する／困らせる／計算する"),
    ("interrupt", "中断する・遮る", "動詞", "Please do not interrupt me while I am speaking.", "強化する／集める／回復する"),
    ("encounter", "遭遇する", "動詞", "The hikers encountered heavy rain on the mountain.", "計算する／代表する／予測する"),
    ("requirement", "要件・必要条件", "名詞", "A valid passport is a requirement for this trip.", "例外／罰／集中"),
    ("estimate", "見積もる", "動詞", "The manager estimated the number of visitors.", "発見する／ふりをする／禁止する"),
    ("end up", "結局～する", "熟語", "We ended up taking a taxi home.", "偶然出会う／折れる／打ち切る"),
    ("movement", "動き・移動", "名詞", "The camera detected movement outside the house.", "装置／品質／習慣"),
    ("sensor", "センサー・感知器", "名詞", "A sensor turns on the light when someone enters.", "資料集／歯車／模型"),
    ("scan", "読み取る・走査する", "動詞", "Scan the code to open the restaurant menu.", "育てる／追跡する／記憶する"),
    ("observe", "観察する", "動詞", "The students observed birds in the school garden.", "予想する／装飾する／訓練する"),
    ("emerge", "現れる・出てくる", "動詞", "A small turtle emerged from its egg.", "閉じ込める／減少する／集める"),
    ("certification", "認証・証明", "名詞", "The farm applied for organic certification.", "品質／化学薬品／観測"),
    ("contain", "含む", "動詞", "This bottle contains fresh orange juice.", "管理する／運ぶ／放出する"),
    ("mechanism", "機構・仕組み", "名詞", "The clock's mechanism needs to be repaired.", "硬貨／彫像／地図"),
    ("ancient", "古代の", "形容詞", "They visited an ancient temple near the river.", "現代の／機械の／損傷した"),
    ("complicated", "複雑な", "形容詞", "The instructions were too complicated to follow.", "完全な／単純な／色鮮やかな"),
    ("clue", "手掛かり", "名詞", "The muddy shoes were an important clue.", "知識／道具／構造"),
    ("astronomy", "天文学", "名詞", "His interest in astronomy began with a book about stars.", "建築学／考古学／生物学"),
    ("demonstrate", "示す・実演する", "動詞", "The instructor demonstrated how to use the machine.", "隠す／修理する／失う"),
    ("impressive", "見事な・印象的な", "形容詞", "The students gave an impressive performance.", "日常的な／不完全な／無作為な"),
    ("innovative", "革新的な", "形容詞", "The company introduced an innovative recycling method.", "従来の／有機の／教育用の"),
    ("repair", "修理する", "動詞", "My brother repaired the broken bicycle.", "注文する／比較する／減らす"),
    ("scratch", "傷・引っかき傷", "名詞", "There is a small scratch on the table.", "塗料／座席／模様"),
    ("progress", "進捗・進歩", "名詞", "She made steady progress in learning English.", "遅延／料金／条件"),
    ("determine", "決定する・特定する", "動詞", "We will determine the final date tomorrow.", "推測する／拒否する／延期する"),
    ("hesitation", "ためらい", "名詞", "He accepted the invitation without hesitation.", "協力／謝罪／遅延"),
    ("cooperation", "協力", "名詞", "The event succeeded thanks to everyone's cooperation.", "競争／反対／衝突"),
    ("decline", "減少する", "動詞", "The number of empty houses began to decline.", "回復する／拡大する／維持する"),
    ("population", "個体数・人口", "名詞", "The island's population has grown over the past decade.", "生息域／食料源／水温"),
    ("vital", "極めて重要な", "形容詞", "Clean water is vital for all living things.", "急速な／個々の／沿岸の"),
    ("identify", "識別する・特定する", "動詞", "We identified the tree by the shape of its leaves.", "記録する／減速する／保護する"),
    ("collision", "衝突", "名詞", "The driver stopped in time to avoid a collision.", "協力／回復／減少"),
    ("endangered", "絶滅の危機にある", "形容詞", "The park protects several endangered species.", "回復した／長寿の／水中の"),
    ("threat", "脅威", "名詞", "Air pollution is a threat to public health.", "効果／進歩／希望"),
    ("adapt", "適応させる・応用する", "動詞", "The teacher adapted the activity for younger students.", "反対する／破壊する／観察する"),
    ("shipping lane", "航路", "名詞", "Fishing boats must stay clear of the busy shipping lane.", "沿岸地域／生息域／海流"),
]


def vocabulary():
    result = []
    for i, (word, meaning, pos, example, distractors) in enumerate(WORDS, 1):
        slug = re.sub(r"[^a-zA-Z0-9_]", "_", word.lower()).strip("_")
        result.append(dict(word=word, meaning=meaning, pos=pos, level="2級",
                           example=example, distractors=distractors.split("／"),
                           wordAudio=f"audio/vocab/w_{i:03d}_{slug}.mp3"))
    return result


def lessonplan(passages):
    honey, machine, email, whales = passages

    def excerpt(p, indexes):
        # Resolve Part 2 blanks correctly for the reading-aloud practice only.
        en = " ".join(p["sentencePairs"][i][0] for i in indexes)
        ja = "".join(p["sentencePairs"][i][1] for i in indexes)
        for q in p["questions"]:
            en = en.replace(f"( {q['number']} )", q["choices"][q["answer"] - 1])
            ja = ja.replace(f"( {q['number']} )", q["choiceTranslations"][q["answer"] - 1])
        return dict(en=f"[出典: {p['title']}]\n{en}", ja=ja)

    def examples(rows):
        return [dict(en=en, ja=ja, note=note) for en, ja, note in rows]

    def questions(rows):
        return [dict(q=q, a=a) for q, a in rows]

    fps = [
        dict(id="fp1", title="No matter how・Even if・Although の譲歩表現",
             subtitle="Concession — An Unexpected or Unchanged Result",
             explanation="譲歩とは『普通なら違う結果を予想する条件でも、実際はこうなる』という関係です。No matter how much S＋V は『どんなに～しても』で程度を問わず結果が変わりません。Even if S＋V は『たとえ～でも』で仮定した条件を含みます。Although S＋V は『実際に～だが』と事実を認めて逆の内容を続けます。今回の古代機械は、古いのに構造が複雑で、日常使用されなかったとしても価値は高い、という関係です。if だけの条件と区別して読みましょう。",
             sourceQuote="Although the device was more than 2,000 years old, it ( 21 ).\nEven if it was not used daily, it remains one of the most impressive ancient devices that has been discovered.",
             sourceLocation="大問1 Q16／大問2B 第1・3段落",
             examples=examples([
                 ("No matter how many times I read it, I find something new.", "何度読んでも、新しいことを見つける。", "how many times が回数を表し、回数にかかわらず結果が成立する。"),
                 ("Even if it rains, the match will take place indoors.", "たとえ雨が降っても、試合は屋内で行われる。", "雨はまだ確定していない条件。Even if の節に未来の will を置かない。"),
                 ("Although the bag is small, it holds many books.", "そのかばんは小さいが、本がたくさん入る。", "小さいという事実と、予想に反する容量を対比する。"),
             ]),
             practicePassage=excerpt(machine, range(0, 6)),
             practiceQuestions=questions([
                 ("Although the device was more than 2,000 years old の主節では、どんな意外な事実が述べられていますか。", "2000年以上前の装置なのに、非常に複雑な歯車構造を備えていたこと。古さと技術の複雑さの対比がQ21の根拠。"),
                 ("Although と Even if の違いを説明してください。", "Although は既にわかっている事実を認めて逆接を表す。Even if は『たとえ～という条件でも』と、未確定・仮定の条件も含められる。"),
                 ("『どんなに一生懸命練習しても、私は緊張する』を No matter how で表してください。", "No matter how hard I practice, I get nervous. how hard は努力の程度を表す。"),
                 ("引用文の who had not expected such complex mechanisms の who は何を説明しますか。", "experts（専門家たち）。彼らがそのような複雑な機構を予想していなかったことを補足し、驚きの理由を示す。"),
             ]),
             highlightPatterns=["Although the device was more than 2,000 years old", "Even if it was not used daily", "Although many parts are still missing", "Although people believe honeybees fly up to ten kilometers from their homes", "despite progress"],
             highlightLabel="譲歩表現"),
        dict(id="fp2", title="関係詞の省略と過去分詞の後置修飾",
             subtitle="Recognizing Reduced Noun Modifiers",
             explanation="名詞の後ろに続く説明を見抜きます。the items they found は the items (that) they found で、found の目的語になる関係代名詞が省略されています。一方、a system called Whale Safe は a system (that was) called Whale Safe と展開できる過去分詞の後置修飾です。前者は『主語＋動詞』、後者は『過去分詞から始まる句』が名詞を説明します。名詞の説明が終わる位置と、文全体の主語・動詞を分けて読むことが重要です。Among the items they found was ... では、主語 a broken object が was の後ろに来る倒置にも注意します。",
             sourceQuote="Among the items they found was a broken object with mechanical parts, along with statues and coins.\nIn the Santa Barbara Channel and San Francisco Bay, for example, a system called Whale Safe encouraged ships to reduce speed.",
             sourceLocation="大問2B 第1段落／大問3B 第3段落",
             examples=examples([
                 ("The book I borrowed was very useful.", "私が借りた本は、とても役に立った。", "book (that) I borrowed。目的格の関係代名詞を省略。文全体の動詞は was。"),
                 ("The bridge built last year connects the two towns.", "昨年建設された橋が、その二つの町をつないでいる。", "bridge (that was) built ...。built は橋を説明し、主節の動詞は connects。"),
                 ("Among the gifts she received was a beautiful notebook.", "彼女が受け取った贈り物の中には、美しいノートがあった。", "gifts (that) she received。場所を先に置いた倒置で、a beautiful notebook が主語。"),
             ]),
             practicePassage=excerpt(whales, range(12, 18)),
             practiceQuestions=questions([
                 ("a system called Whale Safe を、関係代名詞を省略しない形にしてください。", "a system that was called Whale Safe。called ... は system を後ろから説明する過去分詞句。"),
                 ("a system called Whale Safe encouraged ships ... の主語と主節の動詞は何ですか。", "主語は a system called Whale Safe、主節の動詞は encouraged。called は主節の動詞ではない。"),
                 ("the items they found で省略されている語と、found の目的語を答えてください。", "省略されているのは目的格の関係代名詞 that（または which）。found の目的語は先行詞 the items。"),
                 ("Whale Safe が効果を上げても、問題が残るのはなぜですか。", "西海岸では衝突で毎年何十頭も死亡し、観測されない死も多いから。despite progress は進歩と残る脅威の対比。"),
             ]),
             highlightPatterns=["the items they found", "an ancient machine used to observe the sky", "the used car you ordered", "the honey they collect", "a system called Whale Safe"],
             highlightLabel="名詞の後ろの説明"),
        dict(id="fp3", title="either A or B と並列構造の読み方",
             subtitle="Coordination — Matching the Roles of A and B",
             explanation="either A or B は『AかBのどちらか』。AとBが文中で果たす役割をそろえて読みます。本文の served either as an educational tool or to demonstrate ... は、教育の道具として役立ったという用途と、知識や技能を示すという目的を並べています。as＋名詞とto不定詞は形が異なりますが、どちらも served の用途・目的を説明します。単純に or の前後の単語だけを比べず、まとまりの終わりまで読むことが大切です。and が結ぶ二つの動作、複数の名詞、when and how far の二つの疑問語も、役割を確認して読みます。",
             sourceQuote="Rather, they believed it served either as an educational tool or to demonstrate the knowledge and skills of ancient scientists.",
             sourceLocation="大問2B 第3段落",
             examples=examples([
                 ("You can either call the office or send an email.", "事務所に電話するか、メールを送るか、どちらかができる。", "either が結ぶのは call ... と send ... という二つの動詞句。"),
                 ("The room can serve either as a classroom or as a meeting space.", "その部屋は教室としても、会議室としても使える。", "as＋名詞句どうしを並列にする。either ... or は二つの用途の選択。"),
                 ("The app records when and where the bus stops.", "そのアプリは、バスがいつ、どこで止まるかを記録する。", "when と where が共通の主語・動詞 the bus stops につながる。"),
             ]),
             practicePassage=excerpt(machine, range(12, 17)),
             practiceQuestions=questions([
                 ("either と or が結ぶ二つのまとまりを引用してください。", "as an educational tool と to demonstrate the knowledge and skills of ancient scientists。どちらも served の用途・目的。"),
                 ("the knowledge and skills of ancient scientists では and が何を結びますか。", "名詞 knowledge と skills。of ancient scientists は両方にかかり、『古代の科学者の知識と技能』。"),
                 ("『バスで行くか、歩いて行くか、どちらかにできる』を either ... or で表してください。", "You can either take the bus or walk. take the bus と walk は can に続く動詞句。"),
                 ("この装置が毎日の使用を目的としていなかったと考えられる理由は何ですか。", "一部の歯車が頻繁に動かなくなった可能性があるため。教育や技能の実演という別の用途が示されている。"),
             ]),
             highlightPatterns=["either as an educational tool or to demonstrate the knowledge and skills of ancient scientists", "the knowledge and skills of ancient scientists", "when and how far the honeybees fly", "had many small parts and showed the movement", "the progress of the work or the car's condition", "photos, sounds, and the ocean environment"],
             highlightLabel="並列のまとまり"),
        dict(id="fp4", title="前置詞 to・from・by の後ろの動名詞",
             subtitle="Preposition + -ing, Not an Infinitive",
             explanation="to の後ろが常に動詞の原形になるわけではありません。pay attention to の to は前置詞なので、動詞を続けると making になります。pay attention to making sure ... は『確実に～となるよう注意を払う』。同様に keep A from flying は『Aが飛ばないようにする』、by analyzing は『分析することで』という手段です。一方、to track や to show は to不定詞で目的を表します。直前の語と一緒に見て、前置詞＋動名詞なのか、to不定詞なのかを判別しましょう。",
             sourceQuote="Since you need to drive long distances frequently, we are paying close attention to making sure it is in the best possible condition.",
             sourceLocation="大問3A 第2段落／大問2A 第3段落／大問3B 第2段落",
             examples=examples([
                 ("Please pay attention to keeping the classroom clean.", "教室を清潔に保つことに注意を払ってください。", "pay attention to＋動名詞。to keeping の to は前置詞。"),
                 ("The fence keeps the dog from running into the road.", "その柵は犬が道路に飛び出さないようにする。", "keep＋目的語＋from V-ing。from の後ろは動名詞。"),
                 ("You can improve your pronunciation by listening carefully.", "注意深く聞くことで発音を改善できる。", "by V-ing は方法・手段を表す。"),
             ]),
             practicePassage=excerpt(email, range(5, 10)),
             practiceQuestions=questions([
                 ("paying close attention to making sure では、なぜ make ではなく making ですか。", "pay attention to の to は前置詞なので、後ろに動詞を置くと動名詞 making になるため。to不定詞ではない。"),
                 ("Since you need to drive long distances frequently の Since は何を表しますか。", "理由『頻繁に長距離を運転するので』。過去の起点『～以来』ではない。エンジンに特に注意を払う理由を述べる。"),
                 ("to provide you with a safe and perfect car の to は、to making と同じ働きですか。", "異なる。to provide は目的を表す to不定詞『お車をお渡しするために』。to making は前置詞＋動名詞。"),
                 ("『間違いから学ぶことで上達できる』を by＋動名詞で表してください。", "You can improve by learning from your mistakes. by learning は上達の手段。"),
             ]),
             highlightPatterns=["paying close attention to making sure", "keep them from flying long distances", "by analyzing patterns on the whales' tails", "by combining data from photos, sounds, and the ocean environment", "a camera for scanning the codes", "Thank you for coming to our shop the other day"],
             highlightLabel="前置詞＋動名詞"),
        dict(id="fp5", title="今回の重要なパラフレーズ", subtitle="Paraphrases Linking the Passage and the Answer",
             explanation="本文と正答は同じ単語とは限りません。動作の言い換え、能動態と受動態の変換、複数の具体例をまとめる表現に注目します。本文の意味を保った言い換えだけを選び、主語・数量・時点・理由が変わっていないか確認してください。特に『5分の1減った』と『5分の1になった』、将来の期待と現在の実施、クジラの尾の模様と行動パターンは区別します。",
             sourceQuote="① repairing the engine / painting the scratches → fixing the engine and painting scratched sections（Q25）\n② once the exact date has been determined → the day when they can deliver her car（Q26）\n③ identify individual whales / analyzing patterns on the whales' tails → follow each whale by recognizing the patterns on its tail（Q28）\n④ many deaths are never observed → accidents that people never notice（Q29）\n⑤ adapted for other species in danger → applied to protecting other animals that are also under threat（Q30）\n⑥ combining data from photos, sounds, and the ocean environment → using a variety of different methods（Q31）",
             sourceLocation="大問3A Q25・26／大問3B Q28〜31",
             examples=examples([
                 ("The road was repaired. / Workers fixed the road.", "道路が修理された。／作業員が道路を直した。", "repair と fix の言い換えと、受動態から能動態への変更。"),
                 ("Some errors were not noticed. / People failed to spot some mistakes.", "いくつかの誤りは気づかれなかった。／人々はいくつかの間違いを見落とした。", "not noticed＝failed to spot。否定の意味を保って言い換える。"),
                 ("The animals are in danger. / The animals are under threat.", "その動物たちは危機にある。／その動物たちは脅威にさらされている。", "in danger＝under threat。状態の言い換え。"),
             ]),
             practicePassage=excerpt(whales, range(7, 12)),
             practiceQuestions=questions([
                 ("identify individual whales を Q28 の正答ではどう表していますか。", "follow each whale。本文の個体識別と、その次の文の移動追跡を合わせて『個々のクジラを追跡する』と表す。"),
                 ("recognizing the patterns on its tail に対応する本文の表現を引用してください。", "analyzing patterns on the whales' tails。its は each whale の尾、whales' はクジラたちの尾を指す。"),
                 ("using a variety of different methods の具体例を本文から三つ挙げてください。", "AIによる写真認識、水中マイクでの録音、海洋環境のデータ。写真・音・環境の情報を組み合わせている。"),
                 ("AIの尾の模様分析を『クジラの行動パターンから生息域を特定する』と言い換えてよいですか。", "いけない。分析する対象が尾の模様から行動に変わり、目的も個体の追跡から生息域の特定へ変わっている。"),
             ]),
             highlightPatterns=["repairing the engine", "painting the scratches", "once the exact date has been determined", "identify individual whales", "analyzing patterns on the whales' tails", "many deaths are never observed", "adapted for other species in danger", "combining data from photos, sounds, and the ocean environment"],
             highlightLabel="パラフレーズ"),
    ]
    colors = ["#4f8cff", "#34d399", "#f472b6", "#fbbf24", "#f59e0b"]
    for i, (fp, color) in enumerate(zip(fps, colors), 1):
        fp["highlightColor"] = color
        fp["practicePassage"]["audioFile"] = f"audio/practice_pp{i}.mp3"
    return dict(focusPoints=fps)

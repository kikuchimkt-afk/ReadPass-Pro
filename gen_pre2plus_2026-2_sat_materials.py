# -*- coding: utf-8 -*-
"""55 balanced vocabulary items and five source-based lesson cards."""
import re

# word, meaning, part of speech, NEW example, three distractors, source form.
# 25 from Part 1, 15 from Part 2, 15 from Part 3.
WORDS = [
    ("chores", "家事・雑用", "名詞", "We share the household chores on Saturdays.", "要因／書類／間違い", "chores"),
    ("renovate", "改修する", "動詞", "They plan to renovate the old theater this spring.", "説明する／報いる／いら立たせる", "renovate"),
    ("bare", "覆いのない", "形容詞", "The trees were bare in winter.", "堅い／退屈な／遅い", "bare"),
    ("leisure", "余暇", "名詞", "She enjoys painting in her leisure time.", "正直さ／通貨／分数", "leisure"),
    ("battle", "戦う", "動詞", "The firefighters battled the flames all night.", "広げる／ろ過する／ちらりと見る", "battle"),
    ("salary", "給与", "名詞", "His salary increased after he became a manager.", "贈り物／記録／恥", "salary"),
    ("prejudice", "偏見", "名詞", "Learning about other cultures can reduce prejudice.", "手術／砂漠／封筒", "prejudice"),
    ("assist", "手伝う", "動詞", "A guide assisted us with our luggage.", "取り付ける／要求する／起こる", "assist"),
    ("erupt", "噴火する", "動詞", "The mountain may erupt again in the future.", "探検する／修理する／約束する", "erupted"),
    ("silently", "静かに・音を立てずに", "副詞", "The audience waited silently for the music to begin.", "熱心に／正直に／しっかりと", "silently"),
    ("against my will", "自分の意志に反して", "熟語", "I was sent to another school against my will.", "急いで／笑顔で／空中で", "against my will"),
    ("consist of", "～から成る", "熟語", "Our team consists of six players.", "～を心配する／～について話す／～をじっと見る", "consisted of"),
    ("accuse A of", "Aを～のことで非難する", "熟語", "They accused the driver of ignoring the signal.", "Aに～を警告する／Aに～を知らせる／Aに～を確信させる", "accused him of"),
    ("come to life", "活気づく", "熟語", "The quiet square comes to life on market days.", "静まり返る／思い浮かぶ／思い切ってやる", "came to life"),
    ("at risk", "危険にさらされて", "熟語", "The old bridge is at risk of collapsing.", "責任を負って／乗って／力ずくで", "at risk"),
    ("make one's bed", "ベッドを整える", "熟語", "I make my bed before breakfast every morning.", "目を閉じる／車を洗う／本を読む", "make my bed"),
    ("come into contact with", "～と接触する", "熟語", "Volunteers come into contact with people of all ages.", "～に取って代わる／～と恋に落ちる／～を最大限に利用する", "come into contact with"),
    ("factor", "要因", "名詞", "Sleep is an important factor in good health.", "結果／書類／誤り", "factors"),
    ("document", "書類", "名詞", "Please sign this document before you leave.", "雑用／要因／贈り物", "documents"),
    ("honesty", "正直さ", "名詞", "We appreciated her honesty about the mistake.", "余暇／勇気／通貨", "honesty"),
    ("fraction", "一部分・分数", "名詞", "Only a fraction of the seats were empty.", "全体／通貨／正直さ", "fraction"),
    ("currency", "通貨", "名詞", "You can exchange currency at the airport.", "余暇／分数／給与", "currency"),
    ("envelope", "封筒", "名詞", "Put the letter in an envelope.", "偏見／砂漠／手術", "envelope"),
    ("surgery", "手術", "名詞", "He needed surgery on his injured knee.", "偏見／記録／診断", "surgery"),
    ("extinct", "絶滅した", "形容詞", "This species became extinct many years ago.", "危険な／一般的な／健康な", "extinct"),
    ("natural disaster", "自然災害", "名詞", "The city prepared shelters for a natural disaster.", "観光地／交通機関／失業率", "natural disasters"),
    ("population", "人口", "名詞", "The island's population has grown since 2010.", "面積／品質／料金", "population"),
    ("destination", "目的地", "名詞", "The lake is a favorite destination for cyclists.", "災害／入口／出発", "destination"),
    ("entrance fee", "入場料", "名詞", "The museum's entrance fee is five dollars.", "給与／失業率／交通費", "entrance fee"),
    ("attract", "引きつける", "動詞", "Bright flowers attract butterflies to the garden.", "遠ざける／減らす／保管する", "attract"),
    ("as a whole", "全体として", "熟語", "The class as a whole did well on the test.", "特に／少なくとも／その代わりに", "as a whole"),
    ("unemployment rate", "失業率", "名詞", "The unemployment rate fell after the factory opened.", "人口密度／入場料／体温", "unemployment rate"),
    ("disability", "障害", "名詞", "The new ramp helps people with a disability enter the building.", "能力／災害／病原菌", "disabilities"),
    ("store", "保存する", "動詞", "Store the vegetables in a cool place.", "腐らせる／加熱する／増殖する", "stored"),
    ("spoil", "腐る", "動詞", "Milk can spoil if it is left in the sun.", "固まる／新鮮になる／甘くなる", "spoils"),
    ("bacteria", "細菌", "名詞", "Some bacteria are useful in making cheese.", "酸／糖分／水分", "bacteria"),
    ("condition", "条件・状態", "名詞", "These plants grow well in dry conditions.", "手順／要望／約束", "conditions"),
    ("acid", "酸", "名詞", "Lemon juice contains acid.", "砂糖／塩／細菌", "acid"),
    ("dip", "浸す・入れる", "動詞", "Dip the brush into clean water.", "保存する／取り替える／加熱する", "dipped"),
    ("with care", "注意して", "熟語", "Please handle the glass bowl with care.", "急いで／力ずくで／偶然に", "with care"),
    ("appointment", "予約", "名詞", "I have an appointment with a tutor tomorrow.", "会議／希望／診療所", "appointment"),
    ("available", "利用できる・空いている", "形容詞", "A meeting room is available after lunch.", "不便な／危険な／特定の", "available"),
    ("convenient", "都合がよい・便利な", "形容詞", "Is Friday morning convenient for you?", "早すぎる／不在の／定期的な", "convenient"),
    ("checkup", "健康診断", "名詞", "My father has a checkup every year.", "手術／会議／運動", "checkup"),
    ("no more than", "多くても～・～以内", "熟語", "The walk takes no more than ten minutes.", "少なくとも～／～を超えて／ちょうど～より少なく", "no more than"),
    ("confirm", "確認する", "動詞", "Please confirm the address before sending the package.", "断る／変更する／遅らせる", "confirm"),
    ("body temperature", "体温", "名詞", "A nurse measured the child's body temperature.", "室温／気温／運動量", "body temperature"),
    ("sweat gland", "汗腺", "名詞", "A sweat gland produces liquid on the skin.", "呼吸器／血管／鼻の形", "sweat glands"),
    ("depend on", "～に頼る", "熟語", "Young plants depend on regular watering.", "～を防ぐ／～と関係する／～を責める", "depend on"),
    ("effective", "効果的な", "形容詞", "Short daily practice is an effective way to learn.", "不便な／不可能な／危険な", "effective"),
    ("panting", "短い呼吸を素早く繰り返すこと", "名詞", "The runner was panting after the race.", "発汗すること／深呼吸すること／散歩すること", "panting"),
    ("release", "放出する・逃がす", "動詞", "Open the window to release the warm air.", "ため込む／取り込む／増やす", "release"),
    ("be related to", "～に関係する", "熟語", "Good concentration is related to enough sleep.", "～を妨げる／～に取って代わる／～を避ける", "is related to"),
    ("regularly", "定期的に", "副詞", "We meet regularly to discuss our progress.", "突然に／まれに／同じ程度に", "regularly"),
    ("prevent A from", "Aが～するのを防ぐ", "熟語", "The fence prevents children from entering the road.", "Aに～を可能にする／Aに～を勧める／Aを～で非難する", "prevent fur from"),
]


def vocabulary():
    result = []
    for n, (word, meaning, pos, example, distractors, form) in enumerate(WORDS,1):
        slug = re.sub(r"[^a-z0-9]+", "_", word.lower()).strip("_")
        result.append(dict(word=word, meaning=meaning, pos=pos, level="準2級プラス",
                           source="大問1" if n<=25 else "大問2" if n<=40 else "大問3",
                           sourceForm=form, example=example, distractors=distractors.split("／"),
                           wordAudio=f"audio/vocab/w_{n:03d}_{slug}.mp3",
                           exampleAudio=f"audio/vocab/ex_{n:03d}_{slug}.mp3"))
    return result


def example(en, ja, note):
    return dict(en=en, ja=ja, note=note)


def lessonplan(passages):
    city, honey, email, dogs = passages
    def quote(p, n, note):
        en, ja = p["sentencePairs"][n][:2]
        return example(en, ja, note)
    def practice(p, index, audio):
        en = p["paragraphs"][index]
        ja = p["translations"][index]
        for q in p["questions"]:
            en = en.replace(f"( {q['number']} )", q["choices"][q["answer"]-1])
        # Natural completed translations: never change blanks in exam passages.
        if p is city and index==2:
            ja = ja.replace("( 20 )", "村にいくつかの利点")
        if p is honey and index==1:
            ja = ja.replace("はちみつに含まれるいくつかの要因は ( 22 )。", "はちみつに含まれるいくつかの要因は、細菌が生存するのを妨げる働きをする。")
        return dict(en=f"[出典: {p['title']}]\n{en}", ja=ja, audioFile=audio)
    fps = [
        dict(id="fp1", title="後置修飾と結果を添える分詞（collected / lowering / giving）",
             subtitle="Participles: Modifiers and Result Clauses",
             explanation="大問2Aの第3段落では、the entrance fees collected の collected が前の名詞を後ろから説明し、『集められた入場料』となります。一方、lowering ... と giving ... は直前の出来事の結果を添えます。雇用を生んだ→失業率を下げた、村を助けた→新しい命を与えた、というつながりです。once called ... は city を修飾し、かつての呼び名を説明します。過去分詞による名詞の説明と、-ing による結果の補足を区別すると、長い文を主節から読み取れます。",
             sourceQuote='the entrance fees collected / lowering the village\'s unemployment rate / giving new life to the city / once called "the dying city."',
             sourceLocation="大問2A「The Dying City」第3段落", highlightLabel="分詞の役割", highlightColor="#4f8cff",
             examples=[quote(city,15,"主節の have created many jobs に、lowering ... がその結果を添える。"),
                       example("The books donated last week are on this shelf.", "先週寄付された本はこの棚にあります。", "donated last week は books を後ろから修飾する過去分詞句。"),
                       example("The new road shortened the trip, saving us an hour.", "新しい道路で移動が短くなり、1時間節約できました。", "saving ... は移動時間短縮の結果を補足する。")],
             practicePassage=practice(city,2,"audio/practice_pp1.mp3"),
             practiceQuestions=[
                 {"q":"the entrance fees collected の collected は、何を説明していますか。", "a":"entrance fees を後ろから説明する過去分詞で、『集められた入場料』。have been used が文の主動詞です。"},
                 {"q":"lowering ... の前にある主節の出来事と、その結果を分けてください。", "a":"新しい事業が多くの雇用を生んだ、が主節。その結果、村の失業率を下げた、が lowering ... の補足です。"},
                 {"q":"giving new life ... の主語に当たるものは何ですか。", "a":"主節の tourism（観光）。観光が村と住民を助け、それに伴って町に新しい命を与えています。"},
                 {"q":"once called ... の called と giving は同じ働きですか。", "a":"異なります。called は city の以前の呼び名を説明する受け身の修飾。giving は主節の出来事に伴う結果を添えています。"}],
             highlightPatterns=["the entrance fees collected", "including hotels, restaurants, and shops", "lowering the village's unemployment rate", "giving new life to the city", 'once called "the dying city."']),
        dict(id="fp2", title="形式目的語 it と不定詞の意味上の主語（make it hard for A to V）",
             subtitle="Formal Object it: make it hard for A to V",
             explanation="大問2B第2段落の makes it hard for bacteria to grow は、『細菌が増殖することを難しくする』という形です。it は形式目的語で、実際に難しいのは後ろの to grow。for bacteria が不定詞の意味上の主語です。which は直前の少量の酸を受け、その働きを補足します。Q22では、水分・糖分・酸という条件が細菌の生存や増殖を妨げる、という同じ関係を読み取ります。",
             sourceQuote="honey has a small amount of acid, which also makes it hard for bacteria to grow.",
             sourceLocation="大問2B「Honey」第2段落", highlightLabel="形式目的語 it", highlightColor="#f472b6",
             examples=[quote(honey,11,"makes＋it＋hard＋for bacteria＋to grow。it をはちみつそのものと訳さない。"),
                       example("The noise makes it difficult for me to study.", "その騒音のため、私は勉強しにくくなります。", "for me が study の意味上の主語。難しい内容は to study。"),
                       example("The clear map makes it easy for visitors to find the station.", "分かりやすい地図のおかげで、観光客は駅を簡単に見つけられます。", "easy でも同じ形。it の内容は後ろの不定詞。")],
             practicePassage=practice(honey,1,"audio/practice_pp2.mp3"),
             practiceQuestions=[
                 {"q":"makes it hard ... の it は何を指しますか。", "a":"形式目的語です。後ろの to grow（増殖すること）を先に受ける位置に置いています。"},
                 {"q":"for bacteria は to grow とどう結びつきますか。", "a":"増殖する主体が細菌であることを示します。for＋人・ものは不定詞の意味上の主語になります。"},
                 {"q":"which の先行詞と、追加する内容を説明してください。", "a":"先行詞は a small amount of acid。少量の酸も細菌の増殖を難しくする、という働きを補足しています。"},
                 {"q":"Q22の正答と makes it hard for bacteria to grow は、どう対応しますか。", "a":"正答は細菌の生存を妨げること。酸などが細菌の増殖を難しくする説明が、その具体的な根拠です。"}],
             highlightPatterns=["which also makes it hard for bacteria to grow", "makes it hard", "for bacteria to grow"]),
        dict(id="fp3", title="予定の受動表現と数量の上限（be expected to / no more than）",
             subtitle="Expected Events and Upper Limits",
             explanation="予約メール第2段落の The checkup is expected to take ... は、『健康診断は～かかると予想される』という受動態＋不定詞の形です。no more than thirty minutes は上限を示し、『多くても30分・30分以内』。Q25の over half an hour（30分を超える）とは逆です。また、The earliest available date は直前の after my return を受け、帰ってからの最も早い候補を指します。文の形と、数量・日付の範囲を合わせて読みます。",
             sourceQuote="The checkup is expected to take no more than thirty minutes.",
             sourceLocation="大問3A「About your appointment at our clinic」第2段落", highlightLabel="予定・上限", highlightColor="#34d399",
             examples=[quote(email,10,"be expected to V＝～すると予想される。no more than は数量の上限。"),
                       example("The repair is expected to take no more than two days.", "修理は2日以内で終わる見込みです。", "予想を表す受動態と、所要時間の上限を組み合わせる。"),
                       example("No more than ten students may join the workshop.", "その講習には多くても10人の生徒が参加できます。", "no more than ten は『10人以下』で、10人を超えない。")],
             practicePassage=practice(email,1,"audio/practice_pp3.mp3"),
             practiceQuestions=[
                 {"q":"is expected to take の文の形と意味を説明してください。", "a":"be＋過去分詞の受動態に to不定詞が続く形。健康診断には一定の時間がかかると予想されている、という意味です。"},
                 {"q":"no more than thirty minutes は、30分を超える可能性を示しますか。", "a":"いいえ。『多くても30分・30分以内』と上限を示すので、over half an hour と一致しません。"},
                 {"q":"September 1 は、提案された全ての日の中で最も早い日ですか。", "a":"いいえ。8月18日も候補です。9月1日は、帰ってからの候補の中で最も早い日を指します。"},
                 {"q":"通常の健康診断は省略されますか。根拠も示してください。", "a":"省略されません。we will proceed with your regular checkup とあり、通常の健康診断を行います。"}],
             highlightPatterns=["I would like to suggest August 18 at 2 p.m.", "If this time is not convenient for you", "soon after my return", "The earliest available date", "we will proceed with your regular checkup", "is expected to take no more than thirty minutes"]),
        dict(id="fp4", title="倍率比較と使役 let（four times more likely / let heat escape）",
             subtitle="Multiplicative Comparisons and let + Object + Verb",
             explanation="大問3B第3段落では、短い鼻の犬と長い鼻の犬を比較しています。about four times more likely ... than ... は、『～より約4倍起こしやすい』という倍率の比較です。数値を単に『4回多い』とは訳しません。最後の let heat escape は let＋目的語＋動詞の原形で、『熱を逃がす』。make it harder to ... と合わせると、鼻が短いことで熱を逃がしにくい、という理由になります。",
             sourceQuote="they are about four times more likely to get heat problems than dogs with longer noses. / short noses make it harder to let heat escape from the body.",
             sourceLocation="大問3B「Dogs and Heat」第3段落", highlightLabel="倍率・使役", highlightColor="#fbbf24",
             examples=[quote(dogs,16,"about four times＋比較級＋than。more likely to V は『～しやすい』。"),
                       example("This bag is three times heavier than that one.", "このかばんは、あのかばんの3倍の重さです。", "three times は比較の倍率を示す。"),
                       example("The open door lets fresh air enter the room.", "開いたドアから新鮮な空気が部屋に入ります。", "let＋fresh air＋原形 enter。to enter にはしない。")],
             practicePassage=practice(dogs,2,"audio/practice_pp4.mp3"),
             practiceQuestions=[
                 {"q":"約4倍の比較で、比べられている2つの対象は何ですか。", "a":"鼻がより短い犬と、鼻がより長い犬。暑さによる問題の起こりやすさを比べています。"},
                 {"q":"more likely to get heat problems は、どのように訳しますか。", "a":"『暑さによる問題を起こしやすい』。more likely は可能性がより高いという意味です。"},
                 {"q":"let heat escape の heat と escape の関係は何ですか。", "a":"heat が escape する主体。let＋目的語＋動詞の原形で、『熱を逃がす』という使役表現になります。"},
                 {"q":"鼻が短いと問題が起きやすい理由を、最後の文から説明してください。", "a":"鼻が短いと体から熱を逃がすのが難しくなるためです。This is because ... が直前の比較結果の理由を示します。"}],
             highlightPatterns=["allows dogs to release heat", "not all dogs are good at cooling themselves", "Dogs with shorter noses", "have more difficulty cooling down", "about four times more likely to get heat problems", "than dogs with longer noses", "short noses make it harder", "let heat escape from the body"]),
        dict(id="fp5", title="今回の重要なパラフレーズ", subtitle="Key Paraphrases in This Exam",
             explanation="選択肢の語が本文と同じかではなく、主語・範囲・否定・原因と結果が同じかを確かめます。例えば『大勢を引きつけ続けた』は『観光客の来訪を妨げなかった』と言い換えられます。犬の汗腺の働きが弱く、暑さで苦しむという説明は、Q27で原因と結果を一つの文にまとめています。no more than の上限、not very effective の否定、not fail to の意味も落とさずに読みます。",
             sourceQuote="① continued to attract large crowds → did not stop tourists from coming（Q19）\n② the clinic will be closed during that period → no appointments could be made from August 23 to 27.（Q24）\n③ dogs cannot depend on sweating to stay cool / dogs may suffer from heat → They are sensitive to the heat as they are not good at sweating.（Q27）\n④ not very effective in cooling the body → They have little effect on controlling body temperature.（Q28）\n⑤ brush them regularly → not fail to brush their dogs regularly.（Q30）",
             sourceLocation="大問2A Q19／大問3A Q24／大問3B Q27・28・30", highlightLabel="パラフレーズ", highlightColor="#f59e0b",
             examples=[quote(dogs,4,"cannot depend on sweating を『発汗が得意でない』という原因の表現にまとめる。"),
                       example("The train arrived on time. / The train was not late.", "電車は時間どおりに着きました。／電車は遅れませんでした。", "肯定文を否定表現で言い換えても、意味は一致する。"),
                       example("The task takes no more than ten minutes. / The task takes ten minutes or less.", "作業は10分以内で終わります。／作業には10分か、それより少ない時間がかかります。", "上限の表現を or less で言い換える。")],
             practicePassage=practice(dogs,0,"audio/practice_pp5.mp3"),
             practiceQuestions=[
                 {"q":"do not work as well as human sweat glands を日本語で言い換えてください。", "a":"犬の汗腺は、人間の汗腺ほど十分には働かない。人間より汗による冷却が得意でない、という比較です。"},
                 {"q":"cannot depend on sweating to stay cool を短く言い換えるとどうなりますか。", "a":"涼しく過ごすため、汗をかくことには頼れない。発汗だけでは十分に体を冷やせない、ということです。"},
                 {"q":"may suffer from heat を They always suffer from heat と言い換えてよいですか。", "a":"よくありません。may は可能性で、always は『いつも』という断定。頻度・確実性を強めてしまいます。"},
                 {"q":"Q27の正答は本文のどの2つの内容をまとめていますか。", "a":"汗腺が十分に働かず発汗に頼れないことと、暑さで苦しむことがあること。発汗が苦手なため暑さに弱い、という因果をまとめています。"}],
             highlightPatterns=["they do not work as well as human sweat glands", "dogs cannot depend on sweating to stay cool", "Even on days that feel comfortable to humans", "dogs may suffer from heat", "leaving dogs outside in hot weather is very dangerous"]),
    ]
    return dict(focusPoints=fps)

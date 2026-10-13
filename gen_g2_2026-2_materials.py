# -*- coding: utf-8 -*-
"""Balanced vocabulary and the five-focus-point lesson for Grade 2, 2026-2 (main venue)."""
import re

# 25 items from Part 1, 15 from Part 2, 15 from Part 3.
# Each example is new, rather than an extracted test-booklet sentence.
WORDS = [
    ("strictly", "厳しく・厳密に", "副詞", "The rules about phones are strictly followed at this school.", "不公平に／便利に／陽気に"),
    ("importance", "重要性", "名詞", "Our coach often talks about the importance of sleep.", "速さ／勇気／違い"),
    ("tend", "～する傾向がある", "動詞", "I tend to get hungry in the afternoon.", "反映する／奮闘する／投資する"),
    ("postpone", "延期する", "動詞", "We had to postpone the picnic until next week.", "隠す／報いる／強調する"),
    ("minority", "少数派", "名詞", "Only a minority of the students voted against the plan.", "機会／利益／実験"),
    ("proposal", "提案", "名詞", "The mayor accepted our proposal for a new park.", "大評判・感覚／物語／収集"),
    ("predict", "予測する", "動詞", "Nobody can predict what will happen next year.", "絞る／拒否する／実行する"),
    ("unconcerned", "無関心な・気にかけない", "形容詞", "He seemed unconcerned about the test tomorrow.", "嫉妬深い／有能な／障害のある"),
    ("murder", "殺人（事件）", "名詞", "The police are still investigating the murder.", "主題／宝物／喜び"),
    ("exist", "存在する", "動詞", "Dinosaurs existed millions of years ago.", "許す／祈る／じっと見つめる"),
    ("kill time", "時間をつぶす", "熟語", "We killed time at a bookstore before the movie began.", "故障する／見失う／必要を満たす"),
    ("watch out for", "～に気をつける", "熟語", "Watch out for ice on the road this morning.", "～を思いつく／（約束）を破る／～を尊敬する"),
    ("on the whole", "全体として", "熟語", "There were a few mistakes, but on the whole the report was good.", "このため／言い換えれば／その場合は"),
    ("make one's way through", "～をかき分けて進む", "熟語", "She made her way through the busy station to the exit.", "～の順番を務める／～で自分の役目を果たす／～に手を置く"),
    ("ever since", "～以来ずっと", "熟語", "I have liked baseball ever since I was a child.", "～の場合に備えて／まるで～のように／～がなければ"),
    ("make a mess", "散らかす", "熟語", "Please don't make a mess in the kitchen.", "思い切ってやってみる／休憩する／生計を立てる"),
    ("interfere with", "～を妨げる・～に干渉する", "熟語", "Loud noise can interfere with your sleep.", "急に～し出す／～を説明する／～を卒業する"),
    ("in accordance with", "～に従って", "熟語", "The money was used in accordance with the club's rules.", "～と比べて／～に加えて／～の代わりに"),
    ("urgent", "緊急の", "形容詞", "The doctor received an urgent call at midnight.", "整理された／正確な／退屈な"),
    ("tidy up", "片付ける", "熟語", "Let's tidy up the classroom before we go home.", "引き受ける／延期する／打ち切る"),
    ("witness", "目撃者", "名詞", "A witness saw the car hit the fence.", "探偵／容疑者／被害者"),
    ("clue", "手がかり", "名詞", "This footprint may be an important clue.", "証拠書類／罰金／犯行の動機"),
    ("concentration", "集中（力）", "名詞", "Listening to music sometimes helps my concentration.", "混乱／決意／記憶"),
    ("struggle", "奮闘する・苦労する", "動詞", "Many new students struggle to make friends at first.", "傾向がある／投資する／反映する"),
    ("emphasize", "強調する", "動詞", "The teacher emphasized the importance of reviewing.", "延期する／隠す／報いる"),
    ("install", "設置する", "動詞", "The city installed new lights along the river.", "撤去する／修理する／輸入する"),
    ("rescue", "救助", "名詞", "The rescue team found the missing hikers.", "避難所／警報／治療"),
    ("emergency", "緊急事態", "名詞", "Call this number in an emergency.", "事故の原因／災害の予報／安全の規則"),
    ("navigation", "進路の案内・航行", "名詞", "The ship uses satellites for navigation.", "通信料金／天気予報／燃料補給"),
    ("boost", "押し上げる・増やす", "動詞", "The festival boosted sales at local shops.", "減らす／比較する／維持する"),
    ("destination", "目的地・行き先", "名詞", "Hawaii is a popular destination for families.", "出発地／乗り換え駅／宿泊先"),
    ("summit", "山頂", "名詞", "We reached the summit just before sunrise.", "ふもと／斜面／登山道"),
    ("critic", "批判する人・評論家", "名詞", "Some critics said the movie was too long.", "支持者／観光客／住民"),
    ("rural", "田舎の・農村の", "形容詞", "My grandparents live in a quiet rural area.", "都会の／海岸の／工業の"),
    ("resident", "住民", "名詞", "The residents of this town clean the beach every spring.", "観光客／通勤者／移民"),
    ("decline", "減少する", "動詞", "The number of children in the village has declined.", "増加する／回復する／安定する"),
    ("artificial", "人工の", "形容詞", "This lake is artificial; it was made fifty years ago.", "自然の／地下の／古代の"),
    ("habitat", "生息地", "名詞", "Forests are an important habitat for many birds.", "食べ物／天敵／繁殖期"),
    ("measure", "対策・手段", "名詞", "The school took measures to prevent accidents.", "目標／原因／被害"),
    ("maintain", "維持する", "動詞", "It is hard to maintain a healthy diet when you are busy.", "失う／交換する／測定する"),
    ("renovate", "改装する", "動詞", "They renovated the old house and opened a café.", "取り壊す／引っ越す／借りる"),
    ("give away", "（無料で）譲る・手放す", "熟語", "I gave away my old bike to my cousin.", "片付ける／取りに来る／修理に出す"),
    ("layout", "配置・レイアウト", "名詞", "The new layout of the library makes books easy to find.", "家賃／営業時間／品ぞろえ"),
    ("secondhand", "中古の", "形容詞", "He bought a secondhand guitar online.", "手作りの／新品の／特注の"),
    ("scratch", "ひっかき傷", "名詞", "There is a small scratch on my phone screen.", "汚れ／へこみ／ひび"),
    ("appreciate", "ありがたく思う", "動詞", "I would appreciate your help with this project.", "期待する／催促する／確認する"),
    ("crew", "（作業）班・乗組員", "名詞", "A crew of five workers fixed the roof.", "客／店主／設計者"),
    ("invent", "発明する", "動詞", "Who invented the telephone?", "販売する／輸入する／改良する"),
    ("solution", "解決策", "名詞", "We need a better solution to this problem.", "原因／質問／不満"),
    ("fold", "折りたたむ", "動詞", "Please fold the towels and put them on the shelf.", "広げる／押す／運ぶ"),
    ("demonstrate", "実演する・示す", "動詞", "The staff demonstrated how to use the new machine.", "注文する／修理する／禁止する"),
    ("baby stroller", "ベビーカー", "名詞", "The mother pushed a baby stroller through the park.", "買い物かご／三輪車／車いす"),
    ("fundamentally", "根本的に", "副詞", "The Internet has fundamentally changed how we study.", "一時的に／部分的に／偶然に"),
    ("household", "家庭の", "形容詞", "Soap and paper towels are common household goods.", "業務用の／輸入の／高級な"),
    ("convince", "説得する・納得させる", "動詞", "She convinced her parents to let her study abroad.", "疑う／断る／命令する"),
]


def vocabulary():
    result = []
    for word, meaning, pos, example, distractors in WORDS:
        result.append(dict(word=word, meaning=meaning, pos=pos, level="2級",
                           example=example, distractors=distractors.split("／")))
    return result


def lessonplan(passages):
    mountain, bats, email, carts = passages

    def excerpt(p, first, last):
        # A contiguous run of original sentences; Part 2 blanks are resolved with
        # the correct answers for the reading-aloud practice only.
        rows = p["sentencePairs"]
        start = next(i for i, row in enumerate(rows) if row[0].startswith(first))
        end = next(i for i, row in enumerate(rows) if row[0].startswith(last))
        en = " ".join(row[0] for row in rows[start:end + 1])
        ja = "".join(row[1] for row in rows[start:end + 1])
        for q in p["questions"]:
            en = en.replace(f"( {q['number']} )", q["choices"][q["answer"] - 1])
            ja = re.sub(rf"\s*\( {q['number']} \)\s*", q["choiceTranslations"][q["answer"] - 1], ja)
        return dict(en=f"[出典: {p['title']}]\n{en}", ja=ja)

    def examples(rows):
        return [dict(en=en, ja=ja, note=note) for en, ja, note in rows]

    def questions(rows):
        return [dict(q=q, a=a) for q, a in rows]

    fps = [
        dict(id="fp1", title="関係代名詞の非制限用法と制限用法の読み分け",
             subtitle="Relative Clauses — Adding Information or Narrowing Down",
             explanation="関係代名詞の前にコンマがあるかどうかで、読み方が変わります。コンマのない制限用法（people who walked around his store）は『どの人か』を絞り込みます。コンマのある非制限用法（both shoppers, who could shop easily ...）は、先行詞について情報を付け加えます。非制限用法は『～で、その人たちは…』のように、いったん区切って前から読むと文の流れをつかみやすくなります。今回の大問3Bでは、買い物客と店のオーナーのそれぞれにどんな利点があったかを、非制限用法の who が説明しています。これがQ31の根拠です。なお、非制限用法では that は使いません。",
             sourceQuote="Shopping carts could be helpful to both shoppers, who could shop easily and conveniently, and supermarket owners, who could increase their sales.\nSome women thought shopping carts looked like baby strollers, which were used for carrying babies, ...",
             sourceLocation="大問3B 第2・3段落",
             examples=examples([
                 ("My uncle, who lives in Osaka, works at a hospital.", "私のおじは大阪に住んでいて、病院で働いている。", "コンマのある who は情報の追加。『大阪に住んでいるおじ』と、ほかのおじと区別しているわけではない。"),
                 ("The students who finished early helped the others.", "早く終わった生徒たちが、ほかの生徒を手伝った。", "コンマのない who は制限用法。早く終わった生徒に絞り込んでいる。"),
                 ("We visited Kyoto, which has many old temples.", "私たちは京都を訪れた。京都には古い寺がたくさんある。", "固有名詞は一つに決まるので、説明を付け加える非制限用法の which を使う。"),
             ]),
             practicePassage=excerpt(carts, "Before the invention,", "Some women thought"),
             practiceQuestions=questions([
                 ("both shoppers, who could shop easily and conveniently, and supermarket owners, who could increase their sales で、2つの who はそれぞれ何を説明していますか。", "1つ目は shoppers（買い物客）、2つ目は supermarket owners（スーパーマーケットのオーナー）です。客は楽に便利に買い物ができ、オーナーは売り上げを伸ばせる、という利点を付け加えています。"),
                 ("baby strollers, which were used for carrying babies を、前から区切って読んでください。", "『ベビーカーに似ていると思った。ベビーカーは赤ちゃんを運ぶために使われるものだった』のように、いったん区切って情報を付け加える形で読みます。"),
                 ("He hired people who walked around his store ... の who の前にコンマがないのはなぜですか。", "どんな人を雇ったのかを『店内を歩き回る人』に絞り込む制限用法だからです。コンマがあると、雇った人について情報を付け加える読み方になります。"),
                 ("Q31の正解 Shopping carts were thought to be beneficial for both shoppers and supermarket owners. の根拠となる文を引用してください。", "Shopping carts could be helpful to both shoppers, who could shop easily and conveniently, and supermarket owners, who could increase their sales. です。helpful が beneficial に言い換えられています。"),
             ]),
             highlightPatterns=["both shoppers, who could shop easily and conveniently", "supermarket owners, who could increase their sales", "baby strollers, which were used for carrying babies", "He hired people who walked around his store", "many insects, such as flies and moths, that harm plants"],
             highlightLabel="関係詞の説明"),
        dict(id="fp2", title="動詞＋目的語＋to不定詞・原形・-ing の使い分け",
             subtitle="Verb + Object + to V / Bare Infinitive / -ing",
             explanation="『動詞＋目的語＋動詞の形』では、前の動詞によって後ろの形が決まります。enable / allow / cause は to不定詞（enabled mountain workers to communicate、allows new plants to start、causing them to lose）。help は原形または to不定詞（help many plants grow）、make は原形（make them look less manly）です。see は原形または -ing をとり、-ing なら『～しているところを見る』という意味になります（saw others using the carts）。どの形でも、目的語と後ろの動詞は『目的語が～する』という主語と動詞の関係です。この関係に気づくと、だれが何をするのかを正確に読み取れます。",
             sourceQuote="It also enabled mountain workers to communicate about navigation and to ( 18 ).\nIn addition, bats help many plants grow by ( 21 ).\nWhen customers saw others using the carts comfortably, they started using them too.",
             sourceLocation="大問2A 第1段落／大問2B 第1段落／大問3B 第3段落",
             examples=examples([
                 ("The new app enables students to check their grades online.", "その新しいアプリで、生徒は成績をオンラインで確認できる。", "enable＋O＋to V は『Oが～できるようにする』。物が主語のときは『～によって』と訳すと自然になる。"),
                 ("My father helped me carry the heavy boxes.", "父は、私が重い箱を運ぶのを手伝ってくれた。", "help＋O＋原形。help me to carry の形も使える。"),
                 ("I saw a cat crossing the road.", "私は猫が道路を渡っているところを見た。", "see＋O＋-ing は動作の途中を見たことを表す。see＋O＋原形なら、動作の始めから終わりまでを見たことになる。"),
             ]),
             practicePassage=excerpt(bats, "Bats play an important role", "If the number continues"),
             practiceQuestions=questions([
                 ("bats help many plants grow で、grow の主語にあたるのは何ですか。", "many plants です。『コウモリは多くの植物が育つのを助ける』という関係で、育つのは植物です。"),
                 ("This allows new plants to start growing far from the parent plant. の This は何を指しますか。", "コウモリが植物の種をいろいろな場所へ運ぶこと（Q21の正解の内容）です。そのおかげで、親の植物から離れた所で新しい植物が育ち始めます。"),
                 ("allows new plants to start の allow を make に替えると、to start の部分はどうなりますか。", "make＋O＋原形になるので、make new plants start となります。ただし make は『～させる』、allow は『～できるようにする』で、意味も変わります。"),
                 ("農家が作物に使う化学薬品を減らせるのはなぜですか。", "1匹のコウモリが一晩に何千匹もの虫を食べ、植物を傷める虫が減るからです。Since ... が理由を表しています。"),
             ]),
             highlightPatterns=["enabled mountain workers to communicate", "help many plants grow", "allows new plants to start growing", "causing them to lose the body fat", "make them look less manly", "saw others using the carts comfortably"],
             highlightLabel="動詞＋O＋動詞"),
        dict(id="fp3", title="進行形・完了形・助動詞つきの受動態",
             subtitle="Passive Voice with being / have been / could be",
             explanation="受動態（be＋過去分詞）は、ほかの形と組み合わさるとまとまりが長くなります。is being changed は進行形の受動態で、『今～されているところだ』のほか、すでに決まっている近い予定も表します（メールでは改装はこれから始まるので『変えられることになっている』と読みます）。has now been expanded や have been improved は完了形の受動態で『（これまでに）～されてきた・～された状態だ』を表します。could be stored は助動詞つきの受動態で『保管されることができる』です。be / been / being の後ろの過去分詞を見つけて『～される』の意味をつかみ、そこに時の情報を加えて読みましょう。大問3Bの第4段落では、ショッピングカートが時代とともに改良されてきた流れを、受動態が支えています。",
             sourceQuote="We'll no longer need them as the shop's layout is being changed.\nShopping carts have been improved over time. In the middle of the twentieth century, a new cart was designed so that many carts could be stored in a smaller area.",
             sourceLocation="大問3A 第1段落／大問3B 第4段落",
             examples=examples([
                 ("The bridge is being repaired, so we have to take another road.", "その橋は修理されているところなので、別の道を通らなければならない。", "is being＋過去分詞は進行形の受動態で『今～されているところだ』。"),
                 ("The museum has been closed for two years.", "その博物館は2年間閉館している。", "has been＋過去分詞は完了形の受動態。ここでは2年前から今まで続く状態を表す。"),
                 ("These books can be borrowed for two weeks.", "これらの本は2週間借りることができる。", "助動詞＋be＋過去分詞。『～されることができる』は、自然な日本語では『～できる』となることが多い。"),
             ]),
             practicePassage=excerpt(carts, "Shopping carts have been improved", "The invention of shopping carts"),
             practiceQuestions=questions([
                 ("Shopping carts have been improved over time. を、時の流れがわかるように訳してください。", "『ショッピングカートは時とともに改良されてきた。』have been improved は、過去から現在までの間に改良が重ねられてきたことを表します。"),
                 ("a new cart was designed so that many carts could be stored in a smaller area で、新しいカートは何のために設計されましたか。", "多くのカートをより狭い場所に保管できるようにするためです。so that ... could ～ が目的を表し、Q30の正解（カートの置き場所を節約できた）の根拠になります。"),
                 ("the shop's layout is being changed は、店について何を伝えていますか。", "店のレイアウトがこれから変更されることになっている、ということです。メールの初めに We are going to renovate our shop とあり、改装作業は2週間後に始まる（Since the renovation crew will start working in two weeks）ので、工事の最中ではなく、決まっている予定を進行形で表していると読みます。そのため、テーブルや棚がもう必要なくなります。"),
                 ("a safety belt for children's seats was also added の主語と動詞を答えてください。", "主語は a safety belt（for children's seats は belt を説明する語句）、動詞は was added（受動態）です。"),
             ]),
             highlightPatterns=["is being changed", "has now been expanded", "have also been created", "have been improved over time", "many carts could be stored"],
             highlightLabel="受動態の形"),
        dict(id="fp4", title="条件・譲歩・理由をつなぐ in case / even though / since",
             subtitle="Connecting Conditions, Concessions and Reasons",
             explanation="接続詞は、二つの内容の関係を示す道しるべです。In case S＋V には『～するといけないから・～する場合に備えて』と『（もし）～の場合には』の2つの使い方があります。メールの In case you are unable to accept the items は後者で、if とほぼ同じ意味です（名詞が続くときは in case of＋名詞の形になり、大問2Aの in case of emergencies は『緊急の場合に』という意味です）。Even though S＋V は『～ではあるけれども』と、事実を認めたうえで反対の内容を続けます。Since S＋V は、文脈によって理由『～なので』を表します。メールでは、トラックが必要な理由と、金曜日までに返事がほしい理由が、これらの接続詞を使って示されています。Q25・Q26は、この理由の部分が根拠になります。",
             sourceQuote="Even though each one isn't very large, all five together are still too heavy to carry without a truck.\nIn case you are unable to accept the items, I will need to check whether other shops might want them.\nSince the renovation crew will start working in two weeks, please let me know what you think about this by this Friday.",
             sourceLocation="大問3A 第2・3段落",
             examples=examples([
                 ("In case it rains, the event will be held in the gym.", "雨が降った場合は、行事は体育館で行われる。", "ここでの In case S＋V は『～の場合は』（if とほぼ同じ）。Take an umbrella in case it rains.（雨が降るといけないから傘を持って行きなさい）のように『～に備えて』の意味でもよく使う。名詞が続くときは in case of rain（雨の場合は）。"),
                 ("Even though he was tired, he finished his homework.", "彼は疲れていたけれども、宿題を終えた。", "Even though は事実を認めて逆の内容を続ける。Even if（たとえ～でも）は仮定の条件。"),
                 ("Since the store is closed today, let's go tomorrow.", "今日は店が閉まっているので、明日行こう。", "Since S＋V は理由『～なので』。相手もわかっている理由を示すときによく使われる。"),
             ]),
             practicePassage=excerpt(email, "Even though each one", "Since the renovation crew"),
             practiceQuestions=questions([
                 ("Even though each one isn't very large, all five together are still too heavy to carry without a truck. で、ケイティが認めている事実と、伝えたい内容はそれぞれ何ですか。", "認めている事実は一つ一つがそれほど大きくないこと、伝えたい内容は5つ合わせるとトラックなしでは運べないほど重いことです。Q25の根拠です。"),
                 ("too heavy to carry without a truck を、so ... that ～ can't を使って言い換えてください。", "so heavy that we can't carry them without a truck です。too ... to ～は『～するには…すぎる』という意味で、否定の意味を含みます。"),
                 ("In case you are unable to accept the items の In case は、ここではどんな意味ですか。", "『もし～の場合には』という条件です。ジョージの店が受け取れない場合は、ほかの店に問い合わせる必要がある、という流れです。"),
                 ("ケイティが金曜日までに返事がほしい理由を2つ挙げてください。", "ほかの店に問い合わせて返事を待つのに時間がかかるかもしれないこと（Contacting other shops and waiting for their replies may take some time）と、2週間後に改装作業が始まること（Since ...）です。Q26の正解は前者の内容です。"),
             ]),
             highlightPatterns=["Even though each one isn't very large", "In case you are unable to accept the items", "Since the renovation crew will start working in two weeks", "Since one bat can eat thousands of insects a night", "Since there are not enough food sources during the winter"],
             highlightLabel="接続詞の働き"),
        dict(id="fp5", title="今回の重要なパラフレーズ", subtitle="Paraphrases Linking the Passage and the Answer",
             explanation="大問3では、正解の選択肢が本文と同じ内容を別の語句で表していることがよくあります。本文の具体的な説明が選択肢では短くまとめられたり（made of a simple chair that could be folded → a folding chair）、変化の表し方が変わったり（supermarkets grew larger / more people began driving cars → the size ... and the number ... increased）します。反対に、本文の語句を使っていても内容がずれている選択肢は不正解です。主語・数量・時期・目的が本文と一致しているかを確かめて選びましょう。",
             sourceQuote="① want to give away some of the furniture / a secondhand shop like yours might be able to accept it → wants to offer some used items for his shop（Q24）\n② too heavy to carry without a truck. Could you come to pick them up? → cannot transport all five items without the shop's help（Q25）\n③ check whether other shops might want them / may take some time → may need time to ask other shops if they are interested（Q26）\n④ made of a simple chair that could be folded. It had two baskets and wheels. → a folding chair with wheels and two baskets（Q27）\n⑤ supermarkets grew larger and more people began driving cars → the size of the supermarkets and the number of shoppers with cars increased（Q28）\n⑥ hired people who walked around his store ... demonstrating how useful the carts were → hiring people to demonstrate using the carts in the store（Q29）\n⑦ many carts could be stored in a smaller area → save space for shopping carts（Q30）\n⑧ helpful to both shoppers ... and supermarket owners → beneficial for both shoppers and supermarket owners（Q31）",
             sourceLocation="大問3A Q24〜26／大問3B Q27〜31",
             examples=examples([
                 ("The chair can be folded. / It is a folding chair.", "その椅子は折りたためる。／それは折りたたみ椅子だ。", "can be folded（受動態の説明）が folding（名詞を修飾する形）に言い換えられている。"),
                 ("More people began driving cars. / The number of people with cars increased.", "車を運転し始める人が増えた。／車を持つ人の数が増えた。", "more people を『～の数が増えた』と言い換える。どちらも人数の増加を表す。"),
                 ("Many carts could be kept in a smaller area. / The new design saved space.", "多くのカートを狭い場所に置けるようになった。／新しいデザインで場所を節約できた。", "具体的な説明と、それをまとめた言い方の対応。save space は『場所を節約する』。"),
             ]),
             practicePassage=excerpt(carts, "The shopping cart was invented", "Soon after, he introduced"),
             practiceQuestions=questions([
                 ("Q27の正解 a folding chair with wheels and two baskets に対応する本文の表現を、2つの文から引用してください。", "His first shopping cart was made of a simple chair that could be folded. と It had two baskets and wheels. です。could be folded が folding に、two baskets and wheels が with wheels and two baskets にまとめられています。"),
                 ("Q27の選択肢1 a rolling chair with one fixed basket that people could not fold. が不正解なのはなぜですか。", "本文の椅子は折りたためて（could be folded）、かごは2つです。『折りたためない』『かごが1つ』の2点が本文と合いません。"),
                 ("He noticed that shoppers had difficulty continuing shopping を、別の英語で言い換えてください。", "例：He noticed that shoppers found it hard to keep shopping. have difficulty -ing（～するのに苦労する）は、find it hard to V で言い換えられます。"),
                 ("ゴールドマンがショッピングカートを作ったのはなぜですか。", "かごが重くなりすぎて買い物を続けにくいという問題に気づき、その解決策（a solution）を探したからです。最後の文には、人々の買い物の仕方を変えたいと願っていた（hoped to change the way people shopped）とあります。"),
             ]),
             highlightPatterns=["give away some of the furniture", "too heavy to carry without a truck", "made of a simple chair that could be folded", "As supermarkets grew larger and more people began driving cars", "demonstrating how useful the carts were", "in a smaller area", "Shopping carts could be helpful"],
             highlightLabel="パラフレーズ"),
    ]
    colors = ["#4f8cff", "#34d399", "#f472b6", "#fbbf24", "#f59e0b"]
    for fp, color in zip(fps, colors):
        fp["highlightColor"] = color
    return dict(focusPoints=fps)


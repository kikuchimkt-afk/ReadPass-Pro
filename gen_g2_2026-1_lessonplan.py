# -*- coding: utf-8 -*-
"""
2026年度 第1回（準会場）英検2級 data.json 生成スクリプト
Step B: lessonPlan（focusPoints × 5）
"""
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = r"G:\マイドライブ\ReadPass Pro\data\grade2\2026-1-sat\data.json"

fp1 = {
    "id": "fp1",
    "title": "It was not until ... that（〜して初めて…した）",
    "subtitle": "It was not until ... that — Delayed Discovery",
    "explanation": "「It was not until X that S + V」は「Xになって初めてSはVした」という意味の強調構文。出来事が予想より遅れて起こったことを際立たせる表現で、歴史や発見の叙述で頻出する。通常文「S did not V until X」を It was 〜 that で強調した形。only after（〜の後で初めて）、since（〜以来）などの時間表現とあわせて、出来事の時系列を整理しながら読むことがポイント。",
    "sourceQuote": "It was not until the 1940s that this underwater part of the city began attracting attention.",
    "sourceLocation": "大問3B 第3段落",
    "examples": [
        {
            "en": "It was not until last year that the company introduced its first electric car.",
            "ja": "昨年になって初めて、その会社は初の電気自動車を発表した。",
            "note": "It was not until + 時 + that S + V。「〜して初めて…した」の定型"
        },
        {
            "en": "It was not until she read the letter that she understood the truth.",
            "ja": "彼女はその手紙を読んで初めて真実を理解した。",
            "note": "until の後ろに節（S + V）が入る形も可能"
        },
        {
            "en": "The error was not discovered until the report was published.",
            "ja": "その誤りは報告書が出版されるまで発見されなかった。",
            "note": "not ... until の通常語順。It was not until ... that に書き換え可能"
        }
    ],
    "practicePassage": {
        "en": "[出典: The Lost City]\nOver the past two thousand years, many parts of Baia have sunk, and about half of the city's structures are now underwater. It was not until the 1940s that this underwater part of the city began attracting attention. An Italian military pilot discovered mysterious structures under the water in the bay while flying low. Walls and roads in the water were seen clearly in the picture he took. However, investigation in the water only began after scuba devices were advanced enough. Later investigations revealed a room filled with large sculptures, and since the early 2000s, the part of the city that sank into the sea has been managed as a protected marine area.",
        "ja": "過去2000年の間にバイアの多くの部分が沈み、現在では町の建造物の約半分が水中にある。この町の水中部分が注目を集め始めたのは、1940年代になってからのことだった。イタリア軍のパイロットが低空飛行中に、湾の水中に謎の構造物を発見したのだ。彼が撮影した写真には、水中の壁や道路がはっきりと写っていた。しかし、水中での調査は、スキューバ装備が十分に進歩してから初めて始まった。その後の調査で大きな彫刻で満たされた部屋が発見され、2000年代初頭以降、海に沈んだ町の部分は保護海域として管理されている。",
        "audioFile": "audio/practice_pp1.mp3"
    },
    "practiceQuestions": [
        {
            "q": "「It was not until the 1940s that this underwater part of the city began attracting attention」を文法的に分析してください。",
            "a": "It was not until + 時期 + that S + V の強調構文。「1940年代になって初めて水中部分が注目を集め始めた」。通常文 This part did not begin attracting attention until the 1940s の強調形。"
        },
        {
            "q": "水中での本格的な調査が始まったのはいつですか？該当する英語表現も挙げてください。",
            "a": "スキューバ装備が十分に進歩した後。investigation in the water only began after ... が該当し、only after は not until と同様「〜して初めて」を表す。"
        },
        {
            "q": "「investigation in the water only began after scuba devices were advanced enough」を It was not until を使って書き換えてください。",
            "a": "It was not until scuba devices were advanced enough that investigation in the water began.（only after ≒ not until の言い換え）"
        }
    ],
    "highlightPatterns": [
        "It was not until the 1940s that this underwater part of the city began attracting attention",
        "investigation in the water only began after scuba devices were advanced enough",
        "since the early 2000s",
        "Over the past two thousand years",
        "since ancient times",
        "About two thousand years ago",
        "over many centuries",
        "which used to be crowded with dozens of cars",
        "spaces that used to be mainly for cars"
    ],
    "highlightColor": "#4f8cff",
    "highlightLabel": "not until 強調"
}

fp2 = {
    "id": "fp2",
    "title": "同格・言い換えの挿入表現（, or / such as / カンマ同格）",
    "subtitle": "Appositives & Rephrasing: or / such as",
    "explanation": "英文では、難しい語の直後に「, or 〜,」を置いてやさしく言い換えたり、「such as」で具体例を挙げたり、カンマで同格の説明を挿入したりする。大問2Bの「a habitat, or a place to live」では、or の後ろが直前の語 habitat の定義になっている。この or は「または」ではなく「つまり」の意味。未知語の意味を本文中から推測する重要な手がかりになる。",
    "sourceQuote": "it becomes a habitat, or a place to live, for many living things",
    "sourceLocation": "大問2B 第1段落",
    "examples": [
        {
            "en": "Astronomy, or the study of stars and planets, has a very long history.",
            "ja": "天文学、つまり星や惑星の研究には非常に長い歴史がある。",
            "note": "「, or」による言い換え（定義）。「または」と訳さないこと"
        },
        {
            "en": "The blue whale, the largest animal on Earth, can grow to thirty meters.",
            "ja": "地球最大の動物であるシロナガスクジラは、30メートルまで成長することがある。",
            "note": "カンマによる同格。直前の名詞に説明を加える"
        },
        {
            "en": "Citrus fruits, such as oranges and lemons, are rich in vitamin C.",
            "ja": "オレンジやレモンなどの柑橘類はビタミンCが豊富だ。",
            "note": "such as による具体例の列挙。for example より名詞に直結しやすい"
        }
    ],
    "practicePassage": {
        "en": "[出典: Dead Trees]\nDead trees are often full of life. In the woods, for example, they support many different animals and insects in various ways. When a tree is no longer alive or standing, it becomes a habitat, or a place to live, for many living things. First, mushrooms help break down the tree. This allows insects to go inside the tree and lay eggs. In turn, new insects and other creatures begin to grow. Some small animals hide under bark that has fallen off the tree. Some birds build their houses in holes in the wood.",
        "ja": "枯れ木はしばしば生命に満ちあふれている。例えば森の中では、枯れ木はさまざまな方法で多くの異なる動物や昆虫を支えている。木が生きていなかったり立っていなかったりすると、それは多くの生き物にとっての生息地、つまり住む場所になる。まず、キノコが木の分解を助ける。これにより昆虫は木の中に入って卵を産むことができる。やがて、新しい昆虫やその他の生き物が育ち始める。木から剥がれ落ちた樹皮の下に隠れる小動物もいる。木の穴に巣を作る鳥もいる。",
        "audioFile": "audio/practice_pp2.mp3"
    },
    "practiceQuestions": [
        {
            "q": "「a habitat, or a place to live」の or の働きを説明してください。",
            "a": "言い換え（同格）の or。直前の habitat（生息地）を a place to live（住む場所）とやさしく定義し直している。選択の「または」ではない点に注意。"
        },
        {
            "q": "「In the woods, for example」の for example は何の例を導入していますか？",
            "a": "前文「枯れ木は生命に満ちあふれている」の具体例として、森の中で動物や昆虫を支えているという内容を導入している。"
        },
        {
            "q": "未知語 habitat の意味を本文中の手がかりから推測する手順を説明してください。",
            "a": "直後の「, or a place to live,」が定義の挿入になっているので、「住む場所＝生息地」と推測できる。「, or」の言い換えは未知語推測の重要な手がかり。"
        },
        {
            "q": "この段落の「具体例の列挙」を示す表現を2つ挙げてください。",
            "a": "Some small animals hide under bark ... / Some birds build their houses ...。Some ... Some ... の並列で生き物の例を列挙している。"
        }
    ],
    "highlightPatterns": [
        "a habitat, or a place to live",
        "In Bratislava, a central city in Slovakia",
        "such as parks, campgrounds, and roadsides",
        "such as plastic bottles",
        "such as dome-shaped public baths",
        "One successful example is Nevädzová Street",
        "In the woods, for example",
        "For instance, it might be necessary to remove them",
        "like the Las Vegas of the Roman Empire",
        "carbon and other elements"
    ],
    "highlightColor": "#34d399",
    "highlightLabel": "同格・言い換え"
}

fp3 = {
    "id": "fp3",
    "title": "依頼・問い合わせの丁寧表現（whether it would be possible / Could you）",
    "subtitle": "Polite Requests & Inquiries in Formal Emails",
    "explanation": "英文メールでは、I am writing to ask whether ...（〜かどうかお尋ねするためにご連絡しています）、whether it would be possible to V（〜することが可能かどうか）、Could you ...?、Please let me/us know ... など、直接的な命令を避けた丁寧な依頼表現が使われる。would や could は仮定法由来の婉曲用法で、丁寧さを生むのがポイント。英検のEメール問題で頻出し、ライティングでもそのまま使える定型表現。",
    "sourceQuote": "I am writing to ask whether it would be possible for the student to join one of the factory tours held on Fridays by himself.",
    "sourceLocation": "大問3A 第2段落",
    "examples": [
        {
            "en": "I am writing to ask whether it would be possible to change my reservation.",
            "ja": "予約を変更することが可能かどうかお尋ねしたく、ご連絡しております。",
            "note": "I am writing to ask whether ... ＝ メールの用件を丁寧に切り出す定型表現"
        },
        {
            "en": "Could you tell me what documents I should prepare in advance?",
            "ja": "事前にどの書類を準備すべきか教えていただけますか。",
            "note": "Could you + 間接疑問文。Can you より丁寧"
        },
        {
            "en": "Please let me know if there is a convenient time for a meeting.",
            "ja": "会議に都合の良い時間があればお知らせください。",
            "note": "Please let me know if/whether ... ＝ 返信を求める定型表現"
        }
    ],
    "practicePassage": {
        "en": "[出典: Inquiry about the factory]\nI am writing to ask whether it would be possible for the student to join one of the factory tours held on Fridays by himself. His last class of the day ends at 2:00 p.m. on Fridays, which is earlier than on other days. As the school is within walking distance of your factory, if he leaves right after the class, he should be able to arrive by 2:30 p.m. Please let me know if there is an available date and time for a tour on a Friday in the next two months. Could you also tell us what he should bring or prepare in advance? He would like to take a few photos for his class report, so please let us know whether photography is permitted during the tour.",
        "ja": "その生徒が一人で、金曜日に開催されている工場見学ツアーに参加することが可能かどうかをお尋ねしたく、ご連絡しております。金曜日は彼のその日の最後の授業が午後2時に終わり、他の曜日より早く終わります。学校は貴工場から徒歩圏内にありますので、授業後すぐに出発すれば、午後2時30分までには到着できるはずです。今後2か月以内の金曜日で、ツアーに参加できる日時があれば教えてください。また、事前に持参または準備すべきものがあれば教えていただけますでしょうか。彼は授業のレポート用に写真を数枚撮りたいと考えていますので、ツアー中の写真撮影が許可されているかどうかもお知らせください。",
        "audioFile": "audio/practice_pp3.mp3"
    },
    "practiceQuestions": [
        {
            "q": "「I am writing to ask whether it would be possible for the student to join ...」の構造を分析してください。",
            "a": "I am writing to ask（ご連絡している目的）+ whether 名詞節（〜かどうか）+ it would be possible for A to V（形式主語 it ＋ 意味上の主語 for A）。would で婉曲・丁寧さを出している。"
        },
        {
            "q": "Could you also tell us what he should bring or prepare in advance? が Can you ...? より丁寧なのはなぜですか？",
            "a": "could は仮定法由来の婉曲表現で、相手への要求の直接性を弱めるため。さらに疑問詞節（what he should bring）を使う間接疑問で表現が柔らかくなっている。"
        },
        {
            "q": "返信を求める表現を本文から2つ抜き出してください。",
            "a": "①Please let me know if there is an available date and time ... ②please let us know whether photography is permitted during the tour。"
        },
        {
            "q": "「he should be able to arrive by 2:30 p.m.」の should の働きは？",
            "a": "「〜のはずだ」という見込み・推量の should。断定を避けて控えめに伝える働きがあり、依頼メールの丁寧なトーンに合っている。"
        }
    ],
    "highlightPatterns": [
        "I am writing to ask whether it would be possible",
        "Could you also tell us what he should bring or prepare in advance?",
        "Please let me know if there is an available date and time",
        "please let us know whether photography is permitted",
        "Thank you very much for your time and consideration",
        "I look forward to hearing from you",
        "he would like to visit your factory to learn more",
        "He would like to take a few photos for his class report",
        "he should be able to arrive by 2:30 p.m."
    ],
    "highlightColor": "#f472b6",
    "highlightLabel": "丁寧な依頼"
}

fp4 = {
    "id": "fp4",
    "title": "受動態の応用（現在完了受動態 / be known as / be managed as）",
    "subtitle": "Advanced Passives with Prepositions",
    "explanation": "受動態は「be + 過去分詞」の形だけでなく、後ろに続く前置詞とセットで覚えることが重要。be known as（〜として知られる）、be managed as（〜として管理される）、be banned from（〜から締め出される）のように、as / from などの前置詞が意味を決める。また efforts have been made のような現在完了受動態は「（過去から今まで）ずっと〜されてきた」という継続のニュアンスを表す。",
    "sourceQuote": "In Bratislava, a central city in Slovakia, efforts have been made to create a child-friendly city through the “City for Children” program.",
    "sourceLocation": "大問2A 第1段落",
    "examples": [
        {
            "en": "Great efforts have been made to protect the forest from wildfires.",
            "ja": "山火事から森林を守るために多大な努力が払われてきた。",
            "note": "efforts have been made to V＝〜する努力がなされてきた（現在完了受動態で継続を表す）"
        },
        {
            "en": "This area is known as one of the best places to see wild birds.",
            "ja": "この地域は野鳥を見るのに最も良い場所の一つとして知られている。",
            "note": "be known as 〜＝〜として知られる（known to / known for との違いに注意）"
        },
        {
            "en": "The old castle is now managed as a national museum.",
            "ja": "その古い城は現在、国立博物館として管理されている。",
            "note": "be managed as 〜＝〜として管理・運営される"
        }
    ],
    "practicePassage": {
        "en": "[出典: Child-Friendly City]\nIn Bratislava, a central city in Slovakia, efforts have been made to create a child-friendly city through the “City for Children” program. Many schools were surrounded by dangers, and safety measures were taken as a trial. One successful example is Nevädzová Street, which used to be crowded with dozens of cars driven by parents trying to drop off children at school. Now, cars are banned from this street when children go to school. Instead, during the school arrival time from 7:30 to 8:00 a.m., children can walk to school on their own. In Bratislava, any idea is tested on a trial basis before being introduced permanently.",
        "ja": "スロバキアの中心都市ブラチスラバでは、「City for Children（子どものための都市）」プログラムを通じて、子どもに優しい都市をつくる取り組みが行われてきた。多くの学校が危険に囲まれており、試験的に安全対策が取られた。成功例の一つがネヴァヅォヴァー通りで、かつては学校に子どもを送り届けようとする親が運転する何十台もの車で混雑していた。現在では、子どもが登校する時間帯にはこの通りへの車の乗り入れが禁止されている。その代わり、午前7時30分から8時までの登校時間帯には、子どもたちは自分の足で歩いて学校に行くことができる。ブラチスラバでは、どんなアイデアも恒久的に導入される前に試験的に検証されるのだ。",
        "audioFile": "audio/practice_pp4.mp3"
    },
    "practiceQuestions": [
        {
            "q": "「efforts have been made to create a child-friendly city」の時制と意味を説明してください。",
            "a": "現在完了の受動態（have/has been + 過去分詞）。「（過去から現在まで）取り組みがなされてきた」という継続を表す。"
        },
        {
            "q": "受動態が使われている文を本文からさらに2つ抜き出してください。",
            "a": "例：Many schools were surrounded by dangers ／ safety measures were taken as a trial ／ cars are banned from this street ／ any idea is tested on a trial basis など。"
        },
        {
            "q": "「cars are banned from this street」の from の働きは？",
            "a": "ban A from B（AをBから締め出す）の受動形で、from が「どこから禁止されるか」を表す。be banned from ～＝～への立ち入り・使用を禁止される。"
        },
        {
            "q": "be known as と be managed as の as の意味を大問3Bの例で説明してください。",
            "a": "has been known as a hot spring resort（温泉リゾートとして知られてきた）、has been managed as a protected marine area（保護海域として管理されている）。いずれも as は「〜として」（資格・役割）。"
        }
    ],
    "highlightPatterns": [
        "efforts have been made to create a child-friendly city",
        "has been known as a hot spring resort",
        "has been managed as a protected marine area",
        "cars are banned from this street",
        "safety measures were taken as a trial",
        "any idea is tested on a trial basis",
        "Walls and roads in the water were seen clearly",
        "can be visited on foot"
    ],
    "highlightColor": "#fbbf24",
    "highlightLabel": "受動態の応用"
}

fp5 = {
    "id": "fp5",
    "title": "今回の重要なパラフレーズ",
    "subtitle": "Key Paraphrases in This Exam",
    "explanation": "正解の選択肢は本文の表現をそのまま使わず、別の語句で言い換えられる（パラフレーズ）。restore → recharge、gradually → slowly、the glass bottom of boats → special glass on a tour boat のように、動詞・副詞・名詞句レベルの言い換えに気づけるかが正答の鍵。本文を読むときは「この表現は選択肢でどう言い換えられそうか」を意識すると、根拠箇所を素早く特定できる。",
    "sourceQuote": "①create a fun place for them ← community areas where children can actively play together\n②experience the changes and give feedback ← Based on all the opinions and observations\n③classes finish later on other days ← ends at 2:00 p.m. on Fridays, which is earlier than on other days\n④recharge their energy ← restore their energy\n⑤slowly sink beneath the water ← sink underground gradually\n⑥special glass on a tour boat ← the glass bottom of boats",
    "sourceLocation": "大問2A・大問3A・大問3B",
    "examples": [
        {
            "en": "The library allows visitors to borrow up to ten books. → Visitors can take home as many as ten books.",
            "ja": "図書館は来館者が最大10冊借りることを認めている → 来館者は10冊まで家に持ち帰ることができる。",
            "note": "allow A to V ⇔ A can V の言い換え。主語の転換に注意"
        },
        {
            "en": "The event was put off because of the storm. → The event was postponed due to bad weather.",
            "ja": "嵐のためイベントは延期された（put off ⇔ postpone、because of ⇔ due to）。",
            "note": "句動詞 ⇔ 1語動詞の言い換えは頻出パターン"
        },
        {
            "en": "He restored his energy at the hot spring. → He recharged at the hot spring.",
            "ja": "彼は温泉で英気を養った（restore energy ⇔ recharge）。",
            "note": "本試験Q27と同じパターンの動詞言い換え"
        }
    ],
    "practicePassage": {
        "en": "[出典: The Lost City]\nCurrently, tourists can experience this underwater part of the city in various ways. Divers can explore the ancient Roman city in the water with guides. When the ocean is calm, visitors can see the structures in the water through the glass bottom of boats. In addition to the underwater sites, some ruins on land, such as dome-shaped public baths, can be visited on foot. Visiting Baia offers a rare chance to experience both ancient Roman history and the beauty of the sea in one place.",
        "ja": "現在、観光客はこの町の水中部分をさまざまな方法で体験できる。ダイバーはガイドと一緒に水中の古代ローマ都市を探検できる。海が穏やかなときは、訪問者は船のガラス底を通して水中の構造物を見ることができる。水中の遺跡に加えて、ドーム型の公衆浴場など、陸上に残るいくつかの遺跡も徒歩で訪れることができる。バイアを訪れることは、古代ローマの歴史と海の美しさの両方を一つの場所で体験できる貴重な機会を提供してくれる。",
        "audioFile": "audio/practice_pp5.mp3"
    },
    "practiceQuestions": [
        {
            "q": "「through the glass bottom of boats」はQ30の正解選択肢でどう言い換えられていましたか？",
            "a": "special glass on a tour boat。具体的な表現（船のガラス底）→ やや一般的な表現（ツアーボートの特殊なガラス）への言い換え。"
        },
        {
            "q": "「Divers can explore ... with guides」と食い違う誤答選択肢はどれでしたか？",
            "a": "Q30の選択肢1「diving freely in the area without a guide」。本文の with guides（ガイド付き）と矛盾するため誤答と判断できる。"
        },
        {
            "q": "「in various ways」は段落全体でどのように具体化されていますか？",
            "a": "①ガイド付きダイビング、②ガラス底の船からの見学、③徒歩での陸上遺跡見学、の3つの方法として具体化されている。"
        },
        {
            "q": "パラフレーズに気づきやすくなる本文の読み方を説明してください。",
            "a": "動詞・名詞句を「別の言い方でどう表せるか」を意識しながら読む。例：explore ⇔ visit、rare chance ⇔ special opportunity、restore energy ⇔ recharge など。"
        }
    ],
    "highlightPatterns": [
        "community areas where children can actively play together",
        "Based on all the opinions and observations",
        "which is earlier than on other days",
        "restore their energy",
        "sink underground gradually",
        "through the glass bottom of boats",
        "enjoyed parties, hot springs, and the warm climate"
    ],
    "highlightColor": "#f59e0b",
    "highlightLabel": "パラフレーズ"
}

with open(DATA_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

data["lessonPlan"] = {"focusPoints": [fp1, fp2, fp3, fp4, fp5]}

# highlightPatterns が本文に存在するか確認（fp の practicePassage 用語を除き passage 中心）
all_text = ""
for sec in data["sections"]:
    for q in sec.get("questions", []):
        all_text += q["text"] + " "
    for p in sec.get("passages", []):
        all_text += " ".join(p["paragraphs"]) + " "

missing = []
for fp in data["lessonPlan"]["focusPoints"]:
    for pat in fp["highlightPatterns"]:
        if pat not in all_text:
            missing.append(f"{fp['id']}: {pat}")

if missing:
    print("⚠ 本文に見つからないパターン:")
    for m in missing:
        print(" -", m)
    sys.exit(1)

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"✅ lessonPlan 保存完了: {DATA_PATH}")
for fp in data["lessonPlan"]["focusPoints"]:
    print(f"  {fp['id']}: {fp['title']} | patterns: {len(fp['highlightPatterns'])} | pq: {len(fp['practiceQuestions'])}")

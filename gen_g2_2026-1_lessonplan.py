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
        "en": "Coffee has a long and surprising history. It was not until the fifteenth century that people began roasting coffee beans to make a drink. Before that, the beans had been chewed or mixed with food for energy. It was not until coffee houses opened in big cities that drinking coffee became a social activity. These shops quickly became popular places to talk about news and business. In Europe, however, coffee only became common after traders brought large amounts of beans from overseas. Today, it is hard to imagine mornings without it.",
        "ja": "コーヒーには長く驚くべき歴史がある。人々がコーヒー豆を焙煎して飲み物を作り始めたのは、15世紀になってからのことだった。それ以前は、豆はエネルギー源としてかまれたり食べ物に混ぜられたりしていた。コーヒーを飲むことが社交的な活動になったのは、大都市にコーヒーハウスが開店してからだった。これらの店はすぐに、ニュースやビジネスについて語り合う人気の場所になった。しかしヨーロッパでは、貿易商が海外から大量の豆を持ち込んで初めてコーヒーは一般的になった。今日では、コーヒーのない朝は想像しがたい。"
    },
    "practiceQuestions": [
        {
            "q": "「It was not until the fifteenth century that people began roasting coffee beans」を文法的に分析してください。",
            "a": "It was not until + 時期 + that S + V の強調構文。「15世紀になって初めて人々は豆を焙煎し始めた」。通常文 People did not begin roasting ... until the fifteenth century の強調形。"
        },
        {
            "q": "本文中で「コーヒーを飲むことが社交活動になった」きっかけは何ですか？",
            "a": "大都市でコーヒーハウスが開店したこと。It was not until coffee houses opened ... that の構文で「開店して初めて」と強調されている。"
        },
        {
            "q": "「coffee only became common after traders brought large amounts of beans」を not until を使って書き換えてください。",
            "a": "Coffee did not become common until traders brought large amounts of beans from overseas.（only after ≒ not until）"
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
        "en": "Last month, our school invited a musician who plays the theremin, or an electronic instrument that is played without being touched. The inventor, a Russian scientist named Leon Theremin, created it about one hundred years ago. The player moves his or her hands near two antennas, or metal rods, to control the sound. Many movie directors have used its mysterious sound in films, such as science fiction and horror movies. Some modern bands, such as rock and pop groups, also use it on stage. The students were amazed by the instrument, a strange but beautiful invention.",
        "ja": "先月、私たちの学校はテルミン、つまり触れずに演奏する電子楽器を演奏する音楽家を招いた。発明者であるレオン・テルミンというロシアの科学者が、約100年前にそれを作った。奏者は2本のアンテナ、つまり金属の棒の近くで手を動かして音を制御する。多くの映画監督が、SFやホラー映画などの映画でその神秘的な音を使ってきた。ロックやポップグループなどの現代のバンドの中にも、ステージでそれを使うものがある。生徒たちは、奇妙だが美しい発明品であるその楽器に驚嘆した。"
    },
    "practiceQuestions": [
        {
            "q": "「the theremin, or an electronic instrument that is played without being touched」の or の働きを説明してください。",
            "a": "言い換え（同格）の or。「テルミン、つまり〜な電子楽器」と直前の語を定義している。選択の「または」ではない点に注意。"
        },
        {
            "q": "「The inventor, a Russian scientist named Leon Theremin,」の文法構造は？",
            "a": "カンマによる同格。The inventor ＝ a Russian scientist named Leon Theremin で、直前の名詞に説明を加えている。"
        },
        {
            "q": "本文中の such as は何の例を挙げていますか？2つ答えてください。",
            "a": "①films の例として science fiction and horror movies、②modern bands の例として rock and pop groups。"
        },
        {
            "q": "「two antennas, or metal rods」を日本語にしてください。",
            "a": "「2本のアンテナ、つまり金属の棒」。or が直前の語をやさしく言い換えている。"
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
        "en": "Dear Ms. Carter, My name is Daniel Reed, and I am a high school student in your city. I am writing to ask whether it would be possible for me to work as a volunteer at the city library this summer. I am available on weekday afternoons, and I could help with returning books to the shelves or reading stories to children. Could you tell me what I should do to apply for the position? Also, please let me know whether there is an age limit for volunteers. Thank you very much for your time, and I look forward to hearing from you.",
        "ja": "カーター様。私はダニエル・リードと申しまして、市内の高校に通う生徒です。この夏、市立図書館でボランティアとして働くことが可能かどうかお尋ねしたく、ご連絡しております。平日の午後に時間があり、本を棚に戻す作業や子どもへの読み聞かせのお手伝いができます。応募するには何をすべきか教えていただけますか。また、ボランティアに年齢制限があるかどうかもお知らせください。お時間をいただきありがとうございます。お返事をお待ちしております。"
    },
    "practiceQuestions": [
        {
            "q": "「I am writing to ask whether it would be possible for me to work as a volunteer」の構造を分析してください。",
            "a": "I am writing to ask（ご連絡している目的）+ whether 名詞節（〜かどうか）+ it would be possible for A to V（形式主語 it ＋ 意味上の主語 for A）。would で婉曲・丁寧さを出している。"
        },
        {
            "q": "Could you tell me what I should do to apply ...? が Can you ...? より丁寧なのはなぜですか？",
            "a": "could は仮定法由来の婉曲表現で、相手への要求の直接性を弱めるため。さらに疑問詞節（what I should do）を使う間接疑問で表現が柔らかくなっている。"
        },
        {
            "q": "返信を求める表現を本文から2つ抜き出してください。",
            "a": "①Could you tell me what I should do to apply for the position? ②please let me know whether there is an age limit for volunteers."
        },
        {
            "q": "「I look forward to hearing from you」の to は不定詞の to ですか？",
            "a": "いいえ、前置詞。look forward to + 名詞/動名詞で「〜を楽しみに待つ」。to の後は動名詞 hearing になる点に注意。"
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
        "en": "The old lighthouse on Cape Verde Island has been praised for its unique design. It was built in 1885 and has been known as a symbol of the island ever since. For over a century, ships were guided safely to the harbor by its strong light. In 1990, the lighthouse was closed because modern technology was introduced. However, it was not torn down. Instead, the building has been managed as a small museum by local volunteers. Today, visitors are welcomed by friendly guides, and the lighthouse is loved as a popular spot for watching the sunset.",
        "ja": "ケープベルデ島の古い灯台は、その独特なデザインで称賛されてきた。それは1885年に建てられ、それ以来この島のシンボルとして知られてきた。1世紀以上にわたり、船はその強い光によって安全に港へ導かれた。1990年、近代的な技術が導入されたため灯台は閉鎖された。しかし、取り壊されることはなかった。その代わり、建物は地元のボランティアによって小さな博物館として管理されている。今日、訪問者は親切なガイドに迎えられ、灯台は夕日を眺める人気スポットとして愛されている。"
    },
    "practiceQuestions": [
        {
            "q": "「has been praised for its unique design」の時制と意味を説明してください。",
            "a": "現在完了の受動態（have/has been + 過去分詞）。「（過去から現在まで）独特なデザインで称賛されてきた」。for が称賛の理由を表す。"
        },
        {
            "q": "be known as と be known for の違いは何ですか？",
            "a": "be known as 〜は「〜として知られる」（肩書き・呼び名）、be known for 〜は「〜で知られる」（有名な理由）。本文の known as a symbol は「シンボルとして」。"
        },
        {
            "q": "「the building has been managed as a small museum by local volunteers」の as と by の働きは？",
            "a": "as 〜＝「〜として」（管理のされ方）、by 〜＝動作主（誰によって管理されているか）。"
        },
        {
            "q": "受動態が使われている文を本文からさらに2つ抜き出してください。",
            "a": "例：ships were guided safely to the harbor ／ the lighthouse was closed ／ visitors are welcomed ／ the lighthouse is loved など。"
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
        "en": "The city of Greenhill opened a new park last month. The park was designed to give families a safe place to spend time together. Children can play on the wooden playground, and adults can relax in the rose garden. The city also planted more than two hundred trees to make the air cleaner. On weekends, free yoga classes are held near the fountain. City officials say the park has already attracted thousands of visitors. They hope it will encourage more people to spend time outdoors.",
        "ja": "グリーンヒル市は先月、新しい公園を開園した。その公園は家族が一緒に安全に過ごせる場所を提供するために設計された。子どもは木製の遊び場で遊ぶことができ、大人はバラ園でくつろぐことができる。市はまた、空気をよりきれいにするために200本以上の木を植えた。週末には噴水の近くで無料のヨガ教室が開かれる。市の職員によれば、公園はすでに何千人もの訪問者を引きつけているという。彼らは、公園がより多くの人々に屋外で過ごすことを促すと期待している。"
    },
    "practiceQuestions": [
        {
            "q": "「a safe place to spend time together」を選択肢風に言い換えると？",
            "a": "例：a secure area where families can enjoy time with each other。safe ⇔ secure、spend time ⇔ enjoy time のような言い換えが可能。"
        },
        {
            "q": "「to make the air cleaner」のパラフレーズとして適切な表現は？",
            "a": "to improve air quality（空気の質を改善するため）。make + O + 比較級 ⇔ improve の言い換え。"
        },
        {
            "q": "「has already attracted thousands of visitors」を言い換えてください。",
            "a": "例：many people have already come to the park。attract visitors ⇔ people come の主語転換型パラフレーズ。"
        },
        {
            "q": "本試験Q30で「the glass bottom of boats」はどう言い換えられていましたか？",
            "a": "special glass on a tour boat。具体的な表現（船のガラス底）→ やや一般的な表現（ツアーボートの特殊なガラス）への言い換え。"
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

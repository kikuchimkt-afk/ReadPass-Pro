# -*- coding: utf-8 -*-
"""
2026年度 第1回（土曜準会場）英検準2級プラス data.json
Step C: 大問3（reading-comprehension型）Q24〜31
  3A Dog Sitting Email / 3B Avocado Production
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade-pre2plus", "2026-1-sat", "data.json",
)

# --- 3A: Email（ドッグシッター依頼への返信） ---
p3a_paras = [
    "Dear Cooper,",
    "My name is Emma Lawrence. Thank you for your email. I understand you are looking for someone to look after your dog while on a family trip during the school holidays. I am happy to tell you I am available on the dates you mentioned. I used to work as an animal doctor and have five years of experience as a dog sitter. I am confident that your dog will feel safe and comfortable with me.",
    "My services usually include feeding dogs the food you provide, giving them water, and offering snacks if necessary. I take dogs for walks twice a day, for about an hour, and spend time playing with them. I also provide a comfortable place to sleep. However, I cannot prepare dog food, so I ask dog owners to bring their food. Please let me know if there is anything I should know about your dog, such as any health problems.",
    "The daily fee is $50. I will be looking after your dog for three days, so the total will be $150. Payment is required before the service. Since you are under eighteen, please speak with your parents about my services, including the fee. Please respond by June 22 if you wish to use my services. I look forward to hearing from you.",
    "Thank you,\nEmma Lawrence",
]

p3a_trans = [
    "クーパーへ",
    "エマ・ローレンスです。メールありがとうございます。学校の休み中の家族旅行の間、犬の世話をしてくれる人を探しているとのこと、承知しました。ご指定の日程で対応可能です。以前は動物の医者として働いており、ドッグシッターとして5年の経験があります。あなたの犬は私と一緒に安全で快適に過ごせると確信しています。",
    "私のサービスには、通常、飼い主が用意するフードを与えること、水を与えること、必要ならおやつを与えることが含まれます。1日2回、約1時間散歩に連れて行き、遊ぶ時間も設けます。快適な寝る場所も提供します。ただし、私は犬用のフードを調理できないため、飼い主の方にフードを持参していただいています。健康上の問題など、犬について知っておくべきことがあれば教えてください。",
    "1日の料金は50ドルです。3日間お世話するので、合計150ドルになります。サービス前の支払いが必要です。18歳未満の方ですので、料金を含めた私のサービスについて保護者の方と話し合ってください。サービスを利用したい場合は6月22日までにご返信ください。お返事をお待ちしています。",
    "ありがとうございます。\nエマ・ローレンス",
]

p3a_pairs = [
    [
        "I understand you are looking for someone to look after your dog while on a family trip during the school holidays.",
        "学校の休み中の家族旅行の間、犬の世話をしてくれる人を探しているとのこと、承知しました。",
    ],
    [
        "I used to work as an animal doctor and have five years of experience as a dog sitter.",
        "以前は動物の医者として働いており、ドッグシッターとして5年の経験があります。",
    ],
    [
        "However, I cannot prepare dog food, so I ask dog owners to bring their food.",
        "ただし、私は犬用のフードを調理できないため、飼い主の方にフードを持参していただいています。",
    ],
    [
        "Please let me know if there is anything I should know about your dog, such as any health problems.",
        "健康上の問題など、犬について知っておくべきことがあれば教えてください。",
    ],
    [
        "Since you are under eighteen, please speak with your parents about my services, including the fee.",
        "18歳未満の方ですので、料金を含めた私のサービスについて保護者の方と話し合ってください。",
    ],
    [
        "Please respond by June 22 if you wish to use my services.",
        "サービスを利用したい場合は6月22日までにご返信ください。",
    ],
]

# --- 3B: Avocado Production ---
p3b_paras = [
    "Today, many people are more concerned about their health than before. Therefore, foods that are considered healthy are gaining attention. Avocados have been a popular food in many countries around the world. Their health value is especially attractive to people whose diets are based on plants. For example, they contain high amounts of healthy fats, which are better than other kinds of fats found in meat. According to researchers, they can also help reduce the risk of heart disease.",
    "Especially in many European countries and the United States, the number of people eating avocados has increased. Because these countries import a lot of avocados, they are responsible for a large part of the global avocado market. In Europe, countries like France and the United Kingdom have already experienced high demand. However, there is still room for the avocado market to grow in Italy and Eastern European countries, where the market is smaller. In other words, the avocado market in Europe could continue to grow.",
    "However, there are several problems with avocado production due to its increasing demand. For example, because the production requires a lot of water, increased demand puts pressure on water resources. This has created water shortage problems in production areas. Also, the mass production of avocados sometimes causes too much supply, which can lead to reduced prices for avocados. This means that avocado farmers may earn less money and find it harder to continue their business.",
    "To help solve these problems, consumers can choose to buy avocados with the FAIRTRADE Mark. This system was introduced to the avocado industry in 2010. The mark means the avocados are produced in an eco-friendly way and that the farmers receive a fair amount of money. Also, these farmers receive extra money that can be used for their businesses or community projects to protect the environment. In this way, the avocado industry is working to create better working conditions and promote responsible farming for the future.",
]

p3b_trans = [
    "今日、多くの人が以前よりも健康に関心を持っています。そのため、健康的とみなされる食品が注目を集めています。アボカドは世界中の多くの国で人気のある食品です。その健康価値は、特に植物中心の食生活を送る人々にとって魅力的です。例えば、アボカドには健康的な脂肪が多く含まれており、肉に含まれる他の種類の脂肪よりも優れています。研究者によると、心臓病のリスクを減らすのにも役立つとされています。",
    "特に多くのヨーロッパ諸国とアメリカでは、アボカドを食べる人の数が増えています。これらの国は大量にアボカドを輸入しているため、世界のアボカド市場の大きな部分を占めています。ヨーロッパでは、フランスやイギリスのような国はすでに高い需要を経験しています。しかし、市場が小さいイタリアや東欧諸国では、アボカド市場が成長する余地がまだあります。言い換えれば、ヨーロッパのアボカド市場は今後も成長し続ける可能性があります。",
    "しかし、需要の増加により、アボカド生産にはいくつかの問題があります。例えば、生産には多くの水が必要なため、需要の増加は水資源に圧力をかけます。これにより、生産地域で水不足の問題が生じています。また、アボカドの大量生産は供給過多を引き起こすことがあり、アボカドの価格下落につながることがあります。つまり、アボカド農家は収入が減り、事業を続けるのが難しくなる可能性があります。",
    "これらの問題を解決するために、消費者はFAIRTRADEマークの付いたアボカドを選ぶことができます。この制度は2010年にアボカド産業に導入されました。このマークは、アボカドが環境に配慮した方法で生産され、農家が公正な金額を受け取ることを意味します。また、これらの農家は、事業や環境保護のための地域プロジェクトに使える追加の資金を受け取ります。このように、アボカド産業はより良い労働条件の創出と、将来に向けた責任ある農業の推進に取り組んでいます。",
]

p3b_pairs = [
    [
        "For example, they contain high amounts of healthy fats, which are better than other kinds of fats found in meat.",
        "例えば、アボカドには健康的な脂肪が多く含まれており、肉に含まれる他の種類の脂肪よりも優れています。",
    ],
    [
        "Especially in many European countries and the United States, the number of people eating avocados has increased.",
        "特に多くのヨーロッパ諸国とアメリカでは、アボカドを食べる人の数が増えています。",
    ],
    [
        "However, there is still room for the avocado market to grow in Italy and Eastern European countries, where the market is smaller.",
        "しかし、市場が小さいイタリアや東欧諸国では、アボカド市場が成長する余地がまだあります。",
    ],
    [
        "because the production requires a lot of water, increased demand puts pressure on water resources.",
        "生産には多くの水が必要なため、需要の増加は水資源に圧力をかけます。",
    ],
    [
        "the mass production of avocados sometimes causes too much supply, which can lead to reduced prices for avocados.",
        "アボカドの大量生産は供給過多を引き起こすことがあり、アボカドの価格下落につながることがあります。",
    ],
    [
        "This means that avocado farmers may earn less money and find it harder to continue their business.",
        "つまり、アボカド農家は収入が減り、事業を続けるのが難しくなる可能性があります。",
    ],
    [
        "The mark means the avocados are produced in an eco-friendly way and that the farmers receive a fair amount of money.",
        "このマークは、アボカドが環境に配慮した方法で生産され、農家が公正な金額を受け取ることを意味します。",
    ],
    [
        "these farmers receive extra money that can be used for their businesses or community projects to protect the environment.",
        "これらの農家は、事業や環境保護のための地域プロジェクトに使える追加の資金を受け取ります。",
    ],
]

section3 = {
    "name": "大問3",
    "nameEn": "Part 3",
    "type": "reading-comprehension",
    "instruction": "次の英文A，Bの内容に関して，(24)から(31)までの質問に対して最も適切なもの，または文を完成させるのに最も適切なものを1，2，3，4の中から一つ選び，その番号を解答用紙の所定欄にマークしなさい。",
    "passages": [
        {
            "label": "A",
            "title": "Dog Sitting Email",
            "format": "email",
            "meta": {
                "from": "Emma Lawrence <contact@el-service.net>",
                "to": "Cooper Jenkins <cooper.w.jenkins@connet-globally.com>",
                "date": "June 20",
                "subject": "Service information",
            },
            "paragraphs": p3a_paras,
            "translations": p3a_trans,
            "sentencePairs": p3a_pairs,
            "questions": [
                {
                    "number": 24,
                    "question": "Why did Cooper Jenkins contact Emma Lawrence at first?",
                    "questionTranslation": "クーパー・ジェンキンスが最初にエマ・ローレンスに連絡したのはなぜか？",
                    "choices": [
                        "To receive advice from an animal doctor.",
                        "To know how to become a good dog sitter.",
                        "To ask if he can take his dog on his trip.",
                        "To request her service to care for his dog.",
                    ],
                    "choiceTranslations": [
                        "動物の医者からアドバイスを受けるため。",
                        "良いドッグシッターになる方法を知るため。",
                        "旅行に犬を連れて行けるか尋ねるため。",
                        "犬の世話を依頼するため。",
                    ],
                    "answer": 4,
                    "choiceAnalysis": [
                        "❌ To receive advice from an animal doctor＝動物の医者からのアドバイス。looking for someone to look after your dog（犬の世話を依頼）が主題で、治療相談ではない",
                        "❌ To know how to become a good dog sitter＝ドッグシッターになる方法。you are looking for someone to look after your dog（サービスを探している）話で、資格取得の相談ではない",
                        "❌ 旅行に犬を連れて行けるか→while on a family trip の間に世話を頼む話。犬を連れて行く話ではない",
                        "✅ 犬の世話を依頼するため→正解。💡 looking for someone to look after your dog while on a family trip が直接の根拠",
                    ],
                    "sourceEvidence": [
                        "you are looking for someone to look after your dog while on a family trip during the school holidays",
                    ],
                    "grammar": "💡 look after ～＝～の世話をする。while on a trip＝旅行中に。メール冒頭の I understand you are looking for ... が問いの核心。",
                },
                {
                    "number": 25,
                    "question": "In the email, Emma tells Cooper that",
                    "questionTranslation": "メールの中で、エマはクーパーに（　）と伝えている。",
                    "choices": [
                        "she wants to understand his dog's sleeping habits.",
                        "she needs to know how often she should walk his dog.",
                        "she cannot provide food for his dog on her own.",
                        "she cannot welcome his dog if it has health problems.",
                    ],
                    "choiceTranslations": [
                        "犬の睡眠の習慣を理解したい。",
                        "どのくらいの頻度で散歩すべきか知る必要がある。",
                        "自分では犬のフードを用意できない。",
                        "健康上の問題がある犬は受け入れられない。",
                    ],
                    "answer": 3,
                    "choiceAnalysis": [
                        "❌ 睡眠の習慣→comfortable place to sleep（寝場所）は提供するが、習慣を「理解したい」とは書いていない",
                        "❌ she needs to know how often she should walk his dog＝散歩の頻度を尋ねる。I will take your dog for a walk twice a day（1日2回散歩する）とサービス内容として述べており、頻度を聞いているのではない",
                        "✅ 自分ではフードを用意できない→正解。💡 I cannot prepare dog food, so I ask dog owners to bring their food",
                        "❌ 健康問題があると受け入れない→Please let me know ... such as any health problems は「知らせてほしい」であり拒否ではない",
                    ],
                    "sourceEvidence": [
                        "I cannot prepare dog food, so I ask dog owners to bring their food",
                    ],
                    "grammar": "💡 cannot prepare ... so I ask ... to bring＝～を用意できないので持参をお願いする。However が注意を引く接続詞。",
                },
                {
                    "number": 26,
                    "question": "What does Emma ask Cooper to do?",
                    "questionTranslation": "エマはクーパーに何をするよう求めているか？",
                    "choices": [
                        "Talk to his parents about the services and cost.",
                        "Pay the service fee to her by June 22.",
                        "Send her $50 in advance of the service.",
                        "Reply to her in a week for an appointment.",
                    ],
                    "choiceTranslations": [
                        "サービスと料金について保護者と話し合う。",
                        "6月22日までにサービス料を支払う。",
                        "サービス前に50ドルを送る。",
                        "予約のために1週間以内に返信する。",
                    ],
                    "answer": 1,
                    "choiceAnalysis": [
                        "✅ 保護者と話し合う→正解。💡 Since you are under eighteen, please speak with your parents about my services, including the fee",
                        "❌ 6月22日までに支払い→June 22は返信の期限。Payment is required before the service（サービス前の支払い）と別",
                        "❌ Send her $50 in advance of the service＝50ドルを送る。The fee is $50 per day, and the total for three days is $150（1日50ドル、3日で合計150ドル）であり、50ドルだけの話ではない",
                        "❌ Reply to her in a week for an appointment＝1週間以内に返信。I would appreciate it if you could reply by June 22（6月22日までに返信）と具体的な日付で、1週間とは書いていない",
                    ],
                    "sourceEvidence": [
                        "please speak with your parents about my services, including the fee",
                    ],
                    "grammar": "💡 speak with your parents about ～＝保護者と～について話し合う。including the fee＝料金を含めて。under eighteen＝18歳未満。",
                },
            ],
        },
        {
            "label": "B",
            "title": "Avocado Production",
            "paragraphs": p3b_paras,
            "translations": p3b_trans,
            "sentencePairs": p3b_pairs,
            "questions": [
                {
                    "number": 27,
                    "question": "One reason that avocados are gaining attention is that",
                    "questionTranslation": "アボカドが注目を集めている理由の一つは（　）ことである。",
                    "choices": [
                        "eating too many of them can increase the risk of heart disease.",
                        "they provide fats that are considered healthier than fats in meat.",
                        "more people are choosing to be vegetarians to lose weight.",
                        "there is zero fat to be found in them, unlike meat.",
                    ],
                    "choiceTranslations": [
                        "食べ過ぎると心臓病のリスクが高まる。",
                        "肉の脂肪より健康的とみなされる脂肪を提供する。",
                        "減量のためにベジタリアンになる人が増えている。",
                        "肉と違い脂肪がゼロである。",
                    ],
                    "answer": 2,
                    "choiceAnalysis": [
                        "❌ 心臓病リスクが高まる→reduce the risk of heart disease（リスクを減らす）と正反対",
                        "✅ 肉より健康的な脂肪→正解。💡 healthy fats, which are better than other kinds of fats found in meat",
                        "❌ ベジタリアンになる人が増加→diets are based on plants（植物中心の食事）の話はあるが、減量や増加の記述はない",
                        "❌ 脂肪ゼロ→high amounts of healthy fats（健康的な脂肪が多い）と矛盾",
                    ],
                    "sourceEvidence": [
                        "they contain high amounts of healthy fats, which are better than other kinds of fats found in meat",
                    ],
                    "grammar": "💡 which are better than ～＝～より優れている（関係代名詞の非制限用法）。reduce the risk of ～＝～のリスクを減らす。",
                },
                {
                    "number": 28,
                    "question": "What is the situation surrounding avocados in Europe?",
                    "questionTranslation": "ヨーロッパにおけるアボカドの状況について正しいのはどれか？",
                    "choices": [
                        "Some countries, like the United Kingdom, have stopped importing avocados.",
                        "Many European countries rely on the United States to import avocados.",
                        "The custom of eating avocados will probably spread to France in the future.",
                        "Italy and Eastern European countries will be key to expanding the avocado market in Europe.",
                    ],
                    "choiceTranslations": [
                        "イギリスなど一部の国はアボカドの輸入をやめた。",
                        "多くのヨーロッパ諸国はアメリカに輸入を依存している。",
                        "アボカドを食べる習慣は将来フランスに広がるだろう。",
                        "イタリアと東欧諸国がヨーロッパ市場拡大の鍵になる。",
                    ],
                    "answer": 4,
                    "choiceAnalysis": [
                        "❌ 輸入をやめた→イギリスはすでに高い需要（high demand）があると述べられている",
                        "❌ Many European countries rely on the United States to import avocados＝アメリカに輸入依存。European countries and the United States ... the number of people eating avocados has increased（ともに消費が増えた）と並列で、依存の記述はない",
                        "❌ 将来フランスに広がる→フランスはすでに高い需要を経験（already experienced high demand）",
                        "✅ イタリアと東欧が鍵→正解。💡 still room for the avocado market to grow in Italy and Eastern European countries",
                    ],
                    "sourceEvidence": [
                        "there is still room for the avocado market to grow in Italy and Eastern European countries, where the market is smaller",
                    ],
                    "grammar": "💡 there is still room for ～ to grow＝～が成長する余地がまだある。In other words＝言い換えれば（要約の合図）。",
                },
                {
                    "number": 29,
                    "question": "What is one of the problems with avocado production?",
                    "questionTranslation": "アボカド生産の問題の一つは何か？",
                    "choices": [
                        "Avocado producers limit their supply to maintain a high price.",
                        "Increased demand for avocados has caused labor shortages.",
                        "Many avocado farmers produce avocados in a way that is against the law.",
                        "Avocado prices fall if the supply is too high, reducing farmers' income.",
                    ],
                    "choiceTranslations": [
                        "生産者は高値を維持するため供給を制限している。",
                        "需要増加により労働力不足が起きている。",
                        "多くの農家が違法な方法で生産している。",
                        "供給過多で価格が下がり、農家の収入が減る。",
                    ],
                    "answer": 4,
                    "choiceAnalysis": [
                        "❌ 供給を制限→too much supply（供給過多）の問題が述べられており正反対",
                        "❌ Increased demand for avocados has caused labor shortages＝労働力不足。too much supply, which can lead to reduced prices（供給過多で価格下落）が論点で、labor の記述は出てこない",
                        "❌ 違法な生産→against the law の記述はない",
                        "✅ 供給過多で価格下落・収入減→正解。💡 too much supply → reduced prices → farmers may earn less money",
                    ],
                    "sourceEvidence": [
                        "the mass production of avocados sometimes causes too much supply, which can lead to reduced prices for avocados",
                        "avocado farmers may earn less money and find it harder to continue their business",
                    ],
                    "grammar": "💡 lead to ～＝～につながる。This means that ～＝つまり～ということだ（結果の言い換え）。",
                },
                {
                    "number": 30,
                    "question": "What is true about the system using the FAIRTRADE Mark in the avocado industry?",
                    "questionTranslation": "アボカド産業におけるFAIRTRADEマークの制度について正しいのはどれか？",
                    "choices": [
                        "It ensures all avocados are sold only in local, eco-friendly markets.",
                        "It provides the community with money if farmers use modern farming tools.",
                        "It focuses mainly on reducing avocado prices in the international market.",
                        "It allows farmers to earn fair pay and spend it on environmental protection.",
                    ],
                    "choiceTranslations": [
                        "すべてのアボカドが地元の環境配慮型市場でのみ販売される。",
                        "農家が最新の農具を使えば地域に資金が提供される。",
                        "国際市場でのアボカド価格の引き下げに主に焦点を当てている。",
                        "農家が公正な報酬を得て、環境保護に使える。",
                    ],
                    "answer": 4,
                    "choiceAnalysis": [
                        "❌ 地元市場でのみ販売→sold only in local markets の記述はない",
                        "❌ 最新の農具→modern farming tools ではなく community projects to protect the environment",
                        "❌ 価格の引き下げ→fair amount of money（公正な金額）を受け取る話。安売りではない",
                        "✅ 公正な報酬と環境保護への支出→正解。💡 receive a fair amount of money ＋ extra money ... to protect the environment",
                    ],
                    "sourceEvidence": [
                        "the farmers receive a fair amount of money",
                        "extra money that can be used for their businesses or community projects to protect the environment",
                    ],
                    "grammar": "💡 eco-friendly＝環境に配慮した。fair amount of money＝公正な金額。be used for ～＝～に使われる。",
                },
                {
                    "number": 31,
                    "question": "What do we learn from the passage?",
                    "questionTranslation": "本文からわかることはどれか？",
                    "choices": [
                        "The production of avocados helps solve water shortage problems.",
                        "The United States is a major consumer in the avocado market.",
                        "Avocados are especially popular among people who love meat.",
                        "The FAIRTRADE Mark is no longer working out for avocado farmers.",
                    ],
                    "choiceTranslations": [
                        "アボカド生産は水不足問題の解決に役立つ。",
                        "アメリカはアボカド市場の主要な消費国である。",
                        "アボカドは肉好きの人々に特に人気がある。",
                        "FAIRTRADEマークはもはや農家にとってうまく機能していない。",
                    ],
                    "answer": 2,
                    "choiceAnalysis": [
                        "❌ 水不足の解決→water shortage problems in production areas（生産地域で水不足）と矛盾",
                        "✅ アメリカは主要な消費国→正解。💡 European countries and the United States ... number of people eating avocados has increased ＋ large part of the global avocado market",
                        "❌ 肉好きの人々→diets are based on plants（植物中心の食事）の人々に魅力的と述べている",
                        "❌ もはや機能しない→working to create better working conditions and promote responsible farming for the future と正反対",
                    ],
                    "sourceEvidence": [
                        "Especially in many European countries and the United States, the number of people eating avocados has increased",
                        "they are responsible for a large part of the global avocado market",
                    ],
                    "grammar": "💡 be responsible for ～＝～の原因・担い手である。What do we learn from the passage?＝本文全体の要点を問う総合問題。",
                },
            ],
        },
    ],
}

with open(DATA_PATH, encoding="utf-8") as f:
    data = json.load(f)

sections = data.get("sections", [])
s1 = sections[0] if sections and sections[0].get("name") == "大問1" else None
s2 = sections[1] if len(sections) >= 2 and sections[1].get("name") == "大問2" else None
if s1 and s2:
    data["sections"] = [s1, s2, section3]
elif s1:
    data["sections"] = [s1, section3]
else:
    data["sections"] = [section3]

errors = []
for pa in section3["passages"]:
    text = " ".join(pa["paragraphs"])
    for pair in pa["sentencePairs"]:
        if pair[0] not in text:
            errors.append(f"NOT FOUND in '{pa['title']}': {pair[0][:60]}")

if errors:
    print("sentencePairs エラー:")
    for e in errors:
        print(" -", e)
    sys.exit(1)

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

q_count = sum(len(pa["questions"]) for pa in section3["passages"])
print(f"Wrote section3 ({q_count} questions, 2 passages) to {DATA_PATH}")

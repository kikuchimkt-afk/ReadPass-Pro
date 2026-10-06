# -*- coding: utf-8 -*-
"""Image-verified original passages plus the four-field teaching translations.

Each row contains natural Japanese, the main finite verb phrase, and bilingual
reading units. English paragraphs and sentencePairs are derived from these same
units so punctuation/abbreviations cannot be broken by automatic segmentation.
"""


def passage(label, title, blocks, **extra):
    paragraphs, translations, pairs = [], [], []
    for block in blocks:
        english, japanese = [], []
        for ja, verb, slash in block:
            en = " ".join(unit.split("|", 1)[0] for unit in slash.split("||"))
            pairs.append([en, ja, slash, verb])
            english.append(en)
            japanese.append(ja)
        paragraphs.append(" ".join(english))
        translations.append("".join(japanese))
    return dict(label=label, title=title, paragraphs=paragraphs,
                translations=translations, sentencePairs=pairs, questions=[], **extra)


HONEY = passage("A", "Honeybees", [
    [
        ("アメリカのある大学の専門家たちは、ミツバチの動きを追跡するための ( 18 ) を開発した。", "have developed", "Experts from a university in the United States|アメリカのある大学の専門家たちは||have developed ( 18 )|（18）を開発した||to track the movements of honeybees.|ミツバチの動きを追跡するために"),
        ("彼らは飛行パターンを記録するために、3万匹以上のミツバチの背中に小さなQRコードを付けた。", "put", "They put small QR codes|彼らは小さなQRコードを付けた||on the backs of more than 30,000 honeybees|3万匹以上のミツバチの背中に||to record their flight patterns.|飛行パターンを記録するために"),
        ("また、ミツバチのすむ場所に、コードを読み取るカメラを備えたセンサーを設置した。", "placed", "They also placed sensors|またセンサーを設置した||with a camera for scanning the codes|コードを読み取るカメラを備えた||at places where bees live.|ミツバチがすむ場所に"),
        ("これにより、ミツバチがいつ、どのくらい遠くまで飛ぶのかについてのデータを集められた。", "allowed", "This allowed them to collect data|これによって彼らはデータを集められた||on when and how far the honeybees fly.|ミツバチがいつ、どのくらい遠くまで飛ぶのかについて"),
        ("さらに、丸1週間、1日24時間にわたってミツバチの行動を観察できた。", "were", "They were also able to observe honeybees' behavior|さらにミツバチの行動を観察できた||twenty-four hours a day|1日24時間||for a whole week.|丸1週間にわたって"),
    ], [
        ("この研究を通じて、驚くべき発見があった。", "was made", "A surprising finding was made|驚くべき発見があった||through this study.|この研究を通じて"),
        ("専門家たちは、若いミツバチに ( 19 ) 追跡タグを付けた。", "placed", "The experts placed tracking tags|専門家たちは追跡タグを付けた||on young honeybees ( 19 ).|若いミツバチに（19）"),
        ("これによって、以前よりもずっと長い期間、その行動を観察できた。", "allowed", "This allowed them to observe their behavior|これによってその行動を観察できた||for a much longer period than before.|以前よりもずっと長い期間"),
        ("ミツバチは長くても約28日しか生きないと、長い間考えられてきた。", "has long been believed", "It has long been believed|長い間考えられてきた||that honeybees live up to about twenty-eight days.|ミツバチは長くても約28日生きると"),
        ("しかし、蜜を集める行動から、ミツバチが約6週間、活動を続けていたことがわかった。", "discovered", "However, they discovered|しかし彼らは発見した||that honeybees stayed active for about six weeks|ミツバチが約6週間活動を続けていたことを||through their honey-collecting behavior.|蜜を集める行動を通して"),
        ("これは、ミツバチが当初考えられていたよりもずっと長く生きたことを示していた。", "showed", "This showed|これは示していた||that honeybees lived much longer|ミツバチがずっと長く生きたことを||than originally thought.|当初考えられていたよりも"),
    ], [
        ("もう一つの興味深い発見は、ミツバチの飛行についてだった。", "was", "Another interesting finding|もう一つの興味深い発見は||was about their flights.|その飛行についてだった"),
        ("ミツバチは巣から最大10キロメートルまで飛ぶと人々は考えているが、データではそこまで遠くには飛んでいなかった。", "showed", "Although people believe|人々は考えているが||honeybees fly up to ten kilometers from their homes,|ミツバチは巣から最大10キロメートルまで飛ぶと||the data showed|データは示した||they did not fly that far.|そこまで遠くには飛ばなかったと"),
        ("研究対象のミツバチの大半は、1回に数分しか飛ばなかった。", "flew", "Most honeybees in the study|研究対象のミツバチの大半は||flew only a few minutes at a time.|1回に数分しか飛ばなかった"),
        ("これは、巣の近くに十分な食べ物があれば、遠くまで飛ばない傾向があることを示唆している。", "suggests", "This suggests|これは示唆している||that if enough food is near their homes,|巣の近くに十分な食べ物があれば||they tend not to fly far.|遠くまで飛ばない傾向があると"),
        ("( 20 )、ミツバチのすむ場所の近くで植物を育てれば、長距離を飛ばないようにする助けになり得る。", "could help", "( 20 ), growing plants near where they live|（20）、ミツバチのすむ場所の近くで植物を育てることは||could help keep them|ミツバチをとどめる助けになり得る||from flying long distances.|長距離を飛ばないように"),
        ("これは、有機はちみつの認証基準を満たすことにも役立ち得る。", "could", "This could also help meet the standards|これは基準を満たすことにも役立ち得る||for organic honey certification.|有機はちみつの認証の"),
        ("ミツバチの周囲で化学薬品が使われなければ、集めた蜜にはそれらが含まれない。", "will not contain", "If no chemicals are used around them,|ミツバチの周囲で化学薬品が使われなければ||the honey they collect|ミツバチが集める蜜には||will not contain them.|それらが含まれない"),
        ("つまり、人々ははちみつの品質を管理できるのだ。", "means", "This means|これは意味する||people can control the quality of the honey.|人々ははちみつの品質を管理できると"),
    ],
])

MACHINE = passage("B", "A Machine from the Past", [
    [
        ("100年以上前、潜水士たちがギリシャのアンティキティラ島付近で驚くべき発見をした。", "made", "More than one hundred years ago,|100年以上前に||divers made a surprising discovery|潜水士たちが驚くべき発見をした||near the island of Antikythera in Greece.|ギリシャのアンティキティラ島付近で"),
        ("見つかった品々には、彫像や硬貨に加え、機械の部品が付いた壊れた物体があった。", "was", "Among the items they found|彼らが見つけた品々の中には||was a broken object with mechanical parts,|機械の部品が付いた壊れた物体があった||along with statues and coins.|彫像や硬貨に加えて"),
        ("後に科学者たちは、この奇妙な装置が空を観測するために使われた古代の機械だとわかった。", "learned", "Later, scientists learned|後に科学者たちはわかった||that this strange device was an ancient machine|この奇妙な装置が古代の機械だと||used to observe the sky.|空を観測するために使われた"),
        ("それには小さな部品がたくさんあり、太陽、月、そしておそらく惑星の動きを示していた。", "had", "It had many small parts|それには小さな部品がたくさんあり||and showed the movement of the sun, the moon,|太陽と月の動きを示していた||and probably the planets.|そしておそらく惑星の動きも"),
        ("その装置は2000年以上前のものだったにもかかわらず、( 21 )。", "", "Although the device was more than 2,000 years old,|その装置は2000年以上前のものだったにもかかわらず||it ( 21 ).|それは（21）"),
        ("このように複雑な機構を予想していなかった専門家たちは、この技術に驚いた。", "surprised", "This technology surprised experts,|この技術は専門家たちを驚かせた||who had not expected such complex mechanisms.|このように複雑な機構を予想していなかった"),
    ], [
        ("この装置は現在、アンティキティラの機構と呼ばれている。", "is", "The device is now called|この装置は現在呼ばれている||the Antikythera Mechanism.|アンティキティラの機構と"),
        ("最近、ロンドンの科学者たちが詳細な情報を集めようと試みたが、装置の前面はひどく損傷していた。", "attempted", "Recently, scientists in London attempted to gather detailed information,|最近ロンドンの科学者たちは詳細な情報を集めようと試みた||but the front part of it was heavily damaged.|しかし装置の前面はひどく損傷していた"),
        ("( 22 )、彼らはX線と3次元のコンピューターモデルを使った。", "used", "( 22 ), they used X-rays|（22）、彼らはX線を使った||and 3D computer models.|そして3次元のコンピューターモデルを"),
        ("彼らは残された部品と装置の小さな文字を、手掛かりとして調べた。", "examined", "They examined the remaining parts|彼らは残された部品を調べた||and the small letters on the device|そして装置の小さな文字を||as clues.|手掛かりとして"),
        ("ギリシャの天文学や惑星の動きについての知識を使って、装置の前面の動きを示す実物模型を作った。", "built", "They built a physical model|彼らは実物模型を作った||to show the front part's movement,|前面の動きを示すために||using knowledge of Greek astronomy and the movement of planets.|ギリシャの天文学や惑星の動きについての知識を使って"),
        ("まだ多くの部品が失われたままだが、この研究は現代の科学者が古代の装置をどのように研究するかを示している。", "shows", "Although many parts are still missing,|まだ多くの部品が失われたままだが||this study shows|この研究は示している||how modern scientists study ancient devices.|現代の科学者が古代の装置をどのように研究するかを"),
    ], [
        ("別の技術者チームが、異なるコンピューターモデルを使ってこの機構を研究した。", "studied", "A separate team of engineers studied the mechanism|別の技術者チームがこの機構を研究した||using a different computer model.|異なるコンピューターモデルを使って"),
        ("その結果、( 23 ) ということがわかった。", "found", "As a result,|その結果||they found that ( 23 ).|（23）ということがわかった"),
        ("一部の歯車が頻繁に動かなくなった可能性があるため、日常的に使う目的で作られたのではないと考える専門家もいた。", "thought", "Some experts thought|一部の専門家は考えた||it had not been built for everyday use|日常的に使う目的で作られたのではないと||because some gears may have frequently stopped working.|一部の歯車が頻繁に動かなくなった可能性があるため"),
        ("むしろ、教育用の道具として、あるいは古代の科学者の知識や技能を示すために用いられたのだと考えた。", "believed", "Rather, they believed|むしろ彼らは考えた||it served either as an educational tool|教育用の道具として用いられたか||or to demonstrate the knowledge and skills of ancient scientists.|あるいは古代の科学者の知識や技能を示すために用いられたと"),
        ("たとえ毎日は使われなかったとしても、これまでに発見された古代の装置の中で最も見事なものの一つであり続けている。", "remains", "Even if it was not used daily,|たとえ毎日は使われなかったとしても||it remains one of the most impressive ancient devices|最も見事な古代の装置の一つであり続けている||that has been discovered.|これまでに発見された"),
    ],
])

EMAIL = passage("A", "Your car", [
    [
        ("ロドリゲス様", "", "Dear Ms. Rodriguez,|ロドリゲス様"),
        ("先日は当店にお越しいただき、ありがとうございました。", "", "Thank you|ありがとうございます||for coming to our shop the other day.|先日当店にお越しいただき"),
        ("当日は天気が良く、申し分のない状況で近隣の道でタイガー・プラチナムXをお試しいただけたことをうれしく思いました。", "was", "I was glad|私はうれしく思いました||that the weather was nice that day,|当日は天気が良く||and you could try the Tiger Platinum X|タイガー・プラチナムXをお試しいただけて||in the neighborhood in perfect condition.|近隣の道で申し分のない状況で"),
        ("運転したときにどのように感じられるか、確かめる良い機会でした。", "was", "It was a good chance to see|確かめる良い機会でした||how you felt when you drove the car.|その車を運転したときにどのように感じられたかを"),
        ("現在、ご注文いただいた中古車、タイガー・プラチナムXの整備を進めております。", "are", "We are currently working on the Tiger Platinum X,|現在タイガー・プラチナムXの整備を進めております||the used car you ordered.|ご注文いただいた中古車の"),
        ("先日お電話でお伝えしたよりも、時間がかかる見込みです。", "believe", "We believe|当店は考えております||that it will take longer|さらに時間がかかると||than we had informed you during the last phone conversation.|先日のお電話でお伝えしたよりも"),
    ], [
        ("ただいま、担当チームがエンジンを慎重に修理しております。", "is", "Right now,|ただいま||our team is carefully repairing the engine.|担当チームがエンジンを慎重に修理しております"),
        ("お客様は頻繁に長距離を運転なさるため、できる限り良い状態に仕上がるよう、細心の注意を払っております。", "are", "Since you need to drive long distances frequently,|頻繁に長距離を運転なさるため||we are paying close attention to making sure|確実に仕上がるよう細心の注意を払っております||it is in the best possible condition.|できる限り良い状態に"),
        ("また、元の色と正確に一致するよう確認しながら、運転席側のドアと後部の傷を塗装しております。", "are", "Also, we are painting the scratches|また傷を塗装しております||on the driver's side door and the back section,|運転席側のドアと後部の||making sure the color matches exactly with the original.|元の色と正確に一致するよう確認しながら"),
        ("これらの作業のため時間がかかっておりますが、安全で万全な状態のお車をお渡しするために、すべて必要な工程であることをご理解ください。", "is", "Because of these tasks,|これらの作業のため||it is taking more time,|さらに時間がかかっております||but please understand|しかしご理解ください||that all these processes are necessary|これらすべての工程が必要であることを||to provide you with a safe and perfect car.|安全で万全な状態のお車をお渡しするために"),
    ], [
        ("これまでの作業状況から判断して、来週末までにはお車をお届けできると考えております。", "believe", "Considering what we have done so far,|これまでの作業状況から判断して||we believe|当店は考えております||we can deliver the car by the end of next week.|来週末までにお車をお届けできると"),
        ("正確な日付が決まりましたら、ご連絡いたします。", "will contact", "We will contact you|ご連絡いたします||once the exact date has been determined.|正確な日付が決まりましたら"),
        ("作業の進捗やお車の状態についてご質問がございましたら、どうぞ遠慮なくご連絡ください。", "contact", "If you have questions about the progress of the work|作業の進捗についてご質問がございましたら||or the car's condition,|またはお車の状態について||please contact us without hesitation.|どうぞ遠慮なくご連絡ください"),
        ("遅れが生じて申し訳ございませんが、ご理解とご協力をいただけますと幸いです。", "are", "We are sorry for the delay,|遅れが生じて申し訳ございませんが||and we would appreciate your understanding and cooperation.|ご理解とご協力をいただけますと幸いです"),
    ], [
        ("敬具", "", "Sincerely,|敬具"),
        ("マルコ・リー", "", "Marco Lee|マルコ・リー"),
        ("スピードウェイ・モーターズ", "", "Speedway Motors|スピードウェイ・モーターズ"),
    ],
], format="email", meta={"from": "Marco Lee <marco@speedwaymotors.com>", "to": "Sophia Rodriguez <srodriguez@fastlink.com>", "date": "October 7", "subject": "Your car"})
# Retain line breaks in the original greeting and closing/signature, without
# changing paragraph boundaries or breaking the abbreviation Ms.
EMAIL["paragraphs"][0] = EMAIL["paragraphs"][0].replace("Dear Ms. Rodriguez, ", "Dear Ms. Rodriguez,\n", 1)
EMAIL["paragraphs"][-1] = "Sincerely,\nMarco Lee\nSpeedway Motors"
EMAIL["translations"][0] = EMAIL["translations"][0].replace("ロドリゲス様", "ロドリゲス様\n", 1)
EMAIL["translations"][-1] = "敬具\nマルコ・リー\nスピードウェイ・モーターズ"

WHALES = passage("B", "Helping Whales", [
    [
        ("ザトウクジラの数は、捕鯨のために大幅に減少していた。", "had declined", "The number of humpback whales had declined dramatically|ザトウクジラの数は大幅に減少していた||because of whale hunting.|捕鯨のために"),
        ("しかし、近年、その個体数はある程度の回復を見せている。", "has shown", "However, their population has shown some recovery|しかしその個体数はある程度の回復を見せている||in recent years.|近年"),
        ("それでも、今また新たな課題に直面している。", "are", "Yet, they are now facing|それでも今直面している||new challenges.|新たな課題に"),
        ("こうした危険の一つは、太平洋の水温を上げた海洋熱波によるものだ。", "comes", "One of these dangers comes from a marine heat wave|こうした危険の一つは海洋熱波によるものだ||that raised the water temperature of the Pacific Ocean.|太平洋の水温を上げた"),
        ("その結果、クジラにとって重要な食料源であるオキアミが減少した。", "has decreased", "As a result, krill,|その結果オキアミが||a vital food source for these whales,|これらのクジラにとって重要な食料源である||has decreased.|減少した"),
        ("科学者たちは、このような急激な変化はクジラのように長寿で繁殖の遅い動物にとって特に危険だと指摘している。", "point out", "Scientists point out|科学者たちは指摘している||that such rapid changes are especially dangerous|このような急激な変化は特に危険だと||for long-lived, slow-breeding animals like whales.|クジラのように長寿で繁殖の遅い動物にとって"),
        ("北太平洋のザトウクジラの個体数は、過去10年間で約5分の1減ったと報告している。", "report", "They report|彼らは報告している||that the North Pacific population of humpback whales dropped|北太平洋のザトウクジラの個体数が減ったと||by about one-fifth in the last decade.|過去10年間で約5分の1"),
    ], [
        ("科学者たちは人工知能と音響技術を使って、クジラを詳しく観察している。", "are", "Scientists are closely observing whales|科学者たちはクジラを詳しく観察している||using artificial intelligence and sound technology.|人工知能と音響技術を使って"),
        ("AIによる写真認識を用いれば、尾の模様を分析することでクジラの個体を識別できる。", "can identify", "With AI photo recognition,|AIによる写真認識を用いれば||they can identify individual whales|クジラの個体を識別できる||by analyzing patterns on the whales' tails.|クジラの尾の模様を分析することで"),
        ("これにより、長期間にわたってクジラの移動を追跡できる。", "allows", "This allows them to track whale movements|これによりクジラの移動を追跡できる||over long periods.|長期間にわたって"),
        ("また、水中マイクを使ってクジラの音を録音し、種や活動を特定するために、音の資料集と比較する。", "use", "They also use underwater microphones|また水中マイクを使う||to record whale sounds|クジラの音を録音するために||and compare them with a sound library|そしてその音を音の資料集と比較するために||to determine species and activities.|種や活動を特定するために"),
        ("このように、写真、音、海洋環境から得たデータを組み合わせることで、科学者たちはクジラの行動や生活をよりよく理解できる。", "can", "In this way, scientists can better understand whale behaviors and life|このように科学者たちはクジラの行動や生活をよりよく理解できる||by combining data|データを組み合わせることで||from photos, sounds, and the ocean environment.|写真、音、海洋環境からの"),
    ], [
        ("これらの技術は、すでに一部の沿岸地域で明確な効果を上げている。", "have", "These technologies have already produced clear effects|これらの技術はすでに明確な効果を上げている||in some coastal areas.|一部の沿岸地域で"),
        ("例えば、サンタバーバラ海峡やサンフランシスコ湾では、ホエール・セーフというシステムが船に減速を促した。", "encouraged", "In the Santa Barbara Channel and San Francisco Bay, for example,|例えばサンタバーバラ海峡やサンフランシスコ湾では||a system called Whale Safe|ホエール・セーフというシステムが||encouraged ships to reduce speed.|船に減速を促した"),
        ("そのシステムは、船がクジラとの衝突を避ける助けにもなった。", "helped", "It also helped them|そのシステムは船を助けた||avoid collisions with whales.|クジラとの衝突を避けるように"),
        ("しかし、問題全体としては依然として深刻だ。", "remains", "However, the overall problem|しかし問題全体としては||remains serious.|依然として深刻だ"),
        ("西海岸沿いでは、衝突により毎年何十頭もの絶滅の危機にあるクジラが死んでおり、多くの死は観測されないため、実際の数ははるかに多いと専門家たちは考えている。", "die", "Along the West Coast,|西海岸沿いでは||dozens of endangered whales die each year due to collisions,|衝突により毎年何十頭もの絶滅の危機にあるクジラが死んでいる||and experts believe the actual number is much higher|専門家たちは実際の数ははるかに多いと考えている||because many deaths are never observed.|多くの死が観測されないため"),
        ("これは、進歩があっても、クジラが依然として深刻な脅威に直面していることを示している。", "indicates", "This indicates|これは示している||that, despite progress,|進歩があっても||whales continue to face serious threats.|クジラが依然として深刻な脅威に直面していることを"),
    ], [
        ("専門家たちは、これらの技術が北米を越えたより広い地域へ普及することを、なお期待している。", "hope", "Experts still hope|専門家たちはなお期待している||these technologies will expand to larger areas|これらの技術がより広い地域へ普及することを||beyond North America.|北米を越えて"),
        ("このような方法は、世界各地の船との衝突リスクが高い、交通量の多い航路でクジラを守るのに役立つだろう。", "will", "Such methods will likely help protect whales|このような方法はクジラを守るのに役立つだろう||in busy shipping lanes|交通量の多い航路で||with a high risk of ship strikes worldwide.|世界各地の船との衝突リスクが高い"),
        ("科学者たちは、これらの技術がほかの危機にある種にも応用できることを期待している。", "hope", "Scientists also hope|科学者たちはさらに期待している||these technologies can be adapted|これらの技術が応用できることを||for other species in danger.|ほかの危機にある種のために"),
        ("こうした事例は、科学者、地域社会、行政担当者の協力によって、海をより安全にできることを示している。", "show", "These cases show|こうした事例は示している||that cooperation among scientists, local communities, and government officials|科学者、地域社会、行政担当者の協力が||can make the oceans safer.|海をより安全にできることを"),
        ("これらの人々が協力し続ければ、将来、人とクジラはもっと安全に海を共有できるかもしれない。", "may", "If these groups continue to work together,|これらの人々が協力し続ければ||people and whales may share the oceans more safely|人とクジラはもっと安全に海を共有できるかもしれない||in the future.|将来"),
    ],
])


def question(p, number, choices, translations, answer, analysis, grammar,
             evidence_indexes, stem=None, stem_ja=None):
    q = dict(number=number, choices=choices, choiceTranslations=translations,
             answer=answer, choiceAnalysis=analysis, grammar=grammar,
             sourceEvidence=[p["sentencePairs"][i][0] for i in evidence_indexes])
    if stem is not None:
        q.update(question=stem, questionTranslation=stem_ja)
    p["questions"].append(q)


question(HONEY, 18,
         ["a communication tool", "a teaching method", "an innovative way", "a training program"],
         ["意思疎通の道具", "指導方法", "革新的な方法", "訓練プログラム"], 3,
         ["意思疎通の道具。蜂同士や人との通信ではなく、移動を追跡する方法。", "指導方法。学習者への教育は述べられていない。", "革新的な方法→正解。💡QRコードとセンサーで蜂の動きを追跡する新しい手法。", "訓練プログラム。蜂の行動を訓練するのではなく記録している。"],
         "💡to track は開発の目的。They put small QR codes ... と They also placed sensors ... が、追跡の革新的な方法を具体化する。", [1,2])
question(HONEY, 19,
         ["well before they were born", "while they were collecting honey", "when they were about to die", "soon after they emerged from their cells"],
         ["生まれるずっと前に", "蜜を集めている間に", "死ぬ直前に", "巣房から出てきてすぐに"], 4,
         ["生まれるずっと前。生まれていない蜂の背中にタグは付けられない。", "蜜を集めている間。飛行中ではなく、若い蜂を早期から観測する文脈。", "死ぬ直前。以前より長く行動を観測できたという次の文と逆。", "巣房から出てすぐ→正解。💡若い蜂に早期に付けたため、長期間観測できた。"],
         "💡This allowed ... for a much longer period than before が根拠。emerge from は「～から出てくる」、cells はここでは蜂の巣房。", [6,7])
question(HONEY, 20, ["In contrast", "In other words", "Finally", "Rather"],
         ["対照的に", "言い換えれば", "最後に", "むしろ"], 2,
         ["対照的に。近くに餌があれば遠くへ飛ばない、という同じ考えの応用。", "言い換えれば→正解。💡近くに餌があればよいという発見を、近くで植物を育てる案に言い換える。", "最後に。手順や複数事項の最後を列挙する場面ではない。", "むしろ。前の説明を否定・修正する内容ではない。"],
         "💡growing plants ... は動名詞句の主語。keep＋人／物＋from V-ing は「～が…しないようにする」。前文の発見から具体策へつなぐ。", [14,15])
question(MACHINE, 21,
         ["was decorated with many gold parts", "was covered in colorful paintings", "had a very complicated gear structure", "contained a map of nearby islands"],
         ["多くの金の部品で装飾されていた", "色鮮やかな絵で覆われていた", "非常に複雑な歯車構造を備えていた", "近くの島々の地図が入っていた"], 3,
         ["金の部品の装飾。本文に金や装飾の記述はない。", "色鮮やかな絵。絵ではなく天体の動きを示す機構が焦点。", "複雑な歯車構造→正解。💡such complex mechanisms に驚いたという次の文と一致。", "近隣の島の地図。地図の記述はなく、空を観測する装置。"],
         "💡Although は「～にもかかわらず」。2000年以上前のものなのに複雑な技術があった、という意外性。who は experts を説明する。", [3,5])
question(MACHINE, 22, ["Therefore", "Otherwise", "Moreover", "On the other hand"],
         ["そのため", "そうでなければ", "さらに", "一方で"], 1,
         ["そのため→正解。💡前面がひどく損傷していたため、X線と3Dモデルを使った。", "そうでなければ。ある条件が満たされない場合の結果ではない。", "さらに。別の事実を追加するより、損傷に対する対処を示している。", "一方で。二つの対照的な事実ではなく、原因と対処の関係。"],
         "💡前文の heavily damaged が原因、used X-rays and 3D computer models が対処。Therefore で因果関係を示す。", [7,8])
question(MACHINE, 23,
         ["most of the parts were missing", "ancient coins were placed inside", "the computer model made mistakes", "the device was not perfect"],
         ["部品の大半が失われていた", "古代の硬貨が内部に入っていた", "コンピューターモデルが誤りを犯した", "その装置は完全ではなかった"], 4,
         ["部品の大半が失われていた。部品の欠損は既知の状況で、次文の歯車の不調という発見とは異なる。", "古代の硬貨が内部にあった。硬貨は一緒に発見された品で、装置の内部とは書かれていない。", "モデルが誤った。モデルではなく、古代の装置自体がうまく動かなかった可能性。", "装置は完全ではなかった→正解。💡歯車が頻繁に止まった可能性が、その不完全さを説明。"],
         "💡may have＋過去分詞 は過去についての推量。「歯車が動かなくなった可能性」が found that ... の内容を裏付ける。", [14])

question(EMAIL, 24,
         ["spoke with the staff about the delay in the delivery of new cars.", "got into the Tiger Platinum X and drove it around the area.", "looked at the Tiger Platinum X in one of the pamphlets there.", "was informed of which parts of her car the shop had ordered."],
         ["新車の納車遅れについてスタッフと話した。", "タイガー・プラチナムXに乗り、近隣を運転した。", "店にあったパンフレットでタイガー・プラチナムXを見た。", "店が注文した車の部品について説明を受けた。"], 2,
         ["新車の遅れについて話した。注文したのは中古車で、来店時に遅れを話した記述もない。", "近隣を試乗した→正解。💡try ... in the neighborhood と when you drove the car に一致。", "パンフレットで見た。実際に運転しており、パンフレットの記述はない。", "注文済み部品の説明。店が部品を注文したという記述はない。"],
         "💡try the Tiger Platinum X はここでは「試乗する」。in the neighborhood＝around the area。設問は選択肢を続けて文を完成させる形式。", [2,3],
         "When Sophia Rodriguez visited Marco Lee's shop, she", "ソフィア・ロドリゲスがマルコ・リーの店を訪れたとき、彼女は～。")
question(EMAIL, 25,
         ["Because they are installing a new sound system and checking the air conditioner.", "Because they are repairing tires and adjusting the car's headlights.", "Because they are inspecting electrical systems and adding new seats.", "Because they are fixing the engine and painting scratched sections."],
         ["新しい音響装置の設置とエアコンの点検をしているから。", "タイヤの修理とヘッドライトの調整をしているから。", "電気系統の点検と新しい座席の取り付けをしているから。", "エンジンの修理と傷のある部分の塗装をしているから。"], 4,
         ["音響装置とエアコン。いずれも本文にない作業。", "タイヤとライト。いずれも遅延理由として挙げられていない。", "電気系統と座席。本文にない部品を取り違えた選択肢。", "エンジン修理と傷の塗装→正解。💡repairing the engine と painting the scratches の言い換え。"],
         "💡Because of these tasks の these tasks はエンジン修理と傷の塗装。Since はここでは期間ではなく理由「～なので」を示す。", [6,8,9],
         "Why is the team taking extra time to finish the car Sophia ordered?", "なぜ担当チームはソフィアが注文した車の仕上げに余分な時間をかけているのですか。")
question(EMAIL, 26,
         ["To ask her to choose a different color for her car.", "To inform her of the day when they can deliver her car.", "To tell her the name of the mechanic working on her car.", "To notify her about additional charges related to repairing her car."],
         ["車の別の色を選ぶよう頼むため。", "車を届けられる日を知らせるため。", "車を整備している担当者の名前を伝えるため。", "車の修理に関する追加料金を知らせるため。"], 2,
         ["別の色を選ぶ。元の色に正確に合わせるとあり、別の色を求めていない。", "納車日を知らせる→正解。💡正確な日付が決まったら連絡するという記述に一致。", "整備担当者の名前。名前を知らせる予定は書かれていない。", "追加料金。料金についての記述はない。"],
         "💡once は「～したら」。未来のことでも時を表す節では will を使わず、has been determined で「決定済みになったら」を表す。", [10,11],
         "Why will Marco contact Sophia in the future?", "マルコが後日ソフィアに連絡するのはなぜですか。")
question(WHALES, 27,
         ["It forced them to swim into the deeper ocean.", "It created a rapid change in the ocean currents.", "It led to a reduction in their habitats to one-fifth.", "It caused a decline in their main food supply."],
         ["より深い海へ泳ぐことを強いた。", "海流に急激な変化を生じさせた。", "生息域を5分の1に縮小させた。", "主な食料の供給を減少させた。"], 4,
         ["深い海へ移動。移動先の深さは本文に書かれていない。", "海流の変化。変化したのは水温で、海流への影響は述べていない。", "生息域が5分の1に。約5分の1減ったのは個体数で、生息域ではない。", "主な食料が減少→正解。💡水温上昇の結果、重要な食料源のオキアミが減った。"],
         "💡a vital food source は krill の同格説明。dropped by one-fifth は「5分の1だけ減少」であり、to one-fifth「5分の1に」と区別する。", [3,4],
         "How did high ocean temperatures affect humpback whales?", "高い海水温はザトウクジラにどのような影響を与えましたか。")
question(WHALES, 28,
         ["record whale movements under the sea for sound libraries.", "observe whale swimming speed to understand their habits.", "follow each whale by recognizing the patterns on its tail.", "study their behavioral patterns to locate whale habitats."],
         ["音の資料集のために水中のクジラの動きを記録する。", "習性を理解するために泳ぐ速さを観察する。", "尾の模様を認識して個々のクジラを追跡する。", "生息域を特定するために行動パターンを調べる。"], 3,
         ["水中の動きを音の資料集に記録。音を録音するマイクの説明とAIの役割を混同している。", "泳ぐ速さの観察。AIが識別するのは尾の模様で、速度ではない。", "尾の模様で個体を追跡→正解。💡identify individual whales と track whale movements の言い換え。", "生息域の特定。本文は個体識別と移動の追跡を説明している。"],
         "💡by analyzing は手段「分析することで」。individual whales＝each whale、analyzing patterns＝recognizing the patterns の対応を読む。", [8,9],
         "Scientists use artificial intelligence to", "科学者たちは人工知能を使って～。")
question(WHALES, 29,
         ["Some whales die in accidents that people never notice.", "Whales often move away from the coast to safer waters.", "The swimming speed of whales is too fast for ships to follow.", "Several ships come to the area secretly to hunt whales."],
         ["人々が気づかない事故で死ぬクジラもいるから。", "クジラがしばしば沿岸を離れ、安全な海域へ移動するから。", "クジラの泳ぐ速度が速すぎて船が追いつけないから。", "数隻の船が捕鯨のために秘密裏にその海域へ来るから。"], 1,
         ["気づかれない事故死がある→正解。💡many deaths are never observed の言い換え。", "安全な海域への移動。実際の死亡数を把握できない理由として書かれていない。", "船が追いつけない速度。死亡数の観測に関する記述ではない。", "秘密の捕鯨船。西海岸の死因は船との衝突で、秘密の捕鯨ではない。"],
         "💡because many deaths are never observed が理由。never observed（観測されない）を people never notice（人々が気づかない）と能動態で言い換える。", [16],
         "Why do experts believe they cannot know the actual number of West Coast whale deaths?", "専門家たちはなぜ、西海岸でのクジラの実際の死亡数を把握できないと考えているのですか。")
question(WHALES, 30,
         ["be tested first in busy sea lanes near Asian and African ports.", "be applied to protecting other animals that are also under threat.", "cause opposition from local governments regarding their introduction.", "bring about further destruction if they are not used carefully."],
         ["まずアジアとアフリカの港付近の交通量の多い航路で試される。", "同じく脅威にさらされているほかの動物の保護に応用される。", "導入に関して地方政府から反対を招く。", "慎重に使わなければ、さらに破壊をもたらす。"], 2,
         ["アジア・アフリカでまず実験。北米以外への拡大は期待するが、地域や順序を限定していない。", "ほかの動物の保護に応用→正解。💡adapted for other species in danger の言い換え。", "地方政府が反対。本文は行政を含めた協力の重要性を述べている。", "さらなる破壊。技術の悪用による破壊は書かれていない。"],
         "💡be adapted for は「～向けに応用される」。in danger＝under threat。are expected to＋動詞の原形に続けて文を完成させる。", [20],
         "Technologies to help whales are expected to", "クジラを助ける技術は、～することが期待されている。")
question(WHALES, 31,
         ["AI studies show whales become louder when ocean noise grows near ports.", "Whale collisions on the West Coast have ended completely in recent years.", "Coastal governments now observe other species at risk throughout the year.", "Scientists research whales by using a variety of different methods."],
         ["AIの研究では、港付近の海中騒音が大きくなるとクジラの声も大きくなるとわかっている。", "近年、西海岸でのクジラの衝突は完全になくなった。", "沿岸の行政が現在、危機にあるほかの種を一年中観察している。", "科学者たちはさまざまな方法を用いてクジラを研究している。"], 4,
         ["騒音に応じて声が大きくなる。音は録音するが、騒音と声量の関係は書かれていない。", "衝突は完全に終了。現在も毎年何十頭も死亡するという本文に反する。", "行政がほかの種を一年中観察。ほかの種への応用は将来への期待で、現状ではない。", "さまざまな方法で研究→正解。💡写真、音、海洋環境のデータを組み合わせるとある。"],
         "💡a variety of different methods は、AI写真認識・水中マイク・環境データなどをまとめた表現。全体一致問題も具体的な本文根拠で判断する。", [7,10,11],
         "Which of the following statements is true?", "次の記述のうち、正しいものはどれですか。")

PASSAGES = [HONEY, MACHINE, EMAIL, WHALES]

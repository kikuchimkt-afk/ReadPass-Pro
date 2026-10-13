# -*- coding: utf-8 -*-
"""Install the official 2026-2 Grade Pre-1 Part 3 into ReadPass data.

Each paragraph is written as a list of sentences so that the official
paragraphs, the Japanese translations and the sentencePairs are always
derived from one source and cannot drift apart.
"""

from __future__ import annotations

import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "pre-grade1" / "2026-2" / "data.json"


# (English, Japanese, slash reading, main verb)
WELFARE_PARAGRAPHS = [
    [
        (
            "Every month, millions of low-income Americans rely on the United States’ Supplemental Nutrition Assistance Program (SNAP) to afford basic groceries.",
            "毎月、何百万人もの低所得のアメリカ人が、基本的な食料品を買うために、アメリカの補助的栄養支援プログラム（SNAP）に頼っている。",
            "Every month,|毎月||millions of low-income Americans rely on the United States’ Supplemental Nutrition Assistance Program (SNAP)|何百万人もの低所得のアメリカ人がアメリカの補助的栄養支援プログラム（SNAP）に頼っている||to afford basic groceries.|基本的な食料品を買うために",
            "rely on",
        ),
        (
            "SNAP recipients receive benefits loaded onto an electronic card, which can be used at authorized stores to purchase food items.",
            "SNAPの受給者は電子カードに入金された給付を受け取り、そのカードは認可を受けた店舗で食品を購入するのに使うことができる。",
            "SNAP recipients receive benefits|SNAPの受給者は給付を受け取る||loaded onto an electronic card,|電子カードに入金された||which can be used at authorized stores|そのカードは認可を受けた店舗で使うことができる||to purchase food items.|食品を購入するのに",
            "receive",
        ),
        (
            "Despite the program’s long history of success, in the 1990s, concerns that reliance on SNAP would decrease people’s motivation to better themselves economically caused policymakers to introduce stricter employment requirements for certain SNAP participants.",
            "このプログラムには長い成功の歴史があったにもかかわらず、1990年代には、SNAPに頼ることで経済的に向上しようという人々の意欲が低下するのではないかという懸念から、政策立案者は一部のSNAP参加者に対して、より厳しい就労要件を導入した。",
            "Despite the program’s long history of success,|このプログラムの長い成功の歴史にもかかわらず||in the 1990s,|1990年代に||concerns that reliance on SNAP would decrease people’s motivation|SNAPへの依存が人々の意欲を低下させるという懸念が||to better themselves economically|経済的に向上しようとする||caused policymakers to introduce stricter employment requirements|政策立案者により厳しい就労要件を導入させた||for certain SNAP participants.|一部のSNAP参加者に対して",
            "caused",
        ),
        (
            "In particular, the reforms targeted able-bodied adults without dependents, such as single people living alone.",
            "特に、この改革は、一人暮らしの独身者など、扶養家族のいない健常な成人を対象としていた。",
            "In particular,|特に||the reforms targeted able-bodied adults without dependents,|この改革は扶養家族のいない健常な成人を対象としていた||such as single people living alone.|一人暮らしの独身者などの",
            "targeted",
        ),
        (
            "It was hoped that the changes would motivate such individuals to seek employment and discourage long-term reliance on public support.",
            "この変更によって、そうした人々が職を求める意欲を持ち、公的支援への長期的な依存が抑えられることが期待された。",
            "It was hoped|期待された||that the changes would motivate such individuals to seek employment|その変更がそうした人々に職を求める意欲を持たせ||and discourage long-term reliance on public support.|公的支援への長期的な依存を抑えることが",
            "was hoped",
        ),
        (
            "Multiple studies that have examined the validity of these reforms, though, have indicated that the reforms had little or no effect on their overall employment rate.",
            "しかし、これらの改革の妥当性を検証した複数の研究は、改革が対象者全体の就業率にほとんど、あるいはまったく影響を与えなかったことを示している。",
            "Multiple studies|複数の研究は||that have examined the validity of these reforms,|これらの改革の妥当性を検証した||though,|しかし||have indicated|示している||that the reforms had little or no effect on their overall employment rate.|改革が対象者全体の就業率にほとんど、あるいはまったく影響しなかったことを",
            "have indicated",
        ),
    ],
    [
        (
            "Opponents of the employment requirements also point out that while the policy is meant to apply to what are known as able-bodied adults without dependents, in practice, that category includes a wide range of people with varying levels of health, ability to work, and responsibility for others.",
            "就労要件に反対する人々はまた、この政策は「扶養家族のいない健常な成人」と呼ばれる人々に適用されることになっているが、実際にはその区分に、健康状態や働く能力、他者に対する責任の程度がさまざまな、幅広い人々が含まれていると指摘する。",
            "Opponents of the employment requirements also point out|就労要件に反対する人々はまた指摘する||that while the policy is meant to apply|その政策は適用されることになっているが||to what are known as able-bodied adults without dependents,|扶養家族のいない健常な成人として知られる人々に||in practice,|実際には||that category includes a wide range of people|その区分には幅広い人々が含まれる||with varying levels of health, ability to work, and responsibility for others.|健康状態、働く能力、他者への責任の程度がさまざまな",
            "point out",
        ),
        (
            "For instance, individuals recovering from surgery, managing mental illness, or facing housing instability may be classified as “able-bodied” despite significant barriers to regular employment.",
            "たとえば、手術から回復中の人、精神疾患を抱えている人、住居が不安定な人は、定職に就くうえで大きな障壁があるにもかかわらず、「健常」に分類されることがある。",
            "For instance,|たとえば||individuals recovering from surgery, managing mental illness, or facing housing instability|手術から回復中の人、精神疾患を抱えている人、住居が不安定な人は||may be classified as “able-bodied”|「健常」に分類されることがある||despite significant barriers to regular employment.|定職に就くうえで大きな障壁があるにもかかわらず",
            "may be classified",
        ),
        (
            "Moreover, many low-wage jobs provide unpredictable or limited working hours, so people can find themselves falling below the required minimums through no fault of their own.",
            "さらに、多くの低賃金の仕事は労働時間が予測できなかったり限られていたりするため、人々は自分に何の落ち度もないのに、必要とされる最低時間を下回ってしまうことがある。",
            "Moreover,|さらに||many low-wage jobs provide unpredictable or limited working hours,|多くの低賃金の仕事は予測できない、あるいは限られた労働時間しか提供しない||so people can find themselves falling below the required minimums|そのため人々は必要とされる最低時間を下回ってしまうことがある||through no fault of their own.|自分に何の落ち度もないのに",
            "provide",
        ),
        (
            "This inconsistency between rigid policy definitions and real-world conditions often leads to the loss of food assistance among people who are actively trying to support themselves.",
            "硬直的な政策上の定義と現実の状況とのこうした食い違いによって、自活しようと積極的に努力している人々が食料支援を失うことが多い。",
            "This inconsistency between rigid policy definitions and real-world conditions|硬直的な政策上の定義と現実の状況とのこの食い違いは||often leads to the loss of food assistance|しばしば食料支援の喪失につながる||among people who are actively trying to support themselves.|自活しようと積極的に努力している人々の間で",
            "leads to",
        ),
    ],
    [
        (
            "Research has also demonstrated that when recessions occur and unemployment rises, the demand for food assistance increases.",
            "研究ではまた、景気後退が起きて失業が増えると、食料支援の需要が高まることが示されている。",
            "Research has also demonstrated|研究はまた示している||that when recessions occur and unemployment rises,|景気後退が起きて失業が増えると||the demand for food assistance increases.|食料支援の需要が高まることを",
            "has also demonstrated",
        ),
        (
            "However, SNAP work requirements do not always adjust quickly or automatically to these changing conditions.",
            "しかし、SNAPの就労要件は、こうした状況の変化に必ずしも迅速に、あるいは自動的に対応するわけではない。",
            "However,|しかし||SNAP work requirements do not always adjust quickly or automatically|SNAPの就労要件は必ずしも迅速に、あるいは自動的に対応するわけではない||to these changing conditions.|こうした状況の変化に",
            "do not always adjust",
        ),
        (
            "This creates a situation where people who have recently become unemployed may suddenly lose eligibility for assistance because they no longer meet the minimum work hours.",
            "その結果、最近失業した人々が、最低就労時間を満たさなくなったために、突然支援の受給資格を失いかねない状況が生まれる。",
            "This creates a situation|これは状況を生み出す||where people who have recently become unemployed|最近失業した人々が||may suddenly lose eligibility for assistance|突然支援の受給資格を失いかねない||because they no longer meet the minimum work hours.|最低就労時間をもはや満たさないために",
            "creates",
        ),
        (
            "This also has broader consequences beyond individual hardship.",
            "これはまた、個人の困窮にとどまらない、より広範な影響を及ぼす。",
            "This also has broader consequences|これはまた、より広範な影響を及ぼす||beyond individual hardship.|個人の困窮を超えた",
            "has",
        ),
        (
            "SNAP benefits are typically spent immediately and within one’s own community, helping to sustain demand in the economy.",
            "SNAPの給付は通常、すぐに、しかも受給者自身の地域内で使われるため、経済における需要を支える助けとなる。",
            "SNAP benefits are typically spent immediately|SNAPの給付は通常すぐに使われる||and within one’s own community,|しかも自分の地域内で||helping to sustain demand in the economy.|経済における需要を支える助けとなる。",
            "are typically spent",
        ),
        (
            "Without it, struggling areas lose not only food support but also a source of economic activity that could lessen the impact of job losses.",
            "それがなければ、苦境にある地域は、食料支援だけでなく、失業の影響を和らげうる経済活動の源も失うことになる。",
            "Without it,|それがなければ||struggling areas lose not only food support|苦境にある地域は食料支援だけでなく||but also a source of economic activity|経済活動の源も失う||that could lessen the impact of job losses.|失業の影響を和らげうる",
            "lose",
        ),
        (
            "By restricting access to SNAP benefits during economic downturns, the program loses its ability to protect both families and communities from deeper economic harm.",
            "景気後退期にSNAP給付の利用を制限することで、このプログラムは、家族と地域社会の双方をより深刻な経済的打撃から守る力を失ってしまう。",
            "By restricting access to SNAP benefits during economic downturns,|景気後退期にSNAP給付の利用を制限することで||the program loses its ability|このプログラムは力を失う||to protect both families and communities from deeper economic harm.|家族と地域社会の双方をより深刻な経済的打撃から守る",
            "loses",
        ),
        (
            "Taken together, the flaws in efforts to enforce employment requirements for SNAP reveal a policy approach that some experts believe ignores both human needs and economic realities.",
            "総合すると、SNAPの就労要件を課そうとする取り組みの欠陥は、一部の専門家が人々の必要と経済の現実の両方を無視していると考える政策手法を浮き彫りにしている。",
            "Taken together,|総合すると||the flaws in efforts to enforce employment requirements for SNAP|SNAPの就労要件を課そうとする取り組みの欠陥は||reveal a policy approach|ある政策手法を浮き彫りにしている||that some experts believe ignores both human needs and economic realities.|一部の専門家が人々の必要と経済の現実の両方を無視していると考える",
            "reveal",
        ),
    ],
]

HELENA_PARAGRAPHS = [
    [
        (
            "A navigator aboard a Portuguese vessel returning from India is credited with discovering the South Atlantic island of Saint Helena in 1502.",
            "インドから帰国途中のポルトガル船に乗っていた航海士が、1502年に南大西洋の島セントヘレナを発見したとされている。",
            "A navigator aboard a Portuguese vessel|ポルトガル船に乗っていた航海士が||returning from India|インドから帰国途中の||is credited with discovering the South Atlantic island of Saint Helena|南大西洋の島セントヘレナを発見したとされている||in 1502.|1502年に",
            "is credited with",
        ),
        (
            "Although it was uninhabited, the Portuguese did not establish a permanent settlement there.",
            "その島は無人島だったが、ポルトガル人はそこに恒久的な入植地を築かなかった。",
            "Although it was uninhabited,|その島は無人島だったが||the Portuguese did not establish a permanent settlement there.|ポルトガル人はそこに恒久的な入植地を築かなかった。",
            "did not establish",
        ),
        (
            "Instead, with abundant forests and resources, the island became a staging post for their ships to restock with water and other provisions.",
            "その代わりに、豊かな森林と資源を持つこの島は、ポルトガル船が水やその他の物資を補給するための中継地となった。",
            "Instead,|その代わりに||with abundant forests and resources,|豊かな森林と資源を持つ||the island became a staging post|この島は中継地となった||for their ships to restock with water and other provisions.|彼らの船が水やその他の物資を補給するための",
            "became",
        ),
        (
            "For approximately eighty years, this isolated island remained a secret, known only to the Portuguese.",
            "約80年間、この孤立した島はポルトガル人だけが知る秘密のままだった。",
            "For approximately eighty years,|約80年間||this isolated island remained a secret,|この孤立した島は秘密のままだった||known only to the Portuguese.|ポルトガル人だけに知られて",
            "remained",
        ),
        (
            "However, after English explorer Thomas Cavendish came across the island, that changed.",
            "しかし、イギリスの探検家トーマス・キャベンディッシュがこの島を偶然見つけると、その状況は変わった。",
            "However,|しかし||after English explorer Thomas Cavendish came across the island,|イギリスの探検家トーマス・キャベンディッシュがこの島を偶然見つけると||that changed.|その状況は変わった。",
            "changed",
        ),
        (
            "Although the Dutch also attempted to control this strategically important island in the seventeenth century, it was an English trading company, the East India Company, that ultimately took possession of it.",
            "17世紀にはオランダもこの戦略的に重要な島を支配しようとしたが、最終的にこの島を手に入れたのは、イギリスの貿易会社である東インド会社だった。",
            "Although the Dutch also attempted to control this strategically important island|オランダもこの戦略的に重要な島を支配しようとしたが||in the seventeenth century,|17世紀に||it was an English trading company, the East India Company,|イギリスの貿易会社である東インド会社だった||that ultimately took possession of it.|最終的にこの島を手に入れたのは",
            "was",
        ),
    ],
    [
        (
            "As more settlers arrived, infrastructure was developed, and the island became an important hub for the company’s vessels.",
            "入植者が増えるにつれてインフラが整備され、島は同社の船にとって重要な拠点となった。",
            "As more settlers arrived,|入植者が増えるにつれて||infrastructure was developed,|インフラが整備され||and the island became an important hub for the company’s vessels.|島は同社の船にとって重要な拠点となった。",
            "was developed",
        ),
        (
            "During its growth period, enslaved people were brought to the island to work on plantations.",
            "発展期には、プランテーションで働かせるために、奴隷にされた人々が島へ連れてこられた。",
            "During its growth period,|発展期には||enslaved people were brought to the island|奴隷にされた人々が島へ連れてこられた||to work on plantations.|プランテーションで働くために",
            "were brought",
        ),
        (
            "However, after Britain outlawed the slave trade in 1807, the British navy used the island as a base from which to intercept ships carrying slaves.",
            "しかし、1807年にイギリスが奴隷貿易を禁止すると、イギリス海軍はこの島を、奴隷を運ぶ船を拿捕するための基地として利用した。",
            "However,|しかし||after Britain outlawed the slave trade in 1807,|1807年にイギリスが奴隷貿易を禁止すると||the British navy used the island as a base|イギリス海軍はこの島を基地として利用した||from which to intercept ships carrying slaves.|そこから奴隷を運ぶ船を拿捕するための",
            "used",
        ),
        (
            "Although the island remained a key port until well into the nineteenth century, it began to experience a decline.",
            "島は19世紀に入ってもかなりの間、重要な港であり続けたが、やがて衰退し始めた。",
            "Although the island remained a key port|島は重要な港であり続けたが||until well into the nineteenth century,|19世紀に入ってかなりたつまで||it began to experience a decline.|やがて衰退し始めた。",
            "began",
        ),
        (
            "The introduction of steamships was a factor, as these vessels could travel longer distances than sailing ships without resupplying.",
            "蒸気船の導入はその一因だった。蒸気船は帆船よりも長い距離を補給なしで航行できたからである。",
            "The introduction of steamships was a factor,|蒸気船の導入はその一因だった||as these vessels could travel longer distances than sailing ships|蒸気船は帆船よりも長い距離を航行できたからである||without resupplying.|補給なしで",
            "was",
        ),
        (
            "It has also been argued that the Suez Canal, which opened in 1869 and provided a shorter route between Europe and Asia, had an impact.",
            "また、1869年に開通し、ヨーロッパとアジアを結ぶより短い航路をもたらしたスエズ運河が影響を及ぼしたとも主張されている。",
            "It has also been argued|また主張されている||that the Suez Canal,|スエズ運河が||which opened in 1869 and provided a shorter route between Europe and Asia,|1869年に開通し、ヨーロッパとアジアを結ぶより短い航路をもたらした||had an impact.|影響を及ぼしたと",
            "has also been argued",
        ),
    ],
    [
        (
            "The British also utilized Saint Helena for another purpose.",
            "イギリスはセントヘレナを別の目的にも利用した。",
            "The British also utilized Saint Helena|イギリスはセントヘレナを利用した||for another purpose.|別の目的にも",
            "utilized",
        ),
        (
            "After Napoleon I, emperor of the French, was defeated at the Battle of Waterloo in 1815, he was captured.",
            "フランス皇帝ナポレオン1世は、1815年のワーテルローの戦いで敗れた後、捕らえられた。",
            "After Napoleon I, emperor of the French, was defeated at the Battle of Waterloo in 1815,|フランス皇帝ナポレオン1世は1815年のワーテルローの戦いで敗れた後||he was captured.|捕らえられた。",
            "was captured",
        ),
        (
            "The year before, Napoleon had given up his title and been exiled to Elba, a Mediterranean island.",
            "その前年、ナポレオンは帝位を退き、地中海の島エルバへ追放されていた。",
            "The year before,|その前年||Napoleon had given up his title|ナポレオンは帝位を退き||and been exiled to Elba, a Mediterranean island.|地中海の島エルバへ追放されていた。",
            "had given up",
        ),
        (
            "However, he later escaped, returned to France, and regained power.",
            "しかし、彼はその後脱出してフランスに戻り、権力を取り戻した。",
            "However,|しかし||he later escaped, returned to France, and regained power.|彼はその後脱出してフランスに戻り、権力を取り戻した。",
            "escaped",
        ),
        (
            "This time, the British were determined to take no chances, and Saint Helena seemed the perfect choice.",
            "今回、イギリスは決して危険を冒さないと固く決意しており、セントヘレナは最適な選択に思われた。",
            "This time,|今回||the British were determined to take no chances,|イギリスは決して危険を冒さないと固く決意しており||and Saint Helena seemed the perfect choice.|セントヘレナは最適な選択に思われた。",
            "were determined",
        ),
        (
            "The island’s isolated location would make it extremely difficult for any rescue mission to land without being spotted.",
            "島の孤立した立地のため、どんな救出部隊であれ、見つからずに上陸するのは極めて困難になるはずだった。",
            "The island’s isolated location|島の孤立した立地は||would make it extremely difficult|極めて困難にするはずだった||for any rescue mission to land without being spotted.|どんな救出部隊であれ見つからずに上陸することを",
            "would make",
        ),
        (
            "The British even stationed some soldiers on Ascension Island over one thousand kilometers away to prevent its use as a base for any French rescue attempt.",
            "イギリスは、フランスによる救出作戦の拠点として使われるのを防ぐため、1,000キロ以上離れたアセンション島にまで兵士を駐留させた。",
            "The British even stationed some soldiers on Ascension Island|イギリスはアセンション島にまで兵士を駐留させた||over one thousand kilometers away|1,000キロ以上離れた||to prevent its use as a base for any French rescue attempt.|フランスの救出作戦の拠点としてそこが使われるのを防ぐために",
            "stationed",
        ),
        (
            "Not held in a standard prison, Napoleon mainly resided at a secure residence called Longwood House, where he was kept under constant surveillance until he died in 1821.",
            "ナポレオンは通常の刑務所には収容されず、主にロングウッド・ハウスと呼ばれる警備の厳重な邸宅で暮らし、1821年に亡くなるまで、そこで絶えず監視下に置かれた。",
            "Not held in a standard prison,|通常の刑務所には収容されず||Napoleon mainly resided at a secure residence called Longwood House,|ナポレオンは主にロングウッド・ハウスと呼ばれる警備の厳重な邸宅で暮らした||where he was kept under constant surveillance|そこで彼は絶えず監視下に置かれた||until he died in 1821.|1821年に亡くなるまで",
            "resided",
        ),
    ],
    [
        (
            "From a geographic perspective, the volcanic island’s isolation also contributed to the evolution of unique native animal and plant species over millions of years.",
            "地理的な観点から見ると、この火山島の孤立性は、何百万年にもわたって独自の固有動植物種が進化することにも寄与した。",
            "From a geographic perspective,|地理的な観点から見ると||the volcanic island’s isolation also contributed to the evolution|この火山島の孤立性は進化にも寄与した||of unique native animal and plant species|独自の固有動植物種の||over millions of years.|何百万年にもわたって",
            "contributed",
        ),
        (
            "Its physical geography is varied, with steep cliffs and forested interior highlands.",
            "その自然地理は変化に富み、切り立った断崖や森林に覆われた内陸の高地がある。",
            "Its physical geography is varied,|その自然地理は変化に富み||with steep cliffs and forested interior highlands.|切り立った断崖や森林に覆われた内陸の高地がある。",
            "is varied",
        ),
        (
            "Since the discovery of the island, however, its environment has been undermined.",
            "しかし、島の発見以降、その環境は損なわれてきた。",
            "Since the discovery of the island,|島の発見以降||however,|しかし||its environment has been undermined.|その環境は損なわれてきた。",
            "has been undermined",
        ),
        (
            "The introduction of invasive species and livestock, and resource exploitation through deforestation, have taken their toll, leading to the formation of semidesert areas.",
            "外来種や家畜の持ち込み、そして森林伐採による資源の乱用が大きな打撃を与え、半砂漠地帯の形成につながった。",
            "The introduction of invasive species and livestock,|外来種や家畜の持ち込み||and resource exploitation through deforestation,|そして森林伐採による資源の乱用が||have taken their toll,|大きな打撃を与えてきた||leading to the formation of semidesert areas.|半砂漠地帯の形成につながった。",
            "have taken their toll",
        ),
        (
            "Nevertheless, community initiatives have been established to turn the tide on this habitat loss by replanting native trees.",
            "それでも、在来種の木を植え直すことで、この生息地の消失という流れを変えようとする地域主導の取り組みが始められている。",
            "Nevertheless,|それでも||community initiatives have been established|地域主導の取り組みが始められている||to turn the tide on this habitat loss|この生息地の消失という流れを変えるために||by replanting native trees.|在来種の木を植え直すことによって",
            "have been established",
        ),
        (
            "Although some native species are already extinct, there is optimism that recreating the forests that existed before colonization can secure the future of surviving native species.",
            "一部の在来種はすでに絶滅しているものの、植民地化以前に存在した森林を再生することで、生き残っている在来種の未来を守れるという楽観的な見方がある。",
            "Although some native species are already extinct,|一部の在来種はすでに絶滅しているものの||there is optimism|楽観的な見方がある||that recreating the forests that existed before colonization|植民地化以前に存在した森林を再生することが||can secure the future of surviving native species.|生き残っている在来種の未来を守れるという",
            "there is",
        ),
    ],
]

WELFARE_QUESTIONS = [
    {
        "number": 25,
        "question": "According to the first paragraph, studies of the effects of reforms to SNAP have shown that",
        "questionTranslation": "第1段落によると、SNAP改革の効果に関する研究が示しているのは",
        "choices": [
            "the changes seem to have had much more effect on people with dependents than on those who did not have them.",
            "people who were removed from SNAP frequently returned to the program later with stronger motivation to remain employed.",
            "although the changes were intended to encourage people to find jobs, they were mostly unsuccessful in doing so.",
            "providing benefits through electronic cards rather than cash payments significantly increased recipients’ willingness to search for stable employment.",
        ],
        "choiceTranslations": [
            "変更は、扶養家族のいない人々よりも、扶養家族のいる人々にはるかに大きな影響を与えたようだということ。",
            "SNAPから外された人々は、後に就労を続ける意欲を強めてプログラムに戻ることが多かったということ。",
            "変更は人々に職を見つけるよう促すことを意図していたが、ほとんど成功しなかったということ。",
            "現金ではなく電子カードで給付を行うことで、受給者が安定した職を探す意欲が大きく高まったということ。",
        ],
        "answer": 3,
        "choiceAnalysis": [
            "❌ 改革の対象は扶養家族のいない健常な成人であり、扶養家族のいる人々への影響と比較した記述はない。",
            "❌ SNAPから外された人が意欲を高めてプログラムに戻ったという記述はない。",
            "✅ 改革はそうした人々に職を求める意欲を持たせる（motivate such individuals to seek employment）ことが目的だったが、研究では就業率にほとんど、あるいはまったく影響がなかった（little or no effect）→正解。💡 had little or no effect が were mostly unsuccessful に言い換えられている。",
            "❌ 電子カードは給付の受け取り方法として紹介されているだけで、就職意欲を高めたとは述べていない。",
        ],
        "sourceEvidence": [
            "It was hoped that the changes would motivate such individuals to seek employment",
            "the reforms had little or no effect on their overall employment rate",
        ],
    },
    {
        "number": 26,
        "question": "What do we learn about how employment requirements for SNAP can affect able-bodied adults without dependents?",
        "questionTranslation": "SNAPの就労要件が扶養家族のいない健常な成人にどのような影響を及ぼしうるかについて、何が分かるか。",
        "choices": [
            "Rules often disqualify individuals who face barriers to employment that are real but may not be covered by official policies.",
            "They allow people with irregular job schedules to receive payments as long as they work fewer hours than a full-time job.",
            "The longer a person has been receiving SNAP benefits, the more likely they are to be affected by the changes.",
            "People who are classified as able-bodied typically lose the opportunity to do part-time work.",
        ],
        "choiceTranslations": [
            "規則によって、現実に就労の障壁を抱えていても、それが公式の政策では考慮されない可能性がある人々が、受給資格を失うことが多い。",
            "勤務日程が不規則な人でも、フルタイムの仕事より短い時間働いていれば、給付を受けられるようにしている。",
            "SNAPの給付を長く受けている人ほど、変更の影響を受けやすい。",
            "健常と分類された人々は、一般にパートタイムで働く機会を失う。",
        ],
        "answer": 1,
        "choiceAnalysis": [
            "✅ 手術からの回復中や精神疾患、住居の不安定さといった現実の障壁があっても「健常」と分類され、自活しようと努力している人が食料支援を失うことが多いと述べられている→正解。💡 rigid policy definitions と real-world conditions の食い違いが、real but may not be covered by official policies に対応している。",
            "❌ 労働時間が予測できない、または限られている人は最低時間を下回って支援を失うとあり、短時間でも給付を受けられるという内容とは逆である。",
            "❌ 受給期間の長さと影響の受けやすさの関係には触れていない。",
            "❌ パートタイムで働く機会を失うという記述はない。問題とされているのは、労働時間が必要な最低時間を下回ることである。",
        ],
        "sourceEvidence": [
            "individuals recovering from surgery, managing mental illness, or facing housing instability may be classified as “able-bodied” despite significant barriers to regular employment",
            "This inconsistency between rigid policy definitions and real-world conditions often leads to the loss of food assistance among people who are actively trying to support themselves.",
        ],
    },
    {
        "number": 27,
        "question": "What has research shown about the wider economic effects of employment requirements for SNAP benefits?",
        "questionTranslation": "SNAP給付の就労要件がもたらす、より広い経済的影響について、研究は何を示しているか。",
        "choices": [
            "They are much more effective for reducing unemployment rates when a recession is not as serious.",
            "Evidence suggests that they tend to encourage recipients to relocate to areas where more jobs are available.",
            "They tend to free up resources for other types of government programs that promote economic recovery.",
            "Because SNAP benefits have the effect of stimulating local economies, enforcing work requirements can make it harder to recover from recessions.",
        ],
        "choiceTranslations": [
            "景気後退がそれほど深刻でないときには、失業率を下げるのにはるかに効果的である。",
            "受給者に、より多くの仕事がある地域への移住を促す傾向があることが証拠から示唆されている。",
            "景気回復を促すほかの種類の政府プログラムのために、財源を確保する傾向がある。",
            "SNAPの給付には地域経済を刺激する効果があるため、就労要件を課すと景気後退からの回復が難しくなりうる。",
        ],
        "answer": 4,
        "choiceAnalysis": [
            "❌ 景気後退の深刻さによって失業率を下げる効果が変わるという記述はない。",
            "❌ 仕事の多い地域への移住については触れられていない。",
            "❌ 財源がほかのプログラムに回るという記述はない。むしろ苦境にある地域が経済活動の源を失うと述べている。",
            "✅ 給付は地域内ですぐに使われて需要を支えるため、景気後退期に利用を制限すると、地域は失業の影響を和らげる経済活動の源を失う→正解。💡 sustain demand in the economy が stimulating local economies に、lose ... a source of economic activity が make it harder to recover に対応している。",
        ],
        "sourceEvidence": [
            "SNAP benefits are typically spent immediately and within one’s own community, helping to sustain demand in the economy.",
            "struggling areas lose not only food support but also a source of economic activity that could lessen the impact of job losses",
        ],
    },
]

HELENA_QUESTIONS = [
    {
        "number": 28,
        "question": "What is one thing that happened after Saint Helena was discovered in 1502?",
        "questionTranslation": "1502年にセントヘレナが発見された後に起きたことの1つは何か。",
        "choices": [
            "Although there was evidence that vessels of other European nations had already visited, the Portuguese claimed the island for Portugal.",
            "The Portuguese realized that they could profit from the island’s wealth of natural resources by charging Dutch and other nations’ vessels to restock there.",
            "The East India Company quickly took control of the island before it was found by anyone else, allowing it to exploit the natural resources there.",
            "The Portuguese were able to take advantage of the island’s natural resources for decades because other nations were not aware of its existence.",
        ],
        "choiceTranslations": [
            "ほかのヨーロッパ諸国の船がすでに訪れていた証拠があったにもかかわらず、ポルトガル人はこの島をポルトガル領だと主張した。",
            "ポルトガル人は、オランダなどほかの国の船に島での補給の料金を課すことで、島の豊かな天然資源から利益を得られることに気づいた。",
            "東インド会社は、ほかの誰かに見つかる前に素早く島を支配し、そこの天然資源を利用できるようにした。",
            "ほかの国々が島の存在を知らなかったため、ポルトガル人は何十年もの間、島の天然資源を利用することができた。",
        ],
        "answer": 4,
        "choiceAnalysis": [
            "❌ ほかの国の船が先に訪れていた証拠には触れていない。島はポルトガル人だけが知る秘密だった。",
            "❌ ほかの国の船に料金を課したという記述はない。島はポルトガル自身の船の補給地として使われた。",
            "❌ 東インド会社が島を手に入れたのは、キャベンディッシュが島を見つけ、オランダも支配を試みた後のことである。",
            "✅ 島は約80年間ポルトガル人だけが知る秘密で、その間ポルトガル船が水や物資を補給する中継地として使われた→正解。💡 approximately eighty years が for decades に、known only to the Portuguese が other nations were not aware of its existence に言い換えられている。",
        ],
        "sourceEvidence": [
            "the island became a staging post for their ships to restock with water and other provisions",
            "For approximately eighty years, this isolated island remained a secret, known only to the Portuguese.",
        ],
    },
    {
        "number": 29,
        "question": "What is one point the author of the passage makes about the use of Saint Helena as a port in the nineteenth century?",
        "questionTranslation": "19世紀におけるセントヘレナの港としての利用について、本文の筆者が述べている点の1つは何か。",
        "choices": [
            "Its use declined around 1807 because the British navy no longer needed it to patrol the South Atlantic in its fight against the slave trade.",
            "A technological development in the shipping industry contributed to the decline of its utility as a resupply port for trade ships.",
            "Even after 1807, some ships carrying slaves demanded the use of Saint Helena’s port facilities before continuing their journeys across the South Atlantic.",
            "Many nations continued to use it even after the Suez Canal opened because they had established facilities there that enabled them to resupply quickly.",
        ],
        "choiceTranslations": [
            "イギリス海軍が奴隷貿易との戦いで南大西洋を巡回するために島を必要としなくなったため、1807年ごろに利用が減った。",
            "海運業界における技術の発展が、貿易船の補給港としての有用性の低下につながった。",
            "1807年以降も、奴隷を運ぶ一部の船は、南大西洋の航海を続ける前にセントヘレナの港湾施設の使用を要求した。",
            "多くの国は、迅速に補給できる施設を島に設けていたため、スエズ運河の開通後も島を利用し続けた。",
        ],
        "answer": 2,
        "choiceAnalysis": [
            "❌ 1807年以降、イギリス海軍は島を奴隷船を拿捕する基地として使ったとあり、必要なくなったわけではない。",
            "✅ 蒸気船は帆船よりも長い距離を補給なしで航行できたため、島が衰退する一因になった→正解。💡 The introduction of steamships が A technological development in the shipping industry に言い換えられている。",
            "❌ 奴隷船が港の使用を要求したという記述はない。島は奴隷船を拿捕するための基地だった。",
            "❌ スエズ運河の開通は島の衰退に影響したとされており、開通後も利用が続いたとは述べていない。",
        ],
        "sourceEvidence": [
            "The introduction of steamships was a factor, as these vessels could travel longer distances than sailing ships without resupplying.",
        ],
    },
    {
        "number": 30,
        "question": "What do we learn about the British regarding their treatment of Napoleon I?",
        "questionTranslation": "ナポレオン1世の扱いに関して、イギリスについて何が分かるか。",
        "choices": [
            "They took as many precautions as they felt necessary to ensure that there could not be a repetition of the event that had occurred on Elba.",
            "They should have considered relocating him to Ascension, as that island had more secure facilities than those on Saint Helena.",
            "They would have preferred to hold him on the island of Elba because its proximity to Europe made it easier to keep British troops there.",
            "They felt that he should have been kept in a regular prison, but there were no suitable facilities available on Saint Helena at that time.",
        ],
        "choiceTranslations": [
            "エルバ島で起きた出来事が繰り返されることが決してないよう、必要と考えるだけの予防策を講じた。",
            "アセンション島にはセントヘレナよりも安全な施設があったので、彼をそこへ移すことを検討すべきだった。",
            "エルバ島はヨーロッパに近く、イギリス軍を駐留させやすかったため、彼をエルバ島で拘束したかった。",
            "彼は通常の刑務所に収容されるべきだと考えたが、当時セントヘレナには適切な施設がなかった。",
        ],
        "answer": 1,
        "choiceAnalysis": [
            "✅ ナポレオンはエルバ島から脱出して権力を取り戻したため、イギリスは今回は一切危険を冒さないと決め、孤島セントヘレナを選び、アセンション島にまで兵士を置いた→正解。💡 take no chances が took as many precautions as they felt necessary に、エルバ島からの脱出が the event that had occurred on Elba に対応している。",
            "❌ アセンション島は救出作戦の拠点として使われないよう兵士を置いた場所で、より安全な施設があったという記述はない。",
            "❌ エルバ島はナポレオンが脱出した場所であり、そこで拘束したかったという記述はない。",
            "❌ 通常の刑務所に入れるべきだったという考えや、施設がなかったという記述はない。",
        ],
        "sourceEvidence": [
            "However, he later escaped, returned to France, and regained power.",
            "This time, the British were determined to take no chances",
            "The British even stationed some soldiers on Ascension Island over one thousand kilometers away to prevent its use as a base for any French rescue attempt.",
        ],
    },
    {
        "number": 31,
        "question": "Regarding Saint Helena’s environment, the author of the passage concludes that",
        "questionTranslation": "セントヘレナの環境について、本文の筆者が結論づけているのは",
        "choices": [
            "it would be better for local environmental initiatives to focus on removing invasive species that have caused damage rather than spending money on replanting efforts.",
            "efforts by Saint Helena islanders to restore forests damaged by centuries of exploitation could contribute to improvements in the island’s natural environment.",
            "the interior highlands have likely been able to avoid the environmental damage that other areas have suffered from due to their inaccessibility.",
            "the local community should consider introducing animal species from other South Atlantic islands that are similar to those that have become extinct on Saint Helena.",
        ],
        "choiceTranslations": [
            "地元の環境保護の取り組みは、植林にお金を使うよりも、被害をもたらした外来種の駆除に力を注いだほうがよいということ。",
            "何世紀にもわたる乱用で損なわれた森林を回復させようとするセントヘレナの島民の取り組みは、島の自然環境の改善に寄与しうるということ。",
            "内陸の高地は近づきにくいため、ほかの地域が受けた環境被害をおそらく免れてきたということ。",
            "地域社会は、セントヘレナで絶滅した種に似た動物種を、南大西洋のほかの島から導入することを検討すべきだということ。",
        ],
        "answer": 2,
        "choiceAnalysis": [
            "❌ 外来種の駆除を優先すべきだとは述べておらず、在来種の木を植え直す取り組みを肯定的に紹介している。",
            "✅ 在来種の木を植え直す地域主導の取り組みがあり、植民地化以前の森林を再生すれば生き残った在来種の未来を守れるという楽観的な見方がある→正解。💡 community initiatives ... by replanting native trees が efforts by Saint Helena islanders to restore forests に言い換えられている。",
            "❌ 内陸の高地は森林に覆われていると述べられているだけで、環境被害を免れたという記述はない。",
            "❌ ほかの島から動物を導入するという提案はない。",
        ],
        "sourceEvidence": [
            "community initiatives have been established to turn the tide on this habitat loss by replanting native trees",
            "there is optimism that recreating the forests that existed before colonization can secure the future of surviving native species",
        ],
    },
]


def build_passage(label: str, title: str, paragraphs: list[list[tuple]], questions: list[dict]) -> dict:
    return {
        "label": label,
        "title": title,
        "paragraphs": [" ".join(sentence[0] for sentence in paragraph) for paragraph in paragraphs],
        "translations": ["".join(sentence[1] for sentence in paragraph) for paragraph in paragraphs],
        "sentencePairs": [list(sentence) for paragraph in paragraphs for sentence in paragraph],
        "questions": questions,
    }


SECTION3 = {
    "name": "大問3",
    "nameEn": "Part 3",
    "type": "reading-comprehension",
    "instruction": "次の英文A，Bの内容に関して，質問に対して最も適切なものを選びなさい。",
    "passages": [
        build_passage("A", "Employment Requirements for Welfare", WELFARE_PARAGRAPHS, WELFARE_QUESTIONS),
        build_passage("B", "Saint Helena", HELENA_PARAGRAPHS, HELENA_QUESTIONS),
    ],
}


def main() -> None:
    if not DATA_PATH.is_file():
        raise SystemExit(
            f"Base data is missing: {DATA_PATH}. Run gen_pre1_2026-2.py before this generator."
        )

    with DATA_PATH.open(encoding="utf-8") as source:
        data = json.load(source)

    sections = data.get("sections")
    if not isinstance(sections, list):
        raise SystemExit("Base data must contain a sections array.")

    names = [section.get("name") for section in sections]
    if names.count("大問1") != 1 or names.count("大問2") != 1:
        raise SystemExit("Run the Part 1 and Part 2 generators before this generator.")

    retained = [section for section in sections if section.get("name") != "大問3"]
    retained.append(SECTION3)
    data["sections"] = retained

    with DATA_PATH.open("w", encoding="utf-8", newline="\n") as target:
        json.dump(data, target, ensure_ascii=False, indent=4)
        target.write("\n")

    print(f"Wrote {DATA_PATH}")
    print("大問3: 2 passages / 7 questions (Q25-Q31)")


if __name__ == "__main__":
    main()

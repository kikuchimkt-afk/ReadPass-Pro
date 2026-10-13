# -*- coding: utf-8 -*-
"""Install the official 2026-2 Grade Pre-1 Part 2 into ReadPass data.

Each paragraph is written as a list of sentences so that the official
paragraphs, the Japanese translations and the sentencePairs are always
derived from one source and cannot drift apart.
"""

from __future__ import annotations

import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "pre-grade1" / "2026-2" / "data.json"


# (English, Japanese) for sentences containing a numbered blank;
# (English, Japanese, slash reading, main verb) for every other sentence.
Y2K_PARAGRAPHS = [
    [
        (
            "From the mid-twentieth century, the use of computer systems increased rapidly, and many of them employed software that represented years with their final two digits.",
            "20世紀半ばから、コンピューターシステムの使用は急速に広がり、その多くは年を下2桁で表すソフトウェアを採用していた。",
            "From the mid-twentieth century,|20世紀半ばから||the use of computer systems increased rapidly,|コンピューターシステムの使用は急速に広がり||and many of them employed software|その多くはソフトウェアを採用していた||that represented years with their final two digits.|年を下2桁で表す",
            "increased",
        ),
        (
            "Some experts pointed out that the two-digit system ( 19 ).",
            "一部の専門家は、2桁方式は ( 19 ) と指摘した。",
        ),
        (
            "For example, there was the question of what would happen in the year 2000 if computer systems incorrectly interpreted the final two digits to mean 1900 instead of 2000.",
            "たとえば、コンピューターシステムが下2桁を誤って2000年ではなく1900年を意味すると解釈したら、2000年に何が起こるのかという問題があった。",
            "For example,|たとえば||there was the question|問題があった||of what would happen in the year 2000|2000年に何が起こるのかという||if computer systems incorrectly interpreted the final two digits|もしコンピューターシステムが下2桁を誤って解釈したら||to mean 1900 instead of 2000.|2000年ではなく1900年を意味すると",
            "was",
        ),
        (
            "Regardless, such concerns were largely brushed aside; the two-digit system saved space and became standard.",
            "それでも、こうした懸念はおおむね退けられた。2桁方式は記憶容量を節約でき、標準となったのである。",
            "Regardless,|それでも||such concerns were largely brushed aside;|こうした懸念はおおむね退けられた||the two-digit system saved space|2桁方式は記憶容量を節約し||and became standard.|標準となった。",
            "brushed aside",
        ),
        (
            "As the new millennium approached, however, concerns reemerged that this so-called Y2K bug might cause malfunctions in infrastructure, such as banking, power plants, and air traffic control.",
            "しかし、新たな千年紀が近づくと、このいわゆる「Y2Kバグ（2000年問題）」が、銀行業務や発電所、航空管制などのインフラに誤作動を引き起こすかもしれないという懸念が再び浮上した。",
            "As the new millennium approached,|新たな千年紀が近づくと||however,|しかし||concerns reemerged|懸念が再び浮上した||that this so-called Y2K bug might cause malfunctions in infrastructure,|このいわゆるY2Kバグがインフラに誤作動を引き起こすかもしれないという||such as banking, power plants, and air traffic control.|銀行業務、発電所、航空管制などの",
            "reemerged",
        ),
    ],
    [
        (
            "In the 1990s, governments began to take the threat more seriously.",
            "1990年代になると、各国政府はこの脅威をより深刻に受け止め始めた。",
            "In the 1990s,|1990年代になると||governments began to take the threat more seriously.|各国政府はこの脅威をより深刻に受け止め始めた。",
            "began",
        ),
        (
            "Efforts centered around measures to deal with worst-case scenarios or focused on prevention by encouraging organizations in both public and private sectors to fix their computer codes.",
            "取り組みは、最悪の事態に対処するための対策を中心とするか、官民両部門の組織にコンピューターのコードを修正するよう促すことで予防に重点を置くものだった。",
            "Efforts centered around measures|取り組みは対策を中心としていた||to deal with worst-case scenarios|最悪の事態に対処するための||or focused on prevention|あるいは予防に重点を置いていた||by encouraging organizations in both public and private sectors|官民両部門の組織に促すことによって||to fix their computer codes.|コンピューターのコードを修正するよう",
            "centered",
        ),
        (
            "( 20 ), the United States funded efforts by the World Bank to increase awareness of the Y2K bug in developing nations, and the British government put the armed forces on standby, ready to assist the emergency services.",
            "( 20 )、アメリカは発展途上国でY2Kバグへの認識を高めるための世界銀行の取り組みに資金を提供し、イギリス政府は緊急サービスを支援できるよう軍を待機させた。",
        ),
    ],
    [
        (
            "On January 1, 2000, the more extreme predictions did not come to pass.",
            "2000年1月1日、より極端な予測は現実にはならなかった。",
            "On January 1, 2000,|2000年1月1日||the more extreme predictions did not come to pass.|より極端な予測は現実にはならなかった。",
            "did not come to pass",
        ),
        (
            "Although some issues arose, they were generally relatively minor and easy to resolve.",
            "いくつかの問題は発生したものの、それらはおおむね比較的軽微で、容易に解決できるものだった。",
            "Although some issues arose,|いくつかの問題は発生したものの||they were generally relatively minor|それらはおおむね比較的軽微で||and easy to resolve.|容易に解決できるものだった。",
            "were",
        ),
        (
            "For supporters of Y2K-bug initiatives, the ongoing viability of major computer systems and essential services was seen as a success; disaster had been avoided.",
            "Y2Kバグ対策の支持者にとって、主要なコンピューターシステムや不可欠なサービスが引き続き機能したことは成功と見なされた。大惨事は回避されたのである。",
            "For supporters of Y2K-bug initiatives,|Y2Kバグ対策の支持者にとって||the ongoing viability of major computer systems and essential services|主要なコンピューターシステムや不可欠なサービスが引き続き機能したことは||was seen as a success;|成功と見なされた||disaster had been avoided.|大惨事は回避されたのである。",
            "was seen",
        ),
        (
            "Some ( 21 ).",
            "一部の ( 21 ) 。",
        ),
        (
            "They questioned whether the threat had ever been as dangerous as predicted, and they suggested that governments had wasted billions of dollars on unnecessary prevention measures.",
            "彼らは、その脅威がそもそも予測されたほど危険だったのかと疑問を投げかけ、政府が不要な予防策に何十億ドルも浪費したのではないかと示唆した。",
            "They questioned|彼らは疑問を投げかけた||whether the threat had ever been as dangerous as predicted,|その脅威がそもそも予測されたほど危険だったのかと||and they suggested|そして示唆した||that governments had wasted billions of dollars on unnecessary prevention measures.|政府が不要な予防策に何十億ドルも浪費したと",
            "questioned",
        ),
    ],
]

TASTE_PARAGRAPHS = [
    [
        (
            "Scientists recognize five basic tastes: sweet, salty, sour, bitter, and umami.",
            "科学者は、甘味、塩味、酸味、苦味、うま味という5つの基本味を認めている。",
            "Scientists recognize five basic tastes:|科学者は5つの基本味を認めている||sweet, salty, sour, bitter, and umami.|甘味、塩味、酸味、苦味、うま味である。",
            "recognize",
        ),
        (
            "In 1908, the Japanese chemist Ikeda Kikunae identified umami as a distinct savory taste produced primarily by a chemical compound called glutamic acid.",
            "1908年、日本の化学者池田菊苗は、うま味を、主にグルタミン酸と呼ばれる化合物によって生み出される独特の風味豊かな味として特定した。",
            "In 1908,|1908年||the Japanese chemist Ikeda Kikunae identified umami|日本の化学者池田菊苗はうま味を特定した||as a distinct savory taste|独特の風味豊かな味として||produced primarily by a chemical compound called glutamic acid.|主にグルタミン酸と呼ばれる化合物によって生み出される",
            "identified",
        ),
        (
            "People had consumed foods rich in umami for centuries, including kombu, mushrooms, and fermented sauces.",
            "人々は何世紀にもわたって、昆布やキノコ、発酵調味料など、うま味の豊富な食品を口にしてきた。",
            "People had consumed foods rich in umami for centuries,|人々は何世紀にもわたってうま味の豊富な食品を口にしてきた||including kombu, mushrooms, and fermented sauces.|昆布、キノコ、発酵調味料などを含む",
            "had consumed",
        ),
        (
            "( 22 ), scientific agreement on umami’s status was difficult to reach.",
            "( 22 )、うま味の位置づけについて科学的な合意に達するのは難しかった。",
        ),
        (
            "In fact, it took nearly a hundred years of debate and experimental research before umami was recognized worldwide as a distinct basic taste.",
            "実際、うま味が独立した基本味として世界的に認められるまでには、100年近くにわたる議論と実験研究を要した。",
            "In fact,|実際||it took nearly a hundred years of debate and experimental research|100年近くの議論と実験研究を要した||before umami was recognized worldwide|うま味が世界的に認められるまでに||as a distinct basic taste.|独立した基本味として",
            "took",
        ),
    ],
    [
        (
            "Determining whether a new taste qualifies as “basic” is a complex process.",
            "新しい味が「基本味」に該当するかどうかを判断するのは、複雑なプロセスである。",
            "Determining whether a new taste qualifies as “basic”|新しい味が「基本味」に該当するかどうかを判断することは||is a complex process.|複雑なプロセスである。",
            "is a complex process",
        ),
        (
            "While there is no set of official criteria, scientists have proposed certain conditions that should be met.",
            "公式の基準があるわけではないが、科学者たちは満たされるべき一定の条件を提案してきた。",
            "While there is no set of official criteria,|公式の基準があるわけではないが||scientists have proposed certain conditions|科学者たちは一定の条件を提案してきた||that should be met.|満たされるべき",
            "have proposed",
        ),
        (
            "For one, the taste must be activated by distinct chemicals that are unrelated to other tastes.",
            "1つには、その味が、ほかの味とは無関係な独自の化学物質によって引き起こされなければならない。",
            "For one,|1つには||the taste must be activated by distinct chemicals|その味は独自の化学物質によって引き起こされなければならない||that are unrelated to other tastes.|ほかの味とは無関係な",
            "must be activated",
        ),
        (
            "In addition, the taste ( 23 ).",
            "加えて、その味は ( 23 ) 。",
        ),
        (
            "For example, when a person tastes something sweet, the chemical insulin is released into the bloodstream.",
            "たとえば、人が甘いものを味わうと、インスリンという化学物質が血流中に放出される。",
            "For example,|たとえば||when a person tastes something sweet,|人が甘いものを味わうと||the chemical insulin is released into the bloodstream.|インスリンという化学物質が血流中に放出される。",
            "is released",
        ),
    ],
    [
        (
            "In recent years, several possible candidates for a sixth taste have been proposed, including starchy and fatty.",
            "近年、6番目の味として、でんぷん味や脂肪味など、いくつかの候補が提案されている。",
            "In recent years,|近年||several possible candidates for a sixth taste have been proposed,|6番目の味の候補がいくつか提案されている||including starchy and fatty.|でんぷん味や脂肪味を含む",
            "have been proposed",
        ),
        (
            "Scientists are particularly interested in the fatty taste, as it has proved to be the strongest candidate so far.",
            "科学者たちは特に脂肪味に関心を寄せている。これまでのところ最も有力な候補であることが分かっているからだ。",
            "Scientists are particularly interested in the fatty taste,|科学者たちは特に脂肪味に関心を寄せている||as it has proved to be the strongest candidate so far.|これまでのところ最も有力な候補であることが分かっているからだ。",
            "are particularly interested",
        ),
        (
            "Fatty acids activate certain taste receptors that are located on the tongue, and the taste leads to measurable responses in the human body.",
            "脂肪酸は舌にある特定の味覚受容体を活性化し、その味は人体に測定可能な反応をもたらす。",
            "Fatty acids activate certain taste receptors|脂肪酸は特定の味覚受容体を活性化し||that are located on the tongue,|舌にある||and the taste leads to measurable responses in the human body.|その味は人体に測定可能な反応をもたらす。",
            "activate",
        ),
        (
            "Scientists point out that certain tastes ( 24 ).",
            "科学者たちは、ある種の味は ( 24 ) と指摘している。",
        ),
        (
            "For example, studies link reduced sensitivity to the fatty taste with overeating and conditions like obesity.",
            "たとえば、脂肪味に対する感度の低下を、過食や肥満などの症状と結びつける研究がある。",
            "For example,|たとえば||studies link reduced sensitivity to the fatty taste|研究は脂肪味に対する感度の低下を結びつけている||with overeating and conditions like obesity.|過食や肥満などの症状と",
            "link",
        ),
        (
            "Understanding taste more fully may help explain dietary choices and health outcomes.",
            "味覚をより深く理解することは、食の選択や健康上の結果を説明する助けになるかもしれない。",
            "Understanding taste more fully|味覚をより深く理解することは||may help explain dietary choices and health outcomes.|食の選択や健康上の結果を説明する助けになるかもしれない。",
            "may help",
        ),
    ],
]

Y2K_QUESTIONS = [
    {
        "number": 19,
        "choices": [
            "was the only viable option",
            "might have limitations",
            "could only be understood by scientists",
            "mainly benefited large businesses",
        ],
        "answer": 2,
        "choiceTranslations": [
            "唯一の実行可能な選択肢だった",
            "限界があるかもしれない",
            "科学者にしか理解できなかった",
            "主に大企業に利益をもたらした",
        ],
        "choiceAnalysis": [
            "❌ was the only viable option＝唯一の実行可能な選択肢だった。直後の For example で2000年を1900年と誤認する危険が挙げられており、方式を肯定する内容にはつながらない。",
            "✅ might have limitations＝限界があるかもしれない。For example 以下で2000年を1900年と誤って解釈する問題が具体例として示され、次の文で such concerns とまとめられている→正解。💡 空所直後の For example は、空所の内容を具体化する合図。",
            "❌ could only be understood by scientists＝科学者にしか理解できなかった。理解の難しさではなく、日付を誤って解釈するという欠陥が話題になっている。",
            "❌ mainly benefited large businesses＝主に大企業に利益をもたらした。後続の文は利点ではなく懸念（such concerns）を述べている。",
        ],
        "sourceEvidence": [
            "there was the question of what would happen in the year 2000 if computer systems incorrectly interpreted the final two digits to mean 1900 instead of 2000",
            "such concerns were largely brushed aside",
        ],
    },
    {
        "number": 20,
        "choices": ["Furthermore", "However", "In any case", "On the contrary"],
        "answer": 1,
        "choiceTranslations": ["さらに", "しかしながら", "いずれにせよ", "それどころか"],
        "choiceAnalysis": [
            "✅ Furthermore＝さらに。前の2文の「政府が脅威を深刻に受け止め、対策に乗り出した」に、アメリカの資金援助やイギリスの軍の待機という具体的な対策を付け加えている→正解。💡 同じ方向の情報を積み重ねる追加の接続表現。",
            "❌ However＝しかしながら。前後は対立しておらず、どちらも政府による対策の強化を述べている。",
            "❌ In any case＝いずれにせよ。それまでの話を切り上げて要点に戻る表現で、対策の例を付け加える流れには合わない。",
            "❌ On the contrary＝それどころか・反対に。前の内容を否定するときに使うが、後続文は前文を否定していない。",
        ],
        "sourceEvidence": [
            "governments began to take the threat more seriously",
            "the United States funded efforts by the World Bank to increase awareness of the Y2K bug in developing nations",
        ],
    },
    {
        "number": 21,
        "choices": [
            "governments wanted their money back",
            "problems could not be fixed",
            "new bugs were found",
            "people saw it differently",
        ],
        "answer": 4,
        "choiceTranslations": [
            "政府は資金を取り戻したいと考えた",
            "問題は修正できなかった",
            "新たなバグが見つかった",
            "人々は違った見方をした",
        ],
        "choiceAnalysis": [
            "❌ governments wanted their money back＝政府は資金を取り戻したいと考えた。後続文の They は政府の浪費を批判する側であり、政府自身が返金を求めたという記述はない。",
            "❌ problems could not be fixed＝問題は修正できなかった。前の文で、生じた問題は軽微で容易に解決できた（easy to resolve）と述べられている。",
            "❌ new bugs were found＝新たなバグが見つかった。新しいバグには触れておらず、後続文は対策の必要性への疑問を述べている。",
            "✅ people saw it differently＝人々は違った見方をした。支持者は成功と見なしたが、後続文では脅威の大きさを疑い、政府の浪費を指摘する人々が登場する→正解。💡 For supporters ... と Some ... の対比構造に注目する。",
        ],
        "sourceEvidence": [
            "They questioned whether the threat had ever been as dangerous as predicted",
            "governments had wasted billions of dollars on unnecessary prevention measures",
        ],
    },
]

TASTE_QUESTIONS = [
    {
        "number": 22,
        "choices": ["In exchange", "Consequently", "Nevertheless", "In short"],
        "answer": 3,
        "choiceTranslations": ["その代わりに", "その結果", "それにもかかわらず", "要するに"],
        "choiceAnalysis": [
            "❌ In exchange＝その代わりに。何かと引き換えにする関係は前後の文にない。",
            "❌ Consequently＝その結果。何世紀も食べられてきたことが、科学的合意の難しさの原因になったわけではない。",
            "✅ Nevertheless＝それにもかかわらず。うま味の豊富な食品は何世紀も食べられてきたのに、科学的な合意は得にくかったという逆接の関係→正解。💡 「長くなじみがある」と「合意が難しかった」という予想に反する流れを見抜く。",
            "❌ In short＝要するに。前の内容の要約ではなく、反対方向の新しい情報が続いている。",
        ],
        "sourceEvidence": [
            "People had consumed foods rich in umami for centuries",
            "it took nearly a hundred years of debate and experimental research before umami was recognized worldwide as a distinct basic taste",
        ],
    },
    {
        "number": 23,
        "choices": [
            "should be found in a range of food sources",
            "must trigger a physical response in the body",
            "should be easy for people to describe",
            "must last for a certain amount of time",
        ],
        "answer": 2,
        "choiceTranslations": [
            "さまざまな食品に含まれているべきだ",
            "体内で身体的な反応を引き起こさなければならない",
            "人々が説明しやすいものであるべきだ",
            "一定の時間持続しなければならない",
        ],
        "choiceAnalysis": [
            "❌ should be found in a range of food sources＝さまざまな食品に含まれているべきだ。直後の例は食品の種類ではなく、甘味を感じたときの体内の変化を挙げている。",
            "✅ must trigger a physical response in the body＝体内で身体的な反応を引き起こさなければならない。直後の For example で、甘いものを味わうとインスリンが血流に放出されると説明されている→正解。💡 第3段落の measurable responses in the human body もこの条件に対応している。",
            "❌ should be easy for people to describe＝人々が説明しやすいものであるべきだ。味を言葉で表す容易さには触れていない。",
            "❌ must last for a certain amount of time＝一定の時間持続しなければならない。味の持続時間についての記述はない。",
        ],
        "sourceEvidence": [
            "when a person tastes something sweet, the chemical insulin is released into the bloodstream",
            "the taste leads to measurable responses in the human body",
        ],
    },
    {
        "number": 24,
        "choices": [
            "could lose their significance in the future",
            "remain constant throughout a person’s lifetime",
            "often have cultural and historical significance",
            "influence eating behavior and health",
        ],
        "answer": 4,
        "choiceTranslations": [
            "将来その重要性を失う可能性がある",
            "生涯を通じて変わらない",
            "文化的・歴史的な意義を持つことが多い",
            "食行動や健康に影響を与える",
        ],
        "choiceAnalysis": [
            "❌ could lose their significance in the future＝将来その重要性を失う可能性がある。味の重要性が将来失われるという話は出てこない。",
            "❌ remain constant throughout a person’s lifetime＝生涯を通じて変わらない。直後の例は感度の低下（reduced sensitivity）を扱っており、一生変わらないという内容ではない。",
            "❌ often have cultural and historical significance＝文化的・歴史的な意義を持つことが多い。空所後の例は文化や歴史ではなく、過食や肥満という健康の話である。",
            "✅ influence eating behavior and health＝食行動や健康に影響を与える。直後の例で脂肪味への感度の低下が過食や肥満と結びつけられ、最終文でも dietary choices and health outcomes に触れている→正解。💡",
        ],
        "sourceEvidence": [
            "studies link reduced sensitivity to the fatty taste with overeating and conditions like obesity",
            "Understanding taste more fully may help explain dietary choices and health outcomes.",
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


SECTION2 = {
    "name": "大問2",
    "nameEn": "Part 2",
    "type": "passage-fill",
    "instruction": "次の英文A，Bを読み，その文意にそって(19)から(24)までの(　)に入れるのに最も適切なものを選びなさい。",
    "passages": [
        build_passage("A", "The Y2K Bug", Y2K_PARAGRAPHS, Y2K_QUESTIONS),
        build_passage("B", "Searching for a Sixth Taste", TASTE_PARAGRAPHS, TASTE_QUESTIONS),
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

    part1_indexes = [i for i, section in enumerate(sections) if section.get("name") == "大問1"]
    if len(part1_indexes) != 1:
        raise SystemExit(f"Expected exactly one 大問1 section, found {len(part1_indexes)}.")

    retained = [section for section in sections if section.get("name") != "大問2"]
    part1_index = next(i for i, section in enumerate(retained) if section.get("name") == "大問1")
    retained.insert(part1_index + 1, SECTION2)

    data["sections"] = retained
    with DATA_PATH.open("w", encoding="utf-8", newline="\n") as target:
        json.dump(data, target, ensure_ascii=False, indent=4)
        target.write("\n")

    print(f"Wrote {DATA_PATH}")
    print("大問2: 2 passages / 6 questions (Q19-Q24)")


if __name__ == "__main__":
    main()

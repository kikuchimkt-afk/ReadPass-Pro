# -*- coding: utf-8 -*-
"""Strictly verify 2026-1 Grade Pre-1 Part 3 against the official booklet."""

import json
import re
import sys
from pathlib import Path


sys.stdout.reconfigure(encoding="utf-8")


DATA_PATH = (
    Path(__file__).resolve().parent
    / "data"
    / "pre-grade1"
    / "2026-1"
    / "data.json"
)

SECTION_KEYS = {"name", "nameEn", "type", "instruction", "passages"}
PASSAGE_KEYS = {
    "label",
    "title",
    "paragraphs",
    "translations",
    "sentencePairs",
    "questions",
}
QUESTION_KEYS = {
    "number",
    "question",
    "questionTranslation",
    "choices",
    "choiceTranslations",
    "answer",
    "choiceAnalysis",
    "sourceEvidence",
}

EXPECTED_META = {
    "name": "大問3",
    "nameEn": "Part 3",
    "type": "reading-comprehension",
    "instruction": "次の英文A，Bの内容に関して，質問に対して最も適切なものを選びなさい。",
}

EXPECTED_PARAGRAPHS = {
    "A": [
        "The ancient settlement of Uruk was located in a fertile delta between the Tigris and Euphrates rivers in the region of Sumer, in what is now southern Iraq. Uruk began life as a village. However, toward the end of the fourth millennium BC, it had developed to such an extent that some historians consider it the world’s first city. Behind this remarkable growth were several factors, including technological advancements that increased agricultural efficiency, such as the construction of irrigation canals to funnel water to fields and orchards. These advances not only allowed Uruk to support a growing population but also to create a surplus, which could then be traded. Expansion continued, and by the third millennium BC, Uruk was thriving as a Sumerian cultural and religious center, a military power, and the hub of a trade network.",
        "As Uruk grew, it helped shape the political and cultural landscape of the Sumer region, influencing other cities that developed around the same period. Various other developments helped Uruk evolve into the sophisticated city it became, including its early use of cuneiform script. The script was mainly written on clay tablets, many of which survive to this day. In its early form, it was relatively simple, with pictures representing goods, but it allowed for rudimentary recordkeeping. The writing system gradually became more sophisticated and was used for accounting and general administrative matters, which helped facilitate the governance of the increasingly complex city. Over time, the script was used in the Sumer region to keep records in fields such as economics, politics, and religion.",
        "However, Uruk’s dominant position was not to last forever. Uruk had competed with neighboring Sumerian cities for hundreds of years, leaving them all vulnerable to forces from other regions. In the latter half of the third millennium BC, the Akkadians conquered much of Sumer. Despite this conquest, Uruk’s religious districts were respected and protected, and after Akkadian rule came to an end, a renaissance of Sumerian culture occurred. Although later conflicts and invasions meant that Uruk would not return to its earlier heights, it remained an important city for many centuries to come. Archaeological excavations have revealed an immense city wall, sculptures, artworks, large stone buildings decorated with mosaics, and numerous pyramid-like structures called ziggurats that were topped with temples—all of which point to the historical significance of Uruk.",
    ],
    "B": [
        "While the concept of artificially increasing animal intelligence through technology once seemed like science fiction, recent advances suggest it may be achievable. One promising approach for doing so is genetic manipulation. For instance, in 2014, researchers discovered that a human gene called FOXP2 was related to acquiring language skills in humans. When mice were genetically altered to produce it, they were able to learn a route through a maze much more rapidly than their unmodified counterparts, indicating that the gene had significantly enhanced their memory, which is an essential component of intelligence. This research is preliminary, however, and intelligence depends on a multitude of genes, so significant technical and ethical hurdles must be overcome before such advancements can be responsibly applied.",
        "An aspect of animal uplift that needs to be considered is the possibility of unintended outcomes. One experiment compared fish with larger brains that were bred together to fish with smaller brains that were bred together. The young of the larger-brained fish tended to have even bigger brains, and the babies’ performance on cognitive tests was superior to that of fish with smaller brains. However, the researchers also observed that these fish produced young that had smaller digestive systems, and this in turn seems to have led them to produce fewer offspring. This is likely due to the fact that larger brains require substantially more energy. As this experiment indicates, trying to boost intelligence may disrupt other physical attributes, leading to consequences that extend beyond the individual animals to entire populations.",
        "Furthermore, opponents of animal uplift point out that the process would likely involve surgical procedures on healthy animals. There would almost certainly be psychological consequences as well, and an uplifted animal’s existence might well be completely transformed. A mouse, whose life would normally be a simple matter of survival, could instead be thrust into a confusing, possibly terrifying awareness of how brief its lifespan is and how little control it has over its environment. There is also the issue of whether making such radical alterations to an animal’s biology could ever be considered ethical, since it would be impossible for the creature to give consent beforehand, especially since the procedures would probably not be reversible.",
        "George Dvorsky, chairperson of the Institute for Ethics and Emerging Technologies, however, argues that withholding animal uplift is itself unethical. Animals have long been sacrificed as test subjects during the creation of new surgical procedures or the development of medicines that have increased human life expectancy, and if humans artificially increase our own intelligence, animals will likely be sacrificed for that as well. According to Dvorsky, in light of increased awareness of animal rights and given the tremendous role that animals have played in improving human existence, withholding advances that could improve their intelligence would be just as unethical as withholding them from a group of humans who lack sufficient wealth to afford them. While the ability to uplift animals would have undeniable benefits, it is also true that we face an ethical dilemma when altering another species. Clearly, there are difficult decisions about animal uplift that need to be made.",
    ],
}

EXPECTED_TRANSLATIONS = {
    "A": [
        "古代の集落ウルクは、現在のイラク南部にあたるシュメール地方の、チグリス川とユーフラテス川にはさまれた肥沃な三角州に位置していた。ウルクは村として歴史を始めた。しかし紀元前4千年紀の終わりごろには、ウルクは大きく発展し、一部の歴史家が世界最初の都市とみなすほどになっていた。この著しい成長の背景には、農業効率を高めた技術の進歩など、いくつかの要因があった。その一例が、畑や果樹園へ水を導くための灌漑用水路の建設である。こうした進歩によって、ウルクは増え続ける人口を支えられただけでなく、余剰生産物を生み出し、それを交易に回すこともできた。拡大は続き、紀元前3千年紀までには、ウルクはシュメールの文化・宗教の中心地、軍事大国、そして交易網の要として繁栄していた。",
        "ウルクは成長するにつれて、シュメール地方の政治的・文化的な姿を形作り、同じ時期に発展したほかの都市にも影響を与えた。そのほかにもさまざまな発展が、ウルクが洗練された都市へ進化する助けとなった。その中には、くさび形文字を早くから使用したことも含まれていた。その文字は主に粘土板に書かれ、その多くが今日まで残っている。初期の形は比較的単純で、品物を表す絵から成っていたが、基本的な記録管理を可能にした。この文字体系は次第に複雑になり、会計や一般行政に使われるようになった。それによって、ますます複雑化する都市の統治が円滑になった。やがて、その文字はシュメール地方で、経済・政治・宗教などの分野の記録を残すために使われた。",
        "しかし、ウルクの支配的な地位が永遠に続くことはなかった。ウルクは近隣のシュメール諸都市と何百年も競い合っており、そのためそれらすべての都市が他地域の勢力に対して脆弱になっていた。紀元前3千年紀後半、アッカド人がシュメールの大部分を征服した。この征服にもかかわらず、ウルクの宗教地区は尊重され、保護された。そしてアッカド人の支配が終わると、シュメール文化の復興が起こった。その後の争いや侵略によってウルクがかつての隆盛を取り戻すことはなかったが、その後も何世紀にもわたって重要な都市であり続けた。考古学的発掘によって、巨大な市壁、彫刻、美術品、モザイクで装飾された大きな石造建築、さらに神殿を頂くジッグラトと呼ばれる多数のピラミッド状建造物が明らかになっており、そのすべてがウルクの歴史的重要性を示している。",
    ],
    "B": [
        "技術によって動物の知能を人為的に高めるという発想は、かつてはSFのように思われたが、最近の進歩はそれが実現可能かもしれないことを示している。そのための有望な方法の一つが遺伝子操作である。たとえば2014年、研究者たちはFOXP2と呼ばれるヒトの遺伝子が、人間の言語能力の獲得に関係していることを発見した。マウスがFOXP2を発現するよう遺伝的に改変されると、改変されていないマウスよりはるかに速く迷路の経路を覚えられた。このことは、その遺伝子が、知能に欠かせない要素である記憶力を大幅に高めたことを示している。しかし、この研究はまだ予備段階であり、知能は多数の遺伝子に左右される。そのため、このような進歩を責任ある形で応用できるようになるまでには、技術上・倫理上の大きな障壁を克服しなければならない。",
        "動物の知能向上について考慮すべき一面は、意図しない結果が生じる可能性である。ある実験では、脳の大きな魚どうしを交配した群と、脳の小さな魚どうしを交配した群を比較した。脳の大きな魚の子はさらに大きな脳を持つ傾向があり、それらの稚魚の認知テストの成績は、脳の小さな魚の稚魚より優れていた。しかし研究者たちは、これらの魚が消化器官の小さい子を産むことも観察し、それが今度は子の数を減らしたとみられる。これは、脳が大きいほどかなり多くのエネルギーを必要とするためだと考えられる。この実験が示すように、知能を高めようとするとほかの身体的特徴が損なわれ、個体だけでなく集団全体にまで及ぶ結果を招く可能性がある。",
        "さらに、動物の知能向上に反対する人々は、その過程では健康な動物に外科的処置を施す可能性が高いと指摘する。心理面の影響もほぼ確実に生じ、知能を高められた動物の生き方は一変しかねない。通常ならただ生き延びるだけの単純な一生を送るマウスが、代わりに、自分の寿命がいかに短く、環境をほとんど制御できないかという、混乱を招き恐怖さえ伴う認識へと突然追いやられるかもしれない。また、動物の生物学的特徴をこのように根本から変えることが倫理的といえるのかという問題もある。動物が事前に同意することは不可能であり、処置が元に戻せない可能性が高いだけになおさらである。",
        "しかし、倫理・新興技術研究所の代表ジョージ・ドヴォルスキーは、動物の知能向上を行わないこと自体が非倫理的だと主張する。動物は、人間の寿命を延ばしてきた新しい外科処置や医薬品の開発において、長年実験対象として犠牲にされてきた。そして人間が自らの知能を人為的に高めるなら、そのためにも動物が犠牲にされる可能性が高い。ドヴォルスキーによれば、動物の権利への意識が高まり、動物が人間の生活向上に果たしてきた大きな役割を考えれば、動物の知能を高めうる進歩を与えないことは、それを購入できるだけの財力がない人間の集団に同じ進歩を与えないことと同様に非倫理的である。動物の知能を高める能力には否定できない利点がある一方、別の種を改変するとき私たちが倫理的ジレンマに直面することも事実である。明らかに、動物の知能向上については難しい判断を下さなければならない。",
    ],
}

EXPECTED_PASSAGES = {
    "A": {"title": "Uruk", "pair_counts": [6, 6, 6], "questions": [25, 26, 27]},
    "B": {
        "title": "Animal Uplift",
        "pair_counts": [5, 6, 4, 5],
        "questions": [28, 29, 30, 31],
    },
}

EXPECTED_QUESTIONS = {
    25: {
        "question": "What does the author of the passage say about Uruk’s development?",
        "choices": [
            "Rapid progress would have been possible even without the technological advances that increased agricultural efficiency.",
            "One important characteristic was its ability to produce more food than it needed, which allowed for more rapid change to occur.",
            "The construction of canals for agricultural use could not keep up with the needs of a growing population.",
            "It lost out on the most profitable trade deals because it reserved too much of its crop harvests for its own population.",
        ],
        "answer": 2,
        "sourceEvidence": [
            "These advances not only allowed Uruk to support a growing population but also to create a surplus, which could then be traded."
        ],
    },
    26: {
        "question": "What is one thing we learn about the cuneiform script?",
        "choices": [
            "The benefits its use provided were not enough to enable Uruk to stay ahead of rival cities.",
            "Although it had uses that aided development in Uruk, it was less suited to complex bureaucratic tasks.",
            "It was first developed for religious purposes but was later adopted for use in commerce and government.",
            "It provided Uruk with a means to help manage the administration of its increasingly complex society.",
        ],
        "answer": 4,
        "sourceEvidence": [
            "The writing system gradually became more sophisticated and was used for accounting and general administrative matters, which helped facilitate the governance of the increasingly complex city."
        ],
    },
    27: {
        "question": "Which of the following statements is true, based on the final paragraph?",
        "choices": [
            "Even though the Sumer region was attacked and defeated by outside forces, the religious heritage of Uruk was not destroyed.",
            "Uruk borrowed some of its religious architecture and artistic techniques from neighboring cities in Sumer.",
            "The Akkadians had to destroy much of the wall and stone buildings in order to defeat Uruk.",
            "Uruk’s decline can be attributed to the fact that neighboring Sumerian cities created alliances with the Akkadians.",
        ],
        "answer": 1,
        "sourceEvidence": [
            "Despite this conquest, Uruk’s religious districts were respected and protected"
        ],
    },
    28: {
        "question": "What is one thing that we learn about the research into the FOXP2 gene?",
        "choices": [
            "Since it only had a minor effect on the mice’s memory, it cannot really be said to have improved their overall intelligence.",
            "Although it affected one element of the mice’s intelligence, it is just an early step in what will most likely be a complicated process.",
            "It demonstrated that the way that mice communicated with each other was more sophisticated than had previously been believed.",
            "It indicates that mice may actually have a form of intelligence that researchers were not aware of in the past.",
        ],
        "answer": 2,
        "sourceEvidence": [
            "indicating that the gene had significantly enhanced their memory, which is an essential component of intelligence",
            "This research is preliminary, however, and intelligence depends on a multitude of genes",
        ],
    },
    29: {
        "question": "What does the fish experiment indicate about attempts at animal uplift?",
        "choices": [
            "There are limits to how intelligent animals can become, and no amount of breeding will ever be able to overcome them.",
            "It is possible that an attempt to increase animal intelligence will actually have the opposite of its intended effect.",
            "Attempts to increase an animal’s intelligence could interfere with other important aspects of the animal’s biology.",
            "While it is possible to slightly increase animal intelligence, it is not likely that it will be inherited by an animal’s offspring.",
        ],
        "answer": 3,
        "sourceEvidence": [
            "trying to boost intelligence may disrupt other physical attributes, leading to consequences that extend beyond the individual animals to entire populations"
        ],
    },
    30: {
        "question": "One argument against animal uplift that is presented in the third paragraph is that",
        "choices": [
            "it should not be carried out because it is impossible for animals to agree to what is going to happen to them.",
            "it could bring about significant changes in animal behavior that could, in turn, have negative effects on the environment.",
            "there are likely to be more risks in performing operations on animals’ brains due to our lack of knowledge about how they function.",
            "there is a significant risk that the effects of the procedure could reduce the survival instincts of animals that receive it.",
        ],
        "answer": 1,
        "sourceEvidence": [
            "it would be impossible for the creature to give consent beforehand, especially since the procedures would probably not be reversible"
        ],
    },
    31: {
        "question": "What does George Dvorsky believe about animal uplift?",
        "choices": [
            "Humans need to develop better types of surgical procedures so that we do not harm animals when trying to uplift them.",
            "It is likely that the same medical advances that are used to uplift animals will also help them to live longer, healthier lives.",
            "Humans should develop the technology necessary for uplifting animals before we consider whether it is right to do so or not.",
            "If humans use animals in the process of increasing our own intelligence, that would increase our obligation to uplift them.",
        ],
        "answer": 4,
        "sourceEvidence": [
            "if humans artificially increase our own intelligence, animals will likely be sacrificed for that as well",
            "withholding advances that could improve their intelligence would be just as unethical as withholding them from a group of humans who lack sufficient wealth to afford them",
        ],
    },
}


def norm(text):
    return re.sub(r"\s+", " ", text or "").strip()


def has_japanese(text):
    return bool(re.search(r"[\u3040-\u30ff\u3400-\u9fff]", text or ""))


def add_error(errors, message):
    errors.append(message)


def verify_sentence_pairs(passage, expected, errors):
    label = passage.get("label", "?")
    pairs = passage.get("sentencePairs")
    if not isinstance(pairs, list):
        add_error(errors, f"passage {label}: sentencePairs is not a list")
        return

    pair_counts = expected["pair_counts"]
    expected_total = sum(pair_counts)
    if len(pairs) != expected_total:
        add_error(
            errors,
            f"passage {label}: sentencePairs={len(pairs)} expected={expected_total}",
        )

    pair_english = []
    pair_japanese = []
    for index, pair in enumerate(pairs, 1):
        if (
            not isinstance(pair, list)
            or len(pair) != 4
            or not all(isinstance(item, str) and item.strip() for item in pair)
        ):
            add_error(
                errors,
                f"passage {label}: sentencePair {index} must be 4 nonempty strings",
            )
            continue

        english, japanese, slash, main_verb = pair
        pair_english.append(english)
        pair_japanese.append(japanese)
        if not has_japanese(japanese):
            add_error(errors, f"passage {label}: sentencePair {index} has no Japanese")

        slash_units = slash.split("||")
        if len(slash_units) < 2:
            add_error(
                errors,
                f"passage {label}: sentencePair {index} needs at least 2 slash units",
            )
            continue

        english_units = []
        for unit_number, unit in enumerate(slash_units, 1):
            if unit.count("|") != 1:
                add_error(
                    errors,
                    f"passage {label}: sentencePair {index} slash unit {unit_number} must contain one |",
                )
                continue
            slash_english, slash_japanese = unit.split("|", 1)
            if not slash_english.strip() or not slash_japanese.strip():
                add_error(
                    errors,
                    f"passage {label}: sentencePair {index} slash unit {unit_number} is empty",
                )
            if not has_japanese(slash_japanese):
                add_error(
                    errors,
                    f"passage {label}: sentencePair {index} slash unit {unit_number} has no Japanese",
                )
            english_units.append(slash_english)

        if norm(" ".join(english_units)) != norm(english):
            add_error(
                errors,
                f"passage {label}: sentencePair {index} slash English cannot reconstruct source",
            )
        main_verb_matches = list(re.finditer(re.escape(main_verb), english, re.IGNORECASE))
        if len(main_verb_matches) != 1:
            add_error(
                errors,
                f"passage {label}: sentencePair {index} main verb must have one unambiguous literal match",
            )
        if not re.search(rf"(?<!\w){re.escape(main_verb)}(?!\w)", english, re.IGNORECASE):
            add_error(
                errors,
                f"passage {label}: sentencePair {index} main verb match must use word boundaries",
            )

    expected_corpus = " ".join(EXPECTED_PARAGRAPHS[label])
    if norm(" ".join(pair_english)) != norm(expected_corpus):
        add_error(errors, f"passage {label}: sentencePairs do not cover the full text")

    translations = passage.get("translations", [])
    offset = 0
    reconstructed_translations = []
    for count in pair_counts:
        reconstructed_translations.append("".join(pair_japanese[offset : offset + count]))
        offset += count
    if reconstructed_translations != translations:
        add_error(
            errors,
            f"passage {label}: sentencePair Japanese does not reconstruct translations",
        )


def verify_question(question, corpus, errors):
    number = question.get("number")
    expected = EXPECTED_QUESTIONS.get(number)
    if expected is None:
        add_error(errors, f"unexpected question number: {number}")
        return

    if set(question) != QUESTION_KEYS:
        add_error(
            errors,
            f"Q{number}: keys={sorted(question)} expected={sorted(QUESTION_KEYS)}",
        )
    if question.get("question") != expected["question"]:
        add_error(errors, f"Q{number}: official question text mismatch")
    if question.get("choices") != expected["choices"]:
        add_error(errors, f"Q{number}: official choices mismatch")
    if question.get("answer") != expected["answer"]:
        add_error(
            errors,
            f"Q{number}: answer={question.get('answer')} expected={expected['answer']}",
        )

    question_translation = question.get("questionTranslation")
    if not isinstance(question_translation, str) or not has_japanese(question_translation):
        add_error(errors, f"Q{number}: missing Japanese questionTranslation")

    choice_translations = question.get("choiceTranslations")
    if (
        not isinstance(choice_translations, list)
        or len(choice_translations) != 4
        or any(not isinstance(text, str) or not has_japanese(text) for text in choice_translations)
    ):
        add_error(errors, f"Q{number}: choiceTranslations must be 4 Japanese strings")

    analyses = question.get("choiceAnalysis")
    if not isinstance(analyses, list) or len(analyses) != 4:
        add_error(errors, f"Q{number}: choiceAnalysis must contain 4 items")
    else:
        for index, analysis in enumerate(analyses, 1):
            if not isinstance(analysis, str) or not analysis.strip():
                add_error(errors, f"Q{number}: choiceAnalysis {index} is empty")
                continue
            if index == expected["answer"]:
                if not analysis.startswith("✅ "):
                    add_error(errors, f"Q{number}: correct analysis must start with ✅")
                if analysis.count("→正解。💡") != 1:
                    add_error(
                        errors,
                        f"Q{number}: correct analysis needs one exact →正解。💡 marker",
                    )
            else:
                if not analysis.startswith("❌ "):
                    add_error(errors, f"Q{number}: wrong analysis {index} must start with ❌")
                if "→正解" in analysis:
                    add_error(errors, f"Q{number}: wrong analysis {index} says correct")

    evidence = question.get("sourceEvidence")
    if evidence != expected["sourceEvidence"]:
        add_error(errors, f"Q{number}: sourceEvidence differs from audited source")
    if not isinstance(evidence, list) or not evidence:
        add_error(errors, f"Q{number}: sourceEvidence must be a nonempty list")
    else:
        for snippet in evidence:
            if not isinstance(snippet, str) or not snippet.strip():
                add_error(errors, f"Q{number}: sourceEvidence contains an empty item")
            elif snippet not in corpus:
                add_error(
                    errors,
                    f"Q{number}: sourceEvidence is not an exact substring of passage",
                )


def main():
    if not DATA_PATH.is_file():
        print(f"ERROR: data.json が見つかりません: {DATA_PATH}")
        return 1

    with DATA_PATH.open(encoding="utf-8") as source:
        data = json.load(source)

    errors = []
    matches = [
        section
        for section in data.get("sections", [])
        if isinstance(section, dict) and section.get("name") == "大問3"
    ]
    if len(matches) != 1:
        add_error(errors, f"大問3 must appear exactly once; found={len(matches)}")
        section = matches[0] if matches else None
    else:
        section = matches[0]

    if section is not None:
        if set(section) != SECTION_KEYS:
            add_error(
                errors,
                f"section keys={sorted(section)} expected={sorted(SECTION_KEYS)}",
            )
        for key, expected_value in EXPECTED_META.items():
            if section.get(key) != expected_value:
                add_error(errors, f"section {key} mismatch")

        passages = section.get("passages")
        if not isinstance(passages, list) or len(passages) != 2:
            add_error(errors, "大問3 passages must contain exactly A and B")
            passages = passages if isinstance(passages, list) else []

        labels = [passage.get("label") for passage in passages if isinstance(passage, dict)]
        if labels != ["A", "B"]:
            add_error(errors, f"passage labels/order={labels} expected=['A', 'B']")

        seen_questions = []
        for passage in passages:
            if not isinstance(passage, dict):
                add_error(errors, "passage is not an object")
                continue
            label = passage.get("label")
            expected_passage = EXPECTED_PASSAGES.get(label)
            if expected_passage is None:
                add_error(errors, f"unexpected passage label: {label}")
                continue
            if set(passage) != PASSAGE_KEYS:
                add_error(
                    errors,
                    f"passage {label}: keys={sorted(passage)} expected={sorted(PASSAGE_KEYS)}",
                )
            if passage.get("title") != expected_passage["title"]:
                add_error(errors, f"passage {label}: title mismatch")
            if passage.get("paragraphs") != EXPECTED_PARAGRAPHS[label]:
                add_error(errors, f"passage {label}: official paragraph text mismatch")

            translations = passage.get("translations")
            if (
                not isinstance(translations, list)
                or len(translations) != len(EXPECTED_PARAGRAPHS[label])
                or any(not isinstance(text, str) or not has_japanese(text) for text in translations)
            ):
                add_error(
                    errors,
                    f"passage {label}: translations must cover every paragraph in Japanese",
                )
            if translations != EXPECTED_TRANSLATIONS[label]:
                add_error(errors, f"passage {label}: audited full translation mismatch")

            verify_sentence_pairs(passage, expected_passage, errors)

            questions = passage.get("questions")
            if not isinstance(questions, list):
                add_error(errors, f"passage {label}: questions is not a list")
                continue
            numbers = [q.get("number") for q in questions if isinstance(q, dict)]
            if numbers != expected_passage["questions"]:
                add_error(
                    errors,
                    f"passage {label}: question numbers={numbers} expected={expected_passage['questions']}",
                )
            corpus = " ".join(passage.get("paragraphs", []))
            for question in questions:
                if not isinstance(question, dict):
                    add_error(errors, f"passage {label}: question is not an object")
                    continue
                seen_questions.append(question.get("number"))
                verify_question(question, corpus, errors)

        if seen_questions != list(range(25, 32)):
            add_error(errors, f"question sequence={seen_questions} expected=25..31")

        actual_pairs = {
            pair[0]: pair[1:]
            for passage in passages
            for pair in passage.get("sentencePairs", [])
            if isinstance(pair, list) and len(pair) == 4
        }
        critical_pairs = {
            "These advances not only allowed Uruk to support a growing population but also to create a surplus, which could then be traded.": [
                "こうした進歩によって、ウルクは増え続ける人口を支えられただけでなく、余剰生産物を生み出し、それを交易に回すこともできた。",
                "These advances|こうした進歩によって||not only allowed Uruk to support a growing population|ウルクは増え続ける人口を支えられただけでなく||but also to create a surplus,|余剰生産物を生み出すこともでき||which could then be traded.|それを交易に回すこともできた。",
                "allowed",
            ],
            "When mice were genetically altered to produce it, they were able to learn a route through a maze much more rapidly than their unmodified counterparts, indicating that the gene had significantly enhanced their memory, which is an essential component of intelligence.": [
                "マウスがFOXP2を発現するよう遺伝的に改変されると、改変されていないマウスよりはるかに速く迷路の経路を覚えられた。このことは、その遺伝子が、知能に欠かせない要素である記憶力を大幅に高めたことを示している。",
                "When mice were genetically altered|マウスが遺伝的に改変されると||to produce it,|FOXP2を発現するように||they were able to learn a route|経路を覚えることができた||through a maze|迷路を通る||much more rapidly than their unmodified counterparts,|改変されていないマウスよりはるかに速く||indicating that the gene had significantly enhanced their memory,|その遺伝子が記憶力を大幅に高めたことを示しており||which is an essential component of intelligence.|それは知能に欠かせない要素である。",
                "were able",
            ],
            "The young of the larger-brained fish tended to have even bigger brains, and the babies’ performance on cognitive tests was superior to that of fish with smaller brains.": [
                "脳の大きな魚の子はさらに大きな脳を持つ傾向があり、それらの稚魚の認知テストの成績は、脳の小さな魚の稚魚より優れていた。",
                "The young of the larger-brained fish|脳の大きな魚の子は||tended to have even bigger brains,|さらに大きな脳を持つ傾向があり||and the babies’ performance|そしてそれらの稚魚の成績は||on cognitive tests|認知テストでの||was superior to that|それより優れていた||of fish with smaller brains.|脳の小さな魚の稚魚より。",
                "tended",
            ],
            "However, the researchers also observed that these fish produced young that had smaller digestive systems, and this in turn seems to have led them to produce fewer offspring.": [
                "しかし研究者たちは、これらの魚が消化器官の小さい子を産むことも観察し、それが今度は子の数を減らしたとみられる。",
                "However, the researchers also observed|しかし研究者たちはさらに観察した||that these fish produced young|これらの魚が子を産むことを||that had smaller digestive systems,|より小さな消化器官を持つ||and this in turn seems to have led them|そしてそのことが今度は、それらの魚が||to produce fewer offspring.|より少ない子しか産まないことにつながったようだ。",
                "observed",
            ],
            "This is likely due to the fact that larger brains require substantially more energy.": [
                "これは、脳が大きいほどかなり多くのエネルギーを必要とするためだと考えられる。",
                "This is likely due to the fact|これはおそらく〜という事実による||that larger brains require|大きな脳ほど必要とする||substantially more energy.|はるかに多くのエネルギーを。",
                "is likely due",
            ],
        }
        for sentence, expected_pair in critical_pairs.items():
            if actual_pairs.get(sentence) != expected_pair:
                add_error(errors, f"audited critical sentencePair regressed: {sentence}")

    print(
        "section3 passages=2 questions=7 sentencePairs=38 "
        f"errors={len(errors)}"
    )
    for error in errors:
        print(f"  {error}")
    if errors:
        return 1
    print("OK: 2026-1 Grade Pre-1 Part 3 verified")
    return 0


if __name__ == "__main__":
    sys.exit(main())

# -*- coding: utf-8 -*-
"""Install the five lesson focus points for Grade Pre-1 2026-2.

Practice passages are built from the official passages already stored in
data.json (blanks filled with the official answers), so they always match
the exam text. Audio paths (audioFile) are added later by
data/pre-grade1/2026-2/_gen_tts.py once the MP3 files exist.
"""

from __future__ import annotations

import json
import re
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "pre-grade1" / "2026-2" / "data.json"

# Official answers for the Part 2 blanks, in English and in the Japanese
# wording that reads naturally inside the stored translations.
BLANK_FILLS = {
    19: ("might have limitations", "限界を抱えているかもしれない"),
    20: ("Furthermore", "さらに"),
    21: ("people saw it differently", "人々は違った見方をした"),
    22: ("Nevertheless", "それにもかかわらず"),
    23: ("must trigger a physical response in the body", "体内で身体的な反応を引き起こさなければならない"),
    24: ("influence eating behavior and health", "食行動や健康に影響を与える"),
}
BLANK_RE = re.compile(r"\(\s*(\d+)\s*\)")
JA_BLANK_RE = re.compile(r"\s*\(\s*(\d+)\s*\)\s*")

FOCUS_POINTS = [
    {
        "id": "fp1",
        "title": "concerns reemerged that... / the question of what...（名詞の内容を説明する同格表現）",
        "subtitle": "Appositive Clauses Separated from Their Nouns",
        "explanation": "大問2A「The Y2K Bug」では、concerns や the question といった名詞の「中身」を、後ろの that 節や of + 疑問詞節で説明しています。特に concerns reemerged that ... では、同格の that 節が名詞 concerns の直後ではなく、動詞 reemerged の後ろに回されています。長い同格節を主語の直後に置くと主語が重くなりすぎるため、英語では重い要素を文末に送ることがあります。名詞と同格節が離れていても、that 以下がどの名詞の内容なのかを見抜くことが、準1級の長文を正確に読む鍵になります。",
        "sourceQuote": "concerns reemerged that this so-called Y2K bug might cause malfunctions in infrastructure",
        "sourceLocation": "Part 2A「The Y2K Bug」第1段落",
        "examples": [
            {
                "en": "As the new millennium approached, however, concerns reemerged that this so-called Y2K bug might cause malfunctions in infrastructure.",
                "ja": "しかし、新たな千年紀が近づくと、このいわゆるY2Kバグがインフラに誤作動を引き起こすかもしれないという懸念が再び浮上した。",
                "note": "that 節は concerns の内容を表す同格節です。主語 concerns と同格節の間に動詞 reemerged が入っています。",
            },
            {
                "en": "Rumors spread that the company would soon close its factory.",
                "ja": "その会社がまもなく工場を閉鎖するといううわさが広まった。",
                "note": "Rumors that ... spread とすると主語が長くなるため、同格節を動詞の後ろに回しています。",
            },
            {
                "en": "There was the question of what would happen in the year 2000.",
                "ja": "2000年に何が起こるのかという問題があった。",
                "note": "of + 疑問詞節も同格の働きをし、question の具体的な中身を示します。",
            },
        ],
        "practicePassage": {"passage": "The Y2K Bug", "paragraphs": [0, 1, 2]},
        "practiceQuestions": [
            {
                "q": "concerns reemerged that ... の that 節は何を説明していますか？",
                "a": "主語 concerns の中身、つまり「このいわゆるY2Kバグが、銀行業務や発電所などのインフラに誤作動を引き起こすかもしれない」という懸念の内容を説明する同格節です。",
            },
            {
                "q": "その that 節が concerns の直後ではなく reemerged の後ろに置かれているのはなぜですか？",
                "a": "長い同格節を主語の直後に置くと主語が重くなり、動詞 reemerged が文末で孤立してしまうためです。英語では重い要素を文末に回す傾向があります。",
            },
            {
                "q": "the question of what would happen in the year 2000 の of はどのような働きをしていますか？",
                "a": "同格の of です。question の内容が「2000年に何が起こるのか」という間接疑問であることを示しています。",
            },
            {
                "q": "Q19で might have limitations を選ぶ手がかりになる表現を2つ挙げてください。",
                "a": "空所直後の For example 以下にある、下2桁を誤って1900年と解釈する問題の例と、次の文でそれをまとめた such concerns です。",
            },
        ],
        "highlightPatterns": [
            "concerns reemerged that this so-called Y2K bug might cause malfunctions in infrastructure",
            "there was the question of what would happen in the year 2000",
        ],
        "highlightColor": "#FF6B6B",
        "highlightLabel": "同格表現",
    },
    {
        "id": "fp2",
        "title": "it took nearly a hundred years ... before ...（実現までにかかった時間）",
        "subtitle": "It Took + Time + Before S V",
        "explanation": "大問2B「Searching for a Sixth Taste」では、うま味が基本味として認められるまでの長い道のりを、it took + 時間 + before S V で表しています。この構文は「SがVするまでに～の時間がかかった」という意味で、before は「～する前に」ではなく「～するまでに」と訳すと自然です。文頭の In fact は、直前の「合意に達するのは難しかった」を具体的な事実で裏付ける働きをしています。また、Determining whether ... is a complex process のように動名詞句が長い主語になる文では、主語の終わり（動詞 is の直前）を見極めることが大切です。",
        "sourceQuote": "it took nearly a hundred years of debate and experimental research before umami was recognized worldwide as a distinct basic taste",
        "sourceLocation": "Part 2B「Searching for a Sixth Taste」第1段落",
        "examples": [
            {
                "en": "It took nearly a hundred years of debate before umami was recognized as a basic taste.",
                "ja": "うま味が基本味として認められるまでに、100年近くの議論を要した。",
                "note": "it took + 時間 + before S V＝「SがVするまでに～かかった」。before は「～するまでに」と訳します。",
            },
            {
                "en": "It will be a long time before the new bridge is completed.",
                "ja": "新しい橋が完成するまでには長い時間がかかるだろう。",
                "note": "未来のことでも、時を表す before 節の中は現在形（is completed）を使います。",
            },
            {
                "en": "Determining whether a new taste qualifies as “basic” is a complex process.",
                "ja": "新しい味が「基本味」に該当するかどうかを判断するのは、複雑なプロセスである。",
                "note": "動名詞句 Determining whether ... “basic” 全体が主語で、動詞は is です。whether は「～かどうか」。",
            },
        ],
        "practicePassage": {"passage": "Searching for a Sixth Taste", "paragraphs": [0, 1, 2]},
        "practiceQuestions": [
            {
                "q": "it took nearly a hundred years ... before umami was recognized を自然な日本語にしてください。",
                "a": "「うま味が独立した基本味として世界的に認められるまでに、100年近くにわたる議論と実験研究を要した」です。before は「～するまでに」と訳します。",
            },
            {
                "q": "第1段落の In fact はどのような働きをしていますか？",
                "a": "直前の「うま味の位置づけについて科学的な合意に達するのは難しかった」を、100年近くかかったという具体的な事実で裏付けて強めています。",
            },
            {
                "q": "Determining whether a new taste qualifies as “basic” is a complex process. の主語と動詞を答えてください。",
                "a": "主語は動名詞句 Determining whether a new taste qualifies as “basic”、動詞は is です。",
            },
            {
                "q": "Q22で Nevertheless が正解になる理由を説明してください。",
                "a": "うま味の豊富な食品は何世紀も食べられてきたのに、科学的な合意は得にくかったという、予想に反する逆接の関係だからです。",
            },
        ],
        "highlightPatterns": [
            "it took nearly a hundred years of debate and experimental research before umami was recognized worldwide",
            "Determining whether a new taste qualifies as “basic” is a complex process",
        ],
        "highlightColor": "#4ECDC4",
        "highlightLabel": "時間の経過",
    },
    {
        "id": "fp3",
        "title": "a policy approach that some experts believe ignores...（連鎖関係詞節）",
        "subtitle": "Relative Clauses with an Inserted Opinion Verb",
        "explanation": "大問3A「Employment Requirements for Welfare」の最終文では、a policy approach that some experts believe ignores ... という連鎖関係詞節が使われています。関係代名詞 that の直後に some experts believe が挿入され、that は ignores の主語になっています。「一部の専門家が～を無視していると考える政策手法」と、挿入部分を先に訳すと自然です。同じ文章の what are known as ～（いわゆる～）も、先行詞を含む関係代名詞 what を使った表現で、政策上の呼び名と現実の状況とのずれを示す重要な合図になっています。",
        "sourceQuote": "a policy approach that some experts believe ignores both human needs and economic realities",
        "sourceLocation": "Part 3A「Employment Requirements for Welfare」第3段落",
        "examples": [
            {
                "en": "The flaws reveal a policy approach that some experts believe ignores both human needs and economic realities.",
                "ja": "その欠陥は、一部の専門家が人々の必要と経済の現実の両方を無視していると考える政策手法を浮き彫りにしている。",
                "note": "that（主語）＋ some experts believe（挿入）＋ ignores（動詞）の語順です。",
            },
            {
                "en": "He hired a coach who he thought could improve the team’s results.",
                "ja": "彼は、チームの成績を改善できると思ったコーチを雇った。",
                "note": "who は could improve の主語です。he thought は挿入なので、who を whom にはしません。",
            },
            {
                "en": "The policy is meant to apply to what are known as able-bodied adults without dependents.",
                "ja": "その政策は、いわゆる扶養家族のいない健常な成人に適用されることになっている。",
                "note": "what are known as ～＝「～として知られるもの（人々）」→「いわゆる～」。",
            },
        ],
        "practicePassage": {"passage": "Employment Requirements for Welfare", "paragraphs": [1, 2]},
        "practiceQuestions": [
            {
                "q": "a policy approach that some experts believe ignores ... の that の働きと、ignores の主語を答えてください。",
                "a": "that は主格の関係代名詞で、ignores の主語です。some experts believe が挿入され、「一部の専門家が～を無視していると考える政策手法」となります。",
            },
            {
                "q": "この連鎖関係詞節を、関係代名詞を使わずに2文に分けて書いてください。",
                "a": "It is a policy approach. Some experts believe (that) it ignores both human needs and economic realities. のようになります。",
            },
            {
                "q": "what are known as able-bodied adults without dependents の意味と構造を説明してください。",
                "a": "what は先行詞を含む関係代名詞で「～として知られる人々」→「いわゆる扶養家族のいない健常な成人」という意味です。政策上の分類名であることを示しています。",
            },
            {
                "q": "Q26の正解選択肢で、本文の rigid policy definitions と real-world conditions の食い違いはどう言い換えられていますか？",
                "a": "barriers to employment that are real but may not be covered by official policies（現実に存在するが、公式の政策では考慮されないかもしれない就労の障壁）と言い換えられています。",
            },
        ],
        "highlightPatterns": [
            "a policy approach that some experts believe ignores both human needs and economic realities",
            "what are known as able-bodied adults without dependents",
        ],
        "highlightColor": "#45B7D1",
        "highlightLabel": "連鎖関係詞",
    },
    {
        "id": "fp4",
        "title": "a base from which to intercept... / Not held in...（前置詞＋関係代名詞＋不定詞と否定の分詞構文）",
        "subtitle": "Preposition + Which + To-Infinitive and Negative Participle Clauses",
        "explanation": "大問3B「Saint Helena」では、a base from which to intercept ships carrying slaves という〈前置詞＋関係代名詞＋to不定詞〉が使われています。これは a base from which they could intercept ships とほぼ同じ意味で、「そこから奴隷を運ぶ船を拿捕するための基地」となります。また、Not held in a standard prison, Napoleon ... は、受動の分詞構文の前に not を置いた否定の分詞構文で、「通常の刑務所には収容されず」という意味です。分詞構文を否定するときは、not を分詞の直前に置くことを押さえましょう。",
        "sourceQuote": "the British navy used the island as a base from which to intercept ships carrying slaves",
        "sourceLocation": "Part 3B「Saint Helena」第2段落",
        "examples": [
            {
                "en": "The British navy used the island as a base from which to intercept ships carrying slaves.",
                "ja": "イギリス海軍はこの島を、そこから奴隷を運ぶ船を拿捕するための基地として利用した。",
                "note": "from which to intercept＝from which they could intercept。intercept ships from the base の from が which の前に出た形です。",
            },
            {
                "en": "She needed a quiet room in which to study.",
                "ja": "彼女には勉強するための静かな部屋が必要だった。",
                "note": "study in a room の in が which の前に出ています。in which to study＝to study in です。",
            },
            {
                "en": "Not held in a standard prison, Napoleon mainly resided at a secure residence called Longwood House.",
                "ja": "ナポレオンは通常の刑務所には収容されず、主にロングウッド・ハウスと呼ばれる警備の厳重な邸宅で暮らした。",
                "note": "As he was not held ... から接続詞と主語、being を省いた否定の分詞構文です。not は分詞の直前に置きます。",
            },
        ],
        "practicePassage": {"passage": "Saint Helena", "paragraphs": [1, 2]},
        "practiceQuestions": [
            {
                "q": "a base from which to intercept ships の from which to intercept を、主語と助動詞を使って書き換えてください。",
                "a": "a base from which they could intercept ships です。「そこから船を拿捕できる基地」という意味になります。",
            },
            {
                "q": "Not held in a standard prison, を接続詞を使った節に書き換えてください。",
                "a": "As he was not held in a standard prison, です。受動の分詞構文で being が省略され、否定の not が分詞 held の前に置かれています。",
            },
            {
                "q": "take no chances はどういう意味で、イギリスはどのような行動でそれを示しましたか？",
                "a": "「一切危険を冒さない」という意味です。孤立したセントヘレナを選び、1,000キロ以上離れたアセンション島にまで兵士を駐留させました。",
            },
            {
                "q": "第2段落が挙げる、19世紀にセントヘレナが港として衰退した要因を2つ答えてください。",
                "a": "補給なしで長距離を航行できる蒸気船の導入と、ヨーロッパとアジアを結ぶより短い航路をもたらしたスエズ運河の開通です。Q29の正解は前者の言い換えです。",
            },
        ],
        "highlightPatterns": [
            "a base from which to intercept ships carrying slaves",
            "Not held in a standard prison, Napoleon mainly resided at a secure residence called Longwood House",
        ],
        "highlightColor": "#96CEB4",
        "highlightLabel": "前置詞＋関係詞・分詞構文",
    },
    {
        "id": "fp5",
        "title": "今回の重要なパラフレーズ",
        "subtitle": "Key Paraphrases in This Exam",
        "explanation": "準1級の内容一致問題では、本文の表現がそのまま選択肢に出ることはほとんどありません。今回も、had little or no effect が were mostly unsuccessful に、known only to the Portuguese が other nations were not aware of its existence に言い換えられています。本文の主語・因果関係・程度（may や could などの可能性の表現）を保ったまま別の表現に置き換えられているかを確認し、本文にない比較対象・提案・理由を加えた選択肢を除外しましょう。",
        "sourceQuote": "①had little or no effect on their overall employment rate = were mostly unsuccessful in doing so\n②may be classified as “able-bodied” despite significant barriers = barriers to employment that are real but may not be covered by official policies\n③helping to sustain demand in the economy = stimulating local economies\n④known only to the Portuguese = other nations were not aware of its existence\n⑤The introduction of steamships = A technological development in the shipping industry\n⑥take no chances = took as many precautions as they felt necessary\n⑦community initiatives ... by replanting native trees = efforts by Saint Helena islanders to restore forests",
        "sourceLocation": "Part 3 全体",
        "examples": [
            {
                "en": "had little or no effect on their overall employment rate → were mostly unsuccessful in doing so",
                "ja": "全体の就業率にほとんど、あるいはまったく影響しなかった → それ（就職を促すこと）にほとんど成功しなかった",
                "note": "効果の有無を「成功しなかった」という評価に置き換えています（Q25）。",
            },
            {
                "en": "The introduction of steamships → A technological development in the shipping industry",
                "ja": "蒸気船の導入 → 海運業界における技術の発展",
                "note": "具体的な事物を、抽象的な上位概念で言い換えるパターンです（Q29）。",
            },
            {
                "en": "the British were determined to take no chances → They took as many precautions as they felt necessary",
                "ja": "イギリスは一切危険を冒さないと決意していた → 必要と考えるだけの予防策を講じた",
                "note": "否定形の決意を、具体的な行動を表す肯定形に変換しています（Q30）。",
            },
        ],
        "practicePassage": {"passage": "Saint Helena", "paragraphs": [0, 3]},
        "practiceQuestions": [
            {
                "q": "Q28で、For approximately eighty years, this isolated island remained a secret, known only to the Portuguese. は正解選択肢でどう言い換えられていますか？",
                "a": "for decades because other nations were not aware of its existence（ほかの国々が島の存在を知らなかったため何十年もの間）と言い換えられています。",
            },
            {
                "q": "Q28の選択肢3（東インド会社がほかの誰よりも先に島を支配した）が誤りである根拠は何ですか？",
                "a": "東インド会社が最終的に島を手に入れた（ultimately took possession of it）のは、キャベンディッシュが島を見つけ、オランダも支配を試みた後のことだからです。",
            },
            {
                "q": "Q31で、community initiatives have been established ... by replanting native trees はどう言い換えられていますか？",
                "a": "efforts by Saint Helena islanders to restore forests（森林を回復させようとするセントヘレナの島民の取り組み）と言い換えられています。",
            },
            {
                "q": "本文の there is optimism that ... can secure the future と、Q31の正解選択肢の could contribute to improvements は、どのような点で対応していますか？",
                "a": "どちらも断定ではなく可能性（can / could）として改善への期待を述べています。楽観的な見通しという程度を保ったまま言い換えられています。",
            },
        ],
        "highlightPatterns": [
            "known only to the Portuguese",
            "community initiatives have been established to turn the tide on this habitat loss by replanting native trees",
        ],
        "highlightColor": "#f59e0b",
        "highlightLabel": "パラフレーズ",
    },
]


def fill_english(text: str) -> str:
    return BLANK_RE.sub(lambda match: BLANK_FILLS[int(match.group(1))][0], text)


def fill_japanese(text: str) -> str:
    return JA_BLANK_RE.sub(lambda match: BLANK_FILLS[int(match.group(1))][1], text)


def build_practice_passage(passages: dict[str, dict], spec: dict) -> dict[str, str]:
    passage = passages[spec["passage"]]
    english = " ".join(fill_english(passage["paragraphs"][index]) for index in spec["paragraphs"])
    japanese = "".join(fill_japanese(passage["translations"][index]) for index in spec["paragraphs"])
    if BLANK_RE.search(english) or BLANK_RE.search(japanese):
        raise ValueError(f"Unfilled blank in practice passage for {spec['passage']}")
    return {"en": f"[出典: {spec['passage']}]\n{english}", "ja": japanese}


def main() -> None:
    if not DATA_PATH.is_file():
        raise FileNotFoundError(
            f"Base data does not exist: {DATA_PATH}. Run gen_pre1_2026-2.py first."
        )

    with DATA_PATH.open("r", encoding="utf-8") as handle:
        data = json.load(handle)

    passages = {
        passage["title"]: passage
        for section in data.get("sections", [])
        for passage in section.get("passages", [])
    }
    missing = {fp["practicePassage"]["passage"] for fp in FOCUS_POINTS} - set(passages)
    if missing:
        raise SystemExit(f"Run the Part 2 and Part 3 generators first; missing passages: {sorted(missing)}")

    focus_points = []
    for focus_point in FOCUS_POINTS:
        built = dict(focus_point)
        built["practicePassage"] = build_practice_passage(passages, focus_point["practicePassage"])
        focus_points.append(built)

    data["lessonPlan"] = {"focusPoints": focus_points}

    with DATA_PATH.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(data, handle, ensure_ascii=False, indent=4)
        handle.write("\n")

    print(f"Installed {len(focus_points)} focus points in {DATA_PATH}")


if __name__ == "__main__":
    main()

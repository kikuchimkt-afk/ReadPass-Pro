# -*- coding: utf-8 -*-
"""2026-1 3級（本会場）監査向け一括修正 — ○表記・根拠・大問3解説強化"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade3", "2026-1", "data.json",
)

SECTION3_ANALYSES = {
    21: [
        "✅ Bring a notebook.＝ノートを持参。Remember to bring an apron and a notebook. の notebook と一致→正解",
        "❌ Wash the dishes after cooking.＝料理後の皿洗い。wash dishes の記述なし",
        "❌ Buy Mr. Chen's recipe book.＝レシピ本購入。recipe book の記述なし",
        "❌ Learn to speak Chinese.＝中国語学習。Chinese recipes を学ぶが speak Chinese とは異なる",
    ],
    22: [
        "❌ gave lessons to students online.＝オンライン授業。online lessons の記述なし",
        "❌ taught teenagers on Saturday mornings.＝土曜の朝。Classes は Saturdays, 2:00 p.m.（午後）",
        "❌ invited his friends to the cooking classes.＝友達を招待。チェン先生を特別講師として招くのは主催者で、友達を招いたとは書かれていない",
        "✅ won some cooking contests.＝He has won some international cooking contests. と一致→正解",
    ],
    23: [
        "✅ She bought a coat and a scarf.＝bought it for you（scarf）＋bought a coat for myself と一致→正解",
        "❌ She found a nice wallet.＝すてきな財布を見つけた。財布はおばあちゃんから先月もらった物で、昨日デパートでした行動ではない",
        "❌ She bought a brown sweater.＝茶色のセーターを買った。couldn't find any brown ones と矛盾",
        "❌ She worked as a staff member.＝店員として勤務。staff member の記述なし",
    ],
    24: [
        "❌ at a shop in the park.＝公園内の店。本文は a cake shop near the park（公園の近くのケーキ店）で、公園内ではない",
        "✅ at a shopping mall beside the museum.＝I found it at a shopping mall next to the museum. と一致→正解",
        "❌ at a shop next to her house.＝家の隣の店。next to the museum とあり、家の隣ではない",
        "❌ at a department store in Linda's city.＝リンダの街のデパート。department store は Judy の買い物場所",
    ],
    25: [
        "❌ She shared a cake with Linda.＝ケーキ共有。cakes は訪問前に買う予定で料理中の行動ではない",
        "❌ She visited a park with her mother.＝公園訪問。mother は仕事で同行しない（第三通メール）",
        "✅ She listened to Linda's stories.＝Linda often told me stories when you were cooking（リンダが話す物語を聞く）と一致→正解",
        "❌ She helped her grandmother in the kitchen.＝台所手伝い。told me stories（リンダが話し、ジュディが聞く）と異なる",
    ],
    26: [
        "✅ Drawing on paper.＝drawing pictures on paper her father bought for her と一致→正解",
        "❌ Taking pictures.＝写真撮影。taking pictures の記述なし",
        "❌ Buying gifts for her father.＝父への贈り物。father bought paper for her（父が紙を買った）",
        "❌ Playing games at home.＝家でゲーム。played outside with her brothers と外で遊ぶ",
    ],
    27: [
        "❌ She had to teach art to her son.＝美術指導。teach art の記述なし",
        "✅ She had a problem with her hands.＝because her hands hurt. So, she decided to try painting と一致→正解",
        "❌ She did not want to look old.＝老けたくない。look old の記述なし",
        "❌ She did not enjoy living on her farm.＝農場で暮らすのが嫌だった。lived on the local farm she loved とあり、農場を愛していた",
    ],
    28: [
        "❌ made her much poorer.＝彼女をさらに貧しくした。本文にアンナの収入や貧しさについての記述はない",
        "❌ made people free.＝人を自由に。made people free の記述なし",
        "❌ were sold to farmers.＝農民に売却。sold to farmers の記述なし",
        "✅ had a lot of colors.＝painted in a simple way with many colors と一致→正解",
    ],
    29: [
        "❌ She tried to travel across America.＝アメリカ横断。travel across America の記述なし",
        "❌ She invented new colors.＝新色発明。invented colors の記述なし",
        "✅ She created many works of art.＝created more than 1,500 works of art in her life と一致→正解",
        "❌ She built a famous museum.＝有名な美術館を建てた。people come to see her paintings in museums とあるだけで、アンナが美術館を建てたとは書かれていない",
    ],
    30: [
        "❌ A woman who loved her grandmother.＝祖母を愛した女性。Grandma Moses はアンナの通称で、この内容ではない",
        "✅ A popular artist in America.＝American artist、paintings became popular across the country と一致→正解",
        "❌ How to live on a farm.＝農場生活の仕方。farm life は背景の一部",
        "❌ How to help older people.＝高齢者支援。anyone can try something new が主テーマ",
    ],
}

SOURCE_EVIDENCE = {
    21: ["Remember to bring an apron and a notebook."],
    22: ["He has won some international cooking contests."],
    23: ["I saw a nice scarf and bought it for you! I also bought a coat for myself."],
    24: ["I found it at a shopping mall next to the museum."],
    25: ["Linda often told me stories when you were cooking in the kitchen."],
    26: ["She often enjoyed drawing pictures on paper her father bought for her."],
    27: [
        "it was hard for her to do some things on the farm because her hands hurt.",
        "So, she decided to try painting instead.",
    ],
    28: ["painted in a simple way with many colors"],
    29: ["She created more than 1,500 works of art in her life"],
    30: ["was an American artist", "her paintings became popular across the country"],
}

PASSAGE_TRANSLATION_UPDATES = {
    "A": {
        2: "来年3月、エヴァンスフィールド文化センターでは、中国料理のレシピを学びたい人のための料理教室を開催します。チェン先生を特別講師として招きます。",
        6: "講師について\nチェン先生は市内でも最高のシェフの一人です。国際的な料理コンテストで優勝したことがあります。昨年は「年間最優秀若手シェフ」にも選ばれました。",
    },
}

QUESTION_FIELD_UPDATES = {
    22: {
        "grammar": "He has won some international cooking contests＝国際的な料理コンテストで優勝したことがある。",
    },
    23: {
        "grammar": "ジュディはマフラーをおばあちゃんに、コートを自分に買った。",
    },
    24: {
        "grammar": "おばあちゃんのメールでは、財布は博物館の隣のショッピングモールで見つけたとある。場所が選択肢2と一致する。",
        "grammarSimple": "さいふを見つけたのは、博物館のとなりのショッピングモールだよ。",
    },
    25: {
        "grammar": "おばあちゃんが料理しているとき、Linda often told me stories とあるので、ジュディはリンダが話す物語を聞いていた。",
    },
    27: {
        "grammar": "手が痛くて農作業が難しくなったため、代わりに絵を描いてみることにした。",
    },
    28: {
        "grammar": "with many colors＝多くの色を使った絵。",
    },
    30: {
        "grammar": "グランマ・モーゼスという、アメリカで人気になった画家の生涯。",
    },
}


def normalize_choice_analysis(q):
    """Use the established grade-3 notation: ○ only for the correct choice."""
    normalized = []
    for i, t in enumerate(q.get("choiceAnalysis", [])):
        t = t.strip()
        if t.startswith(("✅", "❌", "○")):
            t = t[1:].lstrip()
        if i + 1 == q["answer"]:
            t = "○ " + t
        normalized.append(t)
    q["choiceAnalysis"] = normalized


with open(DATA_PATH, encoding="utf-8") as f:
    data = json.load(f)

for sec in data["sections"]:
    for q in sec.get("questions", []):
        normalize_choice_analysis(q)
    for p in sec.get("passages", []):
        for index, translation in PASSAGE_TRANSLATION_UPDATES.get(p.get("label"), {}).items():
            p["translations"][index] = translation
        for q in p.get("questions", []):
            n = q["number"]
            if n in SECTION3_ANALYSES:
                q["choiceAnalysis"] = SECTION3_ANALYSES[n]
            normalize_choice_analysis(q)
            if n in SOURCE_EVIDENCE:
                q["sourceEvidence"] = SOURCE_EVIDENCE[n]
            q.update(QUESTION_FIELD_UPDATES.get(n, {}))

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Applied audit fixes to {DATA_PATH}")

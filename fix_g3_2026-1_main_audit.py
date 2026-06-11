# -*- coding: utf-8 -*-
"""2026-1 3級（本会場）監査向け一括修正 — ✅/❌・sourceEvidence・大問3解説強化"""
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
        "❌ invited his friends to the cooking classes.＝友達招待。invite friends の記述なし",
        "✅ won some cooking contests.＝He has won some international cooking contests. と一致→正解",
    ],
    23: [
        "✅ She bought a coat and a scarf.＝bought it for you（scarf）＋bought a coat for myself と一致→正解",
        "❌ She found a nice wallet.＝財布発見。wallet はおばあちゃんのプレゼントでデパートでの行動ではない",
        "❌ She bought a brown sweater.＝茶色セーター。couln't find any brown ones と矛盾",
        "❌ She worked as a staff member.＝店員として勤務。staff member の記述なし",
    ],
    24: [
        "❌ at a shop in the park.＝公園の店。park は後の cake shop の場所",
        "✅ at a shopping mall beside the museum.＝I found it at a shopping mall next to the museum. と一致→正解",
        "❌ at a shop next to her house.＝家の隣の店。next to her house の記述なし",
        "❌ at a department store in Linda's city.＝リンダの街のデパート。department store は Judy の買い物場所",
    ],
    25: [
        "❌ She shared a cake with Linda.＝ケーキ共有。cakes は訪問前に買う予定で料理中の行動ではない",
        "❌ She visited a park with her mother.＝公園訪問。mother は仕事で同行しない（第三通メール）",
        "✅ She listened to Linda's stories.＝Linda often told me stories when you were cooking と一致→正解",
        "❌ She helped her grandmother in the kitchen.＝台所手伝い。told me stories（物語を聞く）と異なる",
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
        "❌ She did not enjoy living on her farm.＝農場が嫌。loved the local farm she loved と矛盾",
    ],
    28: [
        "❌ made her much poorer.＝貧しくした。became popular across the country と成功の話",
        "❌ made people free.＝人を自由に。made people free の記述なし",
        "❌ were sold to farmers.＝農民に売却。sold to farmers の記述なし",
        "✅ had a lot of colors.＝painted in a simple way with many colors と一致→正解",
    ],
    29: [
        "❌ She tried to travel across America.＝アメリカ横断。travel across America の記述なし",
        "❌ She invented new colors.＝新色発明。invented colors の記述なし",
        "✅ She created many works of art.＝created more than 1,500 works of art in her life と一致→正解",
        "❌ She built a famous museum.＝博物館建設。come to see her paintings in museums（既存の博物館）",
    ],
    30: [
        "❌ A woman who loved her grandmother.＝おばあちゃん愛。Grandma Moses はAnnaのあだ名",
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
    27: ["it was hard for her to do some things on the farm because her hands hurt"],
    28: ["painted in a simple way with many colors"],
    29: ["She created more than 1,500 works of art in her life"],
    30: ["was an American artist", "her paintings became popular across the country"],
}


def mark_choice_analysis(q):
    marked = []
    for i, t in enumerate(q.get("choiceAnalysis", [])):
        t = t.strip()
        if t.startswith("○"):
            t = t[1:].strip()
        if t.startswith(("✅", "❌")):
            marked.append(t)
        else:
            marked.append(("✅ " if i + 1 == q["answer"] else "❌ ") + t)
    q["choiceAnalysis"] = marked


with open(DATA_PATH, encoding="utf-8") as f:
    data = json.load(f)

for sec in data["sections"]:
    for q in sec.get("questions", []):
        mark_choice_analysis(q)
    for p in sec.get("passages", []):
        for q in p.get("questions", []):
            n = q["number"]
            if n in SECTION3_ANALYSES:
                q["choiceAnalysis"] = SECTION3_ANALYSES[n]
            else:
                mark_choice_analysis(q)
            if n in SOURCE_EVIDENCE:
                q["sourceEvidence"] = SOURCE_EVIDENCE[n]

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Applied audit fixes to {DATA_PATH}")

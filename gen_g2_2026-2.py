# -*- coding: utf-8 -*-
"""Reproducible source for Grade 2, 2026-2 (main venue, October 4).

English text, choices and question stems come from the text layer of the
supplied booklet (2026年度第2回_2級_問題冊子.pdf, pp. 3-11); answers from the
separate official answer sheet. audit_g2_2026-2.py checks both against the PDFs.

Audio references (wordAudio / practicePassage.audioFile) are not written here:
data/grade2/2026-2/_gen_tts.py adds them once the MP3 files exist, so the app
never shows a play button for missing audio. Rerunning this generator removes
them again; run _gen_tts.py afterwards (it skips files that already exist).
"""
import importlib.util
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "data/grade2/2026-2/data.json"
READING = [4, 2, 3, 1, 4, 1, 2, 1, 4, 2, 3, 1, 3, 3, 2, 2, 1,
           1, 2, 4, 4, 2, 2, 3, 1, 2, 2, 1, 4, 4, 1]
LISTENING = [3, 1, 2, 2, 4, 4, 3, 2, 1, 1, 3, 1, 4, 4, 1,
             4, 4, 4, 3, 1, 1, 2, 2, 2, 1, 1, 3, 2, 2, 1]


def module(suffix):
    spec = importlib.util.spec_from_file_location(suffix, ROOT / f"gen_g2_2026-2_{suffix}.py")
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def build():
    part1 = module("part1")
    passages = module("passages")
    materials = module("materials")
    questions = []
    for number, row in enumerate(part1.PART1, 1):
        text, translation, choices, ctrans, answer, analysis, grammar = row
        questions.append(dict(number=number, text=text, translation=translation,
                              choices=choices, choiceTranslations=ctrans, answer=answer,
                              choiceAnalysis=analysis, grammar=grammar))
    sections = [
        dict(name="大問1", nameEn="Part 1", type="vocabulary",
             instruction="次の(1)から(17)までの(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選び，その番号を解答用紙の所定欄にマークしなさい。", questions=questions),
        dict(name="大問2", nameEn="Part 2", type="passage-fill",
             instruction="次の英文A，Bを読み，その文意にそって(18)から(23)までの(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選び，その番号を解答用紙の所定欄にマークしなさい。", passages=passages.PASSAGES[:2]),
        dict(name="大問3", nameEn="Part 3", type="reading-comprehension",
             instruction="次の英文A，Bの内容に関して，(24)から(31)までの質問に対して最も適切なもの，または文を完成させるのに最も適切なものを1，2，3，4の中から一つ選び，その番号を解答用紙の所定欄にマークしなさい。", passages=passages.PASSAGES[2:]),
    ]
    data = dict(grade="2級", year="2026", session="2",
                title="2026年度 第2回 英検2級 リーディング",
                vocabulary=materials.vocabulary(), sections=sections,
                lessonPlan=materials.lessonplan(passages.PASSAGES),
                listening={"part1": dict(zip(map(str, range(1, 16)), LISTENING[:15])),
                           "part2": dict(zip(map(str, range(16, 31)), LISTENING[15:]))})
    answers = [q["answer"] for q in questions] + [q["answer"] for p in passages.PASSAGES for q in p["questions"]]
    if answers != READING:
        raise ValueError(f"official answer mismatch: {answers}")
    return data


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(build(), ensure_ascii=False, indent=4) + "\n", encoding="utf-8")
    print(OUT)

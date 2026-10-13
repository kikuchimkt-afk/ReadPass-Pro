# -*- coding: utf-8 -*-
"""Reproducible source for Grade Pre-2, 2026-2 (main venue, October 4).

English text, choices and question stems come from the text layer of the
supplied booklet (2026年度第2回_準2級_問題冊子.pdf, pp. 3-9); answers from the
separate official answer sheet. audit_pre2_2026-2.py checks both.

Audio references (wordAudio / exampleAudio / practicePassage.audioFile) are not
written here: data/grade-pre2/2026-2/_gen_tts.py adds them once the MP3 files
exist. Rerunning this generator removes them again; run _gen_tts.py afterwards
(it skips files that already exist).
"""
import importlib.util
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "data/grade-pre2/2026-2/data.json"
READING = [4, 4, 4, 2, 4, 3, 3, 3, 1, 4, 2, 4, 2, 4, 3,
           3, 2, 1, 1, 4, 3, 1, 3, 1, 3, 2, 3, 4, 2]
LISTENING = [3, 3, 2, 3, 2, 3, 3, 2, 3, 3,
             1, 2, 1, 1, 2, 2, 2, 1, 3, 2,
             4, 1, 1, 1, 4, 3, 2, 2, 1, 3]


def module(suffix):
    spec = importlib.util.spec_from_file_location(suffix, ROOT / f"gen_pre2_2026-2_{suffix}.py")
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def questions(rows, start):
    return [dict(number=n, text=r[0], translation=r[1], choices=r[2], choiceTranslations=r[3],
                 answer=r[4], choiceAnalysis=r[5], grammar=r[6]) for n, r in enumerate(rows, start)]


def build():
    part12 = module("part12")
    passages = module("passages")
    materials = module("materials")
    sections = [
        dict(name="大問1", nameEn="Part 1", type="vocabulary",
             instruction="次の(1)から(15)までの(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選び，その番号を解答用紙の所定欄にマークしなさい。",
             questions=questions(part12.PART1, 1)),
        dict(name="大問2", nameEn="Part 2", type="vocabulary",
             instruction="次の四つの会話文を完成させるために，(16)から(20)に入るものとして最も適切なものを1，2，3，4の中から一つ選び，その番号を解答用紙の所定欄にマークしなさい。",
             questions=questions(part12.PART2, 16)),
        dict(name="大問3", nameEn="Part 3", type="passage-fill",
             instruction="次の英文を読み，その文意にそって(21)と(22)の(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選び，その番号を解答用紙の所定欄にマークしなさい。",
             passages=passages.PASSAGES[:1]),
        dict(name="大問4", nameEn="Part 4", type="reading-comprehension",
             instruction="次の英文A，Bの内容に関して，(23)から(29)までの質問に対して最も適切なもの，または文を完成させるのに最も適切なものを1，2，3，4の中から一つ選び，その番号を解答用紙の所定欄にマークしなさい。",
             passages=passages.PASSAGES[1:]),
    ]
    data = dict(grade="準2級", year="2026", session="2",
                title="2026年度 第2回 英検準2級 リーディング",
                vocabulary=materials.vocabulary(), sections=sections,
                lessonPlan=materials.lessonplan(passages.PASSAGES),
                listening={f"part{i + 1}": dict(zip(map(str, range(10 * i + 1, 10 * i + 11)), LISTENING[10 * i:10 * i + 10]))
                           for i in range(3)})
    answers = [q["answer"] for s in sections for q in s.get("questions", [])]
    answers += [q["answer"] for s in sections for p in s.get("passages", []) for q in p["questions"]]
    if answers != READING:
        raise ValueError(f"official answer mismatch: {answers}")
    return data


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(build(), ensure_ascii=False, indent=4) + "\n", encoding="utf-8")
    print(OUT)

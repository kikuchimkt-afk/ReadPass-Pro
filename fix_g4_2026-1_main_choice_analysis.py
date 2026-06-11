# -*- coding: utf-8 -*-
"""choiceAnalysis の ○ を ✅/❌ に変換（本会場4級 2026-1）"""
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade4", "2026-1", "data.json",
)


def mark_ca(items, answer):
    out = []
    for i, text in enumerate(items):
        cleaned = re.sub(r"^[○✅❌]\s*", "", text)
        prefix = "✅" if i + 1 == answer else "❌"
        out.append(f"{prefix} {cleaned}")
    return out


def iter_questions(data):
    for sec in data.get("sections", []):
        for q in sec.get("questions", []):
            yield q
        for p in sec.get("passages", []):
            for q in p.get("questions", []):
                yield q


with open(DATA_PATH, encoding="utf-8") as f:
    data = json.load(f)

count = 0
for q in iter_questions(data):
    if not q.get("choiceAnalysis") or not q.get("answer"):
        continue
    q["choiceAnalysis"] = mark_ca(q["choiceAnalysis"], q["answer"])
    count += 1

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Updated choiceAnalysis for {count} questions")

# -*- coding: utf-8 -*-
"""2026-1-sat 準2級プラス 監査修正:
旧形式の残骸キー（id / name / passages）を除去し、
他の稼働中データ（2025-3-sat 等）と同じキー順に標準化する。
"""
import json
import os
import sys
from collections import OrderedDict

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade-pre2plus", "2026-1-sat", "data.json",
)

with open(DATA_PATH, encoding="utf-8") as f:
    d = json.load(f)

removed = [k for k in ("id", "name", "passages") if k in d]
clean = OrderedDict()
for k in ("grade", "year", "session", "title", "sections", "lessonPlan", "vocabulary"):
    if k in d:
        clean[k] = d[k]

missing = [k for k in ("grade", "year", "session", "title", "sections", "lessonPlan", "vocabulary") if k not in clean]
if missing:
    print(f"必須キーが欠落: {missing}")
    sys.exit(1)

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(clean, f, ensure_ascii=False, indent=4)

print(f"除去した旧キー: {removed}")
print(f"最終キー順: {list(clean.keys())}")

# -*- coding: utf-8 -*-
"""2026-1-sat 3級 監査修正: キー順標準化・不要キー除去"""
import json
import os
import sys
from collections import OrderedDict

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade3", "2026-1-sat", "data.json",
)

with open(DATA_PATH, encoding="utf-8") as f:
    d = json.load(f)

removed = [k for k in ("id", "name", "passages") if k in d]

order = (
    "grade", "year", "session", "title", "exam",
    "sections", "writing", "listening", "vocabulary", "lessonPlan",
)
clean = OrderedDict()
for k in order:
    if k in d:
        clean[k] = d[k]
for k in d:
    if k not in clean:
        clean[k] = d[k]

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(clean, f, ensure_ascii=False, indent=4)

print(f"除去した旧キー: {removed or 'なし'}")
print(f"最終キー順: {list(clean.keys())}")

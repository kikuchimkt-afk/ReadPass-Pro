# -*- coding: utf-8 -*-
"""Create the base ReadPass data file for EIKEN Grade Pre-1 2026-1."""

import json
import os
import sys


sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(BASE, "data", "pre-grade1", "2026-1")
OUT_PATH = os.path.join(OUT_DIR, "data.json")

data = {
    "grade": "準1級",
    "year": "2026",
    "session": "1",
    "title": "2026年度 第1回 英語資格検定準1級 リーディング",
    "vocabulary": [],
    "sections": [],
    "lessonPlan": {},
}

os.makedirs(OUT_DIR, exist_ok=True)
with open(OUT_PATH, "w", encoding="utf-8") as handle:
    json.dump(data, handle, ensure_ascii=False, indent=4)
    handle.write("\n")

print(f"Wrote {OUT_PATH}")
print("  metadata: 準1級 / 2026 / 第1回")

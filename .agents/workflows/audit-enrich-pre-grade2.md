---
description: 準2級（本会場）既存試験の解説を監査し、手厚く強化する
---

# ReadPass Pro — 準2級 解説 監査・強化ワークフロー

// turbo-all

## 概要

既に `data/grade-pre2/{exam_id}/data.json` として実装済みの準2級試験について、
**解説（`grammar` と `choiceAnalysis`）を監査し、保護者も納得する手厚さへ強化する**ための手順。

新規追加は `add-exam-pre-grade2.md` を参照。本書は **既存データの解説品質を引き上げる**専用。

> 実績: 2025年 本会場 第1〜3回（各29問・計87問）をこの手順で強化（コミット `4792b28`）。

---

## 対象と前提

- 対象: `data/grade-pre2/2025-1` `2025-2` `2025-3`（`-sat` は準会場なので本会場は接尾辞なし）
- ソースPDF: `D:\Files\英検過去問\準2級\準2級{year}-{session}\`
  - 問題: `{year}-{session}-1ji-p2kyu.pdf`
  - 正答表: `{year}{session}Fp2kyu.pdf`
- 新形式（2024年度改訂後）は **29問**（大問1=15 / 大問2=5 / 大問3=2 / 大問4=7）

---

## ★ 最重要: 既存フォーマットと表示仕様を壊さない

`app.js` は正誤を **`answer`（1始まり）のインデックスで判定**して `correct-item` / `wrong-item` を付与する。
`choiceAnalysis` の ✅/❌ や「→正解」は**表示上の慣習**であり、判定には使われない。
ただし一貫性のため、級・大問ごとの既存慣習を必ず踏襲する。

| 大問 | type | 正解行の書式 | 誤答行の書式 |
|------|------|--------------|--------------|
| 大問1 | vocabulary | `✅ 語＝意味。…→正解` | `❌ 語＝意味。…（なぜ不適か）` |
| 大問2 | vocabulary(会話) | `和訳→正解。💡 会話の流れの根拠` | `和訳→（具体的な不適理由）` |
| 大問3 | passage-fill | `和訳→正解。💡 本文の英語根拠` | `和訳→（本文にない/矛盾を具体的に）` |
| 大問4 | reading-comprehension | `和訳→正解。💡 本文の英語根拠` | `和訳→（本文にない/矛盾を具体的に）` |

- `grammar` は必ず `💡` で開始。
- `choiceAnalysis` の要素数は `choices` と一致（通常4）。
- `choiceTranslations` があれば `choices` と長さ一致。
- **和訳系（translation / choiceTranslations / questionTranslation / sentencePairs）は原則保持**。誤りがある場合のみ修正。

---

## 解説の書き方（手厚さの型）

### 大問1（語彙・文法）
`grammar`: `💡 答えの語＝意味（品詞）。コロケーション。類義/反意語。用法・発音などの注意`
`choiceAnalysis`（各行）: **文中のヒント → 答えの語（品詞・意味）→ なぜ合うか → 主な誤答がなぜ違うか**
- 誤答は「文脈に合わない」で済ませず、**その語の意味では何がずれるか**を具体化する。

### 大問2（会話文空所補充）
- 選択肢は文レベルで `choiceTranslations` が表示されるため、`choiceAnalysis` では英文を繰り返さず **和訳→理由**。
- 正解行は会話の流れ（直前・直後の発話）を根拠に。

### 大問3・大問4（長文）
- 正解行は **本文の英語表現を引用**して根拠を示す（例: `💡 roads that people went through only by bicycle or on foot が根拠`）。
- 誤答行は **本文にない／別内容／矛盾** のどれかを具体的に。
- 設問タイプ別の解法を `grammar` に添える（Why=理由、How=手段、What is true=各選択肢を本文照合、パラフレーズ注意 等）。

---

## 手順

### Step 0: 準備（監査）

1. 3回分の構造・設問数・現状の解説の手厚さを一括監査（type順・平均文字数・欠落チェック）。
2. 正答表PDFを抽出し、`data.json` の全 `answer` が公式と一致するか照合。
   - `pdfplumber` でテキスト抽出 → 正答を辞書化 → 突き合わせ。
3. 各回の `data.json` を精読し、本文・選択肢・現行解説を把握。
   - 特に **大問4の長文本文**は根拠引用のため必読。

```python
# 監査例（設問数・平均長・欠落）
import json, os, statistics
GB = r"data\grade-pre2"
for exam in ("2025-1","2025-2","2025-3"):
    d = json.load(open(os.path.join(GB,exam,"data.json"),encoding="utf-8"))
    qs=[]
    for s in d["sections"]:
        qs+=s.get("questions",[])
        for p in s.get("passages",[]): qs+=p["questions"]
    gr=[len(q.get("grammar","")) for q in qs]
    print(exam, "q=",len(qs), "avgGR=", round(statistics.mean(gr),1), "minGR=", min(gr))
```

### Step 1: 強化スクリプト作成（回ごと）

- `_enrich_p2_{year}_{session}.py` を作成し、`number -> (grammar, choiceAnalysis[4])` の辞書で全問を定義。
- `apply()` で sections/passages を走査し、`grammar` と `choiceAnalysis` のみ上書き（和訳系は触らない）。
- Python文字列内では英文引用に `『』` を使うと二重引用符のエスケープ事故を防げる。

```python
# apply() の骨子
def apply():
    d = json.load(open(P, encoding="utf-8"))
    for sec in d["sections"]:
        qlists = [sec.get("questions", [])] + [p.get("questions", []) for p in sec.get("passages", [])]
        for ql in qlists:
            for q in ql:
                if q["number"] in E:
                    g, ca = E[q["number"]]
                    q["grammar"] = g
                    q["choiceAnalysis"] = ca
    json.dump(d, open(P,"w",encoding="utf-8"), ensure_ascii=False, indent=4)
```

- **データ不整合を見つけたら併せて修正**する。
  - 例: 2025-3 Q29 は選択肢2・4の `choiceAnalysis` と `choiceTranslations` が入れ替わっており、
    正解行（answer=4）が「本文にない」と矛盾していた → 正しい並びに修正。

### Step 2: 検証

- 次を全問チェックするスクリプトを実行し、`OK` を確認してから次へ。
  1. `answer` が公式解答と一致
  2. `choiceAnalysis` の要素数＝`choices` 数、`choiceTranslations` があれば長さ一致
  3. 大問1: 正解行のみ `✅`、他は `❌`
  4. 大問2〜4: `正解` を含む行がちょうど1つで、その位置が `answer`
  5. `grammar` が `💡` 始まり・十分な長さ（目安35字以上）
  6. 平均文字数を出力し、強化前より増えていること

### Step 3: 後片付け・コミット

1. 一時ファイル（`_*.py` / 抽出フォルダ）を削除。
2. 変更が `data/grade-pre2/*/data.json` のみであることを `git status --short` で確認。
3. PowerShell はヒアドキュメント不可のため、**コミットメッセージはファイルに書き出して** `git commit -F` で渡す。
4. `git push`。

---

## 落とし穴と対策

| 問題 | 原因 | 対策 |
|------|------|------|
| 正解行が矛盾表示 | `choiceAnalysis`/`choiceTranslations` が選択肢とズレている | 監査時に `answer` インデックスと本文根拠を突き合わせて整列を確認 |
| 誤答理由が薄い | 「文脈に合わない」等の定型 | 語の意味で何がずれるかを具体的に書く |
| 二重引用符でスクリプトが壊れる | 解説内の英文引用に `"` | 英文引用は `『』` で囲む／Pythonはファイル実行 |
| 本会場と準会場の取り違え | `-sat` 付きが準会場 | 本会場は接尾辞なし（`2025-1` 等） |
| 和訳が消える | 強化スクリプトで全キー再生成 | `grammar`/`choiceAnalysis` のみ上書きし和訳系は保持 |
| PS でヒアドキュメント不可 | `<<'EOF'` を使用 | コミット文はファイル化して `git commit -F` |

---

## ファイル構成（強化時に触るもの）

```
data/grade-pre2/{exam_id}/data.json   ← grammar / choiceAnalysis を上書き（必要時のみ和訳修正）
（lessonPlan・vocabulary・本文・音声は原則変更しない）
```

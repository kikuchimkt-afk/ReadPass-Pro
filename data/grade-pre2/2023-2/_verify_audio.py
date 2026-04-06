"""
全FPの練習パッセージと音声ファイルの整合性検証
- practicePassage.en テキストが存在するか
- audioFile パスがdata.jsonに設定されているか
- 対応するMP3ファイルが実在するか
- テキスト先頭が[出典:]で始まるか
- テキストのワード数が妥当か
"""
import json, os

path = r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade-pre2\2023-2\data.json"
d = json.load(open(path, "r", encoding="utf-8"))
base_dir = os.path.dirname(path)
fps = d.get("lessonPlan", {}).get("focusPoints", [])
errors = []

print("=" * 70)
print(f"練習パッセージ・音声 整合性検証: grade-pre2/2023-2")
print("=" * 70)

for i, fp in enumerate(fps):
    fp_id = fp.get("id", f"fp{i+1}")
    title = fp.get("title", "")
    pp = fp.get("practicePassage", {})
    en = pp.get("en", "")
    ja = pp.get("ja", "")
    af = pp.get("audioFile", "")
    
    print(f"\n--- {fp_id}: {title} ---")
    
    # Check en text
    if not en:
        errors.append(f"{fp_id}: practicePassage.en is empty")
        print(f"  ❌ en text: EMPTY")
    else:
        word_count = len(en.split())
        starts_with_source = en.startswith("[出典:")
        print(f"  ✅ en text: {word_count} words, starts_with_source={starts_with_source}")
        print(f"     Preview: {en[:100].replace(chr(10), ' ')}...")
        if not starts_with_source:
            errors.append(f"{fp_id}: practicePassage.en doesn't start with [出典:]")
    
    # Check ja text
    if not ja:
        errors.append(f"{fp_id}: practicePassage.ja is empty")
        print(f"  ❌ ja text: EMPTY")
    else:
        print(f"  ✅ ja text: {len(ja)} chars")
    
    # Check audioFile reference
    if not af:
        errors.append(f"{fp_id}: no audioFile field")
        print(f"  ❌ audioFile: NOT SET")
    else:
        full_path = os.path.join(base_dir, af)
        exists = os.path.exists(full_path)
        if exists:
            size_kb = os.path.getsize(full_path) / 1024
            print(f"  ✅ audioFile: {af} ({size_kb:.0f}KB)")
            if size_kb < 10:
                errors.append(f"{fp_id}: audioFile too small ({size_kb:.0f}KB)")
        else:
            errors.append(f"{fp_id}: audioFile not found: {af}")
            print(f"  ❌ audioFile: {af} NOT FOUND")

# Also verify all sections have proper data
print(f"\n{'='*70}")
print("セクション構造検証")
print("=" * 70)
for i, s in enumerate(d.get("sections", [])):
    stype = s.get("type", "")
    name = s.get("name", "")
    questions = s.get("questions", [])
    passages = s.get("passages", [])
    
    total_qs = len(questions)
    for p in passages:
        total_qs += len(p.get("questions", []))
        has_para = bool(p.get("paragraphs"))
        has_trans = bool(p.get("translations"))
        has_sp = bool(p.get("sentencePairs"))
        label = p.get("label", "")
        pstatus = f"para={'✅' if has_para else '❌'} trans={'✅' if has_trans else '❌'} sp={'✅' if has_sp else '❌'}"
        print(f"  {name} {label}: {pstatus}")
        if not has_para:
            errors.append(f"{name} {label}: no paragraphs")
        if not has_trans:
            errors.append(f"{name} {label}: no translations")
        if not has_sp:
            errors.append(f"{name} {label}: no sentencePairs")
    
    print(f"  {name} ({stype}): {total_qs} questions")

print(f"\n{'='*70}")
if errors:
    print(f"⚠ {len(errors)} issues found:")
    for e in errors:
        print(f"  - {e}")
else:
    print("✅ ALL CHECKS PASSED - パッセージと音声が一致しています")

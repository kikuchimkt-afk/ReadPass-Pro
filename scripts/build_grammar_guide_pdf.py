# -*- coding: utf-8 -*-
"""文法解説プリント（講師用）: one focus point per A4 portrait page, fixed PDF.

Usage:
  python scripts/build_grammar_guide_pdf.py --grade grade-pre2 --exam 2024-1-sat
  python scripts/build_grammar_guide_pdf.py --all

Content = the exam's lessonPlan.focusPoints: ポイント解説, 本文の引用, 例文と解説,
練習パッセージ＋参考和訳, 確認問題と模範解答. Each focus point is laid out on exactly
one page; font sizes shrink step by step until it fits, and the build stops with an
error if it would need text smaller than the minimum scale.

Output: output/pdf/ReadPass_EIKEN_<Grade>_<exam>_Grammar_Guide_v1.pdf
--all also rewrites output/pdf/grammar_guides.json, which print.js reads to show the
閲覧 / DL buttons. Layout ported from ReadPass Studio scripts/lib/build_grammar_guide_pdf.py.
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
from pathlib import Path
import re
import sys
import time

from reportlab.lib.colors import Color
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_fixed_exam_pdf as base  # noqa: E402

PAGE_W, PAGE_H = base.PAGE_W, base.PAGE_H
X0 = 40
X1 = PAGE_W - 40
WIDTH = X1 - X0
TOP = PAGE_H - 36
BOTTOM = 44
INK, MID, LINE, PALE = base.INK, base.MID, base.LINE, base.PALE
ACCENT = Color(0.20, 0.33, 0.62)
ANSWER = Color(0.05, 0.42, 0.18)
QUOTE_BG = Color(0.95, 0.95, 0.98)
MIN_SCALE = 0.74
MAX_SCALE = 1.12
# Proportional BIZ UDPGothic (subfont 1 of the same .ttc) for Japanese text mixed with English.
JP = "ReadPassJP-P"
JP_BOLD = "ReadPassJP-P-Bold"
PDF_DIR = base.REPO_ROOT / "output" / "pdf"
MANIFEST = PDF_DIR / "grammar_guides.json"

# Closing punctuation must not start a line (simple kinsoku: hang it on the previous line).
NO_LINE_START = set("、。，．・：；？！」』）】〕〉》ー…‥ゝゞヽヾぁぃぅぇぉっゃゅょァィゥェォッャュョ%)]},.:;!?")
# Opening brackets must not end a line.
NO_LINE_END = set("（「『【〔〈《([{")


def register_fonts() -> None:
    base.register_fonts()
    pdfmetrics.registerFont(TTFont(JP, r"C:\Windows\Fonts\BIZ-UDGothicR.ttc", subfontIndex=1))
    pdfmetrics.registerFont(TTFont(JP_BOLD, r"C:\Windows\Fonts\BIZ-UDGothicB.ttc", subfontIndex=1))


# Mixed Japanese / English lines: English runs are set in Times New Roman like the exam
# PDF, Japanese runs in BIZ UDPGothic. Times looks smaller than the gothic at the same
# size, so English runs are scaled up slightly.
LATIN = {JP: base.SERIF, JP_BOLD: base.SERIF_BOLD}
LATIN_SCALE = 1.08


def is_latin(ch: str) -> bool:
    o = ord(ch)
    return o < 0x0250 or 0x2000 <= o <= 0x206F


def token_font(token: str, font: str, size: float):
    """(font, size) used to draw one token of a line set in `font`."""
    if font in LATIN and token and is_latin(token[0]):
        return LATIN[font], size * LATIN_SCALE
    return font, size


def string_width(text: str, font: str, size: float) -> float:
    if font not in LATIN:
        return pdfmetrics.stringWidth(text, font, size)
    return sum(pdfmetrics.stringWidth(t, *token_font(t, font, size)) for t in base.tokenize(text))


def draw_string(c, x: float, y: float, text: str, font: str, size: float) -> None:
    """drawString; with a Japanese gothic, English runs switch to Times New Roman."""
    if font not in LATIN:
        c.setFont(font, size)
        c.drawString(x, y, text)
        return
    run, run_font = "", None
    for t in base.tokenize(text):
        f = token_font(t, font, size)
        if run and f != run_font:
            c.setFont(*run_font)
            c.drawString(x, y, run)
            x += pdfmetrics.stringWidth(run, *run_font)
            run = ""
        run_font, run = f, run + t
    if run:
        c.setFont(*run_font)
        c.drawString(x, y, run)


def draw_right(c, x: float, y: float, text: str, font: str, size: float) -> None:
    draw_string(c, x - string_width(text, font, size), y, text, font, size)


def draw_centred(c, x: float, y: float, text: str, font: str, size: float) -> None:
    draw_string(c, x - string_width(text, font, size) / 2, y, text, font, size)


def wrap(text: str, font: str, size: float, width: float) -> list[str]:
    lines: list[str] = []
    for paragraph in base.clean_text(text, wide_blanks=False).split("\n"):
        if not paragraph:
            lines.append("")
            continue
        current, cur_w = "", 0.0
        for token in base.tokenize(paragraph):
            tw = string_width(token, font, size)
            if not current or cur_w + tw <= width:
                current, cur_w = current + token, cur_w + tw
                continue
            if token[0] in NO_LINE_START:
                current, cur_w = current + token, cur_w + tw   # hang punctuation in the margin
                continue
            carry = ""
            while current and current[-1] in NO_LINE_END:
                carry = current[-1] + carry
                current = current[:-1]
            lines.append(current.rstrip())
            current = carry + token.lstrip()
            cur_w = string_width(current, font, size)
        if current:
            lines.append(current.rstrip())
    return lines or [""]


class Page:
    """Draws (or only measures, when c is None) one focus point at a scale."""

    def __init__(self, c, scale: float):
        self.c = c
        self.s = scale
        self.y = TOP

    def text(self, value, font, size, x=X0, width=WIDTH, leading=1.45, color=INK, gap=0.0):
        size *= self.s
        lines = wrap(value, font, size, width)
        if self.c:
            self.c.setFillColor(color)
        for line in lines:
            self.y -= size * leading
            if self.c:
                draw_string(self.c, x, self.y + size * (leading - 1.0) * 0.5, line, font, size)
        self.y -= gap * self.s

    def heading(self, label):
        self.y -= 7 * self.s
        self.text(label, JP_BOLD, 10.2, color=INK, leading=1.3)
        self.y -= 3 * self.s

    def box(self, draw_body, fill=None, stroke=LINE, pad=7.0, bar=None):
        """Measure the body first, then draw the frame behind it."""
        pad *= self.s
        start = self.y
        probe = Page(None, self.s)
        probe.y = start - pad
        draw_body(probe)
        height = (start - probe.y) + pad
        if self.c:
            if fill or stroke:
                self.c.setFillColor(fill or Color(1, 1, 1))
                self.c.setStrokeColor(stroke or LINE)
                self.c.setLineWidth(0.6)
                self.c.rect(X0, start - height, WIDTH, height, stroke=1 if stroke else 0, fill=1 if fill else 0)
            if bar:
                self.c.setFillColor(bar)
                self.c.rect(X0, start - height, 2.6, height, stroke=0, fill=1)
            self.y = start - pad
            draw_body(self)
        self.y = start - height


def practice_qa(item: dict) -> tuple[str, str]:
    """Question and model answer; older Grade 5 data stores multiple-choice checks."""
    if "q" in item:
        return item["q"], item.get("a", "")
    question = item.get("question", "")
    choices = item.get("choices") or []
    answer = item.get("answer")
    if choices:
        question += "　" + "／".join(f"{i}. {choice}" for i, choice in enumerate(choices, 1))
    if isinstance(answer, int) and 0 <= answer < len(choices):
        return question, f"{answer + 1}. {choices[answer]}"
    return question, str(answer or "")


def split_passage(en: str) -> tuple[str, str]:
    """Source label ([出典: ...]) and body; untagged passages are body only."""
    if en.startswith("[出典:") and "\n" in en:
        label, body = en.split("\n", 1)
        return label, body
    return "", en


COLUMN_GAP = 14


def two_columns(q: Page, blocks: list[str]) -> None:
    """Lists of short dialogues (Grade 4/5) run in two balanced columns to fit one page."""
    col_w = (WIDTH - 16 - COLUMN_GAP) / 2

    def block_height(block: str) -> float:
        probe = Page(None, q.s)
        probe.text(block, base.SERIF, 9.7, width=col_w, leading=1.4, gap=4)
        return TOP - probe.y

    heights = [block_height(block) for block in blocks]
    split, running = len(blocks), 0.0
    for index, height in enumerate(heights):
        running += height
        if running >= sum(heights) / 2:
            split = index + 1
            break
    start = q.y
    ends = []
    for column, column_blocks in enumerate((blocks[:split], blocks[split:])):
        q.y = start
        for block in column_blocks:
            q.text(block, base.SERIF, 9.7, x=X0 + 8 + column * (col_w + COLUMN_GAP), width=col_w,
                   leading=1.4, gap=4)
        ends.append(q.y)
    q.y = min(ends)


WHOLE, FIRST_HALF, SECOND_HALF = 0, 1, 2


def layout(c, fp: dict, number: int, scale: float, grade_label: str, exam_label: str,
           qr_url: str, page_no: int, pages: int, part: int = WHOLE) -> float:
    """Draw one page. A focus point too long for one page is split into the explanation
    half (FIRST_HALF) and the practice half (SECOND_HALF)."""
    p = Page(c, scale)
    # header
    if c:
        c.setFillColor(INK)
        draw_string(c, X0, PAGE_H - 24, "ReadPass 文法解説プリント（講師用）", JP_BOLD, 7.4)
        draw_right(c, X1, PAGE_H - 24, f"{grade_label}  |  {exam_label}", JP, 7.4)
        base.draw_rule(c, X0, PAGE_H - 30, WIDTH, base.DARK, 0.75)
        qr = 46
        base.draw_qr(c, qr_url, X1 - qr, PAGE_H - 36 - qr - 2, qr)
        c.setFillColor(MID)
        draw_centred(c, X1 - qr / 2, PAGE_H - 36 - qr - 9, "ReadPassで本文", JP, 5.6)
    title_w = WIDTH - 58
    p.y -= 4
    focus_label = f"Focus {number}" + (" (continued)" if part == SECOND_HALF else "")
    p.text(focus_label, base.SERIF_BOLD, 10, width=title_w, color=ACCENT, leading=1.25)
    p.text(fp.get("title", "") + ("（続き）" if part == SECOND_HALF else ""), JP_BOLD, 14.2,
           width=title_w, leading=1.32)
    if fp.get("subtitle"):
        p.text(fp["subtitle"], base.SERIF_ITALIC, 9.2, width=title_w, color=MID, leading=1.35)
    p.y = min(p.y, TOP - 58)
    if c:
        base.draw_rule(c, X0, p.y - 3, WIDTH, base.DARK, 1.0)
    p.y -= 4

    if part != SECOND_HALF:
        explanation_half(p, fp, scale)
    if part != FIRST_HALF:
        practice_half(p, fp, scale)

    if c:
        base.draw_rule(c, X0, 34, WIDTH, LINE, 0.4)
        c.setFillColor(MID)
        draw_string(c, X0, 22, "ECCベストワン藍住校・北島中央校  |  教室内利用", JP, 6.2)
        c.setFont(base.SANS, 7)
        c.drawRightString(X1, 22, f"{page_no} / {pages}")
    return p.y


def explanation_half(p: Page, fp: dict, scale: float) -> None:
    p.heading("▶ ポイント解説")
    p.text(fp.get("explanation", ""), JP, 9.0, leading=1.62)

    if fp.get("sourceQuote"):
        def quote(q):
            q.text(fp["sourceQuote"], base.SERIF_ITALIC, 9.6, x=X0 + 11, width=WIDTH - 20, leading=1.42)
            if fp.get("sourceLocation"):
                q.text("— " + fp["sourceLocation"], JP, 7.4, x=X0 + 11, width=WIDTH - 20, color=MID, leading=1.4)
        p.y -= 6 * scale
        p.box(quote, fill=QUOTE_BG, stroke=None, bar=ACCENT)

    examples = [ex for ex in fp.get("examples") or [] if isinstance(ex, dict) and ex.get("en")]
    if examples:
        p.heading("▶ 例文と解説")
        for i, ex in enumerate(examples, 1):
            def example(q, ex=ex, i=i):
                q.text(f"({i}) {ex['en']}", base.SERIF_BOLD, 9.9, x=X0 + 8, width=WIDTH - 16, leading=1.36)
                if ex.get("ja"):
                    q.text("→ " + ex["ja"], JP, 8.6, x=X0 + 8, width=WIDTH - 16, leading=1.5)
                if ex.get("note"):
                    q.text("ポイント：" + ex["note"], JP, 8.2, x=X0 + 8, width=WIDTH - 16, color=ACCENT, leading=1.5)
            p.box(example, fill=PALE, stroke=LINE, pad=5.5)
            p.y -= 4 * scale


def practice_half(p: Page, fp: dict, scale: float) -> None:
    pp = fp.get("practicePassage") or {}
    if pp.get("en"):
        p.heading("▶ 練習パッセージ")

        def passage(q):
            if pp["en"].count("[出典:") > 1:          # several exam items, each with its own label
                for line in pp["en"].split("\n"):
                    if line.startswith("[出典:"):
                        q.text(line, JP, 7.6, x=X0 + 8, width=WIDTH - 16, color=MID, leading=1.4)
                    elif line.strip():
                        q.text(line, base.SERIF, 9.7, x=X0 + 8, width=WIDTH - 16, leading=1.45)
                return
            label, body = split_passage(pp["en"])
            if label:
                q.text(label, JP, 7.6, x=X0 + 8, width=WIDTH - 16, color=MID, leading=1.4)
            blocks = [block.strip("\n") for block in body.split("\n\n") if block.strip()]
            if body.count("\n") >= 14 and len(blocks) >= 4:
                two_columns(q, blocks)
            else:
                q.text(body, base.SERIF, 9.7, x=X0 + 8, width=WIDTH - 16, leading=1.5)
        p.box(passage, stroke=LINE, pad=6)
        p.y -= 4 * scale

        if pp.get("ja"):
            # Dialogue lists separate items with blank lines; the translation keeps one item per line.
            ja = re.sub(r"\n\s*\n+", "\n", pp["ja"].strip())

            def translation(q):
                q.text("【参考和訳】" + ja, JP, 8.2, x=X0 + 8, width=WIDTH - 16, color=base.DARK, leading=1.58)
            p.box(translation, fill=Color(0.975, 0.975, 0.975), stroke=LINE, pad=6)

    questions = [item for item in fp.get("practiceQuestions") or [] if isinstance(item, dict)]
    if questions:
        p.heading("▶ 確認問題と模範解答")
        for i, item in enumerate(questions, 1):
            question, answer = practice_qa(item)
            p.text(f"Q{i}. {question}", JP_BOLD, 8.8, leading=1.48)
            p.text(f"A. {answer}", JP, 8.5, x=X0 + 14, width=WIDTH - 14, color=ANSWER, leading=1.5, gap=2.5)


def fit_scale(fp, number, labels, part=WHOLE) -> float | None:
    """Largest scale (MAX_SCALE downwards) at which this page fits, or None."""
    scale = MAX_SCALE
    while scale >= MIN_SCALE - 1e-9:
        if layout(None, fp, number, scale, *labels, number, 1, part) >= BOTTOM:
            return scale
        scale = round(scale - 0.02, 3)
    return None


def plan_pages(fps: list[dict], labels) -> tuple[list[tuple[int, dict, int]], float]:
    """One page per focus point; a focus point that cannot fit is split over two pages."""
    pages, scales = [], []
    for number, fp in enumerate(fps, 1):
        scale = fit_scale(fp, number, labels)
        if scale is not None:
            pages.append((number, fp, WHOLE))
            scales.append(scale)
            continue
        halves = [fit_scale(fp, number, labels, part) for part in (FIRST_HALF, SECOND_HALF)]
        if None in halves:
            raise RuntimeError(f"Focus {number} does not fit two A4 pages even at scale {MIN_SCALE}")
        pages += [(number, fp, FIRST_HALF), (number, fp, SECOND_HALF)]
        scales += halves
    # One common scale for every page (the densest page decides), so all pages look alike.
    return pages, min(scales)


def output_name(grade: str, exam: str) -> str:
    return f"ReadPass_EIKEN_{base.GRADE_FILE_TOKENS[grade]}_{exam}_Grammar_Guide_v1.pdf"


def focus_points(grade: str, exam: str) -> list[dict]:
    path = base.REPO_ROOT / "data" / grade / exam / "data.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    return (data.get("lessonPlan") or {}).get("focusPoints") or []


def render(grade: str, exam: str) -> tuple[int, int, float, bytes]:
    """Build the PDF in memory: (focus point count, page count, scale, PDF bytes)."""
    fps = focus_points(grade, exam)
    if not fps:
        raise RuntimeError(f"{grade}/{exam}: lessonPlan.focusPoints がありません")
    grade_label = base.GRADE_LABELS[grade]
    exam_label = base.exam_display_label(exam)
    url = base.DIRECT_URL.format(grade=grade, exam=exam)
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=(PAGE_W, PAGE_H), pageCompression=1, invariant=1)
    c.setTitle(f"ReadPass - {grade_label} {exam_label} 文法解説プリント（講師用）")
    c.setAuthor("ECC Best One Aizumi / Kitajima-Chuo")
    c.setSubject("ReadPass grammar focus points, one per A4 page")
    labels = (grade_label, exam_label, url)
    pages, scale = plan_pages(fps, labels)
    for page_no, (number, fp, part) in enumerate(pages, 1):
        layout(c, fp, number, scale, *labels, page_no, len(pages), part)
        c.showPage()
    c.save()
    return len(fps), len(pages), scale, buffer.getvalue()


def build(grade: str, exam: str, output: Path) -> tuple[int, int, float, bytes]:
    focus_count, page_count, scale, data = render(grade, exam)
    output.parent.mkdir(parents=True, exist_ok=True)
    # On Windows a just-written PDF is sometimes held briefly by a scanner or preview.
    for attempt in range(10):
        try:
            output.write_bytes(data)
            break
        except OSError:
            if attempt == 9:
                raise
            time.sleep(0.5 * (attempt + 1))
    return focus_count, page_count, scale, data


def manifest_entry(grade: str, exam: str, focus_count: int, pages: int, data: bytes) -> dict:
    name = output_name(grade, exam)
    version = hashlib.sha256(data).hexdigest()[:10]
    return {
        "label": f"{base.GRADE_LABELS[grade]} {base.exam_display_label(exam)}",
        "path": f"output/pdf/{name}?v={version}",
        "downloadName": name,
        "focusPoints": focus_count,
        "pages": pages,
    }


def all_exams() -> list[tuple[str, str]]:
    exams = []
    for grade in base.GRADE_LABELS:
        for path in sorted((base.REPO_ROOT / "data" / grade).glob("*/data.json")):
            exams.append((grade, path.parent.name))
    return exams


def check() -> None:
    """Every exam with focus points needs an up-to-date PDF and manifest entry."""
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8")) if MANIFEST.exists() else {}
    problems = []
    for grade, exam in all_exams():
        if not focus_points(grade, exam):
            continue
        key = f"{grade}/{exam}"
        entry = manifest.get(key)
        if not entry or not (PDF_DIR / entry["downloadName"]).exists():
            problems.append(f"{key}: 文法解説PDFがありません")
            continue
        focus_count, pages, _scale, data = render(grade, exam)
        if entry != manifest_entry(grade, exam, focus_count, pages, data):
            problems.append(f"{key}: data.json の更新が文法解説PDFに反映されていません")
    print(f"checked {len(manifest)} manifest entries")
    if problems:
        print("再生成: python scripts/build_grammar_guide_pdf.py --grade <級> --exam <回>（または --all）")
        for problem in problems:
            print("  " + problem)
        raise SystemExit(1)
    print("GRAMMAR GUIDES OK")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the one-page-per-focus-point grammar guide PDF.")
    parser.add_argument("--grade")
    parser.add_argument("--exam")
    parser.add_argument("--all", action="store_true", help="build every exam and rewrite grammar_guides.json")
    parser.add_argument("--check", action="store_true",
                        help="report exams whose guide is missing or older than data.json; writes nothing")
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()
    if not (args.all or args.check) and not (args.grade and args.exam):
        parser.error("--grade と --exam、--all、または --check を指定してください")
    register_fonts()
    if args.check:
        check()
        return

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8")) if MANIFEST.exists() else {}
    targets = all_exams() if args.all else [(args.grade, args.exam)]
    failures = []
    for grade, exam in targets:
        if not focus_points(grade, exam):
            print(f"skip {grade}/{exam}: focusPoints なし")
            continue
        out = (args.output if (args.output and not args.all) else PDF_DIR / output_name(grade, exam)).resolve()
        try:
            focus_count, pages, scale, data = build(grade, exam, out)
        except RuntimeError as error:
            failures.append(f"{grade}/{exam}: {error}")
            continue
        if out.parent == PDF_DIR.resolve():
            manifest[f"{grade}/{exam}"] = manifest_entry(grade, exam, focus_count, pages, data)
        print(f"{grade}/{exam}: {focus_count} focus points / {pages} pages, scale {scale:.2f} -> {out.name}")

    MANIFEST.write_text(json.dumps(dict(sorted(manifest.items())), ensure_ascii=False, indent=2) + "\n",
                        encoding="utf-8")
    print(f"manifest: {len(manifest)} exams -> {MANIFEST.relative_to(base.REPO_ROOT)}")
    if failures:
        print("FAILED:")
        for failure in failures:
            print("  " + failure)
        raise SystemExit(1)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()

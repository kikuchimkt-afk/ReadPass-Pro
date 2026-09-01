from __future__ import annotations

import argparse
import json
import math
import re
from pathlib import Path

from reportlab.graphics import renderPDF
from reportlab.graphics.barcode.qr import QrCodeWidget
from reportlab.graphics.shapes import Drawing
from reportlab.lib.colors import Color, white
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


REPO_ROOT = Path(__file__).resolve().parents[1]
PAGE_W, PAGE_H = A4
MARGIN_X = 42
RIGHT_X = PAGE_W - 42
CONTENT_W = RIGHT_X - MARGIN_X
BOTTOM_Y = 48

GUTTER_X = 39
GUTTER_W = 42
BODY_X = GUTTER_X + GUTTER_W + 12
BODY_W = RIGHT_X - BODY_X

JP_REGULAR = "ReadPassJP"
JP_BOLD = "ReadPassJP-Bold"
SERIF = "EikenSerif"
SERIF_BOLD = "EikenSerif-Bold"
SERIF_ITALIC = "EikenSerif-Italic"
SERIF_BOLD_ITALIC = "EikenSerif-BoldItalic"
SANS = "EikenSans"
SANS_BOLD = "EikenSans-Bold"

INK = Color(0.035, 0.035, 0.035)
DARK = Color(0.18, 0.18, 0.18)
MID = Color(0.39, 0.39, 0.39)
LINE = Color(0.58, 0.58, 0.58)
GUTTER = Color(0.76, 0.76, 0.76)
PALE = Color(0.94, 0.94, 0.94)

GRADE_LABELS = {
    "pre-grade1": "英検準1級",
    "grade5": "英検5級",
    "grade4": "英検4級",
    "grade3": "英検3級",
    "grade-pre2": "英検準2級",
    "grade-pre2plus": "英検準2級プラス",
    "grade2": "英検2級",
}
GRADE_FILE_TOKENS = {
    "pre-grade1": "GradePre1",
    "grade5": "Grade5",
    "grade4": "Grade4",
    "grade3": "Grade3",
    "grade-pre2": "GradePre2",
    "grade-pre2plus": "GradePre2Plus",
    "grade2": "Grade2",
}
DIRECT_URL = "https://read-pass-pro.vercel.app/index.html?grade={grade}&exam={exam}"


def register_fonts() -> None:
    font_files = {
        JP_REGULAR: (Path(r"C:\Windows\Fonts\BIZ-UDGothicR.ttc"), 0),
        JP_BOLD: (Path(r"C:\Windows\Fonts\BIZ-UDGothicB.ttc"), 0),
        SERIF: (Path(r"C:\Windows\Fonts\times.ttf"), None),
        SERIF_BOLD: (Path(r"C:\Windows\Fonts\timesbd.ttf"), None),
        SERIF_ITALIC: (Path(r"C:\Windows\Fonts\timesi.ttf"), None),
        SERIF_BOLD_ITALIC: (Path(r"C:\Windows\Fonts\timesbi.ttf"), None),
        SANS: (Path(r"C:\Windows\Fonts\arial.ttf"), None),
        SANS_BOLD: (Path(r"C:\Windows\Fonts\arialbd.ttf"), None),
    }
    missing = [str(path) for path, _ in font_files.values() if not path.exists()]
    if missing:
        raise RuntimeError(f"Required fonts not found: {missing}")
    for name, (path, subfont_index) in font_files.items():
        kwargs = {"subfontIndex": subfont_index} if subfont_index is not None else {}
        pdfmetrics.registerFont(TTFont(name, str(path), **kwargs))


EXAM_BLANK = "\u2002" * 7
NUMBERED_EXAM_BLANK = "\u2002" * 3


def clean_text(value: object, wide_blanks: bool = True) -> str:
    text = "" if value is None else str(value)
    # Match the wide answer blank used in official EIKEN question booklets.
    # En spaces survive the normal ASCII whitespace cleanup and keep the blank
    # width stable in the embedded Times New Roman font.
    if wide_blanks:
        text = re.sub(r"\([ \t\u3000]*\)", f"({EXAM_BLANK})", text)
        text = re.sub(
            r"\([ \t\u3000]+(\d{1,2})[ \t\u3000]+\)",
            lambda match: f"({NUMBERED_EXAM_BLANK}{match.group(1)}{NUMBERED_EXAM_BLANK})",
            text,
        )
    replacements = {
        "\u3000": " ",
        "\u2010": "-",
        "\u2011": "-",
        "\u2012": "-",
        "\u2013": "-",
        "\u2014": "-",
        "\u2212": "-",
        "\u00a0": " ",
    }
    for before, after in replacements.items():
        text = text.replace(before, after)
    return re.sub(r"[ \t]+", " ", text).strip()


def printable_instruction(value: object) -> str:
    text = clean_text(value, wide_blanks=False)
    return text.replace(
        "一つ選び，その番号のマーク欄をぬりつぶしなさい。",
        "一つ選びなさい。",
    )


def exam_display_label(exam: str) -> str:
    parts = exam.split("-")
    if len(parts) < 2:
        raise ValueError(f"Unsupported exam id: {exam}")
    venue = "（準会場）" if len(parts) >= 3 and parts[2] == "sat" else ""
    return f"{parts[0]}年度 第{parts[1]}回{venue}"


def question_range_label(questions: list[dict]) -> str:
    if not questions:
        return ""
    return f"Q{int(questions[0]['number'])}-Q{int(questions[-1]['number'])}"


def paginate_part1(questions: list[dict]) -> list[list[dict]]:
    if not questions:
        raise ValueError("Part 1 must contain at least one question")
    if len(questions) <= 15:
        return [questions[index:index + 5] for index in range(0, len(questions), 5)]

    first_page = questions[:4]
    remaining = questions[4:]
    base_size, extra = divmod(len(remaining), 3)
    pages = [first_page]
    cursor = 0
    for page_index in range(3):
        size = base_size + (1 if page_index < extra else 0)
        pages.append(remaining[cursor:cursor + size])
        cursor += size
    if any(not page for page in pages) or cursor != len(remaining):
        raise RuntimeError("Part 1 pagination failed")
    return pages


def tokenize(text: str) -> list[str]:
    # Keep an opening quotation mark attached to the following word so it is
    # never stranded at the end of a wrapped line.
    return re.findall(r'"?[A-Za-z0-9][A-Za-z0-9\'.,:;!?()\-/"]*|\s+|.', text)


def wrap_text(
    text: str,
    font: str,
    size: float,
    max_width: float,
    wide_blanks: bool = True,
) -> list[str]:
    lines: list[str] = []
    for paragraph in clean_text(text, wide_blanks=wide_blanks).split("\n"):
        if not paragraph:
            lines.append("")
            continue
        current = ""
        for token in tokenize(paragraph):
            candidate = current + token
            if not current or pdfmetrics.stringWidth(candidate, font, size) <= max_width:
                current = candidate
                continue
            lines.append(current.rstrip())
            current = token.lstrip()
        if current:
            lines.append(current.rstrip())
    return lines or [""]


def draw_wrapped(
    c: canvas.Canvas,
    text: str,
    x: float,
    y: float,
    width: float,
    font: str = SERIF,
    size: float = 10.5,
    leading: float | None = None,
    color: Color = INK,
    wide_blanks: bool = True,
) -> float:
    leading = leading or (size * 1.28)
    c.setFillColor(color)
    c.setFont(font, size)
    cursor = y
    for line in wrap_text(text, font, size, width, wide_blanks=wide_blanks):
        c.drawString(x, cursor, line)
        cursor -= leading
    return cursor


def draw_rule(c: canvas.Canvas, x: float, y: float, width: float, color: Color = LINE, weight: float = 0.5) -> None:
    c.setDash()
    c.setStrokeColor(color)
    c.setLineWidth(weight)
    c.line(x, y, x + width, y)


def draw_dotted_rule(c: canvas.Canvas, x: float, y: float, width: float) -> None:
    c.setStrokeColor(LINE)
    c.setLineWidth(0.45)
    c.setDash(1.3, 1.7)
    c.line(x, y, x + width, y)
    c.setDash()


def draw_qr(c: canvas.Canvas, text: str, x: float, y: float, size: float) -> None:
    widget = QrCodeWidget(text)
    x1, y1, x2, y2 = widget.getBounds()
    scale = size / max(x2 - x1, y2 - y1)
    drawing = Drawing(size, size, transform=[scale, 0, 0, scale, -x1 * scale, -y1 * scale])
    drawing.add(widget)
    renderPDF.draw(drawing, c, x, y)


def draw_page_header(c: canvas.Canvas, grade_label: str, exam_label: str) -> None:
    y = PAGE_H - 27
    c.setFillColor(INK)
    c.setFont(JP_BOLD, 7.4)
    c.drawString(MARGIN_X, y, "ReadPass 過去問演習")
    c.setFont(JP_REGULAR, 7.4)
    c.drawRightString(RIGHT_X, y, f"{grade_label}  |  {exam_label}")
    draw_rule(c, MARGIN_X, y - 8, CONTENT_W, DARK, 0.75)


def draw_page_footer(c: canvas.Canvas, page_number: int, total_pages: int) -> None:
    draw_rule(c, MARGIN_X, 35, CONTENT_W, LINE, 0.4)
    c.setFillColor(MID)
    c.setFont(JP_REGULAR, 6.4)
    c.drawString(MARGIN_X, 22, "ECCベストワン藍住校・北島中央校  |  教室内利用")
    c.setFont(SANS, 7)
    c.drawRightString(RIGHT_X, 22, f"{page_number} / {total_pages}")


def draw_section_title(c: canvas.Canvas, title: str, instruction: str, y: float) -> float:
    c.setFillColor(INK)
    c.setFont(JP_BOLD, 15.5)
    c.drawString(MARGIN_X, y, clean_text(title))
    draw_rule(c, MARGIN_X, y - 8, CONTENT_W, DARK, 0.75)
    return draw_wrapped(
        c,
        instruction,
        MARGIN_X,
        y - 23,
        CONTENT_W,
        font=JP_REGULAR,
        size=8.2,
        leading=10.5,
        color=MID,
        wide_blanks=False,
    ) - 8


def draw_cover(c: canvas.Canvas, grade_label: str, exam_label: str, grade: str, exam: str) -> float:
    top = PAGE_H - 52
    c.setFillColor(INK)
    c.setFont(SERIF_BOLD, 11)
    c.drawString(MARGIN_X, top, "ReadPass Practice Test")
    c.setFont(JP_BOLD, 22)
    c.drawString(MARGIN_X, top - 31, f"{grade_label}  リーディング問題")
    c.setFont(JP_BOLD, 11)
    c.drawString(MARGIN_X, top - 57, exam_label)
    draw_rule(c, MARGIN_X, top - 69, CONTENT_W, DARK, 1.05)

    c.setFont(JP_REGULAR, 9)
    c.drawString(MARGIN_X, top - 91, "氏名")
    draw_rule(c, MARGIN_X + 34, top - 93, 180, MID)
    c.drawString(MARGIN_X + 236, top - 91, "実施日")
    draw_rule(c, MARGIN_X + 279, top - 93, 126, MID)

    qr_size = 58
    draw_qr(c, DIRECT_URL.format(grade=grade, exam=exam), RIGHT_X - qr_size, top - 129, qr_size)
    c.setFont(JP_REGULAR, 6.2)
    c.drawCentredString(RIGHT_X - (qr_size / 2), top - 139, "ReadPassで復習")

    c.setFont(JP_BOLD, 8.3)
    c.drawString(MARGIN_X, top - 123, "解答方法")
    c.setFont(JP_REGULAR, 8.1)
    draw_wrapped(
        c,
        "各問について、最も適切なものを1つ選び、問題冊子の選択肢に○を付けてください。",
        MARGIN_X + 56,
        top - 123,
        345,
        font=JP_REGULAR,
        size=8.1,
        leading=10.5,
    )
    c.setFillColor(MID)
    c.setFont(JP_REGULAR, 7.2)
    c.drawString(MARGIN_X + 56, top - 145, "正解は最終ページにあります。すべて解いてから確認してください。")
    return top - 176


def draw_gutter(c: canvas.Canvas, top: float, bottom: float = BOTTOM_Y) -> None:
    c.setFillColor(GUTTER)
    c.rect(GUTTER_X, bottom, GUTTER_W, max(0, top - bottom), stroke=0, fill=1)


def draw_dialogue_text(
    c: canvas.Canvas,
    text: str,
    x: float,
    y: float,
    width: float,
    size: float = 11.25,
    leading: float = 14.2,
) -> float:
    cursor = y
    for source_line in clean_text(text).split("\n"):
        match = re.match(r"^([^:]{1,18}:)\s*(.*)$", source_line)
        if not match:
            cursor = draw_wrapped(c, source_line, x, cursor, width, font=SERIF, size=size, leading=leading)
            continue
        speaker, remainder = match.groups()
        speaker = re.sub(r"\s*:$", ":", speaker)
        label_width = pdfmetrics.stringWidth(speaker, SERIF_BOLD_ITALIC, size)
        text_x = x + label_width + 4
        c.setFillColor(INK)
        c.setFont(SERIF_BOLD_ITALIC, size)
        c.drawString(x, cursor, speaker)
        lines = wrap_text(remainder, SERIF, size, width - label_width - 4)
        c.setFont(SERIF, size)
        for line in lines:
            c.drawString(text_x, cursor, line)
            cursor -= leading
    return cursor


def draw_choice(c: canvas.Canvas, number: int, choice: str, x: float, y: float, width: float, size: float = 10.7) -> float:
    number_width = 19
    c.setFillColor(INK)
    c.setFont(SERIF_BOLD, size)
    c.drawString(x, y, str(number))
    return draw_wrapped(c, choice, x + number_width, y, width - number_width, font=SERIF, size=size, leading=size * 1.22)


def draw_question_block(
    c: canvas.Canvas,
    question: dict,
    top: float,
    height: float,
    choice_layout: str,
    separator: bool = False,
    body_size: float = 11.25,
    body_leading: float = 14.2,
    choice_size: float = 10.7,
    trim_final_stack_gap: bool = False,
) -> None:
    number = int(question["number"])
    text = question.get("text") or question.get("question") or ""
    choices = question.get("choices", [])
    bottom = top - height
    draw_gutter(c, top, bottom)

    c.setFillColor(INK)
    c.setFont(SERIF_ITALIC, 11.5)
    c.drawCentredString(GUTTER_X + (GUTTER_W / 2), top - 18, f"({number})")

    fitted_body_size = body_size
    fitted_body_leading = body_leading
    # Avoid leaving a final period or other closing mark alone on the next
    # line. A very small per-question reduction preserves the fixed layout and
    # keeps the punctuation attached to the sentence, as in official booklets.
    if "\n" not in clean_text(text, wide_blanks=False):
        for step in range(13):
            candidate_size = body_size - (step * 0.05)
            lines = wrap_text(text, SERIF, candidate_size, BODY_W)
            if not any(re.fullmatch(r"[.,:;!?]+", line.strip()) for line in lines):
                fitted_body_size = candidate_size
                fitted_body_leading = body_leading * (candidate_size / body_size)
                break

    cursor = draw_dialogue_text(
        c,
        text,
        BODY_X,
        top - 17,
        BODY_W,
        size=fitted_body_size,
        leading=fitted_body_leading,
    ) - 7
    if choice_layout == "row4":
        col_w = BODY_W / 4
        bottoms = [
            draw_choice(c, index + 1, choice, BODY_X + (index * col_w), cursor, col_w - 5, size=choice_size)
            for index, choice in enumerate(choices)
        ]
        cursor = min(bottoms)
    elif choice_layout == "grid2":
        col_w = BODY_W / 2
        row_gap = 19
        bottoms = []
        for index, choice in enumerate(choices):
            col = index % 2
            row = index // 2
            bottoms.append(
                draw_choice(
                    c,
                    index + 1,
                    choice,
                    BODY_X + (col * col_w),
                    cursor - (row * row_gap),
                    col_w - 7,
                    size=choice_size,
                )
            )
        cursor = min(bottoms)
    elif choice_layout == "stack":
        for index, choice in enumerate(choices):
            cursor = draw_choice(c, index + 1, choice, BODY_X, cursor, BODY_W, size=choice_size + 0.3)
            if index + 1 < len(choices) or not trim_final_stack_gap:
                cursor -= 3.5
    else:
        raise ValueError(f"Unknown choice layout: {choice_layout}")

    if cursor < bottom + 7:
        raise RuntimeError(f"Question {number} overflowed its fixed block")
    if separator:
        draw_dotted_rule(c, BODY_X, bottom + 2, BODY_W)


def draw_questions_page(
    c: canvas.Canvas,
    page_number: int,
    total_pages: int,
    grade_label: str,
    exam_label: str,
    section_title: str,
    instruction: str,
    questions: list[dict],
    choice_layout: str,
    first_page: bool = False,
    grade: str = "",
    exam: str = "",
    separator: bool = False,
    compact: bool = False,
    question_height_weights: list[float] | None = None,
    trim_final_stack_gap: bool = False,
) -> None:
    if first_page:
        top = draw_cover(c, grade_label, exam_label, grade, exam)
    else:
        draw_page_header(c, grade_label, exam_label)
        top = PAGE_H - 58
    top = draw_section_title(c, section_title, instruction, top)
    available_height = top - BOTTOM_Y
    if question_height_weights is not None:
        if len(question_height_weights) != len(questions) or any(weight <= 0 for weight in question_height_weights):
            raise ValueError("Question height weights must match the questions and be positive")
        total_weight = sum(question_height_weights)
        block_heights = [available_height * weight / total_weight for weight in question_height_weights]
    else:
        block_heights = [available_height / len(questions)] * len(questions)
    cursor = top
    for question, block_height in zip(questions, block_heights):
        draw_question_block(
            c,
            question,
            cursor,
            block_height,
            choice_layout,
            separator=separator,
            body_size=10.3 if compact else 11.25,
            body_leading=12.4 if compact else 14.2,
            choice_size=9.85 if compact else 10.7,
            trim_final_stack_gap=trim_final_stack_gap,
        )
        cursor -= block_height
    draw_page_footer(c, page_number, total_pages)
    c.showPage()


def stack_question_height_weights(
    questions: list[dict],
    trim_final_stack_gap: bool = False,
) -> list[float]:
    """Estimate readable block heights without shrinking long answer choices."""
    body_size = 11.25
    body_leading = 14.2
    choice_size = 11.0
    choice_leading = choice_size * 1.22
    weights: list[float] = []
    for question in questions:
        text = question.get("text") or question.get("question") or ""
        body_lines = len(wrap_text(text, SERIF, body_size, BODY_W))
        choice_lines = sum(
            len(wrap_text(choice, SERIF, choice_size, BODY_W - 19))
            for choice in question.get("choices", [])
        )
        weights.append(
            30
            + (body_lines * body_leading)
            + (choice_lines * choice_leading)
            + (
                max(
                    len(question.get("choices", [])) - (1 if trim_final_stack_gap else 0),
                    0,
                )
                * 3.5
            )
        )
    return weights


def pre1_passage_fill_panel_height(passages: list[dict], minimum: float = 360) -> float:
    """Use one readable fixed height for both Pre-1 fill passages in an exam."""
    required_height = minimum
    article_width = BODY_W - 40
    for passage in passages:
        content_height = 57.0
        for paragraph in passage.get("paragraphs", []):
            line_count = len(wrap_text(paragraph, SERIF, 10.45, article_width))
            content_height += (line_count * 13.7) + 10
        required_height = max(required_height, content_height + 12)
    return math.ceil(required_height / 10.0) * 10.0


def draw_word_order_block(
    c: canvas.Canvas,
    question: dict,
    top: float,
    height: float,
) -> None:
    number = int(question["number"])
    bottom = top - height
    draw_gutter(c, top, bottom)

    c.setFillColor(INK)
    c.setFont(SERIF_ITALIC, 11.5)
    c.drawCentredString(GUTTER_X + (GUTTER_W / 2), top - 18, f"({number})")
    cursor = draw_wrapped(
        c,
        question.get("text", ""),
        BODY_X,
        top - 17,
        BODY_W,
        font=JP_REGULAR,
        size=10.4,
        leading=13.2,
        wide_blanks=False,
    ) - 4

    words = [clean_text(word) for word in question.get("words", [])]
    columns = 4 if len(words) <= 4 else 3
    rows = (len(words) + columns - 1) // columns
    cell_gap = 5
    cell_height = 28
    cell_width = (BODY_W - (cell_gap * (columns - 1))) / columns
    circled_numbers = "①②③④⑤⑥"
    for index, word in enumerate(words):
        row = index // columns
        col = index % columns
        x = BODY_X + (col * (cell_width + cell_gap))
        cell_top = cursor - (row * cell_height)
        c.setFillColor(PALE)
        c.rect(x, cell_top - 23, cell_width, 23, stroke=0, fill=1)
        c.setFillColor(INK)
        c.setFont(JP_BOLD, 8.8)
        c.drawString(x + 5, cell_top - 15, circled_numbers[index])
        draw_wrapped(c, word, x + 23, cell_top - 10, cell_width - 28, font=SERIF, size=9.2, leading=10.2)
    cursor -= rows * cell_height + 2

    prefix = clean_text(question.get("framePrefix", ""))
    suffix = clean_text(question.get("frameSuffix", ""))
    c.setFillColor(INK)
    c.setFont(SERIF, 10.2)
    x = BODY_X
    if prefix:
        c.drawString(x, cursor, prefix)
        x += pdfmetrics.stringWidth(prefix, SERIF, 10.2) + 8
    suffix_width = pdfmetrics.stringWidth(suffix, SERIF, 10.2) if suffix else 0
    slot_gap = 5
    slot_width = (RIGHT_X - x - suffix_width - 10 - (slot_gap * (len(words) - 1))) / len(words)
    for _ in words:
        c.setStrokeColor(DARK)
        c.setLineWidth(0.65)
        c.line(x, cursor - 3, x + slot_width, cursor - 3)
        x += slot_width + slot_gap
    if suffix:
        c.drawString(x + 2, cursor, suffix)
    cursor -= 21

    choices = question.get("choices", [])
    col_width = BODY_W / 4
    for index, choice in enumerate(choices):
        x = BODY_X + (index * col_width)
        c.setFillColor(INK)
        c.setFont(SERIF_BOLD, 9.8)
        c.drawString(x, cursor, str(index + 1))
        draw_wrapped(
            c,
            choice,
            x + 18,
            cursor,
            col_width - 23,
            font=JP_REGULAR,
            size=9.6,
            leading=10.8,
            wide_blanks=False,
        )

    if cursor < bottom + 12:
        raise RuntimeError(f"Word-order question {number} overflowed its fixed block")
    draw_dotted_rule(c, BODY_X, bottom + 2, BODY_W)


def draw_word_order_page(
    c: canvas.Canvas,
    page_number: int,
    total_pages: int,
    grade_label: str,
    exam_label: str,
    section: dict,
) -> None:
    draw_page_header(c, grade_label, exam_label)
    questions = section.get("questions", [])
    top = draw_section_title(
        c,
        f"大問3  語句整序  {question_range_label(questions)}",
        printable_instruction(section.get("instruction", "")),
        PAGE_H - 58,
    )
    block_height = (top - BOTTOM_Y) / len(questions)
    cursor = top
    for question in questions:
        draw_word_order_block(c, question, cursor, block_height)
        cursor -= block_height
    draw_page_footer(c, page_number, total_pages)
    c.showPage()


def draw_notice_page(
    c: canvas.Canvas,
    page_number: int,
    total_pages: int,
    grade_label: str,
    exam_label: str,
    passage: dict,
) -> None:
    questions = passage.get("questions", [])
    draw_page_header(c, grade_label, exam_label)
    top = draw_section_title(
        c,
        f"大問4A  案内文  {question_range_label(questions)}",
        "案内文を読み、最も適切なものを1つ選びなさい。",
        PAGE_H - 58,
    )
    draw_gutter(c, top)

    paragraphs = passage.get("paragraphs", [])
    first_lines = [clean_text(line) for line in (paragraphs[0].splitlines() if paragraphs else []) if clean_text(line)]
    title = clean_text(passage.get("title", ""))
    if first_lines and first_lines[0].lower() == title.lower():
        first_lines = first_lines[1:]
    info_height = max(48, 16 + (len(first_lines) * 14))
    info_top = top - 47
    body_height = sum(
        (len(wrap_text(paragraph, SERIF, 10.7, BODY_W - 36)) * 13.8) + 8
        for paragraph in paragraphs[1:]
    )
    required_panel_height = math.ceil(47 + info_height + 15 + body_height + 12)
    panel_height = max(255, required_panel_height)
    if top - panel_height - 8 <= BOTTOM_Y + 170:
        raise RuntimeError("Notice and questions cannot fit on one page")
    c.setStrokeColor(DARK)
    c.setLineWidth(0.7)
    c.rect(BODY_X, top - panel_height, BODY_W, panel_height, stroke=1, fill=0)
    c.setFillColor(INK)
    c.setFont(SERIF_BOLD, 16)
    c.drawCentredString(BODY_X + (BODY_W / 2), top - 28, clean_text(passage.get("title", "")))

    c.setFillColor(PALE)
    c.rect(BODY_X + 14, info_top - info_height, BODY_W - 28, info_height, stroke=0, fill=1)
    cursor = info_top - 18
    for line in first_lines:
        c.setFillColor(INK)
        c.setFont(SERIF_BOLD, 10.7)
        c.drawString(BODY_X + 28, cursor, line)
        cursor -= 14
    cursor = info_top - info_height - 15
    for paragraph in paragraphs[1:]:
        cursor = draw_wrapped(c, paragraph, BODY_X + 18, cursor, BODY_W - 36, font=SERIF, size=10.7, leading=13.8) - 8
    if cursor < top - panel_height + 12:
        raise RuntimeError("Notice overflowed its fixed panel")

    questions_top = top - panel_height - 8
    block_height = (questions_top - BOTTOM_Y) / len(questions)
    cursor = questions_top
    for question in questions:
        draw_question_block(c, question, cursor, block_height, "stack", separator=True)
        cursor -= block_height
    draw_page_footer(c, page_number, total_pages)
    c.showPage()


def draw_flyer(c: canvas.Canvas, passage: dict, x: float, top: float, width: float, height: float) -> None:
    c.setStrokeColor(DARK)
    c.setLineWidth(0.7)
    c.rect(x, top - height, width, height, stroke=1, fill=0)
    c.setFillColor(PALE)
    c.rect(x + 10, top - 48, width - 20, 36, stroke=0, fill=1)
    c.setFillColor(INK)
    c.setFont(SERIF_BOLD, 16)
    c.drawCentredString(x + (width / 2), top - 36, clean_text(passage.get("title", "Volunteer Work")))

    paragraphs = passage.get("paragraphs", [])
    title = clean_text(passage.get("title", ""))
    schedule_content = list(paragraphs)
    if schedule_content and clean_text(schedule_content[0]).lower() == title.lower():
        schedule_content = schedule_content[1:]
    if (
        len(schedule_content) == 3
        and all(len(str(item).splitlines()) >= 3 for item in schedule_content[:2])
    ):
        note_lines = len(wrap_text(schedule_content[2], SERIF, 8.8, width - 48))
        note_height = max(42, 14 + (note_lines * 10.3))
        panel_bottom = top - height
        note_bottom = panel_bottom + 10
        note_top = note_bottom + note_height
        c.setFillColor(PALE)
        c.rect(x + 14, note_bottom, width - 28, note_height, stroke=0, fill=1)
        note_cursor = draw_wrapped(
            c,
            schedule_content[2],
            x + 24,
            note_top - 14,
            width - 48,
            font=SERIF,
            size=8.8,
            leading=10.3,
        )
        if note_cursor < note_bottom + 4:
            raise RuntimeError("Schedule flyer note overflowed its fixed panel")

        card_gap = 8
        card_top = top - 65
        card_bottom = note_top + 8
        card_height = card_top - card_bottom
        card_width = (width - 28 - card_gap) / 2
        for index, paragraph in enumerate(schedule_content[:2]):
            card_x = x + 14 + (index * (card_width + card_gap))
            c.setStrokeColor(MID)
            c.setLineWidth(0.45)
            c.rect(card_x, card_bottom, card_width, card_height, stroke=1, fill=0)
            lines = [clean_text(line) for line in str(paragraph).splitlines() if clean_text(line)]
            c.setFillColor(INK)
            c.setFont(SERIF_BOLD, 10)
            c.drawString(card_x + 8, card_top - 15, lines[0])
            card_cursor = draw_wrapped(
                c,
                "\n".join(lines[1:]),
                card_x + 8,
                card_top - 31,
                card_width - 16,
                font=SERIF,
                size=8.5,
                leading=10.1,
            )
            if card_cursor < card_bottom + 5:
                raise RuntimeError("Schedule flyer card overflowed its fixed panel")
        return

    if len(paragraphs) > 5:
        content = list(paragraphs)
        if content and clean_text(content[0]).lower() == title.lower():
            content = content[1:]
        if len(content) < 3:
            raise ValueError("Expanded flyer layout requires event details and feature blocks")

        cursor = draw_wrapped(
            c,
            content[0],
            x + 14,
            top - 69,
            width - 28,
            font=SERIF_BOLD,
            size=9.8,
            leading=11.8,
        ) - 6
        info_lines = len(wrap_text(content[1], SERIF_BOLD, 9.2, width - 50))
        info_height = max(34, 12 + (info_lines * 11.2))
        c.setFillColor(PALE)
        c.rect(x + 14, cursor - info_height, width - 28, info_height, stroke=0, fill=1)
        draw_wrapped(
            c,
            content[1],
            x + 25,
            cursor - 13,
            width - 50,
            font=SERIF_BOLD,
            size=9.2,
            leading=11.2,
        )

        cards = content[2:]
        columns = 2
        rows = (len(cards) + columns - 1) // columns
        card_gap = 8
        card_top = cursor - info_height - 9
        card_height = (card_top - (top - height + 10) - ((rows - 1) * card_gap)) / rows
        card_width = (width - 28 - card_gap) / columns
        for index, paragraph in enumerate(cards):
            row = index // columns
            col = index % columns
            card_x = x + 14 + (col * (card_width + card_gap))
            item_top = card_top - (row * (card_height + card_gap))
            c.setStrokeColor(MID)
            c.setLineWidth(0.45)
            c.rect(card_x, item_top - card_height, card_width, card_height, stroke=1, fill=0)
            lines = [clean_text(line) for line in str(paragraph).splitlines() if clean_text(line)]
            if not lines:
                continue
            heading_width = pdfmetrics.stringWidth(lines[0], SERIF_BOLD, 9.1)
            has_short_heading = len(lines) > 1 and heading_width <= card_width - 16
            if has_short_heading:
                c.setFillColor(INK)
                c.setFont(SERIF_BOLD, 9.1)
                c.drawString(card_x + 8, item_top - 14, lines[0])
                body_cursor = draw_wrapped(
                    c,
                    " ".join(lines[1:]),
                    card_x + 8,
                    item_top - 29,
                    card_width - 16,
                    font=SERIF,
                    size=8.7,
                    leading=10.2,
                )
            else:
                body_cursor = draw_wrapped(
                    c,
                    "\n".join(lines),
                    card_x + 8,
                    item_top - 14,
                    card_width - 16,
                    font=SERIF,
                    size=8.25,
                    leading=9.6,
                )
            if body_cursor < item_top - card_height + 5:
                raise RuntimeError("Expanded flyer card overflowed its fixed panel")
        return

    cursor = top - 70
    if paragraphs and clean_text(paragraphs[0]).lower() != "notice":
        cursor = draw_wrapped(c, paragraphs[0], x + 14, cursor, width - 28, font=SERIF_BOLD, size=10.15, leading=12.7) - 7
    for paragraph in paragraphs[1:3]:
        cursor = draw_wrapped(c, paragraph, x + 14, cursor, width - 28, font=SERIF, size=10.15, leading=12.7) - 7

    when_where = clean_text(paragraphs[3] if len(paragraphs) > 3 else "")
    c.setFillColor(PALE)
    c.rect(x + 14, cursor - 48, width - 28, 48, stroke=0, fill=1)
    draw_wrapped(c, when_where, x + 25, cursor - 16, width - 50, font=SERIF_BOLD, size=9.8, leading=14.5)
    cursor -= 63
    if len(paragraphs) > 4:
        cursor = draw_wrapped(c, paragraphs[4], x + 14, cursor, width - 28, font=SERIF, size=10.15, leading=12.7)
    if cursor < top - height + 12:
        raise RuntimeError("Passage A overflowed its fixed panel")


def draw_passage_a_page(
    c: canvas.Canvas,
    page_number: int,
    total_pages: int,
    grade_label: str,
    exam_label: str,
    section: dict,
    passage: dict,
) -> None:
    draw_page_header(c, grade_label, exam_label)
    top = draw_section_title(c, "大問3A  案内文", section.get("instruction", ""), PAGE_H - 58)
    draw_gutter(c, top)
    flyer_height = 300
    draw_flyer(c, passage, BODY_X, top, BODY_W, flyer_height)
    questions_top = top - flyer_height - 8
    questions = passage.get("questions", [])
    block_height = (questions_top - BOTTOM_Y) / len(questions)
    cursor = questions_top
    for question in questions:
        draw_question_block(c, question, cursor, block_height, "stack", separator=True)
        cursor -= block_height
    draw_page_footer(c, page_number, total_pages)
    c.showPage()


def draw_passage_fill_page(
    c: canvas.Canvas,
    page_number: int,
    total_pages: int,
    grade_label: str,
    exam_label: str,
    section: dict,
    passage: dict,
    section_title: str = "大問3  長文の語句空所補充  Q21-Q22",
    panel_height: float = 270,
    compact_questions: bool = False,
) -> None:
    draw_page_header(c, grade_label, exam_label)
    top = draw_section_title(
        c,
        section_title,
        section.get("instruction", ""),
        PAGE_H - 58,
    )
    draw_gutter(c, top)

    c.setStrokeColor(DARK)
    c.setLineWidth(0.7)
    c.rect(BODY_X, top - panel_height, BODY_W, panel_height, stroke=1, fill=0)
    article_x = BODY_X + 20
    article_w = BODY_W - 40
    c.setFillColor(INK)
    c.setFont(SERIF_BOLD, 15.5)
    c.drawCentredString(
        article_x + (article_w / 2),
        top - 28,
        clean_text(passage.get("title", "")),
    )
    cursor = top - 57
    for paragraph in passage.get("paragraphs", []):
        cursor = draw_wrapped(
            c,
            paragraph,
            article_x,
            cursor,
            article_w,
            font=SERIF,
            size=10.45,
            leading=13.7,
        ) - 10
    if cursor < top - panel_height + 12:
        raise RuntimeError("Passage-fill text overflowed its fixed panel")

    questions = passage.get("questions", [])
    questions_top = top - panel_height - 8
    block_height = (questions_top - BOTTOM_Y) / len(questions)
    cursor = questions_top
    for question in questions:
        draw_question_block(
            c,
            question,
            cursor,
            block_height,
            "row4",
            separator=True,
            body_size=10.3 if compact_questions else 11.25,
            body_leading=12.4 if compact_questions else 14.2,
            choice_size=9.7 if compact_questions else 10.7,
        )
        cursor -= block_height
    draw_page_footer(c, page_number, total_pages)
    c.showPage()


def passage_emails(passage: dict) -> list[dict]:
    explicit_emails = passage.get("emails", [])
    if explicit_emails:
        return explicit_emails

    paragraphs = passage.get("paragraphs", [])
    if len(paragraphs) % 2 != 0:
        raise ValueError("Email passage must contain header/body paragraph pairs")
    emails: list[dict] = []
    for index in range(0, len(paragraphs), 2):
        meta: dict[str, str] = {}
        for line in paragraphs[index].splitlines():
            key, separator, value = line.partition(":")
            if separator and key.strip().lower() in {"from", "to", "date", "subject"}:
                meta[key.strip().lower()] = value.strip()
        if set(meta) != {"from", "to", "date", "subject"}:
            raise ValueError("Email header is missing From, To, Date, or Subject")
        emails.append({"meta": meta, "body": paragraphs[index + 1]})
    return emails


def measure_email_height(email: dict, width: float) -> float:
    body_lines = len(wrap_text(email.get("body", ""), SANS, 10.5, width - 28))
    return 62 + 18 + (body_lines * 12.8) + 14


def draw_email(c: canvas.Canvas, email: dict, x: float, top: float, width: float, height: float) -> None:
    c.setStrokeColor(DARK)
    c.setLineWidth(0.7)
    c.rect(x, top - height, width, height, stroke=1, fill=0)
    meta = email.get("meta", {})
    header_lines = [
        f"From: {clean_text(meta.get('from'))}",
        f"To: {clean_text(meta.get('to'))}",
        f"Date: {clean_text(meta.get('date'))}",
        f"Subject: {clean_text(meta.get('subject'))}",
    ]
    c.setFillColor(INK)
    c.setFont(SANS, 10)
    header_y = top - 15
    for line in header_lines:
        c.drawString(x + 13, header_y, line)
        header_y -= 11.2
    draw_dotted_rule(c, x + 13, top - 62, width - 26)
    cursor = draw_wrapped(c, email.get("body", ""), x + 14, top - 79, width - 28, font=SANS, size=10.5, leading=12.8)
    if cursor < top - height + 10:
        raise RuntimeError("Email overflowed its fixed panel")


def draw_emails_page(
    c: canvas.Canvas,
    page_number: int,
    total_pages: int,
    grade_label: str,
    exam_label: str,
    emails: list[dict],
    title: str,
    instruction: str = "3通のメールを読み、後の設問に答えなさい。",
) -> None:
    draw_page_header(c, grade_label, exam_label)
    top = draw_section_title(c, title, instruction, PAGE_H - 58)
    draw_gutter(c, top)
    cursor = top
    for email in emails:
        email_height = measure_email_height(email, BODY_W)
        draw_email(c, email, BODY_X, cursor, BODY_W, email_height)
        cursor -= email_height + 14
    if cursor < BOTTOM_Y:
        raise RuntimeError("Email page overflowed")
    draw_page_footer(c, page_number, total_pages)
    c.showPage()


def draw_email_passage_page(
    c: canvas.Canvas,
    page_number: int,
    total_pages: int,
    grade_label: str,
    exam_label: str,
    passage: dict,
    section_prefix: str = "大問4A",
    question_range: str = "Q23-Q25",
) -> None:
    draw_page_header(c, grade_label, exam_label)
    title = clean_text(passage.get("title", "メール問題"))
    top = draw_section_title(
        c,
        f"{section_prefix}  {title}",
        f"メールを読み、次ページの{question_range}に答えなさい。",
        PAGE_H - 58,
    )
    draw_gutter(c, top)
    email = {
        "meta": passage.get("meta", {}),
        "body": "\n\n".join(passage.get("paragraphs", [])),
    }
    email_height = measure_email_height(email, BODY_W)
    draw_email(c, email, BODY_X, top, BODY_W, email_height)
    if top - email_height < BOTTOM_Y:
        raise RuntimeError("Single-email page overflowed")
    draw_page_footer(c, page_number, total_pages)
    c.showPage()


def draw_email_questions_page(
    c: canvas.Canvas,
    page_number: int,
    total_pages: int,
    grade_label: str,
    exam_label: str,
    title: str,
    email: dict | None,
    questions: list[dict],
    section_prefix: str = "大問3B",
    question_range: str = "Q23-Q25",
) -> None:
    draw_page_header(c, grade_label, exam_label)
    instruction = f"最後のメールを読み、{question_range}に答えなさい。" if email else f"前ページのメールを読み、{question_range}に答えなさい。"
    top = draw_section_title(c, f"{section_prefix}  {clean_text(title)}", instruction, PAGE_H - 58)
    draw_gutter(c, top)
    questions_top = top
    if email:
        email_height = measure_email_height(email, BODY_W)
        draw_email(c, email, BODY_X, top, BODY_W, email_height)
        questions_top = top - email_height - 9
    block_height = (questions_top - BOTTOM_Y) / len(questions)
    cursor = questions_top
    for question in questions:
        draw_question_block(c, question, cursor, block_height, "stack", separator=True)
        cursor -= block_height
    draw_page_footer(c, page_number, total_pages)
    c.showPage()


def draw_letter_passage_page(
    c: canvas.Canvas,
    page_number: int,
    total_pages: int,
    grade_label: str,
    exam_label: str,
    passage: dict,
    section_prefix: str = "大問3B",
    question_range: str = "Q23-Q25",
) -> None:
    draw_page_header(c, grade_label, exam_label)
    title = clean_text(passage.get("title", "手紙問題"))
    top = draw_section_title(
        c,
        f"{section_prefix}  {title}",
        f"手紙を読み、次ページの{question_range}に答えなさい。",
        PAGE_H - 58,
    )
    draw_gutter(c, top)
    letter_x = BODY_X + 22
    letter_w = BODY_W - 44
    cursor = top - 18
    date = clean_text(passage.get("meta", {}).get("date", ""))
    if date:
        c.setFillColor(INK)
        c.setFont(SERIF, 10.45)
        c.drawString(letter_x, cursor, date)
        cursor -= 24
    for paragraph in passage.get("paragraphs", []):
        cursor = draw_wrapped(c, paragraph, letter_x, cursor, letter_w, font=SERIF, size=10.45, leading=13.7) - 10
    if cursor < BOTTOM_Y + 8:
        raise RuntimeError("Letter overflowed its fixed page")
    draw_page_footer(c, page_number, total_pages)
    c.showPage()


def draw_article_page(
    c: canvas.Canvas,
    page_number: int,
    total_pages: int,
    grade_label: str,
    exam_label: str,
    passage: dict,
    section_title: str = "大問3C  長文",
    instruction: str = "本文を読み、次ページのQ26-Q30に答えなさい。",
) -> None:
    draw_page_header(c, grade_label, exam_label)
    top = draw_section_title(c, section_title, instruction, PAGE_H - 58)
    draw_gutter(c, top)
    article_x = BODY_X + 22
    article_w = BODY_W - 44
    c.setFillColor(INK)
    c.setFont(SERIF_BOLD, 16)
    c.drawCentredString(article_x + (article_w / 2), top - 22, clean_text(passage.get("title", "")))
    cursor = top - 50
    for paragraph in passage.get("paragraphs", []):
        cursor = draw_wrapped(c, paragraph, article_x, cursor, article_w, font=SERIF, size=10.45, leading=13.7) - 10
    if cursor < BOTTOM_Y + 8:
        raise RuntimeError("Article overflowed its fixed page")
    draw_page_footer(c, page_number, total_pages)
    c.showPage()


def draw_answer_page(
    c: canvas.Canvas,
    page_number: int,
    total_pages: int,
    grade_label: str,
    exam_label: str,
    questions: list[dict],
    grade: str,
    exam: str,
    answer_number_only_from: int | None = None,
) -> None:
    draw_page_header(c, grade_label, exam_label)
    y = PAGE_H - 70
    c.setFillColor(INK)
    c.setFont(JP_BOLD, 20)
    c.drawString(MARGIN_X, y, "正解一覧")
    c.setFillColor(MID)
    c.setFont(JP_REGULAR, 8.4)
    answer_note = "すべて解き終えてから確認してください。"
    if answer_number_only_from is not None:
        answer_note += " 大問3は正解番号のみを表示しています。"
    c.drawString(MARGIN_X, y - 20, answer_note)
    qr_size = 54
    draw_qr(c, DIRECT_URL.format(grade=grade, exam=exam), RIGHT_X - qr_size, y - qr_size + 9, qr_size)

    grid_top = y - 78
    col_gap = 12
    col_w = (CONTENT_W - (col_gap * 2)) / 3
    header_h = 24
    if len(questions) <= 30:
        question_groups = [questions[index:index + 10] for index in range(0, len(questions), 10)]
        row_h = 47
        question_size = 9.4
        answer_y_offset = 32
        answer_size = 8.2
        answer_leading = 9.8
    elif len(questions) == 31:
        question_groups = [questions[:11], questions[11:21], questions[21:]]
        row_h = 47
        question_size = 9.4
        answer_y_offset = 32
        answer_size = 8.2
        answer_leading = 9.8
    else:
        group_size = (len(questions) + 2) // 3
        question_groups = [questions[index:index + group_size] for index in range(0, len(questions), group_size)]
        row_h = 39 if grade == "pre-grade1" else 40
        question_size = 8.8
        answer_y_offset = 28
        answer_size = 7.3
        answer_leading = 8.4
    for col, group in enumerate(question_groups):
        x = MARGIN_X + (col * (col_w + col_gap))
        c.setFillColor(DARK)
        c.rect(x, grid_top - header_h, col_w, header_h, stroke=0, fill=1)
        c.setFillColor(white)
        c.setFont(SERIF_BOLD, 9)
        c.drawCentredString(
            x + (col_w / 2),
            grid_top - 17,
            f"Q{int(group[0]['number']):02d}-Q{int(group[-1]['number']):02d}",
        )
        for row, question in enumerate(group):
            answer = int(question["answer"])
            answer_text = question.get("choices", [])[answer - 1]
            cell_top = grid_top - header_h - (row * row_h)
            c.setFillColor(PALE if row % 2 == 0 else white)
            c.setStrokeColor(LINE)
            c.setLineWidth(0.45)
            c.rect(x, cell_top - row_h, col_w, row_h, stroke=1, fill=1)
            c.setFillColor(INK)
            c.setFont(SERIF_BOLD, question_size)
            c.drawString(x + 7, cell_top - 15, f"Q{int(question['number']):02d}")
            c.drawRightString(x + col_w - 7, cell_top - 15, str(answer))
            if answer_number_only_from is not None and int(question["number"]) >= answer_number_only_from:
                continue
            if grade in {"grade5", "grade4"}:
                answer_font = JP_REGULAR if any(ord(character) > 127 for character in answer_text) else SERIF
                draw_wrapped(
                    c,
                    answer_text,
                    x + 7,
                    cell_top - answer_y_offset,
                    col_w - 14,
                    font=answer_font,
                    size=answer_size,
                    leading=answer_leading,
                    color=DARK,
                    wide_blanks=False,
                )
            else:
                generic_answer_y_offset = answer_y_offset if grade == "pre-grade1" else 32
                generic_answer_size = answer_size if grade == "pre-grade1" else 8.2
                generic_answer_leading = answer_leading if grade == "pre-grade1" else 9.8
                draw_wrapped(
                    c,
                    answer_text,
                    x + 7,
                    cell_top - generic_answer_y_offset,
                    col_w - 14,
                    font=SERIF,
                    size=generic_answer_size,
                    leading=generic_answer_leading,
                    color=DARK,
                )

    record_y = 68
    c.setStrokeColor(DARK)
    c.setLineWidth(0.7)
    c.rect(MARGIN_X, record_y, CONTENT_W, 47, stroke=1, fill=0)
    c.setFillColor(INK)
    c.setFont(JP_BOLD, 8.5)
    c.drawString(MARGIN_X + 10, record_y + 30, "学習記録")
    c.setFont(JP_REGULAR, 7.8)
    c.drawString(MARGIN_X + 78, record_y + 30, "得点")
    draw_rule(c, MARGIN_X + 106, record_y + 28, 48, MID)
    c.drawString(MARGIN_X + 160, record_y + 30, f"/ {len(questions)}")
    c.drawString(MARGIN_X + 215, record_y + 30, "やり直す問題")
    draw_rule(c, MARGIN_X + 286, record_y + 28, 180, MID)
    c.drawString(MARGIN_X + 78, record_y + 12, "メモ")
    draw_rule(c, MARGIN_X + 106, record_y + 10, 360, MID)
    draw_page_footer(c, page_number, total_pages)
    c.showPage()


def build_exam_pdf(grade: str, exam: str, output_path: Path) -> None:
    if grade not in GRADE_LABELS:
        raise ValueError(f"Unsupported grade: {grade}")
    data_path = REPO_ROOT / "data" / grade / exam / "data.json"
    with data_path.open("r", encoding="utf-8") as stream:
        data = json.load(stream)

    sections = data.get("sections", [])
    part1 = sections[0].get("questions", [])
    part2 = sections[1].get("questions", [])
    part1_pages = paginate_part1(part1)
    if len(part1_pages) > 4:
        raise RuntimeError("Part 1 must fit within four pages")

    grade_label = GRADE_LABELS[grade]
    exam_label = exam_display_label(exam)
    if exam == "2026-1-sat" and grade in {"grade5", "grade4", "grade3", "grade-pre2"}:
        exam_label = "2026年度 第1回（土曜準会場）"
    # Keeping Part 1 at four pages or fewer makes every later page number shift
    # deterministically while each grade keeps its own fixed section sequence.
    pre2_fill_count = (
        len(sections[2].get("passages", []))
        if grade == "grade-pre2" and len(sections) >= 3
        else 0
    )
    pre1_reading_count = (
        len(sections[2].get("passages", []))
        if grade == "pre-grade1" and len(sections) >= 3
        else 0
    )
    grade2_reading_count = (
        len(sections[2].get("passages", []))
        if grade == "grade2" and len(sections) >= 3
        else 0
    )
    default_trailing_pages = 7
    if grade == "pre-grade1" and pre1_reading_count in {2, 3}:
        default_trailing_pages = 3 + (2 * pre1_reading_count)
    elif grade == "grade-pre2" and pre2_fill_count == 2:
        default_trailing_pages = 8
    elif grade == "grade2" and grade2_reading_count == 3:
        default_trailing_pages = 9
    trailing_pages = {"grade5": 3, "grade4": 8}.get(
        grade,
        default_trailing_pages,
    )
    total_pages = len(part1_pages) + trailing_pages
    output_path.parent.mkdir(parents=True, exist_ok=True)
    pdf = canvas.Canvas(str(output_path), pagesize=A4, pageCompression=1, invariant=1)
    pdf.setTitle(f"ReadPass - {grade_label} {exam_label} 過去問演習")
    pdf.setAuthor("ECC Best One Aizumi / Kitajima-Chuo")
    pdf.setSubject("ReadPass fixed-layout practice exam")

    part1_instruction = (
        printable_instruction(sections[0].get("instruction", ""))
        if grade in {"grade5", "grade4"}
        else sections[0].get("instruction", "")
    )
    for page_number, questions in enumerate(part1_pages, start=1):
        draw_questions_page(
            pdf,
            page_number,
            total_pages,
            grade_label,
            exam_label,
            f"大問1  語彙・文法  {question_range_label(questions)}",
            part1_instruction,
            questions,
            "row4",
            first_page=(page_number == 1),
            grade=grade,
            exam=exam,
            compact=(len(questions) >= 6),
        )
    page_number = len(part1_pages) + 1

    if grade == "grade5":
        if len(sections) != 3:
            raise ValueError("Grade 5 layout requires three sections")
        word_order_section = sections[2]
        if [len(part2), len(word_order_section.get("questions", []))] != [5, 5]:
            raise ValueError("Grade 5 layout requires question counts 5 / 5 after Part 1")
        draw_questions_page(
            pdf,
            page_number,
            total_pages,
            grade_label,
            exam_label,
            f"大問2  会話文  {question_range_label(part2)}",
            printable_instruction(sections[1].get("instruction", "")),
            part2,
            "grid2",
        )
        page_number += 1
        draw_word_order_page(pdf, page_number, total_pages, grade_label, exam_label, word_order_section)
        page_number += 1
        all_questions = part1 + part2 + word_order_section.get("questions", [])
        if page_number != total_pages:
            raise RuntimeError("Grade 5 page numbering drifted")
        draw_answer_page(pdf, page_number, total_pages, grade_label, exam_label, all_questions, grade, exam)
        pdf.save()
        return

    if grade == "grade4":
        if len(sections) != 4:
            raise ValueError("Grade 4 layout requires four sections")
        word_order_section = sections[2]
        passages = sections[3].get("passages", [])
        if len(passages) != 3:
            raise ValueError("Grade 4 layout requires three reading passages")
        notice_passage, email_passage, article_passage = passages
        count_signature = [
            len(part2),
            len(word_order_section.get("questions", [])),
            len(notice_passage.get("questions", [])),
            len(email_passage.get("questions", [])),
            len(article_passage.get("questions", [])),
        ]
        if count_signature != [5, 5, 2, 3, 5]:
            raise ValueError("Grade 4 layout requires question counts 5 / 5 / 2 / 3 / 5 after Part 1")

        draw_questions_page(
            pdf,
            page_number,
            total_pages,
            grade_label,
            exam_label,
            f"大問2  会話文  {question_range_label(part2)}",
            printable_instruction(sections[1].get("instruction", "")),
            part2,
            "grid2",
        )
        page_number += 1
        draw_word_order_page(pdf, page_number, total_pages, grade_label, exam_label, word_order_section)
        page_number += 1
        draw_notice_page(pdf, page_number, total_pages, grade_label, exam_label, notice_passage)
        page_number += 1

        email_questions = email_passage.get("questions", [])
        email_range = question_range_label(email_questions)
        emails = passage_emails(email_passage)
        if len(emails) != 2:
            raise ValueError("Grade 4 email passage requires two messages")
        email_title = clean_text(email_passage.get("title", "メール問題"))
        draw_emails_page(
            pdf,
            page_number,
            total_pages,
            grade_label,
            exam_label,
            emails,
            f"大問4B  {email_title}",
            instruction=f"2通のメールを読み、次ページの{email_range}に答えなさい。",
        )
        page_number += 1
        draw_email_questions_page(
            pdf,
            page_number,
            total_pages,
            grade_label,
            exam_label,
            email_title,
            None,
            email_questions,
            section_prefix="大問4B",
            question_range=email_range,
        )
        page_number += 1

        article_questions = article_passage.get("questions", [])
        article_range = question_range_label(article_questions)
        draw_article_page(
            pdf,
            page_number,
            total_pages,
            grade_label,
            exam_label,
            article_passage,
            section_title="大問4C  長文",
            instruction=f"本文を読み、次ページの{article_range}に答えなさい。",
        )
        page_number += 1
        draw_questions_page(
            pdf,
            page_number,
            total_pages,
            grade_label,
            exam_label,
            f"大問4C  長文設問  {article_range}",
            "前ページの本文を読み、最も適切なものを1つ選びなさい。",
            article_questions,
            "stack",
            separator=True,
        )
        page_number += 1
        all_questions = (
            part1
            + part2
            + word_order_section.get("questions", [])
            + notice_passage.get("questions", [])
            + email_questions
            + article_questions
        )
        if page_number != total_pages:
            raise RuntimeError("Grade 4 page numbering drifted")
        draw_answer_page(pdf, page_number, total_pages, grade_label, exam_label, all_questions, grade, exam)
        pdf.save()
        return

    if grade == "pre-grade1":
        if len(sections) != 3:
            raise ValueError("Grade Pre-1 layout requires three sections")
        passage_fills = sections[1].get("passages", [])
        reading_passages = sections[2].get("passages", [])
        count_signature = [
            *[len(passage.get("questions", [])) for passage in passage_fills],
            *[len(passage.get("questions", [])) for passage in reading_passages],
        ]
        allowed_reading_counts = {2, 3}
        expected_signature = [3, 3, 3, 4] if len(reading_passages) == 2 else [3, 3, 3, 3, 4]
        if (
            len(passage_fills) != 2
            or len(reading_passages) not in allowed_reading_counts
            or count_signature != expected_signature
        ):
            raise ValueError(
                "Grade Pre-1 layout requires two fill passages and two or three reading passages"
            )

        fill_panel_height = pre1_passage_fill_panel_height(passage_fills)
        for index, passage in enumerate(passage_fills):
            questions = passage.get("questions", [])
            section_prefix = f"大問2{chr(ord('A') + index)}"
            draw_passage_fill_page(
                pdf,
                page_number,
                total_pages,
                grade_label,
                exam_label,
                sections[1],
                passage,
                section_title=f"{section_prefix}  長文の語句空所補充  {question_range_label(questions)}",
                panel_height=fill_panel_height,
            )
            page_number += 1

        reading_questions: list[dict] = []
        for index, passage in enumerate(reading_passages):
            questions = passage.get("questions", [])
            reading_questions.extend(questions)
            question_range = question_range_label(questions)
            section_prefix = f"大問3{chr(ord('A') + index)}"
            normal_question_weights = stack_question_height_weights(questions)
            # The fixed question area is about 694 pt. Reserve a small buffer
            # for line-width rounding only on exceptionally dense pages.
            trim_final_stack_gap = sum(normal_question_weights) > 680
            draw_article_page(
                pdf,
                page_number,
                total_pages,
                grade_label,
                exam_label,
                passage,
                section_title=f"{section_prefix}  長文",
                instruction=f"本文を読み、次ページの{question_range}に答えなさい。",
            )
            page_number += 1
            draw_questions_page(
                pdf,
                page_number,
                total_pages,
                grade_label,
                exam_label,
                f"{section_prefix}  長文設問  {question_range}",
                "前ページの本文を読み、最も適切なものを1つ選びなさい。",
                questions,
                "stack",
                separator=True,
                question_height_weights=stack_question_height_weights(
                    questions,
                    trim_final_stack_gap=trim_final_stack_gap,
                ),
                trim_final_stack_gap=trim_final_stack_gap,
            )
            page_number += 1

        all_questions = (
            part1
            + passage_fills[0].get("questions", [])
            + passage_fills[1].get("questions", [])
            + reading_questions
        )
        if page_number != total_pages:
            raise RuntimeError("Grade Pre-1 page numbering drifted")
        draw_answer_page(
            pdf,
            page_number,
            total_pages,
            grade_label,
            exam_label,
            all_questions,
            grade,
            exam,
            answer_number_only_from=int(reading_questions[0]["number"]),
        )
        pdf.save()
        return

    if grade in {"grade-pre2plus", "grade2"}:
        layout_name = "Grade Pre-2 Plus" if grade == "grade-pre2plus" else "Grade 2"
        passage_fills = sections[1].get("passages", [])
        reading_passages = sections[2].get("passages", [])
        allowed_reading_counts = {2, 3} if grade == "grade2" else {2}
        if len(passage_fills) != 2 or len(reading_passages) not in allowed_reading_counts:
            allowed = "two or three" if grade == "grade2" else "two"
            raise ValueError(f"{layout_name} layout requires two fill passages and {allowed} reading passages")
        email_passage = reading_passages[0]
        article_passages = reading_passages[1:]
        count_signature = [
            *[len(passage.get("questions", [])) for passage in passage_fills],
            len(email_passage.get("questions", [])),
            *[len(passage.get("questions", [])) for passage in article_passages],
        ]
        expected_signature = [3, 3, 3, 5] if len(reading_passages) == 2 else [3, 3, 3, 4, 5]
        if count_signature != expected_signature:
            expected = " / ".join(str(value) for value in expected_signature)
            raise ValueError(f"{layout_name} layout requires question counts {expected} after Part 1")
        fill_panel_height = (
            370
            if grade == "grade2" and grade2_reading_count == 3
            else 350
            if grade == "grade2"
            else 340
        )
        if grade == "grade-pre2plus" and exam == "2025-3-sat":
            fill_panel_height = 360

        draw_passage_fill_page(
            pdf,
            page_number,
            total_pages,
            grade_label,
            exam_label,
            sections[1],
            passage_fills[0],
            section_title=f"大問2A  長文の語句空所補充  {question_range_label(passage_fills[0].get('questions', []))}",
            panel_height=fill_panel_height,
        )
        page_number += 1
        draw_passage_fill_page(
            pdf,
            page_number,
            total_pages,
            grade_label,
            exam_label,
            sections[1],
            passage_fills[1],
            section_title=f"大問2B  長文の語句空所補充  {question_range_label(passage_fills[1].get('questions', []))}",
            panel_height=fill_panel_height,
        )
        page_number += 1
        email_questions = email_passage.get("questions", [])
        email_range = question_range_label(email_questions)
        draw_email_passage_page(
            pdf,
            page_number,
            total_pages,
            grade_label,
            exam_label,
            email_passage,
            section_prefix="大問3A",
            question_range=email_range,
        )
        page_number += 1
        email_title = clean_text(email_passage.get("title", "メール問題"))
        draw_email_questions_page(
            pdf,
            page_number,
            total_pages,
            grade_label,
            exam_label,
            email_title,
            None,
            email_questions,
            section_prefix="大問3A",
            question_range=email_range,
        )
        page_number += 1
        article_questions: list[dict] = []
        for index, article_passage in enumerate(article_passages):
            questions = article_passage.get("questions", [])
            article_questions.extend(questions)
            article_range = question_range_label(questions)
            section_prefix = f"大問3{chr(ord('B') + index)}"
            draw_article_page(
                pdf,
                page_number,
                total_pages,
                grade_label,
                exam_label,
                article_passage,
                section_title=f"{section_prefix}  長文",
                instruction=f"本文を読み、次ページの{article_range}に答えなさい。",
            )
            page_number += 1
            draw_questions_page(
                pdf,
                page_number,
                total_pages,
                grade_label,
                exam_label,
                f"{section_prefix}  長文設問  {article_range}",
                "前ページの本文を読み、最も適切なものを1つ選びなさい。",
                questions,
                "stack",
                separator=True,
            )
            page_number += 1
        all_questions = (
            part1
            + passage_fills[0].get("questions", [])
            + passage_fills[1].get("questions", [])
            + email_questions
            + article_questions
        )
        if page_number != total_pages:
            raise RuntimeError(f"{layout_name} page numbering drifted")
        draw_answer_page(pdf, page_number, total_pages, grade_label, exam_label, all_questions, grade, exam)
        pdf.save()
        return

    part2_for_print = part2
    part2_has_shared_dialogue = False
    if grade == "grade-pre2":
        part2_for_print = []
        for index, question in enumerate(part2):
            printable_question = dict(question)
            if index > 0 and clean_text(question.get("text", "")) == clean_text(part2[index - 1].get("text", "")):
                part2_has_shared_dialogue = True
                printable_question["text"] = f"(See Q{part2[index - 1].get('number')})"
            part2_for_print.append(printable_question)

    draw_questions_page(
        pdf,
        page_number,
        total_pages,
        grade_label,
        exam_label,
        f"大問2  会話文  {question_range_label(part2)}",
        sections[1].get("instruction", ""),
        part2_for_print,
        "row4" if grade == "grade-pre2" else "grid2",
        compact=(grade == "grade-pre2"),
        question_height_weights=(
            [
                1.45
                if index + 1 < len(part2_for_print)
                and clean_text(part2_for_print[index + 1].get("text", "")).startswith("(See Q")
                else 0.55
                if clean_text(question.get("text", "")).startswith("(See Q")
                else 1.0
                for index, question in enumerate(part2_for_print)
            ]
            if grade == "grade-pre2" and (pre2_fill_count == 2 or part2_has_shared_dialogue)
            else None
        ),
    )
    page_number += 1

    if grade == "grade3":
        passages = sections[2].get("passages", [])
        part3_questions = [question for passage in passages for question in passage.get("questions", [])]
        if [len(part2), len(part3_questions)] != [5, 10]:
            raise ValueError("Grade 3 layout requires question counts 5 / 10 after Part 1")
        draw_passage_a_page(pdf, page_number, total_pages, grade_label, exam_label, sections[2], passages[0])
        page_number += 1
        email_passage = passages[1]
        emails = email_passage.get("emails", [])
        email_title = clean_text(email_passage.get("title", "メール問題"))
        email_questions = email_passage.get("questions", [])
        email_range = question_range_label(email_questions)
        if emails:
            draw_emails_page(pdf, page_number, total_pages, grade_label, exam_label, emails[:2], f"大問3B  {email_title}")
        else:
            draw_letter_passage_page(
                pdf,
                page_number,
                total_pages,
                grade_label,
                exam_label,
                email_passage,
                section_prefix="大問3B",
                question_range=email_range,
            )
        page_number += 1
        final_email = emails[2] if len(emails) >= 3 else None
        draw_email_questions_page(pdf, page_number, total_pages, grade_label, exam_label, email_title, final_email, email_questions, question_range=email_range)
        page_number += 1
        article_questions = passages[2].get("questions", [])
        article_range = question_range_label(article_questions)
        draw_article_page(pdf, page_number, total_pages, grade_label, exam_label, passages[2], instruction=f"本文を読み、次ページの{article_range}に答えなさい。")
        page_number += 1
        draw_questions_page(pdf, page_number, total_pages, grade_label, exam_label, f"大問3C  長文設問  {article_range}", "前ページの本文を読み、最も適切なものを1つ選びなさい。", article_questions, "stack", separator=True)
        page_number += 1
        all_questions = part1 + part2 + part3_questions
    else:
        passage_fills = sections[2].get("passages", [])
        reading_passages = sections[3].get("passages", [])
        if len(passage_fills) not in {1, 2} or len(reading_passages) != 2:
            raise ValueError("Grade Pre-2 layout requires one or two fill passages and two reading passages")
        email_passage, article_passage = reading_passages
        count_signature = [
            len(part2),
            *[len(passage.get("questions", [])) for passage in passage_fills],
            len(email_passage.get("questions", [])),
            len(article_passage.get("questions", [])),
        ]
        expected_signature = [5, 2, 3, 4] if len(passage_fills) == 1 else [5, 2, 3, 3, 4]
        if count_signature != expected_signature:
            expected = " / ".join(str(value) for value in expected_signature)
            raise ValueError(f"Grade Pre-2 layout requires question counts {expected} after Part 1")
        passage_questions: list[dict] = []
        for index, passage_fill in enumerate(passage_fills):
            questions = passage_fill.get("questions", [])
            passage_questions.extend(questions)
            section_suffix = chr(ord("A") + index) if len(passage_fills) == 2 else ""
            draw_passage_fill_page(
                pdf,
                page_number,
                total_pages,
                grade_label,
                exam_label,
                sections[2],
                passage_fill,
                section_title=(
                    f"大問3{section_suffix}  長文の語句空所補充  "
                    f"{question_range_label(questions)}"
                ),
                panel_height=345 if len(passage_fills) == 2 else 270,
                compact_questions=(len(passage_fills) == 2),
            )
            page_number += 1
        email_questions = email_passage.get("questions", [])
        email_range = question_range_label(email_questions)
        draw_email_passage_page(pdf, page_number, total_pages, grade_label, exam_label, email_passage, question_range=email_range)
        page_number += 1
        email_title = clean_text(email_passage.get("title", "メール問題"))
        draw_email_questions_page(
            pdf,
            page_number,
            total_pages,
            grade_label,
            exam_label,
            email_title,
            None,
            email_questions,
            section_prefix="大問4A",
            question_range=email_range,
        )
        page_number += 1
        article_questions = article_passage.get("questions", [])
        article_range = question_range_label(article_questions)
        draw_article_page(
            pdf,
            page_number,
            total_pages,
            grade_label,
            exam_label,
            article_passage,
            section_title="大問4B  長文",
            instruction=f"本文を読み、次ページの{article_range}に答えなさい。",
        )
        page_number += 1
        draw_questions_page(
            pdf,
            page_number,
            total_pages,
            grade_label,
            exam_label,
            f"大問4B  長文設問  {article_range}",
            "前ページの本文を読み、最も適切なものを1つ選びなさい。",
            article_questions,
            "stack",
            separator=True,
        )
        page_number += 1
        all_questions = (
            part1
            + part2
            + passage_questions
            + email_questions
            + article_questions
        )

    if page_number != total_pages:
        raise RuntimeError("Page numbering drifted")
    draw_answer_page(pdf, page_number, total_pages, grade_label, exam_label, all_questions, grade, exam)
    pdf.save()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a deterministic ReadPass practice-exam PDF.")
    parser.add_argument("--grade", default="grade3")
    parser.add_argument("--exam", default="2025-1")
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    register_fonts()
    output = args.output or (
        REPO_ROOT
        / "output"
        / "pdf"
        / f"ReadPass_EIKEN_{GRADE_FILE_TOKENS[args.grade]}_{args.exam}_Practice_Exam_Large_Type.pdf"
    )
    build_exam_pdf(args.grade, args.exam, output.resolve())
    print(output.resolve())


if __name__ == "__main__":
    main()

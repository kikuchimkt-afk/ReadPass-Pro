from __future__ import annotations

import argparse
import json
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
    "grade3": "英検3級",
    "grade-pre2": "英検準2級",
}
GRADE_FILE_TOKENS = {
    "grade3": "Grade3",
    "grade-pre2": "GradePre2",
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


def tokenize(text: str) -> list[str]:
    return re.findall(r"[A-Za-z0-9][A-Za-z0-9'.,:;!?()\-/\"]*|\s+|.", text)


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
) -> None:
    number = int(question["number"])
    text = question.get("text") or question.get("question") or ""
    choices = question.get("choices", [])
    bottom = top - height
    draw_gutter(c, top, bottom)

    c.setFillColor(INK)
    c.setFont(SERIF_ITALIC, 11.5)
    c.drawCentredString(GUTTER_X + (GUTTER_W / 2), top - 18, f"({number})")

    cursor = draw_dialogue_text(
        c,
        text,
        BODY_X,
        top - 17,
        BODY_W,
        size=body_size,
        leading=body_leading,
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
            cursor = draw_choice(c, index + 1, choice, BODY_X, cursor, BODY_W, size=choice_size + 0.3) - 3.5
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
) -> None:
    if first_page:
        top = draw_cover(c, grade_label, exam_label, grade, exam)
    else:
        draw_page_header(c, grade_label, exam_label)
        top = PAGE_H - 58
    top = draw_section_title(c, section_title, instruction, top)
    block_height = (top - BOTTOM_Y) / len(questions)
    cursor = top
    for question in questions:
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
        )
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
) -> None:
    draw_page_header(c, grade_label, exam_label)
    top = draw_section_title(
        c,
        "大問3  長文の語句空所補充  Q21-Q22",
        section.get("instruction", ""),
        PAGE_H - 58,
    )
    draw_gutter(c, top)

    panel_height = 270
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
        draw_question_block(c, question, cursor, block_height, "row4", separator=True)
        cursor -= block_height
    draw_page_footer(c, page_number, total_pages)
    c.showPage()


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
) -> None:
    draw_page_header(c, grade_label, exam_label)
    top = draw_section_title(c, title, "3通のメールを読み、後の設問に答えなさい。", PAGE_H - 58)
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
) -> None:
    draw_page_header(c, grade_label, exam_label)
    title = clean_text(passage.get("title", "メール問題"))
    top = draw_section_title(
        c,
        f"大問4A  {title}",
        "メールを読み、次ページのQ23-Q25に答えなさい。",
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
) -> None:
    draw_page_header(c, grade_label, exam_label)
    y = PAGE_H - 70
    c.setFillColor(INK)
    c.setFont(JP_BOLD, 20)
    c.drawString(MARGIN_X, y, "正解一覧")
    c.setFillColor(MID)
    c.setFont(JP_REGULAR, 8.4)
    c.drawString(MARGIN_X, y - 20, "すべて解き終えてから確認してください。")
    qr_size = 54
    draw_qr(c, DIRECT_URL.format(grade=grade, exam=exam), RIGHT_X - qr_size, y - qr_size + 9, qr_size)

    grid_top = y - 78
    col_gap = 12
    col_w = (CONTENT_W - (col_gap * 2)) / 3
    header_h = 24
    row_h = 47
    question_groups = [questions[index:index + 10] for index in range(0, len(questions), 10)]
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
            c.setFont(SERIF_BOLD, 9.4)
            c.drawString(x + 7, cell_top - 15, f"Q{int(question['number']):02d}")
            c.drawRightString(x + col_w - 7, cell_top - 15, str(answer))
            draw_wrapped(c, answer_text, x + 7, cell_top - 32, col_w - 14, font=SERIF, size=8.2, leading=9.8, color=DARK)

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

    grade_label = GRADE_LABELS[grade]
    exam_label = f"{exam[:4]}年度 第{exam.split('-')[1]}回"
    total_pages = 10
    output_path.parent.mkdir(parents=True, exist_ok=True)
    pdf = canvas.Canvas(str(output_path), pagesize=A4, pageCompression=1, invariant=1)
    pdf.setTitle(f"ReadPass - {grade_label} {exam_label} 過去問演習")
    pdf.setAuthor("ECC Best One Aizumi / Kitajima-Chuo")
    pdf.setSubject("ReadPass fixed-layout practice exam")

    part1_instruction = sections[0].get("instruction", "")
    draw_questions_page(pdf, 1, total_pages, grade_label, exam_label, "大問1  語彙・文法  Q1-Q5", part1_instruction, part1[:5], "row4", first_page=True, grade=grade, exam=exam)
    draw_questions_page(pdf, 2, total_pages, grade_label, exam_label, "大問1  語彙・文法  Q6-Q10", part1_instruction, part1[5:10], "row4")
    draw_questions_page(pdf, 3, total_pages, grade_label, exam_label, "大問1  語彙・文法  Q11-Q15", part1_instruction, part1[10:15], "row4")
    draw_questions_page(
        pdf,
        4,
        total_pages,
        grade_label,
        exam_label,
        "大問2  会話文  Q16-Q20",
        sections[1].get("instruction", ""),
        part2,
        "row4" if grade == "grade-pre2" else "grid2",
        compact=(grade == "grade-pre2"),
    )

    if grade == "grade3":
        passages = sections[2].get("passages", [])
        part3_questions = [question for passage in passages for question in passage.get("questions", [])]
        if [len(part1), len(part2), len(part3_questions)] != [15, 5, 10]:
            raise ValueError("Grade 3 layout requires question counts 15 / 5 / 10")
        draw_passage_a_page(pdf, 5, total_pages, grade_label, exam_label, sections[2], passages[0])
        email_passage = passages[1]
        emails = email_passage.get("emails", [])
        email_title = clean_text(email_passage.get("title", "メール問題"))
        draw_emails_page(pdf, 6, total_pages, grade_label, exam_label, emails[:2], f"大問3B  {email_title}")
        final_email = emails[2] if len(emails) >= 3 else None
        draw_email_questions_page(pdf, 7, total_pages, grade_label, exam_label, email_title, final_email, email_passage.get("questions", []))
        draw_article_page(pdf, 8, total_pages, grade_label, exam_label, passages[2])
        draw_questions_page(pdf, 9, total_pages, grade_label, exam_label, "大問3C  長文設問  Q26-Q30", "前ページの本文を読み、最も適切なものを1つ選びなさい。", passages[2].get("questions", []), "stack", separator=True)
        all_questions = part1 + part2 + part3_questions
    else:
        passage_fill = sections[2].get("passages", [])[0]
        reading_passages = sections[3].get("passages", [])
        email_passage, article_passage = reading_passages
        count_signature = [
            len(part1),
            len(part2),
            len(passage_fill.get("questions", [])),
            len(email_passage.get("questions", [])),
            len(article_passage.get("questions", [])),
        ]
        if count_signature != [15, 5, 2, 3, 4]:
            raise ValueError("Grade Pre-2 layout requires question counts 15 / 5 / 2 / 3 / 4")
        draw_passage_fill_page(pdf, 5, total_pages, grade_label, exam_label, sections[2], passage_fill)
        draw_email_passage_page(pdf, 6, total_pages, grade_label, exam_label, email_passage)
        email_title = clean_text(email_passage.get("title", "メール問題"))
        draw_email_questions_page(
            pdf,
            7,
            total_pages,
            grade_label,
            exam_label,
            email_title,
            None,
            email_passage.get("questions", []),
            section_prefix="大問4A",
        )
        draw_article_page(
            pdf,
            8,
            total_pages,
            grade_label,
            exam_label,
            article_passage,
            section_title="大問4B  長文",
            instruction="本文を読み、次ページのQ26-Q29に答えなさい。",
        )
        draw_questions_page(
            pdf,
            9,
            total_pages,
            grade_label,
            exam_label,
            "大問4B  長文設問  Q26-Q29",
            "前ページの本文を読み、最も適切なものを1つ選びなさい。",
            article_passage.get("questions", []),
            "stack",
            separator=True,
        )
        all_questions = (
            part1
            + part2
            + passage_fill.get("questions", [])
            + email_passage.get("questions", [])
            + article_passage.get("questions", [])
        )

    draw_answer_page(pdf, 10, total_pages, grade_label, exam_label, all_questions, grade, exam)
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

#!/usr/bin/env python3
"""Render the GSIA Markdown manuscript as a submission PDF.

The renderer intentionally supports only the Markdown constructs used by the
manuscript: headings, paragraphs, ordered and unordered lists, pipe tables,
horizontal rules, links, emphasis, and inline code.
"""

from __future__ import annotations

import argparse
import html
import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    HRFlowable,
    ListFlowable,
    ListItem,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


NAVY = colors.HexColor("#18324D")
BLUE = colors.HexColor("#176B93")
LIGHT_BLUE = colors.HexColor("#EAF2F6")
GRID = colors.HexColor("#B8CAD5")
TEXT = colors.HexColor("#20262D")
MUTED = colors.HexColor("#52606D")


def register_fonts() -> tuple[str, str, str, str]:
    candidates = [
        (
            "/System/Library/Fonts/Supplemental/Arial.ttf",
            "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
            "/System/Library/Fonts/Supplemental/Arial Italic.ttf",
            "/System/Library/Fonts/Supplemental/Arial Bold Italic.ttf",
        ),
        (
            "/System/Library/Fonts/Supplemental/Helvetica.ttf",
            "/System/Library/Fonts/Supplemental/Helvetica Bold.ttf",
            "/System/Library/Fonts/Supplemental/Helvetica Oblique.ttf",
            "/System/Library/Fonts/Supplemental/Helvetica Bold Oblique.ttf",
        ),
    ]
    for regular, bold, italic, bold_italic in candidates:
        if all(Path(path).exists() for path in (regular, bold, italic, bold_italic)):
            pdfmetrics.registerFont(TTFont("GSIA", regular))
            pdfmetrics.registerFont(TTFont("GSIA-Bold", bold))
            pdfmetrics.registerFont(TTFont("GSIA-Italic", italic))
            pdfmetrics.registerFont(TTFont("GSIA-BoldItalic", bold_italic))
            pdfmetrics.registerFontFamily(
                "GSIA",
                normal="GSIA",
                bold="GSIA-Bold",
                italic="GSIA-Italic",
                boldItalic="GSIA-BoldItalic",
            )
            return "GSIA", "GSIA-Bold", "GSIA-Italic", "GSIA-BoldItalic"
    return "Helvetica", "Helvetica-Bold", "Helvetica-Oblique", "Helvetica-BoldOblique"


FONT, FONT_BOLD, FONT_ITALIC, FONT_BOLD_ITALIC = register_fonts()


def normalize_text(value: str) -> str:
    return (
        value.replace("\u2010", "-")
        .replace("\u2011", "-")
        .replace("\u2012", "-")
        .replace("\u2013", "-")
        .replace("\u2014", " - ")
        .replace("\u2212", "-")
        .replace("\u00a0", " ")
    )


def inline_markup(value: str) -> str:
    value = normalize_text(value)
    protected: dict[str, str] = {}

    def hold(markup: str) -> str:
        key = f"GSIAINLINE{len(protected)}TOKEN"
        protected[key] = markup
        return key

    def link_repl(match: re.Match[str]) -> str:
        label = html.escape(match.group(1))
        href = html.escape(match.group(2), quote=True)
        return hold(f'<link href="{href}" color="#176B93">{label}</link>')

    def code_repl(match: re.Match[str]) -> str:
        code = html.escape(match.group(1))
        return hold(f'<font name="Courier" color="#18324D">{code}</font>')

    value = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link_repl, value)
    value = re.sub(r"`([^`]+)`", code_repl, value)
    value = html.escape(value)
    value = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", value)
    value = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", value)
    for key, markup in protected.items():
        value = value.replace(key, markup)
    return value


def build_styles():
    base = getSampleStyleSheet()
    body = ParagraphStyle(
        "Body",
        parent=base["BodyText"],
        fontName=FONT,
        fontSize=8.7,
        leading=11.3,
        textColor=TEXT,
        spaceAfter=5.5,
        allowWidows=0,
        allowOrphans=0,
    )
    return {
        "title": ParagraphStyle(
            "Title",
            parent=body,
            fontName=FONT_BOLD,
            fontSize=20.5,
            leading=24,
            textColor=NAVY,
            spaceAfter=12,
            keepWithNext=True,
        ),
        "h2": ParagraphStyle(
            "H2",
            parent=body,
            fontName=FONT_BOLD,
            fontSize=14,
            leading=16,
            textColor=NAVY,
            spaceBefore=10,
            spaceAfter=5,
            keepWithNext=True,
        ),
        "h3": ParagraphStyle(
            "H3",
            parent=body,
            fontName=FONT_BOLD,
            fontSize=10.5,
            leading=12.5,
            textColor=BLUE,
            spaceBefore=7,
            spaceAfter=3,
            keepWithNext=True,
        ),
        "body": body,
        "meta": ParagraphStyle(
            "Meta",
            parent=body,
            fontSize=9,
            leading=11.5,
            spaceAfter=4,
        ),
        "small": ParagraphStyle(
            "Small",
            parent=body,
            fontSize=7.4,
            leading=9.2,
            textColor=MUTED,
        ),
        "table": ParagraphStyle(
            "Table",
            parent=body,
            fontSize=6.6,
            leading=8.1,
            spaceAfter=0,
        ),
        "table_header": ParagraphStyle(
            "TableHeader",
            parent=body,
            fontName=FONT_BOLD,
            fontSize=6.7,
            leading=8.2,
            textColor=colors.white,
            spaceAfter=0,
        ),
        "list": ParagraphStyle(
            "List",
            parent=body,
            leftIndent=0,
            firstLineIndent=0,
            spaceAfter=1.5,
        ),
        "footer": ParagraphStyle(
            "Footer",
            parent=body,
            fontSize=7,
            leading=8,
            textColor=MUTED,
            alignment=TA_CENTER,
        ),
    }


STYLES = build_styles()


def parse_pipe_row(line: str) -> list[str]:
    stripped = line.strip().strip("|")
    return [cell.strip() for cell in stripped.split("|")]


def is_table_separator(line: str) -> bool:
    cells = parse_pipe_row(line)
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells)


def table_widths(column_count: int, available: float) -> list[float]:
    if column_count == 2:
        ratios = [0.37, 0.63]
    elif column_count == 3:
        ratios = [0.22, 0.18, 0.60]
    elif column_count == 4:
        ratios = [0.12, 0.29, 0.25, 0.34]
    elif column_count == 5:
        ratios = [0.25, 0.16, 0.20, 0.20, 0.19]
    else:
        ratios = [1 / column_count] * column_count
    return [available * ratio for ratio in ratios]


def make_table(rows: list[list[str]], available: float) -> Table:
    column_count = max(len(row) for row in rows)
    padded = [row + [""] * (column_count - len(row)) for row in rows]
    data = []
    for row_index, row in enumerate(padded):
        style = STYLES["table_header"] if row_index == 0 else STYLES["table"]
        data.append([Paragraph(inline_markup(cell), style) for cell in row])
    table = Table(
        data,
        colWidths=table_widths(column_count, available),
        repeatRows=1,
        hAlign=TA_LEFT,
        splitByRow=1,
    )
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), NAVY),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("GRID", (0, 0), (-1, -1), 0.35, GRID),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT_BLUE]),
            ]
        )
    )
    return table


def markdown_story(source: Path, available: float):
    lines = source.read_text(encoding="utf-8").splitlines()
    story = []
    index = 0
    first_heading = True

    while index < len(lines):
        line = lines[index].rstrip()
        stripped = line.strip()
        if not stripped:
            index += 1
            continue

        if stripped == "---":
            story.extend(
                [
                    Spacer(1, 5),
                    HRFlowable(width="100%", thickness=0.7, color=GRID),
                    Spacer(1, 5),
                ]
            )
            index += 1
            continue

        if stripped.startswith("|") and index + 1 < len(lines):
            next_line = lines[index + 1].strip()
            if next_line.startswith("|") and is_table_separator(next_line):
                rows = [parse_pipe_row(stripped)]
                index += 2
                while index < len(lines) and lines[index].strip().startswith("|"):
                    rows.append(parse_pipe_row(lines[index]))
                    index += 1
                story.extend([make_table(rows, available), Spacer(1, 6)])
                continue

        heading = re.match(r"^(#{1,3})\s+(.+)$", stripped)
        if heading:
            level = len(heading.group(1))
            text = inline_markup(heading.group(2))
            if first_heading and level == 1:
                story.append(Paragraph(text, STYLES["title"]))
                story.append(HRFlowable(width="100%", thickness=1.4, color=BLUE))
                story.append(Spacer(1, 10))
                first_heading = False
            else:
                story.append(Paragraph(text, STYLES["h2" if level == 2 else "h3"]))
            index += 1
            continue

        list_match = re.match(r"^(\d+)\.\s+(.+)$", stripped)
        bullet_match = re.match(r"^-\s+(.+)$", stripped)
        if list_match or bullet_match:
            ordered = bool(list_match)
            items = []
            while index < len(lines):
                current = lines[index].strip()
                match = (
                    re.match(r"^(\d+)\.\s+(.+)$", current)
                    if ordered
                    else re.match(r"^-\s+(.+)$", current)
                )
                if not match:
                    break
                value = match.group(2) if ordered else match.group(1)
                items.append(
                    ListItem(
                        Paragraph(inline_markup(value), STYLES["list"]),
                        leftIndent=12,
                    )
                )
                index += 1
            story.append(
                ListFlowable(
                    items,
                    bulletType="1" if ordered else "bullet",
                    start="1" if ordered else "\u2022",
                    leftIndent=18,
                    bulletFontName=FONT,
                    bulletFontSize=8,
                    bulletColor=NAVY,
                    spaceAfter=5,
                )
            )
            continue

        paragraph_lines = [stripped]
        index += 1
        while index < len(lines):
            candidate = lines[index].strip()
            if not candidate:
                break
            if (
                candidate == "---"
                or re.match(r"^#{1,3}\s+", candidate)
                or re.match(r"^\d+\.\s+", candidate)
                or re.match(r"^-\s+", candidate)
                or candidate.startswith("|")
            ):
                break
            paragraph_lines.append(candidate)
            index += 1
        paragraph = " ".join(paragraph_lines)
        style = STYLES["meta"] if len(story) < 12 else STYLES["body"]
        story.append(Paragraph(inline_markup(paragraph), style))

    return story


class GSIAProfile:
    title = "The Global Spectral Index Atlas - Version 3"
    author = "Daniel Bally"
    subject = "Open registry and structural audit of environmental remote-sensing method specifications"
    keywords = "remote sensing, spectral index, Sentinel-2, band algebra, validation, open science"


def draw_page(canvas, document):
    canvas.saveState()
    canvas.setTitle(GSIAProfile.title)
    canvas.setAuthor(GSIAProfile.author)
    canvas.setSubject(GSIAProfile.subject)
    canvas.setKeywords(GSIAProfile.keywords)
    width, _ = LETTER
    if document.page > 1:
        canvas.setStrokeColor(GRID)
        canvas.setLineWidth(0.4)
        canvas.line(0.72 * inch, 0.54 * inch, width - 0.72 * inch, 0.54 * inch)
    canvas.setFont(FONT, 7)
    canvas.setFillColor(MUTED)
    canvas.drawCentredString(width / 2, 0.34 * inch, str(document.page))
    canvas.restoreState()


def render(source: Path, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    document = BaseDocTemplate(
        str(output),
        pagesize=LETTER,
        leftMargin=0.72 * inch,
        rightMargin=0.72 * inch,
        topMargin=0.66 * inch,
        bottomMargin=0.68 * inch,
        title=GSIAProfile.title,
        author=GSIAProfile.author,
        subject=GSIAProfile.subject,
    )
    frame = Frame(
        document.leftMargin,
        document.bottomMargin,
        document.width,
        document.height,
        id="normal",
    )
    document.addPageTemplates(
        [PageTemplate(id="GSIA", frames=[frame], onPage=draw_page)]
    )
    story = markdown_story(source, document.width)
    document.build(story)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    render(args.source, args.output)


if __name__ == "__main__":
    main()

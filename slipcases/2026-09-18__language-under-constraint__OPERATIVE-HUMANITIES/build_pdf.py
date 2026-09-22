#!/usr/bin/env python3
from pathlib import Path
import re, textwrap
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "Language_Under_Constraint_Operative_Humanities_FINAL.md"
OUT = ROOT / "Language_Under_Constraint_Operative_Humanities_FINAL.pdf"

styles = getSampleStyleSheet()
body = ParagraphStyle("Body", parent=styles["BodyText"], fontName="Times-Roman", fontSize=10.8, leading=14.2, spaceAfter=7)
title = ParagraphStyle("TitleX", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=25, leading=29, spaceAfter=6, alignment=TA_LEFT)
subtitle = ParagraphStyle("SubtitleX", parent=styles["Normal"], fontName="Helvetica-Oblique", fontSize=12.5, textColor=colors.HexColor("#555555"), leading=16, spaceAfter=14)
h1 = ParagraphStyle("H1X", parent=styles["Heading1"], fontName="Helvetica-Bold", fontSize=15, leading=18, spaceBefore=13, spaceAfter=6)
abstract = ParagraphStyle("AbstractX", parent=body, fontName="Times-Italic", fontSize=9.8, leading=12.8, leftIndent=0.32*inch, rightIndent=0.32*inch)
ref = ParagraphStyle("RefX", parent=body, fontSize=9.2, leading=11.5, leftIndent=0.28*inch, firstLineIndent=-0.28*inch, spaceAfter=4)
meta = ParagraphStyle("MetaX", parent=styles["Normal"], fontName="Helvetica", fontSize=8.5, textColor=colors.HexColor("#666666"), leading=11, spaceAfter=9)

def esc(s):
    s = s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"\*(.+?)\*", r"<i>\1</i>", s)
    s = re.sub(r"`(.+?)`", r"<font name='Courier'>\1</font>", s)
    return s

lines = SRC.read_text(encoding="utf-8").splitlines()
story=[]
in_refs=False
i=0
while i < len(lines):
    line=lines[i].strip()
    if not line:
        story.append(Spacer(1,5))
        i+=1; continue
    if line.startswith("# "):
        story.append(Paragraph(esc(line[2:]), title))
    elif line.startswith("## "):
        txt=line[3:]
        if txt=="Semantic Instruments for Operative Humanities":
            story.append(Paragraph(esc(txt), subtitle))
        elif txt=="References":
            in_refs=True
            story.append(Paragraph(txt, h1))
        else:
            story.append(Paragraph(esc(txt), h1))
    elif line.startswith("**Working Paper"):
        story.append(Paragraph(esc(line.replace("**","")), meta))
    elif line.startswith("### Abstract"):
        # collect until next heading/keywords
        buf=[]
        i+=1
        while i<len(lines):
            t=lines[i].strip()
            if t.startswith("**Keywords:**") or t.startswith("## "):
                i-=1; break
            if t: buf.append(t)
            i+=1
        story.append(Paragraph("<b>Abstract.</b> "+esc(" ".join(buf)), abstract))
    elif line.startswith("**Keywords:**"):
        story.append(Paragraph(esc(line.replace("**","")), meta))
    elif in_refs:
        story.append(Paragraph(esc(line), ref))
    else:
        story.append(Paragraph(esc(line), body))
    i+=1

def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#777777"))
    canvas.drawCentredString(LETTER[0]/2, 0.45*inch, f"Language Under Constraint · Working Paper · {doc.page}")
    canvas.restoreState()

pdf=SimpleDocTemplate(str(OUT), pagesize=LETTER, rightMargin=0.9*inch, leftMargin=0.9*inch, topMargin=0.75*inch, bottomMargin=0.7*inch,
                      title="Language Under Constraint: Semantic Instruments for Operative Humanities")
pdf.build(story, onFirstPage=footer, onLaterPages=footer)
print(OUT)

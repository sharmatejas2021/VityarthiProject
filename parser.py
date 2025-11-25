# parser.py
# reads PDF or DOCX files directly from memory
# keeps things simple for beginners

import re
from PyPDF2 import PdfReader
from docx import Document

def _clean(text):
    if not text:
        return ""
    text = text.replace("\xa0", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def _read_pdf(stream):
    try:
        reader = PdfReader(stream)
        pages = []
        for p in reader.pages:
            pages.append(p.extract_text() or "")
        return "\n".join(pages)
    except:
        return ""

def _read_docx(stream):
    try:
        stream.seek(0)
        doc = Document(stream)
        return "\n".join([p.text for p in doc.paragraphs if p.text])
    except:
        return ""

def extract_text_from_fileobj(file, filename):
    name = filename.lower()
    if name.endswith(".pdf"):
        return _clean(_read_pdf(file))
    if name.endswith(".docx"):
        return _clean(_read_docx(file))
    try:
        raw = file.read().decode("utf-8", "ignore")
        return _clean(raw)
    except:
        return ""

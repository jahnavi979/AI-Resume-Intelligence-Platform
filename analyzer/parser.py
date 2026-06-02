import pdfplumber
from docx import Document

def extract_text_from_pdf(file_obj):
    text = ""
    with pdfplumber.open(file_obj) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def extract_text_from_docx(file_obj):
    doc = Document(file_obj)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

def extract_text(file_obj, filename):
    if filename.lower().endswith(".pdf"):
        return extract_text_from_pdf(file_obj)
    elif filename.lower().endswith(".docx"):
        return extract_text_from_docx(file_obj)
    return ""
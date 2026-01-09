from pypdf import PdfReader
from docx import Document

def load_pdf(file):
    reader = PdfReader(file)
    return "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])

def load_docx(file):
    doc = Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

def load_txt(file):
    return file.read().decode("utf-8")

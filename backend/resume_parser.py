from pypdf import PdfReader
import re


def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text

    return text


# Known skills database
SKILLS_DB = [
    "python",
    "java",
    "c++",
    "sql",
    "machine learning",
    "deep learning",
    "react",
    "node.js",
    "docker",
    "kubernetes",
    "tensorflow",
    "pytorch",
    "data analysis",
    "flask",
    "fastapi",
    "html",
    "css",
    "javascript",
    "mysql",
    "kotlin",
    "xml",
    "matlab",
    "autocad",
    "figma",
    "canva",
    "ui/ux"
]


def clean_text(text):
    """
    Fix PDFs that separate letters with spaces:
    P Y T H O N → python
    """
    text = text.lower()

    # collapse spaced letters
    text = re.sub(r'(?<=\b)([a-z])\s(?=[a-z]\b)', r'\1', text)

    return text


def extract_skills(text):
    text = clean_text(text)
    found_skills = []

    for skill in SKILLS_DB:
        if skill in text:
            found_skills.append(skill)

    return found_skills


def parse_resume(file_path):
    text = extract_text_from_pdf(file_path)
    skills = extract_skills(text)

    return {
        "text": text,
        "skills": skills
    }
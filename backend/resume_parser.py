from pypdf import PdfReader
import io
import re


# ---------------------------
# 1. Extract text from PDF
# ---------------------------
def extract_text_from_resume(file_bytes):
    pdf = PdfReader(io.BytesIO(file_bytes))
    text = ""

    for page in pdf.pages:
        text += page.extract_text() or ""

    return text


# ---------------------------
# 2. Skill database
# ---------------------------
SKILLS_DB = [
    "python", "java", "c++", "sql",
    "machine learning", "deep learning",
    "react", "node.js", "docker", "kubernetes",
    "tensorflow", "pytorch",
    "html", "css", "javascript", "mysql",
    "kotlin", "xml", "matlab", "autocad",
    "figma", "canva", "ui/ux"
]


# ---------------------------
# 3. Clean text (fix spaced letters)
# ---------------------------
def clean_text(text):
    text = text.lower()

    # Fix "P Y T H O N" → "python"
    text = re.sub(r'(\b[a-z])\s(?=[a-z]\b)', r'\1', text)

    return text


# ---------------------------
# 4. Extract skills
# ---------------------------
def extract_skills(text):
    text = clean_text(text)
    found_skills = []

    for skill in SKILLS_DB:
        if skill in text:
            found_skills.append(skill)

    return found_skills


# ---------------------------
# 5. FINAL FUNCTION (IMPORTANT)
# ---------------------------
def parse_resume(file_bytes):
    text = extract_text_from_resume(file_bytes)
    skills = extract_skills(text)

    return {
        "text": text,
        "skills": skills
    }
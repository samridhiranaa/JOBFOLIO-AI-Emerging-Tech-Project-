from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os

from backend.resume_parser import parse_resume
from backend.jd_parser import extract_skills_from_jd
from backend.skill_gap import analyze_skill_gap
from backend.ats_scoring import calculate_ats_score
from rag.retriever import retrieve_context

app = FastAPI()

# Enable CORS (for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Home route
@app.get("/")
def home():
    return {"message": "Jobfolio AI Backend Running"}


# Main analysis endpoint
@app.post("/analyze")
async def analyze_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):

    resume_bytes = await resume.read()

    parsed_resume = parse_resume(resume_bytes)
    resume_skills = parsed_resume["skills"]

    # ---------------------------
    # 3. Parse Job Description
    # ---------------------------
    job_skills = extract_skills_from_jd(job_description)

    # ---------------------------
    # 4. Skill Gap Analysis
    # ---------------------------
    gap = analyze_skill_gap(resume_skills, job_skills)

    # ---------------------------
    # 5. ATS Score Calculation
    # ---------------------------
    ats = calculate_ats_score(
        gap["match_percentage"],
        experience_years=1,          # you can later extract this from resume
        required_experience=2,
        education_level="bachelor"
    )

    # ---------------------------
    # 6. RAG Project Suggestions
    # ---------------------------
    query = " ".join(gap["missing_skills"])
    projects = retrieve_context(query)


    # ---------------------------
    # 8. Final Response
    # ---------------------------
    return {
        "ats_score": ats["ats_score"],
        "matched_skills": gap["matched_skills"],
        "missing_skills": gap["missing_skills"],
        "match_percentage": gap["match_percentage"],
        "recommended_projects": projects
    }
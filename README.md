# Jobfolio AI – Resume Intelligence System

An **AI-powered resume analysis platform** that evaluates a candidate’s resume against a job description using **Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), and Data Visualization**.

The system identifies **skill gaps, ATS compatibility, and role match percentage**, while also recommending **projects and improvements** to strengthen the resume.

---

## Project Overview

Recruiters often use **Applicant Tracking Systems (ATS)** to filter resumes. Many candidates fail to pass these systems because their resumes lack required skills or keywords.

**Jobfolio AI** solves this problem by:

* Analyzing resumes using AI
* Comparing them with job descriptions
* Identifying missing skills
* Providing an ATS compatibility score
* Recommending improvements and projects

The platform also visualizes insights through **interactive dashboards**.

---

## Key Technologies

| Technology                               | Purpose                                   |
| ---------------------------------------- | ----------------------------------------- |
| **LLM (OpenAI / Gemini)**                | Resume analysis and recommendations       |
| **RAG (Retrieval-Augmented Generation)** | Context retrieval for project suggestions |
| **FAISS Vector Database**                | Efficient knowledge retrieval             |
| **FastAPI**                              | Backend API                               |
| **Python**                               | Core development language                 |
| **React**                                | Frontend interface                        |
| **Recharts / Chart.js**                  | Data visualization dashboards             |

---

## Core Features

### Resume & Job Description Analysis

Upload a resume and provide a job description.
The system analyzes compatibility using AI.

### ATS Score Estimation

Generates an **ATS compatibility score** based on:

* skill alignment
* experience relevance
* keyword coverage

### Skill Gap Detection

Identifies missing skills required for the target job role.

Example:

```
Required Skills:
Python, SQL, Docker, Machine Learning

Resume Skills:
Python, SQL

Missing Skills:
Docker, Machine Learning
```

---

### Role Match Percentage

Estimates how closely the resume matches the job role.

Example output:

```
Frontend Developer: 58%
Backend Developer: 74%
Machine Learning Engineer: 42%
```

---

### Recommended Projects

Using the **RAG system**, Jobfolio retrieves relevant project ideas to help users close their skill gaps.

Example:

Missing Skill: Docker

Suggested Projects:

* Dockerized Flask API
* CI/CD Pipeline with Docker and GitHub Actions

---

### Data Visualization Dashboard

The system generates interactive charts:

* **ATS Score Gauge**
* **Skill Gap Bar Chart**
* **Role Match Radar Chart**

These visualizations help users easily understand their resume performance.

---

## System Architecture

```
User
 │
 │ Upload Resume + Job Description
 ▼
Backend (FastAPI)
 │
 ├─ Resume Parser
 │      Extract skills and experience
 │
 ├─ Skill Gap Analyzer
 │      Compare resume vs job requirements
 │
 ├─ RAG Retrieval
 │      Retrieve relevant knowledge and projects
 │
 ├─ LLM Analysis
 │      Generate insights and recommendations
 │
 └─ Visualization Engine
        Generate dashboard charts
```

---

## Project Structure

```
JOBFOLIO-AI
│
├── backend
│   ├── main.py
│   ├── resume_parser.py
│   ├── jd_parser.py
│   ├── skill_gap.py
│   ├── ats_scoring.py
│   └── llm_analysis.py
│
├── rag
│   ├── vector_store.py
│   └── retriever.py
│
├── data
│   └── skills_database.txt
│
├── frontend
│
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```
git clone https://github.com/samridhiranaa/JOBFOLIO-AI-Emerging-Tech-Project-
cd JOBFOLIO-AI-Emerging-Tech-Project-
```

Create a virtual environment:

```
python -m venv venv
```

Activate environment:

Windows

```
venv\Scripts\activate
```

Mac/Linux

```
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the backend server:

```
uvicorn main:app --reload
```

---

## Example Workflow

1. User uploads resume
2. User pastes job description
3. Resume text is extracted
4. Skills are compared with job requirements
5. Missing skills are detected
6. RAG retrieves relevant project suggestions
7. LLM generates insights
8. Dashboard visualizes results

---

## Future Improvements

* Automatic resume rewriting
* Multi-role compatibility analysis
* Integration with job platforms
* AI career advisor chatbot
* Real-time resume optimization

---

## Author

**Samridhi Rana**

BTech Computer Science
Manipal University Jaipur


This project is for **educational and research purposes**.

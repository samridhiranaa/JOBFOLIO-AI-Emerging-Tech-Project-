def analyze_skill_gap(resume_skills, job_skills):

    # Convert to sets for comparison
    resume_set = set([skill.lower() for skill in resume_skills])
    job_set = set([skill.lower() for skill in job_skills])

    # Matched skills
    matched_skills = resume_set.intersection(job_set)

    # Missing skills
    missing_skills = job_set.difference(resume_set)

    # Skill match percentage
    if len(job_set) == 0:
        match_percentage = 0
    else:
        match_percentage = (len(matched_skills) / len(job_set)) * 100

    result = {
        "matched_skills": list(matched_skills),
        "missing_skills": list(missing_skills),
        "match_percentage": round(match_percentage, 2)
    }

    return result


if __name__ == "__main__":

    resume_skills = ["Python", "SQL"]

    job_skills = ["Python", "SQL", "Docker", "Machine Learning"]

    analysis = analyze_skill_gap(resume_skills, job_skills)

    print("\nMatched Skills:", analysis["matched_skills"])
    print("Missing Skills:", analysis["missing_skills"])
    print("Skill Match %:", analysis["match_percentage"])
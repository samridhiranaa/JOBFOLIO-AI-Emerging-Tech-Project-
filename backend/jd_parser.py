import re

def load_skills_database(file_path="data/skills_database.txt"):
    skills = []
    
    with open(file_path, "r") as f:
        for line in f:
            skills.append(line.strip().lower())
    
    return skills


def extract_skills_from_jd(job_description):

    skills_db = load_skills_database()
    jd_text = job_description.lower()

    found_skills = []

    for skill in skills_db:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, jd_text):
            found_skills.append(skill.title())

    return list(set(found_skills))


if __name__ == "__main__":

    jd_text = """
    We are looking for a Python developer with experience in
    Machine Learning, SQL, Docker, and REST APIs.
    """

    skills = extract_skills_from_jd(jd_text)

    print("Extracted Skills:", skills)
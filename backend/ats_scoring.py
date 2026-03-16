def calculate_ats_score(skill_match, experience_years, required_experience, education_level):

    # ----- Skill Score -----
    skill_score = skill_match

    # ----- Experience Score -----
    if experience_years >= required_experience:
        experience_score = 100
    else:
        experience_score = (experience_years / required_experience) * 100

    # ----- Education Score -----
    education_weights = {
        "phd": 100,
        "masters": 90,
        "bachelor": 80,
        "diploma": 60,
        "high school": 40
    }

    education_score = education_weights.get(education_level.lower(), 50)

    # ----- Resume Formatting Score -----
    # (simple placeholder rule)
    format_score = 80

    # ----- Weighted ATS Score -----
    ats_score = (
        skill_score * 0.4 +
        experience_score * 0.3 +
        education_score * 0.2 +
        format_score * 0.1
    )

    result = {
        "ats_score": round(ats_score, 2),
        "skill_score": skill_score,
        "experience_score": round(experience_score, 2),
        "education_score": education_score,
        "format_score": format_score
    }

    return result


if __name__ == "__main__":

    skill_match = 60
    experience_years = 1
    required_experience = 2
    education_level = "Bachelor"

    score = calculate_ats_score(
        skill_match,
        experience_years,
        required_experience,
        education_level
    )

    print("\nATS Score:", score["ats_score"])
    print("Skill Score:", score["skill_score"])
    print("Experience Score:", score["experience_score"])
    print("Education Score:", score["education_score"])
    print("Formatting Score:", score["format_score"])
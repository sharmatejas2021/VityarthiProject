# scoring.py
# friendly and readable scoring logic

import json
import re

with open("skill_data.json", "r", encoding="utf-8") as f:
    SKILLS = json.load(f)

def _norm(s):
    return re.sub(r"[^a-z0-9 ]", " ", s.lower())

def find_skills(text):
    t = _norm(text or "")
    found = []
    for s in SKILLS:
        if s.lower() in t:
            found.append(s)
    return sorted(set(found))

def estimate_experience(text):
    if not text:
        return 0
    t = text.lower()
    m = re.findall(r"(\d+)\s*\+?\s*years?", t)
    if m:
        try:
            return max(int(x) for x in m)
        except:
            pass
    return 0

def score_resume(skills, years):
    skill_score = int((len(skills) / len(SKILLS)) * 100) if SKILLS else 0
    exp_score = min(30, years * 5)
    fmt_score = 20
    total = int(skill_score * 0.5 + exp_score + fmt_score)
    return min(100, total)

def evaluate_resume(text):
    if not text:
        return {
            "score": 0,
            "skills": [],
            "experience_years": 0,
            "message": "No readable text found.",
            "suggestions": ["Try uploading a clearer resume."]
        }

    skills = find_skills(text)
    years = estimate_experience(text)
    score = score_resume(skills, years)

    suggestions = []
    if len(skills) < 3:
        suggestions.append("Consider adding more technical skills.")
    if years < 2:
        suggestions.append("Add internships or small projects.")
    if "education" not in text.lower():
        suggestions.append("Include an Education section.")

    return {
        "score": score,
        "skills": skills,
        "experience_years": years,
        "message": "Resume checked successfully.",
        "suggestions": suggestions
    }

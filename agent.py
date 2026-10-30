"""Compare resume evidence with declared job requirements for recruiter review."""
from __future__ import annotations


def review_resume(requirements: dict, resume: dict) -> dict:
    required = {str(value).lower() for value in requirements.get("required_skills", [])}
    skills = {str(value).lower() for value in resume.get("skills", [])}
    matched, missing = sorted(required & skills), sorted(required - skills)
    minimum = max(float(requirements.get("minimum_years", 0)), 0)
    years = max(float(resume.get("years_experience", 0)), 0)
    coverage = round(len(matched) / len(required), 2) if required else 1.0
    return {"candidate_id": resume.get("candidate_id"), "skill_coverage": coverage, "matched_skills": matched, "missing_or_unverified_skills": missing, "experience_evidence": {"reported_years": years, "minimum_years": minimum, "meets_declared_minimum": years >= minimum}, "protected_characteristics_used": False, "decision": None, "uncertainty": "Resume claims are self-reported and may use different terminology.", "recruiter_review_required": True}

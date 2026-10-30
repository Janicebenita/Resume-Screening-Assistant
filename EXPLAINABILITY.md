# Resume Screening Assistant Explainability

## Decision and Reasoning Process

The agent's decision support compares resume evidence with the job's stated essential and preferred criteria. Its reasoning identifies matched requirements, gaps, ambiguous claims, and suggested verification questions.

## Inputs and Data Sources Used

Input data includes the job description, recruiter-defined criteria, and candidate-provided resume. No hidden profile data or inferred protected characteristics are used as data sources.

## Outputs and Supporting Evidence

The output contains a criterion-by-criterion summary, evidence citations, missing information, and interview questions. Each observation points to the relevant resume text or declared job requirement.

## Limits, Constraints, and Known Issues

A major limitation is that a resume may be incomplete, exaggerated, or formatted poorly. The agent is constrained from making autonomous hiring decisions or treating missing information as proof of ineligibility.

## Uncertainty and Human Review

Uncertainty is clearly marked when evidence is incomplete or terminology differs. Human review is mandatory before any employment decision.

## Implementation in This Repository

`agent.py` implements `review_resume(requirements, resume)`. It normalizes declared role and resume skills, reports matched and missing-or-unverified skills, compares reported with minimum experience, retains the exact evidence, excludes protected characteristics, returns no decision, states resume uncertainty, and requires recruiter review. `test_agent.py` verifies that missing skills remain visible and no decision is made.

No applicant-tracking integration or trained hiring model is included. Every employment decision remains under human control.

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

The repository is a declarative OpenGAP implementation consisting of `agent.yaml`, `SOUL.md`, this explainability file, and `README.md`. The manifest describes resume and job-requirement inputs and an evidence-linked review output; the policy documents require uncertainty reporting and prohibit autonomous selection or rejection.

No applicant-tracking integration or trained hiring model is included. A compatible host must show the supporting resume evidence to a human reviewer and keep every employment decision under human control.

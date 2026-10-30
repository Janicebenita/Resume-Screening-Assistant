import unittest
from agent import review_resume


class ResumeTests(unittest.TestCase):
    def test_review_reports_evidence_without_decision(self):
        result = review_resume({"required_skills": ["Python", "SQL"]}, {"skills": ["Python"]})
        self.assertEqual(result["missing_or_unverified_skills"], ["sql"])
        self.assertIsNone(result["decision"])


if __name__ == "__main__":
    unittest.main()

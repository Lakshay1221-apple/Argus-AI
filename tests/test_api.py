import unittest
from unittest.mock import patch
from fastapi.testclient import TestClient

# Mock ModelLoader.load_model and generate_response before importing app
with patch('argus.resume.api.model_loader.ModelLoader.load_model') as mock_load:
    from argus.resume.api.main import app

class TestResumeAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_health_check(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], "ok")
        self.assertIn("gpu_stats", data)

    @patch('argus.resume.api.model_loader.ModelLoader.generate_response')
    def test_resume_summary(self, mock_generate):
        mock_generate.return_value = "This is a mock resume summary."
        
        response = self.client.post("/summary", json={"resume_text": "John Doe Resume..."})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["summary"], "This is a mock resume summary.")
        mock_generate.assert_called_once_with(
            instruction="Generate a professional resume summary.",
            input_text="John Doe Resume...",
            max_new_tokens=250
        )

    @patch('argus.resume.api.model_loader.ModelLoader.generate_response')
    def test_ats_review_success(self, mock_generate):
        # Valid JSON response from model
        mock_generate.return_value = (
            '{\n  "ats_score": 85,\n  "strengths": ["Clear format"],\n  '
            '"weaknesses": ["No metrics"],\n  "suggestions": ["Add numbers"],\n  '
            '"verdict": "Strong Fit"\n}'
        )
        
        response = self.client.post("/review", json={"resume_text": "Resume..."})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["ats_score"], 85)
        self.assertEqual(data["strengths"], ["Clear format"])
        self.assertEqual(data["verdict"], "Strong Fit")

    @patch('argus.resume.api.model_loader.ModelLoader.generate_response')
    def test_ats_review_malformed_json_repair(self, mock_generate):
        # Malformed markdown JSON response that needs repair
        mock_generate.return_value = (
            "Here is the feedback:\n"
            "```json\n"
            "{\n"
            "  \"ats_score\": 90,\n"
            "  \"strengths\": [\"Python experience\"],\n"
            "  \"weaknesses\": [\"No education listed\"],\n"
            "  \"suggestions\": [\"Add education section\"],\n"
            "  \"verdict\": \"Potential Fit\",\n"  # trailing comma
            "}\n"
            "```"
        )
        
        response = self.client.post("/review", json={"resume_text": "Resume..."})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["ats_score"], 90)
        self.assertEqual(data["strengths"], ["Python experience"])
        self.assertEqual(data["verdict"], "Potential Fit")

    @patch('argus.resume.api.model_loader.ModelLoader.generate_response')
    def test_classify_section(self, mock_generate):
        mock_generate.return_value = "Experience"
        
        response = self.client.post("/classify-section", json={"section_text": "2020-2022: Developer"})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["label"], "Experience")

    @patch('argus.resume.api.model_loader.ModelLoader.generate_response')
    def test_job_fit(self, mock_generate):
        mock_generate.return_value = "Fit"
        
        response = self.client.post("/job-fit", json={
            "resume_text": "Experienced web developer",
            "job_description": "Hiring a web developer"
        })
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["fit"], "Fit")

if __name__ == "__main__":
    unittest.main()

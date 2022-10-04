"""Test for service API
"""

import sys
import json
import unittest
from pathlib import Path
from dotenv import load_dotenv
from fastapi.testclient import TestClient

BASE_DIR = Path(__file__).resolve().parent.parent
TEST_DIR = Path(__file__).resolve().parent
ENV_PATH = BASE_DIR / ".env"

sys.path.append(BASE_DIR.as_posix())
load_dotenv(ENV_PATH.as_posix())

from main import app

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)
        self.file_path = TEST_DIR.as_posix() + "/test-data/patents/US11325698B2.json"

    def test_classify_route(self):
        with open(self.file_path, "r") as test_file:
            test_data = json.load(test_file)
        input_text = test_data["abstract"]
        text = input_text
        n = 5
        data = {"text": text, "n": n, "model": "BOWSubclassPredictor"}
        response = self.client.post("/classify", json=data)
        self.assertEqual(200, response.status_code)


if __name__ == "__main__":
    unittest.main()

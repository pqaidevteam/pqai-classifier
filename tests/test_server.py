"""Test for service API
Attributes:
    dotenv_file (str): Absolute path to .env file (used for reading port no.)
    HOST (str): IP address of the host where service is running
    PORT (str): Port no. on which the server is listening
    PROTOCOL (str): `http` or `https`
"""
import os
import sys
import json
import unittest
from pathlib import Path
import requests
from dotenv import load_dotenv

env_file = str((Path(__file__).parent.parent / ".env").resolve())
load_dotenv(env_file)

test_dir = str(Path(__file__).parent.resolve())
BASE_DIR = Path(__file__).parent.parent
sys.path.append(str(BASE_DIR.resolve()))

PROTOCOL = "http"
HOST = "localhost"
PORT = os.environ["PORT"]
API_ENDPOINT = "{}://{}:{}".format(PROTOCOL, HOST, PORT)


class TestAPI(unittest.TestCase):
    """For testing server api"""

    def setUp(self):
        """Initial setup"""
        self.file_path = test_dir + "/test-data/patents/US11325698B2.json"

    def test_classify_route(self):
        """Tests the server api request route"""
        with open(self.file_path, "r") as test_file:
            test_data = json.load(test_file)
        input_text = test_data["abstract"]
        text = input_text
        n = 5
        data = {"text": text, "n": n, "model": "BOWSubclassPredictor"}
        response = self.call_route("/classify", data=data)
        self.assertEqual(200, response.status_code)

    def call_route(self, route, data):
        """Make request to given route with given parameters
        Args:
            route (str): Route, e.g. '/search'
            params (dict): Query string parameters
        Returns:
            response: Response against HTTP request
        """
        route = route.lstrip("/")
        url = f"{PROTOCOL}://{HOST}:{PORT}/{route}"
        response = requests.post(url, json=data)
        return response


if __name__ == "__main__":
    unittest.main()

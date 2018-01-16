import unittest
from flask_api import FlaskAPI
import requests

class TestFlaskAPIUsingRequests(unittest.TestCase):
    def test_api_for_404(self):
        response = requests.get('http://localhost:5000')
        print "code:",response.status_code
        self.assertEqual(response.status_code,404)
    def test_api_path_for_404(self):
        response = requests.get('http://localhost:5000/api')
        print "code:",response.status_code
        self.assertEqual(response.status_code,404)

if __name__ == "__main__":
    unittest.main()

import unittest
from flask_api import FlaskAPI
import requests

headers = {
'Host': 'localhost:5000',
'Accept': 'application/json, text/plain, */*',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate',
'Referer': 'http://localhost:3000/',
'Content-Type': 'application/x-www-form-urlencoded',
'Content-Length': '28',
'Origin': 'http://localhost:3000',
'Connection': 'close'
}
payload = {''}
class TestFlaskAPIUsingRequests(unittest.TestCase):
    def test_api_for_404(self):
        response = requests.get('http://localhost:5000')
        print "code:",response.status_code
        self.assertEqual(response.status_code,404)
    def test_api_path_for_404(self):
        response = requests.get('http://localhost:5000/api')
        print "code:",response.status_code
        self.assertEqual(response.status_code,404)
    def test_api_login(self):
        resp = requests.post('http://localhost:5000/api/login',"user_name=rand&password=pass",headers=headers)
        print(resp.status_code)
	print(resp.json())
        self.assertEqual(resp.json(),{u'auth': u'0'})
if __name__ == "__main__":
    unittest.main()
			
			

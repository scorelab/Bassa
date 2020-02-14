import unittest
import requests
import logging as logger
from flask import g

headers = {
    'Host': 'localhost:5000',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'http://localhost:3000',
}
user_data = {
    "user_name": "user",
    "password": "password",
    "email": "user@email.com",
    "auth": "0"
}

regular_user_data = {
    "user_name": "reg_user",
    "password": "password",
    "email": "regular_user@email.com",
}

correctlogin = "user_name=rand&password=pass"

url = "http://localhost:5000/api"

class TestFlaskAPIUsingRequests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super(TestFlaskAPIUsingRequests, cls).setUpClass()
        resp = requests.post(url + '/login', correctlogin, headers=headers)
        cls.token = resp.headers['token']

    def test_api_user_login(self):
        resp = requests.post(url + '/user', json=user_data,
                             headers={'Content-Type': 'application/json', 'token': self.token,
                                      'Access-Control-Expose-Headers': 'token',
                                      'Access-Control-Allow-Origin': 'http://localhost:3000'})
        self.assertEqual(resp.status_code, 200)

    def test_api_regular_user_login(self):
        resp = requests.post(url + '/regularuser', json=regular_user_data,
                             headers={'Content-Type': 'application/json'})
        self.assertEqual(resp.status_code, 200)

    def test_api_remove_user_request(self):
        resp = requests.delete(url + '/user/user',
                               headers={'token': self.token, 'Access-Control-Expose-Headers': 'token',
                                        'Access-Control-Allow-Origin': 'http://localhost:3000'})
        self.assertEqual(resp.status_code, 200)


if __name__ == "__main__":
    unittest.main()



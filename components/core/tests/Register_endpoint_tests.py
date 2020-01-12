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

correct_username="username"
correct_password="password123"     
correct_email="email@gmail.com"
incorrect_username="admin"
incorrect_password="admin"
correct_string="user_name="+correct_username+"&password="+correct_password+"&email="+correct_email
correctlogin="user_name="+"rand"+"&password="+"pass"
incorrect_string="user_name="+incorrect_username+"&password="+incorrect_password
payload = {''}
token = ''
class TestFlaskAPIUsingRequests(unittest.TestCase):
    def test_api_login_returns_auth_level(self):
        resp = requests.post('http://localhost:5000/api/login',correctlogin,headers=headers)
        self.assertEqual(resp.json(),{u'auth': u'0'})
        token = resp.headers['token']
        print(token)
    def test_api_add_user(self):
        resp = requests.post('http://localhost:5000/api/user',correct_string,headers={'Content-Type':'application/x-www-form-urlencoded','token':token})
        self.assertEqual(resp.status_code,200)
        
    # def test_api_login_incorrectly_return_403(self):
    #     resp = requests.post('http://localhost:5000/api/login',incorrect_string,headers=headers)
    #     self.assertEqual(resp.status_code,403)
if __name__ == "__main__":
    unittest.main()

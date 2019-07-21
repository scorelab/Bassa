import unittest
import requests

headers = {
'Host': 'localhost:5000',
'Accept': 'application/json, text/plain, */*',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate',
'Content-Type': 'application/x-www-form-urlencoded',
'Origin': 'http://localhost:3000'
}

correct_username="rand"
correct_password="pass"
incorrect_username="admin"
incorrect_password="admin"
correct_string="user_name="+correct_username+"&password="+correct_password
incorrect_string="user_name="+incorrect_username+"&password="+incorrect_password
payload = {''}

correct_grantee_name="rush"
correct_access="write"
incorrect_grantee_name="admin"
incorrect_access="admin"
correct_acl_string="user_name"+correct_grantee_name+"&access"+correct_access
incorrect_acl_string="user_name"+incorrect_grantee_name+"&access"+incorrect_access
entity_id = '1'
user_id = '2'
correct_params = {'type': 'fr'}
incorrect_params = {'type': 'fo'}

class TestFlaskAPIUsingRequests(unittest.TestCase):

    def test_api_login_returns_auth_level(self):
        resp = requests.post('http://localhost:5000/api/login', correct_string, headers=headers)
        self.assertEqual(resp.json(),{u'auth': u'0'})

    def test_api_login_incorrectly_return_403(self):
        resp = requests.post('http://localhost:5000/api/login', incorrect_string, headers=headers)
        self.assertEqual(resp.status_code,403)

    def test_api_acl_check_access_pass(self):
        resp = requests.get('http://localhost:5000/api/user/drive/'+entity_id+'/check/'+user_id, params=correct_params, headers=headers)
        self.assertEqual(resp.json(),[[u'write']])

    def test_api_acl_check_access_fail(self):
        resp = requests.get('http://localhost:5000/api/user/drive/'+entity_id+'/check/'+user_id, params=incorrect_params, headers=headers)
        self.assertEqual(resp.status_code,400)

    def test_api_acl_grant_access_pass(self):
        resp = requests.post('http://localhost:5000/api/user/drive/'+entity_id+'/grant', correct_acl_string, params=correct_params, headers=headers)
        self.assertEqual(resp.json(),{u'status': u'success'})

    def test_api_acl_grant_access_fail(self):
        resp = requests.post('http://localhost:5000/api/user/drive/'+entity_id+'/grant', incorrect_acl_string, params=incorrect_params, headers=headers)
        self.assertEqual(resp.status_code,400)

if __name__ == "__main__":
    unittest.main()

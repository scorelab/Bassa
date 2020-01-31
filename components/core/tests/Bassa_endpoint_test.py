import unittest
import requests

import testing.mysqld
# Generate MYSQLD class which shares the generated database
MYSQLD = testing.mysqld.MysqldFactory(cache_initialized_db=True)

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
class TestFlaskAPIUsingRequests(unittest.TestCase):
    def setUp(self):
        # Use the generated MYSQLD class instead of testing.mysqld
        self.mysqld = MYSQLD()

    def tearDown(self):
        self.mysqld.stop()
    
    def tearDownModule(self):
        # clear cached database at end of tests
        MYSQLD.clear_cache()
        
    def test_api_login_returns_auth_level(self):
        resp = requests.post('http://localhost:5000/api/login',correct_string,headers=headers)
        self.assertEqual(resp.json(),{u'auth': u'0'})
    def test_api_login_incorrectly_return_403(self):
        resp = requests.post('http://localhost:5000/api/login',incorrect_string,headers=headers)
        self.assertEqual(resp.status_code,403)
if __name__ == "__main__":
    unittest.main()

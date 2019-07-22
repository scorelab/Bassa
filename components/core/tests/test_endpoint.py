import unittest
import requests
import pytest

headers = {
'Host': 'localhost:5000',
'Accept': 'application/json, text/plain, */*',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate',
'Content-Type': 'application/x-www-form-urlencoded',
'Origin': 'http://localhost:3000',
'token': 'random_token_value'
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
folder_name="child_folder"
file_name="child_file"
edit_folder_name="test_folder"
edit_file_name="test_file"
move_folder_parent_name="init_folder"
move_file_parent_name="test_folder"
incorrect_grantee_name="admin"
incorrect_access="admin"

fr_entity_id = '1'
fl_entity_id = '2'
fr_edit_id = '2'
fl_edit_id = '2'
fr_rem_id = '3'
fl_rem_id = '3'
fr_move_id = '2'
fl_move_id = '2'
user_id = '2'
parent_id = '1'

correct_acl_string="user_name="+correct_grantee_name+"&access="+correct_access
incorrect_acl_string="user_name="+incorrect_grantee_name+"&access="+incorrect_access
add_folder_string="name="+folder_name+"&parent_id="+parent_id
add_file_string="name="+file_name+"&parent_id="+parent_id
edit_folder_string="name="+edit_folder_name
edit_file_string="name="+edit_file_name
move_folder_string="parent_name="+move_folder_parent_name
move_file_string="parent_name="+move_file_parent_name

correct_params = {'type': 'fr'}
incorrect_params = {'type': 'folder'}
correct_params_file = {'type': 'fl'}
incorrect_params_file = {'type': 'file'}


class TestFlaskAPIUsingRequests(unittest.TestCase):

    @pytest.mark.run(order=1)
    def test_api_login_returns_auth_level(self):
        resp = requests.post('http://localhost:5000/api/login', correct_string, headers=headers)
        self.assertEqual(resp.json(), {'auth':'0'})

    @pytest.mark.run(order=2)
    def test_api_login_incorrectly_return_403(self):
        resp = requests.post('http://localhost:5000/api/login', incorrect_string, headers=headers)
        self.assertEqual(resp.status_code, 403)

    @pytest.mark.run(order=3)
    def test_api_acl_check_access_pass(self):
        resp = requests.get('http://localhost:5000/api/user/drive/'+fr_entity_id+'/check/'+user_id, params=correct_params, headers=headers)
        self.assertEqual(resp.json(),[['write']])

    @pytest.mark.run(order=4)
    def test_api_acl_check_access_fail(self):
        resp = requests.get('http://localhost:5000/api/user/drive/'+fr_entity_id+'/check/'+user_id, params=incorrect_params, headers=headers)
        self.assertEqual(resp.status_code, 400)

    @pytest.mark.run(order=5)
    def test_api_acl_grant_access_pass(self):
        resp = requests.post('http://localhost:5000/api/user/drive/'+fr_entity_id+'/grant', correct_acl_string, params=correct_params, headers=headers)
        self.assertEqual(resp.json(), {'status':'success'})

    @pytest.mark.run(order=6)
    def test_api_acl_grant_access_fail(self):
        resp = requests.post('http://localhost:5000/api/user/drive/'+fr_entity_id+'/grant', incorrect_acl_string, params=incorrect_params, headers=headers)
        self.assertEqual(resp.status_code, 400)

    @pytest.mark.run(order=7)
    def test_api_directory_fetch_entity_folder_pass(self):
        resp = requests.get('http://localhost:5000/api/user/drive/'+fr_entity_id, params=correct_params, headers=headers)
        self.assertEqual(resp.json(), [[1, 'init_folder']])

    @pytest.mark.run(order=8)
    def test_api_directory_fetch_entity_folder_fail(self):
        resp = requests.get('http://localhost:5000/api/user/drive/'+fr_entity_id, params=incorrect_params, headers=headers)
        self.assertEqual(resp.status_code, 400)

    @pytest.mark.run(order=9)
    def test_api_directory_fetch_entity_file_pass(self):
        resp = requests.get('http://localhost:5000/api/user/drive/'+fl_entity_id, params=correct_params_file, headers=headers)
        self.assertEqual(resp.json(), [[2, 'test_file']])

    @pytest.mark.run(order=10)
    def test_api_directory_fetch_entity_file_fail(self):
        resp = requests.get('http://localhost:5000/api/user/drive/'+fl_entity_id, params=incorrect_params_file, headers=headers)
        self.assertEqual(resp.status_code, 400)

    @pytest.mark.run(order=11)
    def test_api_directory_add_entity_folder_pass(self):
        resp = requests.post('http://localhost:5000/api/user/drive/'+user_id+'/add', add_folder_string, params=correct_params, headers=headers)
        self.assertEqual(resp.json(), {'status':'success'})

    @pytest.mark.run(order=12)
    def test_api_directory_add_entity_folder_fail(self):
        resp = requests.post('http://localhost:5000/api/user/drive/'+user_id+'/add', add_folder_string, params=incorrect_params, headers=headers)
        self.assertEqual(resp.status_code, 400)

    @pytest.mark.run(order=13)
    def test_api_directory_add_entity_file_pass(self):
        resp = requests.post('http://localhost:5000/api/user/drive/'+user_id+'/add', add_file_string, params=correct_params_file, headers=headers)
        self.assertEqual(resp.json(), {'status':'success'})

    @pytest.mark.run(order=14)
    def test_api_directory_add_entity_file_fail(self):
        resp = requests.post('http://localhost:5000/api/user/drive/'+user_id+'/add', add_file_string, params=incorrect_params_file, headers=headers)
        self.assertEqual(resp.status_code, 400)

    @pytest.mark.run(order=15)
    def test_api_directory_edit_entity_folder_pass(self):
        resp = requests.put('http://localhost:5000/api/user/drive/'+fr_edit_id+'/edit', edit_folder_string, params=correct_params, headers=headers)
        self.assertEqual(resp.json(), {'status':'success'})

    @pytest.mark.run(order=16)
    def test_api_directory_edit_entity_folder_fail(self):
        resp = requests.put('http://localhost:5000/api/user/drive/'+fr_edit_id+'/edit', edit_folder_string, params=incorrect_params, headers=headers)
        self.assertEqual(resp.status_code, 400)

    @pytest.mark.run(order=17)
    def test_api_directory_edit_entity_file_pass(self):
        resp = requests.put('http://localhost:5000/api/user/drive/'+fl_edit_id+'/edit', edit_file_string, params=correct_params_file, headers=headers)
        self.assertEqual(resp.json(), {'status':'success'})

    @pytest.mark.run(order=18)
    def test_api_directory_edit_entity_file_fail(self):
        resp = requests.put('http://localhost:5000/api/user/drive/'+fl_edit_id+'/edit', edit_file_string, params=incorrect_params_file, headers=headers)
        self.assertEqual(resp.status_code, 400)

    @pytest.mark.run(order=19)
    def test_api_directory_remove_entity_folder_pass(self):
        resp = requests.delete('http://localhost:5000/api/user/drive/'+fr_rem_id+'/remove', params=correct_params, headers=headers)
        self.assertEqual(resp.json(), {'status':'success'})

    @pytest.mark.run(order=20)
    def test_api_directory_remove_entity_folder_fail(self):
        resp = requests.delete('http://localhost:5000/api/user/drive/'+fr_rem_id+'/remove', params=incorrect_params, headers=headers)
        self.assertEqual(resp.status_code, 400)

    @pytest.mark.run(order=21)
    def test_api_directory_remove_entity_file_pass(self):
        resp = requests.delete('http://localhost:5000/api/user/drive/'+fl_rem_id+'/remove', params=correct_params_file, headers=headers)
        self.assertEqual(resp.json(), {'status':'success'})

    @pytest.mark.run(order=22)
    def test_api_directory_remove_entity_file_fail(self):
        resp = requests.delete('http://localhost:5000/api/user/drive/'+fl_rem_id+'/remove', params=incorrect_params_file, headers=headers)
        self.assertEqual(resp.status_code, 400)

    @pytest.mark.run(order=23)
    def test_api_directory_move_entity_folder_pass(self):
        resp = requests.post('http://localhost:5000/api/user/drive/'+fr_move_id+'/move', move_folder_string, params=correct_params, headers=headers)
        self.assertEqual(resp.json(), {'status':'success'})

    @pytest.mark.run(order=24)
    def test_api_directory_move_entity_folder_fail(self):
        resp = requests.post('http://localhost:5000/api/user/drive/'+fr_move_id+'/move', move_folder_string, params=incorrect_params, headers=headers)
        self.assertEqual(resp.status_code, 400)

    @pytest.mark.run(order=25)
    def test_api_directory_move_entity_file_pass(self):
        resp = requests.post('http://localhost:5000/api/user/drive/'+fl_move_id+'/move', move_file_string, params=correct_params_file, headers=headers)
        self.assertEqual(resp.json(), {'status':'success'})

    @pytest.mark.run(order=26)
    def test_api_directory_move_entity_file_fail(self):
        resp = requests.post('http://localhost:5000/api/user/drive/'+fl_move_id+'/move', move_file_string, params=incorrect_params_file, headers=headers)
        self.assertEqual(resp.status_code, 400)


if __name__ == "__main__":
    unittest.main()

from UserManager import * 
import unittest
username = "admin"
password = "admin"
usernamer = "rand"
passwordr = "pass"
class Test(unittest.TestCase):
 def test_Incorrect_Login(self):
    self.assertEqual(False, user_login(username, password))
 def test_Correct_Login(self):
    self.assertEqual(True, user_login(usernamer, passwordr))
 def test_Incorrect_check_approved(self):
    self.assertEqual(False, check_approved(username, password))
 def test_Correct_check_approved(self):
    self.assertEqual(True, check_approved(usernamer, passwordr))
unittest.main()  

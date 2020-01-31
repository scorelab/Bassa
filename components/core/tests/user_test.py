# !/usr/bin/python
# -*- coding: utf-8 -*-
from UserManager import *
import unittest
import Models


import unittest
import testing.mysqld

# Generate MYSQLD class which shares the generated database
MYSQLD = testing.mysqld.MysqldFactory(cache_initialized_db=True)


class User:
    def __init__(self, userName, email, password, auth):
        self.userName = userName
        self.email = email
        self.password = password
        self.auth = auth

    def userName(self):
        return self.userName

    def password(self):
        return self.password

    def email(self):
        return self.email

    def auth(self):
        return self.auth


class Test(unittest.TestCase):
    def setUp(self):
        # Use the generated MYSQLD class instead of testing.mysqld
        self.mysqld = MYSQLD()

    def tearDown(self):
        self.mysqld.stop()
    
    def tearDownModule(self):
        # clear cached database at end of tests
        MYSQLD.clear_cache()

    def test_check_existing_username(self):
        self.assertEqual(True, check_user_name('rand'))

    def test_correct_register(self):
        self.assertEqual("success", add_user(user=User('normal_user', 'emailnormal@email.com', '12345678', '0')))

    def test_get_user(self):
        self.assertIsInstance(get_user('normal_user'), Models.User)

    def test_incorrect_regular_register_before_regular_user_register(self):
        self.assertEqual("username taken",
                         add_regular_user(user=User('normal_user', 'emailnormal@email.com', '12345678', '0')))

    def test_correct_regular_user_register(self):
        self.assertEqual("success", add_regular_user(user=User('reg', 'emailregular@email.com', '12345678', '0')))

    def test_incorrect_regular_register_after_regular_user_register(self):
        self.assertEqual("username taken",
                         add_regular_user(user=User('reg', 'emailregular@email.com', '12345678', '0')))

    def test_update_user(self):
        self.assertEqual("success", update_user(user=User('updated_user', 'emailnormal@email.com', '12345678', '0'),
                                                username="normal_user"))

    def test_remove_user(self):
        self.assertEqual("success", remove_user('updated_user'))

    def test_remove_regular_user(self):
        self.assertEqual("success", remove_user('reg'))


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python
# -*- coding: utf-8 -*-
from UserManager import *
import unittest

import testing.mysqld
# Generate MYSQLD class which shares the generated database
MYSQLD = testing.mysqld.MysqldFactory(cache_initialized_db=True)


def username():
    return 'admin'


def password():
    return 'admin'


def usernamer():
    return 'rand'


def passwordr():
    return 'pass'


class Test(unittest.TestCase):
    def setUp(self):
        # Use the generated MYSQLD class instead of testing.mysqld
        self.mysqld = MYSQLD()

    def tearDown(self):
        self.mysqld.stop()
    
    def tearDownModule(self):
        # clear cached database at end of tests
        MYSQLD.clear_cache()

    def test_incorrect_login(self):
        self.assertEqual(False, user_login(username(), password()))

    def test_correct_login(self):
        self.assertEqual(True, user_login(usernamer(), passwordr()))

    def test_incorrect_check_approved(self):
        self.assertEqual(False, check_approved(username(), password()))

    def test_correct_check_approved(self):
        self.assertEqual(True, check_approved(usernamer(), passwordr()))


if __name__ == "__main__":
    unittest.main()

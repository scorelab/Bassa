#!/usr/bin/python
# -*- coding: utf-8 -*-
from UserManager import *
import unittest


def username():
    return 'admin'


def password():
    return 'admin'


def usernamer():
    return 'rand'


def passwordr():
    return 'pass'


class Test(unittest.TestCase):

    def test_incorrect_login(self):
        self.assertEqual(False, user_login(username(), password()))

    def test_correct_login(self):
        self.assertEqual(True, user_login(usernamer(), passwordr()))

    def test_incorrect_check_approved(self):
        self.assertEqual(False, check_approved(username(), password()))

    def test_correct_check_approved(self):
        self.assertEqual(True, check_approved(usernamer(), passwordr()))


unittest.main()

#!/usr/bin/python
# -*- coding: utf-8 -*-
from UserManager import *
import unittest


def username_short():
    return 'ad'

def username_long():
    return 'admin'

def wrong_email():
    return 'admin@gmail.'

def password_short():
    return '123456'

def auth():
    return 0

def usernamer():
    return 'username'

def emailr():
    return 'email@email.com'

def passwordr():
    return '12345678'


class Test(unittest.TestCase):

    def test_incorrect_register_short_username(self):
        self.assertEqual("db connection error", add_user(username_short(),passwordr(),auth(),emailr()))

    def test_incorrect_register_long_username(self):
        self.assertEqual("db connection error", add_user(username_long(), passwordr(),auth(),emailr()))

    def test_incorrect_register_wrong_email(self):
        self.assertEqual("db connection error", add_user(usernamer(), passwordr(),auth(),wrong_email()))

    def test_incorrect_register_password_short(self):
        self.assertEqual("db connection error", add_user(username(), password(),auth(),emailr()))

    def test_correct_register(self):
        self.assertEqual("success", add_user(usernamer(), passwordr(),auth(),emailr()))

    def test_correct_register(self):
        self.assertEqual("username taken", add_regular_user(usernamer(), passwordr(),auth(),emailr())

if __name__ == "__main__":
    unittest.main()

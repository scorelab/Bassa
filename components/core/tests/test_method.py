#!/usr/bin/python
# -*- coding: utf-8 -*-

from managers.UserManager import *
from managers.AclManager import *
from managers.DirectoryManager import *
from utils.test_method_utils import *

import unittest


class Test(unittest.TestCase):

    def test_incorrect_login(self):
        self.assertEqual(False, user_login(username(), password()))

    def test_correct_login(self):
        self.assertEqual(True, user_login(usernamer(), passwordr()))

    def test_incorrect_check_approved(self):
        self.assertEqual(False, check_approved(username(), password()))

    def test_correct_check_approved(self):
        self.assertEqual(True, check_approved(usernamer(), passwordr()))

    def test_correct_give_access(self):
        response = give_access(access_id(), access_user(), folder(), access())
        self.assertEqual('success', response)

    def test_get_access(self):
        response = get_access(access_id(), user_id(), folder())
        self.assertEqual(True, isinstance(response[0][0], str))

    def test_create_folder(self):
        entity = folder_instance()
        response = entity.create(entity_name('add'), user_id(), parent_id())
        self.assertEqual('success', response)

    def test_create_file(self):
        entity = file_instance()
        response = entity.create(entity_name('add'), user_id(), parent_id())
        self.assertEqual('success', response)

    def test_update_folder(self):
        entity = folder_instance()
        response = entity.update(entity_name('edit'), entity_id())
        self.assertEqual('success', response)

    def test_update_file(self):
        entity = file_instance()
        response = entity.update(entity_name('edit'), entity_id())
        self.assertEqual('success', response)

    def test_get_folder(self):
        entity = folder_instance()
        response = entity.get(entity_id())
        self.assertEqual(True, isinstance(response[0][1], str))
        self.assertEqual(True, isinstance(response[0][0], int))

    def test_get_file(self):
        entity = file_instance()
        response = entity.get(entity_id())
        self.assertEqual(True, isinstance(response[0][1], str))
        self.assertEqual(True, isinstance(response[0][0], int))

    def test_delete_folder(self):
        entity= folder_instance()
        response = entity.delete(entity_id())
        self.assertEqual('success', response)

    def test_delete_file(self):
        entity= file_instance()
        response = entity.delete(entity_id())
        self.assertEqual('success', response)


if __name__ == "__main__":
    unittest.main()

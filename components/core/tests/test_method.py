#!/usr/bin/python
# -*- coding: utf-8 -*-

from managers.UserManager import *
from managers.AclManager import *
from managers.DirectoryManager import *
from utils.test_method_utils import *

import unittest
import pytest


class Test(unittest.TestCase):

    @pytest.mark.run(order=1)
    def test_incorrect_login(self):
        self.assertEqual(False, user_login(username(), password()))

    @pytest.mark.run(order=2)
    def test_correct_login(self):
        self.assertEqual(True, user_login(usernamer(), passwordr()))

    @pytest.mark.run(order=3)
    def test_incorrect_check_approved(self):
        self.assertEqual(False, check_approved(username(), password()))

    @pytest.mark.run(order=4)
    def test_correct_check_approved(self):
        self.assertEqual(True, check_approved(usernamer(), passwordr()))

    @pytest.mark.run(order=5)
    def test_correct_give_access(self):
        response = give_access(access_id(), access_user(), folder(), access())
        self.assertEqual('success', response)

    @pytest.mark.run(order=6)
    def test_get_access(self):
        response = get_access(access_id(), user_id(), folder())
        self.assertEqual(True, isinstance(response[0][0], str))

    @pytest.mark.run(order=7)
    def test_create_folder(self):
        entity = folder_instance()
        response = entity.create(entity_name('add'), user_id(), parent_id())
        self.assertEqual('success', response)

    @pytest.mark.run(order=8)
    def test_create_file(self):
        entity = file_instance()
        response = entity.create(entity_name('add'), user_id(), parent_id())
        self.assertEqual('success', response)

    @pytest.mark.run(order=9)
    def test_update_folder(self):
        entity = folder_instance()
        response = entity.update(entity_name('edit'), entity_id())
        self.assertEqual('success', response)

    @pytest.mark.run(order=10)
    def test_update_file(self):
        entity = file_instance()
        response = entity.update(entity_name('edit'), entity_id())
        self.assertEqual('success', response)

    @pytest.mark.run(order=11)
    def test_get_folder(self):
        entity = folder_instance()
        response = entity.get(entity_id())
        self.assertEqual(True, isinstance(response[0][1], str))
        self.assertEqual(True, isinstance(response[0][0], int))

    @pytest.mark.run(order=12)
    def test_get_file(self):
        entity = file_instance()
        response = entity.get(entity_id())
        self.assertEqual(True, isinstance(response[0][1], str))
        self.assertEqual(True, isinstance(response[0][0], int))

    @pytest.mark.run(order=13)
    def test_delete_folder(self):
        entity= folder_instance()
        response = entity.delete(user_id(), entity_name('remove'))
        self.assertEqual('success', response)

    @pytest.mark.run(order=14)
    def test_delete_file(self):
        entity= file_instance()
        response = entity.delete(user_id(), entity_name('remove'))
        self.assertEqual('success', response)


if __name__ == "__main__":
    unittest.main()

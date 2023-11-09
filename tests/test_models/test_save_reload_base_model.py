#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models import storage
"""Test Class for storage and BaseModel methods for
saving and reloading objects
"""


class TestSaveReload(unittest.TestCase):
    """
    Defines methods and attritutes of saving and reloading objects test class
    """

    def test_save(self):
        """
        tests method save of Storage class
        """

        my_obj = BaseModel()
        storage.save()
        my_obj_id = my_obj.id
        all_instances = storage.all()
        keys = ""
        for key in all_instances.keys():
            keys += key
        self.assertIn(my_obj_id, keys)

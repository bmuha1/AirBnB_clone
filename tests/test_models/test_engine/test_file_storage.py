#!/usr/bin/python3
""" Unittest for FileStorage class """
import unittest
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):
    """ FileStorage class """
    def test_all(self):
        """ type of dictionary """
        brba = FileStorage()
        storage.reload()
        self.assertEqual(type(brba.all()), dict)

    def test_new(self):
        """ new method """
        brba = FileStorage()
        storage.reload()
        brba.new(BaseModel())
        self.assertTrue(brba.all())

    def test_save(self):
        """ json file check """
        brba = FileStorage()
        storage.reload()
        brba.new(BaseModel())
        brba.save()
        self.assertTrue(os.path.isfile("file.json"))

    def test_reload(self):
        """ reload method """
        brba = FileStorage()
        storage.reload()
        my_model = BaseModel()
        key = "BaseModel" + "." + my_model.id
        brba.new(my_model)
        brba.save()
        brba.reload()
        self.assertTrue(brba.all()[key])

if __name__ == '__main__':
    unittest.main()

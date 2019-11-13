#!/usr/bin/python3
""" Test for BaseModel class """
import unittest
from datetime import datetime, date, time
import uuid
from models import storage
from models.base_model import BaseModel
import os
import time


class TestBaseModel(unittest.TestCase):
    """ Test for BaseModel class """

    def setUp(self):
        """ Move json file if it exists """
        if os.path.isfile("file.json"):
            os.rename("file.json", "file.json.temp")

    def tearDown(self):
        """ Delete test json file and put original file back """
        if os.path.isfile("file.json"):
            os.remove("file.json")
        if os.path.isfile("file.json.temp"):
            os.rename("file.json.temp", "file.json")

    def test_types1(self):
        """ name, number, class type test """
        brba = BaseModel()
        self.assertTrue(type(brba), BaseModel)
        brba.name = "Holberton"
        self.assertEqual(brba.name, "Holberton")
        self.assertTrue(type(brba.name), str)
        brba.my_number = 89
        self.assertEqual(brba.my_number, 89)
        self.assertTrue(type(brba.my_number), int)

    def test_types2(self):
        """ created_at, updated_at, id type test """
        brba = BaseModel()
        self.assertEqual(type(brba.id), str)
        self.assertEqual(type(brba.created_at), datetime)
        self.assertEqual(type(brba.updated_at), datetime)

    def test_default_attr(self):
        """ id, created_at, updated_at default attributes """
        brba = BaseModel()
        self.assertTrue(hasattr(brba, "id"))
        self.assertTrue(hasattr(brba, "created_at"))
        self.assertTrue(hasattr(brba, "updated_at"))

    def test_extra_attr(self):
        """ extra attributes """
        brba = BaseModel()
        brba.dicti = {"br": True}
        brba.bday = [2, 2, 1989]
        self.assertTrue(hasattr(brba, "dicti"))
        self.assertEqual(type(brba.dicti), dict)
        self.assertTrue(hasattr(brba, "bday"))
        self.assertEqual(type(brba.bday), list)

    def test_different_id(self):
        """ id should be different """
        brba1 = BaseModel()
        brba2 = BaseModel()
        self.assertNotEqual(brba1.id, brba2.id)
        self.assertEqual(len(brba1.id), len(brba2.id))

    def test_strMethod(self):
        """ check __str__ output """
        brba = BaseModel()
        my_str = "[BaseModel] ({}) {}".format(brba.id, brba.__dict__)
        self.assertEqual(my_str, str(brba))

    def test_save(self):
        """ save updated_at """
        brba = BaseModel()
        br = brba.updated_at
        time.sleep(0.1)
        brba.save()
        ba = brba.updated_at
        self.assertNotEqual(br, ba)

    def test_to_dict(self):
        """ dictionary conversion """
        brba = BaseModel()
        brba.name = "Banu"
        brba.my_number = 89
        dicti = brba.to_dict()
        my_keys = ["id",
                   "name",
                   "my_number",
                   "created_at",
                   "updated_at",
                   "__class__"]
        self.assertEqual(dicti["name"], "Banu")
        self.assertEqual(dicti["my_number"], 89)
        self.assertEqual(dicti["__class__"], "BaseModel")
        self.assertCountEqual(dicti.keys(), my_keys)

    def test_to_dict_attr(self):
        """ created_at, updated_at values """
        brba = BaseModel()
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        dicti = brba.to_dict()
        self.assertEqual(dicti["created_at"],
                         brba.created_at.strftime(time_format))
        self.assertEqual(dicti["updated_at"],
                         brba.updated_at.strftime(time_format))
        self.assertEqual(dicti["__class__"], "BaseModel")
        self.assertEqual(type(dicti["created_at"]), str)
        self.assertEqual(type(dicti["updated_at"]), str)

    def test_kwargs_name_error(self):
        """ kwargs syntax """
        with self.assertRaises(NameError):
            brba = BaseModel(**brba)

    def test_kwargs_type_error(self):
        """ kwargs syntax """
        with self.assertRaises(TypeError):
            brba = BaseModel(**"brba")

    def test_kwargs_name_error(self):
        """ kwargs syntax """
        with self.assertRaises(NameError):
            brba = BaseModel(**{brba})

    def test_kwargs_name_error(self):
        """ kwargs syntax """
        with self.assertRaises(TypeError):
            brba = BaseModel(**{"brba"})

    def test_int_attributes(self):
        """ pass attributes to the class """
        brba = BaseModel(1, 2, 3, 4)
        self.assertTrue(hasattr(brba, "id"))
        self.assertTrue(hasattr(brba, "created_at"))
        self.assertTrue(hasattr(brba, "updated_at"))

    def test_attr_nan(self):
        """ nan attribute """
        brba = BaseModel(float("nan"))
        self.assertTrue(hasattr(brba, "id"))
        self.assertTrue(hasattr(brba, "created_at"))
        self.assertTrue(hasattr(brba, "updated_at"))

    def test_attr_inf(self):
        """ inf attribute """
        brba = BaseModel(float("inf"))
        self.assertTrue(hasattr(brba, "id"))
        self.assertTrue(hasattr(brba, "created_at"))
        self.assertTrue(hasattr(brba, "updated_at"))

    def test_attr_none(self):
        """ None attribute """
        brba = BaseModel(None)
        self.assertTrue(hasattr(brba, "id"))
        self.assertTrue(hasattr(brba, "created_at"))
        self.assertTrue(hasattr(brba, "updated_at"))

if __name__ == '__main__':
    unittest.main()

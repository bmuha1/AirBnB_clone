#!/usr/bin/python3
""" Unittest for FileStorage class """
import unittest
import os.path
import pep8
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """ FileStorage class """

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

    def test_pep8(self):
        """ Test pep8 """
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(
            ['tests/test_models/test_engine/test_file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_all(self):
        """ type of dictionary """
        brba = FileStorage()
        my_model = BaseModel()
        my_user = User()
        my_state = State()
        my_city = City()
        my_amenity = Amenity()
        my_place = Place()
        my_review = Review()
        storage.reload()
        self.assertEqual(type(brba.all()), dict)
        self.assertTrue("BaseModel" in str(brba.all()))
        self.assertTrue("User" in str(brba.all()))
        self.assertTrue("State" in str(brba.all()))
        self.assertTrue("City" in str(brba.all()))
        self.assertTrue("Amenity" in str(brba.all()))
        self.assertTrue("Place" in str(brba.all()))
        self.assertTrue("Review" in str(brba.all()))

    def test_new(self):
        """ new method """
        brba = FileStorage()
        my_model = BaseModel()
        my_user = User()
        my_state = State()
        my_city = City()
        my_amenity = Amenity()
        my_place = Place()
        my_review = Review()
        storage.reload()
        brba.new(BaseModel())
        self.assertTrue(brba.all())
        self.assertTrue("BaseModel" in str(brba.all()))
        self.assertTrue("User" in str(brba.all()))
        self.assertTrue("State" in str(brba.all()))
        self.assertTrue("City" in str(brba.all()))
        self.assertTrue("Amenity" in str(brba.all()))
        self.assertTrue("Place" in str(brba.all()))
        self.assertTrue("Review" in str(brba.all()))

    def test_save(self):
        """ json file check """
        brba = FileStorage()
        my_model = BaseModel()
        my_user = User()
        my_state = State()
        my_city = City()
        my_amenity = Amenity()
        my_place = Place()
        my_review = Review()
        storage.reload()
        brba.new(BaseModel())
        brba.save()
        self.assertTrue(os.path.isfile("file.json"))
        self.assertTrue("BaseModel" in str(brba.all()))
        self.assertTrue("User" in str(brba.all()))
        self.assertTrue("State" in str(brba.all()))
        self.assertTrue("City" in str(brba.all()))
        self.assertTrue("Amenity" in str(brba.all()))
        self.assertTrue("Place" in str(brba.all()))
        self.assertTrue("Review" in str(brba.all()))

    def test_reload(self):
        """ reload method """
        brba = FileStorage()
        my_model = BaseModel()
        my_user = User()
        my_state = State()
        my_city = City()
        my_amenity = Amenity()
        my_place = Place()
        my_review = Review()
        storage.reload()
        key = "BaseModel" + "." + my_model.id
        brba.new(my_model)
        brba.save()
        brba.reload()
        self.assertTrue(brba.all()[key])
        self.assertTrue("BaseModel" in str(brba.all()))
        self.assertTrue("User" in str(brba.all()))
        self.assertTrue("State" in str(brba.all()))
        self.assertTrue("City" in str(brba.all()))
        self.assertTrue("Amenity" in str(brba.all()))
        self.assertTrue("Place" in str(brba.all()))
        self.assertTrue("Review" in str(brba.all()))

if __name__ == '__main__':
    unittest.main()

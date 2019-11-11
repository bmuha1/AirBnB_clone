#!/usr/bin/python3
"""
Define a FileStorage class.
"""
import json
import os.path
from datetime import datetime, date, time
from models.base_model import BaseModel


class FileStorage:
    """Define a FileStorage class."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        with open(self.__file_path, 'w') as f:
            new_dict = {key: obj.to_dict() for key, obj in
                        self.__objects.items()}
            json.dump(new_dict, f)

    def reload(self):
        """Deserialize the JSON file to __objects."""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as f:
                for key, value in json.load(f).items():
                    self.__objects[key] = eval(key.split('.')[0])(**value)

#!/usr/bin/python3
"""
Define a FileStorage class.
"""
import json
import os.path


class FileStorage:
    """Define a FileStorage class."""
    __file_path = ""
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        # return self.__objects.__dict__
        return self.__dict__

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        self.__objects[__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        with open(self.__file_path, 'a+') as f:
            f.write(json.dumps(self.__objects))

    def reload(self):
        """Deserialize the JSON file to __objects."""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as f:
                self.__objects = json.loads(f.read())

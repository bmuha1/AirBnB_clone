#!/usr/bin/python3
"""
Define a BaseModel.
"""
import uuid
from datetime import datetime, date, time
from models.engine.file_storage import FileStorage
# import storage
from models.__init__ import storage

class BaseModel:
    """Define a BaseModel class."""

    def __init__(self, *args, **kwargs):
        """Initialize a BaseModel instance."""
        if (kwargs):
            for key, value in kwargs.items():
                if (key == 'created_at' or key == 'updated_at'):
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if (key == '__class__'):
                    value = eval(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Print the BaseModel attributes."""
        return ('[' + str(type(self).__name__) + '] (' + str(self.id) +
                ') ' + str(self.__dict__))

    def save(self):
        """Update the attribute 'updated_at' with the current datetime."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return a dictionary containing keys/values of __dict__."""
        self.__dict__.update({'__class__' : str(type(self).__name__)})
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        return self.__dict__

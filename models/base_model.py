#!/usr/bin/python3
"""
Define a BaseModel.
"""
import uuid
from datetime import datetime, date, time
import models


class BaseModel:
    """Define a BaseModel class."""

    def __init__(self, *args, **kwargs):
        """Initialize a BaseModel instance."""
        if (kwargs):
            for key, value in kwargs.items():
                if (key == 'created_at' or key == 'updated_at'):
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if (key == '__class__'):
                    from models.user import User
                    value = eval(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Print the BaseModel attributes."""
        return ('[' + str(type(self).__name__) + '] (' + str(self.id) +
                ') ' + str(self.__dict__))

    def save(self):
        """Update the attribute 'updated_at' with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary containing keys/values of __dict__."""
        new_dict = self.__dict__.copy()
        new_dict.update({'__class__': str(type(self).__name__)})
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict

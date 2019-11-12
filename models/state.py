#!/usr/bin/python3
""" State class """
from models.base_model import BaseModel


class State(BaseModel):
    """State class that inherits from BaseModel"""
    def __init__(self, *args, **kwargs):
        """ __init__ method """
        self.name = ""
        super().__init__(**kwargs)

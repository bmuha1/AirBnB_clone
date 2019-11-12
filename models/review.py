#!/usr/bin/python3
""" Review class """

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from BaseModel"""
    def __init__(self, *args, **kwargs):
        """ __init__ method """
        self. place_id = ""
        self.user_id = ""
        self.text = ""
        super().__init__(**kwargs)

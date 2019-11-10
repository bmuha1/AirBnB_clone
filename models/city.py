#!/usr/bin/python3
""" City class """
from models.base_model import BaseModel


class City(BaseModel):
    """City class that inherits from BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initialize City."""
        self.state_id = ""
        self.name = ""
        super().__init__(**kwargs)

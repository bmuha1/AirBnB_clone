#!/usr/bin/python3
""" Amenity class """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class that inherits from BaseModel."""

    def __init__(self, *args, **kwargs):
        """Initialize Amenity."""
        self.name = ""
        super().__init__(**kwargs)

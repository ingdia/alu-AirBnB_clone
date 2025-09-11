#!/usr/bin/python3
"""
BaseModel module for the AirBnB clone project.
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel that defines common attributes/methods for all classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.
        If kwargs is provided, recreate instance from dictionary.
        Otherwise, create new one with unique id and current timestamps.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ("created_at", "updated_at"):
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Return string representation"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update updated_at with current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return dict representation with ISO datetime"""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict

#!/usr/bin/python3
"""
BaseModel module for the AirBnB clone project.

Defines the BaseModel class which all other classes will inherit from.
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel that defines common attributes/methods for all classes.
    """

    def __init__(self):
        """
        Initializes a new instance of BaseModel.
        - id: unique string (UUID4)
        - created_at: datetime of creation
        - updated_at: datetime of last update
        """
        self.id = str(uuid.uuid4())  # generate unique id
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns string representation of the instance:
        [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the public instance attribute updated_at with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the instance:
        - adds '__class__' key with class name
        - converts datetime attributes to ISO 8601 string
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict

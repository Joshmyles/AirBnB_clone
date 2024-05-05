#!/usr/bin/python3

"""
Basemodel does initialiazation, serialization & deserialization of instances.
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """ BaseModel for all classes
    """
    def __init__(self, *args, **kwargs):
        """ Constructor """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    d_val = datetime.strptime(value, '5Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, d_val)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ String Representation """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ Save method, it updates the updated_at """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returns the dictionary representation of an instance """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

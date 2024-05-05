# models/engine/file_storage.py

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ Class for serializing & deserializing instances """
    CLASSES = {
        'BaseModel': BaseModel,
        'User': User,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
        }

    __file_path = "file.json"
    __objects = {}  # dictionary to store all objects by <class name>.id
    
    def __init__(self):
        """ Initialization """
        self._reloading = False

    def all(self):
        """ Returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """ Serializes __object to the JSON file """
        data = {}
        for key, value in self.__objects.items():
            data[key] = value.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(data, file)

    def reload(self):
        """ Deserialize JSON file to __objects """
        if self._reloading:
            return
        self._reloading = True
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    cls = self.CLASSES[class_name]
                    obj = cls(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"Error reloading objects: {e}")
        finally:
            self._reloading = False

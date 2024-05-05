# models/engine/file_storage.py

import json
from models.amenity import Amenity
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
    __objects = {} # dictionary to store all objects by <class name>.id

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
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    print(class_name, obj_id, value)
        except FileNotFoundError:
            pass

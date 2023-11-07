#!/usr/bin/python3
import json
from models.base_model import BaseModel

"""
File storage model responsible for serialization and deserialization
"""


class FileStorage:
    """
    file storage representation class
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns dictionary representation of an object
        """

        return FileStorage.__objects

    def new(self, obj):
        """
        sets object instances to __objects dictionary
        """

        obj_key = f"{type(obj).__name__}.{obj.id}"

        obj_value = BaseModel.to_dict(obj)

        FileStorage.__objects[obj_key] = obj_value

    def save(self):
        """
        Serialize an __object in a JSON file
        """

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """

        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                FileStorage.__objects = json.load(f)
        except:
            pass

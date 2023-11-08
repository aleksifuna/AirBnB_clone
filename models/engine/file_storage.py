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
        FileStorage.__objects[obj_key] = obj

    def save(self):
        """
        Serialize an __object in a JSON file
        """
        my_dict = {}
        for key, value in FileStorage.__objects.items():
            my_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """

        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                obj_dict = {k: BaseModel(**v) for k, v in obj_dict.items()}
                FileStorage.__objects = obj_dict
        except FileNotFoundError:
            pass
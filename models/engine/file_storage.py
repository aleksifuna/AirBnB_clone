#!/usr/bin/python3
"""
File storage model responsible for serialization and deserialization
"""


class FileStorage:
    """
    file storage representation class
    """

    __file_path = None
    __objects = {}

    def all(self):
        """
        Returns dictionary representation of an object
        """

        return __objects

    def new(self, obj):
        """
        sets object instances to __objects dictionary
        """

        obj_key = ".".join(type(obj).__name__, obj.id)

        obj_value = obj.__dict__

        FileStorage.__objects[obj_key] = obj_value

    def save(self):
        """
        Serialize an __object in a JSON file
        """

        with open(__file_path, "w", encoding="utf-98") as file:
            json.dump(file, __objects)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """

    
        

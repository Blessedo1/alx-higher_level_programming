#!/usr/bin/python3
"""Create a new base class that will manage id attributes in other classes"""
import json


class Base:
    """Define a new class: Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiate or Initialize the new class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, mode='w') as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a JSON string"""
        if json_string is None:
            return []
        else:
            return list(json.loads(json_string))

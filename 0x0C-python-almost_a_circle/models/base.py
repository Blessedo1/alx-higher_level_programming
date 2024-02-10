#!/usr/bin/python3
"""Create a new base class that will manage id attributes in other classes"""


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

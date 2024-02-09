#!/usr/bin/python3
"""Create a BaseGeometry class thata is inherited by class Rectangle"""


class BaseGeometry:
    """Define a class BaseGeometry"""

    def area(self):
        """raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function validates a value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """Define a class Rectangle"""

    def __init__(self, width, height):
        """Instantiate with default attributes for Rectangle class"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

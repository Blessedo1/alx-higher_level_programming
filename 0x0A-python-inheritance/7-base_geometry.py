#!/usr/bin/python3
"""Create a BaseGeometry Module"""


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

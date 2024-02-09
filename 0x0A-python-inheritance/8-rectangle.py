#!/usr/bin/python3
"""Create a BaseGeometry class that is inherited by class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Define a class Rectangle"""

    def __init__(self, width, height):
        """Instantiate with default attributes for Rectangle class"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

#!/usr/bin/python3
"""Create a BaseGeometry class that is inherited by class square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Define a class Square"""

    def __init__(self, size):
        """Instantiate with default attributes for square class"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size**2

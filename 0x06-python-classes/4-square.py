#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initializetion of a new Square.

        Args:
            size(int): The size of the new square.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Method for area of square"""

        self.squarearea = self.__size**2
        return self.squarearea

    @property
    def size(self):
        """Getter to retrieve the value of size"""

        return self.__size

    @size.setter
    def size(self, value):
        """Setter to set the value of size"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value



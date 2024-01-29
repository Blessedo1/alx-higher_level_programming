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
        """Setter to set the value of size

        Args:
            value(int): The new size of the square
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def my_print(self):
        """Method to print the square with a character"""

        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()

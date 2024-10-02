#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialization of a new Square.

        Args:
            size(int): The size of the new square.
            position(int, int): The position of the new square
        """

        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Getter to retrieve value of position"""

        return self.__position

    @position.setter
    def position(self, value):
        """Setter to set the value of position"""

        if not isinstance(position, tuple) or len(position) != 2:
            if (not isinstance(position[0], int) or
                not isinstance(position[1], int)):
                if position[0] < 0 or position[1] < 0:
                    raise TypeError(
                            "position must be a tuple of 2 positive integers"
                    )
        self.__position = value

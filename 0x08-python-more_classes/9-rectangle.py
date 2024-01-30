#!/usr/bin/python3
"""Define a class Rectangle"""


class Rectangle:
    """Represent a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle.

        Args:
            width(int): the width of the rectangle
            height(int): the height of the rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """retreive the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width of the rectangle.

        Args:
             value(int): value to be parsed into width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retreive the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the width of the rectangle.

        Args:
             value(int): value to be parsed into height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area of a rectangle"""
        area_of_rectangle = self.__width * self.__height
        return area_of_rectangle

    def perimeter(self):
        """perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        peri_of_rectangle = 2 * (self.__width + self.__height)
        return peri_of_rectangle

    def __str__(self):
        """print a representation character"""
        if self.__width == 0 or self.__height == 0:
            return ""
        result = ""
        for i in range(self.__height):
            for j in range(self.__width):
                result += str(self.print_symbol)
            if i < self.__height - 1:
                result += "\n"
        return result

    def __repr__(self):
        """official representation of the rectangle"""
        repre = "Rectangle({}, {})".format(self.__width, self.__height)
        return repre

    def __del__(self):
        """deconstructing the rectangle"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """new triangle instance with width == height == size"""
        return cls(size, size)

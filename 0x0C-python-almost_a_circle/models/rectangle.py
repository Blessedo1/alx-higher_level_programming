#!/usr/bin/python3
"""Create a class Rectangle that inherits from class Base"""
from models.base import Base


class Rectangle(Base):
    """Define a class Rectangle with getter and setter methods"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiate the Rectangle class object"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def tweak_width(self):
        """retrieve the width of the rectangle"""
        return self.__width

    @property
    def tweak_height(self):
        """retrieve the height of the rectangle"""
        return self.__height

    @property
    def tweak_x(self):
        """retrieve the x coordinate of the rectangle"""
        return self.__x

    @property
    def tweak_y(self):
        """retrieve the y coordinate of the rectangle"""
        return self.__y

    @tweak_width.setter
    def tweak_width(self, value):
        """set the width of the rectangle"""
        self.__width = value

    @tweak_height.setter
    def tweak_height(self, value):
        """set the height of the rectangle"""
        self.__height = value

    @tweak_x.setter
    def tweak_x(self, value):
        """set the x coordinates of the rectangle"""
        self.__x = value

    @tweak_y.setter
    def tweak_y(self, value):
        """set the y coordinates of the rectangle"""
        self.__y = value

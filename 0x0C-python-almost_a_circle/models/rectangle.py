#!/usr/bin/python3
"""Create a class Rectangle that inherits from class Base"""
from models.base import Base


class Rectangle(Base):
    """Define a class Rectangle with methods"""


    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the Rectangle class object
        
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
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
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @tweak_height.setter
    def tweak_height(self, value):
        """set the height of the rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @tweak_x.setter
    def tweak_x(self, value):
        """set the x coordinates of the rectangle"""
        if type(sel.__x) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @tweak_y.setter
    def tweak_y(self, value):
        """set the y coordinates of the rectangle"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.width * self.height

    def display(self):
        for y in range(self.y):
            print()
        for h in range(self.height):
            for x in range(self.x):
                print(" ", end='')
            for w in range(self.width):
                print("#", end='')
            print()

    def update(self, *args, **kwargs):
        if args and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]

        elif kwargs and len(kwargs) != 0:
            for i, j in kwargs.items():
                if i == 'width':
                    self.width = j
                if i == 'height':
                    self.height = j
                if i == 'x':
                    self.x = j
                if i == 'y':
                    self.y = j
                if i == 'id':
                    self.id = j

    def __str__(self):
        return f"[Rectangle] ({self.id})\
 {self.x}/{self.y} - {self.width}/{self.height}"

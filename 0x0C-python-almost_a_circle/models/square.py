#!/usr/bin/python3
"""Create a class square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Define a class square that inherits from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization of the class instance"""
        width = size
        height = size
        super().__init__(width, height, x, y, id)

    def __str__(self):
        """Return the print() and str() representation of a square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Get the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the square
        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            if len(args) >= 1:
                self.size = args[0]
            elif len(args) >= 2:
                self.size = args[1]
            elif len(args) >= 3:
                self.size = args[2]
            elif len(args) >= 4:
                self.size = args[3]

        elif kwargs and len(kwargs) != 0:
            for i, j in kwargs.items():
                if i == 'size':
                    self.width = j
                elif i == 'x':
                    self.x = j
                elif i == 'y':
                    self.y = j
                elif i == 'id':
                    self.id = j

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

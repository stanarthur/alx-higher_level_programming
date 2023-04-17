#!/usr/bin/python3
""" Starting a square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defining the square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializing the square class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Printing the square class by overloading __str__ method"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
    @property
    def size(self):
        """Getting the size of square"""
        return self.width

    @size.setter
    def size(self, value):
        """Setting the size of square"""
        self.width = value
        self.height = value

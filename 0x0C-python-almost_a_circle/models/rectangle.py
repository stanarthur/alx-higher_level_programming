#!/usr/bin/python3
"""Defining the rectangle class"""

from models.base import Base

class Rectangle(Base):
    """Intializing the Rectangle class that inherits from Base, with a given height width,x,y and id"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """The width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """The  width of the rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height of the rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """The x axis of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """The x axis of the rectangle"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """The y axis of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """The y axis of the rectangle"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
 
    def display(self):
        """Displaying the rectangle in stdout"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)
    def __str__(self):
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.x, self.y, self.width, self.height)

    def area(self):
        """Update-The area of the rectangle"""
        return self.width * self.height

#    def update(self, *args):
#        """Update-the public method that asssigns an argument to each attribute"""
#        if len(args) >= 1:
#            self.id = args[0]
#        if len(args) >= 2:
#            self.width = args[1]
#        if len(args) >= 3:
#            self.height = args[2]
#        if len(args) >= 4:
#            self.x = args[3]
#        if len(args) >= 5:
#            self.y = args[4]

    def update(self, *args, **kwargs):
        """Update: changing the prototype that assigns a key that hasvalue argument to attributes"""
        if args:
            for i in range(len(args)):
                """Intializing the count for non keyword arguments"""
                if i == 0:
                    if type(args[i]) is not int:
                        raise TypeError("id must be an integer")
                    self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                elif i == 2:
                    self.height = args[i]
                elif i == 3:
                    self.x = args[i]
                elif i == 4:
                    self.y = args[i]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) is not int:
                        raise TypeError("id must be an integer")
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value


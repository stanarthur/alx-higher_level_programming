#!/usr/bin/python3
"""Creating a base class"""

class Base:
    """Defining class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing a new instance of a class Base"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

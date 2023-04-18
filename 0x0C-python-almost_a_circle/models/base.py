#!/usr/bin/python3
"""Creating a base class"""

import json


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


	@staticmethod
    def to_json_string(list_dictionaries):
        """Returning json string representation of list of dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if (type(list_dictionaries) != list or
           not all(type(x) == dict for x in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)

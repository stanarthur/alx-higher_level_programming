#!/usr/bin/python3
""" Starting a square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defining square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializing square class"""
        super().__init__(size, size, x, y, id)

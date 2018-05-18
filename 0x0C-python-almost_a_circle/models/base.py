#!/usr/bin/python3
"""Defines Base class"""


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """__init__ method for Base class
        Args:
            id (int): id for object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

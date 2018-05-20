#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """__init__ method of Square class
        Args:
            size (int): size of square
            x (int): x-coordinate
            y (int): y-coordinate
            id (int): id of square object
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of square object"""
        return "[{}] ({:d}) {:d}/{:d} - {:d}".format(
            type(self).__name__, self.id, self.x, self.y, self.width)

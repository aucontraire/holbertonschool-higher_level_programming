#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """__init__ method of Rectangle class
        Args:
            id (int): id of rectangle object
            width (int): width of rectangle
            height (int): height of rectangle
            x (int): x-coordinate
            y (int): y-coordinate
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, width):
        self.__width = width

    @height.setter
    def height(self, height):
        self.__height = height

    @x.setter
    def x(self, x):
        self.__x = x

    @y.setter
    def y(self, y):
        self.__y = y

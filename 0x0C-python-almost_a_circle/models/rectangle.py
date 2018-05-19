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
        """Width setter
        Args:
            width (int): width of rectangle
        Raises:
            TypeError: if not an integer
            ValueError: if not greater than zero
        """

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """Height setter
        Args:
            height (int): height of rectangle
        Raises:
            TypeError: if not an integer
            ValueError: if not greater than zero
        """

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        """x-coordinate setter
        Args:
            x (int): x-coordinate of rectangle
        Raises:
            TypeError: if not an integer
            ValueError: if negative
        """

        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """y-coordinate setter
        Args:
            y (int): y-coordinate of rectangle
        Raises:
            TypeError: if not an integer
            ValueError: if negative
        """

        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Area of rectangle
        Returns:
            area of rectangle
        """
        return self.width * self.height

    def display(self):
        """Prints # representation of rectangle"""
        rows = self.height
        columns = self.width
        for _ in range(self.y):
            print()
        for r in range(rows):
            print(' ' * self.x, end='')
            for c in range(columns):
                print('#', end='')
            print()

    def __str__(self):
        """Returns string representation of rectangle object"""
        return "[{}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            type(self).__name__,
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args):
        """Update attributes
        0 - id attribute
        1 - width attribute
        2 - height attribute
        3 - x attribute
        4 - y attribute
        """
        for i, arg in enumerate(args):
            if i == 0:
                self.id = arg
            if i == 1:
                self.width = arg
            if i == 2:
                self.height = arg
            if i == 3:
                self.x = arg
            if i == 4:
                self.y = arg

#!/usr/bin/python3


class BaseGeometry:
    """BaseGeometry class with area method"""
    def area(self):
        """Area method not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer validator
        Args:
            name (str): name
            value (int): integer value
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 1
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 1:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """__init__ method
        Args:
            width (int): width integer must be greater than 0
            height (int): height integer must be greater than 0
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """string representation"""
        return "[{}] {:d}/{:d}".format(
            type(self).__name__, self.__width, self.__height)

    def area(self):
        """Area of rectangle"""
        return self.__width * self.__height


if __name__ == '__main__':
    r = Rectangle(3, 5)

    print(r)
    print(r.area())

#!/usr/bin/python3


class Square:
    """Square class."""

    def __init__(self, size=0):
        """__init__ method that sets the size of square.
        Args:
            size (int): size of Square

        """
        self.size = size

    def area(self):
        """Gets the area of the Square.

        Returns:
            Area of squre

        """
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """size setter  method that sets the size of square.
        Args:
            value (int): size of Square
        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.

        """
        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, square):
        """Implements equals"""
        return self.area() == square.area()

    def __ne__(self, square):
        """Implements not equal"""
        return self.area() != square.area()

    def __gt__(self, square):
        """Implements greater than"""
        return self.area() > square.area()

    def __ge__(self, square):
        """Implements greater or equal to"""
        return self.area() >= square.area()

    def __lt__(self, square):
        """Implements less than"""
        return self.area() < square.area()

    def __le__(self, square):
        """Implements less than or equal to"""
        return self.area() <= square.area()


if __name__ == '__main__':
    s_5 = Square(5)
    s_6 = Square(6)

    if s_5 < s_6:
        print("Square 5 < Square 6")
    if s_5 <= s_6:
        print("Square 5 <= Square 6")
    if s_5 == s_6:
        print("Square 5 == Square 6")
    if s_5 != s_6:
        print("Square 5 != Square 6")
    if s_5 > s_6:
        print("Square 5 > Square 6")
    if s_5 >= s_6:
        print("Square 5 >= Square 6")

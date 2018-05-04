#!/usr/bin/python3


class Square:
    """Square class."""

    def __init__(self, size=0, position=(0, 0)):
        """__init__ method that sets the size and position of square.
        Args:
            size (int): size of Square
            position (tuple): poisition of Square

        """
        self.size = size
        self.position = position

    def area(self):
        """Gets the area of the Square.

        Returns:
            Area of squre

        """
        return self.__size * self.__size

    @property
    def size(self):
        """gets size of square."""
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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """gets position of square."""
        return self.__position

    @position.setter
    def position(self, value):
        """position setter method that sets position of Square.
        Args:
            value (tuple): tuple of two positive integer coordinates
        Raises:
            TypeError: If `value` is not a tuple of two positive integers

        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def __str__(self):
        """Prints a # representation of square based on size."""
        sqr_str = ''
        if self.__size == 0:
            return sqr_str
        else:
            for i in range(self.__position[1]):
                sqr_str += '\n'
            for j in range(self.__size - 1):
                sqr_str += ' ' * self.__position[0] + '#' * self.__size + '\n'
            sqr_str += ' ' * self.__position[0] + '#' * self.__size
        return sqr_str

if __name__ == '__main__':
    my_square = Square(5, (0, 0))
    print(my_square)

    print("--")

    my_square = Square(5, (4, 1))
    print(my_square)

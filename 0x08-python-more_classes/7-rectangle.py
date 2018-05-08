#!/usr/bin/python3


class Rectangle:
    """Rectangle class.
    Attributes:
        number_of_instances (int): number of rectangle instances
        print_symbol (any type): char(s) to represent rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """__init__ method.
        Args:
            width (int): integer width
            height (int): integer height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """width: returns width
        Args:
            width (int): integer width
        Returns:
            rectangle width
        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than 0
        """
        return self.__width

    @property
    def height(self):
        """height: returns height
        Args:
            height (int): integer height
        Returns:
            rectangle height
        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than 0
        """
        return self.__height

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def __str__(self):
        """String representation (#) of rectangle.
        Returns:
            string rep of rectangle
        """
        string = ''
        if self.width == 0 or self.height == 0:
            return string
        for r in range(self.height - 1):
            for c in range(self.width):
                string += str(self.print_symbol)
            string += '\n'
        string += str(self.print_symbol) * self.width
        return string

    def __repr__(self):
        """String representation of Rectangle object"""
        return 'Rectangle({:d}, {:d})'.format(self.width, self.height)

    def __del__(self):
        """Delete method"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def area(self):
        """Returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return self.width * 2 + self.height * 2


if __name__ == '__main__':
    my_rectangle_1 = Rectangle(8, 4)
    print(my_rectangle_1)
    print("--")
    my_rectangle_1.print_symbol = "&"
    print(my_rectangle_1)
    print("--")

    my_rectangle_2 = Rectangle(2, 1)
    print(my_rectangle_2)
    print("--")
    Rectangle.print_symbol = "C"
    print(my_rectangle_2)
    print("--")

    my_rectangle_3 = Rectangle(7, 3)
    print(my_rectangle_3)

    print("--")

    my_rectangle_3.print_symbol = ["C", "is", "fun!"]
    print(my_rectangle_3)

    print("--")

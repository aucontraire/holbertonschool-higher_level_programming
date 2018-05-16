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
            raise TypeError("{:s} must be an integer".format(name))
        if value < 1:
            raise ValueError("{:s} must be greater than 0".format(name))


if __name__ == '__main__':
    bg = BaseGeometry()

    bg.integer_validator("my_int", 12)
    bg.integer_validator("width", 89)

    try:
        bg.integer_validator("name", "John")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        bg.integer_validator("age", 0)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        bg.integer_validator("distance", -4)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

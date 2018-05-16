#!/usr/bin/python3


class BaseGeometry:
    """BaseGeometry class with area method"""
    def area(self):
        """Area method not implemented"""
        raise Exception("area() is not implemented")


if __name__ == '__main__':
    bg = BaseGeometry()

    try:
        print(bg.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

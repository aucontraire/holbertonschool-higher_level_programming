#!/usr/bin/python3

""" add_integer

Adds two integers (a, b) and returns integer sum
Floats get converted to integers, all others raise TypeError
"""


def add_integer(a, b=98):
    """ add_integer - adds two integers (a, b)
    Returns: integer sum
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b


if __name__ == '__main__':
    print(add_integer(1, 2))
    print(add_integer(100, -2))
    print(add_integer(2))
    print(add_integer(100.3, -2))
    try:
        print(add_integer(4, "School"))
    except Exception as e:
        print(e)
    try:
        print(add_integer(None))
    except Exception as e:
        print(e)

    try:
        print(add_integer(1.99, 3.5))
    except Exception as e:
        print(e)

    try:
        print(add_integer(None))
    except Exception as e:
        print(e)

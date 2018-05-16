#!/usr/bin/python3


def inherits_from(obj, a_class):
    """Determines if the object is an instance of a class or inherited
    Args:
        obj (object): object
        a_class (class): class to compare to
    Returns:
        True if object is instance or inherited from class, False otherwise
    """
    if issubclass(type(obj), a_class):
        if type(obj) is not a_class:
            return True
    return False


if __name__ == '__main__':
    a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))
if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool.__name__))
if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object.__name__))

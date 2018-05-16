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

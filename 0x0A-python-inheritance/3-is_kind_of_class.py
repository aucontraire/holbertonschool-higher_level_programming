#!/usr/bin/python3


def is_kind_of_class(obj, a_class):
    """returns True if the object is exactly an instance of the specified class
    otherwise False
    Args:
        obj (obj): object
        a_class (class): a class to compare to
    """
    if isinstance(obj, a_class):
        return True
    return False


if __name__ == '__main__':
    a = 1
    if is_kind_of_class(a, int):
        print("{} comes from {}".format(a, int.__name__))
    if is_kind_of_class(a, float):
        print("{} comes from {}".format(a, float.__name__))
    if is_kind_of_class(a, object):
        print("{} comes from {}".format(a, object.__name__))

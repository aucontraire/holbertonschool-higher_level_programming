#!/usr/bin/python3


def add_attribute(obj, attr, value):
    """Adds a new attribute to an object if possible
    Args:
        obj (object): object
        attr: attribute
        value: value to set
    Raises:
        TypeError: if the attribute can't be set
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")

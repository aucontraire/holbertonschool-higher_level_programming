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
    try:
        setattr(obj, attr, value)
    except Exception:
        raise TypeError("can't add new attribute")


if __name__ == '__main__':
    class MyClass():
        pass

    mc = MyClass()
    add_attribute(mc, "name", "John")
    print(mc.name)

    try:
        a = "My String"
        add_attribute(a, "name", "Bob")
        print(a.name)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

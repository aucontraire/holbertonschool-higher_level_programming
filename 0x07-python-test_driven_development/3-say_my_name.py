#!/usr/bin/python3

""" say_my_name

Prints My name is `first_name` `last_name`
If either argument is not a string it raises TypeError
"""


def say_my_name(first_name, last_name=""):
    """ add_integer - prints first and last name

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print('My name is {:s} {:s}'.format(first_name, last_name))


if __name__ == '__main__':
    say_my_name("John", "Smith")
    say_my_name("Walter", "White")
    say_my_name("Bob")
    try:
        say_my_name("Bob", 12)
    except Exception as e:
        print(e)

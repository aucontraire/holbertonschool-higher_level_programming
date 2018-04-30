#!/usr/bin/python3


def safe_print_integer(value):
    try:
        print('{:d}'.format(value))
        return True
    except ValueError:
        return False
    except TypeError:
        return False

if __name__ == '__main__':
    value = 89
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = -89
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = "Holberton"
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

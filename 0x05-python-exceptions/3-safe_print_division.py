#!/usr/bin/python3


def safe_print_division(a, b):
    quotient = 0

    try:
        q = a / b
    except ZeroDivisionError:
        q = None
    except TypeError:
        q = None
    finally:
        print('Inside result: {}'.format(q))

    return q


if __name__ == '__main__':
    a = 12
    b = 2
    result = safe_print_division(a, b)
    print("{:d} / {:d} = {}".format(a, b, result))

    a = 12
    b = 0
    result = safe_print_division(a, b)
    print("{:d} / {:d} = {}".format(a, b, result))

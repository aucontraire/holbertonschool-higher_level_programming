#!/usr/bin/python3


def safe_print_division(a, b):
    quotient = 0

    try:
        quotient = a / b
    except ZeroDivisionError:
        quotient = None
    except TypeError:
        quotient = None
    finally:
        print('Inside result: {}'.format(quotient))

    return quotient


if __name__ == '__main__':
    a = 12
    b = 2
    result = safe_print_division(a, b)
    print("{:d} / {:d} = {}".format(a, b, result))

    a = 12
    b = 0
    result = safe_print_division(a, b)
    print("{:d} / {:d} = {}".format(a, b, result))

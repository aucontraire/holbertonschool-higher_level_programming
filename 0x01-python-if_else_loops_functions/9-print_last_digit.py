#!/usr/bin/python3


def print_last_digit(number):
    last_digit = 0
    if number >= 0:
        last_digit = number % 10
    else:
        last_digit = 10 - (number % 10)

    print('{:d}'.format(last_digit), end='')
    return last_digit


if __name__ == '__main__':
    print_last_digit(12345)

#!/usr/bin/python3
import random


def get_randn():
    return random.randint(-10000, 10000)


def get_last_digit(number):
    if number >= 0:
        return number % 10
    else:
        return -10 + (number % 10)


def print_last_digit(last_digit):
    print('Last digit of {:d} is {:d}'.format(number, last_digit), end=" ")
    if last_digit > 5:
        print('and is greater than 5')
    elif last_digit == 0:
        print('and is 0')
    elif last_digit < 6 and last_digit != 0:
        print('and is less than 6 and not 0')


if __name__ == '__main__':
    number = get_randn()
    last_digit = get_last_digit(number)
    print_last_digit(last_digit)

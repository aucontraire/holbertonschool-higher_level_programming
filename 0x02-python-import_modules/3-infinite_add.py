#!/usr/bin/python3
from sys import argv


if __name__ == '__main__':
    sum = 0

    for i, arg in enumerate(argv[1:]):
        sum += int(arg)

    print('{:d}'.format(sum))

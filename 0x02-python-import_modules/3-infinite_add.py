#!/usr/bin/python3


if __name__ == '__main__':
    from sys import argv

    sum = 0
    for i, arg in enumerate(argv[1:]):
        sum += int(arg)

    print('{:d}'.format(sum))

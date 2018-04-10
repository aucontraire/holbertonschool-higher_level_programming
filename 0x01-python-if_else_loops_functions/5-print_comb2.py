#!/usr/bin/python3


if __name__ == '__main__':
    for n in range(100):
        if n != 99:
            print('{:02d}'.format(n), end=', ')
        else:
            print('{:02d}'.format(n))

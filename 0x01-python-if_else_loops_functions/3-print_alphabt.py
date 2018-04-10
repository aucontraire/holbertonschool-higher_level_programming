#!/usr/bin/python3


def print_low_alpha_ex():
    for n in range(97, 123):
        if n != 101 and n != 113:
            print('{}'.format(chr(n)), end='')


if __name__ == '__main__':
    print_low_alpha_ex()

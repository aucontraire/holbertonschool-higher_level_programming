#!/usr/bin/python3


def print_low_alpha_ex():
    for c in 'abcdefghijklmnopqrstuvwxyz':
        if c != 'q' and c != 'e':
            print('{}'.format(c), end='')

if __name__ == '__main__':
    print_low_alpha_ex()

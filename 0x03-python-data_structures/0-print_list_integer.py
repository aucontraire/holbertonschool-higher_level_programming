#!/usr/bin/python3


def print_list_integer(my_list=[]):
    for n in my_list:
        print('{:d}'.format(n))


if __name__ == '__main__':
    my_list = [2, 4, 6, 8]
    print_list_integer(my_list)

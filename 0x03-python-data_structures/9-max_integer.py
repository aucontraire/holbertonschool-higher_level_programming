#!/usr/bin/python3


def max_integer(my_list=[]):
    max_int = 0
    if len(my_list) == 0:
        return None
    for i, n in enumerate(my_list):
        if i == 0 or n > max_int:
            max_int = n
    return max_int


if __name__ == '__main__':
    my_list = [1, 90, 2, 13, 34, 5, -13, 3]
    max_value = max_integer(my_list)
    print("Max: {}".format(max_value))

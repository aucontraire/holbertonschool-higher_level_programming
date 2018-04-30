#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    i = 0
    count = 0
    for i in range(x):
        try:
            print('{:d}'.format(my_list[i]), end='')
            count += 1
        except ValueError:
            pass
        except TypeError:
            pass

    print()
    return count

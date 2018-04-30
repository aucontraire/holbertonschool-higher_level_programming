#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    i = 0
    while True:
        try:
            print('{}'.format(my_list[i]), end='')
            i += 1
            if i == x:
                if i != 0:
                    print()
                return i
        except IndexError:
            if i != 0:
                print()
            return i


if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5]
    #my_list = []
    nb_print = safe_print_list(my_list, 2)
    print("nb_print: {:d}".format(nb_print))
    nb_print = safe_print_list(my_list, len(my_list))
    print("nb_print: {:d}".format(nb_print))
    nb_print = safe_print_list(my_list, len(my_list) + 2)
    print("nb_print: {:d}".format(nb_print))

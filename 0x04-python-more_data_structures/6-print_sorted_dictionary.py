#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    if a_dictionary is not None:
        sorted_keys = sorted(a_dictionary.keys())
        for k in sorted_keys:
            print("{:s}: {}".format(k, a_dictionary[k]))


if __name__ == '__main__':
    a_dictionary = {
        'language': "C",
        'Number': 89,
        'track':
        "Low level",
        'ids': [1, 2, 3]
    }
    print_sorted_dictionary(a_dictionary)

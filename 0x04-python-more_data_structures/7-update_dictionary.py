#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    if a_dictionary is not None:
        new_dict = a_dictionary
        new_dict[key] = value
        return new_dict

if __name__ == '__main__':
    print_s = __import__('6-print_sorted_dictionary').print_sorted_dictionary

    a_dictionary = {'language': "C", 'number': 89, 'track': "Low level"}
    new_dict = update_dictionary(a_dictionary, 'language', "Python")
    print_s(new_dict)
    print("--")
    print_s(a_dictionary)

    print("--")
    print("--")

    new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
    print_s(new_dict)
    print("--")
    print_s(a_dictionary)

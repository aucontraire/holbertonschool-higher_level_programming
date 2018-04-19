#!/usr/bin/python3


def roman_to_int(roman_string):
    rom_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev = 1001
    for c in roman_string:
        if rom_dict[c] > prev:
            total += rom_dict[c]
            total -= prev * 2
        else:
            total += rom_dict[c]
        prev = rom_dict[c]
    return total


if __name__ == '__main__':
    """ Roman to Integer test file
    """
    roman_to_int = __import__('12-roman_to_int').roman_to_int

    roman_number = "X"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "VII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "IX"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "LXXXVII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "DCCVII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "CM"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "XCIX"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

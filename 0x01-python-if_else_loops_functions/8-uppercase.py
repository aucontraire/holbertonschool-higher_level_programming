#!/usr/bin/python3


def uppercase(str):
    new_str = ''
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            new_str += chr(ord(c) - 32)
        else:
            new_str += c
    print('{}'.format(new_str))

#!/usr/bin/python3


def no_c(my_string):
    new_list = list(my_string)
    new_string = ''
    for char in new_list:
        if char != 'c' and char != 'C':
            new_string += char
    return new_string


if __name__ == '__main__':
    print(no_c("Holberton School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))

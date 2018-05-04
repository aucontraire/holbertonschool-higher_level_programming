#!/usr/bin/python3


def print_square(size):
    """Prints a square with # representing dimensions
    Arguments:
        size (int): size of square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size > 0:
        for i in range(size):
            print("#" * size)


if __name__ == '__main__':
    print_square(4)
    print("")
    print_square(10)
    print("")
    print_square(0)
    print("")
    print_square(1)
    print("")
    try:
        print_square(-1)
    except Exception as e:
        print(e)
    print("")

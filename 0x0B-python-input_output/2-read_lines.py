#!/usr/bin/python3


def read_lines(filename="", nb_lines=0):
    """Print out number of lines requested
    Args:
        filename (str): string of path to file
        nb_lines (int): number of lines

    """
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        nlines = len(lines)
        if nb_lines <= 0 or nb_lines >= nlines:
            for line in lines:
                print(line, end='')
        else:
            i = 0
            while i < nb_lines:
                print(lines[i], end='')
                i += 1


if __name__ == '__main__':
    print("1 line:")
    read_lines("my_file_0.txt", 1)
    print("--")
    print("3 lines:")
    read_lines("my_file_0.txt", 3)
    print("--")
    print("Full content:")
    read_lines("my_file_0.txt")

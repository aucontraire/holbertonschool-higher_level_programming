#!/usr/bin/python3


def write_file(filename="", text=""):
    """Write string to file
    Args:
        filename (str): string of path to file
        text (str): string to write to file
    Returns:
        number of characters written

    """
    chars_written = 0
    with open(filename, 'w', encoding='utf-8') as f:
        chars_written += f.write(text)
    return chars_written


if __name__ == '__main__':
    nb_characters = write_file(
        "my_first_file.txt", "Holberton School is so cool!\n")
    print(nb_characters)

#!/usr/bin/python3


def append_write(filename="", text=""):
    """Write string to file (append mode)
    Args:
        filename (str): string of path to file
        text (str): string to write to file
    Returns:
        number of characters written

    """
    chars_written = 0
    with open(filename, 'a', encoding='utf-8') as f:
        chars_written += f.write(text)
    return chars_written


if __name__ == '__main__':
    nb_characters_added = append_write(
        "file_append.txt", "Holberton School is so cool!\n")
    print(nb_characters_added)

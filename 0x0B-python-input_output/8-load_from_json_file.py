#!/usr/bin/python3
import json


def load_from_json_file(filename):
    """Creates a Python object from JSON file
    Args:
        filename (str): string of path to file
    Returns:
        Python object
    """
    data = None
    with open(filename, 'r', encoding='utf-8') as json_data:
        data = json.load(json_data)
    return data


if __name__ == '__main__':
    filename = "my_list.json"
    my_list = load_from_json_file(filename)
    print(my_list)
    print(type(my_list))

    filename = "my_dict.json"
    my_dict = load_from_json_file(filename)
    print(my_dict)
    print(type(my_dict))

    try:
        filename = "my_set_doesnt_exist.json"
        my_set = load_from_json_file(filename)
        print(my_set)
        print(type(my_set))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        filename = "my_fake.json"
        my_fake = load_from_json_file(filename)
        print(my_fake)
        print(type(my_fake))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

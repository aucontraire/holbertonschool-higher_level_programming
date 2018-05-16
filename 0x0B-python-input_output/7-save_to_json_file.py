#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    """Writes object in JSON representation to a file
    Args:
        my_obj (object): object to write
        filename (str): path to a file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))


if __name__ == '__main__':
    filename = "my_list.json"
    my_list = [1, 2, 3]
    save_to_json_file(my_list, filename)

    filename = "my_dict.json"
    my_dict = {
        'id': 12,
        'name': "John",
        'places': ["San Francisco", "Tokyo"],
        'is_active': True,
        'info': {
            'age': 36,
            'average': 3.14
        }
    }
    save_to_json_file(my_dict, filename)

    try:
        filename = "my_set.json"
        my_set = {132, 3}
        save_to_json_file(my_set, filename)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

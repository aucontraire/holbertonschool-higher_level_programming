#!/usr/bin/python3


def class_to_json(obj):
    """
    returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization of
    an object
    """
    return obj.__dict__


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """__init__ method
        Args:
            first_name (str): first name
            last_name (str): last name
            age (int): age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Serializes object to dictionary
        Args:
            attr (list): list of attributes to filter object dictionary
        Returns:
            object dictionary
        """
        obj_dict = class_to_json(self)
        if not attrs:
            return obj_dict
        else:
            filter_dict = {}
            for k, v in obj_dict.items():
                if k in attrs:
                    filter_dict[k] = v
            return filter_dict

    def reload_from_json(self, json):
        """Updates attributes through JSON file
        Args:
            json (dict): dictionary of JSON file
        """
        for k, v in json.items():
            if hasattr(self, k):
                setattr(self, k, v)

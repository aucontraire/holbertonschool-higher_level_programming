#!/usr/bin/python3


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
        obj_dict = self.__dict__
        if not attrs:
            return obj_dict
        else:
            filter_dict = {}
            for att in attrs:
                if hasattr(self, att):
                    filter_dict[att] = obj_dict[att]
            return filter_dict

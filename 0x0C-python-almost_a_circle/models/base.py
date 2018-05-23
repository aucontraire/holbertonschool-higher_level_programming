#!/usr/bin/python3
"""Defines Base class"""
import json


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """__init__ method for Base class
        Args:
            id (int): id for object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON string of object dictionary
        Args:
            list_dictionaries (list): list of dictionaries
        Returns:
            JSON string representation of list of dictionary
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file - saves objects to a JSON file
        Args:
            list_objs (list): list of objects
        """
        json_list = []
        json_string = '[]'
        if list_objs is not None:
            for obj in list_objs:
                json_list.append(obj.to_dictionary())

            if len(json_list) > 0:
                json_string = Base.to_json_string(json_list)

        with open(cls.__name__ + '.json', 'w') as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """from_json_string - creates list of the JSON string representation
        Args:
            json_string (str): JSON string of object
        Returns:
            list of JSON string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance with all attributes set
        Args:
            dictionary (dict): dictionary of attributes and values
        Returns:
            instance of an object initialized
        """
        obj = None
        if cls.__name__ == 'Rectangle':
            obj = cls(1, 1)
        elif cls.__name__ == 'Square':
            obj = cls(1)
        cls.update(obj, **dictionary)
        return obj

    @classmethod
    def reset(cls):
        """Reset __nb_objects back to zero"""
        cls.__nb_objects = 0

    @classmethod
    def load_from_file(cls):
        """load_from_file - creates a list of instances from JSON file
        Returns:
            list of instances
        """
        obj_list = []
        try:
            with open(cls.__name__ + '.json', 'r', encoding='utf-8') as f:
                list_output = cls.from_json_string(f.read())
                for obj in list_output:
                    obj_list.append(cls.create(**obj))
        except Exception:
            pass
        return obj_list

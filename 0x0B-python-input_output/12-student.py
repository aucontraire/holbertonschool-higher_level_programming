#!/usr/bin/python3
class_to_json = __import__('10-class_to_json').class_to_json


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


if __name__ == '__main__':
    student_1 = Student("John", "Doe", 23)
    student_2 = Student("Bob", "Dylan", 27)

    j_student_1 = student_1.to_json()
    j_student_2 = student_2.to_json(['first_name', 'age'])
    j_student_3 = student_2.to_json(['middle_name', 'age'])

    print(j_student_1)
    print(j_student_2)
    print(j_student_3)

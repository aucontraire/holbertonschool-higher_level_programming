#!/usr/bin/python3
import json
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):

    def test_class_membership(self):
        b0 = Base()
        self.assertIsInstance(b0, Base)

    def test_no_id_arg(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 2)
        self.assertEqual(b2.id, 3)
        self.assertEqual(b3.id, 4)

    def test_no_id_plus_id_combo(self):
        b4 = Base(5)
        b5 = Base()
        self.assertEqual(b4.id, 5)
        self.assertEqual(b5.id, 5)

    def test_to_json_string(self):
        r = Rectangle(10, 7, 2, 8)
        rd = r.to_dictionary()
        self.assertIsInstance(rd, dict)
        json_rd = Base.to_json_string([rd])
        self.assertIsInstance(json_rd, str)

        s = Square(10)
        sd = s.to_dictionary()
        self.assertIsInstance(sd, dict)
        json_sd = Base.to_json_string([sd])
        self.assertIsInstance(json_sd, str)

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        dict_list = []
        with open('Rectangle.json', 'r', encoding='utf-8') as f:
            dict_list = json.load(f)
        self.assertIsInstance(dict_list, list)
        self.assertEqual(len(dict_list), 2)
        list_ref = [
            {'id': 6, 'height': 7, 'x': 2, 'width': 10, 'y': 8},
            {'id': 7, 'height': 4, 'x': 0, 'width': 2, 'y': 0}
        ]
        self.assertListEqual(dict_list, list_ref)

        Square.save_to_file([])
        dict_list = []
        with open('Square.json', 'r', encoding='utf-8') as f:
            dict_list = json.load(f)
        self.assertIsInstance(dict_list, list)
        self.assertEqual(len(dict_list), 0)

        s1 = Square(2, x=1, y=2, id=98)
        s2 = Square(3, x=5, y=7, id=99)
        Square.save_to_file([s1, s2])
        dict_list = []
        with open('Square.json', 'r', encoding='utf-8') as f:
            dict_list = json.load(f)
        self.assertIsInstance(dict_list, list)
        self.assertEqual(len(dict_list), 2)
        list_ref = [
            {'x': 1, 'id': 98, 'size': 2, 'y': 2},
            {'x': 5, 'id': 99, 'size': 3, 'y': 7}
        ]
        self.assertListEqual(dict_list, list_ref)

    def test_from_json_string(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertListEqual(list_output, list_input)

        list_input = []
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertListEqual(list_output, list_input)

if __name__ == '__main__':
    unittest.main()

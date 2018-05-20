#!/usr/bin/python3
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareClass(unittest.TestCase):

    def test_class_membership(self):
        sq1 = Square(1)
        self.assertIsInstance(sq1, Base)
        self.assertIsInstance(sq1, Rectangle)
        self.assertIsInstance(sq1, Square)

    def test_attributes_with_correct_initialization(self):
        sq2 = Square(5, x=8, y=5, id=25)
        self.assertEqual(sq2.id, 25)
        self.assertEqual(sq2.__str__(), '[Square] (25) 8/5 - 5')
        self.assertEqual(sq2.area(), 25)

    def test_attributes_wrong_data_types(self):
        with self.assertRaises(TypeError):
            sq3 = Square('a')

    def test_attributes_with_wrong_int_range(self):
        with self.assertRaises(ValueError):
            sq4 = Square(0)
        with self.assertRaises(ValueError):
            sq5 = Square(-1)

    def test_area_method(self):
        sq6 = Square(10)
        self.assertEqual(sq6.area(), 100)

    def test_display_method(self):
        output = io.StringIO()
        sys.stdout = output
        sq7 = Square(2)
        sq7.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "##\n##\n")


    def test_str_method(self):
        sq8 = Square(2, id=99)
        str_s = sq8.__str__()
        self.assertEqual(str_s, '[Square] (99) 0/0 - 2')


    def test_display_method_w_coordinates(self):
        output = io.StringIO()
        sys.stdout = output
        sq9 = Square(2, x=1, y=1)
        sq9.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "\n ##\n ##\n")


if __name__ == '__main__':
    unittest.main()

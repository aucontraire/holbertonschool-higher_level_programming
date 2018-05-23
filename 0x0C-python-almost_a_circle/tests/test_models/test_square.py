#!/usr/bin/python3
"""Square class unittests"""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareClass(unittest.TestCase):

    def test_class_membership(self):
        """Square class unittest"""
        sq1 = Square(1)
        self.assertIsInstance(sq1, Base)
        self.assertIsInstance(sq1, Rectangle)
        self.assertIsInstance(sq1, Square)

    def test_attributes_with_correct_initialization(self):
        """Square attribute unittest"""
        sq2 = Square(5, x=8, y=5, id=25)
        self.assertEqual(sq2.id, 25)
        self.assertEqual(sq2.__str__(), '[Square] (25) 8/5 - 5')
        self.assertEqual(sq2.area(), 25)

    def test_attributes_wrong_data_types(self):
        """Square wrong data types unittest"""
        with self.assertRaises(TypeError):
            sq3 = Square('a')

    def test_attributes_with_wrong_int_range(self):
        """Square wrong int range unittest"""
        with self.assertRaises(ValueError):
            sq4 = Square(0)
        with self.assertRaises(ValueError):
            sq5 = Square(-1)

    def test_area_method(self):
        """Square area method unittest"""
        sq6 = Square(10)
        self.assertEqual(sq6.area(), 100)

    def test_display_method(self):
        """Square display method unittest"""
        output = io.StringIO()
        sys.stdout = output
        sq7 = Square(2)
        sq7.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "##\n##\n")

    def test_str_method(self):
        """Square __str__ method unittest"""
        sq8 = Square(2, id=99)
        str_s = sq8.__str__()
        self.assertEqual(str_s, '[Square] (99) 0/0 - 2')

    def test_display_method_w_coordinates(self):
        """Square display method unittest"""
        output = io.StringIO()
        sys.stdout = output
        sq9 = Square(2, x=1, y=1)
        sq9.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "\n ##\n ##\n")

    def test_size_attribute(self):
        """Square size method unittest"""
        sq10 = Square(5)
        self.assertEqual(sq10.size, 5)
        sq10.size = 9
        self.assertEqual(sq10.size, 9)
        with self.assertRaises(TypeError):
            sq10.size = 'a'
        with self.assertRaises(ValueError):
            sq10.size = -10

    def test_update_method_args_kwargs(self):
        """Square update method unittest"""
        sq11 = Square(1)
        sq11.update(1)
        self.assertEqual(sq11.__str__(), '[Square] (1) 0/0 - 1')
        sq11.update(1, 5)
        self.assertEqual(sq11.__str__(), '[Square] (1) 0/0 - 5')
        sq11.update(1, 5, 2, 3)
        self.assertEqual(sq11.__str__(), '[Square] (1) 2/3 - 5')
        sq11.update(id=99, x=4, y=7, size=8)
        self.assertEqual(sq11.__str__(), '[Square] (99) 4/7 - 8')

    def test_to_dictionary_method(self):
        """Square to_dictionary method unittest"""
        sq12 = Square(3)
        d = sq12.to_dictionary()
        self.assertIsInstance(d, dict)
        self.assertEqual(d['id'], 42)
        self.assertEqual(d['size'], 3)
        self.assertEqual(d['x'], 0)
        self.assertEqual(d['y'], 0)

if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
"""Rectangle class unittests"""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):

    def test_class_membership(self):
        """Rectangle class unittest"""
        r0 = Rectangle(10, 2)
        self.assertIsInstance(r0, Base)
        self.assertIsInstance(r0, Rectangle)

    def test_attributes_with_correct_initialization(self):
        """Rectangle  attribute unittest"""
        r1 = Rectangle(5, 6)
        self.assertEqual(r1.id, 16)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 6)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_private_instance_attributes(self):
        """Rectangle private attribute unittest"""
        r2 = Rectangle(7, 8)
        with self.assertRaises(AttributeError):
            r2.__width
        with self.assertRaises(AttributeError):
            r2.__height
        with self.assertRaises(AttributeError):
            r2.__x
        with self.assertRaises(AttributeError):
            r2.__y

    def test_attributes_wrong_data_types(self):
        """Rectangle wrong data types unittest"""
        with self.assertRaises(TypeError):
            r3 = Rectangle('a', 9)
        with self.assertRaises(TypeError):
            r4 = Rectangle(9, 'a')
        with self.assertRaises(TypeError):
            r5 = Rectangle(9, 9, 'a')
        with self.assertRaises(TypeError):
            r6 = Rectangle(9, 9, 3, 'a')

    def test_attributes_with_wrong_int_range(self):
        """Rectangle wrong int range unittest"""
        with self.assertRaises(ValueError):
            r7 = Rectangle(0, 1)
        with self.assertRaises(ValueError):
            r8 = Rectangle(1, 0)
        with self.assertRaises(ValueError):
            r9 = Rectangle(1, 1, -2)
        with self.assertRaises(ValueError):
            r10 = Rectangle(1, 1, 1, -2)

    def test_area_method(self):
        """Rectangle method unittest"""
        r11 = Rectangle(10, 10)
        self.assertEqual(r11.area(), 100)

    def test_display_method(self):
        """Rectangle display method unittest"""
        output = io.StringIO()
        sys.stdout = output
        r12 = Rectangle(2, 2)
        r12.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "##\n##\n")

    def test_str_method(self):
        """Rectangle __str__ method unittest"""
        r13 = Rectangle(2, 2)
        str_r = r13.__str__()
        self.assertEqual(str_r, '[Rectangle] (29) 0/0 - 2/2')
        r14 = Rectangle(4, 6, 2, 1, 12)
        str_r1 = r14.__str__()
        self.assertEqual(str_r1, '[Rectangle] (12) 2/1 - 4/6')

    def test_display_method_w_coordinates(self):
        """Rectangle display method unittest"""
        output = io.StringIO()
        sys.stdout = output
        r15 = Rectangle(2, 2, 2, 1)
        r15.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "\n  ##\n  ##\n")

    def test_update_method(self):
        """Rectangle update method unittest"""
        r16 = Rectangle(2, 2)
        r16.update(3)
        self.assertEqual(r16.id, 3)
        r16.update(3, 5)
        self.assertEqual(r16.width, 5)
        r16.update(3, 5, 7)
        self.assertEqual(r16.height, 7)
        r16.update(3, 5, 7, 1)
        self.assertEqual(r16.x, 1)
        r16.update(3, 5, 7, 1, 2)
        self.assertEqual(r16.y, 2)
        str_r = r16.__str__()
        self.assertEqual(str_r, '[Rectangle] (3) 1/2 - 5/7')

    def test_update_method_args_kwargs(self):
        """Rectangle update method unittest"""
        r17 = Rectangle(1, 1)
        r17.update(width=1, x=2)
        str_r = r17.__str__()
        self.assertEqual(str_r, '[Rectangle] (32) 2/0 - 1/1')
        r18 = Rectangle(2, 2)
        r18.update(x=1, height=2, y=3, width=4, id=99)
        str_r1 = r18.__str__()
        self.assertEqual(str_r1, '[Rectangle] (99) 1/3 - 4/2')
        r19 = Rectangle(10, 10, 10, 10, 10)
        str_r2 = r19.__str__()
        self.assertEqual(str_r2, '[Rectangle] (10) 10/10 - 10/10')

    def test_to_dictionary_method(self):
        """Rectangle to_dictionary method unittest"""
        r20 = Rectangle(3, 3)
        d = r20.to_dictionary()
        self.assertEqual(d['width'], 3)
        self.assertEqual(d['height'], 3)
        self.assertEqual(d['x'], 0)
        self.assertEqual(d['y'], 0)

if __name__ == '__main__':
    unittest.main()

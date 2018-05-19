#!/usr/bin/python3
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):

    def test_class_membership(self):
        r0 = Rectangle(10, 2)
        self.assertIsInstance(r0, Base)
        self.assertIsInstance(r0, Rectangle)

    def test_attributes_with_correct_initialization(self):
        r1 = Rectangle(5, 6)
        self.assertEqual(r1.id, 7)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 6)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_private_instance_attributes(self):
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
        with self.assertRaises(TypeError):
            r3 = Rectangle('a', 9)
        with self.assertRaises(TypeError):
            r4 = Rectangle(9, 'a')
        with self.assertRaises(TypeError):
            r5 = Rectangle(9, 9, 'a')
        with self.assertRaises(TypeError):
            r6 = Rectangle(9, 9, 3, 'a')

    def test_attributes_with_wrong_int_range(self):
        with self.assertRaises(ValueError):
            r7 = Rectangle(0, 1)
        with self.assertRaises(ValueError):
            r8 = Rectangle(1, 0)
        with self.assertRaises(ValueError):
            r9 = Rectangle(1, 1, -2)
        with self.assertRaises(ValueError):
            r10 = Rectangle(1, 1, 1, -2)

    def test_area_method(self):
        r11 = Rectangle(10, 10)
        self.assertEqual(r11.area(), 100)

    def test_display_method(self):
        output = io.StringIO()
        sys.stdout = output
        r12 = Rectangle(2, 2)
        r12.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "##\n##\n")


if __name__ == '__main__':
    unittest.main()

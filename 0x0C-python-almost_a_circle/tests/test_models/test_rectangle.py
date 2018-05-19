#!/usr/bin/python3
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
        self.assertEqual(r1.id, 6)
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

if __name__ == '__main__':
    unittest.main()

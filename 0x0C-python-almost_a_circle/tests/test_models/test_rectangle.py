#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):

    def test_class_membership(self):
        r0 = Rectangle(10, 2)
        self.assertIsInstance(r0, Rectangle)


if __name__ == '__main__':
    unittest.main()

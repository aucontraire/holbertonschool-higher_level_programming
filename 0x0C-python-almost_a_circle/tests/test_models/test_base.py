#!/usr/bin/python3
import unittest
from models.base import Base


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

if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def empty_list(self):
        self.assertEqual(max_integer([]), None)

    def list_int(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([1, 2, 3, 4, -4]), 4)

    def list_float(self):
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)
        self.assertEqual(max_integer([-1.1, -2.2, -3.3, -4.4]), -1.1)
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4, -4.4]), 4.4)

if __name__ == "__main__":
    unittest.main()

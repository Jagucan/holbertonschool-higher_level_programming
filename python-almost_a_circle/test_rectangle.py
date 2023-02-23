#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class Test_Rectangle(unittest.TestCase):

    def setUp(self):
        self.rect1 = Rectangle(2, 4)
        self.rect2 = Rectangle(3, 5, 1, 2)

    def test_width(self):
        self.assertEqual(self.rect1.width, 2)
        self.assertEqual(self.rect2.width, 3)

    def test_height(self):
        self.assertEqual(self.rect1.height, 4)
        self.assertEqual(self.rect2.height, 5)

    def test_x(self):
        self.assertEqual(self.rect1.x, 0)
        self.assertEqual(self.rect2.x, 1)

    def test_y(self):
        self.assertEqual(self.rect1.y, 0)
        self.assertEqual(self.rect2.y, 2)

    def test_area(self):
        self.assertEqual(self.rect1.area(), 8)
        self.assertEqual(self.rect2.area(), 15)

if __name__ == '__main__':
    unittest.main()

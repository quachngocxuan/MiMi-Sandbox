import unittest

from mimi_demo.calc import add, average


class CalcTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_average(self):
        self.assertEqual(average([1, 2, 3, 4]), 2.5)
        with self.assertRaises(ValueError):
            average([])

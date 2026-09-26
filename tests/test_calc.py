import unittest

from mimi_demo.calc import add, average


class CalcTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_average(self):
        self.assertEqual(average([1, 2, 3, 4]), 2.5)
        with self.assertRaises(ValueError):
            average([])


class MedianTest(unittest.TestCase):
    def test_median(self):
        from mimi_demo.calc import median

        self.assertEqual(median([3, 1, 2]), 2)
        self.assertEqual(median([4, 1, 3, 2]), 2.5)
        self.assertEqual(median([7]), 7)
        with self.assertRaises(ValueError):
            median([])

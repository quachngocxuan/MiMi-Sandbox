import unittest

from mimi_demo.dates import is_leap_year


class LeapYearTest(unittest.TestCase):
    def test_leap_years(self):
        for year in (2000, 2024, 1996):
            self.assertTrue(is_leap_year(year), year)

    def test_not_leap_years(self):
        for year in (1900, 2023, 2100):
            self.assertFalse(is_leap_year(year), year)

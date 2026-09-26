import unittest


class DurationTest(unittest.TestCase):
    def test_parse(self):
        from mimi_demo.duration import parse_duration

        self.assertEqual(parse_duration("90s"), 90)
        self.assertEqual(parse_duration("1h30m"), 5400)
        self.assertEqual(parse_duration("2h"), 7200)
        self.assertEqual(parse_duration("1h 5m 10s"), 3910)

    def test_rejects_bad_input(self):
        from mimi_demo.duration import parse_duration

        for bad in ("", "abc", "10", "5x", "-1m"):
            with self.assertRaises(ValueError, msg=bad):
                parse_duration(bad)

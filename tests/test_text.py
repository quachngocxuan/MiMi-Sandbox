import unittest

from mimi_demo.text import slugify, word_count


class TextTest(unittest.TestCase):
    def test_word_count(self):
        self.assertEqual(word_count("MiMi  giao   việc"), 3)

    def test_slugify(self):
        self.assertEqual(slugify("Hello MiMi World"), "hello-mimi-world")

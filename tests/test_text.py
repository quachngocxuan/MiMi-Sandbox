import unittest

from mimi_demo.text import slugify, word_count


class TextTest(unittest.TestCase):
    def test_word_count(self):
        self.assertEqual(word_count("MiMi  giao   việc"), 3)

    def test_slugify(self):
        self.assertEqual(slugify("Hello MiMi World"), "hello-mimi-world")


class WordCountPunctuationTest(unittest.TestCase):
    def test_ignores_punctuation_only_tokens(self):
        self.assertEqual(word_count("a - b"), 2)
        self.assertEqual(word_count("Hello , world !"), 2)
        self.assertEqual(word_count("... ---"), 0)
        self.assertEqual(word_count("MiMi's 2 tasks"), 3)

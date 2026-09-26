import unittest

from mimi_demo.text import slugify, word_count


class TextTest(unittest.TestCase):
    def test_word_count(self):
        self.assertEqual(word_count("MiMi  giao   việc"), 3)

    def test_slugify(self):
        self.assertEqual(slugify("Hello MiMi World"), "hello-mimi-world")


class SlugifyVietnameseTest(unittest.TestCase):
    def test_strips_diacritics_and_punctuation(self):
        self.assertEqual(slugify("Xin chào, MiMi!"), "xin-chao-mimi")
        self.assertEqual(slugify("Đường   Lê Lợi  (Quận 1)"), "duong-le-loi-quan-1")
        self.assertEqual(slugify("  --Hello--  "), "hello")

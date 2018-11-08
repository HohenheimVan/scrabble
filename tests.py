from scrabble import *
import unittest

# a = Dictionary("dictionary.txt")


class WordTest(unittest.TestCase):
    def test_compare_score(self):
        word = Word("aBc")
        self.assertEqual(Word.compare_score(word, 7), word)

    def test_score__is_none(self):
        word = Word("ad.,sfs")
        self.assertIsNone(word.score)

    def test_score(self):
        word = Word("abc")
        self.assertEqual(word.score, 7)

    def test_word_string(self):
        word = Word("abc")
        self.assertEqual(word.string, "ABC")


class DictionaryTest(unittest.TestCase):
    def test_find_best_word(self):
        dictionary = Dictionary("tests.txt")
        self.assertEqual(dictionary.find_best_word(), "21 EXPENSIVE")

    def test_find_word_by_score(self):
        dictionary = Dictionary("tests.txt")
        self.assertEqual(dictionary.find_word_by_score(9).string, "MUSIC")

    def test_find_word_score_by_score(self):
        dictionary = Dictionary("tests.txt")
        self.assertEqual(dictionary.find_word_by_score(10).score, 10)

    def test_find_word_by_score_value_err(self):
        dictionary = Dictionary("tests.txt")
        self.assertRaises(ValueError, dictionary.find_word_by_score(",.ads"))

    def test_find_word_by_score_is_none(self):
        dictionary = Dictionary("tests.txt")
        self.assertIsNone(dictionary.find_word_by_score(100))


if __name__ == "__main__":
    unittest.main()

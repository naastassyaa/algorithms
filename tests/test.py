import unittest
from main import search


class TestPatternSearch(unittest.TestCase):

    def test_needle_found_single_occurrence(self):
        haystack = "AABAACAADAABAB"
        needle = "AABAA"
        self.assertEqual(search(needle, haystack), [0])

    def test_needle_found_multiple_occurrences(self):
        haystack = "AABAACAADAABAAABAA"
        needle = "AABA"
        self.assertEqual(search(needle, haystack), [0, 9, 13])

    def test_needle_not_found(self):
        haystack = "AABAACAADAABAAABAA"
        needle = "ABC"
        self.assertEqual(search(needle, haystack), [])

    def test_empty_needle(self):
        haystack = "AABAACAADAABAAABAA"
        needle = ""
        self.assertEqual(search(needle, haystack), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

    def test_empty_haystack(self):
        haystack = ""
        needle = "ABA"
        self.assertEqual(search(needle, haystack), [])

    def test_needle_longer_than_haystack(self):
        haystack = "AABA"
        needle = "AABAA"
        self.assertEqual(search(needle, haystack), [])

    def test_special_characters(self):
        haystack = "AAB@#C$%DAABAAABAA"
        needle = "@#C$%"
        self.assertEqual(search(needle, haystack), [3])

    def test_case_sensitivity(self):
        haystack = "aabaacaadaabaaabaa"
        needle = "AABAA"
        self.assertEqual(search(needle, haystack), [])

    def test_multiple_occurrences_overlapping(self):
        haystack = "AAABAABAABAAABAABAA"
        needle = "AABA"
        self.assertEqual(search(needle, haystack), [1, 4, 7, 11, 14])

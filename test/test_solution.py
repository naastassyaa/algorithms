import unittest

from main import find_sum


class TestFindSum(unittest.TestCase):
    def test_basic_case(self):
        s = [1, 2, 3, 4, 5]
        sum_to_find = 8
        self.assertTrue(find_sum(s, sum_to_find))

    def test_no_triplets(self):
        s = [1, 2, 3, 4, 5]
        sum_to_find = 20
        self.assertFalse(find_sum(s, sum_to_find))

    def test_empty_list(self):
        s = []
        sum_to_find = 10
        self.assertFalse(find_sum(s, sum_to_find))

    def test_negative_numbers(self):
        s = [-1, 2, -3, 4, 5, -2]
        sum_to_find = 0
        self.assertTrue(find_sum(s, sum_to_find))

    def test_duplicate_elements(self):
        s = [1, 2, 2, 3, 4, 5]
        sum_to_find = 9
        self.assertTrue(find_sum(s, sum_to_find))


if __name__ == '__main__':
    unittest.main()


import unittest
from main import solution


class TestSolution(unittest.TestCase):
    def test_case_5_5(self):
        matrix = [
            ["1", "2", "3", "4", "5"],
            ["6", "7", "8", "9", "10"],
            ["11", "12", "13", "14", "15"],
            ["16", "17", "18", "19", "20"],
            ["21", "22", "23", "24", "25"]
        ]
        expected_output = "1 2 3 4 5 10 9 8 7 6 11 12 13 14 15 20 19 18 17 16 21 22 23 24 25"
        captured_output = solution(matrix)
        self.assertEqual(captured_output, expected_output)

    def test_case_2_4(self):
        matrix = [
            ["1", "2", "5", "6"],
            ["3", "4", "7", "8"]
        ]
        expected_output = "1 2 5 6 8 7 4 3"
        captured_output = solution(matrix)
        self.assertEqual(captured_output, expected_output)

    def test_case_6_1(self):
        matrix = [
            ["1"],
            ["2"],
            ["3"],
            ["4"],
            ["5"],
            ["6"]
        ]
        expected_output = "1 2 3 4 5 6"
        captured_output = solution(matrix)
        self.assertEqual(captured_output, expected_output)

    def test_case_1_6(self):
        matrix = [
            ["1", "2", "3", "4", "5", "6"]
        ]
        expected_output = "1 2 3 4 5 6"
        captured_output = solution(matrix)
        self.assertEqual(captured_output, expected_output)

    def test_case_1_1(self):
        matrix = [
            ["1"]
        ]
        expected_output = "1"
        captured_output = solution(matrix)
        self.assertEqual(captured_output, expected_output)
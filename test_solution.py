# test_solution.py
import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_typical_cases(self):
        test_cases = [
            ([[2, 5, 3], [1, 8, 4], [1, 2, 3]], [2, 5, 3], True),
            ([[2, 5, 3], [1, 8, 4], [1, 2, 3]], [1, 8, 4], True),
            ([[2, 5, 3], [1, 8, 4], [1, 2, 3]], [1, 2, 6], False),
        ]
        for triplets, target, expected in test_cases:
            with self.subTest(triplets=triplets, target=target):
                self.assertEqual(self.solution.mergeTriplets(triplets, target), expected)

    def test_edge_cases(self):
        test_cases = [
            ([[1, 1, 1]], [1, 1, 1], True),
            ([[1, 1, 1]], [2, 2, 2], False),
            ([], [1, 1, 1], False),          
            ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], [1, 1, 1], True),
        ]
        for triplets, target, expected in test_cases:
            with self.subTest(triplets=triplets, target=target):
                self.assertEqual(self.solution.mergeTriplets(triplets, target), expected)

    def test_large_cases(self):
        test_cases = [
            ([[i, i, i] for i in range(1000)], [999, 999, 999], True),
            ([[i, i, i] for i in range(1000)], [1000, 1000, 1000], False),
        ]
        for triplets, target, expected in test_cases:
            with self.subTest(triplets=triplets, target=target):
                self.assertEqual(self.solution.mergeTriplets(triplets, target), expected)

if __name__ == "__main__":
    unittest.main()

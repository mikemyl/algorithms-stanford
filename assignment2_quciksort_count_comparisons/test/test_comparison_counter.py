import unittest
from unittest.mock import patch
from assignment2_quciksort_count_comparisons.app.comparison_counter import ComparisonCounter


class ComparisonCounterTest(unittest.TestCase):
    @patch('builtins.input', return_value='2 2 1 3')
    def test_comparison_counter_can_sort(self, stdin):
        """ComparisonCounter should be able to sort the input array"""
        counter = ComparisonCounter()
        counter.sort()
        expected = [1, 2, 2, 3]
        actual = counter.array
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='3 9 8 4 6 10 2 5 7 1')
    def test_coount_number_of_comparisons(self, stdin):
        """ComparisonCounter should be able to count the number of comparisons"""
        counter = ComparisonCounter()
        counter.sort()
        expected = 25
        actual = counter.comparisons
        self.assertEqual(expected, actual)

    def test_coount_number_of_comparisons_100(self):
        """ComparisonCounter should be able to count the number of comparisons"""
        counter = ComparisonCounter('100.txt')
        counter.sort()
        expected = 615
        actual = counter.comparisons
        self.assertEqual(expected, actual)

    def test_coount_number_of_comparisons_1000(self):
        """ComparisonCounter should be able to count the number of comparisons"""
        counter = ComparisonCounter('1000.txt')
        counter.sort()
        expected = 10297
        actual = counter.comparisons
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()

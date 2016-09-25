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
        actual = counter._array
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()

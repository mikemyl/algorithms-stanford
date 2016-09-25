import unittest
from unittest.mock import patch
from assignment2_quciksort_count_comparisons.app.comparison_counter import QuickSorterFirstElementPivot, \
    QuickSorterLastElementPivot, QuickSorterMedianElementPivot


class ComparisonCounterTest(unittest.TestCase):
    @patch('builtins.input', return_value='2 2 1 3')
    def test_comparison_counter_can_sort(self, stdin):
        """ComparisonCounter should be able to sort the input array"""
        counter = QuickSorterFirstElementPivot()
        counter.sort()
        expected = [1, 2, 2, 3]
        actual = counter.array
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='3 9 8 4 6 10 2 5 7 1')
    def test_count_number_of_comparisons(self, stdin):
        """ComparisonCounter should be able to count the number of comparisons"""
        counter = QuickSorterFirstElementPivot()
        counter.sort()
        expected = 25
        actual = counter.comparisons
        self.assertEqual(expected, actual)

    def test_count_number_of_comparisons_100(self):
        """ComparisonCounter should be able to count the number of comparisons"""
        sorters = (QuickSorterFirstElementPivot('100.txt'), QuickSorterLastElementPivot('100.txt'),
                   QuickSorterMedianElementPivot('100.txt'))
        for sorter in sorters:
            sorter.sort()
        expected = (615, 587, 518)
        actual = (sorters[0].comparisons, sorters[1].comparisons, sorters[2].comparisons)
        self.assertEqual(expected, actual)

    def test_count_number_of_comparisons_1000(self):
        """ComparisonCounter should be able to count the number of comparisons"""
        sorters = (QuickSorterFirstElementPivot('1000.txt'), QuickSorterLastElementPivot('1000.txt'),
                   QuickSorterMedianElementPivot('1000.txt'))
        for sorter in sorters:
            sorter.sort()
        expected = (10297, 10184, 8921)
        actual = (sorters[0].comparisons, sorters[1].comparisons, sorters[2].comparisons)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()

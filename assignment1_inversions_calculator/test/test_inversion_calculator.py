import unittest
from unittest.mock import patch

from assignment1_inversions_calculator.app.inversion_calculator import InversionCalculator


class InversionCalculatorTest(unittest.TestCase):

    @patch('builtins.input', return_value='1 2 3')
    def test_calculator_reads_input(self, stdin):
        """InversionCalculator.read_input should read its input from stdin if no file given"""
        calculator = InversionCalculator()
        calculator.read_input()
        expected = [1, 2, 3]
        actual = calculator.array
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='3 1 2 0 5')
    def test_calculator_sorts_array(self, stdin):
        """InversionCalculator.sort() should sort the given array"""
        calculator = InversionCalculator()
        calculator.read_input()
        expected = [0, 1, 2, 3, 5]
        self.assertEqual(expected, calculator.sort())

    @patch('builtins.input', return_value='9 12 3 1 6 8 2 5 14 13 11 7 10 4 0')
    def test_calculator_counts_inversions(self, stdin):
        """InversionCalculator.sort() should correctly count the number of inversions"""
        calculator = InversionCalculator()
        calculator.read_input()
        calculator.sort()
        expected_inversions = 56
        self.assertEqual(expected_inversions, calculator.inversions)

if __name__ == '__main__':
    unittest.main()

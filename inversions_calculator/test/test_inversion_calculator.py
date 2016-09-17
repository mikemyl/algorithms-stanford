import unittest
from unittest.mock import patch

from inversions_calculator.app.inversion_calculator import InversionCalculator


class InversionCalculatorTest(unittest.TestCase):

    def setUp(self):
        pass

    @patch('builtins.input', return_value='1 2 3')
    def test_calculator_reads_input(self, stdin):
        """Inversion calculator should read its input from stdin"""
        calculator = InversionCalculator()
        expected = [1, 2, 3]
        calculator.read_input()
        actual = calculator.array
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='3 1 2 0 5')
    def test_calculator_sorts_array(self, stdin):
        """InversionCalculator.sort() should sort the given array"""
        calculator = InversionCalculator()
        calculator.read_input()
        expected = [0, 1, 2, 3, 5]
        self.assertEqual(expected, calculator.sort())


if __name__ == '__main__':
    unittest.main()

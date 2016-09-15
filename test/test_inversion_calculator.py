import unittest
from unittest.mock import patch
from app.inversion_calculator import InversionCalculator


class InversionCaclulatorTest(unittest.TestCase):

    def setUp(self):
        pass

    @patch('builtins.input')
    def test_calculator_reads_input(self, stdin):
        calculator = InversionCalculator()
        stdin.return_value = "1\n2\n3\n"
        expected = [1, 2, 3]
        actual = calculator.read_input()
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()

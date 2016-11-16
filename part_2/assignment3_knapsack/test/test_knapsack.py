import unittest
from unittest.mock import patch
from unittest import mock


from part_2.assignment3_knapsack.app.knapsack import Knapsack

one_item_knapsack = "5 1\n" \
                    "5 5"
two_item_knapsack = "10 2\n" \
                    "6 5\n" \
                    "7 5"


class KanpsackTest(unittest.TestCase):

    @patch("builtins.open", create=True)
    def test_Value_OnOneItemKnapsack_RetursThatItem(self, mock_open):
        mock_open.side_effect = [mock.mock_open(read_data=one_item_knapsack).return_value]
        knapsack = Knapsack(one_item_knapsack)
        self.assertEqual(knapsack.value, 5)

    @patch("builtins.open", create=True)
    def test_Value_TwoItemsKnapsack_ReturnsBothItems(self, mock_open):
        mock_open.side_effect = [mock.mock_open(read_data=two_item_knapsack).return_value]
        knapsack = Knapsack(two_item_knapsack)
        self.assertEqual(knapsack.value, 13)

    def test_Value_WithManyItems_ReturnsMaxValue(self):
        knapsack = Knapsack("knapsack_test_1.txt")
        self.assertEqual(knapsack.value, 35)


if __name__ == '__main__':
    unittest.main()

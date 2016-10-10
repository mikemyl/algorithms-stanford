import unittest

from assignment_6_2_median_maintenance.app.median_maintainer import MedianMaintainer


class TestMedianMaintainer(unittest.TestCase):
    def test_find_median_sum_1(self):
        median_maintainer = MedianMaintainer(input_array=[9, 9, 7, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        median_sum = median_maintainer.sum_medians()
        expected_sum = 2
        self.assertEqual(median_sum, expected_sum)

    def test_find_median_sum_2(self):
        median_maintainer = MedianMaintainer(input_array=[2, 8, 9, 7, 3, 1, 4])
        median_sum = median_maintainer.sum_medians()
        expected_sum = 5
        self.assertEqual(median_sum, expected_sum)

    def test_find_median_sum_coursera_testcase(self):
        median_maintainer = MedianMaintainer(input_file='assignment_6_2.txt')
        median_sum = median_maintainer.sum_medians()
        print(median_sum)


if __name__ == '__main__':
    unittest.main()

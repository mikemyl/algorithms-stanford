import unittest

from part_2.assignment1_greedy_algorithms.app.job_scheduler import DifferenceJobScheduler, RatioJobScheduler


class MyTestCase(unittest.TestCase):

    def test_different_job_scheduler_testcase_1(self):
        diff_job_scheduler = DifferenceJobScheduler("test_forum_1.txt")
        self.assertEqual(31814, diff_job_scheduler.sum)

    def test_ratio_job_scheduler_testcase_1(self):
        ratio_job_scheduler = RatioJobScheduler("test_forum_1.txt")
        self.assertEqual(31814, ratio_job_scheduler.sum)

    def test_different_job_scheduler_testcase_2(self):
        diff_job_scheduler = DifferenceJobScheduler("test_forum_2.txt")
        self.assertEqual(61545, diff_job_scheduler.sum)

    def test_ratio_job_scheduler_testcase_2(self):
        ratio_job_scheduler = RatioJobScheduler("test_forum_2.txt")
        self.assertEqual(60213, ratio_job_scheduler.sum)

    def test_different_job_scheduler_testcase_3(self):
        diff_job_scheduler = DifferenceJobScheduler("test_forum_3.txt")
        self.assertEqual(688647, diff_job_scheduler.sum)

    def test_ratio_job_scheduler_testcase_3(self):
        ratio_job_scheduler = RatioJobScheduler("test_forum_3.txt")
        self.assertEqual(674634, ratio_job_scheduler.sum)


if __name__ == '__main__':
    unittest.main()

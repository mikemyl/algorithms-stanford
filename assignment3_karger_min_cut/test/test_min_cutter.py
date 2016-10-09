import unittest
from assignment3_karger_min_cut.app.min_cutter import KargerMinCutter


class MinCutterTest(unittest.TestCase):

    def setUp(self):
        self._min_cutter = KargerMinCutter('four_nodes_test.txt')

    def test_picks_random_edge(self):
        v1, v2 = self._min_cutter._pick_random_edge()
        self.assertIsNotNone((v1, v2))

    def test_eventually_finds_min_cut_4nodes(self):
        min_cut = 999
        for i in range(8):
            min_cutter = KargerMinCutter('four_nodes_test.txt')
            cut = min_cutter.find_min_cut()
            if cut < min_cut:
                min_cut = cut
        self.assertEqual(min_cut, 2)

    def test_eventually_finds_min_cut_8nodes(self):
        min_cut = 999
        for i in range(16):
            min_cutter = KargerMinCutter('eight_nodes_test.txt')
            cut = min_cutter.find_min_cut()
            if cut < min_cut:
                min_cut = cut
        self.assertEqual(min_cut, 2)

    def test_eventually_finds_min_cut_40nodes(self):
        min_cut = 999
        for i in range(80):
            min_cutter = KargerMinCutter('40_nodes_test.txt')
            cut = min_cutter.find_min_cut()
            if cut < min_cut:
                min_cut = cut
        self.assertEqual(min_cut, 3)

    def test_eventually_finds_min_cut_coursera_testcase(self):
        min_cut = 99999
        for i in range(40000):
            min_cutter = KargerMinCutter('coursera_test.txt')
            cut = min_cutter.find_min_cut()
            if cut < min_cut:
                min_cut = cut
            print(min_cut)

import unittest

from assignment4_strongly_connected_components.app.scc_finder import SccFinder


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.scc_finder = SccFinder("jason_smko.txt")

    def test_scc_finder_reads_graph(self):
        self.assertIsNotNone(self.scc_finder)

    def test_scc_finder_sorts_by_finish_times(self):
        expected_finish_times = [5, 2, 8, 3, 6, 9, 4, 7, 1]
        self.scc_finder.compute_finish_times()
        self.assertEqual(self.scc_finder.finish_order, expected_finish_times)

    def test_scc_computes_sccs(self):
        self.scc_finder.compute_finish_times()
        self.scc_finder.compute_sccs()

    def test_scc_computes_sccs_smko_second_testcase(self):
        scc_finder = SccFinder("jason_smko2.txt")
        scc_finder.compute_finish_times()
        scc_finder.compute_sccs()
        expected_sccs = [3, 3, 2]
        self.assertEqual(scc_finder.scc_list, expected_sccs)

    def test_scc_computes_sccs_smko_third_testcase(self):
        scc_finder = SccFinder("jason_smko3.txt")
        scc_finder.compute_finish_times()
        scc_finder.compute_sccs()
        expected_sccs = [3, 3, 1, 1]
        self.assertEqual(scc_finder.scc_list, expected_sccs)

    def test_scc_computes_sccs_smko_fourth_testcase(self):
        scc_finder = SccFinder("jason_smko4.txt")
        scc_finder.compute_finish_times()
        scc_finder.compute_sccs()
        expected_sccs = [7, 1]
        self.assertEqual(scc_finder.scc_list, expected_sccs)

    def test_scc_computes_sccs_smko_last_testcase(self):
        scc_finder = SccFinder("jason_smko_last.txt")
        scc_finder.compute_finish_times()
        scc_finder.compute_sccs()
        expected_sccs = [6, 3, 2, 1]
        self.assertEqual(scc_finder.scc_list, expected_sccs)

    def test_scc_computes_sccs_coursera_large_testcase(self):
        scc_finder = SccFinder("assignment_4.txt")
        scc_finder.compute_finish_times()
        scc_finder.compute_sccs()
        expected_sccs = [434821, 968, 459, 313, 211]
        self.assertEqual(scc_finder.scc_list[:5], expected_sccs)

if __name__ == '__main__':
    unittest.main()

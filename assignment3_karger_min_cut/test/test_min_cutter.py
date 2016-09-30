import unittest
from assignment3_karger_min_cut.app.min_cutter import  MinCutter


class MinCutterTest(unittest.TestCase):
    def test_min_cutter_reads_graph(self):
        min_cutter = MinCutter('four_nodes_test.txt')
        vertexes = min_cutter.get_graph()
        self.assertIsNotNone(vertexes)


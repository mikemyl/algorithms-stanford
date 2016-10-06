import unittest
from assignment5_dijkstra.app.dijkstra_path_finder import DijkstraPathFinder


class MyTestCase(unittest.TestCase):
    def test_small_graph(self):
        path_finder = DijkstraPathFinder('forum_1.txt')


if __name__ == '__main__':
    unittest.main()

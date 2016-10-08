import unittest
from assignment5_dijkstra.app.dijkstra_path_finder import DijkstraPathFinder


class MyTestCase(unittest.TestCase):
    def test_small_graph(self):
        path_finder = DijkstraPathFinder('forum_1.txt')
        paths = path_finder.compute_shortest_paths()
        expected = {1: (0, []), 2: (1, [2]), 3: (2, [2, 3]), 4: (3, [2, 3, 4]), 5: (4, [2, 3, 4, 5]), 6: (4, [8, 7, 6])
                    , 7: (3, [8, 7]), 8: (2, [8])}
        self.assertEqual(expected, paths)

    def test_small_graph_2(self):
        path_finder = DijkstraPathFinder('forum_2.txt')
        paths = path_finder.compute_shortest_paths()
        expected = {1: 0, 3: 2, 2: 3, 6: 4, 7: 4, 10: 4, 4: 6, 8: 6, 9: 8, 5: 9}
        actual = {vertex: distance[0] for (vertex, distance) in paths.items()}
        self.assertEqual(expected, actual)

    def test_assignment_5(self):
        path_finder = DijkstraPathFinder('assignment_5.txt')
        paths = path_finder.compute_shortest_paths()
        actual = {vertex: distance[0] for (vertex, distance) in paths.items()}
        print(actual[7])
        print(actual[37])
        print(actual[59])
        print(actual[82])
        print(actual[99])
        print(actual[115])
        print(actual[133])
        print(actual[165])
        print(actual[188])
        print(actual[197])

if __name__ == '__main__':
    unittest.main()

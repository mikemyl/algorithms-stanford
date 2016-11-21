import unittest

from part_2.assignment4_multiple_shortest_paths.app.multiple_shortest_path_finder import ShortestPathFinder


class MyTestCase(unittest.TestCase):
    def test_forum_1(self):
        path_finder = ShortestPathFinder("test_forum_1.txt")
        self.assertEqual(path_finder.get_shortest_path(), -10003)

    def test_forum_2(self):
        path_finder = ShortestPathFinder("test_forum_2.txt")
        self.assertEqual(path_finder.get_shortest_path(), -6)

if __name__ == '__main__':
    unittest.main()

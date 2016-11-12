import unittest
from part_2.assignment2_clustering.app.cluster_small import ClusterFinder


class ClusterFinderTest(unittest.TestCase):
    def test_forum_1(self):
        cluster_finder = ClusterFinder("cluster_small_forum_1.txt")
        self.assertEqual(cluster_finder.find_clusters(4), 9)

    def test_forum_2(self):
        cluster_finder = ClusterFinder("cluster_small_forum_2.txt")
        self.assertEqual(cluster_finder.find_clusters(4), 17)


if __name__ == '__main__':
    unittest.main()

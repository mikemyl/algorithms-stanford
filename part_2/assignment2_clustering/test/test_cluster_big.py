import unittest
from part_2.assignment2_clustering.app.cluster_big import BigClusterFinder


class ClusterFinderTest(unittest.TestCase):
    def test_forum_1(self):
        cluster_finder = BigClusterFinder("cluster_big_forum_1.txt")
        self.assertEqual(cluster_finder.find_number_of_clusters(), 4)

    def test_forum_2(self):
        cluster_finder = BigClusterFinder("cluster_big_forum_2.txt")
        self.assertEqual(cluster_finder.find_number_of_clusters(), 7)


if __name__ == '__main__':
    unittest.main()

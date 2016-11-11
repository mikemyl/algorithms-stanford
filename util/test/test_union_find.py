import unittest

from util.app.union_find import UnionFind


class UnionFindTest(unittest.TestCase):
    def test_NewUnionFind_WithNoUnions_AllNodesPointToThemselves(self):
        uf = UnionFind(5)
        for item in range(1, 5 + 1):
            self.assertEqual(item, uf.find(item))

    def test_Union_TwoNodes_HaveTheSameParent(self):
        uf = UnionFind(2)
        uf.union(1, 2)
        self.assertEqual(uf.find(1), uf.find(2))


if __name__ == '__main__':
    unittest.main()

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

    def test_Union_ThreeNodesInTwoPairs_AllHaveTheSameParent(self):
        uf = UnionFind(3)
        uf.union(1, 2)
        uf.union(2, 3)
        self.assertEqual(uf.find(1), uf.find(3))

    def test_Find_OnNotConnectedNodes_ReturnsFalse(self):
        uf = UnionFind(5)
        uf.union(1, 2)
        uf.union(2, 3)
        uf.union(3, 4)
        self.assertEqual(uf.find(1), uf.find(3))
        self.assertEqual(uf.find(2), uf.find(4))
        self.assertNotEqual(uf.find(1), uf.find(5))
        self.assertNotEqual(uf.find(4), uf.find(5))

    def test_GetCount_OnNonConnectedNodes_ReturnInitialSizeAsCount(self):
        uf = UnionFind(10)
        self.assertEqual(uf.count, 10)

    def test_GetCount_OnNonEffectUnions_RemainsTheSame(self):
        uf = UnionFind(10)
        uf.union(1, 2)
        self.assertEqual(uf.count, 9)
        uf.union(1, 2)
        self.assertEqual(uf.count, 9)
        uf.union(2, 3)
        self.assertEqual(uf.count, 8)
        uf.union(1, 3)
        self.assertEqual(uf.count, 8)

if __name__ == '__main__':
    unittest.main()

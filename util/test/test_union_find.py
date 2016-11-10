import unittest

from util.app.union_find import UnionFind


class MyTestCase(unittest.TestCase):
    def test_NewUnionFind_NoUnions_AllNodesPointToThemselves(self):
        items = [1, 2, 3, 4, 5]
        uf = UnionFind()
        for index, item in enumerate(uf):
            self.assertEqual(item, uf.find(item))


if __name__ == '__main__':
    unittest.main()

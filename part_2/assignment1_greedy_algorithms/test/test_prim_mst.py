import unittest

from part_2.assignment1_greedy_algorithms.app.prim_mst import PrimMST


class MyTestCase(unittest.TestCase):
    def test_prim_1(self):
        mst = PrimMST("test_prim_1.txt")
        self.assertEqual(4, mst.get_cost())

    def test_prim_2(self):
        mst = PrimMST("test_prim_2.txt")
        self.assertEqual(16, mst.get_cost())

    def test_prim_3(self):
        mst = PrimMST("test_prim_3.txt")
        self.assertEqual(-3, mst.get_cost())


if __name__ == '__main__':
    unittest.main()

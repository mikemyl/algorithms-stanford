import itertools

from util.app.union_find import UnionFind


class BigClusterFinder:

    def __init__(self, input_file):
        with open(input_file, "r") as file:
            nodes, bits_per_node = file.readline().split()
            self._size = int(nodes)
            self._bits = int(bits_per_node)
            self._numbers = {}
            for node in range(1, self._size + 1):
                line = file.readline().split()
                bits = tuple((int(num) for num in line))
                num = 0
                for index, bit in enumerate(bits[::-1]):
                    num += bit * (2 ** index)
                if num in self._numbers:
                    self._numbers[num].append((node, bits))
                else:
                    self._numbers[num] = [(node, bits)]

    def find_number_of_clusters(self):
        uf = UnionFind(self._size)
        distances = [2 ** i for i in range(self._bits)]
        distances.extend([-num for num in distances])
        for pair in itertools.combinations(distances, 2):
            bit_1, bit_2 = pair
            distances.append(bit_1 + bit_2)
        distances = [0] + distances
        unions_zero, unions_one, unions_two = [], [], []
        for distance in distances:
            for i in self._numbers.keys():
                if (i + distance) in self._numbers:
                    for node_from, bits_from in self._numbers[i]:
                        for node_to, bits_to in self._numbers[i + distance]:
                            if self._hamming(bits_from, bits_to) == 0:
                                unions_zero.append((node_from, node_to))
                            elif self._hamming(bits_from, bits_to) == 1:
                                unions_one.append((node_from, node_to))
                            elif self._hamming(bits_from, bits_to) == 2:
                                unions_two.append((node_from, node_to))
        self._make_unions(uf, unions_zero)
        self._make_unions(uf, unions_one)
        self._make_unions(uf, unions_two)
        return uf.count

    @staticmethod
    def _hamming(bits_from, bits_to):
        hamming = 0
        for index, bit in enumerate(bits_from):
            if bit != bits_to[index]:
                hamming += 1
        return hamming

    @staticmethod
    def _make_unions(uf, unions_zero):
        for node_from, node_to in unions_zero:
            if not uf.connected(node_from, node_to):
                uf.union(node_from, node_to)


if __name__ == "__main__":
    cluster_finder = BigClusterFinder("clustering_big.txt")
    print(cluster_finder.find_number_of_clusters())
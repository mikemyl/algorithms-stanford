class UnionFind:

    def __init__(self, size):
        """
        Creates a new Union-Find data structure that holds <size> elements
        This class uses 1-based indexing, which means that we allocate 1 extra slot,
        but we have a more clear mapping

        :param size: the # of elements that we hold in our UF data structure
        """
        if size < 1:
            raise ValueError("size should be greater than one")
        self.count = size
        self._size = size
        self._uf = [None] * (self._size + 1)
        for num in range(1, self._size + 1):
            self._uf[num] = (num, 0)

    def find(self, item):
        """
        Finds the "leader" of the item <item>

        :param item: the item to check
        :return: the leader item that the <item> belongs to
        """
        if not 1 <= item <= self._size:
            raise ValueError("Item should be in the range [1..{}".format(self._size))
        parent = self._get_parent(item)
        prev = item
        while self._uf[parent][0] != parent:
            self._uf[prev] = self._uf[parent][0], self._uf[prev][1]
            prev = parent
            parent = self._get_parent(parent)
        return parent

    def connected(self, first, second):
        """
        Checks whether <first> and <second> are in the same group

        :param first: the first item to be checked
        :param second: the second item
        :return: True if connected, else otherwise
        """
        if not (1, 1) <= (first, second) <= (self._size, self._size):
            raise ValueError("Items {}, {} should be in the range [1..{}]".format(first, second, self._size))
        return self.find(first) == self.find(second)

    def union(self, first, second):
        """
        Unions <first> with <second> item

        :param first: the first item to be connected
        :param second: the second item to be connected
        :return: None
        """
        if not (1, 1) <= (first, second) <= (self._size, self._size):
            raise ValueError("Items {}, {} should be in the range [1..{}]".format(first, second, self._size))
        first_parent = self.find(first)
        second_parent = self.find(second)
        if first_parent == second_parent:
            return
        self.count -= 1
        first_rank = self._uf[first_parent][1]
        second_rank = self._uf[second_parent][1]

        if first_rank > second_rank:
            self._uf[second_parent] = self._uf[first_parent][0], self._uf[second_parent][1]
        elif second_rank > first_rank:
            self._uf[first_parent] = self._uf[second_parent][0], self._uf[first_parent][1]
        else:
            self._uf[second_parent] = self._uf[first_parent]
            self._uf[first_parent] = (first_parent, self._uf[first_parent][1] + 1)

    def _get_parent(self, item):
        node, node_range = self._uf[item]
        return node


from operator import itemgetter

import sys


class Knapsack:
    def __init__(self, input_file):
        self.value = 0
        self._cache = {}
        with open(input_file, "r") as file:
            self._weight, item_count = (int(num) for num in file.readline().split())
            self._items = [None] * item_count
            for index in range(item_count):
                value, weight = (int(num) for num in file.readline().split())
                self._items[index] = Item(value, weight)
        self.value = self._compute_value(self._weight, item_count - 1)

    def _compute_value(self, weight, index):
        if weight == 0 or index == -1:
            return 0
        item = self._items[index]
        if item.weight > weight:
            if (weight, index - 1) not in self._cache:
                self._cache[(weight, index - 1)] = self._compute_value(weight, index - 1)
            return self._cache[(weight, index - 1)]
        else:
            if (weight - item.weight, index - 1) not in self._cache:
                self._cache[(weight - item.weight, index - 1)] = self._compute_value(weight - item.weight, index - 1)
            solution_including_this_item = item.value + self._cache[(weight - item.weight, index - 1)]
            if (weight, index - 1) not in self._cache:
                self._cache[(weight, index - 1)] = self._compute_value(weight, index - 1)
            solution_without_this_item = self._cache[(weight, index - 1)]
            return max(solution_including_this_item, solution_without_this_item)


class Item(tuple):
    __slots__ = []

    def __new__(cls, value, weight):
        return tuple.__new__(cls, (value, weight))

    value = property(itemgetter(0))
    weight = property(itemgetter(1))

if __name__ == "__main__":
    sys.setrecursionlimit(3000)
    knapsack = Knapsack("knapsack_small.txt")
    print(knapsack.value)

    knapsack_big = Knapsack("knapsack_big.txt")
    print(knapsack_big.value)
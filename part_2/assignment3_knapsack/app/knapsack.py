from operator import itemgetter


class Knapsack:
    def __init__(self, input_file):
        self.value = 0
        with open(input_file, "r") as file:
            self._weight, item_count = (int(num) for num in file.readline().split())
            self._items = [None] * item_count
            for index in range(item_count):
                value, weight = (int(num) for num in file.readline().split())
                self._items[index] = Item(value, weight)
        self._compute_value()

    def _compute_value(self):
        self.value = 0
        remaining_weight = self._weight
        for item in self._items:
            if item.weight <= remaining_weight:
                self.value += item.value
                remaining_weight -= item.weight
        return self.value


class Item(tuple):
    __slots__ = []

    def __new__(cls, value, weight):
        return tuple.__new__(cls, (value, weight))

    value = property(itemgetter(0))
    weight = property(itemgetter(1))

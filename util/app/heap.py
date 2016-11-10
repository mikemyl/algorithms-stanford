class IndexedMinHeap:

    def __init__(self, key=lambda x: x, custom_hash=lambda x: x):
        self.key = key
        self.custom_hash = custom_hash
        self._heap = []
        self._item_to_index = {}

    def insert(self, item):
        self._heap.append(item)
        self._item_to_index[self.custom_hash(item)] = len(self._heap) - 1
        self._siftdown(len(self._heap) - 1)

    def contains(self, item):
        if self.custom_hash(item) in self._item_to_index:
            return True

    def value_of(self, item):
        return self.key(self._heap[self._item_to_index[self.custom_hash(item)]])

    def _siftdown(self, position):
        current = position
        item = self._heap[current]
        while current > 0:
            parent = (current - 1) // 2
            if self.key(item) < self.key(self._heap[parent]):
                self._heap[current] = self._heap[parent]
                self._item_to_index[self.custom_hash(self._heap[parent])] = current
                current = parent
            else:
                break
        self._heap[current] = item
        self._item_to_index[self.custom_hash(item)] = current

    def delete(self, item):
        index = self._item_to_index[self.custom_hash(item)]
        del self._item_to_index[self.custom_hash(item)]
        if index == len(self._heap) - 1:
            self._heap.pop()
            return
        self._heap[index] = self._heap.pop()
        self._item_to_index[self.custom_hash(self._heap[index])] = index
        self._siftup(index)
        self._siftdown(index)

    def _siftup(self, index):
        item = self._heap[index]
        current = index
        while 2 * current + 1 < len(self._heap):
            lesser_child = 2 * current + 1
            righ_child = 2 * current + 2
            if righ_child < len(self._heap) and self.key(self._heap[righ_child]) < self.key(self._heap[lesser_child]):
                lesser_child = righ_child
            if self.key(item) > self.key(self._heap[lesser_child]):
                self._heap[current] = self._heap[lesser_child]
                self._item_to_index[self.custom_hash(self._heap[lesser_child])] = current
                current = lesser_child
            else:
                break
        self._heap[current] = item
        self._item_to_index[self.custom_hash(item)] = current

    def pop(self):
        del self._item_to_index[self.custom_hash(self._heap[0])]
        if len(self._heap) > 1:
            item = self._heap[0]
            self._heap[0] = self._heap.pop()
            self._item_to_index[self.custom_hash(self._heap[0])] = 0
            self._siftup(0)
        else:
            item = self._heap.pop()
        return item

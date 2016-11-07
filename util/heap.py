class IndexedMinHeap:

    def __init__(self, key=lambda x: x):
        self.key = key
        self._heap = []
        self._item_to_index = {}

    def insert(self, item):
        self._heap.append(item)
        self._siftdown(len(self._heap) - 1)

    def _siftdown(self, position):
        current = position
        item = self._heap[current]
        while current > 0:
            parent = (current - 1) // 2
            if self.key(item) < self.key(self._heap[parent]):
                self._heap[current] = self._heap[parent]
                self._item_to_index[self._heap[parent]] = current
                current = parent
            else:
                break
        self._heap[current] = item
        self._item_to_index[item] = current

    def delete(self, item):
        index = self._item_to_index[item]
        self._heap[index] = self._heap.pop()
        del self._item_to_index[item]
        self._item_to_index[self._heap[index]] = index
        self._siftup(index)

    def _siftup(self, index):
        item = self._heap[index]
        current = index
        while 2 * current + 1 < len(self._heap):
            lesser_child = 2 * current + 1
            if 2 * current + 2 < len(self._heap) and self.key(self._heap[2 * current + 2]) < self.key(self._heap[lesser_child]):
                lesser_child = 2 * current + 2
            if self.key(item) > self.key(lesser_child):
                self._heap[current], self._heap[lesser_child] = self.key(self._heap[lesser_child]), self._heap[current]
                self._item_to_index[self._heap[current]], self._item_to_index[self._heap[lesser_child]] = current, lesser_child
                current = lesser_child
            else:
                break

    def pop(self):
        del self._item_to_index[self._heap[0]]
        if len(self._heap) > 1:
            item = self._heap[0]
            self._heap[0] = self._heap.pop()
            self._item_to_index[self._heap[0]] = 0
            self._siftup(0)
        else:
            item = self._heap.pop()
        return item


if __name__ == "__main__":
    heap = IndexedMinHeap()
    heap.insert(2)
    heap.insert(3)
    heap.insert(1)
    heap.insert(5)
    heap.insert(6)
    heap.insert(7)
    heap.insert(0)
    heap.insert(9)
    heap.delete(0)
    print(heap.pop())
    print(heap.pop())
    print(heap.pop())
    print(heap.pop())
    print(heap.pop())
    print(heap.pop())
    print(heap.pop())
    print(heap.pop())

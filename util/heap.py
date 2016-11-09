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
            if 2 * current + 2 < len(self._heap) and self.key(self._heap[2 * current + 2]) < self.key(self._heap[lesser_child]):
                lesser_child = 2 * current + 2
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


if __name__ == "__main__":
    #test lient
    heap = IndexedMinHeap(key= lambda x: x[1], custom_hash=lambda x: x[0])
    heap.insert((1,2))
    heap.insert((2,3))
    heap.insert((3,1))
    heap.insert((4,5))
    heap.insert((5,6))
    heap.insert((6,7))
    heap.insert((7,0))
    heap.insert((8,9))
    heap.delete((2,6))
    heap.delete((7,5))
    heap.delete((4,3))
    heap.delete((6,1))
    heap.delete((3,2))
    print(heap.value_of((5,6)))
    print(heap.pop())
    print(heap.pop())
    print(heap.pop())

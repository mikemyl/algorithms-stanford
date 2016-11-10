# Programming Assignment 1 - Greedy algorithms
                             

This programming assignment consist of two tasks. In the first task, we are given [this](app/assignment_1.1.txt) 
list of tasks, where each task has a weight (the first number) and a time (the second number). Our goal is to
schedule these tasks so that the sum of the completion times of the tasks (weight * time_that_was_completed) is 
minimized. We are going to evaluate two greedy algorithms: the first one takes the difference (weight - time),
as the greedy choice, while the second one tasks the ratio (weight / time).

In the second part, we need to implement Prim's MST algorithm for a given graph.


##### Challenges
* Special care needs to be taken in order to handle ties (we need to choose the job with the bigger weight first)
* Implement delete custom element from Heap

Regarding the second challenge #2, a custom implementation of heap was made, so as to support deleting
custom elements from it. The idea is to keep track of the position of each item in the heap. This approach
can be seen below:

```python
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
```

Notice the `key` and `custom_hash` attributes of the `IndexedMinHeap` class. These 2 attributes, when provided
during the construction of the `IndexedMinHeap` allow for custom comparison (e.g `IndexedMinHeap(key= lambda x: -x)` 
implements a Max-Heap) and custom hashing. This custom_hash is needed so as to provide a mechanism to be used
for the mapping of items to keys to our position index so that we retrieve an item's position in the heap.
. In our example, given that we store each edge in a tupple: `(to_vertex, distance)` we used `custom_hash= lambda x: x[0]`,
because we want the name of the vertex to be used as a key, and `key= lambda x: x[1]` because we want an
edge's weight to be used for the comparisons in the heap.

##### Solver:

* [job_scheduler.py](app/job_scheduler.py)
* [prim_mst.py](app/prim_mst.py)

##### Unittests:

* [test_job_scheduler.py](test/test_job_scheduler.py)
* [test_prim_mst.py](test/test_prim_mst.py)
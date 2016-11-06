# Programming Assignment 6.2 - Median Maintainer
                             

In the 6.2 programming assignment we are given [this list](app/assignment_6_2.txt) of numbers
and our goal is to treat this list as a stream, and always maintain the median of these numbers.
This list contains the integers from 1 to 10000 in unsorted order. If `k` is odd, the median is
considered the `(k+1)/2`th.

We should provide the result of the sum of these 10000 medians modulo 10000 (the last 4 digits)

We should utilize 2 heaps: 1 min heap, 1 max heap according to the related course. At each step,
the median will reside either on max of the max heap, or the min of the min heap.

##### Challenges:
* Keep the heaps balanced.
* Implement max-heap in python.

Python's [heapq](https://docs.python.org/3/library/heapq.html) modules does not have a max-heap implementation.
The recommended way to use heapq and implement max-heap in python is by using [key functions](https://wiki.python.org/moin/HowTo/Sorting#Key_Functions):

We could wrap the heapq in our own class, supporting max-heap:

```python
import heapq

class Heap(object):
    def __init__(self, initial=None, key=lambda x: x):
        self.key = key
        if initial:
            self._data = [(key(item), item) for item in initial]
            heapq.heapify(self._data)
        else:
            self._data = []

    def push(self, item):
        heapq.heappush(self._data, (self.key(item), item))

    def pop(self):
        return heapq.heappop(self._data)[1]

    def peek(self):
        return self._data[0][1]

    def __len__(self):
        return len(self._data)
```

Now if we want to create a max-heap, we can provide as key: `lambda x: -x`

##### Solver:

* [median_maintainer.py](app/median_maintainer.py)

##### Unittests:

* [test_median_maintainer](test/test_median_maintainer.py)

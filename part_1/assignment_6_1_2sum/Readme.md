# Programming Assignment 6.1 - Dijkstra Shortest Paths
                             

In the 6.1 programming assignment we are given [this long list](app/assignment_6-1.txt) of numbers
and our goal is to compute the number of values `t` in the interval `[-10000, 10000]` such that there are distinct
numbers x,y that satisfy: `x + y = t`

We need to modify the 2SUM algorithm presented in the course, so as to support range 2SUM computation.

##### Challenges:
* The straightforward solution to the 2SUM problem (e.g traverse the array once and add its items to a set, then
 for each number `x` search for `t-x`) does not apply here - it's slow!
* Employ some clever trick in order to avoid searching in portions of the array that it's guaranteed that there 
will be no target values: sort the array, and adjust the searching window properly by binary searching left 
and right end:

```python
class TwoSumFinder:
    def __init__(self, input_file=None):
        self._array = []
        numbers = set()
        self._target_values = 0
        if input_file is None:
            for number in input().split():
                numbers.add(int(number))
        else:
            with open(input_file) as file:
                for number in file.read().splitlines():
                    numbers.add(int(number))
        self._array = sorted(numbers)
        
    def compute_values(self):
        target_values = set()
        for num in self._array:
            low = bisect_left(self._array, -10000 - num)
            high = bisect_right(self._array, 10000 - num)
            for pair_num in self._array[low:high]:
                if pair_num != num:
                    target_values.add(num + pair_num)
        return len(target_values)
```

##### Solver:

* [two_sum_finder.py](app/two_sum_finder.py)

##### Unittests:

* [test_2sum_finder.py](test/test_2sum_finder.py)

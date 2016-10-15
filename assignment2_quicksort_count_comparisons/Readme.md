# Programming Assignment 1 - Inversions Calculator
                             

In this first programming assignment we are given [this](app/assignment_2.txt) long list of integers
and our goal is to sort them using quick sort. More specifically, we should evaluate three different
choices for the pivot element of the partition subroutine:
- Use the first element as the pivot
- Use the last element
- Use the median of the three (first-middle-last) 

and then calculate the number of comparisons made for each pivot strategy.

The quicksort algorithm is as simple as that (using the first element as the pivot):
```python
class QuickSorter(object):
    def sort(self):
        if len(self._array) <= 1:
            return
        self._qsort(0, len(self._array) - 1)

    def _qsort(self, start, end):
        if start >= end:
            return
        pivot = self.partition(start, end)
        self._qsort(start, pivot - 1)
        self._qsort(pivot + 1, end)

    def partition(self, start, end):
        self._comparisons += end - start
        pivot = start
        for i in range(start + 1, end + 1):
            if self._array[i] < self._array[start]:
                pivot += 1
                self._array[i], self._array[pivot] = self._array[pivot], self._array[i]
        self._array[start], self._array[pivot] = self._array[pivot], self._array[start]
        return pivot
```
Regarding the other 2 pivot choices, we could just swap the {median,last} element with the first, and use the partition
method.

We could make use of the inheritance here, in order to reuse this code:

```python
class QuickSorterFirstElementPivot(QuickSorter):
    def partition(self, start, end):
        return super(QuickSorterFirstElementPivot, self).partition(start, end)


class QuickSorterLastElementPivot(QuickSorter):
    def partition(self, start, end):
        self._array[start], self._array[end] = self._array[end], self._array[start]
        return super(QuickSorterLastElementPivot, self).partition(start, end)


class QuickSorterMedianElementPivot(QuickSorter):
    def partition(self, start, end):
        self._choose_median_pivot(start, end)
        return super(QuickSorterMedianElementPivot, self).partition(start, end)

    def _choose_median_pivot(self, start, end):
        length = end - start + 1
        median_index = length // 2 - 1 if length % 2 == 0 else length // 2
        median = start + median_index
        if self._array[start] <= self._array[median] <= self._array[end] or self._array[end] <= self._array[median] <= \
                self._array[start]:
            self._array[start], self._array[median] = self._array[median], self._array[start]
        elif self._array[median] <= self._array[end] <= self._array[start] or self._array[start] <= self._array[end] <= \
                self._array[median]:
            self._array[start], self._array[end] = self._array[end], self._array[start]
```

Now we can write our solution in an elegant, object-oriented way:

```python
if __name__ == '__main__':
    sorters = (QuickSorterFirstElementPivot('assignment_2.txt'),
               QuickSorterLastElementPivot('assignment_2.txt'),
               QuickSorterMedianElementPivot('assignment_2.txt'))
    for sorter in sorters:
        sorter.sort()
    print(sorters[0].comparisons, sorters[1].comparisons, sorters[2].comparisons)
```

Each sorter is  a `QuickSorter` object, so it inherits the `sort()` method, while each specific-sorter overrides its
own implementation of the partition method


Solver:

* [comparison_counter](app/comparison_counter.py)

Unittests:

* [test_comparison_counter](test/test_comparison_counter.py)
class QuickSorter(object):
    def __init__(self, input_file=None):
        self._comparisons = 0
        self._array = []
        self._inversions = 0
        self.read_input(input_file)

    @property
    def comparisons(self):
        return self._comparisons

    @property
    def array(self):
        return self._array

    @array.setter
    def array(self, arr):
        self._array = arr

    def read_input(self, input_file=None):
        if input_file is None:
            self._array = [int(elem) for elem in input().split()]
            return
        with open(input_file) as numbers:
            for number in numbers:
                self._array.append(int(number))

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

if __name__ == '__main__':
    sorters = (QuickSorterFirstElementPivot('assignment_2.txt'),
               QuickSorterLastElementPivot('assignment_2.txt'),
               QuickSorterMedianElementPivot('assignment_2.txt'))
    for sorter in sorters:
        sorter.sort()
    print(sorters[0].comparisons, sorters[1].comparisons, sorters[2].comparisons)

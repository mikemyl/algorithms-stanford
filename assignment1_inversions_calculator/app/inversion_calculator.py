import sys


class InversionCalculator(object):

    def __init__(self):
        self._array = []
        self._inversions = 0

    @property
    def inversions(self):
        """Return the number of inversions of the given list of numbers"""
        return self._inversions

    @property
    def array(self):
        return self._array

    def read_input(self, input_file=None):
        if input_file is None:
            self._array = [int(elem) for elem in input().split()]
            return
        with open(input_file) as numbers:
            for number in numbers:
                self._array.append(int(number))

    def sort(self, array=None):
        if array is None:
            array = self._array
        return self._merge_sort(array)

    def _merge_sort(self, array):
        if len(array) <= 1:
            return array
        mid = (len(array)) // 2
        first_half = self._merge_sort(array[:mid])
        second_half = self._merge_sort(array[mid:])
        i, j, k = 0, 0, 0
        while j < len(first_half) and k < len(second_half):
            if first_half[j] <= second_half[k]:
                array[i] = first_half[j]
                j += 1
            else:
                array[i] = second_half[k]
                k += 1
                self._inversions += (len(first_half) - j)
            i += 1
        while j < len(first_half):
            array[i] = first_half[j]
            j += 1
            i += 1
        while k < len(second_half):
            array[i] = second_half[k]
            k += 1
            i += 1
        return array

if __name__ == '__main__':
    calculator = InversionCalculator()
    in_file = sys.argv[1] if len(sys.argv) > 1 else None
    calculator.read_input()
    calculator.sort()
    print(calculator.inversions)

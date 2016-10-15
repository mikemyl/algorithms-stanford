# Programming Assignment 1 - Inversions Calculator
                             

In this first programming assignment we are given [this](app/ints.txt) long list of integers
and our goal is to compute the number of inversions in this file. We should print out exactly
the number of these inversions.

The idea is to utilize a sorting algorithm for this task, merge sort in particular. We observe that
each time the merge sub routine fetches a number from the "right" subarray we have an inversion. With
one additional line of code to our merge subroutine, we were able to count these inversions:

```python
    def _merge(self, array, first_half, second_half):
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
```


### Challenges
* Employ this trick to merge sort to count the inversions, so as to avoid the brute-force checking of every pair.


Solver:

* [inversion_calculator.py](app/inversion_calculator.py)

Unittests:

* [test_inversion_calculator.py](test/test_inversion_calculator.py)
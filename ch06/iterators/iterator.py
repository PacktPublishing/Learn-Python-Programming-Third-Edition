# iterators/iterator.py
class OddEven:

    def __init__(self, data):
        self._data = data
        self.indexes = (list(range(0, len(data), 2)) +
                        list(range(1, len(data), 2)))

    def __iter__(self):
        return self

    def __next__(self):
        if self.indexes:
            return self._data[self.indexes.pop(0)]
        raise StopIteration


oddeven = OddEven('ThIsIsCoOl!')
print(''.join(c for c in oddeven))  # TIICO!hssol

oddeven = OddEven('CiAo')  # or manually...
it = iter(oddeven)  # this calls oddeven.__iter__ internally
print(next(it))  # C
print(next(it))  # A
print(next(it))  # i
print(next(it))  # o


# make sure it works correctly with edge cases
oddeven = OddEven('')
print(' '.join(c for c in oddeven))

oddeven = OddEven('A')
print(' '.join(c for c in oddeven))

oddeven = OddEven('Ab')
print(' '.join(c for c in oddeven))

oddeven = OddEven('AbC')
print(' '.join(c for c in oddeven))


"""
$ python iterators/iterator.py
TIICO!hssol
C
A
i
o

A
A b
A C b
"""

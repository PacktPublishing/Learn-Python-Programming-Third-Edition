# lists.py
from math import prod
from operator import itemgetter

# creation
print([])  # empty list
print(list())  # same as []
print([1, 2, 3])  # as with tuples, items are comma separated

print([x + 5 for x in [2, 3, 4]])  # Python is magic
print(list((1, 3, 5, 7, 9)))  # list from a tuple
print(list('hello'))  # list from a string

# main methods
a = [1, 2, 1, 3]
a.append(13)  # we can append anything at the end
print(a)

print(a.count(1))  # how many `1` are there in the list?

a.extend([5, 7])  # extend the list by another (or sequence)
print(a)

print(a.index(13))  # position of `13` in the list (0-based indexing)

a.insert(0, 17)  # insert `17` at position 0
print(a)

a.pop()  # pop (remove and return) last element
print(a)

a.pop(3)  # pop element at position 3
print(a)

a.remove(17)  # remove `17` from the list
print(a)

a.reverse()  # reverse the order of the elements in the list
print(a)

a.sort()  # sort the list
print(a)

a.clear()  # remove all elements from the list
print(a)

# extending
a = list('hello')  # makes a list from a string
print(a)

a.append(100)  # append 100, heterogeneous type
print(a)

a.extend((1, 2, 3))  # extend using tuple
print(a)

a.extend('...')  # extend using string
print(a)

# most common operations
a = [1, 3, 5, 7]
print(min(a))  # minimum value in the list

print(max(a))  # maximum value in the list

print(sum(a))  # sum of all values in the list

print(prod(a))  # product of all values in the list

print(len(a))  # number of elements in the list

b = [6, 7, 8]
print(a + b)  # `+` with list means concatenation

print(a * 2)  # `*` has also a special meaning

# cool sorting
a = [(5, 3), (1, 3), (1, 2), (2, -1), (4, 9)]
print(sorted(a))

print(sorted(a, key=itemgetter(0)))
print(sorted(a, key=itemgetter(0, 1)))
print(sorted(a, key=itemgetter(1)))
print(sorted(a, key=itemgetter(1), reverse=True))

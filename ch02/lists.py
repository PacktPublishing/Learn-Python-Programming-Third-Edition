# lists.py

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
# [1, 2, 1, 3, 13, 5, 7]
# >>> a.index(13)  # position of `13` in the list (0-based indexing)
# 4
# >>> a.insert(0, 17)  # insert `17` at position 0
# >>> a
# [17, 1, 2, 1, 3, 13, 5, 7]
# >>> a.pop()  # pop (remove and return) last element
# 7
# >>> a.pop(3)  # pop element at position 3
# 1
# >>> a
# [17, 1, 2, 3, 13, 5]
# >>> a.remove(17)  # remove `17` from the list
# >>> a
# [1, 2, 3, 13, 5]
# >>> a.reverse()  # reverse the order of the elements in the list
# >>> a
# [5, 13, 3, 2, 1]
# >>> a.sort()  # sort the list
# >>> a
# [1, 2, 3, 5, 13]
# >>> a.clear()  # remove all elements from the list
# >>> a
# []


# # extending
# >>> a = list('hello')  # makes a list from a string
# >>> a
# ['h', 'e', 'l', 'l', 'o']
# >>> a.append(100)  # append 100, heterogeneous type
# >>> a
# ['h', 'e', 'l', 'l', 'o', 100]
# >>> a.extend((1, 2, 3))  # extend using tuple
# >>> a
# ['h', 'e', 'l', 'l', 'o', 100, 1, 2, 3]
# >>> a.extend('...')  # extend using string
# >>> a
# ['h', 'e', 'l', 'l', 'o', 100, 1, 2, 3, '.', '.', '.']


# # most common operations
# >>> a = [1, 3, 5, 7]
# >>> min(a)  # minimum value in the list
# 1
# >>> max(a)  # maximum value in the list
# 7
# >>> sum(a)  # sum of all values in the list
# 16
# >>> from math import prod
# >>> prod(a)  # product of all values in the list
# 105
# >>> len(a)  # number of elements in the list
# 4
# >>> b = [6, 7, 8]
# >>> a + b  # `+` with list means concatenation
# [1, 3, 5, 7, 6, 7, 8]
# >>> a * 2  # `*` has also a special meaning
# [1, 3, 5, 7, 1, 3, 5, 7]


# # cool sorting
# >>> from operator import itemgetter
# >>> a = [(5, 3), (1, 3), (1, 2), (2, -1), (4, 9)]
# >>> sorted(a)
# [(1, 2), (1, 3), (2, -1), (4, 9), (5, 3)]
# >>> sorted(a, key=itemgetter(0))
# [(1, 3), (1, 2), (2, -1), (4, 9), (5, 3)]
# >>> sorted(a, key=itemgetter(0, 1))
# [(1, 2), (1, 3), (2, -1), (4, 9), (5, 3)]
# >>> sorted(a, key=itemgetter(1))
# [(2, -1), (1, 2), (5, 3), (1, 3), (4, 9)]
# >>> sorted(a, key=itemgetter(1), reverse=True)
# [(4, 9), (5, 3), (1, 3), (1, 2), (2, -1)]

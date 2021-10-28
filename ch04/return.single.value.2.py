# return.single.value.2.py
from functools import reduce
from operator import mul


def factorial(n):
    return reduce(mul, range(1, n + 1), 1)


f5 = factorial(5)  # f5 = 120
print(f5)
print([factorial(k) for k in range(10)])

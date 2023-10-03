# decorators/two.decorators.py
from time import time
from functools import wraps


def measure(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t = time()
        result = func(*args, **kwargs)
        print(func.__name__, 'took:', time() - t)
        return result
    return wrapper


def max_result(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result > 100:
            print(
                f'Result is too big ({result}). '
                'Max allowed is 100.'
            )
        return result
    return wrapper


@measure
@max_result
def cube(n):
    return n ** 3


print(cube(2))
print(cube(5))


"""
$ python two.decorators.py
cube took: 3.0994415283203125e-06
8
Result is too big (125). Max allowed is 100.
cube took: 5.9604644775390625e-06
125
"""

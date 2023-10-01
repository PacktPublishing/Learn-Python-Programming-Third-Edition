# decorators/decorators.factory.py
from functools import wraps


def max_result(threshold):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result > threshold:
                print(
                    f'Result is too big ({result}). '
                    f'Max allowed is {threshold}.'
                )
            return result
        return wrapper
    return decorator


@max_result(75)
def cube(n):
    return n ** 3


@max_result(100)
def square(n):
    return n ** 2


@max_result(1000)
def multiply(a, b):
    return a * b


print(cube(5))


"""
$ python decorators.factory.py
Result is too big (125). Max allowed is 75.
125
"""

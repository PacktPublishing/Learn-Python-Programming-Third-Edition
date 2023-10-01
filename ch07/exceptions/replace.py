# exceptions/replace.py
# This is not a valid Python module - Don't run it.
# >>> class NotFoundError(Exception):
# ...     pass
# ...
# >>> vowels = {'a': 1, 'e': 5, 'i': 9, 'o': 15, 'u': 21}
# >>> try:
# ...     pos = vowels['y']
# ... except KeyError as e:
# ...     raise NotFoundError(*e.args)
# ...
# Traceback (most recent call last):
#   File "<stdin>", line 2, in <module>
# KeyError: 'y'

# During handling of the above exception, another exception occurred:

# Traceback (most recent call last):
#   File "<stdin>", line 4, in <module>
# __main__.NotFoundError: y
# >>> try:
# ...     pos = vowels['y']
# ... except KeyError as e:
# ...     raise NotFoundError(*e.args) from e
# ...
# Traceback (most recent call last):
#   File "<stdin>", line 2, in <module>
# KeyError: 'y'

# The above exception was the direct cause of the following exception:

# Traceback (most recent call last):
#   File "<stdin>", line 4, in <module>
# __main__.NotFoundError: y

# dictionary.comprehensions.py
from string import ascii_lowercase
from pprint import pprint


lettermap = {c: k for k, c in enumerate(ascii_lowercase, 1)}
# lettermap = dict((c, k) for k, c in enumerate(ascii_lowercase, 1))


pprint(lettermap)

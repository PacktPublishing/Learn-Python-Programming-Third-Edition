# dictionary.comprehensions.py
from string import ascii_lowercase


lettermap = {c: k for k, c in enumerate(ascii_lowercase, 1)}
# lettermap = dict((c, k) for k, c in enumerate(ascii_lowercase, 1))


from pprint import pprint
pprint(lettermap)

# defaultdict.py
from collections import defaultdict

d = {}
d['age'] = d.get('age', 0) + 1  # age not there, we get 0 + 1
print(d)

d = {'age': 39}
d['age'] = d.get('age', 0) + 1  # age is there, we get 40
print(d)

dd = defaultdict(int)  # int is the default type (0 the value)
dd['age'] += 1  # short for dd['age'] = dd['age'] + 1
print(dd)

# dicts.py

a = dict(A=1, Z=-1)
b = {'A': 1, 'Z': -1}
c = dict(zip(['A', 'Z'], [1, -1]))
d = dict([('A', 1), ('Z', -1)])
e = dict({'Z': -1, 'A': 1})
print(a == b == c == d == e)  # are they all the same?

# zip
print(list(zip(['h', 'e', 'l', 'l', 'o'], [1, 2, 3, 4, 5])))
print(list(zip('hello', range(1, 6))))  # equivalent, more pythonic

# basic
d = {}
d['a'] = 1  # let's set a couple of (key, value) pairs
d['b'] = 2
print(len(d))  # how many pairs?

print(d['a'])  # what is the value of 'a'?

print(d)  # how does `d` look now?
del d['a']  # let's remove `a`
print(d)

d['c'] = 3  # let's add 'c': 3
print('c' in d)  # membership is checked against the keys
print(3 in d)  # not the values
print('e' in d)

d.clear()  # let's clean everything from this dictionary
print(d)

# views
d = dict(zip('hello', range(5)))
print(d)

print(d.keys())
print(d.values())
print(d.items())
print(3 in d.values())

print(('o', 4) in d.items())

# other methods
print(d)
print(d.popitem())  # removes a random item (useful in algorithms)

print(d)
print(d.pop('l'))  # remove item with key `l`
# print(d.pop('not-a-key'))  # remove a key not in dictionary: KeyError
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'not-a-key'

print(d.pop('not-a-key', 'default-value'))  # with a default value?

print(d.update({'another': 'value'}))  # we can update dict this way
print(d.update(a=13))  # or this way (like a function call)
print(d)

print(d.get('a'))  # same as d['a'] but if key is missing no KeyError
print(d.get('a', 177))  # default value used if key is missing

print(d.get('b', 177))  # like in this case
print(d.get('b'))  # key is not there, so None is returned

# setdefault
d = {}
print(d.setdefault('a', 1))  # 'a' is missing, we get default value
print(d)
# {'a': 1}  # also, the key/value pair ('a', 1) has now been added

print(d.setdefault('a', 5))  # let's try to override the value
print(d)
# {'a': 1}  # no override, as expected

# setdefault example
d = {}
d.setdefault('a', {}).setdefault('b', []).append(1)
print(d)

# union
d = {'a': 'A', 'b': 'B'}
e = {'b': 8, 'c': 'C'}
print(d | e)
print(e | d)

print({**d, **e})
print({**e, **d})

d |= e
print(d)
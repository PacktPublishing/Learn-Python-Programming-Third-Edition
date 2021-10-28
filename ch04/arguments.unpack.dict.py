# arguments.unpack.dict.py
def func(a, b, c):
    print(a, b, c)

values = {'b': 1, 'c': 2, 'a': 42}
func(**values)  # equivalent to func(b=1, c=2, a=42)

# arguments.combined.py
def func(a, b, c, d, e, f):
    print(a, b, c, d, e, f)

func(1, *(2, 3), f=6, *(4, 5))
func(*(1, 2), e=5, *(3, 4), f=6)
func(1, **{'b': 2, 'c': 3}, d=4, **{'e': 5, 'f': 6})
func(c=3, *(1, 2), **{'d': 4}, e=5, **{'f': 6})

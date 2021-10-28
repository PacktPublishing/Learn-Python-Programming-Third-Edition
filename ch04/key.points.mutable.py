# key.points.mutable.py
x = [1, 2, 3]
def func(x):
    x[1] = 42  # this affects the `x` argument!

func(x)
print(x)  # prints: [1, 42, 3]

# key.points.mutable.assignment.py
x = [1, 2, 3]


def func(x):
    x[1] = 42  # this changes the original `x` argument!
    x = 'something else'  # this points x to a new string object


func(x)
print(x)  # still prints: [1, 42, 3]

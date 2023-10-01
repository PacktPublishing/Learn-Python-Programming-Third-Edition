# key.points.assignment.py
x = 3


def func(x):
    x = 7  # defining a local x, not changing the global one
    print(x)


func(x)
print(x)  # prints: 3

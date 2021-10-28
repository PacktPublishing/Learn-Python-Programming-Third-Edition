# arguments.positional.keyword.py
def func(a, b, c):
    print(a, b, c)

func(42, b=1, c=2)

func(b=1, c=2, 42)  # positional argument after keyword arguments

"""
$ python arguments.positional.keyword.py
  File "arguments.positional.keyword.py", line 7
    func(b=1, c=2, 42)  # positional argument after keyword arguments
                     ^
SyntaxError: positional argument follows keyword argument
"""

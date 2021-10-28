# parameters.variable.keyword.py
def func(**kwargs):
    print(kwargs)

func(a=1, b=42)  # prints {'a': 1, 'b': 42}
func()  # prints {}
func(a=1, b=46, c=99)  # prints {'a': 1, 'b': 46, 'c': 99}

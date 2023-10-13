# parameters.positional.only.optional.py
def func(a, b=2, /):
    print(a, b)


func(4, 5)  # prints 4 5
func(3)  # prints 3 2

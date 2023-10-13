# parameters.default.py
def func(a, b=4, c=88):
    print(a, b, c)


func(1)              # prints: 1 4 88
func(b=5, a=7, c=9)  # prints: 7 5 9
func(42, c=9)        # prints: 42 4 9
func(42, 43, 44)     # prints: 42, 43, 44

# arguments.multiple.value.py
def func(a, b, c):
    print(a, b, c)


func(2, 3, a=1)

"""
$ python arguments.multiple.value.py
Traceback (most recent call last):
  File "arguments.multiple.value.py", line 5, in <module>
    func(2, 3, a=1)
TypeError: func() got multiple values for argument 'a'
"""

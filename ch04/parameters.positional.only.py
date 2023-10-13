# parameters.positional.only.py
def func(a, b, /, c):
    print(a, b, c)


func(1, 2, 3)  # prints: 1 2 3
func(1, 2, c=3)  # prints 1 2 3
# func(1, b=2, c=3)  # produces the following traceback:

"""
Traceback (most recent call last):
  File "arguments.positional.only.py", line 7, in <module>
    func(1, b=2, c=3)
TypeError: func() got some positional-only arguments
passed as keyword arguments: 'b'
"""

"""
def func_name(positional_only_parameters, /,
    positional_or_keyword_parameters, *,
    keyword_only_parameters):


Valid:

def func_name(p1, p2, /, p_or_kw, *, kw):
def func_name(p1, p2=None, /, p_or_kw=None, *, kw):
def func_name(p1, p2=None, /, *, kw):
def func_name(p1, p2=None, /):
def func_name(p1, p2, /, p_or_kw):
def func_name(p1, p2, /):


Invalid:

def func_name(p1, p2=None, /, p_or_kw, *, kw):
def func_name(p1=None, p2, /, p_or_kw=None, *, kw):
def func_name(p1=None, p2, /):


Why it is useful:

def divmod(a, b, /):
    "Emulate the built in divmod() function"
    return (a // b, a % b)


len(obj='hello')  # The "obj" keyword argument impairs readability
"""


def func_name(name, /, **kwargs):
    print(name)
    print(kwargs)


func_name('Positional-only name', name='Name in **kwargs')
"""
Prints:
Positional-only name
{'name': 'Name in **kwargs'}
"""

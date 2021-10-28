# exceptions/unhandled.py
1 + "one"
print("This line will never be reached")

"""
$ python exceptions/unhandled.py
Traceback (most recent call last):
  File "exceptions/unhandled.py", line 3, in <module>
    1 + "one"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
"""

# pdebugger.py
# d comes from a JSON payload we don't control
d = {'first': 'v1', 'second': 'v2', 'fourth': 'v4'}
# keys also comes from a JSON payload we don't control
keys = ('first', 'second', 'third', 'fourth')

def do_something_with_value(value):
    print(value)

for key in keys:
    do_something_with_value(d[key])

print('Validation done.')

"""
$ python pdebugger.py
v1
v2
Traceback (most recent call last):
  File "pdebugger.py", line 11, in <module>
    do_something_with_value(d[key])
KeyError: 'third'
"""

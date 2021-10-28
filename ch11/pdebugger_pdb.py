# pdebugger_pdb.py
# d comes from a JSON payload we don't control
d = {'first': 'v1', 'second': 'v2', 'fourth': 'v4'}
# keys also comes from a JSON payload we don't control
keys = ('first', 'second', 'third', 'fourth')

def do_something_with_value(value):
    print(value)


import pdb
pdb.set_trace()

# or:
# breakpoint()


for key in keys:
    do_something_with_value(d[key])

print('Validation done.')


"""
$ python pdebugger_pdb.py
[0] > pdebugger_pdb.py(17)<module>()
-> for key in keys:
(Pdb++) l
 17
 18  -> for key in keys:  # breakpoint comes in
 19         do_something_with_value(d[key])
 20

(Pdb++) keys  # inspecting the keys tuple
('first', 'second', 'third', 'fourth')
(Pdb++) d.keys()  # inspecting keys of `d`
dict_keys(['first', 'second', 'fourth'])
(Pdb++) d['third'] = 'placeholder'  # add missing item
(Pdb++) c  # continue
v1
v2
placeholder
v4
Validation done.
"""

# oop/mro.simple.py
class A:
    label = 'a'

class B(A):
    label = 'b'

class C(A):
    label = 'c'

class D(B, C):
    pass

d = D()
print(d.label)  # Hypothetically this could be either 'b' or 'c'
print(d.__class__.mro())  # notice another way to get the MRO
# prints:
# [<class '__main__.D'>, <class '__main__.B'>,
#  <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]


"""
$ python mro.simple.py
b
[
    <class '__main__.D'>, <class '__main__.B'>,
    <class '__main__.C'>, <class '__main__.A'>,
    <class 'object'>
]
"""

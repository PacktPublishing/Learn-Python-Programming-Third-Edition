# oop/mro.py
class A:
    label = 'a'


class B(A):
    pass  # was: label = 'b'


class C(A):
    label = 'c'


class D(B, C):
    pass


d = D()
print(d.label)  # 'c'
print(d.__class__.mro())  # notice another way to get the MRO
# prints:
# [<class '__main__.D'>, <class '__main__.B'>,
#  <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]


"""
$ python oop/mro.py
c
[
    <class '__main__.D'>, <class '__main__.B'>,
    <class '__main__.C'>, <class '__main__.A'>,
    <class 'object'>
]
"""

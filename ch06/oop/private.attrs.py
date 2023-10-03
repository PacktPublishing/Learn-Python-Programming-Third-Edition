# oop/private.attrs.py
class A:
    def __init__(self, factor):
        self._factor = factor

    def op1(self):
        print('Op1 with factor {}...'.format(self._factor))


class B(A):
    def op2(self, factor):
        self._factor = factor
        print('Op2 with factor {}...'.format(self._factor))


obj = B(100)
obj.op1()    # Op1 with factor 100...
obj.op2(42)  # Op2 with factor 42...
obj.op1()    # Op1 with factor 42...  <- This is BAD

print(obj.__dict__.keys())
# dict_keys(['_factor'])


"""
$ python private.attrs.py
Op1 with factor 100...
Op2 with factor 42...
Op1 with factor 42...
dict_keys(['_factor'])
"""

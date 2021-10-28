# oop/private.attrs.fixed.py
class A:
    def __init__(self, factor):
        self.__factor = factor

    def op1(self):
        print('Op1 with factor {}...'.format(self.__factor))

class B(A):
    def op2(self, factor):
        self.__factor = factor
        print('Op2 with factor {}...'.format(self.__factor))


obj = B(100)
obj.op1()    # Op1 with factor 100...
obj.op2(42)  # Op2 with factor 42...
obj.op1()    # Op1 with factor 100...  <- Wohoo! Now it's GOOD!

print(obj.__dict__.keys())
# dict_keys(['_A__factor', '_B__factor'])


"""
$ python private.attrs.fixed.py
Op1 with factor 100...
Op2 with factor 42...
Op1 with factor 100...
dict_keys(['_A__factor', '_B__factor'])
"""

# parameters.keyword.only.py
def kwo(*a, c):
    print(a, c)


kwo(1, 2, 3, c=7)  # prints: (1, 2, 3) 7
kwo(c=4)           # prints: () 4
# kwo(1, 2)  # breaks, invalid syntax, with the following error
# TypeError: kwo() missing 1 required keyword-only argument: 'c'


def kwo2(a, b=42, *, c):
    print(a, b, c)


kwo2(3, b=7, c=99)  # prints: 3 7 99
kwo2(3, c=13)       # prints: 3 42 13
# kwo2(3, 23)  # breaks, invalid syntax, with the following error
# TypeError: kwo2() missing 1 required keyword-only argument: 'c'

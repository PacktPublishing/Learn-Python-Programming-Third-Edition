# numbers.py
from math import pow

# integers
a = 14
b = 3
print(a + b)   # addition
print(a - b)   # subtraction
print(a * b)   # multiplication
print(a / b)   # true division
print(a // b)  # integer division
print(a % b)   # modulo operation (reminder of division)
print(a ** b)  # power operation
print(pow(10, 3))
print(10 ** 3)
print(pow(10, -3))
print(10 ** -3)
print(pow(123, 4))
print(pow(123, 4, 100))
# 41  # notice: 228886641 % 100 == 41

print(pow(37, -1, 43))  # modular inverse of 37 mod 43
# 7

print(7 * 37 % 43)  # proof the above is correct
# 1

# integer and true division
print(7 / 4)  # true division
print(7 // 4)  # integer division, truncation returns 1
print(-7 / 4)  # true division again, result is opposite of previous
print(-7 // 4)  # integer div., result not the opposite of previous

# modulo operator
print(10 % 3)  # remainder of the division 10 // 3
# >>> 10 % 4  # remainder of the division 10 // 4
# 2


# # truncation towards 0
# >>> int(1.75)
# 1
# >>> int(-1.75)
# -1

# # creating ints
# >>> int('10110', base=2)
# 22


# # underscored
# >>> n = 1_024
# >>> n
# 1024
# >>> hex_n = 0x_4_0_0  # 0x400 == 1024
# >>> hex_n
# 1024


# # booleans
# >>> int(True)  # True behaves like 1
# 1
# >>> int(False)  # False behaves like 0
# 0
# >>> bool(1)  # 1 evaluates to True in a boolean context
# True
# >>> bool(-42)  # and so does every non-zero number
# True
# >>> bool(0)  # 0 evaluates to False
# False
# >>> # quick peak at the operators (and, or, not)
# >>> not True
# False
# >>> not False
# True
# >>> True and True
# True
# >>> False or True
# True


# # int and bool
# >>> 1 + True
# 2
# >>> False + 42
# 42
# >>> 7 - True
# 6


# # reals
# >>> pi = 3.1415926536  # how many digits of PI can you remember?
# >>> radius = 4.5
# >>> area = pi * (radius ** 2)
# >>> area
# 63.617251235400005


# # sys.float_info
# >>> import sys
# >>> sys.float_info
# sys.float_info(
#     max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308,
#     min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307,
#     dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2,
#     rounds=1
# )

# # approximation issue
# >>> 0.3 - 0.1 * 3  # this should be 0!!!
# -5.551115123125783e-17


# # complex
# >>> c = 3.14 + 2.73j
# >>> c = complex(3.14, 2.73)  # same as above
# >>> c.real  # real part
# 3.14
# >>> c.imag  # imaginary part
# 2.73
# >>> c.conjugate()  # conjugate of A + Bj is A - Bj
# (3.14-2.73j)
# >>> c * 2  # multiplication is allowed
# (6.28+5.46j)
# >>> c ** 2  # power operation as well
# (2.4067000000000007+17.1444j)
# >>> d = 1 + 1j  # addition and subtraction as well
# >>> c - d
# (2.14+1.73j)


# # fractions
# >>> from fractions import Fraction
# >>> Fraction(10, 6)  # mad hatter?
# Fraction(5, 3)  # notice it's been simplified
# >>> Fraction(1, 3) + Fraction(2, 3)  # 1/3 + 2/3 == 3/3 == 1/1
# Fraction(1, 1)
# >>> f = Fraction(10, 6)
# >>> f.numerator
# 5
# >>> f.denominator
# 3
# >>> f.as_integer_ratio()
# (5, 3)


# # decimal
# >>> from decimal import Decimal as D  # rename for brevity
# >>> D(3.14)  # pi, from float, so approximation issues
# Decimal('3.140000000000000124344978758017532527446746826171875')
# >>> D('3.14')  # pi, from a string, so no approximation issues
# Decimal('3.14')
# >>> D(0.1) * D(3) - D(0.3)  # from float, we still have the issue
# Decimal('2.775557561565156540423631668E-17')
# >>> D('0.1') * D(3) - D('0.3')  # from string, all perfect
# Decimal('0.0')
# >>> D('1.4').as_integer_ratio()  # 7/5 = 1.4 (isn't this cool?!)
# (7, 5)

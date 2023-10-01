# bytearray.py

print(bytearray())  # empty bytearray object

print(bytearray(10))  # zero-filled instance with given length

print(bytearray(range(5)))  # bytearray from iterable of integers

name = bytearray(b'Lina')  # bytearray from bytes
print(name.replace(b'L', b'l'))

print(name.endswith(b'na'))

print(name.upper())

print(name.count(b'L'))

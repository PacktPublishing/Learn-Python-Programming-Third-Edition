# assertions.py
mylist = [1, 2, 3]  # pretend this comes from an external source

assert 4 == len(mylist)  # this will break

for position in range(4):
    print(mylist[position])


"""
$ python assertions.py
Traceback (most recent call last):
  File "assertions.py", line 4, in <module>
    assert 4 == len(mylist)  # this will break
AssertionError
"""

# asserts with message
assert 4 == len(mylist), f"Mylist has {len(mylist)} elements"


"""
$ python assertions.py
Traceback (most recent call last):
  File "assertions.py", line 19, in <module>
    assert 4 == len(mylist), f"Mylist has {len(mylist)} elements"
AssertionError: Mylist has 3 elements
"""

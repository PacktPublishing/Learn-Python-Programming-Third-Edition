# objects.py

# code block # 1
# >>> age = 42
# >>> age
# 42
# >>> age = 43  #A
# >>> age
# 43


# # code block # 2
# >>> age = 42
# >>> id(age)
# 4377553168
# >>> age = 43
# >>> id(age)
# 4377553200


# # code block # 3
# >>> class Person:
# ...     def __init__(self, age):
# ...         self.age = age
# ...
# >>> fab = Person(age=42)
# >>> fab.age
# 42
# >>> id(fab)
# 4380878496
# >>> id(fab.age)
# 4377553168
# >>> fab.age = 25  # I wish!
# >>> id(fab)  # will be the same
# 4380878496
# >>> id(fab.age)  # will be different
# 4377552624

# objects.py

# code block # 1
age = 42
print(age)

age = 43  # A
print(age)

# code block # 2
age = 42
print(id(age))

age = 43
print(id(age))


# code block # 3
class Person:
    def __init__(self, age):
        self.age = age


fab = Person(age=42)
print(fab.age)
print(id(fab))
print(id(fab.age))

fab.age = 25  # I wish!
print(id(fab))  # will be the same
print(id(fab.age))  # will be different

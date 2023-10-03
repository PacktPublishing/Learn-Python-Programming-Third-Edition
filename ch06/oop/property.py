# oop/property.py
class Person:
    def __init__(self, age):
        self.age = age  # anyone can modify this freely


class PersonWithAccessors:
    def __init__(self, age):
        self._age = age

    def get_age(self):
        return self._age

    def set_age(self, age):
        if 18 <= age <= 99:
            self._age = age
        else:
            raise ValueError('Age must be within [18, 99]')


class PersonPythonic:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if 18 <= age <= 99:
            self._age = age
        else:
            raise ValueError('Age must be within [18, 99]')


person = PersonPythonic(39)
print(person.age)  # 39 - Notice we access as data attribute
person.age = 42    # Notice we access as data attribute
print(person.age)  # 42
person.age = 100   # ValueError: Age must be within [18, 99]


"""
$ python property.py
39
42
Traceback (most recent call last):
  File "/Users/fab/srv/lpp3e/v3/ch06/oop/property.py", line 38, in <module>
    person.age = 100   # ValueError: Age must be within [18, 99]
  File "/Users/fab/srv/lpp3e/v3/ch06/oop/property.py", line 32, in age
    raise ValueError('Age must be within [18, 99]')
ValueError: Age must be within [18, 99]
"""

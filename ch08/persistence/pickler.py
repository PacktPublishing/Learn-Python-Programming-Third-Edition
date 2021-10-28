# persistence/pickler.py
import pickle
from dataclasses import dataclass


@dataclass
class Person:
    first_name: str
    last_name: str
    id: int

    def greet(self):
        print(f'Hi, I am {self.first_name} {self.last_name}'
              f' and my ID is {self.id}')


people = [
    Person('Obi-Wan', 'Kenobi', 123),
    Person('Anakin', 'Skywalker', 456),
]


# save data in binary format to a file
with open('data.pickle', 'wb') as stream:
    pickle.dump(people, stream)


# load data from a file
with open('data.pickle', 'rb') as stream:
    peeps = pickle.load(stream)


for person in peeps:
    person.greet()

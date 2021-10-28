# persistence/shelf.py
import shelve


class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id


with shelve.open('shelf1.shelve') as db:
    db['obi1'] = Person('Obi-Wan', 123)
    db['ani'] = Person('Anakin', 456)
    db['a_list'] = [2, 3, 5]
    db['delete_me'] = 'we will have to delete this one...'

    print(list(db.keys()))  # ['ani', 'delete_me', 'a_list', 'obi1']

    del db['delete_me']  # gone!

    print(list(db.keys()))  # ['ani', 'a_list', 'obi1']

    print('delete_me' in db)  # False
    print('ani' in db)  # True

    a_list = db['a_list']
    a_list.append(7)
    db['a_list'] = a_list

    print(db['a_list'])  # [2, 3, 5, 7]


# this way allows writeback:
# working with lists is easier, but consumes more memory and
# closing the file takes longer.
with shelve.open('shelf2.shelve', writeback=True) as db:
    db['a_list'] = [11, 13, 17]
    db['a_list'].append(19)  # in-place append!

    print(db['a_list'])  # [11, 13, 17, 19]

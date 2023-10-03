# persistence/alchemy.py
from alchemy_models import Person, Address, engine
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind=engine)
session = Session()


# Create a couple of people
anakin = Person(name='Anakin Skywalker', age=32)
obi1 = Person(name='Obi-Wan Kenobi', age=40)

# Add email addresses for both of them
obi1.addresses = [
    Address(email='obi1@example.com'),
    Address(email='wanwan@example.com'),
]

# another way: we can simply append
anakin.addresses.append(Address(email='ani@example.com'))
anakin.addresses.append(Address(email='evil.dart@example.com'))
anakin.addresses.append(Address(email='vader@example.com'))

# Add people to the session. This adds addresses too.
session.add(anakin)
session.add(obi1)
session.commit()


# Query and display both
obi1 = session.query(Person).filter(
    Person.name.like('Obi%')
).first()
print(obi1, obi1.addresses)

anakin = session.query(Person).filter(
    Person.name == 'Anakin Skywalker'
).first()
print(anakin, anakin.addresses)

# capture anakin.id
anakin_id = anakin.id

# then remove the var
del anakin


def display_info():
    # get all addresses first
    addresses = session.query(Address).all()

    # display results
    for address in addresses:
        print(f'{address.person.name} <{address.email}>')

    # display how many objects we have in total
    print('people: {}, addresses: {}'.format(
        session.query(Person).count(),
        session.query(Address).count())
    )


display_info()

# Fetch anakin directly by its id
anakin = session.query(Person).get(anakin_id)

# Delete anakin
session.delete(anakin)
session.commit()


# let's do it again and see the changes
display_info()

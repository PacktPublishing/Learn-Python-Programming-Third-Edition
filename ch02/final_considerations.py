# final_considerations.py
a = 1000000
b = 1000000
print(id(a) == id(b))

a = 5
b = 5
print(id(a) == id(b))

# how to choose data structures
# example customer objects
customer1 = {'id': 'abc123', 'full_name': 'Master Yoda'}
customer2 = {'id': 'def456', 'full_name': 'Obi-Wan Kenobi'}
customer3 = {'id': 'ghi789', 'full_name': 'Anakin Skywalker'}

# collect them in a tuple
customers = (customer1, customer2, customer3)

# or collect them in a list
customers = [customer1, customer2, customer3]

# or maybe within a dictionary, they have a unique id after all
customers = {
    'abc123': customer1,
    'def456': customer2,
    'ghi789': customer3,
}

# negative indexing
a = list(range(10))  # `a` has 10 elements. Last one is 9.
print(a)

print(len(a))  # its length is 10 elements
print(a[len(a) - 1])  # position of last one is len(a) - 1

print(a[-1])  # but we don't need len(a)! Python rocks!

print(a[-2])  # equivalent to len(a) - 2
print(a[-3])  # equivalent to len(a) - 3

import pprint

pp = pprint.PrettyPrinter(indent = 4)

n = 3  # integer number
address = "221b Baker Street, NW1 6XE, London"  # Sherlock Holmes' address
employee = {
  'age': 45,
  'role': 'CTO',
  'SSN': 'AB1234567',
}

# let's print them
print(n)
print(address)
pp.pprint(employee)

# other_name
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
# NameError: name 'other_name' is not defined

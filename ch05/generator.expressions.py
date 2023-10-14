# generator.expressions.py
# This is not a valid Python module - Don't run it.


cubes = [k**3 for k in range(10)]  # regular list
print(cubes)
print(type(cubes))

cubes_gen = (k**3 for k in range(10))  # create as generator
print(cubes_gen)
print(type(cubes_gen))

# <class 'generator'>
# >>> list(cubes_gen)  # this will exhaust the generator
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
# >>> list(cubes_gen)  # nothing more to give
# []

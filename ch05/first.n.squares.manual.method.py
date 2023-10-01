# first.n.squares.manual.method.py
def get_squares_gen(n):
    for x in range(n):
        yield x ** 2


squares = get_squares_gen(3)
print(squares.__next__())  # prints: 0
print(squares.__next__())  # prints: 1
print(squares.__next__())  # prints: 4
# the following raises StopIteration, the generator is exhausted,
# any further call to next will keep raising StopIteration
# print(squares.__next__())

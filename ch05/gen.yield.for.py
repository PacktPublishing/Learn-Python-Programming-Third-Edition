# gen.yield.for.py
def print_squares(start, end):
    for n in range(start, end):
        yield n ** 2


for n in print_squares(2, 5):
    print(n)

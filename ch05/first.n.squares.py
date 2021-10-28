# first.n.squares.py
def get_squares(n):  # classic function approach
    return [x ** 2 for x in range(n)]

print(get_squares(10))


def get_squares_gen(n):  # generator approach
    for x in range(n):
        yield x ** 2  # we yield, we don't return

print(list(get_squares_gen(10)))

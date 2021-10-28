# matrix.multiplication.func.py
# this function could also be defined in another module
def matrix_mul(a, b):
    return [[sum(i * j for i, j in zip(r, c)) for c in zip(*b)]
            for r in a]


a = [[1, 2], [3, 4]]
b = [[5, 1], [2, 1]]

c = matrix_mul(a, b)
print(c)

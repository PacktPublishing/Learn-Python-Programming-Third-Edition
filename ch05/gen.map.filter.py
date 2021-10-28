# gen.map.filter.py
# finds the cubes of all multiples of 3 or 5 below N
N = 20

cubes1 = map(
    lambda n: (n, n**3),
    filter(lambda n: n % 3 == 0 or n % 5 == 0, range(N))
)

cubes2 = (
    (n, n**3) for n in range(N) if n % 3 == 0 or n % 5 == 0)

print(list(cubes1))
print(list(cubes2))

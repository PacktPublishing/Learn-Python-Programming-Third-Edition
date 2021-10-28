# pythagorean.triple.generation.for.py
from functions import gcd


def gen_triples(N):
    for m in range(1, int(N**.5) + 1):            # 1
        for n in range(1, m):                     # 2
            if (m - n) % 2 and gcd(m, n) == 1:    # 3
                c = m**2 + n**2                   # 4
                if c <= N:                        # 5
                    a = m**2 - n**2               # 6
                    b = 2 * m * n                 # 7
                    yield (a, b, c)               # 8


triples = sorted(gen_triples(50), key=sum)        # 9
print(triples)

# gen.yield.return.py

def geometric_progression(a, q):
    k = 0
    while True:
        result = a * q**k
        if result <= 100000:
            yield result
        else:
            return
        k += 1


for n in geometric_progression(2, 5):
    print(n)

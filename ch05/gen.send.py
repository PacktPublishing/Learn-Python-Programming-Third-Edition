# gen.send.py
def counter(start=0):
    n = start
    while True:
        result = yield n             # A
        print(type(result), result)  # B
        if result == 'Q':
            break
        n += 1

c = counter()
print(next(c))         # C
print(c.send('Wow!'))  # D
print(next(c))         # E
print(c.send('Q'))     # F

from itertools import count

for n in count(5, 3):
    if n > 20:
        break
    print(n, end=', ')  # instead of newline, comma and space

print()

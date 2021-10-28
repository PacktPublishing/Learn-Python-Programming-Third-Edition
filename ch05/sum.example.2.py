# sum.example.2.py
s = sum([n**2 for n in range(10**9)])  # this is killed
s = sum(n**2 for n in range(10**9))  # this succeeds

print(s)  # prints: 333333332833333333500000000

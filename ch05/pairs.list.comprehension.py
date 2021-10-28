# pairs.list.comprehension.py

items = 'ABCD'
pairs = [(items[a], items[b])
    for a in range(len(items)) for b in range(a, len(items))]

print(pairs)

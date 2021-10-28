# set.comprehensions.py
word = 'Hello'

letters1 = {c for c in word}
letters2 = set(c for c in word)
print(letters1)  # prints: {'H', 'o', 'e', 'l'}
print(letters1 == letters2)  # prints: True

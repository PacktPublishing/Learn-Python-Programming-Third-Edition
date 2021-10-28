# dictionary.comprehensions.positions.py
word = 'Hello'

positions = {c: k for k, c in enumerate(word)}

print(positions)  # prints: {'H': 0, 'e': 1, 'l': 3, 'o': 4}

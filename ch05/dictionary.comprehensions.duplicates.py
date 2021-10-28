# dictionary.comprehensions.duplicates.py
word = 'Hello'

swaps = {c: c.swapcase() for c in word}

print(swaps)  # prints: {'H': 'h', 'e': 'E', 'l': 'L', 'o': 'O'}

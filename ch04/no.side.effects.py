# no.side.effects.py

numbers = [4, 1, 7, 5]
print(sorted(numbers))  # won't sort the original `numbers` list

print(numbers)  # let's verify
# [4, 1, 7, 5]  # good, untouched

numbers.sort()  # this will act on the list
print(numbers)
# [1, 4, 5, 7]

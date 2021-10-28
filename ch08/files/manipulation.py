# files/manipulation.py
from collections import Counter
from string import ascii_letters


chars = ascii_letters + ' '


def sanitize(s, chars):
    return ''.join(c for c in s if c in chars)


def reverse(s):
    return s[::-1]


with open('fear.txt') as stream:
    lines = [line.rstrip() for line in stream]


# let's write the mirrored version of the file
with open('raef.txt', 'w') as stream:
    stream.write('\n'.join(reverse(line) for line in lines))


# now we can calculate some statistics
lines = [sanitize(line, chars) for line in lines]
whole = ' '.join(lines)


# we perform comparisons on the lowercased version of `whole`
cnt = Counter(whole.lower().split())

# we can print the N most common words
print(cnt.most_common(3))

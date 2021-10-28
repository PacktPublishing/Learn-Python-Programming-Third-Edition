# files/open_try.py
fh = open('fear.txt', 'rt')  # r: read, t: text

for line in fh.readlines():
    print(line.strip())  # remove whitespace and print

fh.close()


# secured by try/finally
fh = open('fear.txt', 'rt')

try:
    for line in fh.readlines():
        print(line.strip())

finally:
    fh.close()


# equivalent to:
fh = open('fear.txt')  # rt is default

try:
    for line in fh:  # we can iterate directly on fh
        print(line.strip())

finally:
    fh.close()

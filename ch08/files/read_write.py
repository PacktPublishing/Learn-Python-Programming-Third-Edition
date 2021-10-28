# files/read_write.py
with open('fear.txt') as f:
    lines = [line.rstrip() for line in f]


with open('fear_copy.txt', 'w') as fw:  # w - write
    fw.write('\n'.join(lines))

# files/read_write_bin.py
with open('example.bin', 'wb') as fw:
    fw.write(b'This is binary data...')


with open('example.bin', 'rb') as f:
    print(f.read())  # prints: b'This is binary data...'

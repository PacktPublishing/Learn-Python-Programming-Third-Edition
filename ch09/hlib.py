# hlib.py
# NOT A PYTHON MODULE - DO NOT ATTEMPT TO RUN

# hlib.py
import hashlib

print(hashlib.algorithms_available)
print(hashlib.algorithms_guaranteed)

h = hashlib.blake2b()
h.update(b'Hash me')
h.update(b' now!')

print(h.hexdigest())
print(h.digest())

print(h.block_size)
print(h.digest_size)
print(h.name)

print(hashlib.sha256(b'Hash me now!').hexdigest())

h1 = hashlib.blake2b(b'Important data', digest_size=16, person=b'part-1')
h2 = hashlib.blake2b(b'Important data', digest_size=16, person=b'part-2')

h3 = hashlib.blake2b(b'Important data', digest_size=16)
print(h1.hexdigest())
print(h2.hexdigest())
print(h3.hexdigest())

import os
dk = hashlib.pbkdf2_hmac('sha256', b'Password123', salt=os.urandom(16), iterations=100000)
print(dk.hex())
# 'f8715c37906df067466ce84973e6e52a955be025a59c9100d9183c4cbec27a9e'

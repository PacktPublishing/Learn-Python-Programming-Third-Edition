# secrs/secr_rand.py
import secrets


# utils
print(secrets.choice('Choose one of these words'.split()))

print(secrets.randbelow(10 ** 6))

print(secrets.randbits(32))


# tokens
print(secrets.token_bytes(16))

print(secrets.token_hex(32))

print(secrets.token_urlsafe(32))

# compare digests against timing attacks
secrets.compare_digest('abc123', 'abc123')

"""
$ python secr_rand.py
one
504156
3172492450
b'\xda\x863\xeb\xbb|\x8fk\x9b\xbd\x14Q\xd4\x8d\x15}'
9f90fd042229570bf633e91e92505523811b45e1c3a72074e19bbeb2e5111bf7
bl4qz_Av7QNvPEqZtKsLuTOUsNLFmXW3O03pn50leiY
"""

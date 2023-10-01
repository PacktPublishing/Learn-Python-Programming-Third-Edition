# secrs/secr_gen.py
import secrets
from string import digits, ascii_letters


def generate_pwd(length=8):
    chars = digits + ascii_letters
    return ''.join(secrets.choice(chars) for c in range(length))


def generate_secure_pwd(length=16, upper=3, digits=3):
    if length < upper + digits + 1:
        raise ValueError('Nice try!')

    while True:
        pwd = generate_pwd(length)
        if (any(c.islower() for c in pwd)
            and sum(c.isupper() for c in pwd) >= upper
                and sum(c.isdigit() for c in pwd) >= digits):
            return pwd


print(generate_secure_pwd())
print(generate_secure_pwd(length=3, upper=1, digits=1))

"""
$ python secr_gen.py
nsL5voJnCi7Ote3F
J5e
"""

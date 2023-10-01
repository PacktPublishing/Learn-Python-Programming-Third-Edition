# jwt/token_rsa.py
import jwt
# from cryptography.hazmat.backends import default_backend
# from cryptography.hazmat.primitives import serialization


data = {'payload': 'data'}


def encode(data, priv_filename, algorithm='RS256'):

    with open(priv_filename, 'rb') as key:
        private_key = key.read()

    return jwt.encode(data, private_key, algorithm=algorithm)


def decode(data, pub_filename, algorithm='RS256'):

    with open(pub_filename, 'rb') as key:
        public_key = key.read()

    return jwt.decode(data, public_key, algorithms=[algorithm])


token = encode(data, 'jwt/rsa/key')
data_out = decode(token, 'jwt/rsa/key.pub')
print(data_out)

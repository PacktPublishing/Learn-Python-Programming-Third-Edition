# jwt/tok.py
import jwt


data = {'payload': 'data', 'id': 123456789}
algs = ['HS256', 'HS512']

token = jwt.encode(data, 'secret-key')
data_out = jwt.decode(token, 'secret-key', algorithms=algs)
print(token)
print(data_out)


# decode without verifying the signature
jwt.decode(token, options={'verify_signature': False})


# let's use another algorithm
token512 = jwt.encode(data, 'secret-key', algorithm='HS512')
data_out = jwt.decode(token512, 'secret-key', algorithms=['HS512'])
print(data_out)

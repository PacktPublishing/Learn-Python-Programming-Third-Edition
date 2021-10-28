# secrs/secr_reset.py
import secrets


def get_reset_pwd_url(token_length=16):
    token = secrets.token_urlsafe(token_length)
    return f'https://example.com/reset-pwd/{token}'


print(get_reset_pwd_url())


"""
$ python secr_reset.py
https://example.com/reset-pwd/dfVPEPl_pCkQ8YNV4er-UQ
"""

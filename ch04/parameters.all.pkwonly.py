# parameters.all.pkwonly.py
def allparams(a, /, b,  c=42, *args, d=256, e, **kwargs):
    print('a, b, c:', a, b, c)
    print('d, e:', d, e)
    print('args:', args)
    print('kwargs:', kwargs)

allparams(1, 2, 3, 4, 5, 6, e=7, f=9, g=10)

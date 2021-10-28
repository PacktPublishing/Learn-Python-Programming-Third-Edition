# files/tmp.py
from tempfile import NamedTemporaryFile, TemporaryDirectory


with TemporaryDirectory(dir='.') as td:
    print('Temp directory:', td)
    with NamedTemporaryFile(dir=td) as t:
        name = t.name
        print(name)

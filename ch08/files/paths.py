# files/paths.py
from pathlib import Path


p = Path('fear.txt')

print(p.absolute())
print(p.name)
print(p.parent.absolute())
print(p.suffix)

print(p.parts)
print(p.absolute().parts)

readme_path = p.parent / '..' / '..' / 'README.rst'
print(readme_path.absolute())
print(readme_path.resolve())


"""
/Users/fab/srv/lpp3e/ch08/files/fear.txt
fear.txt
/Users/fab/srv/lpp3e/ch08/files
.txt
('fear.txt',)
('/', 'Users', 'fab', 'srv', 'lpp3e', 'ch08', 'files', 'fear.txt')
/Users/fab/srv/lpp3e/ch08/files/../../README.rst
/Users/fab/srv/lpp3e/README.rst
"""

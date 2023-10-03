# files/existence.py
from pathlib import Path

p = Path('fear.txt')
path = p.parent.absolute()

print(p.is_file())        # True
print(path)               # /Users/fab/srv/lpp3e/ch08/files
print(path.is_dir())      # True

q = Path(path)
print(q.is_dir())         # True

# files/walking.pathlib.py
from pathlib import Path


p = Path('.')

for entry in p.rglob('*'):
    print('File:' if entry.is_file() else 'Folder:', entry)


"""
File: fixed_amount.py
File: existence.py
File: manipulation.py
File: print_file.py
File: read_write_bin.py
File: paths.py
File: open_with.py
File: walking.py
File: tmp.py
File: read_write.py
File: listing.py
File: write_not_exists.py
File: buffer.py
Folder: compression
File: ops_create.py
File: fear.txt
File: open_try.py
File: walking.pathlib.py
Folder: compression/subfolder
File: compression/tar.py
File: compression/content1.txt
File: compression/content2.txt
File: compression/zip.py
File: compression/subfolder/content3.txt
File: compression/subfolder/content4.txt
"""

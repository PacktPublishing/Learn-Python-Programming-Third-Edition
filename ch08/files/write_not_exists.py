# files/write_not_exists.py
import pathlib
file_to_rem = pathlib.Path('write_x.txt')
file_to_rem.unlink()


with open('write_x.txt', 'x') as fw:  # this succeeds
    fw.write('Writing line 1')


# with open('write_x.txt', 'x') as fw:  # this fails
#    fw.write('Writing line 2')

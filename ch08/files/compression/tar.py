# files/compression/tar.py
import tarfile

with tarfile.open('example.tar.gz', 'w:gz') as tar:
    tar.add('content1.txt')
    tar.add('content2.txt')
    tar.add('subfolder/content3.txt')
    tar.add('subfolder/content4.txt')

with tarfile.open('example.tar.gz', 'r:gz') as tar:
    tar.extractall('extract_tar')

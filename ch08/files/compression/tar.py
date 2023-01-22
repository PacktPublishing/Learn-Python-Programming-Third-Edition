# files/compression/tar.py
import tarfile

with tarfile.open('example.tar.gz', 'w:gz') as tar:
    tar.add('content1.txt')
    tar.add('content2.txt')
    tar.add('subfolder/content3.txt')
    tar.add('subfolder/content4.txt')

with tarfile.open('example.tar.gz', 'r:gz') as tar:
    
    import os
    
    def is_within_directory(directory, target):
        
        abs_directory = os.path.abspath(directory)
        abs_target = os.path.abspath(target)
    
        prefix = os.path.commonprefix([abs_directory, abs_target])
        
        return prefix == abs_directory
    
    def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
    
        for member in tar.getmembers():
            member_path = os.path.join(path, member.name)
            if not is_within_directory(path, member_path):
                raise Exception("Attempted Path Traversal in Tar File")
    
        tar.extractall(path, members, numeric_owner=numeric_owner) 
        
    
    safe_extract(tar, "extract_tar")

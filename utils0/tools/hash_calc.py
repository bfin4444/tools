'''
Created on Oct 20, 2020

@author: bfin4
'''

import hashlib
h  = hashlib.sha256()
b  = bytearray(128*1024)
mv = memoryview(b)
with open('C:/Users/bfin4/programing/python/tools/check_sums/data/file4.txt', 'rb', buffering=0) as f:
    for n in iter(lambda : f.readinto(mv), 0):
        h.update(mv[:n])
print(h.hexdigest())
'''
Created on Oct 16, 2020
@author: bfin4
'''
import glob, os, hashlib
from _sha256 import sha256
BUF_SIZE = 65536

# Get and print original check sums from check sum file
d_original_cksums = {}
with open("C:/Users/bfin4/programing/python/tools/check_sums/checksum_reference.txt") as f:
    for line in f:
        (key, val) = line.split()
        d_original_cksums[key] = val
for key in d_original_cksums:
#    print(key, " ", d_original_cksums[key])
    f.close()

# Computes the individual file checksums
d_computed_cksum = {}
for file in glob.glob("/Users/bfin4/programing/python/tools/check_sums/data/*.txt"):
    m  = hashlib.sha256()
    with open(file, 'rb') as f:
         while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            m.update(data)
#             print("{0}".format(m.hexdigest()))
            d_computed_cksum[os.path.basename(file)] = "{0}".format(m.hexdigest())
            print(os.path.basename(file), ' ', d_computed_cksum[os.path.basename(file)])
    f.close()
    
if d_original_cksums == d_computed_cksum:
    print('whooHoo!')
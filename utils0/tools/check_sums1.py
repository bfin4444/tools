'''
Created on Oct 16, 2020

@author: bfin4
'''
from pandas import DataFrame
import glob, os, hashlib
from _sha256 import sha256

check_sum_dir='Users/bfin4/programing/python/tools/check_sums/data/'
check_sum_file='checksum_reference.txt'

# Get and print original check sums from check sum file
d_original_cksums = {}
with open("C:/Users/bfin4/programing/python/tools/check_sums/checksum_reference.txt") as f:
    for line in f:
        (key, val) = line.split()
        d_original_cksums[key] = val
for key in d_original_cksums:
    print(key, " ", d_original_cksums[key])
    f.close()

# Compute and print sha256 checksum

BUF_SIZE = 65536  # lets read stuff in 64kb chunks!

# Note: This computes the cksum for one hash called 'm' and not for each file. It's kind
# of a cumulative effect.
# Good for a zip or tar file
d_computed_cksum = {}
m = hashlib.sha256()
for file in glob.glob("/Users/bfin4/programing/python/tools/check_sums/data/*.txt"):
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
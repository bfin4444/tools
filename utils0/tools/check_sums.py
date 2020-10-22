'''
Created on Oct 16, 2020

@author: bfin4
'''
from pandas import DataFrame
import glob, os, hashlib
from _sha256 import sha256

check_sum_dir='/Users/bfin4/programing/python/tools/check_sums/data/'
check_sum_file='checksum_reference.txt'

d = {}
with open("/Users/bfin4/programing/python/tools/check_sums/data/checksum_reference.txt") as f:
    for line in f:
        (key, val) = line.split()
        d[key] = val
for key in d:
    print(key, " ", d[key])
# BUF_SIZE is totally arbitrary, change for your app!
BUF_SIZE = 65536  # lets read stuff in 64kb chunks!

os.chdir(check_sum_dir)
for file in glob.glob("*.txt"):
    print(file)

m = hashlib.sha256()
for file in glob.glob("*.txt"):
    with open(file, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            m.update(data)
            print(file, "{0}".format(m.hexdigest()))

def sha256sum(filename):
    h  = hashlib.sha256()
    b  = bytearray(128*1024)
    mv = memoryview(b)
    with open(filename, 'rb', buffering=0) as f:
        for n in iter(lambda : f.readinto(mv), 0):
            h.update(mv[:n])
    return h.hexdigest()

if __name__ == '__main__':
    print(sha256sum('/Users/bfin4/programing/python/tools/check_sums/data/file0.txt'))





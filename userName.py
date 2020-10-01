'''
Created on Oct 1, 2020

@author: bfin4
'''
import psutil
pid = int(input('Enter PID'))
p=psutil.Process(pid)
print('User is:', psutil.Process.username(p))
print('Command line name is:', psutil.Process.cmdline(p))
if __name__ == '__main__':
    pass
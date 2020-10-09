'''
Created on Oct 9, 2020

@author: bfin4
'''
import time, win32com.client

shell = win32com.client.Dispatch("WScript.Shell")
shell.AppActivate("Command Prompt")
shell.run("cmd")
# shell2.run("cmd")

shell.AppActivate("cmd")
time.sleep(2)
shell.SendKeys("{ENTER}")
shell.SendKeys("dir{ENTER}")
time.sleep(2)
# shell.SendKeys('^c')
# time.sleep(2)
shell.SendKeys('exit')
time.sleep(1)
shell.SendKeys("{ENTER}")
if __name__ == '__main__':
    pass
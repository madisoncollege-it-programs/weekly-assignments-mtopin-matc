#!/usr/bin/env python3
import subprocess
import string

myProc = subprocess.run(['ps', '-axco', 'command'],stdout=subprocess.PIPE)
print(f'Command Line: {myProc.args}\n')
print(f'Exit Status: {myProc.returncode}\n')
myProcString = myProc.stdout.decode().strip()
# print(f'Output Of Command; {myProcString[1::]}\n')
myProcList = myProcString.split('\n')
# print(f'Output Of Command; {myProcList[1::]}\n')

for i in myProcList:
    print(i)
    
print(f'{len(myProcList[1::])}')
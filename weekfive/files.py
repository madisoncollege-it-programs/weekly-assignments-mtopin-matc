#!/usr/bin/python3
import sys

# Name: Madison Topin
# This Script Will Be For The File Interactions Lab
# The First section Will Read Into A String And Return The Length
# The Second Section Will Read Into A List And Return The Length
# The Third Section Will Read One Line At A Time And Iterate With A Loop Before Returning The Length 

with open("/etc/passwd","r") as hFile:
    strEtcPass = hFile.read()
print(len(strEtcPass))
print("The len() function returns the length of our string strEtcPass")

print("")
print("")

with open("/etc/passwd","r") as hFile:
    listEtcPass = hFile.readlines()
print(len(listEtcPass))
print("The len() function returns the length of our list listEtcPass")

print("")
print("")

with open("/etc/passwd","r") as hFile:
    countLines = 0 
    try:
        while True:
            countLines += len(next(hFile))
    except StopIteration:
        print("Reached The End Of The File")
print(f"The length of the file is: {countLines}")
print('''
    You would  use a loop and iterate 
    instead of a plain read function is 
    for extremely large files
    ''')

#!/usr/bin//env python3
import sys

# Author; Madison Topin
# This Script Will Read A File And Search It For Target Words.
# Then We Will Add Together the Line They Were Each On To Get A Total Line Value
print("Name: Madison Topin")

# Establishing Variables And List
Total = 0
lineNumber = 1
wordList = ["gmeach18@ed.gov",
            "248.253.63.149",
            "Whiteland",
            "80.222.19.190",
            "Kayley",
            "dcassyqw@microsoft.com"]

# Searching For The Words In the List
with open('Midterm-if.txt' , 'r') as hFile:
    next(hFile)
    for line in hFile:
        for currentWord in wordList:
            if  currentWord  in line:
                Total += lineNumber
                print(f"{Total}")
                print(f"Current Line: {lineNumber}")
        lineNumber += 1
print(f"The Total Is: {Total}")

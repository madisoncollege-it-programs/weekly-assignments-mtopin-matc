#!/usr/bin/env python3
import sys


# Author: Madison Topin
# This Script Will Read A File Into A list And Slice It In Several Different Ways
print("Name: Madison Topin")

with open("slicing-file.txt", "r") as myFile:
    myList = myFile.read().splitlines()
    print(f"{myList}")

# Slicing
print("")
print(myList[24:25:])
print(myList[2:5:])
print(myList[-10:-15:-2])
print(myList[10:13:])
print(myList[-19:-22:-1])

# Making The Slices Their Own Strings
print("")
stringOne = " ".join(myList[24:25:])
stringTwo = " ".join(myList[2:5:])
stringThree = " ".join(myList[-10:-15:-2])
stringFour = " ".join(myList[10:13:])
stringFive = " ".join(myList[-19:-22:-1])
print(f"{stringOne}")
print(f"{stringTwo}")
print(f"{stringThree}")
print(f"{stringFour}")
print(f"{stringFive}")

# Joining The Strings To Make The Quote
print("")
myQuote = " ".join([stringOne, stringTwo, stringThree, stringFour, stringFive])
print(f"{myQuote}")


# Unused Code From Testing (I Keep For My Own Reference)
#print(sliceOne)
#joinedSlices = "myString".join(sliceOne, sliceTwo, sliceThree, sliceFour, sliceFive)

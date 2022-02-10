#!/usr/bin/python3
import sys
print("Hello Timmy")

print("")
print("")

varString = "Here is a nice string to slice"
varList = ["Here", "is", "a", "nice", "list", "to", "slice"]

print(f"Slicing The String: {varString}")
print("")
print(varString[3::])
print(varString[:3:])
print(varString[3:12])
print(varString[::2])
print(varString[::-1])

print("")
print("")

print("Slicing The List; {varlist}")
print("")
print(varList[::-1])
print(varList[2::-1])
print(varList[2:4:])
print(varList[::3])
print(varList[1::])

print("")
print("")
print("For Loops:")
print("")
for i in varString:
    print(i)

print("")
print("")

for i in varList:
    print(i)

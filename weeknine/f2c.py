#!/usr/bin/env python3

#  import sys


def Fahrenheit_Celsius(tempF):
    tempC = (tempF - 32) * 5/9
    return tempC


def main():
    myTemp = int(input("Please Input A Temperature In Fahrenheit: "))
    print("Now We Will Convert Your Temperature To Celsius!")
    print(f"The Temperature In Celsius Is: {Fahrenheit_Celsius(myTemp)}")
if __name__ == '__main__':
    main()

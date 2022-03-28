#!/usr/bin/env python3
#  import sys


def Celsius_Fahrenheit(tempC):
    tempF = (tempC * 9/5) + 32
    return tempF


def main():
    myTemp = int(input("Please Input A Temperature In Celsius: "))
    print("Now We Will Convert Your Temperature To Fahrenheit!")
    print(f"The Temperature In Fahrenheit Is: {Celsius_Fahrenheit(myTemp)}")

if __name__ == '__main__':
    main()

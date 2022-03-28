#!/usr/bin/env python3

from f2c import Fahrenheit_Celsius
from c2f import Celsius_Fahrenheit
# import sys


def inputTemp():
    while True:
        try:
            myTemp = int(input("Please Enter A Temperature: "))
            myMeasure = input("Is That Temperature In Fahrenheit? Or Celsius?: ")

            if myMeasure == "Fahrenheit" or myMeasure == "fahrenheit":
                print("Your Temperature Was In Fahrenheit?")
                print("Excellent!")
                print("Now We Will Convert It To Celsius!")
                print(f"{myTemp} Degrees Fahrenheit Is {Fahrenheit_Celsius(myTemp)} Degrees Celsius!")
            elif myMeasure == "Celsius" or myMeasure == "celsius":
                print("Your Temperature Was In Celsius?")
                print("Excellent!")
                print("Now We Will Convert It To Fahrenheit!")
                print(f"{myTemp} Degrees Celsius Is {Celsius_Fahrenheit(myTemp)} Degrees Fahrenheit!")
            elif myMeasure == "Calvin" or myMeasure == "calvin":
                print("I'm Sorry, But This Converter Is Not Currently PRogrammed To Utilize Calvin :(")
            else:
                print(f"I'm Sorry, {myMeasure} Isn't A Valid Unit Of Measurment For Temperature")
            break
        except ValueError:
            print("I'm Sorry, That Is Not A Valid Temperature :(")
            pass
inputTemp()

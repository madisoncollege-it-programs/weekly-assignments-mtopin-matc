#!/usr/bin/env python3

import sys
#print(f"{int(sys.argv[1]) + 50}")

import argparse

parser = argparse.ArgumentParser(description="This Is A Description Of What My Application Does")

##### Most Basic Example
parser.add_argument('-m', dest='BASIC', help='Enter some text')

##### This is how we input an integer of ports
parser.add_argument('-i', '--integer', dest='varInteger', metavar='[an integer]', default=10, type=int, required=False, help='<required> Enter a simple Integer')

##### This is how we input a float
parser.add_argument('-d', '--float', dest='varFloat', metavar='[a float]', default=10.0, type=float, required=False, help='Enter a simple Float')

##### This is how we input a string
parser.add_argument('-s', '--string', dest='varString', metavar='[a string]', default='hello', type=str, required=False, help='Enter a simple String')

##### This is just passing a list to the argument (space delimited set of strings)
parser.add_argument('-l', dest='varList', metavar='[strings]', default=[], nargs='+', required=False, help='Enter a list of strings (space delimited)')

##### This is how we work with Boolean values #####
##### - This is False by default, use ‘-t’ to set it to True
parser.add_argument('-t', '--set-true', dest='bool_t', default=False, action='store_true', required=False, help='Toggle from default False to True')

##### - This is True by default, use ‘-f’ to set it to False
parser.add_argument('-f', '--set-false', dest='bool_f', default=True, action='store_false', required=False, help='Toggle from default True to False')

##### This is how we show the script version ######
parser.add_argument('-v','--version', action='version', version='%(prog)s 1.0')


#Can Use required=True or required=False to require entries from the user. This overrides default and makes it do nothing

input_results = parser.parse_args()
print(input_results)

print(f"Your Integer Is: {input_results.varInteger}\nYour Float Is: {input_results.varFloat}\nYour String Is: {input_results.varString}\nYour List Is: {input_results.varList}\n") 
#Run with -f Madison -l Topin
#Or Run with --help or -h

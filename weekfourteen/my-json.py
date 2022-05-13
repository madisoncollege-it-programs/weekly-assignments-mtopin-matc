#!/usr/bin/env python3

import json
import argparse
import parser
import requests




parser = argparse.ArgumentParser(description="This Is A Description Of What My Application Does")
parser.add_argument('-i', '--ipaddress', dest='varIP', metavar='[An Ip Address]', type=str, required=True, help='<required> Enter An IP Address')

input_results = parser.parse_args()
myVar = input_results.varIP
response = requests.get(f"http://ipinfo.io/{myVar}/json")
myDict = json.loads(response.text)
for key in myDict:
    print(f"{key} : {myDict[key]}")

#print(myDict)
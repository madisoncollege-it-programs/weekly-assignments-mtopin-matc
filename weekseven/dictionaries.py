#!/usr/bin/env python3 
import sys

# Setting up Dictionary -  myDictionary ["FQDN":"IP Address"]

myDictionary = {"server1.testlab.com":"192.168.1.10",
                "server2.testlab.com":"192.168.1.11",
                "server3.testlab.com":"192.168.1.12",
                "server4.testlab.com":"192.168.1.13",
                "server5.testlab.com":"192.168.1.14",
                "server6.testlab.com":"192.168.1.15"}


# Listing The FQDNs:
print("Keys:")
for key in myDictionary.keys():
    print(f"{key}")

# listing The IP Addresses
print(" ")
print("Values:")
for value in myDictionary.values():
    print(f"{value}")

# Listing The Data Pairs
print(" ")
print("(Key, Value) Pairs:")
for item in myDictionary.items():
    print(f"{item}")

# Adding (Key, Value) Pairs To The Dictionary
myDictionary["server7.testlab.com"] = "192.168.1.16"
myDictionary["server8.testlab.com"] = "192.168.1.17"

print(" ")
print("Right Before this Line Printed, Code Was Executed To Add The Next 2 Pairs To The Dictionary")

# Checking If server2 Is Still In The Dictionary And Whether Or Not server10 Exists By Reprinting It
print(" ")
print("(Key, Value) Pairs:")
for item in myDictionary.items():
    print(f"{item}")

# Other Way

# Listing The FQDNs:
# print(f"{myDictionary.keys()}\n")

# listing The IP Addresses
# print(f"{myDictionary.values()}\n")

# Listing The Data Pairs
# print(f"{myDictionary.items()}\n")

# Looks Wonky And Messy When It Prints, Like This

# dict_keys(['server1.testlab.com', 'server2.testlab.com', 'server3.testlab.com', 'ser
# ver4.testlab.com', 'server5.testlab.com', 'server6.testlab.com'])

# dict_values(['192.168.0.10', '192.168.0.11', '192.168.0.12', '192.168.0.13', '192.168.0.14', '192.16
# 8.0.15'])

# dict_items([('server1.testlab.com', '192.168.0.10'), ('server2.testlab.com', '192.168.0.11'), ('serv
# er3.testlab.com', '192.168.0.12'), ('server4.testlab.com', '192.168.0.13'), ('server5.testlab.com', '192.168.0.14'), ('server6.testlab.com', '192.168.0.15')])

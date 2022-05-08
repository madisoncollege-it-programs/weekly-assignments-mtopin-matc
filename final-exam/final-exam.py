#!/usr/bin/env python3

from cgi import parse_header
import http
import sys
import requests
import json
import argparse
import socket
from bs4 import BeautifulSoup

#myVar='172.31.29.252'
varFirstName='Madison'
varLastName='Topin'
#response = requests.get(f"http://{myVar}/q1")
#print(f"{varName}")
#print(f"http://{myVar}/q1")
#print(f"Answer: {response.text}")

def get_Response(myVar):
    response = requests.get(f"http://{myVar}/q1")
    print(f"{varFirstName} {varLastName}")
    print(f"http://{myVar}/q1")
    return response.text
    #print(f"ANSWER: {response.text}")

def parse_String(myVar):
    response = requests.get(f"http://{myVar}/q2")
    soup = BeautifulSoup(response.text, 'html.parser')
    header3 = str(soup.findAll('h3'))
    print(f"{varFirstName} {varLastName}")
    print(f"http://{myVar}/q2")
    appended_header3 = header3[9:26:2] + ' ' + varFirstName
    return appended_header3
    #print(f"ANSWER: {header3[9:26:2]} <{varFirstName}>")

def parse_Header(myVar):
    response = requests.get(f"http://{myVar}/q3")
    print(f"{varFirstName} {varLastName}")
    print(f"http://{myVar}/q3")
    return response.headers['MATC-HEADER']
    #print(f"Answer: {response.headers['MATC-HEADER']}")

def parse_Json(myVar):
    response = requests.get(f"http://{myVar}/q4")
    myDict = json.loads(response.text)['Music And Books'][3]
    print(f"{varFirstName} {varLastName}")
    print(f"http://{myVar}/q4")
    for key in myDict.keys():
        if key == 'publish_info':
            publisherDict = myDict[key]
            for key in publisherDict.keys():
                if key == 'publisher':
                    return publisherDict[key]
                    #print(f'ANSWER: {publisherDict[key]}')

def socket_Client(myVar):
    RHOST           = myVar
    SND_DATA        = 'secret'
    encoded_DATA    = SND_DATA.encode()

    for RPORT in range(5000, 6000):
        try:
            C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            C_SOCK.connect((RHOST, RPORT))
            C_SOCK.send(encoded_DATA)
            RCV_DATA = C_SOCK.recv(1024)
            print(f"{varFirstName} {varLastName}")
            print(f"http://{myVar}/q5")
            return RCV_DATA.decode()
            #print(f'{RCV_DATA.decode()}')
            #print(f'Port {RPORT} Is Open')
            C_SOCK.close()
            break
        except:
            # print(f"Port {RPORT} Is Closed")
            None

#RHOST       = '172.31.29.253'
#SND_DATA    = 'secret'
#encoded_DATA = SND_DATA.encode()

#for RPORT in range(5000, 6000):
    #try:
        #C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #C_SOCK.connect((RHOST, RPORT))
        #C_SOCK.send(encoded_DATA)
        #RCV_DATA = C_SOCK.recv(1024)
        #print(f'{RCV_DATA.decode()}')
         #print(f'Port {RPORT} Is Open')
       # C_SOCK.close()
      #  break
    #except:
     #   None
       # print(f"Port {RPORT} Is Closed")
    
        
#response = requests.get(f"http://{myVar}/q4")
#print(json.dumps(json.loads(response.text),indent=4))
#myDict = json.loads(response.text)['Music And Books'][3]
#print(myDict)
#for key in myDict.keys():
 #   if key == 'publish_info':
  #      publisherDict = myDict[key]
   #     for key in publisherDict.keys():
    #        if key == 'publisher':
     #           print(f'ANSWER: {publisherDict[key]}')

parser = argparse.ArgumentParser(description="This Is A Description Of What My Application Does")

parser.add_argument('-i', '--ipaddress', dest='varIP', metavar='[An Ip Address]', type=str, required=True, help='<required> Enter An IP Address')
parser.add_argument('-f', '--function', dest='varFunction', metavar='[Function Number]', type=int, required=True, help='<required> Enter A Function Number to Call (1, 2, 3, 4, 5)')

input_results = parser.parse_args()
myVar = input_results.varIP
varFunct=input_results.varFunction
#print(input_results)

if varFunct==1:
    print(f'ANSWER: {get_Response(myVar)}')
    #get_Response(myVar)
elif varFunct==2:
    print(f'ANSWER: {parse_String(myVar)}')
    #parse_String(myVar)
elif varFunct==3:
    print(f'ANSWER: {parse_Header(myVar)}')
    #parse_Header(myVar)
elif varFunct==4:
    print(f'ANSWER: {parse_Json(myVar)}')
    #parse_Json(myVar)
elif varFunct==5:
    print(f'ANSWER: {socket_Client(myVar)}')
    #socket_Client(myVar)
else:
    print("Something Went Wrong")
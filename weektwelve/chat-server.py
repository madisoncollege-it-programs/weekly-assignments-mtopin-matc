#!/usr/bin/env python3
import socket

RHOST    = socket.gethostbyname('127.0.0.1') # The target IP address, retrieved by FQDN
#RPORT    = 80 # The target port as used by the server
condition = 0
while condition == 0:
    inputData = input ("Please Enter The Word Exit: ")
    if inputData == "Exit":
        condition = 1
encodedDATA = inputData.encode()
for RPORT in range(5000, 6000):
        try:
            C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            C_SOCK.connect((RHOST, RPORT))
            C_SOCK.send(encodedDATA)
            #RCV_DATA = C_SOCK.recv(1024)
             # This will print out the data returned from the server
            #print(RCV_DATA.decode())
            # close() initiates the socket shutdown sequence
            # client -> server [FIN, ACK]
            # client <- server [FIN, ACK]
            # client -> server [ACK]
            

            break
        except:
            None

# Empty quotes means listen on all available interfaces
LHOST = RHOST
# Arbitrary non-privileged port to listen on             	
LPORT = RPORT
RCV_DATA = encodedDATA  	

L_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
L_SOCK.bind((LHOST, LPORT))

while(1):
    L_SOCK.listen(1)
    L_CONN, addr = L_SOCK.accept()
    print(f'Connected by', RHOST)
    while 1:
        RCV_DATA = L_CONN.recv(1024)
        if not RCV_DATA: break
        print(f"The server received this data:{RCV_DATA}")
        # This line sends the data back to the client
        L_CONN.sendall(RCV_DATA)

    L_CONN.close()
RCV_DATA = C_SOCK.recv(1024)
# This will print out the data returned from the server
print(RCV_DATA.decode())
#!/usr/bin/env python3
import socket

RHOST    = socket.gethostbyname('127.0.0.1') # The target IP address, retrieved by FQDN
#RPORT    = 80 # The target port as used by the server
condition = 0
while condition == 0:
    inputData = input ("Please Enter The Word Exit: ")
    if inputData == "Exit":
        print("Sending Your Word To The Server")
        condition = 1
encodedDATA = inputData.encode()
for RPORT in range(5000, 6000):
        try:
            C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            C_SOCK.connect((RHOST, RPORT))
            C_SOCK.send(encodedDATA)
            RCV_DATA = C_SOCK.recv(1024)
             # This will print out the data returned from the server
            print(RCV_DATA.decode())
            # close() initiates the socket shutdown sequence
            # client -> server [FIN, ACK]
            # client <- server [FIN, ACK]
            # client -> server [ACK]
            C_SOCK.close()

            break
        except:
            None

# The connect() function handles the handshake 
# client -> server [SYN]
# client <- server [SYN,ACK]
# client -> server [ACK]
#C_SOCK.connect((RHOST, RPORT))

# the send() function pushes your SND_DATA variable to the server.
# client -> server [PSH, ACK]
# client <- server [ACK]
#C_SOCK.send(encoded_DATA)

# The recv() function catches data returned (pushed) from the server and stores # it in the RCV_DATA variable.
# client <- server [PSH, ACK]
# client -> server [ACK]
#RCV_DATA = C_SOCK.recv(1024)

# This will print out the data returned from the server
#print(RCV_DATA.decode())

# close() initiates the socket shutdown sequence
# client -> server [FIN, ACK]
# client <- server [FIN, ACK]
# client -> server [ACK]
#C_SOCK.close()

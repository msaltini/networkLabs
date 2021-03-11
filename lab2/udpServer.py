#!/usr/bin/env python3
from socket import *
#For a UDP server all we need to open the socket is the port number. Then we open
#the socket in the same way that we 
serverPort = 5006
serverSocket = socket(AF_INET, SOCK_DGRAM) #AF_INET -> IPv4, SOCK_DGRAM -> UDP socket
#bind is used to assing the port number, serverPort, to the newly created socket
#TODO: add exception handling
serverSocket.bind(('', serverPort))
print("The server is ready to receive packets.")
#In this while loop the server will receive messages from the client and print them.
#The clientAddress value is the tuple for the UDP client, containing the IPv4 and the
#port number.
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    print(message.decode(), clientAddress)
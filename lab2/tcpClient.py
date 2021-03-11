#!/usr/bin/env python3
#TCP client program for Lab 2 Question 2
from socket import *

serverName = '192.168.254.71'
serverPort = 5006
#Like for UDP sockets, we define the socket using the socket function
serverSocket = socket(AF_INET, SOCK_STREAM) #AF_INET -> IPv4, SOCK_STREAM -> TCP
message = "Hello, my name is Matteo and I'm from Modena, Italy."
#For UDP we just send the message to the server, because UDP is a connection less
#protocol, but for TCP we first have to establish a connection. We do this through
#the connect() function. The only parameter is the tuple of the server socket.
#TODO: add exception handling
serverSocket.connect((serverName, serverPort))
serverSocket.send(message.encode())
print('Message sent to server.')
message = serverSocket.recv(2048)
print('The following message was received from the server:\n' + message.decode())
#It is good practice to close the socket in order to avoid any memory leaks.
serverSocket.close()

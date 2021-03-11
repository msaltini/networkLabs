#!/usr/bin/env python3
#UDP client application for Lab 2 question 1
from socket import *
#Here I define the name and the port of the server. The name is usually the IP address
#or the the hostname of the server. Port is how to tell what port to send the data to
serverName = "192.168.254.71"
serverPort = 5006
#The function socket creates a socket and returns that obejct. AF_INET indicates 
#that the socket will communicate over IPv4, and SOCK_DGRAM indicates that it is
#a UDP socket
#TODO: Add exception handling when opening the socket and sending the message
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = "Hello, my name is Matteo and I was born in Modena, Italy."
#sendto sends messages to the socket specified in the tuple passed as an argument.
#The parameters are the econded message, since it can only send bytes over, and the
#tuple.
clientSocket.sendto(message.encode(), (serverName, serverPort))
#close simply closes the socket. it is good practice to close the socket in order 
#to not have memory leaks
clientSocket.close()



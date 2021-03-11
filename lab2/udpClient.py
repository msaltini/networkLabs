#/usr/bin/env python3
#UDP client application for Lab 2 question 1
from socket import *
#Here I define the name and the port of the server. The name is usually the IP address
#or the the hostname of the server. Port is how to tell what port to send the data to
serverName = "192.168.254.71"
serverPort = 5006
#The function socket creates a socket and returns that obejct. AF_INET indicates 
#that the socket will communicate over IPv4, and SOCK_DGRAM indicates that it is
#a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = "Hello, my name is Matteo and I was born in Modena, Italy."

clientSocket.sendto(message.encode(), (serverName, serverPort))
clientSocket.close()



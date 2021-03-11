#/usr/bin/env python3
from socket import *

serverName = '192.168.254.71'
serverPort = 5006

serverSocket = socket(AF_INET, SOCK_STREAM)
message = "Hello, my name is Matteo and I'm from Modena, Italy."

serverSocket.connect((serverName, serverPort))
serverSocket.send(message.encode())
print('Message sent to server.')
message = serverSocket.recv(2048)
print('The following message was received from the server:\n' + message.decode())
serverSocket.close()

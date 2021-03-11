#/usr/bin/env python3
from socket import *

serverPort = 5006
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive packets.")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    print(message.decode())
#/usr/bin/env python3
from socket import *

serverName = "192.168.254.71"
serverPort = 5006

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to receive")

while True:
    connectionSocket, addr = serverSocket.accept()
    message = connectionSocket.recv(1024)
    print('The following message was received from the client:\n' + message.decode())
    connectionSocket.send(message.upper().encode())
    connectionSocket.close()

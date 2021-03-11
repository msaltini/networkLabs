#!/usr/bin/env python3
from socket import *

serverName = "192.168.254.71"
serverPort = 5006
#Same as with the client we define a TCP socket with IPv4 address
serverSocket = socket(AF_INET, SOCK_STREAM)
#bind is used to assign the port number to the socket that we just created
serverSocket.bind(('', serverPort))
#listen is specific to TCP, and it allows the server to accept incoming connections
#The argument is the number of open connections that it can support
serverSocket.listen(1)
print("The server is ready to receive")
#The receiving is almost similar to UDP, except we have to accept a connection. This
#returns the tuple of the connecting socket. We then receive and send back messages to
#that socket
while True:
    connectionSocket, addr = serverSocket.accept()
    message = connectionSocket.recv(1024)
    print('The following message was received from the client:\n' + message.decode())
    connectionSocket.send(message.upper().encode())
    connectionSocket.close()

r'''
Date: 2022-01-27 12:57:37
LastEditors: Kunyang Xie
LastEditTime: 2022-01-27 13:27:04
FilePath: \Assignment1\UDPServer.py
'''

from socket import *
serverPort = 8080
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)

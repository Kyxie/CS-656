r'''
Date: 2022-01-27 13:24:53
LastEditors: Kunyang Xie
LastEditTime: 2022-01-27 15:44:40
FilePath: \Assignment1\UDPClient.py
'''

from socket import *
serverName = 'localhost'
serverPort = 8080
clientSocket = socket(AF_INET, SOCK_DGRAM)  # SOCK_DGRAM表示UDP
message = input('Input lowercase sentence: ')
clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()

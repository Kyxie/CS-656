r'''
Date: 2022-01-27 12:57:49
LastEditors: Kunyang Xie
LastEditTime: 2022-01-27 15:48:47
FilePath: \Assignment1\TCPClient.py
'''

from socket import *
serverName = 'localhost'
serverPort = 8080
clientSocket = socket(AF_INET, SOCK_STREAM)  # SOCK_STREAM表示TCP
clientSocket.connect((serverName, serverPort))
sentence = input('Input lowercase sentence: ')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print(modifiedSentence.decode())
clientSocket.close()

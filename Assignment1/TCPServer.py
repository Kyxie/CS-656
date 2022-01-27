r'''
Date: 2022-01-27 12:57:55
LastEditors: Kunyang Xie
LastEditTime: 2022-01-27 15:26:48
FilePath: \Assignment1\TCPServer.py
'''

from socket import *
serverPort = 8080
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()

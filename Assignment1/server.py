r'''
Date: 2022-01-27 15:29:49
LastEditors: Kunyang Xie
LastEditTime: 2022-01-27 21:37:14
FilePath: \Assignment1\server.py
'''
import sys
from socket import *


class Server:
    def __init__(self, req_code):
        self.req_code = req_code

    def negotiate(self):
        serverPort = 8080
        serverSocket = socket(AF_INET, SOCK_DGRAM)
        serverSocket.bind(('', serverPort))
        print("The server is ready to receive")
        while True:
            message, clientAddress = serverSocket.recvfrom(2048)
            print(message.decode())

    def transaction(self):
        ...


def main():
    # Obtain command
    argv = sys.argv
    req_code = argv[1]
    file_to_send = argv[2]

    server = Server(req_code=req_code)
    server.negotiate()


if __name__ == '__main__':
    main()

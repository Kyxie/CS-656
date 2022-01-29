r'''
Date: 2022-01-27 15:29:49
LastEditors: Kunyang Xie
LastEditTime: 2022-01-29 16:10:16
FilePath: \undefinedd:\Waterloo\term2\CS 656\Assignment\Assignment1\Server\server.py
'''
import sys
import re
import random
import os
from socket import *


class Server:
    def __init__(self, req_code, file_to_send):
        self.req_code = req_code
        self.file_to_send = file_to_send

    def negotiate(self):
        serverPort = 8080
        serverSocket = socket(AF_INET, SOCK_DGRAM)  # Generate UDP
        serverSocket.bind(('', serverPort))
        print('The server is ready to receive')
        while True:
            message, clientAddress = serverSocket.recvfrom(2048)
            # mode: first 4
            mode = message.decode()[:4]

            # Find dash
            dash = re.search(r'/', message.decode())
            # req_code: dash to end
            get_req_code = message.decode()[dash.span()[1]:]
            if get_req_code == self.req_code:
                if mode == 'PORT':
                    # r_port: 5 to dash
                    r_port = int(message.decode()[4:dash.span()[0]])
                elif mode == 'PASV':
                    r_port = random.randint(8000, 8888)
                else:
                    print('Error: Undefined mode')
                    continue
                acknowledgement = '1' + str(r_port)
                serverSocket.sendto(acknowledgement.encode(), clientAddress)
                print('Negotiation stage successful, r_port: ' + str(r_port))
                break
            else:
                acknowledgement = '0'
                serverSocket.sendto(acknowledgement.encode(), clientAddress)
                print('req_code wrong')
                continue
        return r_port

    def transaction(self, r_port):
        serverSocket = socket(AF_INET, SOCK_STREAM)  # Generate TCP
        serverSocket.bind(('', r_port))
        serverSocket.listen(1)
        if os.path.exists(self.file_to_send):
            file = open(self.file_to_send)
            while True:
                connectionSocket, _ = serverSocket.accept()
                connectionSocket.send(file.read().encode())
                file.close()
                connectionSocket.close()
                print('Send successfully' + '\n')
                break
        else:
            print('File "' + self.file_to_send + '" not found')


def main():
    # Obtain command
    argv = sys.argv
    req_code = argv[1]
    file_to_send = argv[2]

    server = Server(req_code=req_code, file_to_send=file_to_send)
    while True:
        r_port = server.negotiate()
        server.transaction(r_port=r_port)


if __name__ == '__main__':
    main()

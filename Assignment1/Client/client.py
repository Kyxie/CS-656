r'''
Date: 2022-01-27 15:30:09
LastEditors: Kunyang Xie
LastEditTime: 2022-01-29 21:19:36
FilePath: \Assignment1\Client\client.py
'''

import sys
from socket import *


class Client:
    def __init__(self, server_address, n_port, mode, req_code, file_received):
        self.server_address = server_address
        self.n_port = n_port
        self.mode = mode
        self.req_code = req_code
        self.flie_received = file_received

    def negotiate(self):
        serverName = self.server_address
        serverPort = int(self.n_port)
        clientSocket = socket(AF_INET, SOCK_DGRAM)  # Generate UDP

        message = ''    # String init
        if self.mode == 'PORT':
            r_port = self.getFreePort()  # Generate r_port
            # Generate message (PORT + r_port + req_code)
            message = 'PORT' + str(r_port) + '/' + self.req_code
        elif self.mode == 'PASV':
            message = 'PASV' + '/' + self.req_code    # PASV + req_code
        else:
            print('Error: Undefined mode')
            exit(0)

        # Send message
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        # Receive, omit serverAddress
        acknowledgement, _ = clientSocket.recvfrom(2048)

        # If receive 0
        if len(acknowledgement.decode()) == 1 and acknowledgement.decode()[0] == '0':
            print('req_code wrong')
        elif acknowledgement.decode()[0] == '1':
            r_port = int(acknowledgement.decode()[1:])  # Success
            print('Negotiation stage successful, r_port: ' + str(r_port))
        clientSocket.close()
        return r_port

    def transaction(self, r_port):
        serverName = self.server_address
        serverPort = r_port
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName, serverPort))
        file = open(self.flie_received, 'w')
        reveive = clientSocket.recv(1024)
        file.write(reveive.decode())
        file.close()
        clientSocket.close()
        print('Reveive successfully')

    def getFreePort(self):
        testSock = socket(AF_INET, SOCK_STREAM)
        testSock.bind(('', 0))
        port = testSock.getsockname()[1]
        testSock.close()
        return port


def main():
    # Obtain command
    argv = sys.argv
    server_address = argv[1]
    n_port = argv[2]
    mode = argv[3]
    req_code = argv[4]
    file_received = argv[5]

    client = Client(server_address=server_address,
                    n_port=n_port, mode=mode, req_code=req_code, file_received=file_received)
    r_port = client.negotiate()
    client.transaction(r_port)


if __name__ == '__main__':
    main()

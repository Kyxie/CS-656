r'''
Date: 2022-01-27 15:30:09
LastEditors: Kunyang Xie
LastEditTime: 2022-01-28 01:04:54
FilePath: \Assignment1\client.py
'''

import sys
import random
from socket import *


class Client:
    def __init__(self, server_address, n_port, mode, req_code):
        self.server_address = server_address
        self.n_port = n_port
        self.mode = mode
        self.req_code = req_code

    def negotiate(self):
        serverName = self.server_address
        serverPort = int(self.n_port)
        clientSocket = socket(AF_INET, SOCK_DGRAM)

        message = ''
        if self.mode == 'PORT':
            r_port = random.randint(8000, 8888)
            print('init r_port = ' + str(r_port))
            message = 'PORT' + str(r_port) + '/' + self.req_code
        elif self.mode == 'PASV':
            message = 'PASV' + self.req_code

        clientSocket.sendto(message.encode(), (serverName, serverPort))
        acknowledgement, _ = clientSocket.recvfrom(2048)
        if len(acknowledgement.decode()) == 1 and acknowledgement.decode()[0] == '0':
            print('req_code wrong')
        elif acknowledgement.decode()[0] == '1':
            r_port = int(acknowledgement.decode()[1:])
        print(r_port)
        clientSocket.close()

    def transaction(self):
        # print(self.server_address)
        ...


def main():
    # Obtain command
    argv = sys.argv
    server_address = argv[1]
    n_port = argv[2]
    mode = argv[3]
    req_code = argv[4]
    file_received = argv[5]

    # generate r_port
    r_port = random.randint(8000, 8888)

    client = Client(server_address=server_address,
                    n_port=n_port, mode=mode, req_code=req_code)
    client.negotiate()
    client.transaction()


if __name__ == '__main__':
    main()

# python client.py localhost 8080 PORT 11 aa

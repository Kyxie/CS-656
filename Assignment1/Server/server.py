r'''
Date: 2022-01-27 15:29:49
LastEditors: Kunyang Xie
LastEditTime: 2022-02-05 15:34:56
FilePath: \Assignment1\Server\server.py
'''
import sys
import re
import os
from socket import *


class Server:
    def __init__(self, req_code: str, file_to_send: str) -> None:
        self.req_code = req_code
        self.file_to_send = file_to_send

    def negotiate(self) -> int:
        serverSocket = socket(AF_INET, SOCK_DGRAM)  # Generate UDP
        serverSocket.bind(('', 0))  # Distribute a free port
        serverPort = serverSocket.getsockname()[1]
        print('SERVER_PORT = ' + str(serverPort))

        while True:
            message, clientAddress = serverSocket.recvfrom(2048)
            # mode: first 4 characters
            mode = message.decode()[:4]

            # Active negotiation message format: "PORT + r_port + '/' + req_code"
            # Find dash
            dash = re.search(r'/', message.decode())
            # req_code: dash to end
            get_req_code = message.decode()[dash.span()[1]:]

            # req_code confirmed
            if get_req_code == self.req_code:
                if mode == 'PORT':
                    # r_port: the fifth character to dash
                    r_port = int(message.decode()[4:dash.span()[0]])
                elif mode == 'PASV':
                    # Generate a free port
                    r_port = self.getFreePort()
                else:
                    print('Error: Undefined mode')
                    continue

                # Feedback to client
                # If req_code success, return '1' + 'r_port'
                acknowledgement = '1' + str(r_port)
                serverSocket.sendto(acknowledgement.encode(), clientAddress)
                print('Negotiation stage successful, r_port: ' + str(r_port))
                serverSocket.close()
                break
            else:
                # req_code fail
                acknowledgement = '0'
                serverSocket.sendto(acknowledgement.encode(), clientAddress)
                print('req_code wrong')
                continue
        return r_port

    def transaction(self, r_port: int) -> None:
        serverSocket = socket(AF_INET, SOCK_STREAM)  # Generate TCP
        serverSocket.bind(('', r_port))
        serverSocket.listen(1)

        # Find file
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

    def getFreePort(self) -> int:
        testSock = socket(AF_INET, SOCK_STREAM)
        testSock.bind(('', 0))
        port = testSock.getsockname()[1]
        testSock.close()
        return port


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

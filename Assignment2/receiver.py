r'''
Date: 2022-03-01 11:02:07
LastEditors: Kunyang Xie
LastEditTime: 2022-03-13 15:53:05
FilePath: \Assignment\Assignment2\receiver.py
'''

import sys
from socket import *
from packet import Packet

finish = False
arrival_log = []


class Log:
    def __init__(self):
        self.arrival_log = []

    def logArrival(self, num):
        self.arrival_log.append(str(num))

    def export(self):
        f = open('arrival.log', 'w+')
        for log in self.arrival_log:
            f.write(str(log) + "\n")
        f.close()


class ReceiveWindow:
    def __init__(self, socket, address, port, file, log):
        self.size = 10
        self.receive_base = 0
        self.receive_map = {}
        self.socket = socket
        self.address = address
        self.port = port
        self.file = file
        self.list = [self.receive_base]
        self.log = log

    def send(self, packet):
        if packet.typ == 2:
            data = Packet(2, packet.seqnum, 0, '').encode()
        else:
            data = Packet(0, packet.seqnum, 0, '').encode()
        print("send :", packet.seqnum)
        self.socket.sendto(
            data, (self.address, self.port))

    def forward(self):
        # Received base packet, so move the receive window
        self.file.write(self.receive_map[self.receive_base])
        del self.receive_map[self.receive_base]
        self.receive_base = (self.receive_base + 1) % 32
        self.list = list(
            range(self.receive_base, self.receive_base + self.size))
        self.list = [index % 32 for index in self.list]

    def move(self):
        # Received base packet, so move the receive window
        while self.receive_map.get(self.receive_base):
            self.forward()

    def run(self):
        global finish
        msg, _ = self.socket.recvfrom(4096)
        packet = Packet(msg)
        packet_type = packet.typ
        seq_num = packet.seqnum
        self.send(packet)
        if packet_type == 1:
            self.log.logArrival(seq_num)
        elif packet_type == 2:
            self.log.logArrival('EOT')
            finish = True
        # New packet
        if seq_num in self.list:
            if not self.receive_map.get(seq_num):
                self.receive_map[seq_num] = packet.data.encode()
                self.move()


def main():
    if len(sys.argv) != 5:
        print("Improper number of arguments")
        exit(1)

    address = sys.argv[1]
    port = int(sys.argv[2])
    data_port = int(sys.argv[3])
    filename = sys.argv[4]

    try:
        file = open(filename, 'wb')
    except IOError:
        print('Unable to open', filename)
        return

    client_udp_sock = socket(AF_INET, SOCK_DGRAM)
    client_udp_sock.bind(('', data_port))
    log = Log()
    receive_window = ReceiveWindow(client_udp_sock, address, port, file, log)

    while not finish:
        receive_window.run()

    log.export()

    file.close()


if __name__ == '__main__':
    main()

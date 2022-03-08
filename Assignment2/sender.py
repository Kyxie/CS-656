r'''
Date: 2022-03-01 09:53:23
LastEditors: Kunyang Xie
LastEditTime: 2022-03-07 23:00:20
FilePath: \Assignment\Assignment2\sender.py
'''

from struct import pack
import sys
from packet import Packet
from socket import *

# Constants
SACK = 0
DATA = 1
EOT = 2
MAX_WINDOW_SIZE = 10
PACKET_CAP = 500

# Global variables
window = 1


def file_to_packet(file_to_send):
    file = open(file_to_send)
    file_content = file.read()
    packet_number = len(file_content) // PACKET_CAP
    packets = []
    pointer = 0

    # For the packet whose length is 500
    for i in range(0, packet_number):
        packets.append(Packet(DATA, i % 32, PACKET_CAP,
                              file_content[pointer: pointer + PACKET_CAP]))
        pointer = pointer + PACKET_CAP

    # For the last packet
    packet_number = len(packets)
    packets.append(Packet(DATA, packet_number % 32,
                          len(file_content) % PACKET_CAP, file_content[pointer:]))

    # For the EOT packet
    packet_number = len(packets)
    packets.append(Packet(EOT, packet_number % 32, 0, ''))
    file.close()
    return packets


def main():
    # Obtain command
    argv = sys.argv
    if len(argv) != 6:
        print('Error: Please enter the correct number of inputs!')
        exit(1)

    host_address = argv[1]
    send_port = argv[2]
    receive_port = argv[3]
    timeout = argv[4]
    file_to_send = argv[5]

    packets = file_to_packet(file_to_send)


if __name__ == '__main__':
    main()

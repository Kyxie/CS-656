r'''
Date: 2022-03-01 09:53:23
LastEditors: Kunyang Xie
LastEditTime: 2022-03-08 16:24:27
FilePath: \Assignment\Assignment2\sender.py
'''

import sys
from packet import Packet
from socket import *
import threading
import time

# Constants
SACK = 0
DATA = 1
EOT = 2
MAX_WINDOW_SIZE = 10
PACKET_CAP = 500

# Global variables
window_size = 1
timer_list = []
timeout = 100


class Timer:
    def __init__(self, tid):
        self.tid = tid
        self.time_start = time.time()

    def is_timeout(self):
        if time.time() - self.time_start >= timeout:
            return True
        else:
            return False

    def reset(self):
        self.time_start = time.time()


def check_window(window_size, timer_list_num):
    if window_size > timer_list_num:
        return True
    else:
        return False


def send(packets, sender_socket, emu_addr, send_port):
    global window_size
    global timer_list

    # Start a new thread for receive SACK
    recv_thread = threading.Thread(target=recv)
    recv_thread.start()


def recv():
    ...


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
    global timeout
    # Obtain command inputs
    argv = sys.argv
    if len(argv) != 6:
        print('Error: Please enter the correct number of inputs!')
        exit(1)

    emu_addr = argv[1]
    send_port = argv[2]
    recv_port = argv[3]
    timeout = argv[4]
    file_to_send = argv[5]

    # Read file to packets
    packets = file_to_packet(file_to_send)

    # Generate a new UDP socket
    sender_socket = socket(AF_INET, SOCK_DGRAM)
    sender_socket.bind(('', recv_port))

    send()


if __name__ == '__main__':
    main()

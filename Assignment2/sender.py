r'''
Date: 2022-03-01 09:53:23
LastEditors: Kunyang Xie
LastEditTime: 2022-03-13 15:56:45
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
lock = threading.Lock()
timeout = 100
log = None
Finish = False
updated = False


class Log:
    def __init__(self):
        self.NLog = []
        self.seqnumLog = []
        self.ackLog = []
        self.timestamp = 0

    def nextTick(self):
        self.timestamp = self.timestamp + 1

    def logN(self, num):
        self.NLog.append("t=" + str(self.timestamp) + " " + str(num))

    def logSeq(self, num):
        self.seqnumLog.append("t=" + str(self.timestamp) + " " + str(num))

    def logAck(self, num):
        self.ackLog.append("t=" + str(self.timestamp) + " " + str(num))

    def export(self):
        file = open('seqnum.log', 'w+')
        for log in self.seqnumLog:
            file.write(str(log) + "\n")
        file.close()

        # ack.log
        file = open('ack.log', 'w+')
        for log in self.ackLog:
            file.write(str(log) + "\n")
        file.close()

        # time.log
        file = open('N.log', 'w+')
        for log in self.NLog:
            file.write(str(log) + "\n")
        file.close()


class SendWindow:
    global lock

    def __init__(self, address, port, segment_list, socket):
        self.send_base = 0
        self.size = 1
        self.list = [self.send_base]
        self.address = address
        self.port = port
        self.segment_list = segment_list
        self.socket = socket
        self.send_EOT = False
        self.updated = False

    def reset(self):
        self.size = 1
        self.list = [self.send_base]

    def increase(self):
        if self.size < 10:
            self.size += 1

    def forward(self):
        self.send_base += 1
        self.list = list(range(self.send_base, min(
            self.send_base + self.size, len(self.segment_list))))
        # EOT
        if(self.send_base == len(self.segment_list)):
            self.list = [self.send_base]

    def send(self, segment):
        data = segment.data.encode()
        self.socket.sendto(
            data, (self.address, self.port))

    def move(self):
        lock.acquire()
        while self.segment_list[self.send_base].finish:
            self.forward()
        lock.release()

    def clear_updated(self):
        if(self.updated == True):
            self.updated = False

    def run(self):
        global lock
        global updated

        for index in list(range(self.send_base, min(self.send_base + MAX_WINDOW_SIZE, len(self.segment_list)))):
            # Timeout occurs
            cur = self.segment_list[index]
            if self.updated == True:
                self.updated = False
                print('New Ack Received, Timer list expires')
                break
            if cur.timer:
                try:
                    if cur.timer.is_timeout():
                        # If timeout
                        self.reset()
                        cur.retry = True
                        cur.clear_timer()
                        lock.acquire()
                        if index == self.send_base:
                            # If the packet is send base
                            self.send(cur)
                            cur.start()
                            log.logN(self.size)
                            log.logSeq(cur.seqnum)
                            log.nextTick()
                            lock.release()
                            break
                        log.logN(self.size)
                        log.nextTick()
                        lock.release()
                except:
                    break
                break
        for index in self.list:
            # Send window
            cur = self.segment_list[index]
            if not cur.finish and (not cur.timer or cur.retry):
                # If the packet did not receive
                if cur.data.typ == 2 and self.send_base == len(self.segment_list) - 1 and not self.send_EOT:
                    self.send(cur)
                    log.logSeq('EOT')
                    self.send_EOT = True
                    break
                elif cur.data.typ == 1:
                    self.send(cur)
                    cur.start()
                    log.logSeq(cur.seqnum)
                    log.nextTick()
                    break


class Segment:
    def __init__(self, id, packet):
        self.id = id
        self.seqnum = id % 32
        self.timer = None
        # Receive ACK
        self.finish = False
        # Need to retransmist
        self.retry = False
        # Packet
        self.data = packet

    def start(self):
        self.timer = Timer(self.id)
        self.retry = False

    def clear_timer(self):
        self.timer = None


class Timer:
    def __init__(self, tid):
        self.tid = tid
        self.time_start = time.time()

    def is_timeout(self):
        if time.time() - self.time_start >= timeout / 1000:
            return True
        else:
            return False

    def reset(self):
        self.time_start = time.time()


def send(send_window, segment_list, log, socket):
    # Start a new thread for receiving SACK
    recv_thread = threading.Thread(
        target=recv, args=(socket, send_window, segment_list, log,))
    recv_thread.start()

    while not Finish:
        send_window.run()


def recv(socket, send_window, segment_list, log):
    global Finish
    global lock
    global updated
    while True:
        packet, _ = socket.recvfrom(4096)
        send_window.updated = True
        packet = Packet(packet)
        seqnum = packet.seqnum
        type = packet.typ
        id = seqnum + ((send_window.send_base // 32) * 32)
        print("recv ack", seqnum)

        if type == 2:
            log.logAck('EOT')
            Finish = True
            break
        # New Ack: Not duplicated
        log.logAck(seqnum)
        if not segment_list[id].finish:
            # Window size +1
            cur = segment_list[id]
            lock.acquire()
            send_window.increase()
            cur.finish = True
            log.logN(send_window.size)
            log.nextTick()
            lock.release()
            send_window.move()
            cur.clear_timer()
            continue
        send_window.move()


def file_to_segments(file_to_send):
    file = open(file_to_send)
    file_content = file.read()
    packet_number = len(file_content) // PACKET_CAP
    segments = []
    pointer = 0

    # For the packet whose length is 500
    for i in range(0, packet_number):
        segments.append(Segment(i,
                                Packet(DATA, i % 32, PACKET_CAP,
                                       file_content[pointer: pointer + PACKET_CAP])))
        pointer = pointer + PACKET_CAP

    # For the last packet
    packet_number = len(segments)
    segments.append(Segment(packet_number,
                            Packet(DATA, packet_number % 32,
                                   len(file_content) % PACKET_CAP, file_content[pointer:])))

    # For the EOT packet
    packet_number = len(segments)
    segments.append(Segment(packet_number, Packet(
        EOT, packet_number % 32, 0, '')))
    file.close()
    return segments


def main():
    global timeout
    global log
    # Obtain command inputs
    argv = sys.argv
    if len(argv) != 6:
        print('Error: Please enter the correct number of inputs!')
        exit(1)

    emu_addr = argv[1]
    send_port = int(argv[2])
    recv_port = int(argv[3])
    timeout = int(argv[4])
    file_to_send = argv[5]

    # Read file to packets
    segment_list = file_to_segments(file_to_send)

    # Generate a new UDP socket
    sender_socket = socket(AF_INET, SOCK_DGRAM)
    sender_socket.bind(('', recv_port))

    # Initialize Send Window
    send_window = SendWindow(emu_addr, send_port, segment_list, sender_socket)

    # Initialize Log
    log = Log()
    log.logN(send_window.size)
    log.nextTick()

    send(send_window, segment_list, log, sender_socket)

    log.export()


if __name__ == '__main__':
    main()

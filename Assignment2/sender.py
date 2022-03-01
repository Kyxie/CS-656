r'''
Date: 2022-03-01 09:53:23
LastEditors: Kunyang Xie
LastEditTime: 2022-03-01 16:15:42
FilePath: \Assignment\Assignment2\Sender\sender.py
'''

import argparse

def main():
    # Obtain command
    parser = argparse.ArgumentParser()
    # Parse parameters
    parser.add_argument('hostAddr', help='host address of the network emulator')
    parser.add_argument(
        'sendPort', help='UDP port number used by the emulator to receive data from the sender')
    parser.add_argument(
        'receivePort', help='UDP port number used by the sender to receive SACKs from the emulator')
    parser.add_argument(
        'timeout', help='timeout interval in units of millisecond')
    parser.add_argument('fileToSend', help='name of the file to be transferred')



if __name__ == '__main__':
    main()

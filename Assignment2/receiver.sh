###
 # @Date: 2022-03-01 11:02:14
 # @LastEditors: Kunyang Xie
 # @LastEditTime: 2022-03-01 11:03:30
 # @FilePath: \Assignment\Assignment2\receiver.sh
###

#Number of parameters: 4
#Parameter:
#    $1: <hostname for the network emulator>
#    $2: <UDP port number used by the link emulator to receive ACKs from the receiver>
#    $3: <UDP port number used by the receiver to receive data from the emulator>
#    $4: <name of the file into which the received data is written>

python3 receiver.py $1 $2 $3 $4
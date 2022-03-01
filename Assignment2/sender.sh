###
 # @Date: 2022-03-01 09:53:32
 # @LastEditors: Kunyang Xie
 # @LastEditTime: 2022-03-01 09:55:35
 # @FilePath: \Assignment\Assignment2\sender.sh
###

#Number of parameters: 5
#Parameter:
#    $1: <host address of the network emulator>
#    $2: <UDP port number used by the emulator to receive data from the sender>
#    $3: <UDP port number used by the sender to receive SACKs from the emulator>
#    $4: <timeout interval in units of millisecond>
#    $5: <name of the file to be transferred>

python3 sender.py $1 $2 $3 $4 $5
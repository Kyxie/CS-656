###
 # @Date: 2022-03-01 11:04:06
 # @LastEditors: Kunyang Xie
 # @LastEditTime: 2022-03-01 11:06:24
 # @FilePath: \Assignment\Assignment2\nEmulator.sh
###

#Number of parameters: 9
#Parameter:
#    $1: <emulator's receiving UDP port number in the forward (sender) direction>
#    $2: <receiver's network address>
#    $3: <receiver's receiving UDP port number>
#    $4: <emulator's receiving UDP port number in the backward (receiver) direction>
#    $5: <sender's network address>
#    $6: <sender's receiving UDP port number>
#    $7: <maximum delay of the link in units of millisecond>
#    $8: <packet discard probability>
#    $9: <verbose-mode>

python3 nEmulator.py $1 $2 $3 $4 $5 $6 $7 $8 $9
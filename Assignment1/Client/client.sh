#!/bin/bash
###
 # @Date: 2017-01-16 13:42:30
 # @LastEditors: Kunyang Xie
 # @LastEditTime: 2022-01-29 22:33:56
 # @FilePath: \Assignment1\Client\client.sh
###

#Run script for client distributed as part of
#Assignment 1
#Computer Networks (CS 456)
#Number of parameters: 5
#Parameter:
#    $1: <server_address>
#    $2: <n_port>
#    $3: <mode>
#    $4: <req_code>
#    $5: <file_received>

#Uncomment/update exactly one of the following commands depending on your implementation

#For Python implementation
python3 client.py $1 $2 $3 $4 $5
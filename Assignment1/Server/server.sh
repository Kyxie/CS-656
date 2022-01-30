#!/bin/bash
###
 # @Date: 2022-01-21 15:28:04
 # @LastEditors: Kunyang Xie
 # @LastEditTime: 2022-01-29 22:34:16
 # @FilePath: \Assignment1\Server\server.sh
###

#Run script for the server distributed as a part of
#Assignment 1
#Computer Networks (CS 456)
#Number of parameters: 2
#Parameter:
#    $1: <req_code>
#    $2: <file_to_send>

#Uncomment/update exactly one of the following commands depending on implementation

#For Python implementation
python3 server.py $1 $2
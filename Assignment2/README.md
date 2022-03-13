## CS 656 Assignment 2

### How to Run

1. Firstly, open a terminal and run the network emulator

```shell
sh nEmulator.sh 9991 localhost 9994 9993 localhost 9992 1 0.2 0
```

2. Then open an another terminal and run the receiver

```shell
sh receiver.sh localhost 9993 9994 output.txt
```

2. Finally run the sender 

```shell
sh sender.sh localhost 9991 9992 50 input.txt
```

### Files

| File Name   | Description               |
| ----------- | ------------------------- |
| input.txt   | File sent by sender       |
| output.txt  | File received by receiver |
| ack.log     | Generated by sender       |
| seqnum.log  | Generated by sender       |
| N.log       | Generated by sender       |
| arrival.log | Generated by receiver     |

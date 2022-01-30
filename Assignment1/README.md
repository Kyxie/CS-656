## CS 656 Assignment 1

### How to run

1. Firstly, open a terminal and run the server.

```shell
# Open the terminal at the root path
cd Server
sh server.sh 11 file_to_send.txt
```

- The *req_code* is **11**, which can be replaced by any other numbers.
- *The  double quotes ("") or single quotes ('') are unnecessary.*
- When the server is running, it will print the *n_port*.

2. Then, do not close the terminal, and open a new terminal to run the client.

```shell
# Open the terminal at the root path
cd Client
sh client.sh localhost n_port PORT 11 file_received.txt
```

- The *server_address* is **localhost**, which can be replaced by any other address.
- *n_port* is the port number printed by server's terminal.
- *Type **PORT** for active mode or **PASV** for passive mode.*
- The *req_code* is **11**, which should be same as server's *req_code*.
- The  double quotes ("") or single quotes ('') are unnecessary.

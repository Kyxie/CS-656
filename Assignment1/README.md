## CS 656 Assignment 1

### Code Details

- Negotiate Stage:

  - Active mode:

    The client will send a binary message, which can be decoded to **'PORT' + str(r_port) + '/' + req_code**, to the server, for example, if the req_code is  11, and r_port is 8080, the client will send **b'PORT8080/11'** to the server, the letter 'b' before the string means binary and same below.

  - Passive mode:

    The client will send a binary message, which can be decoded to **'PASV' + '/' + req_code**, to the server, for example, if the req_code is 11, the client will send **b'PASV/11'** to the server.

  - Server:

    - If the req_code matches successfully, the server will send a binary message **b'1' + 'r_port'**, for example, if the r_port is 8888, server will send **b'18888'**.

    - If unsuccessful, the server will send **b'0'**.

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

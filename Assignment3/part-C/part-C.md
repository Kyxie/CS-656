## Part-C

## 1.

```Shell
POX> INFO:host_tracker:Learned 3 1 00:00:00:00:00:01
INFO:host_tracker:Learned 3 1 00:00:00:00:00:01 got IP 10.0.0.1
INFO:host_tracker:Learned 6 1 00:00:00:00:00:05
INFO:host_tracker:Learned 6 1 00:00:00:00:00:05 got IP 10.0.0.5
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:05.1 -> 00:00:00:00:00:01.3
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:05.1 -> 00:00:00:00:00:01.3
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:05.2 -> 00:00:00:00:00:01.1
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:05.3 -> 00:00:00:00:00:01.1
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:05.3 -> 00:00:00:00:00:01.1
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:01.1 -> 00:00:00:00:00:05.3
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:01.1 -> 00:00:00:00:00:05.3
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:01.1 -> 00:00:00:00:00:05.2
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:01.3 -> 00:00:00:00:00:05.1
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:01.3 -> 00:00:00:00:00:05.1
```



## 2.

```shell
mininet> h1 ping h5
PING 10.0.0.5 (10.0.0.5) 56(84) bytes of data.
64 bytes from 10.0.0.5: icmp_seq=1 ttl=64 time=16.5 ms
64 bytes from 10.0.0.5: icmp_seq=2 ttl=64 time=0.057 ms
64 bytes from 10.0.0.5: icmp_seq=3 ttl=64 time=0.077 ms
64 bytes from 10.0.0.5: icmp_seq=4 ttl=64 time=0.058 ms
64 bytes from 10.0.0.5: icmp_seq=5 ttl=64 time=0.058 ms
```



## 3.

```Shell
mininet@mininet-vm:~/pox$ sudo ovs-ofctl dump-flows s1
 cookie=0x0, duration=79.252s, table=0, n_packets=34, n_bytes=1394, priority=65000,dl_dst=01:23:20:00:00:01,dl_type=0x88cc actions=CONTROLLER:65535
 cookie=0x0, duration=79.237s, table=0, n_packets=0, n_bytes=0, priority=32769,arp,dl_dst=02:00:00:00:be:ef actions=CONTROLLER:65535
```

```shell
mininet@mininet-vm:~/pox$ sudo ovs-ofctl dump-flows s2
 cookie=0x0, duration=2741.150s, table=0, n_packets=1643, n_bytes=67363, priority=65000,dl_dst=01:23:20:00:00:01,dl_type=0x88cc actions=CONTROLLER:65535
 cookie=0x0, duration=2741.133s, table=0, n_packets=0, n_bytes=0, priority=32769,arp,dl_dst=02:00:00:00:be:ef actions=CONTROLLER:65535
```

```Shell
mininet@mininet-vm:~/pox$ sudo ovs-ofctl dump-flows s3
 cookie=0x0, duration=2785.750s, table=0, n_packets=557, n_bytes=22837, priority=65000,dl_dst=01:23:20:00:00:01,dl_type=0x88cc actions=CONTROLLER:65535
 cookie=0x0, duration=2785.706s, table=0, n_packets=0, n_bytes=0, priority=32769,arp,dl_dst=02:00:00:00:be:ef actions=CONTROLLER:65535
```

```Shell
mininet@mininet-vm:~/pox$ sudo ovs-ofctl dump-flows s4
 cookie=0x0, duration=2816.177s, table=0, n_packets=563, n_bytes=23083, priority=65000,dl_dst=01:23:20:00:00:01,dl_type=0x88cc actions=CONTROLLER:65535
 cookie=0x0, duration=2816.144s, table=0, n_packets=0, n_bytes=0, priority=32769,arp,dl_dst=02:00:00:00:be:ef actions=CONTROLLER:65535
```

```Shell
mininet@mininet-vm:~/pox$ sudo ovs-ofctl dump-flows s5
 cookie=0x0, duration=2847.990s, table=0, n_packets=1705, n_bytes=69905, priority=65000,dl_dst=01:23:20:00:00:01,dl_type=0x88cc actions=CONTROLLER:65535
 cookie=0x0, duration=2847.967s, table=0, n_packets=0, n_bytes=0, priority=32769,arp,dl_dst=02:00:00:00:be:ef actions=CONTROLLER:65535
```

```Shell
mininet@mininet-vm:~/pox$ sudo ovs-ofctl dump-flows s6
 cookie=0x0, duration=2904.725s, table=0, n_packets=580, n_bytes=23780, priority=65000,dl_dst=01:23:20:00:00:01,dl_type=0x88cc actions=CONTROLLER:65535
 cookie=0x0, duration=2904.708s, table=0, n_packets=0, n_bytes=0, priority=32769,arp,dl_dst=02:00:00:00:be:ef actions=CONTROLLER:65535
```

```Shell
mininet@mininet-vm:~/pox$ sudo ovs-ofctl dump-flows s7
 cookie=0x0, duration=2932.822s, table=0, n_packets=586, n_bytes=24026, priority=65000,dl_dst=01:23:20:00:00:01,dl_type=0x88cc actions=CONTROLLER:65535
 cookie=0x0, duration=2932.782s, table=0, n_packets=0, n_bytes=0, priority=32769,arp,dl_dst=02:00:00:00:be:ef actions=CONTROLLER:65535
```


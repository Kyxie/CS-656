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

After the network topology is created, the controller first attempts to connect all switches. It will attempt to detect links and create connections between each switch.

When we ping h5 from h1, packet passes s3, S2, S1, S5 and S6 successively. Since ping is bidirectional, there are ten records in total.

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

The first ping takes much longer than the other four pings.

This is because during the first ping, the controller does not know the route of sending the packet from h1 to h5. So the controller needs time to calculate the route.

After rules are installed on the switch, routes do not need to be recalculated, which is saving time.

## 3.

#### S1

Before

```Shell
mininet@mininet-vm:~/pox$ sudo ovs-ofctl dump-flows s1
 cookie=0x0, duration=79.252s, table=0, n_packets=34, n_bytes=1394, priority=65000,dl_dst=01:23:20:00:00:01,dl_type=0x88cc actions=CONTROLLER:65535
 cookie=0x0, duration=79.237s, table=0, n_packets=0, n_bytes=0, priority=32769,arp,dl_dst=02:00:00:00:be:ef actions=CONTROLLER:65535
```

After

```Shell
mininet@mininet-vm:~/pox$ sudo ovs-ofctl dump-flows s1
 cookie=0x0, duration=26.365s, table=0, n_packets=7, n_bytes=574, hard_timeout=1800, priority=65001,dl_src=00:00:00:00:00:05,dl_dst=00:00:00:00:00:01 actions=output:"s1-eth1"
 cookie=0x0, duration=26.360s, table=0, n_packets=6, n_bytes=532, hard_timeout=1800, priority=65001,dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:05 actions=output:"s1-eth2"
 cookie=0x0, duration=139.680s, table=0, n_packets=48, n_bytes=1968, priority=65000,dl_dst=01:23:20:00:00:01,dl_type=0x88cc actions=CONTROLLER:65535
 cookie=0x0, duration=139.638s, table=0, n_packets=0, n_bytes=0, priority=32769,arp,dl_dst=02:00:00:00:be:ef actions=CONTROLLER:65535
```

#### S2

Before

```shell
mininet@mininet-vm:~/pox$ sudo ovs-ofctl dump-flows s2
 cookie=0x0, duration=2741.150s, table=0, n_packets=1643, n_bytes=67363, priority=65000,dl_dst=01:23:20:00:00:01,dl_type=0x88cc actions=CONTROLLER:65535
 cookie=0x0, duration=2741.133s, table=0, n_packets=0, n_bytes=0, priority=32769,arp,dl_dst=02:00:00:00:be:ef actions=CONTROLLER:65535
```

After

```Shell
mininet@mininet-vm:~/pox$ sudo ovs-ofctl dump-flows s2
 cookie=0x0, duration=101.564s, table=0, n_packets=7, n_bytes=574, hard_timeout=1800, priority=65001,dl_src=00:00:00:00:00:05,dl_dst=00:00:00:00:00:01 actions=output:"s2-eth1"
 cookie=0x0, duration=101.561s, table=0, n_packets=6, n_bytes=532, hard_timeout=1800, priority=65001,dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:05 actions=output:"s2-eth3"
 cookie=0x0, duration=214.877s, table=0, n_packets=116, n_bytes=4756, priority=65000,dl_dst=01:23:20:00:00:01,dl_type=0x88cc actions=CONTROLLER:65535
 cookie=0x0, duration=214.834s, table=0, n_packets=0, n_bytes=0, priority=32769,arp,dl_dst=02:00:00:00:be:ef actions=CONTROLLER:65535
```

#### S3

Before

```Shell
mininet@mininet-vm:~/pox$ sudo ovs-ofctl dump-flows s3
 cookie=0x0, duration=2785.750s, table=0, n_packets=557, n_bytes=22837, priority=65000,dl_dst=01:23:20:00:00:01,dl_type=0x88cc actions=CONTROLLER:65535
 cookie=0x0, duration=2785.706s, table=0, n_packets=0, n_bytes=0, priority=32769,arp,dl_dst=02:00:00:00:be:ef actions=CONTROLLER:65535
```

After

```Shell
mininet@mininet-vm:~/pox$ sudo ovs-ofctl dump-flows s3
 cookie=0x0, duration=131.152s, table=0, n_packets=7, n_bytes=574, hard_timeout=1800, priority=65001,dl_src=00:00:00:00:00:05,dl_dst=00:00:00:00:00:01 actions=output:"s3-eth1"
 cookie=0x0, duration=131.150s, table=0, n_packets=6, n_bytes=532, hard_timeout=1800, priority=65001,dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:05 actions=output:"s3-eth3"
 cookie=0x0, duration=244.468s, table=0, n_packets=45, n_bytes=1845, priority=65000,dl_dst=01:23:20:00:00:01,dl_type=0x88cc actions=CONTROLLER:65535
 cookie=0x0, duration=244.427s, table=0, n_packets=0, n_bytes=0, priority=32769,arp,dl_dst=02:00:00:00:be:ef actions=CONTROLLER:65535
```

#### S4

Before

```Shell
mininet@mininet-vm:~/pox$ sudo ovs-ofctl dump-flows s4
 cookie=0x0, duration=2816.177s, table=0, n_packets=563, n_bytes=23083, priority=65000,dl_dst=01:23:20:00:00:01,dl_type=0x88cc actions=CONTROLLER:65535
 cookie=0x0, duration=2816.144s, table=0, n_packets=0, n_bytes=0, priority=32769,arp,dl_dst=02:00:00:00:be:ef actions=CONTROLLER:65535
```

After

```Shell
mininet@mininet-vm:~/pox$ sudo ovs-ofctl dump-flows s4
 cookie=0x0, duration=267.218s, table=0, n_packets=50, n_bytes=2050, priority=65000,dl_dst=01:23:20:00:00:01,dl_type=0x88cc actions=CONTROLLER:65535
 cookie=0x0, duration=267.175s, table=0, n_packets=0, n_bytes=0, priority=32769,arp,dl_dst=02:00:00:00:be:ef actions=CONTROLLER:65535
```

#### S5

Before

```Shell
mininet@mininet-vm:~/pox$ sudo ovs-ofctl dump-flows s5
 cookie=0x0, duration=2847.990s, table=0, n_packets=1705, n_bytes=69905, priority=65000,dl_dst=01:23:20:00:00:01,dl_type=0x88cc actions=CONTROLLER:65535
 cookie=0x0, duration=2847.967s, table=0, n_packets=0, n_bytes=0, priority=32769,arp,dl_dst=02:00:00:00:be:ef actions=CONTROLLER:65535
```

After

```Shell
mininet@mininet-vm:~/pox$ sudo ovs-ofctl dump-flows s5
 cookie=0x0, duration=209.262s, table=0, n_packets=7, n_bytes=574, hard_timeout=1800, priority=65001,dl_src=00:00:00:00:00:05,dl_dst=00:00:00:00:00:01 actions=output:"s5-eth3"
 cookie=0x0, duration=209.255s, table=0, n_packets=6, n_bytes=532, hard_timeout=1800, priority=65001,dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:05 actions=output:"s5-eth1"
 cookie=0x0, duration=322.574s, table=0, n_packets=180, n_bytes=7380, priority=65000,dl_dst=01:23:20:00:00:01,dl_type=0x88cc actions=CONTROLLER:65535
 cookie=0x0, duration=322.530s, table=0, n_packets=0, n_bytes=0, priority=32769,arp,dl_dst=02:00:00:00:be:ef actions=CONTROLLER:65535
```

#### S6

Before

```Shell
mininet@mininet-vm:~/pox$ sudo ovs-ofctl dump-flows s6
 cookie=0x0, duration=2904.725s, table=0, n_packets=580, n_bytes=23780, priority=65000,dl_dst=01:23:20:00:00:01,dl_type=0x88cc actions=CONTROLLER:65535
 cookie=0x0, duration=2904.708s, table=0, n_packets=0, n_bytes=0, priority=32769,arp,dl_dst=02:00:00:00:be:ef actions=CONTROLLER:65535
```

After

```Shell
mininet@mininet-vm:~/pox$ sudo ovs-ofctl dump-flows s6
 cookie=0x0, duration=240.180s, table=0, n_packets=7, n_bytes=574, hard_timeout=1800, priority=65001,dl_src=00:00:00:00:00:05,dl_dst=00:00:00:00:00:01 actions=output:"s6-eth3"
 cookie=0x0, duration=240.171s, table=0, n_packets=6, n_bytes=532, hard_timeout=1800, priority=65001,dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:05 actions=output:"s6-eth1"
 cookie=0x0, duration=353.493s, table=0, n_packets=67, n_bytes=2747, priority=65000,dl_dst=01:23:20:00:00:01,dl_type=0x88cc actions=CONTROLLER:65535
 cookie=0x0, duration=353.451s, table=0, n_packets=0, n_bytes=0, priority=32769,arp,dl_dst=02:00:00:00:be:ef actions=CONTROLLER:65535
```

#### S7

Before

```Shell
mininet@mininet-vm:~/pox$ sudo ovs-ofctl dump-flows s7
 cookie=0x0, duration=2932.822s, table=0, n_packets=586, n_bytes=24026, priority=65000,dl_dst=01:23:20:00:00:01,dl_type=0x88cc actions=CONTROLLER:65535
 cookie=0x0, duration=2932.782s, table=0, n_packets=0, n_bytes=0, priority=32769,arp,dl_dst=02:00:00:00:be:ef actions=CONTROLLER:65535
```

After

```Shell
mininet@mininet-vm:~/pox$ sudo ovs-ofctl dump-flows s7
 cookie=0x0, duration=374.746s, table=0, n_packets=71, n_bytes=2911, priority=65000,dl_dst=01:23:20:00:00:01,dl_type=0x88cc actions=CONTROLLER:65535
 cookie=0x0, duration=374.704s, table=0, n_packets=0, n_bytes=0, priority=32769,arp,dl_dst=02:00:00:00:be:ef actions=CONTROLLER:65535
```

The initial rules are used to let the switches ask controller what is the destination of the packet to be sent.

No, S4 and S7 do not change because when we ping h5 from h1, the route do not pass s4 and s7, so the controller will not change the rules of s4 and s7.

The OVS rule has new fields compare to A1 such as `hart_timeout=1800`, which is used to delete this rule after this time.


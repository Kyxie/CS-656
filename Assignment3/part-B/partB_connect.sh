#!/usr/bin/env bash

# Sets bridge s1 to use OpenFlow 1.3
ovs-vsctl set bridge s1 protocols=OpenFlow13

# Sets bridge s2 to use OpenFlow 1.3
ovs-vsctl set bridge s2 protocols=OpenFlow13

# Sets bridge s3 to use OpenFlow 1.3
ovs-vsctl set bridge s3 protocols=OpenFlow13

# Sets bridge r1 to use OpenFlow 1.3
ovs-vsctl set bridge r1 protocols=OpenFlow13

# Sets bridge r2 to use OpenFlow 1.3
ovs-vsctl set bridge r2 protocols=OpenFlow13

# Print the protocols that each switch supports
for switch in s1 s2 s3 r1 r2;
do
    protos=$(ovs-vsctl get bridge $switch protocols)
    echo "Switch $switch supports $protos"
done

# Avoid having to write "-O OpenFlow13" before all of your ovs-ofctl commands.
ofctl='ovs-ofctl -O OpenFlow13'

# OVS rules for switch 1
$ofctl add-flow s1 \
    in_port=1,actions=output:2
$ofctl add-flow s1 \
    in_port=2,actions=mod_dl_src:0A:00:00:00:01:01,mod_dl_dst:AA:AA:AA:AA:AA:AA,output=1

# OVS rules for switch 2
$ofctl add-flow s2 \
    in_port=1,actions=output:2
$ofctl add-flow s2 \
    in_port=2,actions=output:1,3
$ofctl add-flow s2 \
    in_port=3,actions=output:2

# OVS rules for switch 3
$ofctl add-flow s3 \
    in_port=1,actions=output:2
$ofctl add-flow s3 \
    in_port=2,actions=output:1

# OVS rules for router 1
$ofctl add-flow r1 \
    in_port=1,ip,nw_src=10.1.1.17,nw_dst=10.4.4.48,actions=mod_dl_src:0A:00:00:01:01:02,mod_dl_dst:0A:00:00:00:02:01,output=2
$ofctl add-flow r1 \
    in_port=2,ip,nw_src=10.4.4.48,nw_dst=10.1.1.17,actions=mod_dl_src:0A:00:00:01:01:01,mod_dl_dst:0A:00:00:00:01:02,output=1

# OVS rules for router 2
$ofctl add-flow r2 \
    in_port=1,ip,nw_src=10.4.4.48,nw_dst=10.6.6.69,actions=mod_dl_src:0A:00:00:01:02:02,mod_dl_dst:0A:00:00:00:03:01,output=2
$ofctl add-flow r2 \
    in_port=2,ip,nw_src=10.6.6.69,nw_dst=10.4.4.48,actions=mod_dl_src:0A:00:00:01:02:01,mod_dl_dst:0A:00:00:00:02:03,output=1

# Print the flows installed in each switch
for switch in s1 s2 s3 r1 r2;
do
    echo "Flows installed in $switch:"
    $ofctl dump-flows $switch
    echo ""
done

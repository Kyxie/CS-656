## Explain the meaning of the rule

```shell
$ofctl add-flow s0 \
    in_port=1,ip,nw_src=10.0.0.2,nw_dst=10.0.3.2,actions=mod_dl_src:0A:00:0B:01:00:03,mod_dl_dst:0A:00:0B:FE:00:02,output=3
```

`add-flow s0`: create a rule for `s0`.

`in_port=1`: the input port is 1

`nw_src`: the source ip (`h0`)

`nw_dsw`: the destination ip (`h3`)

`mod_dl_src`: the mac address of output of `s0`

`mod_dl_dst`: the mac address of next input of next node (`s2`)

`output`: output port of `s0`
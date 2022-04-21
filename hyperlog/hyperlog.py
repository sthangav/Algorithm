#!/usr/local/bin/python3

import hyperloglog

hll = hyperloglog.HyperLogLog(0.01)
hll.add("Nuts")
hll.add("bolts")
hll.add("bolts")
print(len(hll))


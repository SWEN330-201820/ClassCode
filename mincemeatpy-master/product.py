#!/usr/bin/env python
import mincemeat

# 1 * 2 * 3 * 4 * 5 * 6
low = 1
high = 50000
#high = 8

data = range(low, high + 1,4)

# The data source can be any dictionary-like object
datasource = dict(enumerate(data))

def mapfn(k, v):
    yield 'product', v * (v + 1) * (v + 2) * (v + 3)

def reducefn(k, vs):
    total = vs[0]
    for i in range(len(vs) -1):
        total *= vs[i+1]
    return total

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
print results

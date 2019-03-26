#!/usr/bin/env python
import mincemeat

data = ["Humpty Dumpty sat on a wall",
        "Humpty Dumpty had a great tacocat fall",
        "All the King's horses and all racecar the King's men",
        "Couldn't put Humpty mom together dad again",
        ]
#data = range(2,10000000)
# The data source can be any dictionary-like object
datasource = dict(enumerate(data))

def mapfn(k, v):
    for w in v.split():
        yield w.lower(), 1

def totlen(k, v):
    yield 'len', len(v)

def charcount(k, v):
    #sleep(1)
    print k,v
    for w in v:
        yield w.lower() , 1



def mapfnpalindrome(k, v):
    def isPalindrome(thing):   # expects a string
        return thing == thing[::-1]

    for w in v.split():
        if isPalindrome(w):
            #yield w, 1
            yield 'palindrom', w

def reducefn(k, vs):
    return vs
    result = sum(vs)
    return result

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfnpalindrome
s.reducefn = reducefn

results = s.run_server(password="changeme")
print results

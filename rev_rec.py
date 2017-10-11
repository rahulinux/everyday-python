#!/usr/bin/env python 

def rev(s):
    if s == "":
        return s
    else:
        print s
        return rev(s[1:]) + s[0]


print rev("abc")

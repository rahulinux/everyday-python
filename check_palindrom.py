#!/usr/bin/env python


def rev(s):
    start = len(s) - 1
    temp = ""
    while start >= 0:
        temp += s[start]
        start = start - 1
    return temp



def check_palindrom(data):
    # This can be simply solve using 
    # return data[::-1] == data
    # But lets solve this without using any built-in help
    return rev(data) == data



print check_palindrom("Rahul")
print check_palindrom("nitin")

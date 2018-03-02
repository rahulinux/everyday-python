#!/usr/bin/env python



def decimal_to_bin(data):
    temp = []
    while data:
        temp.append(data % 2)
        data = data >> 1
    return temp[::-1]

def dec_to_bin_2(n):
    if n<2: return str(n)
    else:
        return dec_to_bin(n/2) + dec_to_bin(n%2)



print decimal_to_bin(11)

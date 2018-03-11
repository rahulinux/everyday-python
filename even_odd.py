#!/usr/bin/env python

"""
input is an array of integers, and you have to reorder its entries so that the even entries appear first
"""

def sortf(arr):
    swap = True
    while swap:
        swap = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
                swap = True
    return arr


def even_odd(arr):

    even = [ i for i in arr if i%2 == 0 ]
    odd = [ i for i in arr if i%2 == 1 ]

    return sortf(even) + sortf(odd)


input_arr = [3,9,1,10,12,4,2,39,34,6]

print even_odd(input_arr)



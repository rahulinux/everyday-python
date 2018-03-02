#!/usr/bin/env python

"""
Write a function - duplicate_items to find the redundant or repeated items in a list and return them in sorted order. 
This method should return a list of redundant integers in ascending sorted order (as illustrated below). 

Examples:
duplicate_items([1, 3, 4, 2, 1]) => [1]

duplicate_items([1, 3, 4, 2, 1, 2, 4]) => [1, 2, 4]
"""

def duplicate_items(list_numbers):
    dup_numbers = []
    list_numbers = sorted(list_numbers)
    for i,a in enumerate(list_numbers):
        if a in list_numbers[:i:-1] and a not in dup_numbers:
            dup_numbers.append(a)
    return dup_numbers


print duplicate_items([1,2,3,1,4,2])


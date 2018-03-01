#!/usr/bin/env python


def find_missing_number(list_numbers,end_number=10):
    # Solution 1#
    #for i in range(1,end_number):
    #   if i not in list_numbers:
    #      return i

    # Solution 2# 
    total_expectation = sum(range(end_number+1))
    return total_expectation - sum(list_numbers)



l = [1,2,3,4,6,7,8,9,10]
print find_missing_number(l)

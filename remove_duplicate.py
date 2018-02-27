#!/usr/loca/env python

"""
Remove duplicate from sorted list
"""

def remove_dup(nums):
   new_array = []
   for i in nums:
      if i not in new_array:
          new_array.append(i)
   return new_array
   


print remove_dup([1,1,2,2,3])

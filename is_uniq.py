#!/usr/bin/env python

"""
implement an algorithm to determine if a string has all uniq characters. 
"""


def is_uniq(input_string):
   input_string = input_string.lower()
   for i in range(len(input_string)-1):
     if input_string[i] in input_string[i+1:]:
        return (input_string,False)
   return (input_string,True)


for s in [ "Linux", "Hadoop", "Neha", "Rahul" ]:
  print is_uniq(s)


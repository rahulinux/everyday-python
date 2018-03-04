#!/usr/bin/env python


def power_of_four(number):
   if number!=None and not(number&(number-1)):
     count = 0
     while number > 1:
       number >>= 1
       count += 1
     return (count%2 ==0)
   return False


for i in range(1,6):
  print power_of_four(i)

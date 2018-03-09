#!/usr/bin/env python

def is_prime(n):
   if n <= 1: 
     return False
   # If number is divedable by 1 and it self 
   # and number dividable by anyother number then 
   # its not prime number 
   for i in range(2,n):
     if n%n == 0 and n%1 == 0 and n%i == 0: 
      return (n,False)
   return (n,True)



for i in range(1,12):
  print is_prime(i)

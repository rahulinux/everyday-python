#!/usr/bin/env python

def fib(n):
    # Time complexity : O(2n)
    if n <= 1:
        return 0
    else:
        return fib(n-1) + fib(n-2) 


def fib2(n):    
    # O(1) 
    a,b = 0,1
    for _ in range(n):
       a,b = b, a+b
    return a

def fib3(n):
    # O(n)
    f = [0,1]
    for i in range(2,n):
      f.append(f[i-1] + f[i-2])
    return f



for j in range(10):
    print fib2(j)

print fib3(10)
